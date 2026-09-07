# Goal Protocol v0.1

> 状态：**冻结**
>
> 冻结日期：2026-09-02

## 1. Goal 的定义

> **Goal = 一个具有明确、可验证产出目标的组织目标。**

Goal 描述希望世界发生什么变化，而不是要求某个人执行什么动作。

## 2. Proposal 权与 Activation 权分离

- 任何 **Human** 都可以提出 Goal Proposal。
- 任何 **Agent** 都可以基于观察或 Evidence 提出 Goal Proposal。
- Proposal 不等于组织承诺资源。
- 只有获得授权的 **Human Goal Authority** 可以激活 Goal，并成为或指定 Human Owner。

因此：

```text
Human / Agent → Goal Proposal → Human Review → Reject / Activate
```

目标控制保持在人类责任体系中，机会发现保持分布式。

## 3. Goal Proposal 的最低信息

Proposal 阶段只要求：

1. 发现了什么问题或机会？
2. 如果解决，可能产生什么价值？
3. 建议的可验证 Outcome 是什么？

低门槛是为了避免用复杂立项表堵塞创新入口。

## 4. Active Goal 的最低结构

每个 Active Goal 必须包含：

### Outcome

希望产生什么结果或变化。

### Success Criteria

如何知道 Outcome 已经达到。衡量可以是数字，也可以是可验证的实验结果或证据条件，不强制等同于 KPI。

### Boundary

根据需要声明时间、预算、数据权限、人员、合规红线、风险和不可触碰事项。没有特殊限制时不增加形式字段。

### Human Owner

对最终 Outcome 和关键判断负责的人。Owner 不等于日常派活的 Project Manager，其核心责任包括修改、暂停、终止、资源追加、Challenge 判断和最终结果责任。

```text
Active Goal = Outcome + Success Criteria + Boundary + Human Owner
```

## 5. Goal 不包含 Solution

错误示例：

> 建立一个 AI Agent 来提高新人培训效率。

更好的 Goal：

> 将新人达到指定能力标准的平均时间降低 30%。

Agent、导师、知识库、课程改变或其他路径均由后续探索决定。Goal 不写死 Solution 或 Workflow。

## 6. Evidence Challenge

任何 Human 或 Agent 都可以基于 Evidence Challenge 一个 Active Goal，例如指标失效、环境变化、核心假设被否定或边界已不合理。

Human Owner 对 Challenge 作出：

`Keep / Modify / Pause / Achieve / Terminate / Supersede`

Challenge 必须附带可检查依据，不能仅以偏好改变目标。

## 7. 生命周期

```text
Proposed → Active → Achieved
                  → Paused
                  → Failed
                  → Cancelled / Terminated
                  → Superseded
```

- **Achieved**：Success Criteria 已满足并完成授权确认。
- **Paused**：暂时停止资源投入，保留恢复可能。
- **Failed**：Evidence 表明 Outcome 未实现，且继续投入已无合理成功预期。
- **Terminated/Cancelled**：不能据此断定成败，但因环境、资源或价值变化停止投入。
- **Superseded**：由新 Goal 取代，并需重新评估下游 Task。

探索性 Goal 即使 Failed，只要留下高质量 Evidence 与 Knowledge，仍可能具有重要组织价值。

## 2026-09-04 基线复核

历史字段 Measure 已由 **Success Criteria** 取代；数字指标、实验结果和可检查证据均可用，不强制 KPI 化。现行正文与 [[Acceptance Protocol v0.1]] 保持一致。
