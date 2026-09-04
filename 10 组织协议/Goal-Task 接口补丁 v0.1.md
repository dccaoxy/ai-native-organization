# Goal–Task 接口补丁 v0.1

> 状态：**冻结**
>
> 目的：修补 Goal Protocol v0.1 与 Task Protocol v0.1 之间的四个接口断点。

## 补丁 1：Active Goal 自动触发 Decomposition

Goal 不能直接进入 Task Bus。正确链路是：

```text
Goal Proposal → Human Activate → Active Goal
→ Decomposition Trigger → Task Proposal → Validation
→ Active Task → Task Bus
```

每个 Active Goal 必须有 Decomposition Trigger。系统负责寻找合适的 Human、Agent 或 Human-Agent Decomposer，并确保第一批 Task Proposal 实际产生；Human Owner 不必亲自拆解。

## 补丁 2：统一责任角色命名

- **Goal Owner**：Human，对最终 Outcome 负责。
- **Task Executor**：Human、Agent 或 Human-Agent Unit，对 Expected Output 负责。
- **Reviewer**：对 Review 判断负责。
- **Acceptor**：对是否接受结果负责。

Task 不再使用 Owner 一词，避免把结果责任、执行责任与验收责任混在一起。

## 补丁 3：Goal Alignment Check

每个新 Task 必须回答：

> 这个 Task 如何推进 Parent Goal？

```text
新发现 → 仍服务当前 Goal？
              ├─ 是 → New Task → Validation
              └─ 否 → New Goal Proposal
```

这既允许探索自由生长，也防止 Task Graph 悄悄把 Goal A 漂移成 Goal B。

## 补丁 4：Goal 状态变化触发下游 Task Re-evaluation

- **Goal Pause**：下游 Task 默认进入 `Pause Pending Review`。
- **Goal Terminated**：停止新领取和派发，逐项决定 `Terminate / Preserve / Re-parent`。
- **Goal Modified**：所有下游 Task 重新执行 Goal Alignment Check。
- **Goal Superseded**：评估 Task 是否迁移到新 Goal。

系统不能简单 Kill 所有 Task，因为既有投入、Evidence 与 Artifact 可能仍然有价值。
