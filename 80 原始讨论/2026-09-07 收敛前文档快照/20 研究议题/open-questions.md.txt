---
type: project-open-questions
status: active
project: AI-Native Organization
reviewed: 2026-09-04
---

# 尚未解决的问题 / Open Questions

本页是项目开放问题的统一入口，用于本地续接时快速判断哪些内容尚未形成正式结论。

权威边界：

- 基础研究命题及其研究状态以 [[AI-Native Organization Fundamentals Backlog]] 为准。
- 近期行动顺序以 [[next-actions]] 为准。
- 各模块的具体设计状态以对应专题文件为准。
- 本页只汇总、分类和链接，不把待研究假设写成已确认规则。

## P0：继续设计前必须补齐的输入

1. 确定 2–3 个有代表性的真实任务，用来校验现有 Goal、Task 与 Work 规则。
2. 明确技术与数据边界：可使用的平台和 Agent、可进入 AI 的数据、禁止范围、权限、合规要求及现有协作系统。
3. 明确第一阶段 Human-Agent 协作实验的变量与最小安全边界。

详见 [[next-actions]]。

## P1：当前主线设计问题

### Knowledge → Behavior（当前主线）

- 谁有权晋升 Inform → Recommend → Default → Mandatory？
- 如何区分可信度、显著性、行为权力，并保留 Exploration / Exploitation 平衡？
- Default Override 与 Mandatory 授权例外怎样留痕并形成新 Evidence？

权威讨论：[[Knowledge to Behavior - Behavioral Authority]]。Scope 核心设计已在 [[Generalization & Scope]] 完成；剩余是迁移、过期与重验的操作化，不再标记整个 Scope 待设计。

### Agent Governance & Runtime（骨架已确认）

Capability、Lifecycle、Performance、Revocation、Shared Agent 归属/权限/责任待详细设计，见 [[Agent Governance & Runtime]]。后续一级模块包括 [[Capability & Human Learning 待设计]]、Contribution / Honor、[[Governance Audit Risk 待设计]]。

### Human-Agent 协作

- Human 领取 Task 后，应何时作为 Executor、Orchestrator 或 Supervisor？
- 三种角色如何根据 Task 风险、可验证性、Human 能力与学习目标动态切换？
- 新人需要亲自执行多少，才能形成真实判断力，而不是只会调用和验收 Agent？
- Human Oversight Capability 如何定义、证明和升级？
- Agent 能力超过 Human 判断能力时，Human-Agent Unit 的可信能力上限在哪里？

当前权威文件：[[Operating Loop v0.2]]、[[Free Work Space Protocol v0.1]]、[[Task Protocol v0.1]]。Work 作为 Free Work Space 的定位已经确认；此处仍开放的是其中 Human-Agent 协作与能力形成问题。

### Reference Workflow 与 Ontology

- 如何用一个真实任务完整跑通 Goal → Task → Work → Review → Knowledge → Learning → Honor？
- 最小 Ontology v0.1 需要哪些 Node、Edge、字段与约束？
- Operating Model、Ontology 与 Reference Workflow 如何互相走查？

当前权威文件：[[ontology-and-graph]]、[[next-actions]]。

### Audit Layer

- Audit Event Schema、权限、保留期限、查询、Override 与责任边界如何设计？
- 如何让 Audit 横跨 Goal、Task、Lease、Review、Acceptance、Knowledge 与 Ontology，同时避免过度记录？

当前权威边界：[[Audit Layer 待设计]]。横向定位已确认，协议尚未设计。

### 实验设计与衡量

- 一年实验应如何分期，并建立什么 Baseline？
- 如何衡量效率、创新、学习速度、适应变化、Capability Growth、组织智能与人的连接？
- 如何计算 Human Time、AI Compute、Management Attention、Communication Cost 与单位组织产出成本？
- 如何证明 AI-native 组织相对于“传统组织 + 人人使用 AI”发生了组织形态变化？
- Review Cost 与 Error Detection Rate 如何取得最优平衡？
- MTTD / MTTR 如何定义并用于衡量组织响应能力？
- 组织如何开展自我实验并区分相关性与因果性？

当前权威文件：[[AI-Native Organization Fundamentals Backlog]]、[[next-actions]]。

## P2：模块级待验证问题

### Organizational Memory

- 不同 Personal Agent 平台的最小统一接口是什么，如何可靠触发 Knowledge Commit？
- 人工确认负担与知识质量之间如何平衡？
- 错误知识的污染、冲突、取代、过期、回滚与影响追踪如何处理？
- 隐私、权限与公司数据边界如何落实到 Human 和 Agent？
- Knowledge Diffusion Latency 如何测量和降低？
- Evidence 独立性、反证、时效性与 Provenance Graph 如何操作化？
- Knowledge Promotion / Challenge / Deprecated / Superseded 状态机如何设计？

当前知识形成主干：[[Organizational Learning & Knowledge Formation]]。

当前权威文件：[[organizational-memory]]。

### 自动化与可验证性

- 自动化上限主要取决于 Agent Execution Capability，还是 Task Verifiability？
- 提高 Verifiability 能否直接扩大 Agent Auto-Accept 的安全边界？
- Human Attention 应集中在哪些机器无法可靠闭环的节点？

当前权威文件：[[AI-Native Organization Fundamentals Backlog]]、[[Task Protocol v0.1]]。

### 创新与探索

- Exploration Engine 如何从未知问题形成假设、实验、失败、新知识和新任务？
- 如何在提高执行效率的同时，避免组织只优化已知任务？
- 高质量失败如何进入 Knowledge、Capability 与 Contribution，而不被误判为人员绩效失败？

当前权威文件：[[AI-Native Organization Fundamentals Backlog]]、[[contribution-and-honor-wall]]。

### 人的成长、连接与文化

- AI 大量执行以后，Junior 如何成长为 Senior？
- 哪些能力可通过观察、Review 和纠错获得，哪些必须亲手完成？
- Learning Trace 如何可靠证明 Capability Growth？
- 哪些 Human Friction 应由 AI 消除，哪些应保留以形成信任、协作和真实连接？
- 如何避免形成“任务完成率很高，但成员彼此并不认识”的组织？

当前权威文件：[[AI-Native Organization Fundamentals Backlog]]。

### Contribution 与激励

- 真实运行数据积累到什么程度后，才有必要引入 Contribution Score？
- 如何避免奖励动作数量，而真正识别复用、影响、创新、协作、可靠性与风险发现？
- 评分机制如何接受公平性、博弈和反激励测试？

当前权威文件：[[contribution-and-honor-wall]]。

## 已明确暂缓的问题

- 暂不开发完整平台。
- 暂不选择数据库、Agent Framework 或 Graph 技术栈。
- 暂不制定 Contribution Score。
- 暂不把 Task Decomposition 粒度写入强制 Protocol。
- 未经真实任务验证，不把开放问题升级为正式规则。

详见 [[next-actions]]。

## 问题关闭规则

开放问题只有在获得真实任务 Evidence、形成明确设计结论并更新对应权威文件后，才可从本页移除或标记为已解决。原始讨论仅用于追溯理由，不直接构成关闭依据。
