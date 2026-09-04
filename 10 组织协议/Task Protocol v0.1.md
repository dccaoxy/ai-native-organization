# Task Protocol v0.1

> 状态：**冻结**
>
> 冻结日期：2026-09-02

## 1. Task 的定义

> **Task = 为推动某个 Goal 向前发展，需要 Human 或 Agent 完成，并能够产生可验收结果的最小工作单元。**

Task 是结果单元，不是动作清单。它回答“现在需要交付什么”，而不是“具体怎么做”。

## 2. 合法 Task 的最低要求

1. **Parent / Purpose**：至少追溯到 Goal、Parent Task、Experiment 或 Incident，并说明如何推进 Parent Goal。
2. **Expected Output**：最终必须交付什么。
3. **Acceptance Criteria**：从 Parent Goal Success Criteria 推导，Reviewer 据此判断 Pass 或 Retry。
4. **Boundary**：必要时声明 Resource、Permission 与 Risk。
5. **Due Time**：最晚何时提交 Output + Evidence。

## 3. Task Decomposition 是 Capability

Human、Agent 或 Human-Agent Unit 都可以拆 Task。谁来拆取决于谁更适合当前问题，而不是职位权力。系统应从真实结果中学习 Decomposition Capability。

## 4. Progressive Decomposition

Goal 启动时不要求一次拆完未来所有 Task。第一批 Task 执行后产生的新 Evidence 可以继续生长出后续 Task。

> **Goal 相对稳定，Task Graph 动态生长。**

## 5. Proposal、Validation 与 Active Task

```text
Task Proposal → Validation → Active Task → Task Bus
```

Validation 至少检查：

- 是否服务当前 Goal；
- Expected Output 与 Acceptance Criteria 是否明确；
- 是否重复；
- 是否超出资源、权限或风险边界。

低风险、低资源且在边界内的 Task 可以自动激活。超过边界必须 Escalate 给 Human Approval。

## 6. Routing：Pull + Push + Failover

### Pull

Human 或 Agent 主动领取。系统可以依据 Capability、Workload、Learning Need、Reputation 与 Interest 推荐；符合边界者仍可申请未被推荐的 Task。

### Push

紧急、关键路径、无人领取或能力明确匹配的 Task 可以由系统主动派发。

### ACK 与 Failover

`Assigned ≠ Accepted`。Push 必须经过：

```text
Assigned → Acknowledged → In Progress
```

超过 Acknowledgement SLA 未 ACK 时，系统 Re-route 到下一候选人；连续失败后才 Human Escalation。

## 6A. Time、Task Lease 与 Recovery

每个 Active Task 必须有 Due Time；Push Task 必须有 ACK SLA。执行期间监测 Task Lease 与可信 Progress Signal，而不是分布式 Agent 是否在线。无可信进展时进入 Stalled Candidate；到期未提交时进入 Overdue Review，由 Task Orchestrator 选择 `Extend / Re-scope / Reassign / Escalate / Terminate`。详见 [[Time & Recovery Protocol v0.1]] 与 [[Task Lease & Progress Protocol v0.1]]。

## 7. Executor 可以 Reject

Reject 必须附带理由，如能力不匹配、负载过高、缺少资源、边界或验收不清、Task 重复或 Task 本身有问题。

同一 Task 被多人连续 Reject 时触发 Task Quality Review，必要时返回 Decomposer；不能无限寻找第 N 个执行者。Reject 是组织学习数据。

## 8. Human WIP = 1

第一阶段新人组织默认：

> **一个 Human 同时只拥有一个 Active Task；Finish before Start。**

这限制的是 Human Attention，不限制受监督的 Agent 执行。Human Task 下可有多个 Agent Subtask。

## 9. Agent 并发受 Human Oversight 约束

系统必须区分 Execution Capability Requirement 与 Oversight Capability Requirement。Agent 能力高，不代表负责 Human 能可靠发现错误。

Agent Parallelism、Task Complexity、Risk Boundary 与未来 Human WIP 只能随经真实任务验证的 Oversight Capability 逐步提高。

## 10. Work 不写死

Task 定义 What，不规定 How。执行者可选择 Agent、工具、Subtask、研究、实验及协作方法，只要不突破边界。

Operating Loop v0.2 进一步明确：Task Bus 路由给 Human / Agent / Human-Agent Unit 后，进入 Task 内部的 Free Work Space。Workflow、Agent Calls、Tools、Temporary Subtasks、Exploration 与 Collaboration 默认不进入组织级 Task Bus。

Temporary Subtask 只有在需要独立 Executor、独立资源、独立 Acceptance、跨成员协调、独立追踪或对 Goal 产生重要影响时，才 Promote to Task，并重新经过 `Task Proposal → Goal Alignment + Boundary Validation → Active Task → Task Bus`。

## 11. Output + Evidence

执行者提交 Expected Output，同时提交 Evidence：能够让 Reviewer 独立判断 Acceptance Criteria 是否满足的可检查依据。

Evidence 可以是数据、文档、代码、实验、用户反馈、测试、日志、Artifact 或其他 Task Output。Evidence Requirement 应尽量在工作开始前明确，不能在提交后临时改变标准。

## 12. Submitted 不等于 Completed

```text
In Progress → Submitted → Review → Accepted → Closed
```

Submitted 只表示执行者认为已完成。只有满足 Acceptance Criteria 并经过授权 Acceptance 后，Task 才能 Closed。

## 13. Agent-first Review

所有 Task 默认先由独立 Review Agent 检查，不允许执行 Agent 仅靠自检完成闭环。

Review Agent 可以：

`Pass / Retry / Escalate / Unable to Reliably Judge`

Review 同时是 Quality Gate 与 Learning Gate；Hard Review 检查 Completeness、Compliance、Evidence、Correctness、Risk，Confidence 作为元数据。Learning Gate 捕获 New Knowledge、New Evidence、Ontology Signal 与 System Learning，详见 [[Review Protocol v0.1]]。

## 14. Acceptance：Risk × Verifiability

| Task 类型 | Review | Acceptance |
|---|---|---|
| 低风险、易验证 | 独立 Agent | Agent Auto-Accept |
| 中等风险或判断复杂 | 独立 Agent | Human |
| 高风险或重大决策 | Agent + 专项检查 | Human Decision Owner |

Human Attention 集中在机器无法可靠闭环的节点。

Acceptance Criteria 从 Goal Success Criteria 向下推导，采用 Hard Gates + Judgment；Task Active 后默认冻结，修改必须记录 Version、Reason 与 Audit Trail。详见 [[Acceptance Protocol v0.1]]。

## 15. 异常状态

- **Retry**：未达到标准，但继续执行仍有合理成功可能。
- **Blocked**：因资源、权限、信息或上游依赖暂时无法继续。
- **Escalated**：超出当前 Unit 的能力、权限或风险边界。
- **Failed**：合理恢复尝试后仍无法合理预期成功，或 Evidence 否定核心假设。
- **Terminated**：不能证明成败，但因 Goal、环境、资源或价值变化停止投入。

`Review Failed ≠ Task Failed`；Review 未通过通常进入 Retry。

## 16. Failure Record

Failed Task 必须产生结构化 Failure Record，至少记录：

- 原 Task、Expected Output 与 Acceptance Criteria；
- 已进行的合理尝试、Retry、Re-route 与 Escalation；
- 关键 Evidence；
- 失败原因与被否定的假设；
- 可复用教训、后续建议与仍有价值的 Artifact。

Failure Record 不用于追责，而用于阻止重复失败并形成 Knowledge。

## 17. Task 结果闭环

无论 Accepted、Failed 或 Terminated，Task 都应触发必要的闭环更新：

- **Knowledge**：产生、验证、修正或淘汰了什么组织知识；
- **Capability**：执行者、Reviewer 和 Human-Agent Unit 的什么能力获得了证据；
- **Contribution**：哪些可归因贡献值得被组织识别；
- **Routing**：哪些任务类型与执行者、Reviewer 或 Agent 更匹配；
- **New Task / Goal Proposal**：是否出现后续工作或新的方向。

Task 完成不是信息终点，而是组织学习循环的输入。

关联：[[Operating Loop v0.2]]。
