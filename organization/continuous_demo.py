"""Continuous synthetic browser/Agent acceptance, starting without execution or knowledge.
Restart IPC exists only in this temporary test orchestrator, never in the gateway.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
import threading
import time
from tests.test_core import CoreTests
from organization.agent_gateway import server
from organization.store import Store


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--node', default='node')
    parser.add_argument('--modules', default='')
    parser.add_argument('--output', default='development/autodev/continuous-demo')
    args = parser.parse_args()
    fixture = CoreTests(); fixture.setUp()
    http = None; child = None
    try:
        fixture.task()
        fixture.call('create_task', {'id':'T2','primary_goal':'G1','expected_output':'Synthetic reuse','acceptance_criteria':'Traceable bounded reuse','boundary':['read'],'execution_mode':'parallel','review_authority':'H2','acceptance_authority':'H1','selection_authority':'H3'})
        fixture.call('publish', {'task_id':'T2'})
        assert not fixture.org.store.state().get('Execution')
        assert not fixture.org.store.state().get('KnowledgeRevision')
        initial_events = len(fixture.org.store.events())
        ipc = Path(fixture.tmp.name)
        key = secrets.token_urlsafe(32)
        http = server(fixture.org.store.path, key)
        port = http.server_port
        thread = threading.Thread(target=http.serve_forever, daemon=True); thread.start()
        out = Path(args.output).resolve(); out.mkdir(parents=True, exist_ok=True)
        env = dict(os.environ, LAB_URL=f'http://127.0.0.1:{port}', LAB_KEY=key,
                   LAB_IDENTITY=str(ipc/'reuse.json'), LAB_SECOND_IDENTITY=str(ipc/'revalidation.json'),
                   LAB_PYTHON=sys.executable, LAB_OUTPUT=str(out), LAB_IPC=str(ipc))
        if args.modules: env['NODE_PATH'] = args.modules
        child = subprocess.Popen([args.node, 'organization/continuous_web_test.cjs'], env=env)
        deadline = time.monotonic() + 240
        restarts = []
        while child.poll() is None:
            if time.monotonic() > deadline: raise TimeoutError('Continuous browser acceptance exceeded 240 seconds')
            request = ipc/'restart.request'
            if request.exists():
                number = int(request.read_text()); request.unlink()
                before = fixture.org.store.events()
                http.shutdown(); http.server_close(); thread.join()
                http = server(fixture.org.store.path, key, port=port)
                thread = threading.Thread(target=http.serve_forever, daemon=True); thread.start()
                assert before == http.gateway.org.store.events()
                restarts.append({'number':number,'events_before':len(before),'events_after':len(http.gateway.org.store.events())})
                (ipc/f'restart.{number}.done').write_text('ready')
            time.sleep(.05)
        if child.returncode: raise RuntimeError('Continuous browser acceptance failed')
        state = fixture.org.store.state(); events = fixture.org.store.events()
        assert len(restarts) == 2 and Store.replay(events) == state
        plan = next(iter(state['RevalidationPlan'].values()))
        old = plan['knowledge_id']
        assert plan['status'] == 'passed'
        assert state['KnowledgeRevision'][old]['status'] == 'superseded'
        assert state['CapabilityRoute']['route/R1']['status'] == 'stale'
        assert state['CapabilityRoute'][plan['replacement_package']]['status'] == 'reproduced'
        assert len(state['AgentRegistration']) == 4
        assert all(e['accountable_owner'] in state['Human'] for e in state['Execution'].values())
        payload = json.dumps({'state':state,'events':events}, ensure_ascii=False, indent=2)
        for secret in [key]+[json.loads(p.read_text())['token'] for p in ipc.glob('*.json')]:
            assert secret not in payload
        (out/'evidence.json').write_text(payload, encoding='utf-8')
        report = {'verdict':'PASS','synthetic':True,'real_human_participants':0,'model_called':False,
                  'initial_execution_count':0,'initial_knowledge_count':0,'initial_event_count':initial_events,
                  'event_count':len(events),'registered_agents':4,'independent_agent_processes':True,
                  'real_browser':True,'browser':os.environ.get('LAB_BROWSER_CHANNEL','Chromium'),
                  'restarts':restarts,'restart_idempotency':True,'agent_interruption_recovery':True,
                  'foreign_human_recovery_disabled':True,'event_replay_matches':True,
                  'new_task_revalidation':'passed','old_knowledge':'superseded','old_package':'stale',
                  'source_hashes':{p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
                                   for root in ('organization','specs') for p in Path(root).rglob('*')
                                   if p.is_file() and p.suffix in ('.py','.js','.css','.html','.cjs','.json')}}
        (out/'report.json').write_text(json.dumps(report,indent=2), encoding='utf-8')
        print(f'PASS: continuous registration -> execution -> knowledge -> failure -> revalidation; {len(events)} events, 2 server restarts')
    finally:
        if child and child.poll() is None: child.kill(); child.wait()
        if http: http.shutdown(); http.server_close(); thread.join()
        fixture.tearDown()


if __name__ == '__main__': main()
