# AI-Native Organization

## GitHub 阅读入口

本仓库整理自 Obsidian 项目，保留原始讨论、研究文档、PNG 图片与可编辑 HTML。正文中的 `[[双链]]` 适合在 Obsidian 中阅读；GitHub 浏览可使用以下目录链接。

- [项目总览](00%20项目总览/)
- [组织协议](10%20组织协议/)
- [研究议题](20%20研究议题/)
- [原始讨论](80%20原始讨论/)
- [项目管理与版本状态](90%20项目管理/)
- [协议视觉图：8 套、73 张独立页面](00%20项目总览/视觉图/AI-Native%20组织协议图解%20v0.1/)

同步基线：2026-09-04。文字已纳入当日阶段设计；视觉图为此前生成版本，尚未完整覆盖最新组织记忆与行为治理机制。历史原文中的乱码、附件占位与证据缺口保留原状，不代表已无损恢复。

这是一次阶段快照，不是自动持续同步。冻结、已确认和待设计的具体边界以版本状态文档为准。

这是一个为期一年的实验型组织设计项目：约 60 名来自不同部门的应届生，在保留正式岗位与职责的同时，组成一个跨部门的第二组织，与多种 AI Agent 共同完成真实工作。

项目不把“员工使用更多 AI 工具”等同于 AI-Native。我们研究的是：当目标、任务、能力、证据、知识与反馈都能被 Human 和 Agent 共同读取、调度和更新时，组织能否获得更高效率、更强创新、更快学习、更高组织智能，同时维持人的成长与真实连接。

## 导航

- [[00 项目总览/项目背景与实验目标|项目背景与实验目标]]
- [[00 项目总览/总体设计原则|总体设计原则]]
- [[10 组织协议/Goal Protocol v0.1|Goal Protocol v0.1]]（冻结）
- [[10 组织协议/Task Protocol v0.1|Task Protocol v0.1]]（冻结）
- [[10 组织协议/Goal-Task 接口补丁 v0.1|Goal–Task 接口补丁 v0.1]]（冻结）
- [[10 组织协议/Operating Loop v0.2|Operating Loop v0.2]]（已确认）
- [[10 组织协议/Free Work Space Protocol v0.1|Free Work Space Protocol v0.1]]（冻结）
- [[10 组织协议/Time & Recovery Protocol v0.1|Time & Recovery Protocol v0.1]]（冻结）
- [[10 组织协议/Task Lease & Progress Protocol v0.1|Task Lease & Progress Protocol v0.1]]（冻结）
- [[10 组织协议/Review Protocol v0.1|Review Protocol v0.1]]（冻结）
- [[10 组织协议/Acceptance Protocol v0.1|Acceptance Protocol v0.1]]（冻结）
- [[10 组织协议/Audit Layer 待设计|Audit Layer]]（待设计）
- [[10 组织协议/Organization Runtime & Protocol OTA|Organization Runtime & Protocol OTA]]（核心架构已确认）
- [[10 组织协议/Organizational Learning & Knowledge Formation|Organizational Learning & Knowledge Formation]]（知识形成 v0.1 已冻结；行为治理未冻结）
- [[10 组织协议/Evidence Core Principles|Evidence Core Principles]]（核心定义与原则已确认）
- [[10 组织协议/Verification Protocol v0.1|Verification Protocol v0.1]]（冻结）
- [[10 组织协议/Generalization & Scope|Generalization / Scope]]（核心设计已完成，纳入 Knowledge Formation v0.1）
- [[20 研究议题/AI-Native Organization Fundamentals Backlog|Fundamentals 研究议题总索引]]
- [[90 项目管理/设计状态与版本|设计状态与版本]]
- [[90 项目管理/变更记录|变更记录]]
- [[00 项目总览/视觉图/AI-Native 组织协议图解 v0.1/使用说明|AI-Native 组织协议图解 v0.1]]（73 张小红书 3:4 页面）

## 当前主循环

```text
Goal Proposal → Active Goal → Decomposition → Task Proposal
  → Validation → Active Task → Task Bus → Pull / Push → Executor Unit
  → Free Work Space → Output + Evidence → Review（Quality + Learning）
  → Acceptance → Result → Knowledge / Evidence / Capability / New Task
  ↔ Organizational Memory（持续学习层）
```

完整主链及 Temporary Subtask 升级规则见 [[10 组织协议/Operating Loop v0.2|Operating Loop v0.2]]。

## 当前知识形成主干

```text
Raw Events → Organizational Attention Mechanism → Observation → Pattern
→ Hypothesis Cloud ⇄ Evidence ⇄ Verification
→ Generalization / Scope → Knowledge
→ Behavior Change → New Events
```

其中 [[10 组织协议/Verification Protocol v0.1|Verification Protocol v0.1]] 已冻结；[[10 组织协议/Generalization & Scope|Generalization / Scope]] 核心设计已完成并纳入 [[10 组织协议/Organizational Knowledge Formation Protocol v0.1|Organizational Knowledge Formation Protocol v0.1]]（冻结）。下一问题是 Knowledge→Behavior 由谁治理晋升。

## 版本原则

- Protocol 固定，Workflow 动态。
- 冻结表示已形成 v0.1 共识，不表示永远不变；只有真实运行证据才推动 v0.2。
- 研究问题与协议分离：未知问题进入研究议题，已确认的组织不变量进入协议。
- 本目录当前不受 Git 管理；项目 Git 版本源待明确，不宣称已同步 GitHub。日常浏览以指定 Obsidian 项目为载体。

## 当前基线入口（2026-09-04）

独立工作轨道首先读取 [[90 项目管理/DESIGN-ISSUE-001 基线入口]]，再读取 [[90 项目管理/设计状态与版本]] 和 [[90 项目管理/next-actions]]。

- [[10 组织协议/Organizational Knowledge Formation Protocol v0.1]]：v0.1 冻结。
- [[10 组织协议/organizational-memory|Organizational Memory]]：核心架构已形成 / Knowledge→Behavior 治理未冻结。
- [[10 组织协议/Knowledge to Behavior - Behavioral Authority]]：四级行为权威设计有效，晋升治理未冻结。
- [[10 组织协议/Agent Governance & Runtime]]：一级模块，骨架已确认，待详细设计。
- [[90 项目管理/DESIGN-ISSUE-001 基线同步裁决]]：Resolved — baseline sync gap, not protocol contradiction。

## 2026-09-04 阶段基线

[[设计状态与版本]] 为状态入口，[[阶段同步报告 2026-09-04]] 记录写入与证据缺口。

- [[organizational-memory]]
- [[Context Assembly v0.1]]
- [[Knowledge Consolidation & Salience v0.1]]
- [[Knowledge Intervention v0.1]]
- [[Knowledge Usage Feedback]]
- [[Knowledge Injection 与同步边界]]
- [[Agent Governance & Runtime]]
- [[Capability & Human Learning 待设计]]
- [[contribution-and-honor-wall]]
- [[Governance Audit Risk 待设计]]
- [[设计与开发轨道]]
