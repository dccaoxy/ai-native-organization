# Free Work Space Protocol v0.1

> 状态：**冻结**  
> 冻结日期：2026-09-02

## 定位

Goal 与 Task 是组织级对象；Work 是 Active Task 内部的 **Free Work Space**，不作为同等级的重型对象。Human / Agent / Human-Agent Unit 可自主决定 Workflow、Agent Calls、Tools、Temporary Subtasks、Exploration 与 Collaboration。

Free Work Space 只有三项硬约束：不偏离 Task；不突破 Boundary；最终产生可验收的 Output + Evidence。

## 六类 Escalation Triggers

1. **Boundary Trigger**：即将突破预算、时间、权限、数据或风险边界 → `Pause / Escalate`。
2. **Capability Trigger**：Human 已无法可靠理解、监督或验收 Agent 的工作 → 停止扩大能力或并发并升级。
3. **Task Trigger**：工作需要独立 Executor、资源、Acceptance、跨成员协调、独立追踪，或对 Goal 有重要影响 → `Promote to Task Proposal`。
4. **Goal Trigger**：当前 Task 已无法有效推进 Goal，或出现超出当前 Goal 的重要机会 → `Goal Challenge / New Goal Proposal`。
5. **Knowledge Trigger**：产生可复用的经验、方法、失败、Evidence 或发现 → `Candidate Knowledge → Knowledge Commit`。
6. **Risk / Exception Trigger**：发现未识别的重大风险、异常或不可逆操作 → 立即停止自动执行并升级 Human。

除触发以上条件外，默认不升级：`Default = Do not escalate`。

## 两类出口

```text
正常：Free Work Space → Output + Evidence → Submit
冒泡：Free Work Space → Trigger → Task / Goal / Knowledge / Human
```

关联：[[Operating Loop v0.2]] · [[Task Protocol v0.1]] · [[organizational-memory]]

## 知识注入边界

**Inject cognition, not workflow**。普通 Knowledge 提供认知、Scope 与 Caution；不写死执行步骤。更强行为约束需治理，当前见 [[Knowledge to Behavior - Behavioral Authority]]。
