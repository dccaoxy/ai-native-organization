"""Check retained actual browser evidence against the current source files."""
import hashlib,json,subprocess,sys
from pathlib import Path
from organization.store import Store


def main():
    subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-q'],check=True)
    root=Path('development/autodev/learning-demo')
    report=json.loads((root/'report.json').read_text())
    assert report['verdict']=='PASS' and report['cross_task_reuse'] and report['independent_agent_process']
    assert report['real_human_participants']==0 and not report['model_called']
    for path,sha in report['source_hashes'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha,path
    data=json.loads((root/'evidence.json').read_text(encoding='utf-8'))
    assert Store.replay(data['events'])==data['state']
    assert len(data['events'])==report['event_count']
    assert data['state']['CapabilityRoute']['route/R1']['status']=='reproduced'
    print('PASS: source-bound browser evidence and complete test suite')

if __name__=='__main__':main()
