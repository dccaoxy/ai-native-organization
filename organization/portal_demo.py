"""Browser-only onboarding acceptance; uses disposable accounts, never real participants."""
import argparse,hashlib,json,os,subprocess,tempfile,threading,sys
from pathlib import Path
from organization.portal import server
from organization.store import Store

def main():
 p=argparse.ArgumentParser();p.add_argument('--node',default='node');p.add_argument('--modules',default='');a=p.parse_args()
 with tempfile.TemporaryDirectory() as tmp:
  http=server(Path(tmp)/'portal.sqlite3');thread=threading.Thread(target=http.serve_forever,daemon=True);thread.start()
  try:
   out=Path('development/autodev/portal-demo').resolve();out.mkdir(parents=True,exist_ok=True)
   env=dict(os.environ,LAB_URL=http.origin,LAB_OUTPUT=str(out),LAB_PYTHON=sys.executable);
   if a.modules:env['NODE_PATH']=a.modules
   subprocess.run([a.node,'organization/portal_web_test.cjs'],env=env,check=True,timeout=120)
   events=http.portal.store.events();state=http.portal.store.state();assert Store.replay(events)==state
   assert len(state['Human'])==2 and len(state['Selection'])==1
   assert 'synthetic-browser-password' not in json.dumps(events)
   (out/'events.json').write_text(json.dumps(events,ensure_ascii=False,indent=2),encoding='utf-8')
   (out/'report.json').write_text(json.dumps({'verdict':'PASS','synthetic':True,'real_human_participants':0,'browser_only':True,'event_count':len(events),'account_count':2,'model_called':False,'source_hashes':{p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('organization').rglob('*') if p.is_file() and p.suffix in ('.py','.js','.cjs','.html','.css')}},indent=2),encoding='utf-8')
  finally:http.shutdown();http.server_close();thread.join()
if __name__=='__main__':main()
