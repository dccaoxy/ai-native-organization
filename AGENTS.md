# AI-Native Organization 开发接续入口

本文件是任何新 Human、Work、Codex 或 Agent 进入本仓库时的第一入口。开发者不得依赖上一段聊天上下文；应从仓库现实重建上下文。

## 启动顺序

1. 阅读 [`development/CURRENT_STATE.md`](development/CURRENT_STATE.md)，确认当前阶段、Milestone、已完成项与阻碍。
2. 阅读 [`development/NEXT_ACTIONS.md`](development/NEXT_ACTIONS.md)，只从最高优先级的未完成动作开始。
3. 阅读当前 Milestone 规格：[`development/milestones/M01_MINIMUM_ORGANIZATION.md`](development/milestones/M01_MINIMUM_ORGANIZATION.md)。
4. 按需读取 [`development/ROADMAP.md`](development/ROADMAP.md) 与设计入口；不要默认通读全部历史讨论。
5. 开发前检查工作树与最近提交；开发后运行与变更风险相称的验证。

## 不可擅自改变的边界

- [`Operating Model v0.1 Final Design Baseline`](00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) 是当前设计权威。
- L1/L2、Task ≠ Execution、唯一 Human Accountability、Free Work Space、Boundary/Escalation、正式 Return、Review/Acceptance 与 Organizational Event 等冻结语义，不得因实现便利被静默改写。
- [`Frozen / Tunable / Experimental`](90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Freeze%20Classification%20v0.1.md) 是设计确定性维度；M0/M1/M2 是实现优先级；运行/验证状态另列，三者不可混用。
- Tunable 项可通过明确配置调整，但必须记录默认值、依据和变更事件；Experimental 项只能形成假设和测量设计，不能伪造验证结果。
- 新证据若挑战冻结原则，先记录 Evidence / Hypothesis / Change Proposal，并请求 Human 裁决；不要直接改基线。

## 当前开发原则

> **Build the loop before building the intelligence.** 先把闭环建起来，再给闭环增加智能。

> **Capture before optimize.** 先保证组织事实能够正确留下，再优化推荐、评分和自动化。

当前是 P0 / M01。除非 M01 需要，不要优先开发 3D 地图、复杂推荐、Knowledge Pulse、Reward、Honor、Progression 或 Organization-owned Agent。

## AD00 / AutoDev 接续

- 层级：Phase 0–9 = 生命周期；M0/M1/M2 = 实现成熟度与 Scope；Milestone = 独立工程成果；Stage = Milestone 内自动推进单元。
- 先读 `development/autodev/README.md`、`M01.json` 和 `M01.state.json`（若存在），再看当前 Stage 的运行证据；不能从聊天推断 PASS。
- 工程使命覆盖到 Phase 8；Phase 9 不能由 AutoDev 自动完成，须真实 Human、时间及实验结果。
- Build/Test、独立进程反证 Review、Principle Audit 逻辑分离；新内容必须重新验证，不复用不匹配摘要的审查。
- 默认在明确边界内自动推进；工程失败记为 BLOCKED_ENGINEERING。只有 Purpose/Authority/Risk、真实外部数据/权限或冻结 L1/L2 变更才记 HUMAN_DECISION_REQUIRED。
- 每个 PASS Stage 有 commit、不可覆盖的 annotated tag、artifact 与可恢复状态。不得 force-push、reset 历史或自动操作真实公司系统。
- 当前内置 reviewer/auditor 为确定性独立校验，不宣称已经获得独立 Human/LLM 审查。通用模型 Builder/Repair 需另行配置，不假定桌面登录等同云端凭据。

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
