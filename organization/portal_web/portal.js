"use strict";
let csrf='',currentHuman='',portalConnections={};
async function portalApi(path,body){const r=await fetch(path,{method:body?'POST':'GET',headers:body?{'Content-Type':'application/json','X-CSRF-Token':csrf}:{},body:body?JSON.stringify(body):undefined});const d=await r.json();if(!r.ok)throw Error(d.error||'请求失败');return d;}
async function enter(){const me=await portalApi('/api/me');csrf=me.csrf;currentHuman=me.human;await refresh();$('login').hidden=true;$('workspace').hidden=false;showPanel();$('password').value='';message('已登录，选择下一步操作。');}
async function authenticate(create){try{if(create)await portalApi('/api/signup',{username:$('username').value,name:$('display-name').value,password:$('password').value});const r=await portalApi('/api/login',{username:$('username').value,password:$('password').value});csrf=r.csrf;await enter();}catch(e){message(e.message,true);}}
$('signin').onclick=()=>authenticate(false);$('signup').onclick=()=>authenticate(true);
$('refresh').onclick=()=>refresh().catch(e=>message(e.message,true));
$('logout').onclick=async()=>{try{await portalApi('/api/logout',{});location.reload();}catch(e){message(e.message,true);}};
$('create-agent').onclick=async()=>{try{const r=await portalApi('/api/agent',{name:$('agent-name').value});$('connection').textContent=agentInstructions({url:location.origin,registration_id:r.registration_id,token:r.token});await refresh();message('接入说明已生成。复制整段交给 Agent，再为它选择允许的任务并使用基础权限授权。');}catch(e){message(e.message,true);}};
$('copy-connection').onclick=()=>navigator.clipboard.writeText($('connection').textContent).then(()=>message('已复制，请仅交给你的 Agent。')).catch(()=>message('浏览器未允许复制，请手动选择配置文本。',true));
function renderSetup(){const root=$('setup-forms');root.replaceChildren();
 const goal=card(root,'1 · 创建目标');const desire=field(goal,'希望实现什么变化'),criteria=field(goal,'目标成功标准'),boundary=field(goal,'允许的操作（逗号分隔）','read');const gid='G-'+crypto.randomUUID();button(goal,'创建目标',()=>command('activate_goal',{id:gid,desired_change:desire.value,success_criteria:criteria.value,boundary:boundary.value.split(',').map(s=>s.trim()).filter(Boolean),goal_authority:currentHuman}));
 const task=card(root,'2 · 创建任务');const goals=values('Goal').filter(g=>g.goal_authority===currentHuman&&g.status==='active');if(!goals.length){node('p','先创建目标，才能拆分任务。',task);return;}
 const g=select(task,'所属目标',goals.map(g=>[g.id,g.desired_change]));const expected=field(task,'任务预期结果'),acceptance=field(task,'任务验收标准'),bounds=field(task,'任务操作范围（逗号分隔）',goals[0].boundary.join(','));g.onchange=()=>bounds.value=state.Goal[g.value].boundary.join(',');const people=values('Human').map(h=>[h.id,h.display_name]);const reviewer=select(task,'谁审查结果可信度',people),acceptor=select(task,'谁验收任务标准',people),selector=select(task,'谁选择最终结果',people);node('p','三项决定分开记录。可邀请其他人注册后，分别指定责任人。',task);const tid='T-'+crypto.randomUUID();button(task,'保存任务',()=>command('create_task',{id:tid,primary_goal:g.value,expected_output:expected.value,acceptance_criteria:acceptance.value,boundary:bounds.value.split(',').map(s=>s.trim()).filter(Boolean),execution_mode:'parallel',review_authority:reviewer.value,acceptance_authority:acceptor.value,selection_authority:selector.value}));
 for(const t of values('Task').filter(t=>t.status==='draft'&&state.Goal[t.primary_goal].goal_authority===currentHuman))button(root,'发布任务：'+t.expected_output,()=>command('publish',{task_id:t.id}));
}
async function agentApi(path,body){const r=await fetch('/v1/'+path,{method:body?'POST':'GET',headers:{Authorization:'Bearer '+$('agent-token').value,...(body?{'Content-Type':'application/json'}:{})},body:body?JSON.stringify(body):undefined});const d=await r.json();if(!r.ok)throw Error(d.error||'Agent 请求失败');return d;}
$('agent-tasks').onclick=async()=>{try{const me=await agentApi('me');await agentApi('connect',{registration_id:me.registration.id});await refresh();const d=await agentApi('tasks');$('agent-task').replaceChildren();for(const t of d.tasks){const o=node('option',t.expected_output,$('agent-task'));o.value=t.id;}message(d.tasks.length?'请选择任务，再运行协议测试。':'尚无已授权的可执行任务。');}catch(e){message(e.message,true);}};
let testRun=null;
$('agent-run').onclick=async()=>{if(busy)return;busy=true;try{const reg=(await agentApi('me')).registration;const task=$('agent-task').value;if(!task)throw Error('请先连接 Agent 并选择任务');if(!testRun||testRun.task!==task||testRun.registration!==reg.id)testRun={id:'browser-'+crypto.randomUUID(),task,registration:reg.id};const id=testRun.id;const cmd=(command,data,step)=>agentApi('commands',{command,data,idempotency_key:id+'/'+step});await cmd('claim',{id,task_id:task,hau_id:reg.hau_id},'claim');await cmd('ack',{execution_id:id},'ack');await cmd('submit',{id:'R-'+id,execution_id:id,result:'浏览器协议测试完成（非业务成果）',observed_terrain:'明确标识的测试组织任务',major_execution_facts:'经明确授权领取任务、确认执行并提交正式 Return；未调用模型',reflection:'仅证明接入与提交协议可用，不能证明实际业务任务已完成'},'return');await refresh();message('协议测试 Return 已提交，请由指定账号分别审查和验收。');}catch(e){message(e.message,true);}finally{busy=false;}};
enter().catch(()=>{});

function showPanel(){const selected=location.hash.slice(1)||'setup';for(const id of ['setup','agent-connect','agents','tasks','results','learning','events'])$(id).hidden=!(id===selected||(selected==='agents'&&id==='agent-connect'));}
window.addEventListener('hashchange',showPanel);

function agentInstructions(config){return `请作为我的 Agent 接入 AI-Native Organization 测试平台，按以下说明完成连接，不要只回复操作建议。

一、连接配置（含私密凭据，仅用于这个地址，不要公开、写入结果或提交到仓库）
\`\`\`json
${JSON.stringify(config,null,2)}
\`\`\`

二、先检查你是否能执行 HTTP 请求
需要有实际的网络/工具执行能力；纯文字对话无法完成接入。当前地址若为 127.0.0.1 或 localhost，只能从平台所在电脑访问。若你在云端或另一台电脑，请明确报告“地址不可达，需要开发者提供可访问的测试地址”，不要把自己的 localhost 当作平台，不要无限重试或要求用户安装依赖。

三、完成接入
平台已为我创建注册记录，不要再调用 /v1/agents/register，不要创建 Human 账号。
所有请求发往配置 url，使用请求头 Authorization: Bearer <配置 token>；POST 另加 Content-Type: application/json。不要将凭据发送到重定向地址。
1. GET /v1/me，确认返回 registration.id 与配置 registration_id 一致。
2. POST /v1/connect，JSON 请求体为 {"registration_id":"配置中的 registration_id"}。成功返回 connected=true，网页会显示已接入。重复调用不会创建新注册。
3. 再读取 GET /v1/me。若 status=pending，报告“已接入，等待所属用户授权任务”，到这里停止；不要猜测权限。若 revoked/403，报告授权已撤销或不可用。只有 approved 才继续。

四、获准后执行
GET /v1/tasks 读取允许的任务，GET /v1/executions 核对已有执行；读取任务目标、验收标准和 boundary。无可领取任务就报告等待分配；不得领取未授权任务。恢复时先检查已有 Execution，避免重复。
只使用 /v1/me 返回的 permissions 和 hau_id。POST /v1/commands 的格式是：
{"command":"命令名","data":{},"idempotency_key":"该动作的稳定唯一编号"}
步骤示例（替换占位符，不得直接照抄编号）：
- claim: data={"id":"新建的唯一 Execution 编号","task_id":"授权任务 id","hau_id":"返回的 hau_id"}
- ack: data={"execution_id":"刚领取的 Execution 编号"}
- 实际完成任务后 submit: data={"id":"新建的唯一 Return 编号","execution_id":"该 Execution 编号","result":"实际结果","observed_terrain":"观察事实","major_execution_facts":"主要执行事实","reflection":"反思与限制"}
- 实际失败时使用 fail，data 与 submit 格式一致，诚实说明失败，不能用示例数据冒充完成。
请求失败重试须复用完全相同的 idempotency_key/data；新动作才生成新键。遇到 401/403/409 应核对凭据、权限和当前状态，禁止绕过；网络最多重试两次后报告阻碍。
不要申请 Human 密码、切换 Human 身份或替 Human 审查、验收、选择结果。基础权限不包含批准扩权；不得超出任务边界或收集私有思考日志。权限可能被用户调整，每次继续工作前重读 /v1/me。
其他操作的完整协议可访问 ${config.url}/agent-guide.txt；只调用已经明确授权且理解参数的命令。

五、向我汇报
报告真实的连接/授权状态、注册编号、已领取任务和 Execution/Return 编号（若有），以及需要我在网页处理的事项。不回显 token。没有实际调用接口时，不得宣称注册或任务已完成。`;}

const accessOptions=[['claim','领取已授权任务'],['ack','确认开始执行'],['progress','汇报进度'],['submit','提交完成结果'],['fail','报告执行失败'],['blocked','报告阻塞'],['release','放弃本次执行'],['resume','恢复本次执行'],['escalate','请求负责人协助'],['request_boundary','申请扩大任务边界（仍需 Human 批准）'],['challenge_goal','报告目标疑问'],['use_knowledge','记录知识采用或拒绝'],['report_knowledge_issue','报告知识问题']];
const basicAccess=['claim','ack','progress','submit','fail','blocked','release','resume','escalate'];
function accessForm(c,r){const editing=r.status==='approved';node('p',editing?'更改后立即生效；已有 Execution 的负责人和边界不变。移除任务或提交权限会阻止 Agent 继续相关操作。':'默认基础权限：领取与执行已授权任务、汇报进度/阻塞、提交结果或失败、恢复或放弃执行、请求协助。',c);const tasks=[];for(const t of values('Task').filter(t=>t.status==='published'||r.allowed_tasks.includes(t.id))){const l=node('label',undefined,c),check=node('input',undefined,l);check.type='checkbox';check.value=t.id;check.checked=r.allowed_tasks.includes(t.id);l.append(document.createTextNode('任务：'+t.expected_output));tasks.push(check);}if(!tasks.length)node('p','尚无可选任务。Agent 可以先接入，创建并发布任务后再授权。',c);const advanced=node('details',undefined,c);node('summary','调整操作权限（高级）',advanced);const permissions=[];for(const [name,label]of accessOptions){const l=node('label',undefined,advanced),check=node('input',undefined,l);check.type='checkbox';check.value=name;check.setAttribute('aria-label',name);check.checked=(editing?r.permissions:basicAccess).includes(name);l.append(document.createTextNode(label));permissions.push(check);}button(c,editing?'保存权限调整':'确认任务与授权',()=>command(editing?'update_agent_access':'approve_agent',{registration_id:r.id,...(editing?{}:{hau_id:'U-'+currentHuman}),allowed_tasks:tasks.filter(x=>x.checked).map(x=>x.value),permissions:permissions.filter(x=>x.checked).map(x=>x.value)}));}
