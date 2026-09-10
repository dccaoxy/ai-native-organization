# Current Development State

最后更新：2026-09-10。GitHub main 是 Development Source of Truth。

当前工程成果：**AD00 AutoDev v0 已跑通；M01 S01–S08 工程验收 PASS。**
当前 Stage：**S08 — Simulation + Audit + Final Acceptance Package**。
范围：Phase 2–3 / M0；真实实验尚未开始。

## 已完成及证据

- AD00：持久化 Stage Specs、有限重试/修复、独立进程 Review/Audit、Human Gate、Git commit/tag/artifact、断点恢复与非破坏回滚。
- M01：版本化契约、SQLite 事件现实、Human/HAU/Agent 绑定、Goal/Task/Execution、Boundary、正式 Return、Review/Acceptance/Selection、HTTP 与工作台。
- 完整本地套件执行 102 项测试通过；包含复用场景的累计测试，不代表 102 个互不重复的业务场景。
- M01 合成运行实际产生 42 条事件，通过 10 项最终断言；覆盖五类必过场景及 Agent/runtime interruption。无真实 Human 样本或 E01–E08 结论。
- 冻结文件与原始 Git 对象的摘要核验通过；L1/L2 未修改。
- 浏览器实际验证：合成身份/Goal 建立、发布、领取、ACK、工作台和事件同步。

证据：`autodev/M01.state.json`、`autodev/runs/`、`autodev/simulation/`、[M01 acceptance](M01_ACCEPTANCE.md)。
S04/v1 的依赖入库缺陷已由 S04/v2 修复；保留历史，不覆盖标签。

## 云端与外部状态

GitHub Actions runner 已配置：push / manual / 每 6 小时恢复；云端实测结果见 `autodev/DELIVERY.json`。
模型 Builder/Repair 未配置。云端可持续验证与推进准备好的 Stage，不能据此声称已在无人介入地编写后续 Milestone。
Obsidian Dashboard 只同步本仓库投影；同步回执见 `autodev/DELIVERY.json`。

## HUMAN DECISION REQUIRED

云端自动代码编写所需模型 provider/account、费用上限、仓库访问范围与 secret 配置尚未提供。
真实 Human Pilot、公司数据/Action、Residual Risk、奖金政策或 Frozen L1/L2 变更仍需单独 Human 决定。
以上未授权项目均未执行；不阻断已完成的 M01 合成工程验证。

## 尚未完成

- Phase 1 剩余概念 DEMO、完整下钻和 3–5 人理解测试。
- M02 / Phase 4 更大规模合成组织；M03 / M1 Learning Layer。
- Phase 6–8 真实组织部署与行为证据；Phase 9 的真实 Human、时间与实验。
- 当前 deterministic Review/Audit 不等同独立 Human/LLM 架构认证，也不表示 101 条 L2 的全部机制已实现。

## 无聊天接续

先读 AGENTS → 本页 → NEXT_ACTIONS → autodev/README → M01.json/M01.state.json。
Python 3.11+ / Git；`python -m unittest discover -s tests -v`；`python -m autodev.runtime run`。
工作台：`python -m organization.server`，仅 `http://127.0.0.1:8765` 合成模式。

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
| S08 Simulation + Audit + Final Acceptance Package | PASS | autodev/M01/S08/v2 |

Source: `development/autodev/M01.state.json`. Simulation evidence is not Human Pilot or E01–E08 evidence. Phase 9 requires real Humans, time and experimental results.
<!-- AUTODEV:END -->
