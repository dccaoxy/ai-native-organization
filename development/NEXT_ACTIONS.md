# Next Actions

最后更新：2026-09-08。这里是当前可执行动作的唯一权威列表；旧 `90 项目管理/next-actions.md` 仅保留为入口。

## Now — 只做这一项

1. **建立 M01 Engineering Specification 的第一版骨架并完成核心契约。**
   - 定义 Human、HAU、Representative Agent、Goal、Task、Execution、Boundary、Return/Result、Review、Acceptance 与 Organizational Event 的最小字段。
   - 定义 Task 与 Execution 状态机、允许的转换、失败/释放/返回路径。
   - 定义统一 Event Envelope，并列出 M01 每个状态变化必须产生的正式事件。
   - 定义每个动作的 Human Authority、Human Accountable Owner 与 Agent 权限。
   - 产物建议落在 `specs/objects/`、`specs/events/`、`specs/state-machines/`、`specs/interfaces/`；具体技术栈不在此步骤预设。

## Next — 完成 Now 后按序

2. 把 M01 场景写成可执行 acceptance scenarios：3 HAU、1 Goal、同一 Task、3 个独立 Execution，覆盖 Blocked、Boundary Request、Return、Review、Acceptance、Selection 与完整 Event Trail。
3. 选择满足规格的最小实现方式，记录技术决定；建立可运行骨架与持久化边界，不因框架选择改变 L1/L2。
4. 实现纵向薄切：Identity → Goal → Task Publish/Browse/Claim → Execution/ACK/Progress → Blocked/Boundary → Return → Review/Acceptance/Selection → Event Trail。
5. 自动验证成功、失败、Blocked、Boundary Extension、Parallel Result 五类情景，并更新 M01 验收矩阵。
6. 完成一次健康 checkpoint：测试通过、状态文件同步、Obsidian Dashboard 投影更新、另一位开发者可重建运行环境。

## Parallel but non-blocking

- 补齐 Phase 1 的 3–5 人理解测试与剩余视觉 DEMO；不得抢占 M01 核心规格和闭环。
- 准备 2–3 个真实任务与真实 Authority/Boundary 输入，供后续 Pilot 使用。

## 暂不做

- AI 推荐、Capability Match、动态赏金、复杂评分；
- Knowledge Pulse、Reward、Honor、Progression；
- 3D 世界与非必要视觉精修；
- Organization-owned Agent 自动执行；
- 未取得真实观测前对 E01–E08 作效果结论。

## 完成当前动作时必须同步

按顺序更新 [`CURRENT_STATE.md`](CURRENT_STATE.md) → 本文件 → [`MILESTONES.md`](MILESTONES.md) / 当前 Milestone → Obsidian `00 项目总览/项目 Dashboard.md`，再提交。

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
| S08 Simulation + Audit + Final Acceptance Package | CHECKPOINT_PENDING | autodev/M01/S08/v1 |

Source: `development/autodev/M01.state.json`. Simulation evidence is not Human Pilot or E01–E08 evidence. Phase 9 requires real Humans, time and experimental results.
<!-- AUTODEV:END -->
