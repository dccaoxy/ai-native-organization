"""Real browser plus independent Agent subprocess; explicitly synthetic Humans."""
import argparse
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
import tempfile
import threading
from organization.agent_gateway import server


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--node',default='node')
    parser.add_argument('--modules',default='')
    parser.add_argument('--output',default='development/autodev/human-web-demo')
    args=parser.parse_args()
    out=Path(args.output).resolve();out.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        key=secrets.token_urlsafe(32);keyfile=Path(tmp)/'operator.key';keyfile.write_text(key)
        http=server(Path(tmp)/'lab.db',key)
        thread=threading.Thread(target=http.serve_forever,daemon=True);thread.start()
        url=f'http://127.0.0.1:{http.server_port}'
        try:
            subprocess.run([sys.executable,'-m','organization.agent_operator','init-fixture','--url',url,'--operator-key-file',str(keyfile)],check=True,capture_output=True)
            identity=Path(tmp)/'agent.json'
            subprocess.run([sys.executable,'-m','organization.agent_client','register','--url',url,'--identity',str(identity)],check=True,capture_output=True)
            env=dict(os.environ,LAB_URL=url,LAB_KEY=key,LAB_IDENTITY=str(identity),LAB_PYTHON=sys.executable,LAB_OUTPUT=str(out))
            if args.modules:env['NODE_PATH']=args.modules
            subprocess.run([args.node,str(Path(__file__).parent/'human_web_test.cjs')],env=env,check=True,timeout=120)
            state=http.gateway.org.store.state();events=http.gateway.org.store.events()
            assert state['Task']['T']['status']=='closed'
            assert len(state['Review'])==len(state['Acceptance'])==len(state['Selection'])==1
            payload=json.dumps({'state':state,'events':events},ensure_ascii=False,indent=2)
            assert key not in payload and json.loads(identity.read_text())['token'] not in payload
            (out/'evidence.json').write_text(payload,encoding='utf-8')
            (out/'report.json').write_text(json.dumps({'verdict':'PASS','browser':os.environ.get('LAB_BROWSER_CHANNEL','Chromium'),'independent_agent_process':True,'synthetic_human_controls':True,'real_human_participants':0,'model_called':False,'event_count':len(events),'task_closed':True,'credential_leak_in_evidence':False},indent=2),encoding='utf-8')
            print('PASS: real browser approval/review/acceptance/selection and independent Agent subprocess')
        finally:
            http.shutdown();http.server_close();thread.join()

if __name__=='__main__':main()
