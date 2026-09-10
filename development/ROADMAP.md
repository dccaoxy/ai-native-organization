# Development Roadmap v0.1

状态复核：2026-09-10。路线把已冻结的 Operating Model 转化为开发顺序，不改变其设计原则。

## 总目标与实施原则

第一阶段完成三次跃迁：**设计能被理解 → 组织能运行 → 组织能学习**。

> **Build the loop before building the intelligence.**

> **Capture before optimize.**

先建立可运行、可审计、可恢复的组织闭环及其事实记录，再增加推荐、评分、自动化和视觉复杂度。真实行为出现前，不优化实验机制。

## 优先级

| Priority | 范围 | 结果 |
|---|---|---|
| P0 | Phase 0–3 | 理解 → 工程规格 → M0 闭环 |
| P1 | Phase 4–5 | Simulation → Learning / Capability |
| P2 | Phase 6–7 | Human Pilot → Value / Culture |
| P3 | Phase 8–9 | Automation → 60 人规模 |

## Phase 0 — Design Handoff

**目标：** 新开发者无需重读完整讨论即可正确理解系统。

**交付：** Final Baseline、11+1 L1、L2 Principle Tree、L3 Taxonomy、Reality Layer、01–08、X1、Freeze Classification、M0/M1/M2、Experiment Backlog、World Visual Bible、Panorama 与 Glossary。

**状态：** 已完成。设计已冻结不等于参数已定、系统已上线或实验已验证。

## Phase 1 — Visual Comprehension Prototype

**目标：** 验证第三方能否通过 World Model 与 Atlas 快速理解 Operating Model。

**范围：** 7 个概念 DEMO 与 Interactive HTML Atlas；它们是理解层，不创造底层规则。

**状态：** 进行中。Atlas v0.1、DEMO-01 新手村鸟瞰、DEMO-02 赏金酒馆任务墙已完成；其余 DEMO、完整下钻与 3–5 人理解测试未完成。

**退出标准：** 3–5 名未参与者能准确复述 HAU、Parallel Execution、Fog ≠ Risk、Free Work Space 与 Knowledge → Capability。

## Phase 2 — M0 Engineering Specification

**目标：** 把自然语言 Operating Model 转成无须临场解释的工程规格。

**范围：** Human、HAU、Representative Agent、Goal、Task、Execution、Result、Review、Acceptance、Boundary、Organizational Event 的 Object Schema；状态机；Event Envelope；Authority / Accountability；API / Agent Interface；页面与组件边界；Tunable 参数登记。

**状态：** M01 S01 契约已通过工程验收；见 development/M01_ACCEPTANCE.md。

**退出标准：** 开发者无需从历史讨论自行推断字段、状态变化、权限与正式事件。

## Phase 3 — M0 End-to-End Prototype

**目标：** 让最小组织第一次真实闭环。

**范围：** 见 [`milestones/M01_MINIMUM_ORGANIZATION.md`](milestones/M01_MINIMUM_ORGANIZATION.md)。核心是 Task ≠ Execution、Parallel Execution、Human Accountability、ACK/Progress、Blocked/Boundary、Free Work Space、Return、Review/Acceptance/Selection 与完整 Event Trail。

**退出标准：** 成功、失败、Blocked、Boundary Extension、Parallel Result 均能正确闭环，且另一位开发者可从仓库断点复现。

## Phase 4 — Simulation

**目标：** 以合成组织压力测试运行语义，不把模拟结果冒充真实实验数据。

**范围：** 约 10 个模拟 HAU、3 个 Goal、30 个 Task、50–100 个 Execution；覆盖并行领取、失败、脏数据、能力缺口、边界扩展、Agent 掉线与 Goal Challenge。

**退出标准：** Event、Accountability、任务存活性与状态机无已知阻断缺陷。

## Phase 5 — M1 Learning Layer

**目标：** 形成 Execution → Learning → Organizational Capability 闭环。

**顺序：** Experience/Evidence → Knowledge Formation → Knowledge Activation → Capability Evidence/Map → Capability Capture → Reproduction → Dependency Graph → Contribution Ledger。

**退出标准：** 一次执行的证据可被追溯、挑战、激活，并支持另一支 HAU 的能力复现尝试。

## Phase 6 — Human Pilot

**目标：** 5–10 名 Human + Representative Agent 运行 2–4 个 Cycle，取得可解释的真实行为基线。

**要求：** 不频繁改规则；所有重要 Product / Policy 变化记录为 Event；不制造实测数据。

**退出标准：** E01–E08 获得足以判断下一轮干预的基线证据，并明确数据、权限与伦理边界。

## Phase 7 — Value & Culture Layer

**目标：** 在真实 Contribution 数据基础上测试组织价值形成。

**顺序：** Contribution Ledger → Blind Event Valuation → Scarcity/Saturation → Reward Pool → Honor Candidate → Honor Hall → Badge/Achievement。Progression 暂缓，等待证据。

## Phase 8 — Organizational Automation

**目标：** 将可复现、低监督、低风险且易恢复的组织能力交给 Organization-owned Agent。

**门槛：** Capability 已捕获、复现和重新验证；Boundary/Risk 清晰；Human 仍是 Accountability 终点。

## Phase 9 — Scale to 60

**目标：** 进入约 60 人、为期一年的正式实验，把系统作为 Research Instrument 运行 E01–E08，而非继续无边界堆功能。

## 路线治理

- 当前状态只在 [`CURRENT_STATE.md`](CURRENT_STATE.md) 更新；具体行动只在 [`NEXT_ACTIONS.md`](NEXT_ACTIONS.md) 更新。
- Milestone 定义与门槛见 [`MILESTONES.md`](MILESTONES.md)。
- 后续 Phase 可以因证据调整顺序，但任何调整不得静默修改冻结设计，且必须留下明确开发决策与变更事件。

## AD00 自动开发范围与层级

Phase 0–9 = 项目生命周期；M0/M1/M2 = 实现成熟度/Scope；Milestone = 独立工程成果；Stage = AutoDev 自动推进单元。
AD00 工程使命覆盖当前基线至 Phase 8。M01 S01–S08 的 M0 原型已完成合成工程验证。
Phase 9 必须由真实 Human、真实时间和实验结果支持，不能被 AutoDev 自动完成。
软件 Stage 的 AUTO/CONDITIONED AUTO 不代替 Human Purpose/Authority/Risk、真实数据/外部权限与冻结 L1/L2 变更的决定。
