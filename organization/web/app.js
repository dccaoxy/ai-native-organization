'use strict';
const token = document.querySelector('meta[name="simulation-token"]').content;
const $ = id => document.getElementById(id);
let state = {};
const uid = prefix => prefix + '-' + crypto.randomUUID().slice(0, 8);
const notice = (text, error=false) => { $('notice').textContent=text; $('notice').className=error?'error':''; };
async function api(path, body) {
  const response = await fetch('/api/'+path, {method:body?'POST':'GET', headers:{'Content-Type':'application/json','X-Simulation-Token':token}, ...(body?{body:JSON.stringify(body)}:{})});
  const data=await response.json();
  if (!response.ok) throw new Error(data.error || '操作失败');
  return data;
}
async function send(command, data, actor=$('actor').value, key=crypto.randomUUID()) {
  return api('commands',{actor,command,data,idempotency_key:key});
}
async function action(fn) {
  try { await fn(); await refresh(); notice('正式记录已保存，组织现实已更新。'); }
  catch(e) {notice(e.message,true);}
}
function element(tag,text,cls) {const node=document.createElement(tag); if(text!==undefined)node.textContent=text;if(cls)node.className=cls;return node;}
function card(title,status,lines) {const n=element('article',undefined,'card');n.append(element('span',status,'tag'),element('h3',title));lines.forEach(t=>n.append(element('p',t)));return n;}
function buttons(card,items) {const box=element('div',undefined,'actions');for(const [label,fn] of items){const b=element('button',label,'secondary');b.onclick=()=>action(fn);box.append(b);}card.append(box);}
function form(title,fields) {
  return new Promise(resolve=>{
    $('form-title').textContent=title;$('form-fields').replaceChildren();
    for(const [key,label,type='textarea',value=''] of fields){const row=element('label',label);const input=element(type==='textarea'?'textarea':'input');input.name=key;if(type!=='textarea')input.type=type;input.required=type!=='checkbox';if(type==='checkbox')input.checked=Boolean(value);else input.value=value;row.append(input);$('form-fields').append(row);}
    const finish=value=>{$('form-dialog').close();resolve(value);};
    $('cancel').onclick=()=>finish(null);$('form-dialog').oncancel=()=>resolve(null);
    $('action-form').onsubmit=e=>{e.preventDefault();const result={};for(const input of $('form-fields').querySelectorAll('input,textarea'))result[input.name]=input.type==='checkbox'?input.checked:input.value;finish(result);};
    $('form-dialog').showModal();
  });
}
async function refresh() {
  const [current,trail]=await Promise.all([api('state'),api('events')]);state=current.state;
  $('metrics').replaceChildren();
  for(const [kind,label] of [['HAU','已绑定 HAU'],['Goal','正式 Goal'],['Execution','独立 Execution'],['Return','正式 Return']]){const n=element('div',undefined,'metric');n.append(element('b',Object.keys(state[kind]||{}).length),element('span',label));$('metrics').append(n);}
  $('tasks').replaceChildren();
  for(const t of Object.values(state.Task||{})){
    const n=card(t.id,t.status,[t.expected_output,'验收：'+t.acceptance_criteria,'边界：'+t.boundary.join(' / '),'Goal：'+t.primary_goal]);
    if(t.status==='published')buttons(n,[['领取 → 新 Execution',async()=>{const actor=$('actor').value;const hau=Object.values(state.HAU||{}).find(h=>h.human_id===actor||h.agent_id===actor);if(!hau)throw new Error('当前身份没有 HAU 绑定');await send('claim',{id:uid('E'),task_id:t.id,hau_id:hau.id});}]]);
    $('tasks').append(n);
  }
  if(!$('tasks').children.length)$('tasks').append(element('p','尚无 Task。建立合成身份与 Goal 后，可发布任务。','empty'));
  $('executions').replaceChildren();
  for(const e of Object.values(state.Execution||{})){
    const n=card(e.id,e.status,['Task：'+e.task_id,'HAU：'+e.hau_id+' · Human 责任人：'+e.accountable_owner,'当前边界：'+e.runtime_boundary.join(' / ')]);
    const b=[];
    if(e.status==='claimed')b.push(['ACK 确认',()=>send('ack',{execution_id:e.id})]);
    for(const [command,label,states] of [['progress','报告 Progress',['running']],['blocked','报告 Blocked',['running']],['escalate','求助 / 升级',['running','blocked','interrupted']],['resume','恢复执行',['blocked','interrupted']]])if(states.includes(e.status))b.push([label,async()=>{const x=await form(label,[['summary','必要的公开状态摘要']]);if(x)await send(command,{execution_id:e.id,...x});}]);
    if(['running','blocked','interrupted'].includes(e.status))b.push(['申请 Boundary',async()=>{const x=await form('申请边界变更',[['requested_scope','申请的完整范围，以逗号分隔','text',e.runtime_boundary.join(', ')],['reason','为什么需要变更']]);if(x)await send('request_boundary',{id:uid('B'),execution_id:e.id,requested_scope:x.requested_scope.split(',').map(x=>x.trim()).filter(Boolean),reason:x.reason});}]);
    for(const [command,label] of [['submit','提交成功 Return'],['fail','提交失败 Return'],['release','释放并 Return']])if(['running','blocked','interrupted'].includes(e.status)||(e.status==='claimed'&&command!=='submit'))b.push([label,async()=>{const x=await form(label,[['result','Result / 结果'],['observed_terrain','Observed Terrain / 观察到的环境'],['major_execution_facts','Major Execution Facts / 主要事实'],['reflection','Reflection / 反思']]);if(x)await send(command,{id:uid('R'),execution_id:e.id,...x});}]);
    if(['claimed','running','blocked'].includes(e.status))b.push(['标记 Agent 掉线',()=>send('agent_status',{agent_id:state.HAU[e.hau_id].agent_id,runtime_status:'offline'})]);
    buttons(n,b);$('executions').append(n);
  }
  if(!$('executions').children.length)$('executions').append(element('p','领取 Task 后，每一次尝试都会出现在这里。','empty'));
  $('boundaries').replaceChildren();
  for(const r of Object.values(state.BoundaryRequest||{})){
    const n=card(r.id,'Boundary / '+r.status,[r.reason,'申请范围：'+r.requested_scope.join(' / '),'Human Authority：'+r.authority]);
    if(r.status==='pending')buttons(n,[['批准',()=>send('decide_boundary',{request_id:r.id,decision:'approved'})],['拒绝',()=>send('decide_boundary',{request_id:r.id,decision:'rejected'})],['修改范围',async()=>{const x=await form('Human 修改范围',[['scope','明确批准的完整范围','text',r.requested_scope.join(', ')]]);if(x)await send('decide_boundary',{request_id:r.id,decision:'modified',modified_scope:x.scope.split(',').map(x=>x.trim()).filter(Boolean)});}]]);
    $('boundaries').append(n);
  }
  $('returns').replaceChildren();
  for(const r of Object.values(state.Return||{})){
    const e=state.Execution[r.execution_id],t=state.Task[e.task_id];
    const review=Object.values(state.Review||{}).find(x=>x.return_id===r.id);
    const acceptance=Object.values(state.Acceptance||{}).find(x=>x.return_id===r.id);
    const n=card(r.id,'Return / '+r.outcome,[r.result,'Observed Terrain：'+r.observed_terrain,'主要事实：'+r.major_execution_facts,'Reflection：'+r.reflection,...r.human_annotations,'Review：'+(review?String(review.credible):'等待 '+t.review_authority),'Acceptance：'+(acceptance?String(acceptance.accepted):'等待 '+t.acceptance_authority)]);
    const b=[];
    if(!review){
      for(const [a,label] of [['confirm','Human 确认'],['correct','Human 修正'],['add','Human 补充']])b.push([label,async()=>{const x=await form(label,[['text','Human 注记']]);if(x)await send('annotate_return',{return_id:r.id,action:a,...x});}]);
      b.push(['Review 可信性',async()=>{const x=await form('Review · '+t.review_authority,[['credible','结果可信','checkbox',true],['evidence','可信性证据与理由']]);if(x)await send('review',{id:uid('V'),return_id:r.id,...x});}]);
    }
    if(review&&!acceptance)b.push(['Acceptance 用途判断',async()=>{const x=await form('Acceptance · '+t.acceptance_authority,[['accepted','满足用途','checkbox',r.outcome==='success'&&review.credible],['rationale','用途判断理由']]);if(x)await send('accept',{id:uid('C'),return_id:r.id,review_id:review.id,...x});}]);
    if(acceptance?.accepted&&t.status==='published')b.push(['Selection 选择此结果',async()=>{const x=await form('Selection · '+t.selection_authority,[['rationale','多个合格结果中的选择理由']]);if(x)await send('select',{id:uid('SEL'),task_id:t.id,return_id:r.id,...x});}]);
    buttons(n,b);$('returns').append(n);
  }
  $('events').replaceChildren();
  for(const e of trail.events.slice().reverse()){const tr=element('tr');for(const val of [e.sequence,e.type,e.actor,e.accountable_owner,e.authority_source])tr.append(element('td',val));$('events').append(tr);}
}
$('seed').onclick=()=>action(async()=>{
  for(let i=1;i<=3;i++){
    await send('register_human',{id:'H'+i,display_name:'合成参与者 '+i},'SIMULATOR','ui-seed-human-'+i);
    await send('bind_agent',{hau_id:'U'+i,agent_id:'A'+i,permissions:['claim','ack','progress','blocked','escalate','resume','request_boundary','submit','fail','release']},'H'+i,'ui-seed-agent-'+i);
  }
  await send('activate_goal',{id:'G1',desired_change:'验证合成最小组织闭环',success_criteria:'3 HAU 独立执行并留下正式 Return 与选择证据',boundary:['read','draft'],goal_authority:'H1'},'H1','ui-seed-goal');
});
$('new-task').onclick=()=>action(async()=>{const x=await form('发布合成 Task（Goal Authority：H1）',[['expected_output','预期结果','text','合成场景：提出一项可验证的方案'],['acceptance_criteria','验收标准','text','结果有证据，且在声明边界内完成']]);if(x){const id=uid('T');await send('create_task',{id,primary_goal:'G1',...x,boundary:['read'],execution_mode:'parallel',review_authority:'H2',acceptance_authority:'H1',selection_authority:'H3'});await send('publish',{task_id:id});}});
$('refresh').onclick=()=>action(refresh);
$('sweep').onclick=()=>action(()=>send('sweep',{},'SIMULATOR'));
refresh().then(()=>notice('已读取持久化组织状态。')).catch(e=>notice(e.message,true));
