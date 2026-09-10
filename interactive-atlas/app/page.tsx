'use client';

import { useMemo, useState } from 'react';
import Image from 'next/image';
import { BookOpen, Bot, CircleDot, Compass, Crown, Flag, GitBranch, Landmark, Map, Network, Route, ScrollText, ShieldCheck, Sparkles, Target, Users } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Sheet, SheetContent, SheetDescription, SheetHeader, SheetTitle } from '@/components/ui/sheet';
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs';

type View = 'world' | 'architecture' | 'knowledge' | 'authority' | 'value';
type Module = { id: string; name: string; slug: string; place: string; icon: typeof Target; color: string; purpose: string; mechanisms: string[]; principles: string[]; concepts: string[] };
const views: { id: View; label: string }[] = [{ id: 'world', label: 'World' }, { id: 'architecture', label: 'Architecture' }, { id: 'knowledge', label: 'Knowledge' }, { id: 'authority', label: 'Authority' }, { id: 'value', label: 'Value' }];

const modules: Module[] = [
  { id: '00', name: 'Organizational Reality', slug: '00 Organizational Reality', place: '史册与道路网络', icon: Network, color: '#6fd7cf', purpose: '让全组织共享同一个事实世界。Event Graph 记录历史，Dependency Graph 表达当前实质依赖。', mechanisms: ['Unified Event', 'Event Graph', 'Dependency Graph', 'Change Set'], principles: ['One organizational reality', 'Record once, interpret many times'], concepts: ['Object', 'Event', 'Dependency', 'Change Set'] },
  { id: '01', name: 'Goal', slug: '01 Goal', place: '目标灯塔', icon: Target, color: '#efb85c', purpose: '定义组织希望世界发生的变化。Human 保留最终 Goal Authority，Agent 可以提出与 Challenge。', mechanisms: ['Activation', 'Challenge', 'Granular Revision'], principles: ['Desired change, not workflow', 'Human purpose authority'], concepts: ['Proposed', 'Active', 'Paused', 'Achieved', 'Superseded'] },
  { id: '02', name: 'Task & Execution', slug: '02 Task and Execution', place: '赏金酒馆', icon: ScrollText, color: '#e98e57', purpose: 'Task 是共享契约；Execution 是一次真实尝试。同一 Task 可以产生多次并行 Execution。', mechanisms: ['Task Bus', 'Claim', 'Parallel Execution', 'Task Return'], principles: ['Task ≠ Execution', 'Exactly one Human owner'], concepts: ['Task Contract', 'Execution', 'ACK', 'Progress', 'Return', 'Release'] },
  { id: '03', name: 'Free Work / R·A·S', slug: '03 Free Work Review Acceptance', place: '探险与归来站', icon: Route, color: '#86c987', purpose: '组织治理契约和边界，不治理私人思考；Review、Acceptance、Selection 分别处理可信、适用与采用。', mechanisms: ['Free Work Space', 'Review', 'Acceptance', 'Selection'], principles: ['Govern contract, not process', 'Evidence follows impact'], concepts: ['Free Work', 'Return', 'Review', 'Acceptance', 'Selection'] },
  { id: '04', name: 'Learning & Knowledge', slug: '04 Learning and Knowledge', place: '图书馆', icon: BookOpen, color: '#58b9d5', purpose: '经历经证据、反证与范围限定后才成为 Knowledge；重要变化通过 Knowledge Pulse 选择性传播。', mechanisms: ['Hypothesis Cloud', 'Falsification', 'Knowledge Pulse'], principles: ['Experience ≠ Knowledge', 'Knowledge ≠ Policy ≠ Protocol'], concepts: ['Experience', 'Evidence', 'Hypothesis', 'Scope', 'Knowledge', 'Pulse'] },
  { id: '05', name: 'Agent Governance', slug: '05 Agent Governance and Runtime', place: '猎犬与控制塔', icon: Bot, color: '#a99bea', purpose: 'Human 与 Representative Agent 构成 HAU；组织状态持久，Agent 上下文通过 Reconstruction 交接。', mechanisms: ['HAU Binding', 'Runtime Envelope', 'Context Reconstruction', 'Kill Switch'], principles: ['No silent failure', 'Permission ≠ Capability'], concepts: ['Active', 'Degraded', 'Suspended', 'Retired', 'Revoked'] },
  { id: '06', name: 'Capability', slug: '06 Capability', place: '地图室', icon: Map, color: '#80cda8', purpose: 'Capability 是由 Execution Evidence 形成的 Terrain 地图。个人成功经复现，才能成为组织道路。', mechanisms: ['Terrain Evidence', 'Capability Package', 'Reproduction', 'Revalidation'], principles: ['Guidance, not permission', 'Capture = reproducibility'], concepts: ['Candidate', 'Reproduced', 'Revalidation needed'] },
  { id: '07', name: 'Contribution & Honor', slug: '07 Contribution Reward Honor Achievement', place: '徽章墙与功勋殿', icon: Crown, color: '#e0a55b', purpose: 'Contribution、Reward、Achievement 与 Honor 分离；盲评事件，以稀缺与饱和理解边际价值。', mechanisms: ['Blind Valuation', 'Scarcity Signal', 'Reward Pool', 'Honor Story'], principles: ['Impact, not activity', 'Honor remembers events'], concepts: ['Detected', 'Valued', 'Rewarded', 'Achievement', 'Honor'] },
  { id: '08', name: 'Governance / Risk / Audit', slug: '08 Governance Risk Audit', place: '城门与市政厅', icon: ShieldCheck, color: '#d66f63', purpose: '治理是决策权架构。Unknown、Risk、Hard Boundary 与 Permission 必须明确分开。', mechanisms: ['Scoped Authority', 'Risk Shaping', 'Policy Governance', 'Audit Trail'], principles: ['Authority has a source', 'Unknown ≠ Dangerous'], concepts: ['Autonomous', 'Escalated', 'Shaped', 'Decided', 'Audited'] },
];

type ViewCopy = { title: string; description: string; legend: string[]; steps: { label: string; value: string; tone: string }[] };
const viewCopy: Record<View, ViewCopy> = {
  world: { title: '组织如何被人理解', description: '同一个合成 Execution：一支 HAU 从酒馆领取任务，穿过已授权的城门，进入未知区域并返回。', legend: ['空间投影', '未知可探索', 'Synthetic fixture'], steps: [{ label: '任务墙', value: 'T-001：调研新人使用 AI 的主要阻碍', tone: '#e98e57' }, { label: '探险队', value: 'E-003 · Human H-01 + Representative Agent A-01', tone: '#a99bea' }, { label: '当前位置', value: 'Free Work Space · Progress 已回报', tone: '#86c987' }] },
  architecture: { title: '系统如何连接', description: '保持 E-003 不变，显示 Task、Execution、Owner、Event 与 Dependency 的不同关系类型。', legend: ['Object', 'Event', 'Dependency'], steps: [{ label: 'contract', value: 'Goal G-001 → Task T-001', tone: '#efb85c' }, { label: 'attempt', value: 'Task T-001 → Execution E-003', tone: '#e98e57' }, { label: 'accountability', value: 'Execution E-003 → Human H-01', tone: '#a99bea' }, { label: 'event', value: 'E-003 → ProgressReported EV-014', tone: '#6fd7cf' }] },
  knowledge: { title: '组织如何知道', description: '只显示 E-003 当前使用和产生的认知材料；Knowledge 不自动成为 Policy。', legend: ['Evidence', 'Scope', 'Pulse'], steps: [{ label: 'used knowledge', value: 'K-007 · Scope：新人访谈任务', tone: '#58b9d5' }, { label: 'new evidence', value: 'EV-014 · 访谈结构出现重复信号', tone: '#6fd7cf' }, { label: 'status', value: 'Candidate Observation · 尚未形成 Knowledge', tone: '#efb85c' }] },
  authority: { title: '谁能决定什么', description: '显示 E-003 当时有效的 Runtime Envelope；责任不等于无限权力。', legend: ['Source', 'Scope', 'Boundary'], steps: [{ label: 'accountable owner', value: 'Human H-01 · 对本次尝试负责', tone: '#a99bea' }, { label: 'permission', value: '内部访谈资料：read-only', tone: '#80cda8' }, { label: 'hard boundary', value: '不得上传可识别个人信息', tone: '#d66f63' }, { label: 'decision route', value: '扩大数据范围 → Data Authority', tone: '#efb85c' }] },
  value: { title: '组织选择记住什么', description: 'E-003 尚未结束，只显示可追溯的候选贡献；不提前制造 Reward、Badge 或 Honor。', legend: ['Impact', 'Scarcity', 'Memory'], steps: [{ label: 'candidate', value: 'Learning Contribution：发现访谈问题偏差', tone: '#e0a55b' }, { label: 'evidence', value: '关联 EV-014 · 等待正式 Return', tone: '#6fd7cf' }, { label: 'not yet', value: 'Reward / Achievement / Honor 均未产生', tone: '#9aa8a3' }] },
};

const sourceBase = 'https://github.com/dccaoxy/ai-native-organization/tree/main/10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1';

export default function Home() {
  const [view, setView] = useState<View>('world');
  const [selected, setSelected] = useState('02');
  const [detailOpen, setDetailOpen] = useState(false);
  const selectedModule = useMemo(() => modules.find((item) => item.id === selected) ?? modules[2], [selected]);
  const currentView = viewCopy[view];
  const ViewIcon = view === 'world' ? Compass : view === 'architecture' ? GitBranch : view === 'knowledge' ? BookOpen : view === 'authority' ? Landmark : Sparkles;
  const ModuleIcon = selectedModule.icon;
  const selectModule = (id: string) => { setSelected(id); setDetailOpen(true); };
  const specificationUrl = `${sourceBase}/${encodeURIComponent(selectedModule.slug)}/${selectedModule.id}%20Specification.md`;

  return (
    <main className="min-h-screen bg-background text-foreground">
      <header className="sticky top-0 z-40 border-b border-white/10 bg-[#101918]/90 backdrop-blur-xl">
        <div className="mx-auto flex max-w-[1800px] flex-wrap items-center gap-3 px-4 py-2.5 lg:px-6">
          <div className="flex min-w-fit items-center gap-3"><div className="grid size-9 place-items-center rounded-xl border border-[#e4af5c]/30 bg-[#e4af5c]/10 text-[#f2c77d]"><Compass aria-hidden="true" /></div><div><p className="text-sm font-semibold tracking-wide">AI-Native Organization</p><p className="text-xs text-white/50">Interactive Atlas · Concept Demo v0.1</p></div></div>
          <Tabs value={view} onValueChange={(value) => setView(value as View)} className="ml-auto hidden lg:flex"><TabsList className="h-9 bg-white/[.06]">{views.map((item) => <TabsTrigger key={item.id} value={item.id} className="px-3 text-sm text-white/60 data-active:bg-white/10 data-active:text-white">{item.label}</TabsTrigger>)}</TabsList></Tabs>
          <label className="ml-auto flex items-center gap-2 text-sm text-white/65 lg:hidden"><span className="sr-only">选择视角</span><select value={view} onChange={(event) => setView(event.target.value as View)} className="h-9 rounded-lg border border-white/15 bg-[#172724] px-3 text-sm text-white">{views.map((item) => <option key={item.id} value={item.id}>{item.label}</option>)}</select></label>
          <span className="rounded-full border border-amber-300/20 bg-amber-300/10 px-3 py-1 text-xs text-amber-100">Design projection · synthetic</span>
        </div>
      </header>
      <div className="mx-auto grid max-w-[1800px] grid-cols-1 lg:grid-cols-[220px_minmax(0,1fr)]">
        <nav className="border-b border-white/10 bg-[#111c1b] p-3 lg:min-h-[calc(100vh-57px)] lg:border-b-0 lg:border-r" aria-label="Operating Model modules">
          <p className="mb-3 px-2 text-xs font-semibold uppercase tracking-[.14em] text-white/45">Operating model</p>
          <div className="grid grid-cols-2 gap-1 sm:grid-cols-3 lg:grid-cols-1">{modules.map((item) => { const Icon = item.icon; const active = item.id === selected; return <button key={item.id} onClick={() => selectModule(item.id)} className={`group flex min-w-0 items-center gap-2 rounded-lg border px-2 py-2 text-left transition ${active ? 'border-white/15 bg-white/[.09]' : 'border-transparent hover:bg-white/[.04]'}`}><span className="grid size-8 shrink-0 place-items-center rounded-md" style={{ background: `${item.color}18`, color: item.color }}><Icon className="size-4" aria-hidden="true" /></span><span className="min-w-0"><span className="block text-xs text-white/40">{item.id}</span><span className={`block truncate text-sm ${active ? 'text-white' : 'text-white/65'}`}>{item.name}</span></span></button>; })}</div>
          <div className="mt-3 rounded-lg border border-[#6fd7cf]/15 bg-[#6fd7cf]/[.06] p-3"><p className="text-xs font-semibold uppercase tracking-wider text-[#88e2da]">X1 World Layer</p><p className="mt-1 text-sm leading-5 text-white/55">隐喻解释规则，但不创造规则。</p></div>
        </nav>
        <section className="min-w-0 bg-[#152321] p-2.5 lg:p-3" aria-label={`${currentView.title}视角`}>
          <div className="relative min-h-[660px] overflow-hidden rounded-2xl border border-white/10 lg:h-[calc(100vh-81px)]">
            <Image src="/village-atlas-v2.png" alt="位于未知边缘的 AI 原生组织新手村概念图" fill priority sizes="(min-width: 1024px) calc(100vw - 244px), 100vw" className="object-cover object-center" />
            <div className={`absolute inset-0 transition-colors ${view === 'world' ? 'bg-gradient-to-t from-[#101b19]/85 via-transparent to-black/20' : 'bg-[#07110f]/65'}`} />
            <div className="absolute left-4 top-4 max-w-[calc(100%-2rem)] rounded-xl border border-white/15 bg-[#0e1716]/88 p-4 backdrop-blur-lg sm:max-w-xl">
              <div className="flex flex-wrap items-center gap-2 text-sm text-[#8ce1d9]"><ViewIcon className="size-4" aria-hidden="true" />{currentView.title}<span className="rounded-full border border-amber-300/25 px-2 py-0.5 text-xs text-amber-100">Synthetic Execution E-003</span></div>
              <p className="mt-2 text-sm leading-6 text-white/70">{currentView.description}</p>
            </div>
            {view === 'world' && <><button onClick={() => selectModule('02')} className="hotspot left-[15%] top-[43%]"><ScrollText aria-hidden="true" /><span>赏金酒馆</span></button><button onClick={() => selectModule('04')} className="hotspot left-[58%] top-[31%]"><BookOpen aria-hidden="true" /><span>图书馆</span></button><button onClick={() => selectModule('06')} className="hotspot left-[76%] top-[44%]"><Map aria-hidden="true" /><span>地图室</span></button><button onClick={() => selectModule('08')} className="hotspot left-[31%] top-[75%]"><Landmark aria-hidden="true" /><span>城门 / 市政厅</span></button><button onClick={() => selectModule('03')} className="hotspot left-[76%] top-[18%]"><Route aria-hidden="true" /><span>探险路线</span></button></>}
            <div className="absolute inset-x-4 bottom-4 grid gap-2 sm:grid-cols-2 xl:grid-cols-4">{currentView.steps.map((step) => <div key={step.label} className="rounded-xl border border-white/15 bg-[#0b1513]/90 p-3 backdrop-blur-lg"><div className="flex items-center gap-2 text-xs uppercase tracking-wide text-white/45"><span className="size-2 rounded-full" style={{ backgroundColor: step.tone }} />{step.label}</div><p className="mt-1.5 text-sm leading-5 text-white/78">{step.value}</p></div>)}</div>
            <div className="absolute right-4 top-4 hidden gap-2 xl:flex">{currentView.legend.map((item) => <span key={item} className="rounded-full border border-white/15 bg-black/45 px-3 py-1 text-xs text-white/65 backdrop-blur">{item}</span>)}</div>
          </div>
        </section>
      </div>
      <Sheet open={detailOpen} onOpenChange={setDetailOpen}>
        <SheetContent className="w-[min(92vw,480px)] overflow-y-auto border-white/15 bg-[#101918] p-5 text-white sm:max-w-[480px]">
          <SheetHeader className="p-0 pr-8"><div className="flex items-start gap-3"><div className="grid size-11 shrink-0 place-items-center rounded-xl" style={{ background: `${selectedModule.color}18`, color: selectedModule.color }}><ModuleIcon aria-hidden="true" /></div><div><div className="flex items-center gap-2 text-xs text-white/45">MODULE {selectedModule.id}<CircleDot className="size-3" style={{ color: selectedModule.color }} /></div><SheetTitle className="mt-1 text-xl text-white">{selectedModule.name}</SheetTitle><SheetDescription className="mt-1 text-sm text-white/50">World projection · {selectedModule.place}</SheetDescription></div></div></SheetHeader>
          <p className="text-base leading-7 text-white/72">{selectedModule.purpose}</p>
          <div className="flex flex-wrap gap-2">{selectedModule.mechanisms.map((item) => <span key={item} className="rounded-lg border border-white/10 bg-white/[.04] px-2.5 py-1.5 text-sm text-white/68">{item}</span>)}</div>
          {selectedModule.id === '02' && <div className="overflow-hidden rounded-xl border border-white/10"><Image src="/tavern-task-wall.png" width={1600} height={800} alt="标注为结构示例的任务墙，展示一项 Task 和多个独立 Execution" className="aspect-[16/8] w-full object-cover" /><p className="bg-black/30 px-3 py-2 text-xs text-amber-100">Synthetic structure example · 非真实组织运行数据</p></div>}
          <div className="grid gap-3 sm:grid-cols-2"><div className="rounded-xl border border-white/10 bg-white/[.03] p-3"><p className="section-label">Key states / objects</p><div className="mt-3 flex flex-wrap gap-1.5">{selectedModule.concepts.map((item) => <span key={item} className="rounded-md border border-white/10 px-2 py-1.5 text-xs text-white/68">{item}</span>)}</div></div><div className="rounded-xl border border-white/10 bg-white/[.03] p-3"><p className="section-label">Frozen principles</p><ul className="mt-2 space-y-2">{selectedModule.principles.map((item) => <li key={item} className="flex gap-2 text-sm leading-5 text-white/64"><Flag className="mt-1 size-3 shrink-0" style={{ color: selectedModule.color }} aria-hidden="true" />{item}</li>)}</ul></div></div>
          <div className="rounded-xl border border-[#6fd7cf]/15 bg-[#6fd7cf]/[.05] p-3"><div className="flex items-center gap-2 text-sm text-white/80"><Users className="size-4 text-[#7fddd4]" aria-hidden="true" />Human + Representative Agent</div><p className="mt-1.5 text-sm leading-6 text-white/55">HAU 是主要工作单元。Capability 不产生 Permission；所有演示状态均为结构示例。</p></div>
          <Button className="h-10 w-full bg-[#d7a452] text-[#15201e] hover:bg-[#ebbd73]" onClick={() => { setView('architecture'); setDetailOpen(false); }}><GitBranch aria-hidden="true" />在架构视角查看 E-003</Button>
          <a className="text-center text-sm text-[#8ce1d9] underline-offset-4 hover:underline" href={specificationUrl} target="_blank" rel="noreferrer">查看最终 Specification 来源</a>
        </SheetContent>
      </Sheet>
    </main>
  );
}
