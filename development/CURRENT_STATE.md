# Current Development State

## 2026-09-11 · AA02 联合工作台

当前用户授权优先项：AA02 Human × Agent 网页联合工作台，插入 M03 前。注册审批、任务/执行、边界决策、正式 Return 与分离验收页面已实现；136 项回归及实际 Edge 浏览器＋独立 Agent 进程联调通过（18 条合成事件，0 位真实 Human）。AA02 S01 本地 PASS：63d92f3 / autodev/AA02/S01/v1；验收及试用入口见 development/AA02_ACCEPTANCE.md。操作说明：development/milestones/AA02_HUMAN_AGENT_WORKSPACE.md。未推送、未部署；原域名项目不变。


最后更新：2026-09-10。GitHub main 是 Development Source of Truth。

最新授权：仅本地开发与隔离服务器测试，正式推送和部署需用户逐次确认；不改 AEGPC.CN 现有项目/服务。相关本地变更尚未推送。原自动写回 Actions 已暂停（API 核验 disabled_manually、无进行中任务），因此下述定时运行描述仅代表已实现能力，不代表当前正在运行。当前不采购海外实例。

当前工程成果：**AD00 AutoDev v0 已跑通；M01 S01–S08 工程验收 PASS。**
当前 Stage：**AA01 S03 — Agent access acceptance（本地 PASS）**。
Agent 注册/授权、独立客户端及实际模型内容生成联调已完成；完整套件 133 项通过，18 条合成事件。见 [AA01 验收包](AA01_ACCEPTANCE.md)。未新增生产服务或 Human 网页；下一工程 M03/M1 规格。
本地进展：M02 S01–S04 已按声明范围完成合成工程验收，均生成本地 commit/tag/artifact；尚未推送，未部署。见 [M02 验收包](M02_ACCEPTANCE.md)。
范围：Phase 4 / M0；不代表完整 Goal 生命周期、生产容量或真人实验已完成。

## M02 本地验收（尚未发布）

- 10 HAU、3 Goal、30 Task、60 Execution；加入 Goal Challenge 后实际产生 536 条合成事件，16 项规模/恢复断言通过。531 条是 S01 历史运行。
- 并发检查：8 个线程提交 20 个独立领取，Execution 与 Human owner 保持独立；24 次重复请求仅写入一次。冲突幂等键和跨 Task Selection 均被拒绝且不新增事件。
- 完整本地套件 122 项执行通过。历史 M01 的证据与标签保留。
- S01：`e940a5a` / `autodev/M02/S01/v1`；S02：`4bcc8cb` / `autodev/M02/S02/v1`。
- S03：`b48b68b` / `autodev/M02/S03/v1`；S04：`02b5d6c` / `autodev/M02/S04/v1`。证据：`autodev/M02.state.json`、`autodev/runs/M02/`、`autodev/m02-final/report.json`。
- 本机工作台已实际验证质疑、Human 修改、v0→v1、差异/证据/影响记录。仅支持 Keep 与两个文本组件 Modify；完整生命周期/依赖图仍为后续工程。
- 下一步准备 M03/M1 可追溯学习层规格。任何推送/部署仍先交付决策包并取得用户确认。

## 已完成及证据

- AD00：持久化 Stage Specs、有限重试/修复、独立进程 Review/Audit、Human Gate、Git commit/tag/artifact、断点恢复与非破坏回滚。
- M01：版本化契约、SQLite 事件现实、Human/HAU/Agent 绑定、Goal/Task/Execution、Boundary、正式 Return、Review/Acceptance/Selection、HTTP 与工作台。
- 完整本地套件执行 107 项测试通过；包含复用场景的累计测试，不代表 107 个互不重复的业务场景。
- ChatGPT 登录的 Codex adapter 已通过真实隔离测试：生成文件、测试/Review/Audit、checkpoint、自动进入 Human Gate、幂等恢复。见 `autodev/CODEX_SMOKE.json`；该 fixture 不代表新的 M01 Stage 验收。
- M01 合成运行实际产生 42 条事件，通过 10 项最终断言；覆盖五类必过场景及 Agent/runtime interruption。无真实 Human 样本或 E01–E08 结论。
- 冻结文件与原始 Git 对象的摘要核验通过；L1/L2 未修改。
- 浏览器实际验证：合成身份/Goal 建立、发布、领取、ACK、工作台和事件同步。
- Interactive Atlas Concept Demo v0.1 已实现同一合成 Execution 的 World / Architecture / Knowledge / Authority / Value 五视图投影；完整 L2/L3、对象历史与依赖下钻仍待实现。

证据：`autodev/M01.state.json`、`autodev/runs/`、`autodev/simulation/`、[M01 acceptance](M01_ACCEPTANCE.md)。
S04/v1 的依赖入库缺陷已由 S04/v2 修复；保留历史，不覆盖标签。

## 云端与外部状态

GitHub Actions runner 已配置：push / manual / 每 6 小时恢复；云端实测结果见 `autodev/DELIVERY.json`。
模型 Builder/Repair adapter 已实现并完成本机真实 Build 验证，尚未部署到云端或绑定新的正式 Milestone。云端可持续验证与推进准备好的 Stage，不能据此声称已在无人介入地编写后续 Milestone。
Obsidian Dashboard 只同步本仓库投影；同步回执见 `autodev/DELIVERY.json`。

## HUMAN DECISION REQUIRED

2026-09-10 用户已选择 ChatGPT 登录的 Codex，暂不设置额外资源上限，并授权 `dccaoxy/ai-native-organization` 全部仓库权限；不再等待这三项决定。平台配额仍适用。
本机 CLI 和真实模型调用已核验。仓库 API 确认为 public；官方账户登录 CI 方案不支持公开仓库，不能直接接入现有 Actions。云端仍缺明确的可信运行主机/私有执行环境与该环境登录，状态为 `AUTHORIZED_PENDING_PROVISIONING`；部署包见 `autodev/CODEX_RUNNER.md`。
用户提供的 AEGPC.CN 阿里云主机已通过只读 SSH 核查，元数据确认为北京区；不在 ChatGPT 官方支持地域内，不选作直接模型节点。网站可保留在现有主机；仍需支持地区的执行环境。未改服务器、未复制账户凭据。本次代码云端验证通过：[34444419116](https://github.com/dccaoxy/ai-native-organization/actions/runs/34444419116)。
真实 Human Pilot、公司数据/Action、Residual Risk、奖金政策或 Frozen L1/L2 变更仍需单独 Human 决定。
以上未授权项目均未执行；不阻断已完成的 M01 合成工程验证。

## 尚未完成

- Phase 1 剩余概念 DEMO、完整下钻和 3–5 人理解测试。
- 超出 M02 声明覆盖范围的组织规模验证；M03 / M1 Learning Layer。
- Phase 6–8 真实组织部署与行为证据；Phase 9 的真实 Human、时间与实验。
- 当前 deterministic Review/Audit 不等同独立 Human/LLM 架构认证，也不表示 101 条 L2 的全部机制已实现。

## 无聊天接续

先读 AGENTS → 本页 → NEXT_ACTIONS → AA01_ACCEPTANCE → autodev/README → AA01.json/AA01.state.json；M01/M02 状态为历史依据。
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
| S08 Simulation + Audit + Final Acceptance Package | PASS | autodev/M01/S08/v3 |

Source: `development/autodev/M01.state.json`. Simulation evidence is not Human Pilot or E01–E08 evidence. Phase 9 requires real Humans, time and experimental results.
<!-- AUTODEV:END -->
