"""Bounded, explicit learning records. No automatic truth or policy promotion."""
from organization.core import require
from organization.store import DomainError


def items(s, kind):
    return list(s.state.get(kind, {}).values())


def text(value):
    if not isinstance(value, str) or not value.strip():
        raise DomainError('Nonempty explanation required')


def source(s, rid):
    r=s.get('Return',rid);e=s.get('Execution',r['execution_id'])
    return r,e


def accepted(s,rid):
    return any(a['return_id']==rid and a['accepted'] for a in items(s,'Acceptance'))


def invalidate(s,kid,auth,status):
    k=s.get('KnowledgeRevision',kid);k['status']=status
    s.emit('KnowledgeRevision',k,'KnowledgeSuperseded' if status=='superseded' else 'KnowledgeChallenged',auth,k['author'])
    for route in items(s,'CapabilityRoute'):
        if route['knowledge_id']==kid and route['status']!='stale':
            route=dict(route,status='stale')
            s.emit('CapabilityRoute',route,'RouteStale',auth,route['owner'])


def capture_route(s,r,e):
    """Capture candidate within the formal success event; no truth/authority grant."""
    route={'id':'route/'+r['id'],'source_return':r['id'],'source_hau':e['hau_id'],
           'owner':e['accountable_owner'],'knowledge_id':'none','status':'candidate','reproduction_ids':[],
           'components':{'observed_terrain':r['observed_terrain'],'practice':r['major_execution_facts'],
                         'reflection':r['reflection'],'missing':['knowledge','data','tools','agent_configuration','runtime','oversight']}}
    s.attach('CapabilityRoute',route)


def handle(s,command,d):
    if command=='propose_claim':
        require(d,['id','return_id','reviewer','previous_id','core_claim','scope','boundary','mechanism','transfer_conditions','task_ids'])
        s.new('LearningClaim',d['id']);r,e=source(s,d['return_id'])
        auth=s.authority(e['accountable_owner']);s.human(d['reviewer'])
        if d['reviewer']==s.actor:raise DomainError('Separate Human verifier required',403)
        for f in ('core_claim','scope','mechanism','transfer_conditions'):text(d[f])
        if not d['task_ids'] or not isinstance(d['task_ids'],list):raise DomainError('Explicit candidate application tasks required')
        for tid in d['task_ids']:s.get('Task',tid)
        if d['previous_id']!='none':
            old=s.get('KnowledgeRevision',d['previous_id']);s.authority(old['author'])
            if old['status']=='superseded':raise DomainError('Revise current or challenged revision only',409)
        obj={k:v for k,v in d.items() if k!='return_id'}
        obj.update(author=s.actor,source_return=d['return_id'],status='candidate')
        s.emit('LearningClaim',obj,'ClaimProposed',auth,s.actor)
    elif command=='capture_evidence':
        require(d,['id','claim_id','return_id','relation','rationale','upstream_sources'])
        s.new('LearningEvidence',d['id']);claim=s.get('LearningClaim',d['claim_id']);r,e=source(s,d['return_id'])
        auth=s.authority(e['accountable_owner']);text(d['rationale'])
        if d['relation'] not in ('supports','contradicts','discriminates','inconclusive'):raise DomainError('Unknown evidence relation')
        if not isinstance(d['upstream_sources'],list) or not d['upstream_sources'] or any(not isinstance(x,str) or not x.strip() for x in d['upstream_sources']):raise DomainError('Explicit upstream provenance required')
        if any(x['claim_id']==d['claim_id'] and x['return_id']==d['return_id'] for x in items(s,'LearningEvidence')):raise DomainError('Same Return is one source for this claim',409)
        snapshot={'return':r,'execution':e,'task':s.get('Task',e['task_id']),'reviews':[x for x in items(s,'Review') if x['return_id']==r['id']],'acceptances':[x for x in items(s,'Acceptance') if x['return_id']==r['id']]}
        s.emit('LearningEvidence',{**d,'owner':s.actor,'snapshot':snapshot},'EvidenceLinked',auth,s.actor,e['task_id'])
        routeid='route/'+r['id']
        if r['outcome']=='success' and routeid not in s.state.get('CapabilityRoute',{}):
            route={'id':routeid,'source_return':r['id'],'source_hau':e['hau_id'],'owner':s.actor,'knowledge_id':'none','status':'candidate','reproduction_ids':[],
                   'components':{'observed_terrain':r['observed_terrain'],'practice':r['major_execution_facts'],'reflection':r['reflection'],'review_refs':[x['id'] for x in snapshot['reviews']], 'missing':['knowledge','data','tools','agent_configuration','runtime','oversight']}}
            s.emit('CapabilityRoute',route,'RouteCaptured',auth,s.actor,e['task_id'])
        if d['relation']=='contradicts':
            for k in items(s,'KnowledgeRevision'):
                if k['claim_id']==claim['id'] and k['status']=='validated':invalidate(s,k['id'],auth,'challenged')
    elif command=='verify_claim':
        require(d,['id','claim_id','decision','evidence_ids','falsification','alternatives','limitations','independence'])
        s.new('LearningVerification',d['id']);c=s.get('LearningClaim',d['claim_id']);auth=s.authority(c['reviewer'])
        if c['status']!='candidate':raise DomainError('Claim already decided; propose a revision',409)
        if d['decision'] not in ('validated','rejected'):raise DomainError('Unknown verification decision')
        for f in ('falsification','alternatives','limitations','independence'):text(d[f])
        evidence=[s.get('LearningEvidence',eid) for eid in d['evidence_ids']]
        if not evidence or any(x['claim_id']!=c['id'] for x in evidence):raise DomainError('Evidence must belong to this claim')
        if set(d['evidence_ids'])!={x['id'] for x in items(s,'LearningEvidence') if x['claim_id']==c['id']}:raise DomainError('Verification must consider all current evidence',409)
        if d['decision']=='validated':
            if any(x['relation']=='contradicts' for x in evidence):raise DomainError('Counter evidence requires a revised bounded claim',409)
            support=[x for x in evidence if x['relation']=='supports']
            if len({x['snapshot']['execution']['hau_id'] for x in support})<2:raise DomainError('Minimum local gate: two source HAUs required',409)
            upstream=set()
            for x in support:
                if upstream.intersection(x['upstream_sources']):raise DomainError('Shared upstream cannot count as independent evidence',409)
                upstream.update(x['upstream_sources'])
                if not accepted(s,x['return_id']):raise DomainError('Supporting Return requires separate review/acceptance',409)
        c['status']=d['decision'];s.emit('LearningVerification',{**d,'reviewer':s.actor},'ClaimVerified',auth,c['author']);s.attach('LearningClaim',c)
        if d['decision']=='validated':
            previous=c['previous_id'];old=s.get('KnowledgeRevision',previous) if previous!='none' else None
            if old and old['status']=='superseded':raise DomainError('Revision target changed; rebase candidate explicitly',409)
            fields=('core_claim','scope','boundary','mechanism','transfer_conditions','task_ids')
            delta={f:{'before':old[f] if old else None,'after':c[f]} for f in fields if not old or old[f]!=c[f]}
            k={f:c[f] for f in fields};k.update(id=c['id'],claim_id=c['id'],author=c['author'],previous_id=previous,status='validated',version=old['version']+1 if old else 1,evidence_ids=d['evidence_ids'],delta=delta)
            if old:invalidate(s,old['id'],auth,'superseded')
            s.emit('KnowledgeRevision',k,'KnowledgePublished',auth,c['author'])
    elif command=='assemble_route':
        require(d,['package_id','knowledge_id','components'])
        route=s.get('CapabilityRoute',d['package_id']);auth=s.authority(route['owner']);k=s.get('KnowledgeRevision',d['knowledge_id'])
        if route['knowledge_id']!='none':raise DomainError('Package binding immutable; capture a new route for changed dependencies',409)
        if k['status']!='validated':raise DomainError('Validated bounded knowledge required',409)
        if not any(s.get('LearningEvidence',eid)['return_id']==route['source_return'] for eid in k['evidence_ids']):raise DomainError('Route must be grounded in this knowledge evidence',409)
        require(d['components'],['data','tools','agent_configuration','runtime','practice','oversight'])
        for value in d['components'].values():text(value)
        route.update(knowledge_id=k['id'],components=d['components'])
        s.emit('CapabilityRoute',route,'RouteAssembled',auth,route['owner'])
    elif command=='use_knowledge':
        require(d,['id','execution_id','knowledge_id','decision','reason','package_id'])
        s.new('KnowledgeUse',d['id']);e=s.get('Execution',d['execution_id']);auth=s.executor(e,command);k=s.get('KnowledgeRevision',d['knowledge_id'])
        if e['status'] not in ('claimed','running','blocked'):raise DomainError('Knowledge use requires live Execution',409)
        if k['status']!='validated' or e['task_id'] not in k['task_ids']:raise DomainError('Knowledge not valid for explicit task scope',403)
        if not set(k['boundary']).issubset(e['runtime_boundary']):raise DomainError('Knowledge cannot expand runtime boundary',403)
        if d['decision'] not in ('adopted','rejected'):raise DomainError('Explicit adoption or rejection required')
        text(d['reason'])
        if d['package_id']!='none':
            route=s.get('CapabilityRoute',d['package_id'])
            if route['status']=='stale' or route['knowledge_id']!=k['id']:raise DomainError('Package dependency not valid',409)
        s.emit('KnowledgeUse',d,'KnowledgeUsed',auth,e['accountable_owner'],e['task_id'])
    elif command=='record_learning_outcome':
        require(d,['id','use_id','return_id','interpretation'])
        s.new('LearningOutcome',d['id']);u=s.get('KnowledgeUse',d['use_id']);r,e=source(s,d['return_id']);auth=s.authority(e['accountable_owner'])
        if e['id']!=u['execution_id']:raise DomainError('Outcome must belong to the usage Execution',409)
        if any(x['use_id']==u['id'] for x in items(s,'LearningOutcome')):raise DomainError('Outcome already linked',409)
        text(d['interpretation']);s.emit('LearningOutcome',{**d,'owner':s.actor},'LearningOutcomeRecorded',auth,s.actor,e['task_id'])
        # Failure is a revalidation signal, not proof that knowledge caused it.
        if r['outcome']!='success':
            k=s.get('KnowledgeRevision',u['knowledge_id'])
            if k['status']=='validated':invalidate(s,k['id'],auth,'challenged')
    elif command=='record_reproduction':
        require(d,['id','package_id','use_id','return_id'])
        s.new('CapabilityReproduction',d['id']);route=s.get('CapabilityRoute',d['package_id']);auth=s.authority(route['owner']);u=s.get('KnowledgeUse',d['use_id']);r,e=source(s,d['return_id']);k=s.get('KnowledgeRevision',route['knowledge_id'])
        if route['status']=='stale' or k['status']!='validated':raise DomainError('Dependency requires revalidation',409)
        if u['package_id']!=route['id'] or u['execution_id']!=e['id'] or u['decision']!='adopted':raise DomainError('Reproduction requires explicit package adoption',409)
        if e['hau_id']==route['source_hau']:raise DomainError('Another HAU must reproduce',409)
        if any(x['use_id']==u['id'] for x in items(s,'CapabilityReproduction')):raise DomainError('Reproduction already recorded',409)
        if not any(x['use_id']==u['id'] and x['return_id']==r['id'] for x in items(s,'LearningOutcome')):raise DomainError('Link observed outcome first',409)
        if not any(a['return_id']==r['id'] for a in items(s,'Acceptance')):raise DomainError('Reproduction needs a separate final Acceptance decision',409)
        outcome='reproduced' if r['outcome']=='success' and accepted(s,r['id']) else 'not_reproduced'
        s.emit('CapabilityReproduction',{**d,'reviewer':s.actor,'outcome':outcome},'ReproductionRecorded',auth,route['owner'])
        route['reproduction_ids'].append(d['id']);route['status']=outcome if outcome=='reproduced' else 'candidate';s.attach('CapabilityRoute',route)
