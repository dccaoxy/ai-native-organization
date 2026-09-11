"use strict";
function renderLearning(){
 const root=$('learning-list');saveLearningDrafts(root);root.replaceChildren();
 const choices=kind=>values(kind).map(x=>[x.id,x.id+' · '+(labels[x.status||x.outcome]||x.status||x.outcome||'')]);
 const none=kind=>[['none','无 / 新建版本系列'],...choices(kind)];
 function form(title,cmd,fields,transform=x=>x){const d=node('details',undefined,root);node('summary',title,d);d.dataset.command=cmd;d.dataset.actor=$('actor').value;d.dataset.requestId=crypto.randomUUID();const inputs={};for(const [key,label,kind,options] of fields){inputs[key]=kind==='select'?select(d,label,options):field(d,label,'',kind==='text'?'textarea':'input');inputs[key].dataset.field=key;}configureLearningForm(cmd,inputs,d);button(d,'记录：'+title,()=>{const data={};for(const [key,label,kind]of fields){let value=inputs[key].value.trim();if(!value&&kind!=='optional_list')throw Error('请填写：'+label);data[key]=(kind==='list'||kind==='optional_list')?value.split(',').map(x=>x.trim()).filter(Boolean):value;}if(!['assemble_route','complete_revalidation'].includes(cmd))data.id=d.dataset.requestId;return command(cmd,transform(data));});}
 form('1 · 提出候选认知','propose_claim',[
 ['return_id','来源 Return','select',choices('Return')],['reviewer','独立验证 Human','select',choices('Human')],['previous_id','修订自哪个知识版本','select',[['none','新候选；版本修订请使用步骤 9']]],['core_claim','核心主张','text'],['scope','适用情境','text'],['boundary','所需操作边界（逗号分隔）','list'],['mechanism','候选机制解释','text'],['transfer_conditions','迁移条件与不适用情形','text'],['task_ids','本轮适用 Task 编号（逗号分隔）','list']]);
 form('2 · 关联证据','capture_evidence',[
 ['claim_id','对应候选主张','select',choices('LearningClaim')],['return_id','证据来源 Return','select',choices('Return')],['relation','与主张的关系','select',[['inconclusive','暂无法判断'],['supports','支持'],['contradicts','反驳'],['discriminates','区分其他解释']]],['rationale','证据关系及理由','text'],['upstream_sources','共同上游来源标识（逗号分隔，必须如实填写）','list']]);
 form('3 · 反证与独立验证','verify_claim',[
 ['claim_id','待验证主张','select',choices('LearningClaim')],['decision','判断','select',[['rejected','证据不足 / 拒绝'],['validated','在声明范围内确认']]],['evidence_ids','所有相关 Evidence 编号（逗号分隔）','list'],['falsification','反证尝试及观察结果','text'],['alternatives','替代解释','text'],['limitations','局限与未验证范围','text'],['independence','证据独立性判断依据','text']]);
 form('4 · 整理候选能力包','assemble_route',[
 ['package_id','已捕获候选路线','select',choices('CapabilityRoute')],['knowledge_id','依赖的知识版本','select',choices('KnowledgeRevision')],...['data','tools','agent_configuration','runtime','practice','oversight'].map((k,i)=>[k,['数据及版本','工具及版本','Agent 配置','运行环境','可复现方法','Human 审查与监督需求'][i],'text'])],d=>{const components={};for(const k of ['data','tools','agent_configuration','runtime','practice','oversight']){components[k]=d[k];delete d[k];}return {...d,components};});
 form('5 · 记录执行中的采用或拒绝','use_knowledge',[
 ['execution_id','当前 Execution','select',choices('Execution')],['knowledge_id','知识版本','select',choices('KnowledgeRevision')],['package_id','能力包（可不使用）','select',none('CapabilityRoute')],['decision','使用决定','select',[['rejected','拒绝采用'],['adopted','采用']]],['reason','范围判断与使用理由','text']]);
 form('6 · 关联后续结果','record_learning_outcome',[
 ['use_id','使用记录','select',choices('KnowledgeUse')],['return_id','同一 Execution 的 Return','select',choices('Return')],['interpretation','结果观察与解释（不默认归因于知识）','text']]);
 form('7 · 核对另一 HAU 的复现','record_reproduction',[
 ['package_id','能力包','select',choices('CapabilityRoute')],['use_id','采用记录','select',choices('KnowledgeUse')],['return_id','复现 Return','select',choices('Return')]]);

 const impacts=card(root,'待重验影响与处理记录');
 for(const impact of values('KnowledgeImpact')){const c=card(impacts,impact.knowledge_id+' · '+(impact.status==='open'?'需要重验':'已有替代版本通过'));node('p','原版本保持失效；仅采用经过验证的新版本。已有执行不会被自动暂停。',c);dump(c,'原因和影响快照',impact);for(const id of impact.execution_ids){const e=state.Execution[id];node('p','受影响执行 '+id+' · '+(e?.status||'未知')+' · Human '+(e?.accountable_owner||'未知'),c);}for(const id of impact.package_ids)node('p','能力包 '+id+' · '+(labels[state.CapabilityRoute[id]?.status]||state.CapabilityRoute[id]?.status||'未知'),c);}
 form('8 · 建立新重验任务','plan_revalidation',[
 ['knowledge_id','待重验知识','select',choices('KnowledgeRevision')],['task_id','新的重验 Task 编号','input'],['goal_id','所属 Active Goal','select',choices('Goal')],['expected_output','重验预期结果','text'],['acceptance_criteria','重验验收标准','text'],['boundary','重验操作边界（逗号分隔）','list'],['review_authority','任务审查 Human','select',choices('Human')],['acceptance_authority','任务验收 Human','select',choices('Human')],['selection_authority','任务选择 Human','select',choices('Human')],['reason','此次重验理由','text']]);
 form('9 · 带理由修订知识','revise_knowledge',[
 ['return_id','修订依据 Return','select',choices('Return')],['reviewer','新版本验证 Human','select',choices('Human')],['previous_id','失效的知识版本','select',choices('KnowledgeRevision')],['core_claim','修订后的主张','text'],['scope','修订后的适用情境','text'],['boundary','新版本操作边界（逗号分隔）','list'],['mechanism','修订后的机制解释','text'],['transfer_conditions','新迁移条件及失效情境','text'],['task_ids','新版本适用 Task（含重验任务）','list'],['reason','变化理由和如何回应失败','text'],['addressed_triggers','已回应的影响原因编号（逗号分隔）','optional_list']]);
 form('10 · 创建替代能力包','revise_route',[
 ['previous_package','失效能力包','select',choices('CapabilityRoute')],['knowledge_id','已验证的新知识版本','select',choices('KnowledgeRevision')],['reason','能力包变化理由','text'],...['data','tools','agent_configuration','runtime','practice','oversight'].map((k,i)=>[k,['新的数据及版本','新的工具及版本','新的 Agent 配置','新的运行环境','修订后的方法','新的 Human 监督要求'][i],'text'])],d=>{const components={};for(const k of ['data','tools','agent_configuration','runtime','practice','oversight']){components[k]=d[k];delete d[k];}return {...d,components};});
 form('11 · 确认新任务重验通过','complete_revalidation',[
 ['plan_id','重验计划','select',choices('RevalidationPlan')],['reproduction_id','新任务的成功复现记录','select',choices('CapabilityReproduction')]]);
 for(const [kind,title]of [['KnowledgeImpact','失效影响'],['LearningChallenge','Agent 问题报告'],['RevisionRationale','修订理由'],['RevalidationPlan','重验任务与结论'],['RouteRevision','能力包替代关系'],['LearningClaim','候选解释（历史判断）'],['LearningEvidence','证据及来源快照'],['LearningVerification','独立验证记录'],['KnowledgeRevision','知识版本与变化'],['CapabilityRoute','候选路线与复现状态'],['KnowledgeUse','采用 / 拒绝'],['LearningOutcome','结果反馈'],['CapabilityReproduction','跨 HAU 复现']]){const c=card(root,title+' · '+values(kind).length);for(const x of values(kind))dump(c,x.id+' · '+(labels[x.status||x.decision||x.relation||x.outcome]||x.status||x.decision||x.relation||x.outcome||''),x);}
}
