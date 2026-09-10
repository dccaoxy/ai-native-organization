"""Standalone Agent protocol client; no imports of internal organization state."""
import argparse
import json
import os
from pathlib import Path
import secrets
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import uuid


class ProtocolError(RuntimeError):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Client:
    def __init__(self, url, token):
        parsed = urlsplit(url)
        if parsed.scheme != 'http' or parsed.hostname not in ('127.0.0.1','localhost') or parsed.username or parsed.password or parsed.path not in ('','/') or parsed.query or parsed.fragment:
            raise ValueError('This lab client only permits a direct loopback HTTP origin')
        self.url, self.token = url.rstrip('/'), token
        self.opener = build_opener(NoRedirect)

    def request(self, path, data=None):
        if not path.startswith('/') or path.startswith('//'):
            raise ValueError('Relative API path required')
        request = Request(self.url + path, data=json.dumps(data).encode() if data is not None else None,
                          headers={'Authorization':'Bearer ' + self.token, 'Content-Type':'application/json'})
        try:
            with self.opener.open(request, timeout=20) as response:
                return json.load(response)
        except HTTPError as exc:
            with exc:
                try:
                    message = json.load(exc).get('error','Protocol error')
                except (ValueError, AttributeError):
                    message = 'Protocol error'
            raise ProtocolError(exc.code, message) from None

    def command(self, command, data, key):
        return self.request('/v1/commands', {'command':command,'data':data,'idempotency_key':key})


def run_task(client, task_id, run_id, result=None, outcome='success'):
    reg = client.request('/v1/me')['registration']
    if reg['status'] != 'approved':
        return {'status':'WAITING_FOR_HUMAN', 'registration_id':reg['id']}
    execution_id = reg['id'] + '/' + run_id
    attempts = client.request('/v1/executions')['executions']
    existing = next((e for e in attempts if e['id'] == execution_id), None)
    if existing and existing['task_id'] != task_id:
        raise ValueError('run_id already belongs to another task')
    if existing and existing['return_id'] != 'none':
        return {'status':'RETURN_ALREADY_RECORDED','execution_id':execution_id}
    tasks = client.request('/v1/tasks')['tasks']
    if not existing and not any(t['id'] == task_id for t in tasks):
        raise ValueError('Task not available in approved scope')
    client.command('claim', {'id':execution_id,'task_id':task_id,'hau_id':reg['hau_id']}, run_id+'/claim')
    client.command('ack', {'execution_id':execution_id}, run_id+'/ack')
    client.command('progress', {'execution_id':execution_id,'summary':'Independent test Agent reached a public checkpoint'}, run_id+'/progress')
    if outcome == 'interrupted':
        client.command('agent_status', {'agent_id':reg['agent_id'],'runtime_status':'offline'}, run_id+'/offline')
        return {'status':'INTERRUPTION_RECORDED','execution_id':execution_id}
    if outcome == 'blocked':
        client.command('request_boundary', {'id':execution_id+'/boundary','execution_id':execution_id,'requested_scope':['read','draft'],'reason':'Synthetic test needs Human scope authorization'}, run_id+'/boundary')
        return {'status':'WAITING_FOR_BOUNDARY','execution_id':execution_id}
    result = result or {'result':'Synthetic deterministic Agent output','observed_terrain':'Isolated local HTTP lab',
                       'major_execution_facts':'Agent used authenticated claim, ACK and progress interfaces',
                       'reflection':'No real Human or business outcome is claimed'}
    required = {'result','observed_terrain','major_execution_facts','reflection'}
    if set(result) != required or not all(isinstance(v,str) and v.strip() for v in result.values()):
        raise ValueError('Formal Return requires exactly four nonempty text fields')
    client.command('fail' if outcome == 'failure' else 'submit', {'id':execution_id+'/return','execution_id':execution_id,**result}, run_id+'/return')
    return {'status':'FORMAL_RETURN_RECORDED','execution_id':execution_id,'outcome':outcome}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['register','status','run'])
    parser.add_argument('--url', default='http://127.0.0.1:8877')
    parser.add_argument('--identity-file', default='.autodev/test-agent.identity.json')
    parser.add_argument('--task')
    parser.add_argument('--run-id', default='attempt-1')
    parser.add_argument('--outcome', choices=['success','failure','blocked','interrupted'], default='success')
    parser.add_argument('--result-file')
    args = parser.parse_args()
    path = Path(args.identity_file)
    if args.action == 'register' and not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        identity = {'id':uuid.uuid4().hex,'token':secrets.token_urlsafe(32),'url':args.url}
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd,'w') as stream:
            json.dump(identity, stream)
    identity = json.loads(path.read_text())
    if identity['url'].rstrip('/') != args.url.rstrip('/'):
        raise ValueError('Identity belongs to another endpoint; do not forward credentials')
    client = Client(args.url, identity['token'])
    if args.action == 'register':
        result = client.request('/v1/agents/register', {'id':identity['id'],'name':'Independent synthetic test Agent',
                                 'version':'0.1','capabilities':['synthetic-test-return']})
        print(json.dumps({'registration_id':identity['id'],'status':result['registration']['status']}))
    elif args.action == 'status':
        print(json.dumps(client.request('/v1/me')))
    else:
        if not args.task:
            parser.error('--task is required for run')
        result = json.loads(Path(args.result_file).read_text(encoding='utf-8')) if args.result_file else None
        print(json.dumps(run_task(client, args.task, args.run_id, result, args.outcome)))


if __name__ == '__main__':
    main()
