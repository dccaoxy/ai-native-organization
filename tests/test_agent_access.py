import json
from pathlib import Path
import secrets
import subprocess
import sys
import tempfile
import threading
import unittest
from organization.agent_gateway import server
from organization.agent_client import Client, ProtocolError, run_task
from organization.identity import DELEGABLE
from organization.store import Store


class AgentAccessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.path = self.root/'agent.sqlite3'
        self.operator = secrets.token_urlsafe(32)
        self.clock = [100.0]
        self.http = server(self.path, self.operator, clock=lambda:self.clock[0])
        self.thread = threading.Thread(target=self.http.serve_forever, daemon=True)
        self.thread.start()
        self.url = f'http://127.0.0.1:{self.http.server_port}'
        self.control = Client(self.url, self.operator)
        for i in range(2):
            self.op('SIMULATOR','register_human',{'id':f'H{i}','display_name':f'Synthetic Human {i}'},f'h{i}')
        self.op('H0','activate_goal',{'id':'G','desired_change':'Exercise independent Agent access','success_criteria':'Formal auditable Return','boundary':['read','draft'],'goal_authority':'H0'},'goal')
        for tid in ('T','OTHER'):
            self.op('H0','create_task',{'id':tid,'primary_goal':'G','expected_output':'A concise synthetic test recommendation','acceptance_criteria':'Four-field formal Return grounded in synthetic context','boundary':['read'],'execution_mode':'parallel','review_authority':'H1','acceptance_authority':'H0','selection_authority':'H1'},'task-'+tid)
            self.op('H0','publish',{'task_id':tid},'publish-'+tid)
        self.token = secrets.token_urlsafe(32)
        self.agent = Client(self.url, self.token)
        self.registration = {'id':'test-agent-001','name':'Fixture Agent','version':'1','capabilities':['test-return']}

    def tearDown(self):
        self.http.shutdown()
        self.http.server_close()
        self.thread.join()
        self.temp.cleanup()

    def op(self, actor, command, data, key):
        return self.control.request('/control/commands',{'actor':actor,'command':command,'data':data,'idempotency_key':key})

    def enroll(self, permissions=None):
        self.agent.request('/v1/agents/register', self.registration)
        self.op('H0','approve_agent',{'registration_id':self.registration['id'],'hau_id':'U0',
                'permissions':sorted(DELEGABLE) if permissions is None else permissions,'allowed_tasks':['T']},'approve')

    def assert_denied(self, status, fn):
        with self.assertRaises(ProtocolError) as caught:
            fn()
        self.assertEqual(caught.exception.status, status)

    def test_registration_is_pending_and_retry_does_not_duplicate_events(self):
        self.agent.request('/v1/agents/register',self.registration)
        count = len(self.http.gateway.org.store.events())
        self.agent.request('/v1/agents/register',self.registration)
        self.assertEqual(len(self.http.gateway.org.store.events()),count)
        self.assertEqual(self.agent.request('/v1/me')['registration']['status'],'pending')
        self.assert_denied(403, lambda:self.agent.request('/v1/tasks'))
        stranger = Client(self.url,secrets.token_urlsafe(32))
        self.assert_denied(403,lambda:stranger.request('/v1/agents/register',self.registration))

    def test_identity_spoof_and_human_authority_paths_rejected(self):
        self.enroll()
        before = self.http.gateway.org.store.events()
        self.assert_denied(401,lambda:self.agent.request('/control/state'))
        self.assert_denied(400,lambda:self.agent.request('/v1/commands',{'actor':'H0','command':'sweep','data':{},'idempotency_key':'spoof'}))
        for cmd in ('approve_agent','bind_agent','accept','select','decide_boundary','decide_goal_challenge'):
            self.assert_denied(403,lambda:self.agent.command(cmd,{},'forbidden-'+cmd))
        self.assertEqual(self.http.gateway.org.store.events(),before)

    def test_task_hau_scope_and_filtered_queries(self):
        self.enroll()
        self.assertEqual([t['id'] for t in self.agent.request('/v1/tasks')['tasks']],['T'])
        for tid,hau in [('OTHER','U0'),('T','U1')]:
            self.assert_denied(403,lambda:self.agent.command('claim',{'id':'bad','task_id':tid,'hau_id':hau},'bad'))
        result = self.agent.command('claim',{'id':'E','task_id':'T','hau_id':'U0'},'claim')
        self.assertNotIn('state',result)
        self.assertEqual(result['events'][0]['accountable_owner'],'H0')

    def test_failure_and_boundary_cannot_self_approve(self):
        self.enroll()
        run_task(self.agent,'T','failed',outcome='failure')
        run_task(self.agent,'T','blocked',outcome='blocked')
        eid = self.registration['id']+'/blocked'
        self.assert_denied(403,lambda:self.agent.command('resume',{'execution_id':eid,'summary':'Unauthorized extension'},'resume'))
        self.op('H0','decide_boundary',{'request_id':eid+'/boundary','decision':'approved'},'extend')
        self.agent.command('resume',{'execution_id':eid,'summary':'Authorized continuation'},'resume-ok')
        state = self.control.request('/control/state')['state']
        self.assertEqual(state['Execution'][eid]['runtime_boundary'],['read','draft'])
        self.assertEqual(state['Return'][self.registration['id']+'/failed/return']['outcome'],'failure')

    def test_revoke_interrupts_work_and_invalidates_token(self):
        self.enroll()
        self.agent.command('claim',{'id':'E','task_id':'T','hau_id':'U0'},'claim')
        self.agent.command('ack',{'execution_id':'E'},'ack')
        self.op('H0','revoke_agent',{'registration_id':self.registration['id']},'revoke')
        self.assert_denied(403,lambda:self.agent.request('/v1/tasks'))
        state=self.control.request('/control/state')['state']
        self.assertEqual(state['Execution']['E']['status'],'interrupted')
        self.assertEqual(state['Execution']['E']['accountable_owner'],'H0')

    def test_silent_failure_timeout_and_human_recovery(self):
        self.enroll()
        self.agent.command('claim',{'id':'silent','task_id':'T','hau_id':'U0'},'claim')
        self.clock[0] += 301
        self.op('SIMULATOR','sweep',{},'timeout')
        self.assertEqual(self.control.request('/control/state')['state']['Execution']['silent']['status'],'interrupted')
        self.op('H0','resume',{'execution_id':'silent','summary':'Synthetic Human takes over'},'takeover')
        self.assertEqual(self.control.request('/control/state')['state']['Execution']['silent']['status'],'running')

    def test_separate_process_client_registers_runs_and_replays(self):
        path=self.root/'independent.identity.json'
        def cli(*args):
            command=[sys.executable,'-m','organization.agent_client',*args,'--url',self.url,'--identity-file',str(path)]
            result=subprocess.run(command,capture_output=True,text=True,check=True,timeout=30)
            return json.loads(result.stdout)
        registration=cli('register')
        self.op('H0','approve_agent',{'registration_id':registration['registration_id'],'hau_id':'U0','permissions':sorted(DELEGABLE),'allowed_tasks':['T']},'approve-cli')
        result=cli('run','--task','T','--run-id','independent')
        self.assertEqual(result['status'],'FORMAL_RETURN_RECORDED')
        count=len(self.http.gateway.org.store.events())
        self.assertEqual(cli('run','--task','T','--run-id','independent')['status'],'RETURN_ALREADY_RECORDED')
        self.assertEqual(len(self.http.gateway.org.store.events()),count)
        state=self.control.request('/control/state')['state']
        self.assertEqual(Store(self.path).state(),state)
        rid=result['execution_id']+'/return'
        self.op('H1','review',{'id':'V','return_id':rid,'credible':True,'evidence':'Inspected independent client synthetic Return'},'review')
        self.op('H0','accept',{'id':'C','return_id':rid,'review_id':'V','accepted':True,'rationale':'Synthetic acceptance'},'accept')
        self.op('H1','select',{'id':'SEL','return_id':rid,'task_id':'T','rationale':'Explicit synthetic selection'},'select')
        self.assertEqual(self.control.request('/control/state')['state']['Task']['T']['status'],'closed')

    def test_credentials_not_in_events_and_legacy_ui_cannot_open_lab(self):
        self.enroll()
        events=json.dumps(self.http.gateway.org.store.events())
        self.assertNotIn(self.token,events)
        self.assertNotIn(self.operator,events)
        from organization.server import server as legacy
        with self.assertRaises(ValueError):
            legacy(self.path)
        from organization.agent_gateway import Gateway
        reopened=Gateway(self.path,self.operator)
        self.assertEqual(reopened.authenticate(self.token)[0]['status'],'approved')

    def test_undelegated_command_rejected(self):
        self.enroll(['claim'])
        self.agent.command('claim',{'id':'E','task_id':'T','hau_id':'U0'},'claim')
        self.assert_denied(403,lambda:self.agent.command('ack',{'execution_id':'E'},'ack'))

    def test_replacement_binding_denies_old_credential(self):
        self.enroll()
        replacement=Client(self.url,secrets.token_urlsafe(32))
        replacement.request('/v1/agents/register',dict(self.registration,id='test-agent-002'))
        self.op('H0','approve_agent',{'registration_id':'test-agent-002','hau_id':'U0','permissions':['claim'],'allowed_tasks':['T']},'replacement')
        self.assert_denied(403,lambda:self.agent.request('/v1/tasks'))
        self.assertEqual(replacement.request('/v1/me')['registration']['agent_id'],'AG-test-agent-002')

    def test_bad_data_and_missing_credential_do_not_change_state(self):
        self.enroll()
        before=self.http.gateway.org.store.events()
        self.assert_denied(401,lambda:Client(self.url,'invalid').request('/v1/tasks'))
        self.assert_denied(400,lambda:self.agent.command('claim',[],'invalid'))
        self.assertEqual(self.http.gateway.org.store.events(),before)


if __name__ == '__main__':
    unittest.main()
