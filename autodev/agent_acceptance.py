"""Verify cumulative code and previously executed live model evidence locally."""
import subprocess
import sys
from pathlib import Path
from autodev.runtime import read
from organization.store import Store


def main():
    result=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-q'])
    if result.returncode:
        return result.returncode
    root=Path('development/autodev/agent-model-demo')
    report=read(root/'report.json')
    events=read(root/'events.json')['events']
    state=read(root/'state.json')['state']
    assert report['verdict']=='PASS' and report['model_generated_return'] is True
    assert report['model_is_protocol_planner'] is False
    assert report['independent_process_verified'] and report['pending_before_approval_verified']
    assert report['real_human_participants']==0 and len(events)==report['event_count']
    assert all(e['simulation'] for e in events) and Store.replay(events)==state
    assert state['Task']['T']['status']=='closed' and len(state['Return'])==1
    assert all(e['accountable_owner']=='H0' for e in state['Execution'].values())
    print('Live model evidence: content generation and independent protocol flow verified; no semantic business acceptance claim')
    return 0


if __name__=='__main__':
    raise SystemExit(main())
