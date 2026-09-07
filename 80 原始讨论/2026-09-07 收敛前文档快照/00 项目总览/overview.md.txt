---
type: project
status: design
project: AI-Native Organization
reviewed: 2026-09-04
---

# AI-Native Organization

## 项目背景

这是一个跨部门、培训型的实验组织：约 60 名来自公司不同部门的应届生，周期一年。成员保留各自正式岗位，同时在这个“第二组织”中承担真实任务、协作与学习。

核心研究命题：

> 如果一个组织从诞生开始就把 Human 与 AI 都视为智能节点，并围绕 Goal、Task、Knowledge、Capability 重新设计运行方式，它能否获得比传统组织更高的效率、创新能力、学习速度和环境适应能力？

## 价值函数

- 第一优先级：效率、创新。
- 同时观察：学习速度、变化响应速度、人的能力成长、组织智能、人与人的连接。
- 不以 AI 使用量为成功指标，而以 Organizational Output 为中心。
- 当前尚未确定组织将承接的具体真实项目；后续需要用真实任务校验全部规则。

## 总体设计原则

1. Management = Goal + Resource Boundary + Risk Boundary + Efficiency Optimization。
2. 最终 Decision Owner 暂定为 Human，因为 Human 承担最终责任。
3. Human 与 Agent 都可以成为工作节点，分工取决于 Capability、Risk 与 Accountability。
4. 固定 Protocol，不固定 Workflow。
5. Task Bus 是组织级任务调度核心；Work 是 Task 内部的 Free Work Space，不另建组织级 Work Graph。
6. 同时建设 Execution Engine 与 Exploration Engine。
7. Learning 必须嵌入 Work：Work → Feedback → Learning → Retry → Capability Upgrade。
8. Distributed Intelligence + Shared Memory：Local thinking, global learning。
9. 知识应由工作过程产生并被治理，不依赖员工手工维护知识库。
10. Centralized Protocol, Distributed Intelligence：正式进入组织系统的对象必须遵守共同 Schema、Ontology、Permission 与 Audit。
11. 底层 Graph 围绕价值产生，而不是以传统“谁管谁”的组织结构为骨架。
12. 第一阶段不做积分排行榜，先做可追溯的 Evidence-based Honor Wall。

## Operating Loop

```text
Goal Proposal → Active Goal → Decomposition → Task Proposal
→ Validation → Active Task → Task Bus → Executor Unit
→ Free Work Space → Output + Evidence → Review（Quality + Learning）
→ Acceptance → Result → Knowledge / Evidence / Capability / New Task
↔ Organizational Memory（持续学习层）
```

完整版本见 [[Operating Loop v0.2]]。

## 项目地图

- [[Goal Protocol v0.1]]
- [[Task Protocol v0.1]]
- [[Goal-Task 接口补丁 v0.1]]
- [[Operating Loop v0.2|Operating Loop v0.2]]
- [[Free Work Space Protocol v0.1]]
- [[Time & Recovery Protocol v0.1]]
- [[Task Lease & Progress Protocol v0.1]]
- [[Review Protocol v0.1]]
- [[Acceptance Protocol v0.1]]
- [[Audit Layer 待设计]]
- [[Organization Runtime & Protocol OTA]]
- [[Organizational Learning & Knowledge Formation]]
- [[Evidence Core Principles]]
- [[Verification Protocol v0.1]]
- [[Generalization & Scope]]
- [[organizational-memory|Knowledge / Organizational Memory]]
- [[ontology-and-graph|Ontology / Graph 原则]]
- [[contribution-and-honor-wall|Contribution 与 Evidence-based Honor Wall]]
- [[open-questions|尚未解决的问题 / Open Questions]]
- [[AI-Native Organization Fundamentals Backlog]]
- [[next-actions|待办与下一步]]
- [[05项目/AI Native组织/80 原始讨论/探讨AI原生组织-raw-conversation|完整原始对话]]

## 当前状态

执行协议维持已冻结 v0.1，Operating Loop 为 v0.2。Knowledge Formation v0.1 已收敛，Scope 核心设计完成并纳入其中。Memory 三层、稀疏激活与 Cognitive Routing 核心架构形成；Context Assembly 与 Consolidation v0.1 已冻结；Intervention v0.1 核心设计确认。

当前主线是 [[Knowledge to Behavior - Behavioral Authority]]：行为权力晋升与 Exploration / Exploitation。[[Agent Governance & Runtime]] 已正式单列一级模块，骨架确认、待详细设计。

后续一级模块：[[Capability & Human Learning 待设计]]、[[contribution-and-honor-wall|Contribution / Honor]]、[[Governance Audit Risk 待设计]]。完整状态见 [[设计状态与版本]]。真实任务、技术与数据边界仍待补齐。

## 来源

本页整理自 [[05项目/AI Native组织/80 原始讨论/探讨AI原生组织-raw-conversation|ChatGPT 对话「探讨AI原生组织」]]。

## 新增模块入口

- [[Generalization & Scope]]
- [[Cognitive Routing 与 Knowledge Activation]]
- [[Context Assembly v0.1]]
- [[Knowledge Consolidation & Salience v0.1]]
- [[Knowledge Intervention v0.1]]
- [[Knowledge Usage Feedback]]
- [[Knowledge Injection 与同步边界]]
- [[Agent Governance & Runtime]]
- [[Knowledge to Behavior - Behavioral Authority]]
- [[设计与开发轨道]]
- [[阶段同步报告 2026-09-04]]

## 独立工作轨道续接

从 [[DESIGN-ISSUE-001 基线入口]] 进入，核对 [[设计状态与版本]] 与 [[next-actions]]；行为治理见 [[Knowledge to Behavior - Behavioral Authority]]。裁决为 `Resolved — baseline sync gap, not protocol contradiction`。
