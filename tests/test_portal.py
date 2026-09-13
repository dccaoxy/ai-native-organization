import json
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from organization.portal import server

class PortalTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.path=Path(self.tmp.name)/'portal.sqlite3';self.logs=[];self.start()
    def start(self):
        self.http=server(self.path,request_logger=self.logs.append);self.thread=threading.Thread(target=self.http.serve_forever,daemon=True);self.thread.start();self.url=self.http.origin
    def tearDown(self):
        self.http.shutdown();self.http.server_close();self.thread.join();self.tmp.cleanup()
    def req(self,path,data=None,cookie='',csrf='',origin=True):
        h={'Cookie':cookie,'X-CSRF-Token':csrf}
        if origin:h['Origin']=self.url
        if data is not None:h['Content-Type']='application/json'
        q=Request(self.url+path,data=json.dumps(data).encode() if data is not None else None,headers=h)
        try:
            with urlopen(q) as r:return r.status,json.load(r),r.headers.get('Set-Cookie','').split(';')[0]
        except HTTPError as e:
            with e:return e.code,json.load(e),''
    def account(self,name):
        body={'username':name,'name':name,'password':'synthetic-test-password'}
        self.assertEqual(self.req('/api/signup',body)[0],200)
        status,r,cookie=self.req('/api/login',{k:body[k] for k in ('username','password')});self.assertEqual(status,200)
        return r,cookie

    def test_health_and_redacted_structured_request_log(self):
        status,body,_=self.req('/health')
        self.assertEqual(status,200);self.assertEqual(body,{'status':'ok','service':'ai-native-test-portal'})
        self.assertEqual(set(self.logs[-1]),{'event','request_id','method','path','status','duration_ms','client_ip'})
        self.assertEqual(self.logs[-1]['path'],'/health');self.assertEqual(self.logs[-1]['status'],200)
        self.assertNotIn('Cookie',json.dumps(self.logs[-1]));self.assertNotIn('Authorization',json.dumps(self.logs[-1]))

    def test_trusted_proxy_client_address_is_validated_for_rate_limit(self):
        self.http.shutdown();self.http.server_close();self.thread.join()
        self.http=server(self.path,trusted_proxies=['127.0.0.1'],request_logger=self.logs.append);self.thread=threading.Thread(target=self.http.serve_forever,daemon=True);self.thread.start();self.url=self.http.origin
        body={'username':'proxyuser','name':'Proxy User','password':'synthetic-test-password'}
        headers={'Origin':self.url,'Content-Type':'application/json','X-Forwarded-For':'203.0.113.9'}
        with urlopen(Request(self.url+'/api/signup',data=json.dumps(body).encode(),headers=headers)) as response:self.assertEqual(response.status,200)
        with self.http.portal.store.connect() as db:self.assertEqual(db.execute("SELECT count FROM portal_limits WHERE key='signup/203.0.113.9'").fetchone()[0],1)
        headers['X-Forwarded-For']='not-an-ip'
        with self.assertRaises(HTTPError) as error:urlopen(Request(self.url+'/api/signup',data=json.dumps({**body,'username':'other'}).encode(),headers=headers))
        self.assertEqual(error.exception.code,400);error.exception.close()
    def test_login_identity_csrf_logout_and_persistence(self):
        r,c=self.account('alice');self.assertEqual(self.req('/api/state')[0],401)
        self.assertEqual(self.req('/api/agent',{'name':'test'},c)[0],403)
        self.assertEqual(self.req('/api/agent',{'name':'test'},c,r['csrf'],False)[0],403)
        self.http.shutdown();self.http.server_close();self.thread.join();self.start()
        self.assertEqual(self.req('/api/me',cookie=c)[1]['human'],r['human'])
        self.assertEqual(self.req('/api/logout',{},c,r['csrf'])[0],200)
        self.assertEqual(self.req('/api/me',cookie=c)[0],401)
    def test_password_hash_and_login_rejection(self):
        r,c=self.account('alice')
        self.assertEqual(self.req('/api/login',{'username':'alice','password':'wrong'})[0],401)
        with self.http.portal.store.connect() as db:
            row=db.execute('SELECT password FROM portal_accounts').fetchone();self.assertNotEqual(row[0],'synthetic-test-password')
        self.assertNotIn('synthetic-test-password',json.dumps(self.http.portal.store.events()))
    def test_foreign_agent_and_actor_spoof_rejected(self):
        a,ac=self.account('alice');b,bc=self.account('bob')
        status,agent,_=self.req('/api/agent',{'name':'test'},ac,a['csrf']);self.assertEqual(status,200)
        d={'command':'approve_agent','data':{'registration_id':agent['registration_id'],'hau_id':'anything','permissions':['claim'],'allowed_tasks':['T']},'idempotency_key':'one'}
        self.assertEqual(self.req('/api/commands',d,bc,b['csrf'])[0],403)
        d['actor']=a['human'];self.assertEqual(self.req('/api/commands',d,bc,b['csrf'])[0],400)
        self.assertEqual(self.req('/api/state',cookie=bc)[1]['state']['AgentRegistration'],{})
        self.assertNotIn(agent['token'],json.dumps(self.http.portal.store.events()))
    def test_no_operator_or_bootstrap_escape(self):
        a,c=self.account('alice')
        self.assertEqual(self.req('/control/state',cookie=c)[0],404)
        for command in ('register_human','bind_agent','sweep'):
            self.assertEqual(self.req('/api/commands',{'command':command,'data':{},'idempotency_key':command},c,a['csrf'])[0],403)
    def test_rate_limit_and_expired_session(self):
        a,c=self.account('alice')
        with self.http.portal.store.connect() as db:db.execute('UPDATE portal_sessions SET expires=0')
        self.assertEqual(self.req('/api/me',cookie=c)[0],401)
        for i in range(20):self.http.portal.limit('test')
        from organization.store import DomainError
        with self.assertRaises(DomainError):self.http.portal.limit('test')
    def test_command_idempotency(self):
        a,c=self.account('alice')
        d={'command':'activate_goal','data':{'id':'G','desired_change':'test','success_criteria':'trace','boundary':['read'],'goal_authority':a['human']},'idempotency_key':'goal'}
        self.assertEqual(self.req('/api/commands',d,c,a['csrf'])[0],200);n=len(self.http.portal.store.events())
        self.assertEqual(self.req('/api/commands',d,c,a['csrf'])[0],200);self.assertEqual(n,len(self.http.portal.store.events()))
    def test_access_update_immediate_without_rebinding_execution(self):
        from organization.agent_client import Client,ProtocolError
        a,c=self.account('alice');b,bc=self.account('bob')
        portal=self.http.portal
        def cmd(name,data,key):return portal.dispatch('/api/commands',a['human'],{'command':name,'data':data,'idempotency_key':key})
        cmd('activate_goal',{'id':'G','desired_change':'test','success_criteria':'trace','boundary':['read'],'goal_authority':a['human']},'g')
        cmd('create_task',{'id':'T','primary_goal':'G','expected_output':'test','acceptance_criteria':'trace','boundary':['read'],'execution_mode':'parallel','review_authority':b['human'],'acceptance_authority':a['human'],'selection_authority':a['human']},'t')
        cmd('publish',{'task_id':'T'},'pub')
        reg=portal.dispatch('/api/agent',a['human'],{'name':'client'})
        scope={'registration_id':reg['registration_id'],'permissions':['claim','ack','progress','submit'],'allowed_tasks':['T']}
        cmd('approve_agent',{**scope,'hau_id':'ignored'},'approval')
        agent=Client(self.url,reg['token']);me=agent.request('/v1/me')['registration']
        agent.command('claim',{'id':'E','task_id':'T','hau_id':me['hau_id']},'claim');agent.command('ack',{'execution_id':'E'},'ack')
        before=portal.store.state()['Execution']['E'];new={**scope,'permissions':['claim','ack']}
        cmd('update_agent_access',new,'change')
        self.assertEqual(portal.store.state()['Execution']['E'],before)
        self.assertEqual(agent.request('/v1/me')['registration']['permissions'],new['permissions'])
        with self.assertRaises(ProtocolError) as e:agent.command('progress',{'execution_id':'E','summary':'denied'},'progress')
        self.assertEqual(e.exception.status,403)
        with self.assertRaises(ProtocolError) as e:agent.command('update_agent_access',scope,'self-elevate')
        self.assertEqual(e.exception.status,403)
        from organization.store import DomainError
        with self.assertRaises(DomainError):portal.dispatch('/api/commands',b['human'],{'command':'update_agent_access','data':scope,'idempotency_key':'foreign'})
        with self.assertRaises(DomainError):cmd('update_agent_access',{**scope,'permissions':['accept']},'human-only')
        cmd('update_agent_access',{**scope,'permissions':[],'allowed_tasks':[]},'pause')
        self.assertEqual(agent.request('/v1/tasks')['tasks'],[])
        cmd('update_agent_access',scope,'restore')
        self.assertEqual(agent.request('/v1/me')['registration']['permissions'],scope['permissions'])
        self.assertEqual(portal.store.events()[-1]['type'],'AgentAccessUpdated')

    def test_connection_receipt_is_idempotent_and_persists(self):
        from organization.agent_client import Client,ProtocolError
        a,c=self.account('alice');reg=self.http.portal.dispatch('/api/agent',a['human'],{'name':'client'})
        agent=Client(self.url,reg['token']);body={'registration_id':reg['registration_id']}
        n=len(self.http.portal.store.events());receipt=agent.request('/v1/connect',body)
        self.assertEqual(receipt['registration_status'],'pending')
        self.assertEqual(agent.request('/v1/connect',body),receipt)
        self.assertEqual(len(self.http.portal.store.events()),n)
        with self.assertRaises(ProtocolError):agent.request('/v1/connect',{'registration_id':'another'})
        self.http.shutdown();self.http.server_close();self.thread.join();self.start()
        agent=Client(self.url,reg['token']);self.assertEqual(agent.request('/v1/connect',body),receipt)
        data=self.req('/api/state',cookie=c)[1];self.assertEqual(data['connections'][reg['registration_id']],receipt['connected_at'])
