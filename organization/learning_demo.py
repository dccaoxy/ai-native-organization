"""Explicit synthetic M03 fixture, browser operations and separate Agent process."""
import argparse,json,os,secrets,subprocess,sys,threading,hashlib
from pathlib import Path
from tests.test_learning import LearningTests
from organization.agent_gateway import server
from organization.agent_client import Client


def main():
    p=argparse.ArgumentParser();p.add_argument('--node',default='node');p.add_argument('--modules',default='');p.add_argument('--output',default='development/autodev/learning-demo');a=p.parse_args()
    fixture=LearningTests();fixture.setUp();http=None
    try:
        fixture.sources();key=secrets.token_urlsafe(32)
        http=server(fixture.org.store.path,key);thread=threading.Thread(target=http.serve_forever,daemon=True);thread.start()
        url=f'http://127.0.0.1:{http.server_port}';identity=Path(fixture.tmp.name)/'agent.json'
        subprocess.run([sys.executable,'-m','organization.agent_client','register','--url',url,'--identity-file',str(identity)],check=True,capture_output=True)
        rid=json.loads(identity.read_text())['id']
        Client(url,key).request('/control/commands',{'actor':'H3','command':'approve_agent','data':{'registration_id':rid,'hau_id':'U3','permissions':['claim','ack','submit','use_knowledge'],'allowed_tasks':['T2']},'idempotency_key':'demo-approval'})
        out=Path(a.output).resolve();out.mkdir(parents=True,exist_ok=True)
        env=dict(os.environ,LAB_URL=url,LAB_KEY=key,LAB_IDENTITY=str(identity),LAB_PYTHON=sys.executable,LAB_OUTPUT=str(out))
        if a.modules:env['NODE_PATH']=a.modules
        subprocess.run([a.node,'organization/learning_web_test.cjs'],env=env,check=True,timeout=150)
        state=fixture.org.store.state();events=fixture.org.store.events()
        assert state['CapabilityRoute']['route/R1']['status']=='reproduced'
        assert len(state['KnowledgeRevision'])==1 and len(state['KnowledgeUse'])==1
        payload=json.dumps({'state':state,'events':events},ensure_ascii=False,indent=2)
        assert key not in payload and json.loads(identity.read_text())['token'] not in payload
        (out/'evidence.json').write_text(payload,encoding='utf-8')
        (out/'report.json').write_text(json.dumps({'source_hashes':{str(p.as_posix()):hashlib.sha256(p.read_bytes()).hexdigest() for root in ('organization','specs') for p in Path(root).rglob('*') if p.is_file() and p.suffix in ('.py','.js','.css','.html','.cjs','.json')},'verdict':'PASS','synthetic':True,'real_human_participants':0,'model_called':False,'browser':os.environ.get('LAB_BROWSER_CHANNEL','Chromium'),'event_count':len(events),'cross_task_reuse':True,'independent_agent_process':True,'capability_status':'reproduced','scope':'engineering trace only, not learning efficacy'},indent=2),encoding='utf-8')
        print('PASS: browser evidence/verification/package/outcome, independent Agent cross-task reuse')
    finally:
        if http:http.shutdown();http.server_close();thread.join()
        fixture.tearDown()

if __name__=='__main__':main()
