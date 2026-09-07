# Cognitive Routing 与 Knowledge Activation

> 2026-09-07：本页保留有效子机制细则。整体当前基线见 [04完整规格](Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Specification.md)；行为强度治理见 [08 Policy Governance](Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Specification.md)。知识不晋级为Protocol，认知/显著性/行为权力分离，更新按组件及实质依赖传播。下文未定字段、算法与参数不等于核心设计未冻结。


> 状态：核心原则已确认；评分、Schema 与算法待设计。

Current Context → Cognitive Routing → Knowledge Activation → Context Assembly → Context Injection → Human/Agent Reasoning & Action。

Activation 问“现在该想起什么”；Assembly 问“什么组合和深度”；Injection 是实际送入 Runtime Context 的动作。**Knowledge Activation ≠ Context Injection**，语义相关也不等于值得占用注意力。

Context 包含 Goal、Task、Expected Output、Acceptance Criteria、Human Capability、Agent、Risk 与当前工作状态。使用六个 Lens，不先造加权总分：Relevance、Scope Match、Epistemic Strength、Decision Impact、Novelty、Timing。

触发来源包括 Task 领取/激活、工作中的疑问、重要 Decision、异常/Review Fail/Retry，以及 Knowledge 状态变化。默认激活少量 Knowledge；需要解释时下钻 Epistemic，重验/审计时下钻 Experience。权限边界始终生效。

Validated / Supported 优先；Inferred / Unknown 不能以“已验证最佳实践”注入。Invalid Scope 默认不作为行动依据激活。相同 Context 不反复推送无变化知识。

Knowledge 状态变化时通知相关依赖方重新评估，不自动停掉所有任务。普通 Knowledge informs behavior；经治理的 Protocol governs behavior。高可信度不会自动获得强制权限。

关联：[[organizational-memory]] · [[Generalization & Scope]] · [[Context Assembly v0.1]] · [[Knowledge Consolidation & Salience v0.1]]
来源：[[探讨AI原生组织-raw-conversation]]（主设计对话，2026-09-04 阶段同步）。
