"""Explicit synthetic M01 scenario through the public command contract.

These are executed software tests, never observations of real Humans or E01–E08.
"""
import argparse
from pathlib import Path
import tempfile
from organization.core import Organization
from organization.identity import DELEGABLE
from autodev.runtime import write


def scenario(send):
    def call(actor, command, data, key):
        return send(actor=actor, command=command, data=data, idempotency_key='m01-simulation/' + key)
    for i in range(1,4):
        call('SIMULATOR','register_human',{'id':f'H{i}','display_name':f'Synthetic Human {i}'},f'human-{i}')
        call(f'H{i}','bind_agent',{'hau_id':f'U{i}','agent_id':f'A{i}','permissions':sorted(DELEGABLE)},f'agent-{i}')
    call('H1','activate_goal',{'id':'G1','desired_change':'Exercise minimum organization in a synthetic environment','success_criteria':'Three independent attempts, formal returns and accountable selection','boundary':['read','draft'],'goal_authority':'H1'},'goal')
    call('H1','create_task',{'id':'T1','primary_goal':'G1','expected_output':'Synthetic fixture recommendation','acceptance_criteria':'Evidence-backed fixture result with explicit boundary','boundary':['read'],'execution_mode':'parallel','review_authority':'H2','acceptance_authority':'H1','selection_authority':'H3'},'task')
    call('H1','publish',{'task_id':'T1'},'publish')
    for i in range(1,4):
        call(f'A{i}','claim',{'id':f'E{i}','task_id':'T1','hau_id':f'U{i}'},f'claim-{i}')
        call(f'A{i}','ack',{'execution_id':f'E{i}'},f'ack-{i}')
    call('A1','progress',{'execution_id':'E1','summary':'Synthetic public checkpoint'},'progress')
    call('A2','blocked',{'execution_id':'E2','summary':'Needs an explicitly authorized scope extension'},'blocked')
    call('A2','request_boundary',{'id':'B1','execution_id':'E2','requested_scope':['read','draft'],'reason':'Synthetic draft action requires Human authorization'},'boundary-request')
    call('H1','decide_boundary',{'request_id':'B1','decision':'approved'},'boundary-approved')
    call('A2','resume',{'execution_id':'E2','summary':'Resume within Human-authorized scope'},'resume-2')
    call('A3','agent_status',{'agent_id':'A3','runtime_status':'offline'},'runtime-interruption')
    call('H3','resume',{'execution_id':'E3','summary':'Human resumes responsibility after simulated runtime loss'},'resume-3')
    for i in range(1,4):
        call(f'H{i}', 'fail' if i == 3 else 'submit',
             {'id':f'R{i}','execution_id':f'E{i}','result':'Synthetic failure evidence' if i == 3 else f'Synthetic candidate {i}',
              'observed_terrain':'Controlled software-test environment only','major_execution_facts':'Command/Event trail recorded by the running system',
              'reflection':'No real Human behavior or business impact is inferred'},f'return-{i}')
        call(f'H{i}','annotate_return',{'return_id':f'R{i}','action':'confirm','text':'Synthetic owner confirmation'},f'confirm-{i}')
        call('H2','review',{'id':f'V{i}','return_id':f'R{i}','credible':True,'evidence':'Inspected recorded synthetic command outcomes'},f'review-{i}')
        call('H1','accept',{'id':f'C{i}','return_id':f'R{i}','review_id':f'V{i}','accepted':i != 3,'rationale':'Synthetic intended-use judgment; failure is not an accepted success'},f'accept-{i}')
    return call('H3','select',{'id':'SEL1','task_id':'T1','return_id':'R2','rationale':'Explicit selection among two accepted synthetic candidates'},'selection')


def verify(state, events):
    types = {e['type'] for e in events}
    checks = {
        'three_hau_one_goal_one_task_three_independent_executions': len(state['HAU']) == 3 and len(state['Goal']) == 1 and len(state['Task']) == 1 and len(state['Execution']) == 3,
        'success': state['Return']['R1']['outcome'] == 'success' and state['Acceptance']['C1']['accepted'],
        'failure_returns_information': state['Return']['R3']['outcome'] == 'failure' and not state['Acceptance']['C3']['accepted'],
        'blocked_and_boundary_extension': {'Blocked','BoundaryRequested','BoundaryApproved','Resumed'}.issubset(types),
        'parallel_selection_preserves_all_returns': len(state['Return']) == 3 and state['Selection']['SEL1']['return_id'] == 'R2',
        'interruption_visible_and_recoverable': 'ExecutionInterrupted' in types and state['Execution']['E3']['status'] == 'closed',
        'unique_human_accountability': {e['accountable_owner'] for e in state['Execution'].values()} == {'H1','H2','H3'},
        'all_attempts_closed_with_returns': all(e['status'] == 'closed' and e['return_id'] in state['Return'] for e in state['Execution'].values()),
        'review_acceptance_selection_distinct': len(state['Review']) == 3 and len(state['Acceptance']) == 3 and len(state['Selection']) == 1,
        'all_evidence_labelled_simulation': all(e['simulation'] is True for e in events),
    }
    if not all(checks.values()): raise AssertionError(checks)
    return checks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='development/autodev/simulation')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        org = Organization(Path(tmp) / 'simulation.sqlite3')
        scenario(org.execute)
        state, events = org.store.state(), org.store.events()
        checks = verify(state, events)
        root = Path(args.output)
        write(root / 'report.json', {'kind':'synthetic software execution, not real research evidence','checks':checks,
                                     'event_count':len(events),'object_counts':{k:len(v) for k,v in state.items()},
                                     'verdict':'PASS','real_human_participants':0})
        write(root / 'events.json', {'simulation':True,'events':events})
        write(root / 'state.json', {'simulation':True,'state':state})
        print(f'PASS: {len(checks)} assertions, {len(events)} actual synthetic events')


if __name__ == '__main__': main()
