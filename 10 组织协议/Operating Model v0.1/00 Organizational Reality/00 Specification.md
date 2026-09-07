# 00 Specification

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## 对象、事件与依赖

Object 表达当前存在的实体，包括 Human、HAU、Agent、Goal、Task、Execution、Result、Knowledge、Capability、Policy、Risk、Contribution 等。对象结构化、有版本，重要内部组件可被定位。

Organizational Event 使用统一基础模型和 Event Envelope，允许多种 Event Type。事实只记录一次；Knowledge、Capability、Contribution、Reliability 与 Audit 可分别产生解释。TaskCreated 归 Task；ExecutionClaimed、ACK、Progress、ResultSubmitted 归 Execution；Review/Acceptance 关联 Result 与 Execution。

Event Graph 保存历史与事件之间的联系，历史事件原则上不覆盖。Dependency Graph 保存当前有效的实质依赖，可建立、调整或失效，并保留变更历史。A 的实质变化可能要求 B 重新评估，才表示 B 对 A 存在 Dependency。看过、关联或共同出现，不自动构成依赖。

## 组件级演进

Goal 可定位 Desired Change、Success Criteria、Assumptions、Scope、Boundary、Priority/Time Horizon；Knowledge 可定位 Core Claim、Scope、Boundary、Mechanism、Evidence、Transfer Conditions；Capability Package 可定位 Knowledge、Data、Tool、Runtime、Review、Oversight；Human Model 可定位行为维度。

Challenge the smallest meaningful unit。修正保留 Version + Delta + Reason + Evidence，记录旧认知为何成立以及何种证据促成变化。Challenge、Revision、Supersession 的语义不能压缩成整块对象有效/无效。

## Materiality 与选择性传播

Evidence 可以持续进入，不是每个事件都触发结构响应。只有足以改变 Claim、Scope、Boundary、Decision 或当前有效状态的变化才达到 Materiality Threshold，成为 Material Change。具体判定参数为 Tunable，不设统一数值分数。

变化先定位组件，再沿真实 Dependency 分析影响。Scope 缩小时只检查落在被移除范围内的依赖；不得无差别暂停所有 Execution。边界内可以自主响应；需要扩大 Authority、改变 Policy 或接受超授权 Risk 时才进入 Governance。响应与依赖更新形成新的事件。

## Change Set

具有共同 Root Cause 或共同变化上下文的相关 Material Events 聚合为 Change Set。底层事件继续分别存在；Change Set 是治理聚合，不替代 Event。它呈现 Root Evidence、Affected Components、Dependency Impact、Automatic Responses、Required Decisions。各 Authority 只处理自己 Scope 内的决定，避免同一变化产生大量重复审批。

## 采集边界与重建

Prompt、草稿、私人 Agent 推理、临时 Subtask、普通 Tool Call 和内部尝试默认不进入 Organizational Reality。跨越明确边界、成为正式 Result、Evidence、Risk、Boundary Request 或 Organizational State Change 时才进入。

Audit 通过 Event Graph + Object Versions + Authority-at-the-time + Dependency History 重建事实与决策；Handover 利用同一现实重建 Context。两者均不建立第二套事实世界。统一事件字段、组件地址格式、存储与查询 API 仍需工程规格化，不在本次编造。

## Event Envelope 与关系语义

冻结源文明确的最小公共 Envelope：Event ID、Event Type、Actor、Time、Object(s)、Context、Source/Evidence；Before State、After State为可选项；相关时记录Authority、Policy Version、Protocol Version。每种Event Type另有自己的Payload，不能把“统一模型”误解为所有事件具有完全相同载荷。

Event Graph还表达caused、resolved_by、enabled、resulted_in等事件联系，而非只有时间排序。关系须有事实或依据支持；图上的关联不自动证明因果。Dependency第一版采用requires、uses、supports、constrained_by、derived_from、governed_by等少量语义，不预设Dependency Strength数值。

Dependency主要从真实使用及对象组合形成：关键Decision使用Knowledge、Package包含Tool等。Execution结束或对象被替代时更新当前依赖状态，历史关系继续由事件记录。知识被激活但没有实质依赖时，不因“读过”自动建强依赖。

来源：本次原始讨论中turn-ccf7ae80-6ffb-4c88-b0a7-0ee4e3fcdc6e；公共字段语义已确定，具体数据库Schema与字段类型未定。
