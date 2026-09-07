# Organizational Learning & Knowledge Formation

> 状态：**[[Organizational Knowledge Formation Protocol v0.1]] 已冻结；Knowledge → Behavior 治理尚未冻结**  
> 更新日期：2026-09-04  
> 下一主线：[[Knowledge to Behavior - Behavioral Authority]]

## 定位

Organizational Learning 不是 Result 后的附属步骤，而是覆盖 Goal、Decomposition、Task Bus、Free Work、Review、Acceptance 与 Result 的持续学习层。知识可以来自领域事实，也可以来自 Goal 定义、Task 拆解、路由、Agent 协作、Review、失败和恢复等 Operating Knowledge。

## 当前主干

```text
Raw Events
→ Organizational Attention Mechanism
→ Observation
→ Pattern
→ Hypothesis Cloud ⇄ Evidence ⇄ Verification
→ Generalization / Scope
→ Knowledge
→ Behavior Change
→ New Events
```

Hypothesis Cloud 的收缩、扩展、分裂、合并，是 Evidence 与 Verification 循环导致的状态变化，不是单独的线性阶段。

## 1. Organizational Attention Mechanism

> 状态：**核心定义与原则已确认；运行 Schema 待设计**

作用是在海量 Raw Events 与值得投入认知资源的 Observation 之间建立注意力过滤，而不是直接形成 Knowledge。

三类来源：

- **Statistical Attention**：异常、趋势、聚类、变化点、重复关系；
- **Semantic Attention**：识别表达不同但语义相同的现象、矛盾和潜在连接；
- **Organization Lens**：异常性、重复性、影响性、新颖性、冲突性、机会性、风险性。

当前不设计加权 Attention Score，先记录候选与后续价值，再由真实运行数据学习阈值。

## 2. Observation

> 状态：**概念边界已确认；格式待设计**

Observation 是从 Raw Events 中抽取、值得组织进一步认识和解释的现象。它可以由中央系统、Human、Personal Agent 或 Review Agent 提出，但必须能回溯原始 Event / Source。

## 3. Pattern

> 状态：**核心定义已确认**

> **Pattern = 通过统计或语义分析发现的、稳定重复出现的结构或关系。**

Pattern 只回答“什么关系反复发生”，不负责解释原因，不把相关性写成因果。

## 4. Hypothesis Cloud

> 状态：**核心机制已确认；权重算法待设计**

AI 对 Pattern 维护多个竞争解释、替代解释与潜在混杂因素，不宣布单一原因。Evidence 驱动 Belief / Support Weight 变化；多个 Agent 重复同一来源不构成权重提升。

Hypothesis Cloud 允许：

- 收缩或扩展；
- 新增或淘汰解释；
- 分裂或合并；
- 多个 Mechanism 长期并存。

目标是把解释空间缩小到足以预测和行动，不要求坍缩为唯一原因。

## 5. Evidence

> 状态：**核心定义与原则已确认；操作化待设计**

详见 [[Evidence Core Principles]]。Evidence 是可追溯 Observation / Fact / Result 相对于 Claim / Hypothesis 的认知关系，而不是孤立附件。

## 6. Verification

> 状态：**[[Verification Protocol v0.1]] 已冻结**

验证整个 Hypothesis Cloud，优先证伪和高 Information Gain，并在剩余不确定性不再改变行动且继续验证收益低于成本时停止主动验证、继续被动验证。

## 7. Generalization / Scope

核心设计已完成并纳入 v0.1。[[Generalization & Scope]] 定义 Validity Map 的 Validated、Inferred、Invalid / Boundary、Unknown 四种状态，以及 Minimum Validated Scope。知识质量不等于 Scope 大小，未经直接验证的迁移不能伪装成已验证适用域。

## 8. Organizational Knowledge

> 状态：**核心定义与拆分原则已确认；状态机和 Schema 待设计**

> **Organizational Knowledge = 经过足够 Evidence 与 Verification 支持、主要竞争性 Hypothesis 已显著削弱、至少拥有明确的最小验证适用域，足以帮助未来 Human / Agent 判断、预测或行动的最小可复用认知单元。**

原则上一条 Knowledge 只表达一个主要 Claim。文档是 Artifact，不应自动等同于 Knowledge Object。

至少区分：

- Fact Knowledge；
- Pattern / Relational Knowledge；
- Causal Knowledge；
- Mechanism Knowledge；
- Predictive Knowledge；
- Prescriptive Knowledge / Practice。

Validated 是认知状态；Standard 是组织选择采用的运行状态，两者不能混同。

## Behavior Change

知识形成并不自动授予行为控制权。Knowledge 可以 Inform / Recommend；升级 Default / Mandatory 必须经过治理，权限尚待确定，不能直接自动 OTA。

使用链：Organizational Memory → Cognitive Routing → Knowledge Activation → Context Assembly → Context Injection → Human/Agent Action → New Events。

[[Knowledge Intervention v0.1]] 已形成“Learn before prescribe”的渐进框架；[[Knowledge to Behavior - Behavioral Authority]] 继续讨论 Behavioral Authority 与 Exploration / Exploitation。知识使用结果经 [[Knowledge Usage Feedback]] 回到 Evidence 与 Verification。

## 尚未冻结的运行问题

- Observation、Pattern、Hypothesis、Evidence 与 Knowledge 的最小 Schema；
- Human / AI 在升级、挑战、确认与发布中的权责；
- Knowledge Promotion、Challenge、Deprecated、Superseded 状态机；
- 可执行 Practice / Playbook 的正式名称与边界；
- Knowledge 如何扩散、复用、评估并反向修订。

关联：[[organizational-memory]] · [[ontology-and-graph]] · [[Review Protocol v0.1]] · [[Organization Runtime & Protocol OTA]]

## v0.1 冻结边界

Hypothesis → Knowledge 的 Evidence、Falsification、Uncertainty、Scope 四道门已收敛。冻结的是认知原则，不是完整 Schema、评分公式、执行状态机或知识行为授权。原“整体未冻结 / Scope 待设计”的旧状态已由 DESIGN-ISSUE-001 澄清。

来源：[[探讨AI原生组织-raw-conversation]]（主设计对话，2026-09-04 阶段同步）。

## 基线适用说明

本页保留知识形成的已有定义、原则与运行问题；冻结状态以 [[Organizational Knowledge Formation Protocol v0.1]] 为准。下游 Memory 架构及行为权威治理以 [[organizational-memory]]、[[Knowledge to Behavior - Behavioral Authority]] 为准。未决 Schema 或实现细节不再被解释为知识形成协议整体未冻结。
