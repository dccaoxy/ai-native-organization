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
        self.tmp=tempfile.TemporaryDirectory();self.path=Path(self.tmp.name)/'portal.sqlite3';self.start()
    def start(self):
        self.http=server(self.path);self.thread=threading.Thread(target=self.http.serve_forever,daemon=True);self.thread.start();self.url=self.http.origin
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
