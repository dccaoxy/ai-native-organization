# Development Milestones

## 2026-09-11 · AA02 联合工作台

当前用户授权优先项：AA02 Human × Agent 网页联合工作台，插入 M03 前。注册审批、任务/执行、边界决策、正式 Return 与分离验收页面已实现；136 项回归及实际 Edge 浏览器＋独立 Agent 进程联调通过（18 条合成事件，0 位真实 Human）。AA02 S01 本地 PASS：63d92f3 / autodev/AA02/S01/v1；验收及试用入口见 development/AA02_ACCEPTANCE.md。操作说明：development/milestones/AA02_HUMAN_AGENT_WORKSPACE.md。未推送、未部署；原域名项目不变。


最后更新：2026-09-10。

| Milestone | Priority / Phase | 状态 | Outcome |
|---|---|---|---|
| M00 — Design Handoff | P0 / Phase 0 | Complete | 冻结设计、文档与视觉语义可被新开发者接续 |
| AD00 — Autonomous Development Runtime | Cross-phase through Phase 8 | **Harness + local Codex smoke PASS / Cloud host pending** | 持久状态、独立校验、恢复、检查点及真实模型提案验证 |
| M01 — Minimum Organization | P0 / Phase 2–3 | **Complete — M0 simulation engineering; delivery verified** | 3 HAU 围绕 1 Goal 跑通多 Execution 的完整 M0 闭环 |
| M02 — Synthetic Organization | P1 / Phase 4 | Local S01–S04 PASS within declared coverage; not pushed/deployed | 60 Execution / 536 事件；Goal Challenge、并发/恢复与本机工作台验证；见 M02_ACCEPTANCE |
| AA01 — Independent Agent Access | P1 / Phase 4, M0 | Local S01–S03 PASS; not pushed/deployed | 注册/受控授权/独立客户端；133 项测试及模型辅助协议联调；见 AA01_ACCEPTANCE |
| M03 — Learning Organization | P1 / Phase 5 | Planned | Execution → Evidence → Knowledge → Capability 可追溯闭环 |
| M04 — Human Pilot | P2 / Phase 6 | Planned | 5–10 人、2–4 Cycle 的真实行为基线 |
| M05 — Value & Culture | P2 / Phase 7 | Planned | Contribution → Reward / Honor 的可验证机制 |
| M06 — Bounded Automation | P3 / Phase 8 | Planned | 低风险、可复现能力的 Organization-owned Agent 执行 |
| M07 — 60-person Experiment | P3 / Phase 9 | Planned | 约 60 人一年实验与 E01–E08 研究运行 |

状态词只描述实现进度，不替代 Frozen/Tunable/Experimental 或 M0/M1/M2 分类。

## 当前 Milestone

[`AA01 — Independent Agent Access`](milestones/AA01_AGENT_ACCESS.md) 已完成本地验收；下一工程 M03 规格。

Milestone 只有在定义的 Outcome、验收情景、证据和接续条件全部满足时才能标记 Complete；文档存在不等于实现完成。

<!-- AUTODEV:START -->
## AutoDev repository projection

| Stage | Status | Checkpoint tag |
|---|---|---|
| S01 Specification Freeze | PASS | autodev/M01/S01/v1 |
| S02 Reality Foundation | PASS | autodev/M01/S02/v1 |
| S03 Goal + Task + Execution Core | PASS | autodev/M01/S03/v1 |
| S04 HAU + Representative Agent + Runtime | PASS | autodev/M01/S04/v2 |
| S05 Free Work Space + Progress + Boundary/Escalation | PASS | autodev/M01/S05/v1 |
| S06 Return + Review + Acceptance + Selection | PASS | autodev/M01/S06/v1 |
| S07 End-to-End Integration | PASS | autodev/M01/S07/v1 |
| S08 Simulation + Audit + Final Acceptance Package | PASS | autodev/M01/S08/v3 |

Source: `development/autodev/M01.state.json`. Simulation evidence is not Human Pilot or E01–E08 evidence. Phase 9 requires real Humans, time and experimental results.
<!-- AUTODEV:END -->
