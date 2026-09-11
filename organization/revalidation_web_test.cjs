const {chromium}=require('playwright'),{spawnSync}=require('child_process'),path=require('path');
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
agent(setup+`c.command('use_knowledge',{'id':'USE1','execution_id':'E3','knowledge_id':'K1','decision':'adopted','reason':'Synthetic attempted reuse','package_id':'route/R1'},'r01/use')
c.command('fail',{'id':'R3','execution_id':'E3','result':'Explicit synthetic failure','observed_terrain':'Unexpected fixture condition','major_execution_facts':'Reuse failed in declared synthetic case','reflection':'Need revised scope; no causal proof'},'r01/fail')
c.command('report_knowledge_issue',{'id':'ISSUE','execution_id':'E3','use_id':'USE1','return_id':'R3','reason':'Synthetic failure challenges applicability'},'r01/issue')
assert c.request('/v1/knowledge')['knowledge']==[]
assert c.request('/v1/knowledge-alerts')['alerts'][0]['knowledge_id']=='K1'
`);
await page.getByRole('button',{name:'刷新状态'}).click();await page.waitForFunction(()=>state.KnowledgeRevision.K1.status==='challenged');await actor('H1');
await form('8 · 建立新重验任务',{'待重验知识':'K1','新的重验 Task 编号':'T3','所属 Active Goal':'G1','重验预期结果':'Reproduce revised synthetic route','重验验收标准':'Formal trace and revised scope check','重验操作边界（逗号分隔）':'read','任务审查 Human':'H2','任务验收 Human':'H1','任务选择 Human':'H3','此次重验理由':'Respond to Agent fixture failure'});
const triggers=await page.evaluate(()=>state.KnowledgeImpact['impact/K1'].triggers.join(','));
await form('9 · 带理由修订知识',{'修订依据 Return':'R1','新版本验证 Human':'H3','失效的知识版本':'K1','修订后的主张':'Narrowed synthetic claim','修订后的适用情境':'Revalidation fixture only','新版本操作边界（逗号分隔）':'read','修订后的机制解释':'Candidate revised explanation','新迁移条件及失效情境':'Exclude the failed synthetic condition','新版本适用 Task（含重验任务）':'T3','变化理由和如何回应失败':'Narrow scope after ISSUE; no causal conclusion','已回应的影响原因编号（逗号分隔）':triggers});
const kid=await page.evaluate(()=>Object.values(state.LearningClaim).find(c=>c.previous_id==='K1').id);
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
await page.locator('#learning').screenshot({path:path.join(process.env.LAB_OUTPUT,'revalidation.png')});await page.setViewportSize({width:390,height:844});if(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth))throw Error('Narrow viewport overflow');if(errors.length)throw Error(errors.join(';'));
}finally{await browser.close();}})().catch(e=>{console.error(e.message);process.exit(1)});
