# AutoDev Dashboard

## 当前：M03 最小可追溯学习闭环

2026-09-11 用户已确认开发 M03。先读 development/milestones/M03_LEARNING_ORGANIZATION.md 与 development/autodev/M03.state.json；S01–S04 验收正在推进，PASS 以持久状态和提交为准。范围为 Evidence 关系/快照、独立验证的有界 Knowledge 版本、授权复用和 Capability 候选/复现/重验信号。不是完整学习组织或真实效果验证；未推送/部署。下一步完成本地验收并安排用户试用，暂不跳入 Human Pilot。

## 2026-09-11 · AA02 联合工作台

当前用户授权优先项：AA02 Human × Agent 网页联合工作台，插入 M03 前。注册审批、任务/执行、边界决策、正式 Return 与分离验收页面已实现；136 项回归及实际 Edge 浏览器＋独立 Agent 进程联调通过（18 条合成事件，0 位真实 Human）。AA02 S01 本地 PASS：63d92f3 / autodev/AA02/S01/v1；验收及试用入口见 development/AA02_ACCEPTANCE.md。操作说明：development/milestones/AA02_HUMAN_AGENT_WORKSPACE.md。未推送、未部署；原域名项目不变。


## 当前：AA01 Agent 接入本地 PASS

S01–S03 已形成本地 commit/tag/artifact；完整套件 133 项通过。独立客户端与真实模型内容生成联调通过，18 条合成事件、0 位真实 Human。见 [验收包](../AA01_ACCEPTANCE.md)。无新增审批网页或常驻线上服务；下一工程 M03/M1 规格。尚未推送/部署，云端写回保持暂停。

## 本地待发布进展（2026-09-10）

M02 S01–S04 已按声明范围本地 PASS；122 项测试通过，整合运行 536 条合成事件。
四个本地标签 `autodev/M02/S01/v1` 至 `autodev/M02/S04/v1`，证据见 `M02.state.json`。
Goal Challenge 页面已验证；完整生命周期/依赖图仍未实现。下一步准备 M03/M1 规格。未推送、未部署；云端自动写回保持暂停，现有域名项目未改动。
以下 M01 历史表格不代表当前工程阶段。

2026-09-10：Codex 真实模型提案 → 测试/独立校验 → checkpoint → 下一阶段 Gate → 恢复测试通过。完整本地套件 107 项通过。云端模型主机尚待明确与登录；公开仓库不启用账户登录 CI。详见 [接入包](CODEX_RUNNER.md) 和 [真实测试回执](CODEX_SMOKE.json)。

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
