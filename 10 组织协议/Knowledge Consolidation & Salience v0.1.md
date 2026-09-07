# Knowledge Consolidation & Salience v0.1

> 2026-09-07：本页保留有效子机制细则。整体当前基线见 [04完整规格](Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Specification.md)；行为强度治理见 [08 Policy Governance](Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Specification.md)。知识不晋级为Protocol，认知/显著性/行为权力分离，更新按组件及实质依赖传播。下文未定字段、算法与参数不等于核心设计未冻结。


> 状态：已冻结 v0.1。收敛轮次 `ead47c74-e355-47e8-b8d5-4cc388832fa8`；同意冻结 `4065665c-6bc0-453b-9bf9-6a91b08a030b`。

**Epistemic Strength** 回答“有多可信”，由 Evidence、独立性、Verification、反证与 Validated Scope 支持。**Memory Salience** 回答“在当前情境下有多值得想起”。两者分开，不混成一个总分。常用不等于更真，罕见不等于不重要。

## 八类强化信号

1. Repeated Successful Reuse：被实际采用并反复产生有效结果，不能只数检索次数。
2. Utility / Benefit：效率、质量、创新、Human Time、成本、学习速度等实际收益。
3. Risk / Loss Avoidance：低频但遗忘代价高的风险与损失避免。
4. Failure → Correction：失败或重大 Retry 后，应用知识伴随问题纠正。
5. Surprise / Prediction Error：现实偏离原先预测的认知冲击。
6. Connectivity / Explanatory Centrality：解释、支持或约束许多其他知识与 Practice 的认知枢纽。
7. Temporal Persistence：跨月份、任务、Human / Agent 持续复用与验证。
8. Breadth：在已经验证的多个 Context 中成功复用，不擅自扩大 Scope。

Utility Consolidation 强调反复有效、收益、广度、时间持续性；Salience Consolidation 强调重大收益/风险、失败纠正、意外与解释中心性。两条路径均不自动授予 Protocol 权限。

**Activation Count ≠ Knowledge Value**。强化链应是 Activation → Adoption → Outcome → Evidence → Consolidation，避免“推荐更多 → 调用更多 → 再推荐”的自我强化。

Peripheral / Core / Critical / Active 是认知地位，不是真假等级；Validated 是认知状态。重要知识在正确 Context 下优先激活，不是永远加载。Outcome 相关性仍需验证，不能直接当作因果。

关联：[[Cognitive Routing 与 Knowledge Activation]] · [[Knowledge Usage Feedback]] · [[Evidence Core Principles]]
来源：[[探讨AI原生组织-raw-conversation]]（主设计对话，2026-09-04 阶段同步）。
