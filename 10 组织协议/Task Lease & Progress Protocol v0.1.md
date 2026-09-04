# Task Lease & Progress Protocol v0.1

> 状态：**冻结**  
> 冻结日期：2026-09-02

## 核心原则

> 组织不监控分布式 Agent 是否在线，而监控 Task 是否仍被有效持有，以及是否存在可信进展。

```text
Task Lease → ACK → heartbeat / event → Progress Signal
→ Checkpoint → Submit
```

Agent Process 在线不等于 Task 有效推进。可信 Progress Signal 可包括新增 Artifact、Evidence、Checkpoint、依赖推进、相关 Knowledge 调用或中间结果。

## Task Orchestrator

Task Orchestrator 负责 ACK、heartbeat-events、progress、checkpoint、submit 的协议状态；识别 Stalled Candidate；诊断依赖、资源、Task 定义、Executor 响应或能力问题；优先自动恢复和 re-route，必要时才 Human escalation。

恢复遵循最低可处理层级：

1. **L1 Orchestrator**：提醒、状态确认、依赖处理、资源补充、恢复或重新路由。
2. **L2 Human Executor**：确认继续、Blocked、需资源、需延期或无法完成。
3. **L3 Human Authority**：仅处理增加资源、突破 Boundary、修改 Acceptance Criteria、重大延期/风险或 Goal Alignment 等责任判断。

## 三级接入

| 等级 | 可见性与责任 |
|---|---|
| Managed Agent | 完整接入 Task Bus，可报告状态、事件、输出和资源消耗 |
| Connected Agent | 可提交状态和结果，但中央系统不可见完整运行过程 |
| Unmanaged Personal Agent | 不作为独立组织节点；由 Human 持有 Task Lease、ACK、Checkpoint 与 Submit |

关联：[[Time & Recovery Protocol v0.1]] · [[Task Protocol v0.1]] · [[Operating Loop v0.2]]

## 当前架构关联

[[Task Orchestrator]] 汇总恢复职责；Checkpoint 可支持 [[Knowledge Injection 与同步边界|Context Delta 检查]]，但知识调用或 heartbeat 本身不能自动证明任务有效推进。组织运行层归入 [[Agent Governance & Runtime]]。
