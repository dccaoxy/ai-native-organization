# AutoDev Dashboard

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
