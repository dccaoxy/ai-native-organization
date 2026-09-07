# Audit Layer（待设计）

> 状态：**待设计**

Audit 是贯穿整个 Operating Loop 的横向基础设施，不属于 Acceptance 的子模块。它应覆盖 Goal 提出/批准、Task 拆解/激活、领取/派发、Boundary 与标准版本变化、Task Lease、Submit、Review、Acceptance、Knowledge Confirmation 与 Ontology 变更等关键事件。

当前只冻结边界：**Acceptance 是业务决定；Audit 证明该决定及其上下文如何形成。** Audit Protocol 的事件 Schema、权限、保留、查询与追责边界尚未设计。

关联：[[Operating Loop v0.2]] · [[Acceptance Protocol v0.1]] · [[Task Lease & Progress Protocol v0.1]]

所属后续一级模块：[[Governance Audit Risk 待设计]]。Agent 的运行治理与撤销问题见 [[Agent Governance & Runtime]]。
