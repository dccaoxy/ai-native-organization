# AI-Native Organization Operating Loop v0.2

> 状态：**已确认**  
> 确认日期：2026-09-02  
> 替代：Operating Loop v0.1 中将 Work 表达为组织级普通流程节点的设计

## 三层定义

- **Goal**：组织要实现什么。
- **Task**：组织需要交付什么。
- **Work**：Human + Agent 在 Task 内部自由决定怎么做。

Goal 与 Task 是组织级对象。Work 不是与它们同等级的重型对象，而是 Active Task 内部的 **Free Work Space（自由执行空间）**。

## 主循环

```text
Human / Agent
      ↓
Goal Proposal
      ↓
Human Goal Authority
      ↓ Activate
ACTIVE GOAL
  Outcome / Success Criteria / Boundary / Human Owner
      ↓
Decomposition Trigger
      ↓
Human / Agent Decomposer
      ↓
Task Proposal
      ↓
Goal Alignment + Boundary Validation
      ↓
ACTIVE TASK
  Parent / Purpose
  Expected Output
  Acceptance Criteria
  Boundary
  Due Time
      ↓
TASK BUS
      ↓ Pull / Push
Human / Agent / Human-Agent Unit
      ↓
FREE WORK SPACE
  Workflow / Agent Calls / Tools
  Temporary Subtasks / Exploration / Collaboration
      ↓
Output + Evidence
      ↓
Review: Quality Gate + Learning Gate
      ↓
Acceptance
      ↓
Result
  ├─ Knowledge / Evidence
  ├─ Capability
  └─ New Task
         ↓
  Goal Alignment Check
     ├─ YES → Task Bus
     └─ NO  → Goal Proposal
```

Organizational Memory 不是 Result 后的单一终点，而是贯穿 `Work → Review → Acceptance → Result` 的持续学习层，接收 Candidate Knowledge、New Evidence、Ontology Signal 与 System Learning，并通过各自治理流程进入正式记忆。

任务运行由 [[Task Lease & Progress Protocol v0.1]] 和 [[Time & Recovery Protocol v0.1]] 横向支持；关键事件由待设计的 [[Audit Layer 待设计]] 留痕。

## Free Work Space 的三项约束

1. 不偏离 Task。
2. 不突破 Boundary。
3. 最终产生可验收的 Output + Evidence。

在这三项约束内，Executor Unit 可以自由选择 Workflow、Agent Calls、Tools、Temporary Subtasks、Exploration 与 Collaboration。它们默认不进入组织级 Task Bus。

## Temporary Subtask 的升级规则

临时 Subtask 只有在出现以下任一需要时，才 **Promote to Task**：

- 独立 Executor；
- 独立资源；
- 独立 Acceptance；
- 跨成员协调；
- 独立追踪；
- 对 Goal 产生重要影响。

升级后的路径为：

```text
Temporary Subtask → Promote to Task
→ Task Proposal → Goal Alignment + Boundary Validation
→ Active Task → Task Bus
```

## 版本演进

- **v0.1**：以 `Task Bus → Executor Unit → WORK → Output + Evidence` 表达主链，Work 容易被理解为需要独立协议和组织级治理的对象。
- **v0.2**：保留主链位置，但将 Work 明确降为 Task 内部的 Free Work Space；组织严格管理 Task 的契约、边界、路由与验收，不微观管理执行方法。

关联：[[Goal Protocol v0.1]] · [[Task Protocol v0.1]] · [[Free Work Space Protocol v0.1]] · [[Review Protocol v0.1]] · [[Acceptance Protocol v0.1]] · [[Goal-Task 接口补丁 v0.1]]

## 知识形成、使用与治理的连接（2026-09-04）

Raw Events → Organizational Attention → Observation → Pattern → Hypothesis Cloud ⇄ Evidence ⇄ Verification → Generalization / Scope → Knowledge → Behavior Change → New Events。

Memory → Cognitive Routing → Activation → Context Assembly → Injection → Action → Usage Feedback → New Evidence。知识形成不能跳过证据与 Scope，普通 Knowledge 不自动 OTA；治理后的 Protocol 才通过 Runtime 更新。v0.2 执行主链保持有效。

关联：[[Organizational Learning & Knowledge Formation]] · [[organizational-memory]] · [[Agent Governance & Runtime]]
