# M01 — Minimum Organization

状态：**Current / Engineering Specification not started**

优先级：**P0**

对应阶段：**Phase 2–3**

设计依据：[`Minimum Viable Organization v0.1`](../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Minimum%20Viable%20Organization%20v0.1.md)

## Outcome

让 3 个 HAU 围绕 1 个 Goal，在 Task Wall 上竞争领取同一个 Task，形成 3 个相互独立的 Execution；其中至少一次经历 Blocked 与 Boundary Request，最终完成 Return → Review → Acceptance → Selection，并留下完整 Organizational Event Trail。

这不是静态 UI 演示。场景必须由真实状态变化驱动，并可重复验证。

## 必须保持的语义

- Human、Representative Agent 与 HAU 身份关系明确；每个 Execution 创建时解析唯一 Human Accountable Owner。
- Goal 先于正式 Task，且表达 Desired Change、Success Criteria、Boundary、Human Goal Authority 与 Status。
- Task 是共享 intent / contract；Execution 是一次独立 attempt。三次 Claim 不能覆盖或合并为一个 Execution。
- Claim 后必须 ACK；执行期间允许 Progress、Blocked、Need Help / Escalate、Submit、Fail、Release，任务不能静默消失。
- Free Work Space 不要求中央系统捕获全部私有过程，只捕获必要状态与正式 Return。
- 越过 Boundary 必须形成请求并路由给真实 Human Authority；批准、拒绝或修改都留下正式事件。
- 成功与失败都提交结构化 Return，至少包含 Result、Observed Terrain、Major Execution Facts 与 Reflection，并允许 Human Confirm / Correct / Add。
- Review 判断可信性，Acceptance 判断是否满足用途；多个合格 Result 之间进行 Selection。
- 所有改变组织现实的动作进入统一 Event Trail。

## 最小场景

1. Human H1–H3 分别与 Representative Agent 绑定，形成 HAU-1–HAU-3。
2. Human Goal Authority 激活 Goal G1。
3. G1 下创建并发布 Task T1 到 Task Wall。
4. 三个 HAU 分别 Claim T1，系统创建 E1、E2、E3，并各自绑定唯一 Human Accountable Owner。
5. E1–E3 ACK；至少一个 Execution 报告 Progress。
6. 至少一个 Execution 进入 Blocked 并提交 Boundary Request；Human Authority 明确批准、拒绝或修改边界后恢复或结束。
7. 三个 Execution 分别以成功或失败状态提交正式 Return；失败不得无 Return 关闭。
8. Reviewer 对 Result 做 Review；Acceptor 做 Acceptance。
9. 若多个 Result 被接受，Selector 进行 Selection；未被选中不抹除其 Execution 与学习证据。
10. Event Trail 能按时间重建 G1、T1、E1–E3 的完整变化与责任链。

## Phase 2 交付物

- [ ] Core Object Schemas
- [ ] Task / Execution State Machines
- [ ] Organizational Event Envelope + M01 Event Catalog
- [ ] Authority / Accountability Matrix
- [ ] API / Agent Interface Contracts
- [ ] 最小页面与组件边界
- [ ] Tunable Parameter Register（仅登记，不假装已验证默认值）
- [ ] Acceptance Scenarios 与追溯矩阵

## Phase 3 交付物

- [ ] 可运行的最小应用与持久化
- [ ] Identity / Binding
- [ ] Goal activation
- [ ] Task Wall：Publish / Browse / Claim
- [ ] 独立 Execution：ACK / Progress / Blocked / Escalate / Submit / Fail / Release
- [ ] Boundary Request 与 Human Authority 决定
- [ ] Task Return
- [ ] Review / Acceptance / Selection
- [ ] 可查询的 Organizational Event Trail
- [ ] 自动化测试与本地运行说明

## 必过验收

| Scenario | 预期 |
|---|---|
| Success | Execution 提交、Review、Acceptance 并关闭，事件完整 |
| Failure | 失败有正式 Return、责任与事件，不静默消失 |
| Blocked | 可见、可求助/升级、可恢复或正式结束 |
| Boundary Extension | 由正确 Human Authority 决定并留下变更事件 |
| Parallel Result | 同一 Task 的 Execution 独立，支持分别 Review/Acceptance 与最终 Selection |

## 非目标

- AI 推荐、Capability Match、动态赏金或自动派工；
- 复杂 Knowledge、Capability、Contribution、Reward、Honor 或 Progression；
- 3D 地图与视觉精修；
- 60 人规模、生产级集成或真实实验结论。

## 完成定义

M01 只有在上述五类场景可重复运行、自动检查通过、事件可重建、冻结语义未被改写，且 `CURRENT_STATE`、`NEXT_ACTIONS`、本文件与 Obsidian Dashboard 已同步后才可标记 Complete。

<!-- AUTODEV:START -->
## AutoDev repository projection

| Stage | Status | Checkpoint tag |
|---|---|---|
| S01 Specification Freeze | PASS | autodev/M01/S01/v1 |
| S02 Reality Foundation | BLOCKED_ENGINEERING |  |
| S03 Goal + Task + Execution Core | PENDING |  |
| S04 HAU + Representative Agent + Runtime | PENDING |  |
| S05 Free Work Space + Progress + Boundary/Escalation | PENDING |  |
| S06 Return + Review + Acceptance + Selection | PENDING |  |
| S07 End-to-End Integration | PENDING |  |
| S08 Simulation + Audit + Final Acceptance Package | PENDING |  |

Source: `development/autodev/M01.state.json`. Simulation evidence is not Human Pilot or E01–E08 evidence. Phase 9 requires real Humans, time and experimental results.
<!-- AUTODEV:END -->
