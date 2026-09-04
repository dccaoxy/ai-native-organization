# Time & Recovery Protocol v0.1

> 状态：**冻结**  
> 冻结日期：2026-09-02

## Time Contract

每个 Active Task 必须有 **Due Time**。Push Task 还必须有 **ACK SLA**。自由执行不等于无限时间：Task Contract 管理 `WHAT / GOOD / BOUNDARY / WHEN`，HOW 留在 Free Work Space。

```text
Assigned → ACK SLA → Acknowledged → In Progress
→ Progress Checkpoint(s) → Due Time → Submitted
```

## 三个时间闸门

1. **ACK SLA**：确认任务是否被真正接住；超时可 Re-route / Secondary Assignment。
2. **Progress Monitoring**：依据 Artifact、Evidence、Checkpoint、依赖推进、状态更新等可信信号判断是否推进，不依赖 Human 日报。
3. **Due Time**：到期未 Submitted 时进入 **Overdue Review**，不直接判定 Failed 或自动改派。

长时间无可信进展时标记 **Stalled Candidate**，交由 Task Orchestrator 诊断。Overdue Review 根据原因选择：

`Extend / Re-scope / Reassign / Escalate / Terminate`

只有确认原 Executor 已不再是成本最低、成功概率最高的恢复路径时，才 Reassign。

## 待研究指标

- MTTD：Mean Time to Detect，异常平均发现时间。
- MTTR：Mean Time to Recover，异常后恢复有效执行的平均时间。

关联：[[Task Lease & Progress Protocol v0.1]] · [[Task Protocol v0.1]]
