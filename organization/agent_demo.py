"""Actual local HTTP/subprocess demonstration with explicit synthetic Humans.

Optional Codex generates Return content only. It receives no operator/Agent
credential; deterministic client code owns protocol actions and scope checks.
"""
import argparse
import json
import os
from pathlib import Path
import secrets
import shutil
import subprocess
import sys
import tempfile
import threading
from autodev.runtime import write
from organization.agent_client import Client
from organization.agent_gateway import server
from organization.identity import DELEGABLE


def model_result(task):
    executable = shutil.which('codex')
    if not executable:
        raise RuntimeError('Codex CLI unavailable; model demonstration not verified')
    with tempfile.TemporaryDirectory(prefix='agent-model-public-task-') as folder:
        root=Path(folder)
        schema={'type':'object','additionalProperties':False,'properties':{k:{'type':'string'} for k in ['result','observed_terrain','major_execution_facts','reflection']},'required':['result','observed_terrain','major_execution_facts','reflection']}
        write(root/'schema.json',schema)
        prompt='Produce a concise formal Return for this synthetic test task. Propose a useful recommendation grounded only in the provided task. Do not claim tool use, observed execution or real-world results. Explain uncertainty. Do not use tools, inspect files or access credentials. This response is content, not authority to accept or select a result. Task: '+json.dumps(task,ensure_ascii=False)
        result=subprocess.run([executable,'exec','--ignore-user-config','--ephemeral','--sandbox','read-only','--skip-git-repo-check','--color','never','--cd',str(root),'--output-schema',str(root/'schema.json'),'--output-last-message',str(root/'result.json'),'-'],input=prompt,text=True,encoding='utf-8',stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=150)
        if result.returncode:
            raise RuntimeError('Codex model call failed; no model success claimed')
        data=json.loads((root/'result.json').read_text(encoding='utf-8'))
        if set(data)!=set(schema['required']) or not all(isinstance(v,str) and v.strip() for v in data.values()):
            raise ValueError('Invalid formal model Return')
        return data


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--model',action='store_true')
    parser.add_argument('--output',default='development/autodev/agent-demo')
    args=parser.parse_args()
    output=Path(args.output)
    with tempfile.TemporaryDirectory(prefix='agent-lab-') as directory:
        root=Path(directory)
        secret=secrets.token_urlsafe(32)
        httpd=server(root/'lab.sqlite3',secret)
        thread=threading.Thread(target=httpd.serve_forever,daemon=True)
        thread.start()
        url=f'http://127.0.0.1:{httpd.server_port}'
        control=Client(url,secret)
        def op(actor,command,data,key):
            return control.request('/control/commands',{'actor':actor,'command':command,'data':data,'idempotency_key':key})
        identity=root/'client.identity.json'
        def client(*arguments):
            run=subprocess.run([sys.executable,'-m','organization.agent_client',*arguments,'--url',url,'--identity-file',str(identity)],capture_output=True,text=True,timeout=30)
            if run.returncode:
                raise RuntimeError('Independent protocol client failed')
            return json.loads(run.stdout)
        try:
            for i in range(3):
                op('SIMULATOR','register_human',{'id':f'H{i}','display_name':f'Synthetic Human fixture {i}'},f'h{i}')
            op('H0','activate_goal',{'id':'G','desired_change':'Verify independently authenticated Agent workflow','success_criteria':'A traceable synthetic Return with explicit limitations','boundary':['read'],'goal_authority':'H0'},'goal')
            task={'id':'T','primary_goal':'G','expected_output':'Propose three checks for a safe local Agent enrollment workflow','acceptance_criteria':'Checks distinguish registration, authorization and execution, without claiming production evidence','boundary':['read'],'execution_mode':'parallel','review_authority':'H1','acceptance_authority':'H0','selection_authority':'H2'}
            op('H0','create_task',task,'task')
            op('H0','publish',{'task_id':'T'},'publish')
            reg=client('register')
            waiting=client('run','--task','T')
            assert waiting['status']=='WAITING_FOR_HUMAN'
            op('H0','approve_agent',{'registration_id':reg['registration_id'],'hau_id':'U0','permissions':sorted(DELEGABLE),'allowed_tasks':['T']},'approval')
            extra=[]
            if args.model:
                result=model_result(task)
                write(root/'model-return.json',result)
                extra=['--result-file',str(root/'model-return.json')]
            execution=client('run','--task','T',*extra)
            assert execution['status']=='FORMAL_RETURN_RECORDED'
            count=len(httpd.gateway.org.store.events())
            assert client('run','--task','T')['status']=='RETURN_ALREADY_RECORDED'
            assert len(httpd.gateway.org.store.events())==count
            rid=execution['execution_id']+'/return'
            op('H1','review',{'id':'V','return_id':rid,'credible':True,'evidence':'Test controller verified nonempty formal Return and protocol trace; not an independent semantic evaluation'},'review')
            op('H0','accept',{'id':'C','return_id':rid,'review_id':'V','accepted':True,'rationale':'Synthetic test acceptance only; not Human business acceptance'},'accept')
            op('H2','select',{'id':'SEL','task_id':'T','return_id':rid,'rationale':'Synthetic fixture completes the independent decision flow'},'select')
            state=control.request('/control/state')['state']
            events=httpd.gateway.org.store.events()
            assert state['Execution'][execution['execution_id']]['accountable_owner']=='H0'
            assert state['Execution'][execution['execution_id']]['status']=='closed'
            assert state['Task']['T']['status']=='closed'
            raw=json.dumps(events)
            assert secret not in raw and json.loads(identity.read_text())['token'] not in raw
            write(output/'report.json',{'verdict':'PASS','kind':'actual local HTTP plus independent subprocess Agent; synthetic control Humans',
                  'model_generated_return':args.model,'model_is_protocol_planner':False,'independent_process_verified':True,
                  'pending_before_approval_verified':True,'replay_no_duplicate_events':True,'credentials_absent_from_event_trail':True,
                  'event_count':len(events),'real_human_participants':0,'real_company_systems_accessed':False})
            write(output/'events.json',{'simulation':True,'events':events})
            write(output/'state.json',{'simulation':True,'state':state})
            print(f'PASS: independent Agent HTTP flow, {len(events)} synthetic events, model content={args.model}')
        finally:
            httpd.shutdown()
            httpd.server_close()
            thread.join()


if __name__=='__main__':
    main()
