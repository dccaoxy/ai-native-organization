const {chromium}=require('playwright'),{spawnSync}=require('child_process'),path=require('path'),fs=require('fs');
(async()=>{const browser=await chromium.launch({headless:true,channel:process.env.LAB_BROWSER_CHANNEL||undefined});try{
const page=await browser.newPage({viewport:{width:1400,height:1000}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.goto(process.env.LAB_URL);await page.locator('#key').fill(process.env.LAB_KEY);await page.getByRole('button',{name:'连接',exact:true}).click();await page.locator('#workspace').waitFor({state:'visible'});
async function actor(id){await page.locator('#actor').selectOption(id);}
async function form(title,fields){await page.getByText(title,{exact:true}).click();const c=page.locator('#learning-list > details').filter({has:page.getByText(title,{exact:true})});for(const [label,value]of Object.entries(fields)){const e=c.getByLabel(label,{exact:true});if(await e.evaluate(e=>e.tagName)==='SELECT')await e.selectOption(value);else await e.fill(value);}await c.getByRole('button',{name:'记录：'+title,exact:true}).click();await page.waitForFunction(()=>!busy);if(await page.locator('#notice').getAttribute('class')==='error')throw Error(await page.locator('#notice').innerText());}
function agent(code,extra={}){const run=spawnSync(process.env.LAB_PYTHON,['-c',code],{encoding:'utf8',env:{...process.env,...extra}});if(run.status!==0)throw Error('Independent Agent failed: '+run.stderr);}
const setup=`import json,os
from pathlib import Path
from organization.agent_client import Client,ProtocolError
i=json.loads(Path(os.environ['LAB_IDENTITY']).read_text());c=Client(os.environ['LAB_URL'],i['token'])
`;

async function settled(){await page.waitForFunction(()=>!busy);if(await page.locator('#notice').getAttribute('class')==='error')throw Error(await page.locator('#notice').innerText());}
async function refresh(){await page.evaluate(()=>refresh());}
async function restart(n){
 const before=await page.evaluate(()=>JSON.stringify(events));
 fs.writeFileSync(path.join(process.env.LAB_IPC,'restart.request'),String(n));
 const end=Date.now()+20000;while(!fs.existsSync(path.join(process.env.LAB_IPC,'restart.'+n+'.done'))){if(Date.now()>end)throw Error('Restart timed out');await new Promise(r=>setTimeout(r,100));}
 await page.reload();await page.locator('#key').fill(process.env.LAB_KEY);await page.getByRole('button',{name:'连接',exact:true}).click();await page.locator('#workspace').waitFor({state:'visible'});
 if(await page.evaluate(()=>JSON.stringify(events))!==before)throw Error('Restart changed event trail');
}
async function register(identity,human,hau,task,permissions){
 const reg=spawnSync(process.env.LAB_PYTHON,['-m','organization.agent_client','register','--url',process.env.LAB_URL,'--identity-file',identity],{encoding:'utf8'});if(reg.status!==0)throw Error('Agent registration failed: '+reg.stderr);
 await refresh();await page.getByRole('button',{name:'批准注册',exact:true}).waitFor();await actor(human);await page.getByLabel('HAU 编号（绑定当前 Human）').fill(hau);await page.getByLabel('允许的 Task 编号（逗号分隔）').fill(task);for(const p of permissions)await page.getByLabel(p,{exact:true}).check();await page.getByRole('button',{name:'批准注册',exact:true}).click();await settled();
}
async function acceptResult(task,rid){
 await refresh();await page.waitForFunction(id=>!!state.Return[id],rid);await actor('H2');const c=page.locator('#return-list article').filter({has:page.getByRole('heading',{name:task+' / '+rid+' · 成功',exact:true})});
 await c.getByLabel('1 · Review：结果可信度').selectOption('true');await c.getByLabel('审查证据（必填）').fill('Synthetic trace reviewed; no real Human participant');await c.getByRole('button',{name:'记录 Review',exact:true}).click();await settled();
 await actor('H1');await c.getByLabel('2 · Acceptance：是否符合任务标准').selectOption('true');await c.getByLabel('验收理由（必填）').fill('Synthetic protocol criteria met');await c.getByRole('button',{name:'记录 Acceptance',exact:true}).click();await settled();
}
for(const i of [1,2]){
 const identity=path.join(process.env.LAB_IPC,'source'+i+'.json');await register(identity,'H'+i,'U'+i,'T1',['claim','ack','submit']);
 const begin=setup+`c.command('claim',{'id':'E${i}','task_id':'T1','hau_id':'U${i}'},'continuous/${i}/claim')
c.command('ack',{'execution_id':'E${i}'},'continuous/${i}/ack')`;
 agent(begin,{LAB_IDENTITY:identity});await refresh();await page.waitForFunction(id=>state.Execution?.[id]?.status==='running','E'+i);
 if(i===1){await restart(1);const count=await page.evaluate(()=>events.length);agent(begin,{LAB_IDENTITY:identity});await refresh();if(await page.evaluate(()=>events.length)!==count)throw Error('Idempotent retry duplicated events');}
 agent(setup+`c.command('submit',{'id':'R${i}','execution_id':'E${i}','result':'Synthetic source ${i}','observed_terrain':'Isolated fixture ${i}','major_execution_facts':'Independent client Return','reflection':'Protocol test, no efficacy claim'},'continuous/${i}/return')`,{LAB_IDENTITY:identity});await acceptResult('T1','R'+i);
}
await actor('H3');const first=page.locator('#return-list article').filter({has:page.getByRole('heading',{name:'T1 / R1 · 成功',exact:true})});await first.getByLabel('3 · Selection：选择此结果的理由').fill('Synthetic selection distinct from review and acceptance');await first.getByRole('button',{name:'选择采用此结果',exact:true}).click();await settled();
await actor('H1');await form('1 · 提出候选认知',{'来源 Return':'R1','独立验证 Human':'H3','修订自哪个知识版本':'none','核心主张':'Synthetic fixture supports a traceable bounded reuse route','适用情境':'Local synthetic tasks only','所需操作边界（逗号分隔）':'read','候选机制解释':'Protocol trace may help reproduce the fixture','迁移条件与不适用情形':'Same local fixture; no real business extrapolation','本轮适用 Task 编号（逗号分隔）':'T2'});
const initialKid=await page.evaluate(()=>Object.keys(state.LearningClaim)[0]);
for(const i of [1,2]){await actor('H'+i);await form('2 · 关联证据',{'对应候选主张':initialKid,'证据来源 Return':'R'+i,'与主张的关系':'supports','证据关系及理由':'Independent synthetic fixture source; not empirical research','共同上游来源标识（逗号分隔，必须如实填写）':'synthetic-source-'+i});}
const initialIds=await page.evaluate(()=>Object.keys(state.LearningEvidence).join(','));await actor('H3');await form('3 · 反证与独立验证',{'待验证主张':initialKid,'判断':'validated','所有相关 Evidence 编号（逗号分隔）':initialIds,'反证尝试及观察结果':'Synthetic negative-path tests, no real causal proof','替代解释':'Fixture bias and shared implementation','局限与未验证范围':'Only protocol correctness','证据独立性判断依据':'Separate declared synthetic sources, not real independent experimental evidence'});
await actor('H1');await form('4 · 整理候选能力包',{'已捕获候选路线':'route/R1','依赖的知识版本':initialKid,'数据及版本':'Synthetic fixture v1','工具及版本':'Local protocol Client','Agent 配置':'Explicit read scope only','运行环境':'Local test process','可复现方法':'Use bounded claim as context, then produce formal Return','Human 审查与监督需求':'H2 Review, H1 Acceptance; no production authority'});

await register(process.env.LAB_IDENTITY,'H3','U3','T2',['claim','ack','use_knowledge','fail','report_knowledge_issue']);
agent(setup+`c.command('claim',{'id':'E3','task_id':'T2','hau_id':'U3'},'continuous/3/claim')
c.command('ack',{'execution_id':'E3'},'continuous/3/ack')
c.command('use_knowledge',{'id':'USE1','execution_id':'E3','knowledge_id':os.environ['KID'],'decision':'adopted','reason':'Synthetic attempted reuse','package_id':'route/R1'},'r01/use')
c.command('agent_status',{'agent_id':c.request('/v1/me')['registration']['agent_id'],'runtime_status':'offline'},'continuous/offline')`,{KID:initialKid});
await refresh();await page.waitForFunction(()=>state.Execution.E3.status==='interrupted');await actor('H1');if(!await page.getByRole('button',{name:'确认 Agent 已恢复',exact:true}).isDisabled())throw Error('Wrong Human can restore Agent');await actor('H3');await page.getByRole('button',{name:'确认 Agent 已恢复',exact:true}).click();await settled();await page.getByLabel('恢复说明 · E3').fill('Synthetic reconnect; persisted execution checked');await page.getByRole('button',{name:'恢复执行 E3',exact:true}).click();await settled();
agent(setup+`c.command('fail',{'id':'R3','execution_id':'E3','result':'Explicit synthetic failure','observed_terrain':'Unexpected fixture condition','major_execution_facts':'Reuse failed in declared synthetic case','reflection':'Need revised scope; no causal proof'},'r01/fail')
c.command('report_knowledge_issue',{'id':'ISSUE','execution_id':'E3','use_id':'USE1','return_id':'R3','reason':'Synthetic failure challenges applicability'},'r01/issue')
assert c.request('/v1/knowledge')['knowledge']==[]
assert c.request('/v1/knowledge-alerts')['alerts'][0]['knowledge_id']==os.environ['KID']
`,{KID:initialKid});
await page.getByRole('button',{name:'刷新状态'}).click();await page.waitForFunction(()=>state.KnowledgeRevision[Object.keys(state.KnowledgeRevision)[0]].status==='challenged');await restart(2);await actor('H1');
await form('8 · 建立新重验任务',{'待重验知识':initialKid,'新的重验 Task 编号':'T3','所属 Active Goal':'G1','重验预期结果':'Reproduce revised synthetic route','重验验收标准':'Formal trace and revised scope check','重验操作边界（逗号分隔）':'read','任务审查 Human':'H2','任务验收 Human':'H1','任务选择 Human':'H3','此次重验理由':'Respond to Agent fixture failure'});
const triggers=await page.evaluate(k=>state.KnowledgeImpact['impact/'+k].triggers.join(','),initialKid);
await form('9 · 带理由修订知识',{'修订依据 Return':'R1','新版本验证 Human':'H3','失效的知识版本':initialKid,'修订后的主张':'Narrowed synthetic claim','修订后的适用情境':'Revalidation fixture only','新版本操作边界（逗号分隔）':'read','修订后的机制解释':'Candidate revised explanation','新迁移条件及失效情境':'Exclude the failed synthetic condition','新版本适用 Task（含重验任务）':'T3','变化理由和如何回应失败':'Narrow scope after ISSUE; no causal conclusion','已回应的影响原因编号（逗号分隔）':triggers});
const kid=await page.evaluate(k=>Object.values(state.LearningClaim).find(c=>c.previous_id===k).id,initialKid);
for(const i of [1,2]){await actor('H'+i);await form('2 · 关联证据',{'对应候选主张':kid,'证据来源 Return':'R'+i,'与主张的关系':'supports','证据关系及理由':'Source supports only revised fixture scope','共同上游来源标识（逗号分隔，必须如实填写）':'synthetic-source-'+i});}
const ids=await page.evaluate(k=>Object.values(state.LearningEvidence).filter(e=>e.claim_id===k).map(e=>e.id).join(','),kid);
await actor('H3');await form('3 · 反证与独立验证',{'待验证主张':kid,'判断':'validated','所有相关 Evidence 编号（逗号分隔）':ids,'反证尝试及观察结果':'Responded to ISSUE by narrowing fixture scope','替代解释':'Fixture bias remains possible','局限与未验证范围':'No real business efficacy','证据独立性判断依据':'Distinct declared fixture provenance only'});
await actor('H1');await form('10 · 创建替代能力包',{'失效能力包':'route/R1','已验证的新知识版本':kid,'能力包变化理由':'Preserve original route and test new version','新的数据及版本':'fixture v2','新的工具及版本':'local client','新的 Agent 配置':'explicit delegation','新的运行环境':'isolated loopback','修订后的方法':'Bounded claim as context only','新的 Human 监督要求':'Separate H2 review and H1 acceptance'});
const pkg=await page.evaluate(()=>Object.values(state.RouteRevision)[0].package_id);
const reg=spawnSync(process.env.LAB_PYTHON,['-m','organization.agent_client','register','--url',process.env.LAB_URL,'--identity-file',process.env.LAB_SECOND_IDENTITY],{encoding:'utf8'});if(reg.status!==0)throw Error('Second registration failed');
await page.getByRole('button',{name:'刷新状态'}).click();await page.getByRole('button',{name:'批准注册',exact:true}).waitFor();await actor('H3');await page.getByLabel('HAU 编号（绑定当前 Human）').fill('U3');await page.getByLabel('允许的 Task 编号（逗号分隔）').fill('T3');for(const p of ['claim','ack','use_knowledge','submit'])await page.getByLabel(p,{exact:true}).check();await page.getByRole('button',{name:'批准注册',exact:true}).click();await page.waitForFunction(()=>!busy);
agent(setup+`k=c.request('/v1/knowledge')['knowledge'];assert len(k)==1 and k[0]['id']==os.environ['KID']
c.command('claim',{'id':'E4','task_id':'T3','hau_id':'U3'},'r01/newclaim')
c.command('ack',{'execution_id':'E4'},'r01/newack')
c.command('use_knowledge',{'id':'USE4','execution_id':'E4','knowledge_id':os.environ['KID'],'decision':'adopted','reason':'Matches revised fixture scope','package_id':os.environ['PKG']},'r01/newuse')
c.command('submit',{'id':'R4','execution_id':'E4','result':'Synthetic revalidation succeeded','observed_terrain':'New planned test task','major_execution_facts':'Recorded new version adoption and formal Return','reflection':'No empirical learning efficacy claim'},'r01/newreturn')
`,{LAB_IDENTITY:process.env.LAB_SECOND_IDENTITY,KID:kid,PKG:pkg});
await page.getByRole('button',{name:'刷新状态'}).click();await page.waitForFunction(()=>!!state.Return.R4);await actor('H2');const result=page.locator('#return-list article').filter({has:page.getByRole('heading',{name:'T3 / R4 · 成功',exact:true})});await result.getByLabel('1 · Review：结果可信度').selectOption('true');await result.getByLabel('审查证据（必填）').fill('Synthetic new task trace inspected');await result.getByRole('button',{name:'记录 Review',exact:true}).click();await page.waitForFunction(()=>!busy);await actor('H1');await result.getByLabel('2 · Acceptance：是否符合任务标准').selectOption('true');await result.getByLabel('验收理由（必填）').fill('Fixture criteria met');await result.getByRole('button',{name:'记录 Acceptance'}).click();await page.waitForFunction(()=>!busy);
await actor('H3');await form('6 · 关联后续结果',{'使用记录':'USE4','同一 Execution 的 Return':'R4','结果观察与解释（不默认归因于知识）':'New fixture task succeeded; no causal assertion'});
await actor('H1');await form('7 · 核对另一 HAU 的复现',{'能力包':pkg,'采用记录':'USE4','复现 Return':'R4'});
const refs=await page.evaluate(()=>({plan:Object.keys(state.RevalidationPlan)[0],rep:Object.values(state.CapabilityReproduction).find(x=>x.return_id==='R4').id}));await form('11 · 确认新任务重验通过',{'重验计划':refs.plan,'新任务的成功复现记录':refs.rep});
await page.screenshot({path:path.join(process.env.LAB_OUTPUT,'continuous-desktop.png'),fullPage:true});await page.locator('#learning').screenshot({path:path.join(process.env.LAB_OUTPUT,'revalidation.png')});await page.setViewportSize({width:390,height:844});if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Narrow viewport overflow');if(errors.length)throw Error(errors.join(';'));
}finally{await browser.close();}})().catch(e=>{console.error(e.message);process.exit(1)});
