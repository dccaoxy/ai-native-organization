# Foundational Principles — 11 + 1

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](Principle%20Tree%20v0.1.md) · [来源索引](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 85b640cd](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-85b640cd-b88d-4d2b-b822-991ab50aa8d2) · [源文 ec3cb0fa](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

### 01. Human retains purpose authority
**Human 保留组织目的的最终决定权。**

AI 可以发现、建议、挑战、拆解和执行 Goal，但组织最终追求什么，由 Human 决定。

---

### 02. Human may leave execution, never accountability
**Human 可以退出执行环，但不能退出责任环。**

Execution 可以完全由 Agent 完成，但每个 Execution 必须唯一解析到一个 Human Accountable Owner（最终责任人）。

---

### 03. Autonomy is default; boundaries are explicit
**自主是默认状态，边界必须明确。**

Human、HAU 与 Agent 在明确 Boundary 内默认自主；Governance（治理）处理越界与例外，而不是审批正常工作。

---

### 04. Authority must have a source
**任何组织权力都必须有可追溯来源。**

任何 Human、Agent 或 System 执行组织级 Action，都必须能够回答：

> **“我凭什么有权这样做？”**

组织中不存在无人治理、来源不明的 Authority（决策权）。

---

### 05. Authority narrows by delegation; expands only by authorization
**权力向下委托只能保持或收紧；扩大必须获得授权。**

Delegation（委托）不能创造新的 Authority。

---

### 06. Risk authority follows actual consequence bearing
**风险接受权跟随实际后果承担者。**

任何 Actor 都不能替自己无权代表的后果承担者接受 Risk。

同时：

> **Unknown ≠ Dangerous。**

治理应该尽量降低 Exposure（暴露）、提高 Recoverability（可恢复性），把未知变成失败得起的实验。

---

### 07. Govern organizational state, not private thought
**组织治理组织状态，不治理私人思考。**

中央系统治理 Goal、Task、Execution、Authority、Risk、Resource 和正式 Organizational State，但不默认监控 Human / Agent 的私人推理、草稿和内部工作过程。

> **Shared Reality ≠ Total Surveillance。**

---

### 08. Protocol fixed, workflow free
**共同语言稳定，工作方法自由。**

Protocol 统一共同语言、语义和交互结构，而不规定具体 How。

严格区分：

> Knowledge = 我们认为世界是什么样。
> Policy = 当前允许、禁止和要求什么。
> Protocol = 我们如何共同表达和交互。
> Foundational Principles = 最根本的权力与责任原则。

---

### 09. One organizational reality
**整个组织共享同一个现实。**

采用统一：

> Organizational Objects
> Event Graph
> Dependency Graph

并坚持：

> **Record facts once, interpret many times.**
>
> 事实只记录一次，可以被 Knowledge、Capability、Contribution、Human Model、Risk、Audit 等系统分别解释。

---

### 10. Challenge locally, evolve continuously
**局部质疑，持续演进。**

> **Challenge the smallest meaningful unit.**
>
> **Revise locally, propagate selectively.**

Goal、Knowledge、Capability、Policy、Human Model 等对象都应支持颗粒化修正，而不是一有反例就整块推翻。

同时：

> **变化不能抹掉历史。**

组织必须能够知道自己以前相信什么、为什么相信，以及后来为什么改变。

---

### 11. Value is demonstrated through impact, not activity
**价值由真实影响证明，而不是由活动量证明。**

忙碌、Token、工时、Task数量都不是 Contribution 本身。

真正的问题始终是：

> **组织因为这个行为发生了什么可追溯的正向变化？**

Reward 应该追随真实价值，而不是反过来制造“什么叫价值”。

---

# Meta-design Principle
## Seed lightly, observe deeply, formalize late
### 轻量播种，深入观察，延后固化

这是我们**设计这个组织的方法**，而不是普通成员每天必须遵守的组织规则。

第一天只提供必要的：

> Seed Map
> Seed Ontology（种子分类）
> Boundary
> Protocol
> Minimum Structure

然后：

> **真实运行 → Organizational Events → Evidence → Pattern → Learning → 再逐渐正式化。**

所以我们不应该第一天就：

> 画死 Capability体系；
> 写死 Contribution价格；
> 给所有人固定等级；
> 规定完整 Workflow；
> 把所有未知变成制度。

而应该：

> **先让这个组织活起来，再让组织告诉我们它真正是什么。**

---
