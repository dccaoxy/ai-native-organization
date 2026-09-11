import hashlib,json,subprocess,sys
from pathlib import Path
from organization.store import Store

def main():
    subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-q'],check=True)
    root=Path('development/autodev/revalidation-demo');r=json.loads((root/'report.json').read_text());data=json.loads((root/'evidence.json').read_text(encoding='utf-8'))
    assert r['verdict']=='PASS' and r['independent_agent_processes'] and r['new_task_revalidation']=='passed'
    assert r['real_human_participants']==0 and not r['model_called']
    for path,sha in r['source_hashes'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha,path
    assert Store.replay(data['events'])==data['state'] and len(data['events'])==r['event_count']
    assert data['state']['KnowledgeRevision']['K1']['status']=='superseded'
    assert data['state']['CapabilityRoute']['route/R1']['status']=='stale'
    print('PASS: source-bound revalidation browser evidence and full regression')
if __name__=='__main__':main()
