"""Explicit revalidation lineage; failed knowledge is never silently restored."""
from organization.core import require
from organization.store import DomainError
from organization.learning import items,source,text,invalidate


def record_impact(s,kid,auth,trigger):
    identifier='impact/'+kid
    old=s.state.get('KnowledgeImpact',{}).get(identifier,{})
    uses=[u for u in items(s,'KnowledgeUse') if u['knowledge_id']==kid and u['decision']=='adopted']
    active=[u['execution_id'] for u in uses if s.get('Execution',u['execution_id'])['status'] in ('claimed','running','blocked','interrupted')]
    packages=[p['id'] for p in items(s,'CapabilityRoute') if p['knowledge_id']==kid]
    obj={'id':identifier,'knowledge_id':kid,'status':'open','triggers':sorted(set(old.get('triggers',[])+[trigger])),
         'package_ids':sorted(set(old.get('package_ids',[])+packages)), 'execution_ids':sorted(set(old.get('execution_ids',[])+active))}
    s.emit('KnowledgeImpact',obj,'KnowledgeImpactRecorded',auth,s.get('KnowledgeRevision',kid)['author'])


def ensure_revision_context(s,c):
    notes=[n for n in items(s,'RevisionRationale') if n['claim_id']==c['id']]
    if len(notes)!=1:raise DomainError('Explicit revision reason and issue response required',409)
    impact=s.state.get('KnowledgeImpact',{}).get('impact/'+c['previous_id'])
    if impact and not (set(impact['triggers'])-{'superseded'}).issubset(notes[0]['addressed_triggers']):
        raise DomainError('Revision does not address latest impact triggers; propose an updated revision',409)


def descendant(s,new,old):
    seen=set()
    while new!='none' and new not in seen:
        if new==old:return True
        seen.add(new);new=s.get('KnowledgeRevision',new)['previous_id']
    return False


def challenge_knowledge(s,kid,auth,trigger):
    k=s.get('KnowledgeRevision',kid)
    if k['status']=='superseded':record_impact(s,kid,auth,trigger)
    else:invalidate(s,kid,auth,'challenged',trigger)
    for successor in items(s,'KnowledgeRevision'):
        if successor['id']!=kid and successor['status'] in ('validated','challenged') and descendant(s,successor['id'],kid):
            invalidate(s,successor['id'],auth,'challenged','ancestor/'+kid+'/'+trigger)


def eligible_tasks(state,k):
    """Pending revalidation permits trial tasks, not general renewed adoption."""
    ancestors=set();prev=k['previous_id']
    while prev!='none' and prev not in ancestors:
        ancestors.add(prev);prev=state['KnowledgeRevision'][prev]['previous_id']
    trials={p['task_id'] for p in state.get('RevalidationPlan',{}).values() if p['status']=='pending' and p['knowledge_id'] in ancestors}
    return set(k['task_ids']).intersection(trials) if trials else set(k['task_ids'])


def handle(s,cmd,d):
    if cmd=='report_knowledge_issue':
        require(d,['id','execution_id','use_id','return_id','reason'])
        s.new('LearningChallenge',d['id']);u=s.get('KnowledgeUse',d['use_id']);r,e=source(s,d['return_id'])
        if e['id']!=d['execution_id'] or u['execution_id']!=e['id'] or u['decision']!='adopted':raise DomainError('Issue requires own adopted use and formal Return',403)
        auth=s.executor(e,cmd);text(d['reason'])
        s.emit('LearningChallenge',{**d,'reporter':s.actor},'LearningChallengeReported',auth,e['accountable_owner'],e['task_id'])
        k=s.get('KnowledgeRevision',u['knowledge_id'])
        challenge_knowledge(s,k['id'],auth,'challenge/'+d['id'])
    elif cmd=='revise_knowledge':
        require(d,['id','return_id','reviewer','previous_id','core_claim','scope','boundary','mechanism','transfer_conditions','task_ids','reason','addressed_triggers'])
        text(d['reason']);old=s.get('KnowledgeRevision',d['previous_id']);auth=s.authority(old['author'])
        if not isinstance(d['addressed_triggers'],list) or any(not isinstance(x,str) or not x.strip() for x in d['addressed_triggers']):raise DomainError('Trigger references must be a list')
        base={k:v for k,v in d.items() if k not in ('reason','addressed_triggers')}
        s.handle('propose_claim',base)
        note={'id':d['id'],'claim_id':d['id'],'previous_id':old['id'],'reason':d['reason'],'addressed_triggers':d['addressed_triggers']}
        s.emit('RevisionRationale',note,'RevisionExplained',auth,old['author'])
        ensure_revision_context(s,s.get('LearningClaim',d['id']))
    elif cmd=='plan_revalidation':
        require(d,['id','knowledge_id','task_id','goal_id','expected_output','acceptance_criteria','boundary','review_authority','acceptance_authority','selection_authority','reason'])
        s.new('RevalidationPlan',d['id']);k=s.get('KnowledgeRevision',d['knowledge_id']);auth=s.authority(k['author']);text(d['reason'])
        if k['status'] not in ('challenged','superseded'):raise DomainError('Knowledge does not require revalidation',409)
        # Existing task creation checks Goal authority, active Goal and boundary.
        s.handle('create_task',{'id':d['task_id'],'primary_goal':d['goal_id'],'expected_output':d['expected_output'],'acceptance_criteria':d['acceptance_criteria'],'boundary':d['boundary'],'execution_mode':'parallel','review_authority':d['review_authority'],'acceptance_authority':d['acceptance_authority'],'selection_authority':d['selection_authority']})
        s.handle('publish',{'task_id':d['task_id']})
        plan={'id':d['id'],'knowledge_id':k['id'],'task_id':d['task_id'],'owner':s.actor,'reason':d['reason'],'status':'pending','replacement_package':'none','reproduction_id':'none'}
        s.emit('RevalidationPlan',plan,'RevalidationPlanned',auth,s.actor,d['task_id'])
    elif cmd=='revise_route':
        require(d,['id','previous_package','knowledge_id','components','reason'])
        s.new('CapabilityRoute',d['id']);s.new('RouteRevision',d['id'])
        old=s.get('CapabilityRoute',d['previous_package']);auth=s.authority(old['owner']);k=s.get('KnowledgeRevision',d['knowledge_id']);text(d['reason'])
        if old['status']!='stale' or k['status']!='validated' or k['id']==old['knowledge_id'] or not descendant(s,k['id'],old['knowledge_id']):raise DomainError('Stale package requires a validated successor knowledge version',409)
        if not any(s.get('LearningEvidence',eid)['return_id']==old['source_return'] for eid in k['evidence_ids']):raise DomainError('New version must preserve source route evidence',409)
        require(d['components'],['data','tools','agent_configuration','runtime','practice','oversight'])
        for value in d['components'].values():text(value)
        new={**old,'id':d['id'],'knowledge_id':k['id'],'components':d['components'],'status':'candidate','reproduction_ids':[]}
        link={'id':d['id'],'previous_package':old['id'],'package_id':new['id'],'reason':d['reason']}
        s.emit('RouteRevision',link,'RouteRevised',auth,old['owner']);s.attach('CapabilityRoute',new)
    elif cmd=='complete_revalidation':
        require(d,['plan_id','reproduction_id'])
        plan=s.get('RevalidationPlan',d['plan_id']);auth=s.authority(plan['owner'])
        if plan['status']!='pending':raise DomainError('Revalidation already complete',409)
        rep=s.get('CapabilityReproduction',d['reproduction_id']);route=s.get('CapabilityRoute',rep['package_id']);k=s.get('KnowledgeRevision',route['knowledge_id']);r,e=source(s,rep['return_id'])
        if rep['outcome']!='reproduced' or route['status']!='reproduced' or k['status']!='validated' or e['task_id']!=plan['task_id']:raise DomainError('Successful reproduction on the planned new task required',409)
        if k['id']==plan['knowledge_id'] or not descendant(s,k['id'],plan['knowledge_id']):raise DomainError('Replacement must descend from invalidated knowledge',409)
        # New issues reported since revision must be addressed, even if version already published.
        ensure_revision_context(s,s.get('LearningClaim',k['claim_id']))
        plan.update(status='passed',replacement_package=route['id'],reproduction_id=rep['id'])
        s.emit('RevalidationPlan',plan,'RevalidationCompleted',auth,s.actor,plan['task_id'])
        impact=s.get('KnowledgeImpact','impact/'+plan['knowledge_id']);impact['status']='resolved';s.attach('KnowledgeImpact',impact)
