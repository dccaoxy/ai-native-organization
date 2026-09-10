import json
import secrets
import tempfile
import threading
import unittest
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from organization.agent_gateway import server


class HumanWebTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.key=secrets.token_urlsafe(32)
        self.http=server(self.tmp.name+'/lab.db',self.key)
        self.thread=threading.Thread(target=self.http.serve_forever,daemon=True)
        self.thread.start()
        self.url=f'http://127.0.0.1:{self.http.server_port}'

    def tearDown(self):
        self.http.shutdown();self.http.server_close();self.thread.join();self.tmp.cleanup()

    def request(self,path,headers=None,data=None):
        try:
            with urlopen(Request(self.url+path,headers=headers or {},data=data)) as r:
                return r.status,r.headers,r.read().decode()
        except HTTPError as e:
            with e:return e.code,e.headers,e.read().decode()

    def test_public_shell_never_discloses_control_key(self):
        for path in ['/','/human.js','/human.css']:
            status,headers,text=self.request(path)
            self.assertEqual(status,200)
            self.assertNotIn(self.key,text)
            self.assertIn("frame-ancestors 'none'",headers['Content-Security-Policy'])
        self.assertEqual(self.request('/control/state')[0],401)
        self.assertEqual(self.request('/control/events')[0],401)
        self.assertNotEqual(self.request('/../agent-operator.key')[0],200)

    def test_same_origin_control_and_cross_origin_denial(self):
        auth={'Authorization':'Bearer '+self.key,'Origin':self.url,'Content-Type':'application/json'}
        body=json.dumps({'actor':'SIMULATOR','command':'register_human','data':{'id':'H','display_name':'Synthetic Human'},'idempotency_key':'web-test'}).encode()
        self.assertEqual(self.request('/control/commands',auth,body)[0],200)
        self.assertEqual(self.request('/control/commands',dict(auth,Origin='https://other.invalid'),body)[0],403)
        self.assertEqual(self.request('/control/state',dict(auth,Host='other.invalid'))[0],403)
        status,_,text=self.request('/control/events',auth)
        self.assertEqual(status,200)
        self.assertEqual(len(json.loads(text)['events']),1)
        self.assertNotIn(self.key,text)

    def test_agent_cannot_use_browser_control(self):
        agent=secrets.token_urlsafe(32)
        headers={'Authorization':'Bearer '+agent,'Content-Type':'application/json'}
        body=json.dumps({'id':'agent-web-test','name':'Test','version':'1','capabilities':[]}).encode()
        self.assertEqual(self.request('/v1/agents/register',headers,body)[0],200)
        browser=dict(headers,Origin=self.url)
        self.assertEqual(self.request('/control/state',browser)[0],401)
        self.assertEqual(self.request('/control/commands',browser,b'{}')[0],401)
        self.assertEqual(self.request('/v1/me',browser)[0],403)
