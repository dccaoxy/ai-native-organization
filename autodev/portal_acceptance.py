import hashlib,json,subprocess,sys,os
from pathlib import Path

def main():
 subprocess.run([sys.executable,'-m','unittest']+(['tests.test_portal','-q'] if os.environ.get('AUTODEV_STAGE')=='S02' else ['discover','-s','tests','-q']),check=True)
 r=json.loads(Path('development/autodev/portal-demo/report.json').read_text())
 assert r['verdict']=='PASS' and r['browser_only'] and r['account_count']==2 and r['real_human_participants']==0
 for path,sha in r['source_hashes'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha,path
 print('PASS: configured regression and source-bound browser account/Agent acceptance')
if __name__=='__main__':main()
