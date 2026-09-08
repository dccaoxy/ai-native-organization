'use client';

import { useMemo, useState } from 'react';
import { BookOpen, Bot, ChevronRight, CircleDot, Compass, Crown, Flag, GitBranch, Landmark, Map, Network, Route, ScrollText, ShieldCheck, Sparkles, Target, Users } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs';

type View = 'world' | 'architecture' | 'knowledge' | 'authority' | 'value';
const views: { id: View; label: string }[] = [
  { id: 'world', label: 'World' }, { id: 'architecture', label: 'Architecture' },
  { id: 'knowledge', label: 'Knowledge' }, { id: 'authority', label: 'Authority' }, { id: 'value', label: 'Value' },
];
const modules = [
  { id: '00', name: 'Organizational Reality', place: '史册与道路网络', icon: Network, color: '#6fd7cf', purpose: '让全组织共享同一个事实世界。Event Graph 记录历史，Dependency Graph 表达当前实质依赖。', mechanisms: ['Unified Event', 'Event Graph', 'Dependency Graph', 'Change Set'], principles: ['One organizational reality', 'Record once, interpret many times'], states: ['Object', 'Event', 'Dependency'] },
  { id: '01', name: 'Goal', place: '目标灯塔', icon: Target, color: '#efb85c', purpose: '定义组织希望世界发生的变化。Human 保留最终 Goal Authority，Agent 可以提出与 Challenge。', mechanisms: ['Activation', 'Challenge', 'Granular Revision'], principles: ['Desired change, not workflow', 'Human purpose authority'], states: ['Proposed', 'Active', 'Paused'] },
  { id: '02', name: 'Task & Execution', place: '赏金酒馆', icon: ScrollText, color: '#e98e57', purpose: 'Task 是共享契约；Execution 是一次真实尝试。同一 Task 可以产生多次并行 Execution。', mechanisms: ['Task Bus', 'Claim', 'Parallel Execution', 'Task Return'], principles: ['Task ≠ Execution', 'Exactly one Human owner'], states: ['Claimed', 'Active', 'Returned'] },
  { id: '03', name: 'Free Work / R·A·S', place: '探险与归来站', icon: Route, color: '#86c987', purpose: '组织治理契约和边界，不治理私人思考；Review、Acceptance、Selection 分别处理可信、适用与采用。', mechanisms: ['Free Work Space', 'Review', 'Acceptance', 'Selection'], principles: ['Govern contract, not process', 'Evidence follows impact'], states: ['Private', 'Submitted', 'Selected'] },
  { id: '04', name: 'Learning & Knowledge', place: '图书馆', icon: BookOpen, color: '#58b9d5', purpose: '经历经证据、反证与范围限定后才成为 Knowledge；重要变化通过 Knowledge Pulse 选择性传播。', mechanisms: ['Hypothesis Cloud', 'Falsification', 'Knowledge Pulse'], principles: ['Experience ≠ Knowledge', 'Knowledge ≠ Policy ≠ Protocol'], states: ['Hypothesis', 'Verified', 'Challenged'] },
  { id: '05', name: 'Agent Governance', place: '猎犬与控制塔', icon: Bot, color: '#a99bea', purpose: 'Human 与 Representative Agent 构成 HAU；组织状态持久，Agent 上下文通过 Reconstruction 交接。', mechanisms: ['HAU Binding', 'Runtime Envelope', 'Context Reconstruction', 'Kill Switch'], principles: ['No silent failure', 'Permission ≠ Capability'], states: ['Active', 'Degraded', 'Suspended'] },
  { id: '06', name: 'Capability', place: '地图室', icon: Map, color: '#80cda8', purpose: 'Capability 是由 Execution Evidence 形成的 Terrain 地图。个人成功经复现，才能成为组织道路。', mechanisms: ['Terrain Evidence', 'Capability Package', 'Reproduction', 'Revalidation'], principles: ['Guidance, not permission', 'Capture = reproducibility'], states: ['Candidate', 'Reproduced', 'Revalidate'] },
  { id: '07', name: 'Contribution & Honor', place: '徽章墙与功勋殿', icon: Crown, color: '#e0a55b', purpose: 'Contribution、Reward、Achievement 与 Honor 分离；盲评事件，以稀缺与饱和理解边际价值。', mechanisms: ['Blind Valuation', 'Scarcity Signal', 'Reward Pool', 'Honor Story'], principles: ['Impact, not activity', 'Honor remembers events'], states: ['Detected', 'Valued', 'Remembered'] },
  { id: '08', name: 'Governance / Risk / Audit', place: '城门与市政厅', icon: ShieldCheck, color: '#d66f63', purpose: '治理是决策权架构。Unknown、Risk、Hard Boundary 与 Permission 必须明确分开。', mechanisms: ['Scoped Authority', 'Risk Shaping', 'Policy Governance', 'Audit Trail'], principles: ['Authority has a source', 'Unknown ≠ Dangerous'], states: ['Autonomous', 'Escalated', 'Decided'] },
];
const viewCopy: Record<View, { title: string; description: string; legend: string[] }> = {
  world: { title: '组织如何被人理解', description: '从新手村进入酒馆、图书馆、地图室和市政厅。每个空间都是同一组织现实的投影。', legend: ['空间投影', '成长可见', '未知可探索'] },
  architecture: { title: '系统如何连接', description: '沿 Object、Event 与 Dependency 下钻，查看模块、机制与状态，不把所有连接误画成依赖。', legend: ['Object', 'Event', 'Dependency'] },
  knowledge: { title: '组织如何知道', description: '从 Experience、Evidence、Hypothesis 到 Knowledge，并追踪 Scope、Challenge 与 Knowledge Pulse。', legend: ['Evidence', 'Scope', 'Pulse'] },
  authority: { title: '谁能决定什么', description: '查看 Authority Source、对象范围、Permission、Risk 与当时有效的决策权。', legend: ['Source', 'Scope', 'Boundary'] },
  value: { title: '组织选择记住什么', description: '查看 Contribution、Downstream Impact、Reward、Badge 与 Honor 如何分离运作。', legend: ['Impact', 'Scarcity', 'Memory'] },
};

export default function Home() {
  const [view, setView] = useState<View>('world');
  const [selected, setSelected] = useState('02');
  const module = useMemo(() => modules.find((m) => m.id === selected) ?? modules[2], [selected]);
  const ViewIcon = view === 'world' ? Compass : view === 'architecture' ? GitBranch : view === 'knowledge' ? BookOpen : view === 'authority' ? Landmark : Sparkles;
  const ModuleIcon = module.icon;
  return (
    <main className="min-h-screen bg-background text-foreground">
      <header className="sticky top-0 z-50 border-b border-white/10 bg-[#101918]/90 backdrop-blur-xl">
        <div className="mx-auto flex max-w-[1500px] items-center gap-5 px-4 py-3 lg:px-8">
          <div className="flex min-w-fit items-center gap-3"><div className="grid size-9 place-items-center rounded-xl border border-[#e4af5c]/30 bg-[#e4af5c]/10 text-[#f2c77d]"><Compass /></div><div><p className="text-sm font-semibold tracking-wide">AI-Native Organization</p><p className="text-[11px] text-white/45">Interactive Atlas · v0.1</p></div></div>
          <Tabs value={view} onValueChange={(v) => setView(v as View)} className="ml-auto hidden lg:flex"><TabsList className="h-9 bg-white/[.06]">{views.map((item) => <TabsTrigger key={item.id} value={item.id} className="px-3 text-xs text-white/55 data-active:bg-white/10 data-active:text-white">{item.label}</TabsTrigger>)}</TabsList></Tabs>
          <span className="rounded-full border border-emerald-300/20 bg-emerald-300/10 px-3 py-1 text-[11px] text-emerald-200">Final Design Baseline</span>
        </div>
      </header>
      <div className="mx-auto grid max-w-[1500px] grid-cols-1 lg:grid-cols-[260px_minmax(0,1fr)_340px]">
        <nav className="border-b border-white/10 bg-[#111c1b] p-4 lg:min-h-[calc(100vh-65px)] lg:border-b-0 lg:border-r lg:p-5" aria-label="Operating Model modules">
          <p className="mb-3 px-2 text-[10px] font-semibold uppercase tracking-[.18em] text-white/35">Operating model</p>
          <div className="grid grid-cols-2 gap-1.5 sm:grid-cols-3 lg:grid-cols-1">{modules.map((m) => { const Icon = m.icon; const active = m.id === selected; return <button key={m.id} onClick={() => setSelected(m.id)} className={`group flex min-w-0 items-center gap-3 rounded-xl border px-3 py-3 text-left transition ${active ? 'border-white/15 bg-white/[.09]' : 'border-transparent hover:bg-white/[.04]'}`}><span className="grid size-8 shrink-0 place-items-center rounded-lg" style={{ background: `${m.color}18`, color: m.color }}><Icon className="size-4" /></span><span className="min-w-0"><span className="block text-[10px] text-white/35">{m.id}</span><span className={`block truncate text-xs ${active ? 'text-white' : 'text-white/60'}`}>{m.name}</span></span>{active && <ChevronRight className="ml-auto size-3.5 text-white/40" />}</button>; })}</div>
          <div className="mt-5 rounded-xl border border-[#6fd7cf]/15 bg-[#6fd7cf]/[.06] p-3"><p className="text-[10px] font-semibold uppercase tracking-wider text-[#88e2da]">X1 World Layer</p><p className="mt-1.5 text-xs leading-5 text-white/45">一个现实，多种投影。隐喻解释规则，但不创造规则。</p></div>
        </nav>
        <section className="min-w-0 bg-[#152321]">
          <div className="relative aspect-[16/9] max-h-[610px] min-h-[360px] overflow-hidden border-b border-white/10">
            <img src="/village-atlas.png" alt="AI-native organization frontier village with functional spaces and exploration routes" className="h-full w-full object-cover" />
            <div className="absolute inset-0 bg-gradient-to-t from-[#152321] via-transparent to-black/20" />
            <div className="absolute left-5 top-5 flex items-center gap-2 rounded-full border border-white/15 bg-black/45 px-3 py-1.5 backdrop-blur-md lg:hidden"><ViewIcon className="size-3.5 text-[#7fddd4]" /><span className="text-xs">{viewCopy[view].title}</span></div>
            <button onClick={() => setSelected('02')} className="hotspot left-[15%] top-[24%]"><ScrollText />赏金酒馆</button>
            <button onClick={() => setSelected('04')} className="hotspot left-[11%] top-[65%]"><BookOpen />图书馆</button>
            <button onClick={() => setSelected('06')} className="hotspot left-[20%] top-[47%]"><Map />地图室</button>
            <button onClick={() => setSelected('08')} className="hotspot left-[40%] top-[23%]"><Landmark />市政厅</button>
            <button onClick={() => setSelected('03')} className="hotspot left-[55%] top-[63%]"><Route />探险路线</button>
            <div className="absolute inset-x-5 bottom-5 flex items-end justify-between gap-4"><div className="max-w-xl rounded-2xl border border-white/15 bg-[#0e1716]/75 p-4 backdrop-blur-lg"><div className="flex items-center gap-2 text-xs text-[#8ce1d9]"><ViewIcon className="size-4" />{viewCopy[view].title}</div><p className="mt-2 text-sm leading-6 text-white/70">{viewCopy[view].description}</p></div><div className="hidden gap-2 xl:flex">{viewCopy[view].legend.map((x) => <span key={x} className="rounded-full border border-white/15 bg-black/35 px-3 py-1 text-[10px] text-white/55 backdrop-blur">{x}</span>)}</div></div>
          </div>
          <div className="grid gap-4 p-5 xl:grid-cols-3">
            <article className="panel-card xl:col-span-2"><div className="flex items-start gap-4"><div className="grid size-12 shrink-0 place-items-center rounded-2xl" style={{ background: `${module.color}18`, color: module.color }}><ModuleIcon /></div><div><div className="flex items-center gap-2"><span className="text-xs text-white/35">MODULE {module.id}</span><CircleDot className="size-3" style={{ color: module.color }} /></div><h1 className="mt-1 text-2xl font-semibold tracking-tight">{module.name}</h1><p className="mt-1 text-sm text-white/45">World projection · {module.place}</p></div></div><p className="mt-5 max-w-3xl text-[15px] leading-7 text-white/68">{module.purpose}</p><div className="mt-5 flex flex-wrap gap-2">{module.mechanisms.map((x) => <span key={x} className="rounded-lg border border-white/10 bg-white/[.04] px-2.5 py-1.5 text-xs text-white/62">{x}</span>)}</div></article>
            <article className="panel-card"><p className="section-label">State model</p><div className="mt-4 flex items-center gap-2">{module.states.map((x, i) => <div key={x} className="contents"><span className="rounded-lg border border-white/10 bg-black/15 px-2.5 py-2 text-[11px] text-white/65">{x}</span>{i < module.states.length - 1 && <ChevronRight className="size-3 text-white/25" />}</div>)}</div><p className="section-label mt-6">Frozen principles</p><ul className="mt-3 space-y-2">{module.principles.map((x) => <li key={x} className="flex gap-2 text-xs leading-5 text-white/58"><Flag className="mt-0.5 size-3.5 shrink-0" style={{ color: module.color }} />{x}</li>)}</ul></article>
          </div>
        </section>
        <aside className="border-t border-white/10 bg-[#101918] p-5 lg:border-l lg:border-t-0 lg:p-6">
          <div className="flex items-center justify-between"><div><p className="section-label">Selected projection</p><h2 className="mt-1 text-lg font-semibold">{module.place}</h2></div><span className="text-2xl font-light text-white/20">{module.id}</span></div>
          <div className="mt-5 overflow-hidden rounded-2xl border border-white/10"><img src={module.id === '02' ? '/tavern-task-wall.png' : '/village-atlas.png'} alt={module.id === '02' ? 'Task wall showing one Task and parallel Executions' : 'Selected world projection'} className="aspect-[4/3] w-full object-cover" /></div>
          <div className="mt-5 space-y-4"><div className="rounded-xl border border-white/10 bg-white/[.035] p-4"><div className="flex items-center gap-2 text-xs font-medium text-white/75"><Users className="size-4 text-[#7fddd4]" />Human + Representative Agent</div><p className="mt-2 text-xs leading-5 text-white/45">HAU 是主要工作单元。每次 Execution 始终唯一解析到一位 Human Accountable Owner。</p></div><div className="rounded-xl border border-white/10 bg-white/[.035] p-4"><div className="flex items-center gap-2 text-xs font-medium text-white/75"><ShieldCheck className="size-4 text-[#efb85c]" />Semantic guardrail</div><p className="mt-2 text-xs leading-5 text-white/45">世界隐喻只解释被冻结的规则。Capability 不产生 Permission，成长不产生 Authority。</p></div></div>
          <Button className="mt-5 h-10 w-full bg-[#d7a452] text-[#15201e] hover:bg-[#ebbd73]" onClick={() => setView('architecture')}><GitBranch />查看机制与连接</Button>
        </aside>
      </div>
    </main>
  );
}
