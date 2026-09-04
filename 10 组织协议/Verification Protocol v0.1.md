# Verification Protocol v0.1

> 状态：**冻结**  
> 冻结日期：2026-09-03  
> 说明：冻结的是 v0.1 决策原则；量化模型与运行 Schema 等待真实数据。

## 定义

> **Verification = 组织有目的地获取具有辨识力的 Evidence，以合理成本降低 Hypothesis Cloud 的不确定性，并主动给现有解释提供被推翻的机会。**

验证成功不等于某个 Hypothesis 被证明正确。若可靠的新 Evidence 有效排除了错误解释，Verification 同样成功。

## 运行原则

1. **验证整个 Hypothesis Cloud**：寻找能区分多个竞争解释的 Observation / Experiment，而非只验证排名第一的假设。
2. **证伪优先**：主动问“如果这个 Hypothesis 是错的，什么 Evidence 最容易暴露它？”
3. **Information Gain 优先**：相同成本下，优先选择最能让解释空间收敛的方案。
4. **Evidence 持续更新**：`Support / Contradict / Discriminate / Neutral` 持续改变 Hypothesis Cloud，并遵守 [[Evidence Core Principles|Independent Evidence Principle]]。
5. **不要求唯一原因**：多个 Mechanism 可以共同成立；目标是达到足以预测和行动的解释稳定性。

## 三种路径

- **Passive Verification**：等待未来真实 Task 自然产生 Evidence；成本低、速度慢。
- **Retrospective Verification**：重新分析已有历史 Events / Observations；成本较低，但需警惕混杂因素。
- **Active Verification**：主动控制条件、设计 Experiment 或业务干预；辨识力通常更强，成本与风险也更高。

## Stopping Rule

Stopping Rule 是决策阈值，不是真理阈值。当同时满足以下条件，可以停止主动验证：

1. Hypothesis Cloud 已收敛到足以支持当前行动；
2. 剩余合理解释之间的差异不再实质改变行动；
3. 进一步 Verification 的预期信息收益低于成本与风险。

```text
Stop Active Verification → Act → Continue Passive Verification
```

停止主动验证不等于 Knowledge 永久冻结。未来 Counter Evidence 仍可触发 Challenge、重新打开 Hypothesis Cloud 或修订 Scope。

## v0.1 收益与成本判断

当前只用 `Low / Medium / High`，不建立缺少真实数据支撑的精确权重。

收益：

- Information Gain；
- Decision Impact；
- Reuse / Scale。

成本：

- Human Time；
- Agent / Compute；
- Elapsed Time；
- Opportunity Cost；
- Experiment Risk。

高收益、高成本或高风险的验证交由 Human 决定；低价值问题可以仅被动观察。

## 后续研究

[[AI-Native Organization Fundamentals Backlog]] 中保留 **Verification Economics Model / Value of Information**。待积累 Verification Proposal、实际 Human/Compute/时间成本、Hypothesis Cloud 变化、Decision Change、Knowledge Reuse 与最终价值后，再研究数学模型。

关联：[[Organizational Learning & Knowledge Formation]] · [[Evidence Core Principles]] · [[Generalization & Scope]]

