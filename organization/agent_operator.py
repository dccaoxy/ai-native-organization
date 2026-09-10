"""Explicit local test-Human operations; operator key never sent to Agents."""
import argparse
import json
from pathlib import Path
from organization.agent_client import Client


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['init-fixture','list','approve','revoke','state'])
    parser.add_argument('--url',default='http://127.0.0.1:8877')
    parser.add_argument('--operator-key-file',default='.autodev/agent-operator.key')
    parser.add_argument('--registration')
    parser.add_argument('--human',default='H0')
    parser.add_argument('--hau',default='U0')
    parser.add_argument('--tasks',default='T')
    parser.add_argument('--permissions',default='claim,ack,progress,submit,fail,release,request_boundary,resume')
    args=parser.parse_args()
    client=Client(args.url,Path(args.operator_key_file).read_text().strip())
    def command(actor,name,data,key):
        return client.request('/control/commands',{'actor':actor,'command':name,'data':data,'idempotency_key':key})
    if args.action=='init-fixture':
        for i in range(3):
            command('SIMULATOR','register_human',{'id':f'H{i}','display_name':f'Synthetic operator fixture {i}'},f'operator/h{i}')
        command('H0','activate_goal',{'id':'G','desired_change':'Test independent Agent protocol locally','success_criteria':'Traceable formal Return','boundary':['read','draft'],'goal_authority':'H0'},'operator/goal')
        command('H0','create_task',{'id':'T','primary_goal':'G','expected_output':'Suggest three local Agent registration checks','acceptance_criteria':'Explain registration, authorization and Return boundaries','boundary':['read'],'execution_mode':'parallel','review_authority':'H1','acceptance_authority':'H0','selection_authority':'H2'},'operator/task')
        command('H0','publish',{'task_id':'T'},'operator/publish')
        print('Synthetic H0/H1/H2, Goal G and Task T ready; no Agent authorized yet.')
    elif args.action in ('list','state'):
        state=client.request('/control/state')['state']
        print(json.dumps(state.get('AgentRegistration',{}) if args.action=='list' else state,ensure_ascii=False,indent=2))
    else:
        if not args.registration:
            parser.error('--registration required')
        data={'registration_id':args.registration}
        if args.action=='approve':
            data.update(hau_id=args.hau,permissions=args.permissions.split(','),allowed_tasks=args.tasks.split(','))
        command(args.human,'approve_agent' if args.action=='approve' else 'revoke_agent',data,'operator/'+args.action+'/'+args.registration)
        print(args.action+' recorded for '+args.registration)


if __name__=='__main__':
    main()
