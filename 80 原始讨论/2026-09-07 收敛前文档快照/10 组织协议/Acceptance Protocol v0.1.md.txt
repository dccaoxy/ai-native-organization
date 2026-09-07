# Acceptance Protocol v0.1

> 状态：**冻结**  
> 冻结日期：2026-09-02

## 验收链

```text
Goal Success Criteria
→ Task Acceptance Criteria
→ Output + Evidence
→ Review
→ Acceptance
→ Result 正式生效
```

Goal 的 `Measure` 正式改名为 **Success Criteria**。Task Decomposer 不只拆工作，还必须把 Goal Success Criteria 转化为可验证、能解释其贡献关系的 Task Acceptance Criteria。

## Hard Gates + Judgment

Acceptance 不另造一套事后综合评分：

- Hard Criteria 必须全部通过，不能由其他高分抵消；
- Judgment Criteria 可由 Agent 辅助评估，但高判断性任务由 Human Acceptor 决定并记录 Reason；
- 低风险、高可验证 Task 可 `Review Pass → Agent Auto-Accept`；
- 高风险、重大影响或高判断 Task 必须 Human Acceptance。

Task Active 后 Acceptance Criteria 默认冻结。确需修改必须记录 `Version + Reason + Audit Trail`，不得事后移动标准。

## 与 Review、Audit 的边界

- Review 回答“有没有问题”；Acceptance 回答“是否授权结果正式生效”。
- Acceptance 是业务生效机制，不等于 Audit。
- Acceptance 必须被 Audit：记录接受者、时间、标准版本、Review、Evidence、Override 与 Reason。

关联：[[Review Protocol v0.1]] · [[Goal Protocol v0.1]] · [[Task Protocol v0.1]]
