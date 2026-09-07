# Context Assembly v0.1

> 2026-09-07：本页保留有效子机制细则。整体当前基线见 [04完整规格](Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Specification.md)；行为强度治理见 [08 Policy Governance](Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Specification.md)。知识不晋级为Protocol，认知/显著性/行为权力分离，更新按组件及实质依赖传播。下文未定字段、算法与参数不等于核心设计未冻结。


> 状态：已冻结 v0.1。主设计同意轮次：`849158ce-2b9d-474d-ad27-b7add324152a`。

**Knowledge Object = Claim + Scope + Boundary + Epistemic Status**。

- Claim：一个主要、可复用的认知判断。
- Scope：适用条件与验证范围。
- Boundary：不适用范围、限制与失效边界。
- Epistemic Status：当前证据支持状态，不能冒充永久真理。

根据当前 Context 动态生成 **Action Implication** 与必要的 **Caution / Risk**；这不是将固定动作清单永久写入 Knowledge Object，也不是给 Task 偷写 Workflow。

默认不把 Evidence、Hypothesis Cloud、Verification History 和 Raw Events 全部塞入上下文。需要质疑、解释或深入审查时通过 On-demand Retrieval 下钻，保持可追溯入口。

组装少量与当前判断相关的知识；即使已经 Activated，也可能不进入最终 Context Package。普通 Implication / Caution 不得偷偷变成强制规则。

关联：[[Cognitive Routing 与 Knowledge Activation]] · [[Knowledge Injection 与同步边界]] · [[Knowledge to Behavior - Behavioral Authority]]
来源：[[探讨AI原生组织-raw-conversation]]（主设计对话，2026-09-04 阶段同步）。
