# Minimum Viable Organization v0.1

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 928216ea](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-928216ea-1697-4534-bc99-bb116fd440e0)。

# M0 — Day-One Critical
## 第一天必须存在

### 1. Human / HAU Identity

必须能建立：

> Human ID
> HAU ID
> Representative Agent Binding

系统知道：

> 谁是谁；
> 哪个 Agent代表哪个 Human；
> 当前哪个 Representative Agent是 Active。

不需要第一天就有复杂 Human Model。

---

### 2. Goal

至少能够表达：

> Desired Change
> Success Criteria
> Boundary
> Human Goal Authority
> Status

第一天甚至不需要复杂 Goal Graph。

但：

> **没有 Goal 就不能正式产生 Task。**

---

### 3. Task + Execution

这是整个系统的核心工作对象。

必须正式分开：

> **Task = shared intent / contract**
> **Execution = one attempt**

Task至少：

> Primary Goal
> Expected Output
> Acceptance Criteria
> Boundary
> Execution Mode

Execution至少：

> Executor / HAU
> Human Accountable Owner
> Status
> Runtime Boundary
> Time

---

### 4. Task Bus

第一天必须能够：

> Publish
> Browse / Discover
> Claim
> Create Execution

不需要第一天就有：

> AI智能推荐；
> Capability Match；
> 动态赏金算法。

最简单：

> 一面真正能领取任务的“墙”。

就够了。

---

### 5. 最小 Execution Protocol

必须有共同语言：

> `Claim`
> `ACK（确认收到）`
> `Progress`
> `Blocked`
> `Need Help / Escalate`
> `Submit`
> `Fail`
> `Release`

这是 Reliability能够成立的最小基础。

第一天就不能允许：

> Task领取以后消失。

---

### 6. Free Work Space

这不是一个需要大量开发的“功能”，而是一条**系统边界**。

第一天就要保证：

> HAU领取 Execution以后，中央系统不要求上传所有工作过程。

只要求必要状态和正式 Return。

否则我们的实验从第一天就违背 L1。

---

### 7. Boundary / Escalation

第一天至少需要：

> 当前 Execution Boundary
> Boundary Request
> Human Authority Routing

不需要完整 Risk Engine（风险引擎）。

但必须做到：

> Agent / HAU知道什么时候已经越界，以及如何回来申请。

---

### 8. Task Return

这是第一天绝对不能缺的。

Execution结束：

> 成功或者失败

都必须有标准化 Return。

最小可以只有：

> Result
> Observed Terrain
> Major Execution Facts
> Reflection

Human：

> Confirm / Correct / Add。

这是后面所有 Learning的原料。

---

### 9. Review + Acceptance

至少需要：

> Review：Result可信吗？
> Acceptance：满足Task用途吗？

Parallel Execution如果已经允许：

> Selection也需要最小实现。

否则赏金酒馆只能领任务，不能真正闭环。

---

### 10. Organizational Event

第一天必须统一 Event模型。

至少记录：

> Goal Activated
> Task Created
> Execution Claimed
> ACK
> Blocked
> Boundary Requested / Changed
> Result Submitted
> Review
> Acceptance
> Execution Closed

这就是：

> **Organizational Reality最初的时间骨架。**

如果第一天不统一，后面再补 Event Store会非常痛苦。

---

### 11. Human Accountability

每个 Execution创建时：

> **必须立即解析唯一 Human Accountable Owner。**

不能说：

> “自动化以后再补责任系统。”

这是 Foundational Principle。

---

# 到这里，其实组织已经可以跑了

M0形成：

```text id="70n7r8"
Human
  ↓
HAU + Representative Agent
  ↓
Goal
  ↓
Task Bus
  ↓
Task
  ↓
Claim
  ↓
Execution
  ↓
ACK
  ↓
════════════════
 Free Work Space
════════════════
  ↓
Progress / Blocked /
Boundary Request
  ↓
Task Return
  ↓
Review
  ↓
Acceptance
  ↓
Result / Failure
  ↓
Organizational Events
```

这已经是一个真正不同于传统项目管理软件的最小 AI-native Organization。

---

# M1 — Learning Critical
## 可以晚一点，但必须尽快补上

如果 M0运行一个月而 M1还没有：

> 我们会积累大量工作，却没有真正形成 Organizational Learning。

所以这部分应该是紧接 M0 的第二建设优先级。

### 1. Experience / Evidence Layer

把：

> Task Return + Result + Review + Event

组织成可查询 Experience。

---

### 2. Knowledge Formation

最小支持：

> Observation
> Evidence
> Hypothesis
> Knowledge Candidate
> Scope / Boundary
> Challenge

不需要第一天就有复杂 Knowledge Graph。

---

### 3. Knowledge Activation

Representative Agent开始能够：

> 根据 Execution Context 查询相关 Organizational Knowledge。

这是 Knowledge真正产生价值的地方。

---

### 4. Capability Evidence

从 Execution Return自动形成：

> HAU Capability Evidence
> Terrain Evidence

开始点亮地图。

---

### 5. HAU Capability Map

第一版甚至可以很朴素：

> 不需要3D世界。

只要系统知道：

> 哪些 Terrain走过；
> 成功 / 失败；
> Context是什么。

---

### 6. Capability Capture

第一次成功以后：

> 开始提取 Knowledge / Data / Tool / Practice / Review / Oversight。

形成：

> Capability Candidate。

---

### 7. Contribution Ledger

开始从共享 Reality中识别：

> Result / Learning / Capability / Protection / Enablement Contribution。

第一阶段：

> **只记录，不急着发复杂奖励。**

这一点非常重要。

---

### 8. Dependency Graph

我认为这个应该属于 **M1早期**，而不是 M2。

因为 Knowledge / Capability一旦开始运行：

> 就必须知道谁依赖谁。

但 M0第一周如果只有很少 Knowledge：

> 可以先没有完整 Dependency Graph。

---

### 9. Minimal Human Model

从真实 Execution行为开始积累：

> Observed Behavior。

仍然不需要复杂人格模型。

---

# M2 — Scaling / Experience
## 有意晚一点做

这一层很多东西非常诱人。

但我反而建议：

> **故意不要第一天做。**

因为我们需要先看真实组织怎么长。

---

### Knowledge Pulse

设计已经定义。

但应该等：

> Knowledge真正开始产生以后

再实现。

否则第一天根本没有东西值得 Pulse。

---

### Collective Valuation + Reward Pool

Contribution Ledger先跑几个 Cycle。

先看看：

> 真实 Contribution到底长什么样。

然后再开始：

> Blind Valuation
> Scarcity / Saturation
> Reward Pool。

否则我们会太早改变 Human行为。

---

### Honor Hall

更应该晚。

因为：

> **组织还没有历史的时候，不应该提前制造历史。**

先让真正值得记住的 Event发生。

---

### Progression / Badge

Badge可以比较早加入产品体验。

但我仍建议：

> 第一批真实行为数据出来以后再设计第一批 Badge。

否则我们会提前告诉大家：

> “你们应该怎样玩这个游戏。”

---

### Capability-based Auto Execution

必须晚。

因为组织第一天：

> 根本没有成熟 Organizational Capability。

这正好与你之前说的一致。

先让 HAU做。

等真的：

> Reproduce → Revalidate → Oversight下降

再让 Organization-owned Agent接管。

---

### Advanced Organization-owned Agents

例如：

> Autonomous Task Orchestrator
> Knowledge Agent
> Risk Agent

第一阶段都不必很强。

甚至很多功能：

> 先由普通后台 AI + Human完成。

等我们知道真实 Pattern以后再独立成 Agent。

---

### Full Risk Governance

第一天需要：

> Boundary + Escalation。

但复杂：

> Risk Object
> Consequence Routing
> Change Set Governance
> Advanced Authority Registry

可以逐渐长出来。

---

### Interactive 3D / HTML Organization Atlas

属于：

> Experience / Comprehension Layer。

很有价值。

但绝不是运行闭环依赖。

---

# 一个我认为很重要的实施原则

经过这个检查，我觉得可以增加一个 Launch Principle（上线原则），但它不是新的 L1：

> **Build the loop before building the intelligence.**
>
> **先把闭环建起来，再给闭环增加智能。**

例如：

Task Bus第一天：

> 不需要最聪明的AI推荐。

但必须：

> Claim → ACK → Execution → Return → Review → Acceptance

真正闭环。

Knowledge第一版：

> 不需要自动推理出完美 Knowledge。

但必须：

> Experience → Evidence → Knowledge Candidate → Activation

闭环。

Capability第一版：

> 不需要漂亮3D地图。

但必须：

> Execution → Evidence → Map Update → Capture → Reproduction

闭环。

---

# 第二个实施原则

> **Capture before optimize.**
>
> **先保证关键事实被正确捕获，再优化算法。**

因为第一年最大的资产可能不是软件本身，而是：

> 60个 Human + Agent真实运行产生的高质量 Organizational Events。

如果我们第一天 UI很漂亮，但：

> Execution / Boundary / Task Return / Review / Evidence

没有正确结构化记录，

一年以后：

> 很多最珍贵的实验数据已经永远丢了。

所以 M0里 Event Model和 Task Return的优先级反而非常高。

---

# Minimum Viable Organization Check：通过

我现在的判断是：

> **我们的 Operating Model 可以被切成一个非常小的 Day-One Loop，而不违反完整设计。**

这是一个很重要的验证。

说明这套架构不是：

> “只有全部100个功能做完才能运行。”

而是可以：

> **M0先活起来 → M1开始学习 → M2开始产生规模化智能和文化。**

而且每一步都沿同一套 Foundational Principles成长，不需要以后推翻重建。

---


## 当前实现状态

以上是冻结设计的Launch Scope，当前文档收敛不证明任何M0功能已经上线。Atlas体验属于M2，本轮只准备信息拓扑。
