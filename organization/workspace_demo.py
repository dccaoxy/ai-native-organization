"""Real browser tests for drafts and source prefill, without Human decisions."""
import argparse,hashlib,json,os,secrets,subprocess,threading
from pathlib import Path
from tests.test_revalidation import RevalidationTests
from organization.agent_gateway import server
from organization.workspace import prepare

def main():
    p=argparse.ArgumentParser();p.add_argument('--node',default='node');p.add_argument('--modules',default='');p.add_argument('--output',default='development/autodev/workspace-demo');a=p.parse_args()
    f=RevalidationTests();f.setUp();http=None
    try:
        f.fail();f.plan();f.revision()
        db,key=prepare(Path(f.f.tmp.name)/'unified',f.org.store.path);before=f.org.store.events()
        http=server(db,key.read_text());thread=threading.Thread(target=http.serve_forever,daemon=True);thread.start()
        out=Path(a.output).resolve();out.mkdir(parents=True,exist_ok=True)
        env=dict(os.environ,LAB_URL=f'http://127.0.0.1:{http.server_port}',LAB_KEY=key.read_text(),LAB_OUTPUT=str(out))
        if a.modules:env['NODE_PATH']=a.modules
        subprocess.run([a.node,'organization/workspace_web_test.cjs'],env=env,check=True,timeout=120)
        assert before==http.gateway.org.store.events()==f.org.store.events()
        report={'verdict':'PASS','real_browser':True,'prefill_checked':True,'drafts_survive_refresh':True,'drafts_isolated_by_human':True,'logout_clears_drafts':True,'no_automatic_decisions':True,'source_unchanged':True,'source_hashes':{p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('organization').rglob('*') if p.is_file() and p.suffix in ('.py','.js','.css','.html','.cjs')}}
        (out/'report.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print('PASS: real browser prefill/drafts/logout; no organization events changed')
    finally:
        if http:http.shutdown();http.server_close();thread.join()
        f.tearDown()
if __name__=='__main__':main()
