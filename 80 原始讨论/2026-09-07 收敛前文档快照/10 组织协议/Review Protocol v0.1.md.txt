# Review Protocol v0.1

> 状态：**冻结**  
> 冻结日期：2026-09-02

> **Review = Quality Gate + Learning Gate**

## Quality Gate

默认由独立 Agent 负责找明确错误，不允许执行 Agent 仅靠自检闭环。Hard Review 检查：

- Completeness：是否交齐；
- Compliance：是否符合 Task、Boundary 与要求；
- Evidence：证据是否存在、可靠、可复核并支撑结论；
- Correctness：事实、逻辑、代码、计算是否正确；
- Risk：是否存在遗漏、反例、权限、隐私、安全、合规或不可逆风险。

`Confidence` 是 Review 元数据，不是质量维度。低置信度不得轻易 Auto-Accept，应增加 Reviewer 或升级 Human。高判断任务由 Human 对 Quality、Depth、Usefulness 与 Trade-off 作 Judgment。

## Learning Gate

Learning Gate 与 Task Pass/Retry 平行，不影响质量结论：

| Signal | 路由 |
|---|---|
| New Knowledge | Knowledge Commit |
| New Evidence | Knowledge Validation / 冲突与置信度更新 |
| Ontology Signal | Ontology Change Proposal |
| System Learning | Organization Improvement Backlog / Capability / Routing Evidence |

Task 可以 Failed 但产生高价值 Learning，也可以 Pass 而没有新知识。

关联：[[Acceptance Protocol v0.1]] · [[organizational-memory]] · [[Task Protocol v0.1]]
