import hashlib,json,subprocess,sys
from pathlib import Path

def main():
    subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-q'],check=True)
    r=json.loads(Path('development/autodev/workspace-demo/report.json').read_text())
    for key in ('real_browser','prefill_checked','drafts_survive_refresh','drafts_isolated_by_human','logout_clears_drafts','no_automatic_decisions','source_unchanged'):assert r[key]
    for path,sha in r['source_hashes'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha,path
    print('PASS: source-bound workspace browser checks and full suite')
if __name__=='__main__':main()
