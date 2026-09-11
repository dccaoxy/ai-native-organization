"use strict";
// Drafts stay in this tab's memory, separated by synthetic Human. Never credentials.
const learningDrafts=new Map();
function saveLearningDrafts(root){for(const d of root.querySelectorAll('details[data-command]')){if(d.dataset.submitted==='true')continue;const fields={};for(const e of d.querySelectorAll('[data-field]'))fields[e.dataset.field]=e.value;learningDrafts.set(d.dataset.actor+'/'+d.dataset.command,{fields,open:d.open,requestId:d.dataset.requestId});}}
function clearLearningDraft(cmd){learningDrafts.delete($('actor').value+'/'+cmd);const d=document.querySelector('details[data-command="'+cmd+'"]');if(d)d.dataset.submitted='true';}
function clearWorkspaceDrafts(){learningDrafts.clear();}
function configureLearningForm(cmd,f,d){
 const put=(key,value)=>{if(f[key]&&value!==undefined)f[key].value=Array.isArray(value)?value.join(','):value;};
 const watch=(key,fn)=>{if(f[key])f[key].addEventListener('change',fn);};
 const single=(key,list)=>{if(list.length===1)put(key,list[0].id);};
 const correlateUse=()=>{const u=state.KnowledgeUse?.[f.use_id?.value];if(u)single('return_id',values('Return').filter(r=>r.execution_id===u.execution_id));};
 const fill=()=>{
  if(cmd==='verify_claim'){put('evidence_ids',values('LearningEvidence').filter(e=>e.claim_id===f.claim_id.value).map(e=>e.id));}
  if(cmd==='revise_knowledge'){const k=state.KnowledgeRevision?.[f.previous_id.value];if(k){for(const key of ['core_claim','scope','boundary','mechanism','transfer_conditions'])put(key,k[key]);put('return_id',state.LearningClaim?.[k.claim_id]?.source_return);put('reviewer',state.LearningClaim?.[k.claim_id]?.reviewer);const plans=values('RevalidationPlan').filter(p=>p.knowledge_id===k.id&&p.status==='pending');put('task_ids',plans.length?plans.map(p=>p.task_id):k.task_ids);}}
  if(cmd==='plan_revalidation'){const k=state.KnowledgeRevision?.[f.knowledge_id.value],claim=k&&state.LearningClaim?.[k.claim_id],ret=claim&&state.Return?.[claim.source_return],exe=ret&&state.Execution?.[ret.execution_id],task=exe&&state.Task?.[exe.task_id];if(task){put('goal_id',task.primary_goal);put('boundary',task.boundary);for(const key of ['review_authority','acceptance_authority','selection_authority'])put(key,task[key]);put('expected_output','重新验证：'+k.core_claim);put('acceptance_criteria',task.acceptance_criteria);}}
  if(cmd==='revise_route'){const p=state.CapabilityRoute?.[f.previous_package.value];if(p){for(const key of ['data','tools','agent_configuration','runtime','practice','oversight'])put(key,p.components[key]);single('knowledge_id',values('KnowledgeRevision').filter(k=>k.previous_id===p.knowledge_id&&k.status==='validated'));}}
  if(cmd==='record_learning_outcome'||cmd==='record_reproduction')correlateUse();
  if(cmd==='complete_revalidation'){const p=state.RevalidationPlan?.[f.plan_id.value];if(p)single('reproduction_id',values('CapabilityReproduction').filter(r=>r.outcome==='reproduced'&&state.Execution?.[state.Return?.[r.return_id]?.execution_id]?.task_id===p.task_id));}
 };
 const principal={verify_claim:'claim_id',revise_knowledge:'previous_id',plan_revalidation:'knowledge_id',revise_route:'previous_package',record_learning_outcome:'use_id',record_reproduction:'use_id',complete_revalidation:'plan_id'}[cmd];
 if(principal){watch(principal,fill);fill();}
 if(cmd==='plan_revalidation')put('task_id','REVAL-'+crypto.randomUUID().slice(0,8));
 if(cmd==='record_reproduction')watch('package_id',()=>{single('use_id',values('KnowledgeUse').filter(u=>u.package_id===f.package_id.value&&u.decision==='adopted'));correlateUse();});
 if(['verify_claim','revise_knowledge','plan_revalidation','revise_route','record_learning_outcome','record_reproduction','complete_revalidation'].includes(cmd))node('p','已带入现有记录供核对；切换来源会更新关联字段。判断与理由由你填写，提交才会写入。',d);
 if(cmd==='revise_knowledge')button(d,'带入待回应问题编号',()=>{const k=f.previous_id.value;put('addressed_triggers',state.KnowledgeImpact?.['impact/'+k]?.triggers||[]);message('已带入问题编号，请在变化理由中逐项说明如何回应。');});
 const draft=learningDrafts.get($('actor').value+'/'+cmd);if(draft){for(const [key,value]of Object.entries(draft.fields))put(key,value);d.open=draft.open;d.dataset.requestId=draft.requestId;}
}
function renderFlowGuide(){const root=$('flow-guide');root.replaceChildren();const human=$('actor').value;let count=0;
 const action=(text,target)=>{const a=node('a',text,root);a.href=target;a.className='flow-action';count++;};
 for(const r of values('AgentRegistration').filter(r=>r.status==='pending'))action('审批 Agent：'+r.name,'#agents');
 for(const r of values('Return')){const e=state.Execution[r.execution_id],t=state.Task[e.task_id],review=values('Review').find(v=>v.return_id===r.id),accept=values('Acceptance').find(v=>v.return_id===r.id);if(!review&&t.review_authority===human)action('审查结果：'+t.id+' / '+r.id,'#results');else if(review&&!accept&&t.acceptance_authority===human)action('验收结果：'+t.id+' / '+r.id,'#results');else if(accept?.accepted&&t.status==='published'&&t.selection_authority===human)action('选择结果：'+t.id+' / '+r.id,'#results');}
 for(const c of values('LearningClaim').filter(c=>c.status==='candidate'&&c.reviewer===human))action('验证候选认知：'+c.id,'#learning');
 for(const i of values('KnowledgeImpact').filter(i=>i.status==='open'&&state.KnowledgeRevision[i.knowledge_id]?.author===human))action('处理知识重验：'+i.knowledge_id,'#learning');
 if(!count)node('p','当前身份没有上述待处理项。可查看任务与学习记录，或切换到负责下一步的测试 Human。',root);
 node('p','所有操作使用当前工作台的一份数据。刷新会保留本身份的学习表单草稿；退出或重载页面会清除草稿。',root);
}
