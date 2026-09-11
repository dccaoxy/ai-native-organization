import hashlib,json,subprocess,sys
from pathlib import Path

def main():
 subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-q'],check=True)
 r=json.loads(Path('development/autodev/portal-demo/report.json').read_text())
 assert r['verdict']=='PASS' and r['browser_only'] and r['account_count']==2 and r['real_human_participants']==0
 for path,sha in r['source_hashes'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha,path
 print('PASS: full regression and source-bound browser account/Agent acceptance')
if __name__=='__main__':main()
