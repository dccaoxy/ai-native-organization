"""Account-based shared test portal. No operator/control API is exposed.

Single process per SQLite database. Serve through a TLS proxy for remote use.
Accounts authenticate a test participant, not a verified real-world identity.
"""
import argparse
import hashlib
import hmac
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import re
import secrets
import time
from organization.agent_gateway import Gateway
from organization.core import Session, require
from organization.store import DomainError

HUMAN_COMMANDS = set('activate_goal create_task publish approve_agent update_agent_access revoke_agent agent_status resume decide_boundary review accept select annotate_return challenge_goal decide_goal_challenge propose_claim capture_evidence verify_claim assemble_route use_knowledge record_learning_outcome record_reproduction report_knowledge_issue revise_knowledge plan_revalidation revise_route complete_revalidation'.split())


class Portal:
    def __init__(self, path):
        self.gateway = Gateway(path, secrets.token_urlsafe(32))
        self.store = self.gateway.org.store
        self.lock = self.gateway.lock
        with self.store.connect() as db:
            db.executescript('''
            CREATE TABLE IF NOT EXISTS portal_accounts (username TEXT PRIMARY KEY, human TEXT UNIQUE NOT NULL, name TEXT NOT NULL, salt TEXT NOT NULL, password TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS portal_sessions (hash TEXT PRIMARY KEY, human TEXT NOT NULL, csrf TEXT NOT NULL, expires REAL NOT NULL);
            CREATE TABLE IF NOT EXISTS portal_connections (registration TEXT PRIMARY KEY, connected_at REAL NOT NULL);
            CREATE TABLE IF NOT EXISTS portal_agents (registration TEXT PRIMARY KEY, human TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS portal_limits (key TEXT PRIMARY KEY, count INTEGER NOT NULL, until REAL NOT NULL);
            ''')

    def limit(self, key, maximum=20):
        now=time.time()
        with self.store.connect() as db:
            db.execute('BEGIN IMMEDIATE')
            db.execute('DELETE FROM portal_limits WHERE until < ?', (now,))
            row=db.execute('SELECT count FROM portal_limits WHERE key=?',(key,)).fetchone()
            if row and row[0]>=maximum:raise DomainError('请求过于频繁，请稍后再试',429)
            db.execute('INSERT INTO portal_limits VALUES (?,1,?) ON CONFLICT(key) DO UPDATE SET count=count+1',(key,now+300))

    @staticmethod
    def password(value, salt):
        return hashlib.scrypt(value.encode(),salt=bytes.fromhex(salt),n=16384,r=8,p=1).hex()

    def ensure_human(self, human, name):
        def create(state):
            s=Session(state,human,self.store.clock())
            s.new('Human',human)
            s.emit('Human',{'id':human,'display_name':name,'kind':'human'},'HumanRegistered','authenticated test account; no real identity verification',human)
            return s.emitted
        self.store.transact(human,'portal_register',{'name':name},'portal/account/'+human,create)

    def signup(self, data, ip):
        require(data,['username','name','password'])
        self.limit('signup/'+ip,10)
        username=data['username'].strip().lower(); name=data['name'].strip(); password=data['password']
        if not re.fullmatch('[a-z0-9_.-]{3,40}',username) or not 1<=len(name)<=60 or not 12<=len(password)<=128:
            raise DomainError('账号需 3–40 位字母数字；姓名 1–60 字；密码 12–128 字')
        salt=secrets.token_hex(16); digest=self.password(password,salt); human='H-'+secrets.token_hex(12)
        with self.lock:
            with self.store.connect() as db:
                if db.execute('SELECT 1 FROM portal_accounts WHERE username=?',(username,)).fetchone():raise DomainError('账号已存在',409)
                db.execute('INSERT INTO portal_accounts VALUES (?,?,?,?,?)',(username,human,name,salt,digest))
            # Reserved account can finish the event on login after interruption.
            self.ensure_human(human,name)
        return {'registered':True}

    def login(self, data, ip):
        require(data,['username','password'])
        self.limit('login/'+ip)
        if not isinstance(data['password'],str) or len(data['password'])>128:raise DomainError('账号或密码错误',401)
        with self.store.connect() as db:row=db.execute('SELECT human,name,salt,password FROM portal_accounts WHERE username=?',(data['username'].strip().lower(),)).fetchone()
        actual=self.password(data['password'],row[2] if row else '00'*16)
        if not row or not hmac.compare_digest(actual,row[3]):raise DomainError('账号或密码错误',401)
        with self.lock:self.ensure_human(row[0],row[1])
        token=secrets.token_urlsafe(32);csrf=secrets.token_urlsafe(32)
        with self.store.connect() as db:
            db.execute('DELETE FROM portal_sessions WHERE expires < ?',(time.time(),))
            db.execute('INSERT INTO portal_sessions VALUES (?,?,?,?)',(Gateway.hash(token),row[0],csrf,time.time()+28800))
        return {'human':row[0],'csrf':csrf},token

    def session(self, token):
        with self.store.connect() as db:row=db.execute('SELECT human,csrf,expires FROM portal_sessions WHERE hash=?',(Gateway.hash(token),)).fetchone()
        if not row or row[2]<=time.time():raise DomainError('请登录',401)
        return row[0],row[1]

    def owned(self, human, registration):
        with self.store.connect() as db:row=db.execute('SELECT human FROM portal_agents WHERE registration=?',(registration,)).fetchone()
        if not row or row[0]!=human:raise DomainError('无权操作其他用户的 Agent',403)

    def dispatch(self, path, human, data):
        with self.lock:
            if path=='/api/state':
                state=self.store.state()
                with self.store.connect() as db:owned={r[0] for r in db.execute('SELECT registration FROM portal_agents WHERE human=?',(human,))}
                state['AgentRegistration']={k:v for k,v in state.get('AgentRegistration',{}).items() if k in owned}
                with self.store.connect() as db:connections={r[0]:r[1] for r in db.execute('SELECT registration,connected_at FROM portal_connections') if r[0] in owned}
                return {'state':state,'events':self.store.events(),'human':human,'connections':connections}
            if path=='/api/agent':
                require(data,['name'])
                if not isinstance(data['name'],str) or not 1<=len(data['name'].strip())<=80:raise DomainError('请填写 Agent 名称')
                rid=secrets.token_hex(16);token=secrets.token_urlsafe(32)
                self.gateway.register(token,{'id':rid,'name':data['name'].strip(),'version':'portal-v1','capabilities':['external-client']})
                with self.store.connect() as db:db.execute('INSERT INTO portal_agents VALUES (?,?)',(rid,human))
                return {'registration_id':rid,'token':token,'note':'凭据只显示一次；保存到 Agent 的连接配置中，批准前无执行权限'}
            if path=='/api/commands':
                require(data,['command','data','idempotency_key'])
                cmd=data['command'];payload=data['data']
                if cmd not in HUMAN_COMMANDS:raise DomainError('此操作不可从 Human 门户执行',403)
                if cmd in ('approve_agent','revoke_agent','update_agent_access'):
                    self.owned(human,payload.get('registration_id'))
                    if cmd=='approve_agent':payload={**payload,'hau_id':'U-'+human}
                result=self.gateway.org.execute(human,cmd,payload,'portal/'+human+'/'+data['idempotency_key'])
                return {'events':result['events']}
            raise DomainError('Not found',404)


def server(path,port=0,origin=None):
    portal=Portal(path)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args):pass
        def reply(self,status,value,cookie=None,mime='application/json; charset=utf-8'):
            raw=value if isinstance(value,bytes) else json.dumps(value,ensure_ascii=False).encode()
            self.send_response(status)
            for k,v in {'Content-Type':mime,'Content-Length':str(len(raw)),'Cache-Control':'no-store','X-Content-Type-Options':'nosniff','Referrer-Policy':'no-referrer','Content-Security-Policy':"default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'"}.items():self.send_header(k,v)
            if cookie is not None:self.send_header('Set-Cookie','portal_session='+cookie+'; Path=/; HttpOnly; SameSite=Strict'+('; Secure' if self.server.origin.startswith('https:') else '')+('; Max-Age=0' if not cookie else '; Max-Age=28800'))
            self.end_headers();self.wfile.write(raw)
        def handle_request(self):
            try:
                if self.headers.get('Host')!=self.server.origin.split('://',1)[1]:raise DomainError('Host denied',403)
                if self.headers.get('Origin') and self.headers['Origin']!=self.server.origin:raise DomainError('Origin denied',403)
                assets={'/agent-guide.txt':('portal_web/agent-guide.txt','text/plain'),'/':('portal_web/index.html','text/html'),'/portal.js':('portal_web/portal.js','text/javascript'),'/human.css':('portal_web/style.css','text/css'),'/learning.js':('human_web/learning.js','text/javascript'),'/flow.js':('portal_web/flow.js','text/javascript'),'/human.js':('portal_web/human.js','text/javascript')}
                if self.command=='GET' and self.path in assets:
                    file,mime=assets[self.path];return self.reply(200,(Path(__file__).parent/file).read_bytes(),mime=mime+'; charset=utf-8')
                data=None
                if self.command=='POST':
                    if 'application/json' not in self.headers.get('Content-Type',''):raise DomainError('JSON required',415)
                    length=int(self.headers.get('Content-Length','0'))
                    if not 0<length<=65536:raise DomainError('Request too large',413)
                    self.connection.settimeout(10)
                    data=json.loads(self.rfile.read(length))
                if self.path.startswith('/v1/'):
                    if self.path=='/v1/agents/register':raise DomainError('请由所属 Human 在网页创建 Agent 接入凭据',403)
                    auth=self.headers.get('Authorization','')
                    if not auth.startswith('Bearer '):raise DomainError('Agent credential required',401)
                    if self.path=='/v1/connect' and self.command=='POST':
                        require(data,['registration_id'])
                        with portal.lock:
                            reg,_=portal.gateway.authenticate(auth[7:],approved=False)
                            if reg['id']!=data['registration_id']:raise DomainError('Registration mismatch',403)
                            with portal.store.connect() as db:
                                if not db.execute('SELECT 1 FROM portal_agents WHERE registration=?',(reg['id'],)).fetchone():raise DomainError('Portal registration required',403)
                                db.execute('INSERT OR IGNORE INTO portal_connections VALUES (?,?)',(reg['id'],time.time()))
                                first=db.execute('SELECT connected_at FROM portal_connections WHERE registration=?',(reg['id'],)).fetchone()[0]
                            return self.reply(200,{'connected':True,'connected_at':first,'registration_status':reg['status']})
                    return self.reply(200,portal.gateway.dispatch(self.command,self.path,auth[7:],data))
                if self.command=='POST' and self.headers.get('Origin')!=self.server.origin:raise DomainError('Same-origin browser required',403)
                if self.path=='/api/signup' and self.command=='POST':return self.reply(200,portal.signup(data,self.client_address[0]))
                if self.path=='/api/login' and self.command=='POST':
                    result,token=portal.login(data,self.client_address[0]);return self.reply(200,result,token)
                cookie=SimpleCookie();cookie.load(self.headers.get('Cookie',''));token=cookie['portal_session'].value if 'portal_session' in cookie else ''
                human,csrf=portal.session(token)
                if self.command=='POST' and not hmac.compare_digest(self.headers.get('X-CSRF-Token',''),csrf):raise DomainError('CSRF denied',403)
                if self.path=='/api/me' and self.command=='GET':return self.reply(200,{'human':human,'csrf':csrf})
                if self.path=='/api/logout' and self.command=='POST':
                    with portal.store.connect() as db:db.execute('DELETE FROM portal_sessions WHERE hash=?',(Gateway.hash(token),))
                    return self.reply(200,{'logged_out':True},'')
                if (self.path=='/api/state' and self.command=='GET') or (self.path in ('/api/agent','/api/commands') and self.command=='POST'):
                    return self.reply(200,portal.dispatch(self.path,human,data))
                raise DomainError('Not found',404)
            except DomainError as e:self.reply(e.status,{'error':str(e)})
            except (ValueError,TypeError,KeyError,AttributeError):self.reply(400,{'error':'请求格式无效'})
        do_GET=handle_request
        do_POST=handle_request
    http=ThreadingHTTPServer(('127.0.0.1',port),Handler)
    http.portal=portal;http.origin=origin or f'http://127.0.0.1:{http.server_port}'
    if not re.fullmatch(r'https?://[a-zA-Z0-9.:-]+',http.origin):http.server_close();raise ValueError('Explicit origin required without path')
    return http


def main():
    p=argparse.ArgumentParser();p.add_argument('--db',default='.autodev/portal/portal.sqlite3');p.add_argument('--port',type=int,default=8876);p.add_argument('--origin');a=p.parse_args()
    http=server(a.db,a.port,a.origin);print('Account test portal: '+http.origin,flush=True)
    try:http.serve_forever()
    except KeyboardInterrupt:pass
    finally:http.server_close()


if __name__=='__main__':main()
