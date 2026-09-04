# Generalization & Scope

> 状态：核心设计已完成，纳入 Knowledge Formation Protocol v0.1；运行 Schema 与自动化仍待设计。
> 更新：2026-09-04。依据主设计对话收敛及 DESIGN-ISSUE-001 裁决。

Verification 回答为什么相信；Generalization / Scope 回答在哪里可以相信。Scope 不是人工贴上 Research 一类标签，而是通过改变 Task、Human、Agent、环境、时间与资源条件，寻找成立和失效边界的 **Validity Map**。

| 有效性状态 | 含义 |
|---|---|
| Validated Scope | 有直接 Evidence 支持 |
| Inferred Scope | 基于 Mechanism 推测，尚无直接验证 |
| Invalid / Boundary | 已有 Evidence 表明不适用或开始失效 |
| Unknown | 尚未知道，不等于有效或无效 |

**Minimum Validated Scope** 是最小已验证适用域；不要求先证明普适性。Knowledge Quality ≠ Scope Size。扩大 Scope 必须取得新 Evidence，不能靠调用频次、语义相似或多 Agent 共识。

Hypothesis → Knowledge 需跨过四道门：Evidence Gate（可追溯且尽可能独立）、Falsification Gate（真正给过被推翻的机会）、Uncertainty Gate（剩余解释差异不再实质改变当前行动）、Scope Gate（至少具备 Minimum Validated Scope）。具体权重、数值阈值不在 v0.1 冻结范围。

反例可以触发 Claim Challenge、Scope Shrink 或 Re-verification；需区分结论错误和超出适用域。环境/模型变化后的有效期、重验触发与迁移治理继续保留在研究与实现问题中。

关联：[[Organizational Learning & Knowledge Formation]] · [[Verification Protocol v0.1]] · [[Evidence Core Principles]] · [[Cognitive Routing 与 Knowledge Activation]]
来源：[[探讨AI原生组织-raw-conversation]]（主设计对话，2026-09-04 阶段同步）。

基线裁决：[[DESIGN-ISSUE-001 基线同步裁决]]。本模块纳入 [[Organizational Knowledge Formation Protocol v0.1]]，不额外指定独立版本。
