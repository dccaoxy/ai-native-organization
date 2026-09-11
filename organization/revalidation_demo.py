"""Actual browser and independent Agent processes; synthetic revalidation only."""
import argparse,hashlib,json,os,secrets,subprocess,sys,threading
from pathlib import Path
from tests.test_revalidation import RevalidationTests
from organization.agent_gateway import server
from organization.agent_client import Client


def main():
    p=argparse.ArgumentParser();p.add_argument('--node',default='node');p.add_argument('--modules',default='');p.add_argument('--output',default='development/autodev/revalidation-demo');a=p.parse_args()
    f=RevalidationTests();f.setUp();http=None
    try:
        key=secrets.token_urlsafe(32);http=server(f.org.store.path,key);thread=threading.Thread(target=http.serve_forever,daemon=True);thread.start();url=f'http://127.0.0.1:{http.server_port}'
        identity=Path(f.f.tmp.name)/'agent1.json';second=Path(f.f.tmp.name)/'agent2.json'
        subprocess.run([sys.executable,'-m','organization.agent_client','register','--url',url,'--identity-file',str(identity)],check=True,capture_output=True)
        rid=json.loads(identity.read_text())['id'];Client(url,key).request('/control/commands',{'actor':'H3','command':'approve_agent','data':{'registration_id':rid,'hau_id':'U3','permissions':['use_knowledge','fail','report_knowledge_issue'],'allowed_tasks':['T2']},'idempotency_key':'demo/failure-agent'})
        out=Path(a.output).resolve();out.mkdir(parents=True,exist_ok=True)
        env=dict(os.environ,LAB_URL=url,LAB_KEY=key,LAB_IDENTITY=str(identity),LAB_SECOND_IDENTITY=str(second),LAB_PYTHON=sys.executable,LAB_OUTPUT=str(out))
        if a.modules:env['NODE_PATH']=a.modules
        subprocess.run([a.node,'organization/revalidation_web_test.cjs'],env=env,check=True,timeout=150)
        state=f.org.store.state();events=f.org.store.events()
        plan=next(iter(state['RevalidationPlan'].values()));assert plan['status']=='passed'
        assert state['KnowledgeRevision']['K1']['status']=='superseded' and state['CapabilityRoute']['route/R1']['status']=='stale'
        assert state['CapabilityRoute'][plan['replacement_package']]['status']=='reproduced'
        payload=json.dumps({'state':state,'events':events},ensure_ascii=False,indent=2)
        for secret in [key,json.loads(identity.read_text())['token'],json.loads(second.read_text())['token']]:assert secret not in payload
        (out/'evidence.json').write_text(payload,encoding='utf-8')
        report={'verdict':'PASS','synthetic':True,'real_human_participants':0,'model_called':False,'event_count':len(events),'independent_agent_processes':True,'browser':os.environ.get('LAB_BROWSER_CHANNEL','Chromium'),'new_task_revalidation':'passed','old_knowledge':'superseded','old_package':'stale','source_hashes':{p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for root in ('organization','specs') for p in Path(root).rglob('*') if p.is_file() and p.suffix in ('.py','.js','.css','.html','.cjs','.json')}}
        (out/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print('PASS: Agent failure report -> browser revision -> new Agent task -> reviewed revalidation')
    finally:
        if http:http.shutdown();http.server_close();thread.join()
        f.tearDown()

if __name__=='__main__':main()
