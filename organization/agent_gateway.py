"""Loopback-only, single-process authenticated Agent lab, on its own database.

The Human browser shell requires an independently supplied operator key. That credential
represents test control authority, not production Human identity authentication.
"""
import argparse
import hashlib
import hmac
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import secrets
import threading
from organization.core import Organization, require
from organization.identity import DELEGABLE
from organization.store import DomainError


class Gateway:
    def __init__(self, path, operator_token, clock=None):
        if len(operator_token) < 32:
            raise ValueError('Strong independent operator credential required')
        self.org = Organization(path, clock=clock)
        self.operator_hash = self.hash(operator_token)
        self.lock = threading.RLock()
        with self.org.store.connect() as db:
            db.execute('CREATE TABLE IF NOT EXISTS agent_credentials (registration_id TEXT PRIMARY KEY, token_hash TEXT UNIQUE NOT NULL)')

    @staticmethod
    def hash(value):
        return hashlib.sha256(value.encode()).hexdigest()

    def operator(self, token):
        return hmac.compare_digest(self.hash(token), self.operator_hash)

    def register(self, token, body):
        require(body, ['id','name','version','capabilities'])
        if not re.fullmatch(r'[A-Za-z0-9_-]{8,64}', body['id']):
            raise DomainError('Registration id must be 8..64 safe characters')
        if not re.fullmatch(r'[A-Za-z0-9_-]{43,200}', token) or self.operator(token):
            raise DomainError('Fresh high-entropy Agent bearer credential required', 400)
        sha = self.hash(token)
        # Credential reservation precedes the formal event. If interrupted,
        # the same id/token can retry; no registration event means no authority.
        with self.org.store.connect() as db:
            row = db.execute('SELECT token_hash FROM agent_credentials WHERE registration_id=?', (body['id'],)).fetchone()
            if row and not hmac.compare_digest(row[0], sha):
                raise DomainError('Registration credential mismatch', 403)
            other = db.execute('SELECT registration_id FROM agent_credentials WHERE token_hash=?', (sha,)).fetchone()
            if other and other[0] != body['id']:
                raise DomainError('Credential already bound', 409)
            db.execute('INSERT OR IGNORE INTO agent_credentials VALUES (?,?)', (body['id'], sha))
        result = self.org.execute('AGENT_GATEWAY', 'register_agent', body, 'enroll/' + body['id'])
        reg = self.org.store.state()['AgentRegistration'][body['id']]
        return {'registration':reg, 'events':result['events']}

    def authenticate(self, token, approved=True):
        with self.org.store.connect() as db:
            row = db.execute('SELECT registration_id FROM agent_credentials WHERE token_hash=?', (self.hash(token),)).fetchone()
        if not row:
            raise DomainError('Invalid Agent credential', 401)
        state = self.org.store.state()
        reg = state.get('AgentRegistration', {}).get(row[0])
        if not reg:
            raise DomainError('Registration incomplete; retry registration', 403)
        if reg['status'] == 'revoked' or (approved and reg['status'] != 'approved'):
            raise DomainError('Agent awaiting approval or revoked', 403)
        if reg['status'] == 'approved':
            agent = state['RepresentativeAgent'][reg['agent_id']]
            if not agent['active'] or state['HAU'][reg['hau_id']]['agent_id'] != agent['id']:
                raise DomainError('Agent binding has been replaced', 403)
        return reg, state

    def dispatch(self, method, path, token, body):
        # Revocation, authentication and command execution serialize together.
        # Multiple server processes sharing this database are unsupported.
        with self.lock:
            if path.startswith('/control/'):
                if not self.operator(token):
                    raise DomainError('Operator credential required', 401)
                if path == '/control/events' and method == 'GET':
                    return {'events':self.org.store.events()}
                if path == '/control/state' and method == 'GET':
                    return {'state':self.org.store.state()}
                if path == '/control/commands' and method == 'POST':
                    require(body, ['actor','command','data','idempotency_key'])
                    return self.org.execute(**body)
                raise DomainError('Not found', 404)
            if method == 'POST' and path == '/v1/agents/register':
                return self.register(token, body)
            reg, state = self.authenticate(token, approved=path != '/v1/me')
            if method == 'GET' and path == '/v1/me':
                return {'registration':reg}
            if method == 'GET' and path == '/v1/tasks':
                tasks = [t for t in state.get('Task', {}).values() if t['id'] in reg['allowed_tasks'] and t['status'] == 'published' and state['Goal'][t['primary_goal']]['status'] == 'active']
                return {'tasks':tasks}
            if method == 'GET' and path == '/v1/executions':
                return {'executions':[e for e in state.get('Execution', {}).values() if e['hau_id'] == reg['hau_id'] and e['task_id'] in reg['allowed_tasks']]}
            if method != 'POST' or path != '/v1/commands':
                raise DomainError('Not found', 404)
            require(body, ['command','data','idempotency_key'])
            command, data = body['command'], body['data']
            if not isinstance(data, dict):
                raise DomainError('Command data must be an object')
            if command not in DELEGABLE | {'agent_status'}:
                raise DomainError('Human-only or unknown command', 403)
            if command != 'agent_status' and command not in reg['permissions']:
                raise DomainError('Command not delegated', 403)
            if command == 'claim':
                if data.get('hau_id') != reg['hau_id'] or data.get('task_id') not in reg['allowed_tasks']:
                    raise DomainError('Claim outside approved HAU/task scope', 403)
            elif command == 'agent_status':
                if data.get('agent_id') != reg['agent_id']:
                    raise DomainError('Cannot control another Agent runtime', 403)
            elif command == 'challenge_goal':
                goals = {state['Task'][t]['primary_goal'] for t in reg['allowed_tasks']}
                if data.get('goal_id') not in goals:
                    raise DomainError('Goal outside approved task scope', 403)
            else:
                execution = state.get('Execution', {}).get(data.get('execution_id'))
                if not execution or execution['hau_id'] != reg['hau_id'] or execution['task_id'] not in reg['allowed_tasks']:
                    raise DomainError('Execution outside approved scope', 403)
            result = self.org.execute(reg['agent_id'], command, data, 'agent/' + reg['id'] + '/' + body['idempotency_key'])
            return {'events':result['events']}  # Never disclose unrelated global state.


def server(path, operator_token, port=0, clock=None):
    gateway = Gateway(path, operator_token, clock)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *args):
            pass

        def respond(self, status, result):
            data = json.dumps({'simulation':True, **result}, ensure_ascii=False).encode()
            self.send_response(status)
            self.send_header('Content-Type','application/json; charset=utf-8')
            self.send_header('Content-Length',str(len(data)))
            self.send_header('Cache-Control','no-store')
            self.send_header('X-Content-Type-Options','nosniff')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'")
            self.end_headers()
            self.wfile.write(data)

        def handle_request(self):
            try:
                if self.headers.get('Host') not in (f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}'):
                    raise DomainError('Only direct loopback clients permitted', 403)
                origin = self.headers.get('Origin')
                # Only the control API accepts same-origin browser requests.
                if origin and (not self.path.startswith('/control/') or origin != 'http://' + self.headers.get('Host','')):
                    raise DomainError('Cross-origin request denied', 403)
                assets = {'/':'index.html', '/human.js':'human.js', '/human.css':'human.css'}
                if self.command == 'GET' and self.path in assets:
                    filename = assets[self.path]
                    payload = (Path(__file__).parent / 'human_web' / filename).read_bytes()
                    self.send_response(200)
                    self.send_header('Content-Type', {'html':'text/html; charset=utf-8','js':'text/javascript; charset=utf-8','css':'text/css; charset=utf-8'}[filename.rsplit('.',1)[1]])
                    self.send_header('Content-Length',str(len(payload)))
                    self.send_header('Cache-Control','no-store')
                    self.send_header('X-Content-Type-Options','nosniff')
                    self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'")
                    self.end_headers()
                    self.wfile.write(payload)
                    return
                auth = self.headers.get('Authorization','')
                if not auth.startswith('Bearer '):
                    raise DomainError('Bearer credential required', 401)
                body = None
                if self.command == 'POST':
                    length = int(self.headers.get('Content-Length','0'))
                    if not 0 < length <= 65536:
                        raise DomainError('Body must be 1..65536 bytes', 413)
                    body = json.loads(self.rfile.read(length))
                result = gateway.dispatch(self.command, self.path, auth[7:], body)
                self.respond(200, result)
            except DomainError as exc:
                self.respond(exc.status, {'error':str(exc)})
            except (ValueError, TypeError, KeyError):
                self.respond(400, {'error':'Invalid request shape or value'})

        do_GET = handle_request
        do_POST = handle_request
    httpd = ThreadingHTTPServer(('127.0.0.1',port),Handler)
    httpd.gateway = gateway
    return httpd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', default='.autodev/agent-lab.sqlite3')
    parser.add_argument('--operator-key-file', default='.autodev/agent-operator.key')
    parser.add_argument('--port', type=int, default=8877)
    args = parser.parse_args()
    key = Path(args.operator_key_file)
    key.parent.mkdir(parents=True, exist_ok=True)
    if not key.exists():
        import os
        fd = os.open(key, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd,'w') as stream:
            stream.write(secrets.token_urlsafe(32))
    httpd = server(args.db, key.read_text().strip(), args.port)
    print(f'Isolated Agent lab: http://127.0.0.1:{httpd.server_port}; operator credential in local key file, never served over HTTP', flush=True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == '__main__':
    main()
