# Organizational Knowledge Formation Protocol v0.1

> 2026-09-07：本页保留有效子机制细则。整体当前基线见 [04完整规格](Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Specification.md)；行为强度治理见 [08 Policy Governance](Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Specification.md)。知识不晋级为Protocol，认知/显著性/行为权力分离，更新按组件及实质依赖传播。下文未定字段、算法与参数不等于核心设计未冻结。


> 版本：v0.1；状态：冻结。
> 基线同步日期：2026-09-04；裁决：[[DESIGN-ISSUE-001 基线同步裁决]]。

## 协议基线

```text
Raw Events → Organizational Attention Mechanism → Observation → Pattern
→ Hypothesis Cloud ⇄ Evidence ⇄ Verification
→ Generalization / Scope → Knowledge
```

知识形成的已有定义与原则见 [[Organizational Learning & Knowledge Formation]]；Evidence 见 [[Evidence Core Principles]]；验证规则见已冻结的 [[Verification Protocol v0.1]]。

Generalization / Scope 核心设计已完成，作为本协议 v0.1 的组成部分：

- Validity Map：Validated / Inferred / Invalid-Boundary / Unknown。
- Minimum Validated Scope。
- Scope 可随真实 Work 扩张或收缩。

Scope 模块正文见 [[Generalization & Scope]]。Knowledge 保持明确 Claim、Evidence、Scope、认知状态与复用价值；Validated 与组织选择采用的 Standard 不混同。

## 冻结边界

本次是已裁决设计的基线同步，不是重新设计或升级冻结协议。知识形成与知识驱动的Policy Governance均已纳入最终基线，但认知成立与行为授权仍是不同判断；后者见 [[Knowledge to Behavior - Behavioral Authority]]。具体 Schema、算法和实现层未决问题仍按其现有状态保留，不补造已冻结细则。

后续协议升级仍遵守 [[设计状态与版本]] 的真实 Evidence、影响范围和迁移规则。

## 原始讨论补齐：认知闸门

Hypothesis → Knowledge 需经过 Evidence Gate、Falsification Gate、Uncertainty Gate、Scope Gate；具体含义见 [[Generalization & Scope]]。Knowledge 是经过足够 Evidence 与 Verification 支持、主要竞争解释显著削弱、具有 Minimum Validated Scope 且足以帮助未来判断/预测/行动的最小可复用认知单元。

来源：[[探讨AI原生组织-raw-conversation]] 中 `0a555497-ecac-45b0-b5b6-66db3333728c` 收敛段。知识形成后进入 Memory、使用、Behavior Change 和 New Events；更强行为授权仍须治理。
