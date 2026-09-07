# Ontology / Graph 原则

- 状态：设计原则已确认；v0.1 尚未建模

## Ontology 与 Graph

> Ontology = 规则；Graph = 按这些规则连接起来的实例世界。

Ontology 定义对象类型、字段、关系与约束。Graph 让真实 Goal、Task、Person、Agent、Knowledge、Evidence 等实例按这些规则持续连接。

## 两层 Graph

1. 类型层 Graph：组织世界模型，先定义少量核心对象与允许关系。
2. 实例层 Graph：随真实工作自动长出，不由人提前画完。

第一版候选骨架：

```text
Goal → contains → Task
Task → executed_by → Person / Agent
Task → requires → Capability
Task → uses → Knowledge
Task → produces → Artifact
Task → creates → Evidence
Task → contains → Free Work Space
Evidence → supports → Decision
Task / Experiment → generates → Knowledge
Person / Agent → owns → Capability
Person / Agent → contributes → Knowledge
Knowledge → supersedes → Knowledge
Review / Feedback → Learning → Capability
```

## 设计原则

- 不以传统 Org Chart 为骨架；“属于哪个部门、汇报给谁”只是 Person 的部分关系。
- 起点是 Goal，首先描述价值如何产生，而不是谁管谁。
- 每增加一种 Node 或 Edge，都要说明缺少它会失去什么实际能力。
- 从一个真实任务完整走查反推最小 Node + Edge。
- 先画最小 Graph，运行真实任务，再迭代 Ontology。
- Personal Agent 可以挑战 Ontology，但不能直接修改。
- Ontology 由中央维护并版本化，保留迁移记录。

## 核心对象候选

Goal、Task、Person、Agent、Capability、Knowledge、Artifact、Evidence、Decision、Experiment、Resource、Risk。

Work / Workflow / Agent Call / Temporary Subtask 默认不是组织级核心对象或 Task Bus 节点；必要过程可以作为 Task 内部运行记录。Temporary Subtask 只有满足 [[Operating Loop v0.2]] 的升级条件后，才成为正式 Task 与 Graph 节点。

## 下一设计产物

Ontology v0.1 类型关系图应与 Operating Model 和一个真实 Reference Workflow 互相校验；在这之前不急于选数据库或开发知识图谱系统。

来源：[[05项目/AI Native组织/80 原始讨论/探讨AI原生组织-raw-conversation|原始对话]]。

## 2026-09-04 建模边界

最小原型候选进一步包含 Human-Agent Unit、Task Lease、Review、Acceptance、Event、Observation、Pattern、Hypothesis 与 Scope。以上是建模候选，不能将未冻结的 Schema 当作确定实现规范。

Knowledge 间关联、三层 Memory 与 Evidence Provenance 需要相连；Task 产生的是结果与候选经验，经认知闸门才晋升为正式 Knowledge。见 [[Organizational Learning & Knowledge Formation]] 与 [[设计与开发轨道]]。
