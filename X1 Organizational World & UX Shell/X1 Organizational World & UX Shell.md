# X1 Organizational World & UX Shell

> 状态：🔒 v0.1 独立横切层。它投影 Operating Model，不改变底层规则，也不拆回各模块 Mental Model。

## Purpose

回答 Human 如何看见、理解、进入并感受到组织。系统保持三层：`Organizational Reality → Operating Model → World/UX Projections`；所有视角读取同一现实。

## WORLD-01~08

1. **WORLD-01 — One system, multiple projections.** 一个现实可有多种投影，不能有多套现实。
2. **WORLD-02 — Metaphor explains rules; it does not create rules.** 隐喻帮助理解规则，但不创造规则。
3. **WORLD-03 — The world grows from organizational reality.** 世界由真实事件、知识、能力和荣誉驱动生长，禁止假数据。
4. **WORLD-04 — Unknown should feel explorable, not forbidden.** Unknown、Hazard、Hard Boundary、Permission 必须分开。
5. **WORLD-05 — Growth should be visible without becoming hierarchy.** 可见成长不产生等级权力。
6. **WORLD-06 — The village expands through exploration.** Execution Return 让已知世界扩大。
7. **WORLD-07 — Every place corresponds to a real organizational function.** 没有真实机制映射的空间不进入正式世界。
8. **WORLD-08 — Different humans may need different views of the same world.** 同一现实支持 World、Architecture、Knowledge、Authority、Value 等视角。

## Seed World Ontology

| 世界对象 | 系统语义 |
|---|---|
| 新手村 / 城市 | 组织当前已知、可运行的共同世界 |
| 赏金酒馆 / 任务墙 | Task Bus 与 Task Discovery |
| 赏金猎人 + 猎犬 | Human + Representative Agent = HAU |
| 战争迷雾 | Unknown / Uncertainty |
| 危险地形 | Hazard / Risk |
| 城墙 / 禁区 | Hard Boundary |
| 通行证 / 守卫 | Permission / Boundary Enforcement |
| 市政厅 | scoped Decision Rights / Governance |
| 探险 | Execution / Free Work Space |
| 探险报告 | Task Return |
| 检查站 / 评审台 / 选择台 | Review / Acceptance / Selection |
| 个人地图 / 世界地图 | HAU / Organizational Capability & Terrain |
| 小径 / 道路 / 桥梁 | Candidate / Reproduced Capability / Dependency |
| 图书馆 / 脉冲 | Knowledge / Knowledge Pulse |
| 徽章墙 / 功勋殿 | Achievement / Honor |
| 史册 | Event Graph |

## L3 Mechanism Taxonomy

Reality-to-World Projection；World State Rendering；Semantic View Switching；World Navigation；Task Discovery Projection；Terrain/Fog Rendering；Knowledge Pulse Projection；Authority/Boundary Projection；Value Memory Projection；Cross-view Deep Link。

## 全局与模块映射

世界首页提供城市鸟瞰；每个空间可下钻到模块页，再下钻到 Object、Event、Dependency 与 Evidence。模块页保持自己的 Mental Model，X1 只管理跨模块空间语法、视觉语义和体验连续性。

## 两条体验路径验证

### Path A — 新人第一次探险

`城市入口 → 酒馆理解 Goal/Task → 查看 Capability 提示 → Claim 生成 Execution → 携猎犬出村 → 遇 Boundary 请求通行 → Return → Review/Acceptance → 地图与徽章更新`。必须验证：Capability 不阻止领取、未知不被渲染为危险、每次 Execution 显示唯一 Human owner。

### Path B — 组织知识改变

`新 Evidence → 图书馆验证 → Knowledge 组件变更 → Event Graph 记史 → Dependency Graph 定位影响 → Materiality → Change Set → 相关道路/Agent/Policy 席位更新`。必须验证：不会全城警报、Knowledge 不自动改 Policy、Authority 不自动扩大。

## Panorama Topology

```text
City Overview
├─ Tavern → Goal / Task / Execution
├─ Gate & Outside → Work / Boundary / Risk
├─ Return Station → Review / Acceptance / Selection
├─ Map Room → Capability / Dependency
├─ Library → Knowledge / Pulse
├─ Hall → Contribution / Reward / Achievement / Honor
└─ City Hall & Chronicle → Governance / Policy / Audit / Event Graph
```

## Visual Specification

- **Scene/Space**：未知世界边缘持续扩张的新手村/城市；功能空间清楚、非主题乐园。
- **Objects**：见 Seed World Ontology；任何新增对象必须先绑定真实组织对象或机制。
- **Semantic Mapping**：世界对象可追溯到 canonical object/event/dependency；多个视角仅改变投影。
- **Behavior/State**：真实 Execution 消退迷雾，Knowledge 丰富图书馆，复现加固道路，Honor 才进入功勋殿。
- **禁止误读**：禁止假地图、假荣誉、假能力；禁止用游戏惯例推导 winner-takes-all、等级准入或无限权限。

