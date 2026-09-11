"""Source-bound browser evidence and the full regression suite for UX02."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def main():
    subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-q'],check=True)
    r=json.loads(Path('development/autodev/continuous-demo/report.json').read_text())
    assert r['verdict']=='PASS' and r['synthetic'] and r['real_human_participants']==0
    assert r['initial_execution_count']==r['initial_knowledge_count']==0
    assert r['registered_agents']==4 and len(r['restarts'])==2
    for key in ('real_browser','independent_agent_processes','restart_idempotency','agent_interruption_recovery','foreign_human_recovery_disabled','event_replay_matches'): assert r[key],key
    assert all(x['events_before']==x['events_after'] for x in r['restarts'])
    assert r['new_task_revalidation']=='passed' and r['old_package']=='stale'
    for report in (r,json.loads(Path('development/autodev/workspace-demo/report.json').read_text())):
        for path,sha in report['source_hashes'].items():assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==sha,path
    print('PASS: continuous browser/Agent evidence, restart/replay, draft regression and full suite')


if __name__=='__main__':main()
