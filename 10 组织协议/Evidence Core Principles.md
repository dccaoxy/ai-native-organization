# Evidence Core Principles

> 2026-09-07：本页保留有效子机制细则。整体当前基线见 [04完整规格](Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Specification.md)；行为强度治理见 [08 Policy Governance](Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Specification.md)。知识不晋级为Protocol，认知/显著性/行为权力分离，更新按组件及实质依赖传播。下文未定字段、算法与参数不等于核心设计未冻结。


> 状态：**核心定义与原则已确认；Evidence Operationalization 待设计**
> 更新日期：2026-09-03

## 核心定义

> **Evidence 不是附件，而是某个可追溯 Observation / Fact / Result 相对于 Claim / Hypothesis 的认知关系。**

同一项信息对一个 Claim 可能构成 Evidence，对另一个 Claim 可能无关。Evidence 必须能追溯至现实中的 Event、Observation、Experiment、Artifact 或权威 Source。

主要关系：

- `supports`：提高对 Claim / Hypothesis 的相信程度；
- `contradicts`：降低相信程度或触发 Challenge；
- `discriminates`：对竞争 Hypothesis 产生不同预测，帮助区分解释；
- `neutral / inconclusive`：目前不能有效改变解释空间。

## Independent Evidence Principle

> **从观察上升为具有稳定规律意义的 Knowledge，原则上不能依赖单一独立 Evidence Source。**

多个 Agent 重复分析同一来源，不构成多个独立 Evidence。系统应识别 Evidence Provenance、共同上游和循环引用，避免制造虚假共识。

## Evidence Threshold follows Impact

> **一个认知结论越抽象、越普适、越会改变组织行为，需要的独立 Evidence 强度和 Verification 程度越高。**

- 单一高质量权威 Evidence 可以确认某些具体 Fact；
- Pattern 需要多个独立 Observation；
- Causal / Mechanism Claim 需要更强的独立 Evidence 与反证搜索；
- Generalized Knowledge 需要跨场景、时间或来源验证；
- 对全组织有强制影响的Policy/Boundary或Protocol变更需要与后果匹配的更强Evidence与授权；Knowledge本身不晋级成为Protocol。

一条强 Counter Evidence 不能被多条弱 Supporting Evidence 以多数票淹没；它应触发 Scope、Mechanism 或 Knowledge Status 的重新检查。

## 待设计：Evidence Operationalization

- Source Reliability、Measurement Quality 与 Reproducibility；
- Independence / Diversity 的技术判定；
- Evidence Weight 与 Belief Update 是否定性或 Bayesian；
- Counter Evidence 的 Challenge / Reopen 机制；
- Temporal Relevance 与过期；
- Provenance Graph、循环来源识别和最小 Schema。

关联：[[Organizational Learning & Knowledge Formation]] · [[Verification Protocol v0.1]] · [[ontology-and-graph]]
