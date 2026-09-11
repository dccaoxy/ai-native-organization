# AI-Native Organization 开发接续入口

## 当前：M03 最小可追溯学习闭环

2026-09-11 用户已确认开发 M03。先读 development/milestones/M03_LEARNING_ORGANIZATION.md 与 development/autodev/M03.state.json；S01–S04 已本地 PASS，152 项测试通过，实际浏览器＋独立 Agent 跨任务复用产生 38 条合成事件；见 development/M03_ACCEPTANCE.md。范围为 Evidence 关系/快照、独立验证的有界 Knowledge 版本、授权复用和 Capability 候选/复现/重验信号。不是完整学习组织或真实效果验证；未推送/部署。下一步试用可追溯来源链并补充反证/版本变化的复验体验，暂不跳入 Human Pilot。

## 2026-09-11 · AA02 联合工作台

当前用户授权优先项：AA02 Human × Agent 网页联合工作台，插入 M03 前。注册审批、任务/执行、边界决策、正式 Return 与分离验收页面已实现；136 项回归及实际 Edge 浏览器＋独立 Agent 进程联调通过（18 条合成事件，0 位真实 Human）。AA02 S01 本地 PASS：63d92f3 / autodev/AA02/S01/v1；验收及试用入口见 development/AA02_ACCEPTANCE.md。操作说明：development/milestones/AA02_HUMAN_AGENT_WORKSPACE.md。未推送、未部署；原域名项目不变。


本文件是任何新 Human、Work、Codex 或 Agent 进入本仓库时的第一入口。开发者不得依赖上一段聊天上下文；应从仓库现实重建上下文。

## 启动顺序

1. 阅读 [`development/CURRENT_STATE.md`](development/CURRENT_STATE.md)，确认当前阶段、Milestone、已完成项与阻碍。
2. 阅读 [`development/NEXT_ACTIONS.md`](development/NEXT_ACTIONS.md)，只从最高优先级的未完成动作开始。
3. 阅读最新完成的 Agent 接入规格 `development/milestones/AA01_AGENT_ACCESS.md` 和验收包，再按 NEXT_ACTIONS 进入下一工程；原 M01 规格：[`development/milestones/M01_MINIMUM_ORGANIZATION.md`](development/milestones/M01_MINIMUM_ORGANIZATION.md)。
4. 按需读取 [`development/ROADMAP.md`](development/ROADMAP.md) 与设计入口；不要默认通读全部历史讨论。
5. 开发前检查工作树与最近提交；开发后运行与变更风险相称的验证。

## 不可擅自改变的边界

- [`Operating Model v0.1 Final Design Baseline`](00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) 是当前设计权威。
- L1/L2、Task ≠ Execution、唯一 Human Accountability、Free Work Space、Boundary/Escalation、正式 Return、Review/Acceptance 与 Organizational Event 等冻结语义，不得因实现便利被静默改写。
- [`Frozen / Tunable / Experimental`](90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Freeze%20Classification%20v0.1.md) 是设计确定性维度；M0/M1/M2 是实现优先级；运行/验证状态另列，三者不可混用。
- Tunable 项可通过明确配置调整，但必须记录默认值、依据和变更事件；Experimental 项只能形成假设和测量设计，不能伪造验证结果。
- 新证据若挑战冻结原则，先记录 Evidence / Hypothesis / Change Proposal，并请求 Human 裁决；不要直接改基线。

## 当前开发原则

### 最新用户授权（2026-09-10，优先于此前全部仓库权限）

- 当前只做自己的开发和隔离服务器测试，服务面向中国大陆；不自行开通海外资源或更换模型账户。
- 不改 AEGPC.CN 现有项目、域名入口、Nginx、生产服务或生产数据。
- 正式 Git 推送、上线部署、恢复自动写回工作流前，必须先提交具体变更、验证和回滚说明，并取得用户确认。之前的全仓库权限不代表后续推送/部署免确认。
- 本地开发、验证和隔离测试可继续；服务器测试须独立目录/端口，不绑定正式域名，不影响既有服务。
- AutoDev durable runner 已通过 GitHub API 暂停并验证为 disabled_manually，无进行中任务；未获确认前不重新启用。

> **Build the loop before building the intelligence.** 先把闭环建起来，再给闭环增加智能。

> **Capture before optimize.** 先保证组织事实能够正确留下，再优化推荐、评分和自动化。

当前本地工程 AA01 Agent 接入 S01–S03 已 PASS，完整测试 133 项，真实模型辅助协议测试 18 条合成事件；见 development/AA01_ACCEPTANCE.md。M02 S01–S04 已在声明范围通过；下一工程是 M03/M1 规格。Goal 全生命周期与多 Goal 依赖图仍待实现。不要优先开发 3D 地图、复杂推荐、Reward、Honor、Progression 或 Organization-owned Agent。

## AD00 / AutoDev 接续

- 层级：Phase 0–9 = 生命周期；M0/M1/M2 = 实现成熟度与 Scope；Milestone = 独立工程成果；Stage = Milestone 内自动推进单元。
- 先读 `development/autodev/README.md`、`M01.json` 和 `M01.state.json`（若存在），再看当前 Stage 的运行证据；不能从聊天推断 PASS。
- 工程使命覆盖到 Phase 8；Phase 9 不能由 AutoDev 自动完成，须真实 Human、时间及实验结果。
- Build/Test、独立进程反证 Review、Principle Audit 逻辑分离；新内容必须重新验证，不复用不匹配摘要的审查。
- 默认在明确边界内自动推进；工程失败记为 BLOCKED_ENGINEERING。只有 Purpose/Authority/Risk、真实外部数据/权限或冻结 L1/L2 变更才记 HUMAN_DECISION_REQUIRED。
- 每个 PASS Stage 有 commit、不可覆盖的 annotated tag、artifact 与可恢复状态。不得 force-push、reset 历史或自动操作真实公司系统。
- 当前内置 reviewer/auditor 为确定性独立校验，不宣称已经获得独立 Human/LLM 审查。通用模型 Builder/Repair 需另行配置，不假定桌面登录等同云端凭据。
- `autodev.codex_adapter` 已完成本机真实模型 smoke；接入规范见 `development/autodev/CODEX_RUNNER.md`。模型提案仅能写入显式 model_write_paths 与 scope 的交集，不得自动解除 model_gate。仓库已核验为 public，不将 ChatGPT 账户凭据接入本公开仓库的 Actions；云端主机尚待配置。

## 事实源与同步

- **GitHub 是 Development Source of Truth**：代码、规格、测试、技术决策、Milestone、当前状态和下一步均以本仓库为准。
- **Obsidian 是 Project Command Center / Human Dashboard**：展示整个项目进程与设计、实验、开发轨道的 Human View，不形成第二套开发事实源。
- 每个正式 checkpoint 必须按顺序更新：代码/规格与测试 → `development/CURRENT_STATE.md` → `development/NEXT_ACTIONS.md` → 当前 Milestone → Obsidian Dashboard。
- 若 GitHub 与 Obsidian 状态冲突，以 GitHub 为准，并修正 Dashboard 投影。

## Checkpoint 完成标准

一个 checkpoint 只有在另一位开发者能够无聊天上下文接续时才完成。提交前确认：

- 变更没有越过冻结设计边界；
- 实现、测试与文档状态一致；
- `CURRENT_STATE`、`NEXT_ACTIONS` 和当前 Milestone 已同步；
- 未填写模拟实验数据或未验证结论；
- 内部链接有效，工作树只包含本次相关修改；
- 提交说明清楚表达范围，例如 `docs(development): establish M01 handoff baseline`。

遇到权限、数据、真实 Human Authority、公司平台边界或会改变冻结设计的决定时，停止相关实现并向 Human 报告；可继续推进不受该决定影响的工作。
