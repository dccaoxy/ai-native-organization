# Final Design Baseline — 原始讨论增量

来源对话：6a964c7e-f220-83e8-85f2-bb064cd1ace1，《AI native 设计》。

本档案保留最终收敛相关轮次的原文、角色、时间与 ID；包含中间提议和后续修正，不能把单条历史提议当最终规范。仅归档本轮相关增量，不宣称历史对话及附件已完整恢复；附件未复制。对已存原文的 Turn ID 做去重。

## turn-3ebfd1bd-ce65-4ced-b09e-72b8575a5941

时间：2026-09-06T15:16:53.566525+08:00

### Human

Message ID：`3ebfd1bd-ce65-4ced-b09e-72b8575a5941`

我同意

---

### Assistant

Message ID：`75a6d093-f968-479c-912c-7bfc5bbb94ad`

好，那这一层也固定：

> **Protocol Governance（协议治理）是规则层的最高治理权，但不是组织的最终最高权力。**

其上保留一层非常薄的：

> **Foundational / Constitutional Governance（基础原则 / 宪制治理）**

它不负责日常运行，只保存那些**普通 Protocol 无权自行改变的组织基本原则**。

目前已经自然形成的候选包括：

> Human 保留最终 Goal Authority；每个 Task / Execution 必须唯一解析到 Human 最终责任人；Boundary 内默认自主；任何 Authority 必须有可追溯来源；任何 Actor 不能替自己无权代表的后果承担者接受风险；Free Work Space 不被全面监控。

下面则是：

> **Protocol Governance → Operational Governance（日常运行治理）→ Autonomous Operation（自主运行）**

同时明确：

> **OTA（协议远程更新）负责传播规则；Protocol Governance 决定什么规则有资格被传播；Foundational Principles（基础原则）约束普通 Protocol 能改变什么。**

到这里，最后的 **Governance / Audit / Risk** 模块其实已经只剩下 Protocol Governance 的具体变更机制需要收尾：**一条 Protocol 是如何被提出、验证、批准、发布、观察效果，以及必要时回滚的。**把这条生命周期钉住，我们就可以对整个最后模块以及 Operating Model v0.1 做总收敛。

---

## turn-224fea28-88f3-4daf-bc21-08499135b77f

时间：2026-09-06T15:17:55.631691+08:00

### Human

Message ID：`224fea28-88f3-4daf-bc21-08499135b77f`

Protocol 诞生之初的目的是什么

---

### Assistant

Message ID：`bad95f61-fcf8-4b00-ad9a-1e21c22d371a`

这个问题非常值得退回去，因为如果不知道 Protocol（协议）为什么存在，我们很容易把 Protocol Governance 设计成“制度管理”。

如果回到这个词最初的含义，**Protocol 本质上不是 SOP，也不是规章制度。**

它最核心的目的其实是：

> **让多个彼此独立的主体，在不需要每次重新协商的情况下，可以可靠地协同。**

比如互联网里的通信协议就是最典型的例子。

两台机器不需要认识彼此，也不用每次通信之前讨论：

> “你准备怎么发？我怎么确认？失败怎么办？”

因为双方事先遵循共同 Protocol：

> 消息长什么样、怎么发送、怎么确认、错误怎么办……

于是：

> **陌生主体之间产生了可预测的协作。**

这可能就是 Protocol 最本质的价值。

---

### 放回我们的 AI-native 组织

我们为什么最开始需要 Goal Protocol、Task Protocol、ACK、Task Lease、Progress、Escalation？

并不是为了：

> **管员工。**

而是因为我们的组织非常松散：

> Human不同；  
> Representative Agent不同；  
> Private Agent不同；  
> 模型不同；  
> 工作方法不同；  
> HAU之间甚至不需要彼此认识。

但 HAU-012 把一个 Result 交回 Task Bus 时，组织必须理解它。

Task Bus 把 Task 给 HAU-027 时，对方必须知道：

> 这意味着什么。

Agent说：

> `ACK`

组织知道：

> “它已经收到了，并开始承担持续回应义务。”

Agent说：

> `Blocked`

系统知道该发生什么。

这就是 Protocol 的价值：

> **它在高度自由的主体之间建立最小的共同语言和行为预期。**

---

## 所以 Protocol 和 Workflow 的区别就更清楚了

**Workflow（工作流程）**告诉你：

> **事情应该怎么做。**

例如：

> 第一步查资料 → 第二步分析 → 第三步写报告 → 第四步 Review。

而 **Protocol** 告诉你：

> **当你需要和组织发生关系时，我们彼此如何理解对方。**

例如：

> 领取 Task 要 ACK；  
> 无法继续要 Escalate；  
> 需要突破 Boundary 要申请；  
> Submit 要符合某种接口；  
> Task结束要 Return。

至于中间：

> 你怎么查、用几个 Agent、先分析还是先实验，

Protocol 不管。

这正是为什么我们一直强调：

> **Protocol fixed, Workflow free.**
>
> **协议统一，工作方式自由。**

---

## 再往深一点，我认为 Protocol 解决三个问题

**Interoperability（互操作性）**

> 不同 Human / Agent / System 能不能彼此协作？

比如换一个 Representative Agent，仍然能接入 Task Bus，因为它懂同一个 Protocol。

**Predictability（可预期性）**

> 我把东西交给你以后，能不能大概知道接下来会发生什么？

这和刚才 Reliability 的定义直接相关。

不是保证：

> “你一定成功。”

而是保证：

> **“你一定回应。”**

**Coordination without central control（无中央微观控制的协同）**

这个对我们的组织尤其重要。

如果没有 Protocol，要让60个 HAU协调，就需要大量 Manager不断告诉大家：

> 你现在该干什么；  
> 你要向谁汇报；  
> 出问题找谁；  
> 怎么提交。

有 Protocol以后：

> **系统不需要管理每一次行为。**

大家自己按照共同接口运行。

---

# 所以我现在反而想给我们自己的 Protocol 一个正式定义

> **Organizational Protocol = 一组最小的共享规则、状态和接口，使彼此独立的 Human、Agent 与系统能够在保留内部自主性的同时，可靠地理解彼此、交换状态并协同行动。**

注意几个词：

> **最小** —— 不把所有东西都规定掉。
>
> **共享** —— 所有人理解同一种组织语言。
>
> **接口** —— 规定彼此发生关系的地方。
>
> **自主性** —— 不侵入 Free Work Space。
>
> **可靠协同** —— 最终目的。

---

这样一来，我们刚才讨论 Protocol Governance 时，有一个判断标准就突然非常清楚了：

> **不是发现一种“更好的工作方法”，就应该产生 Protocol。**

更好的工作方法首先应该：

> **Knowledge / Recommend / Capability Package。**

只有当组织发现：

> **如果大家不共同遵守某条交互规则，跨 HAU / Human / Agent 的可靠协同就会受损；**

或者：

> **为了保护共同 Boundary，所有 Actor 必须遵守某个最低行为规则；**

才真正有理由把它升级为：

> **Protocol。**

比如：

> “多 Agent Research质量更高。”

不是 Protocol。

最多 Knowledge / Recommend。

但是：

> **领取 Task 必须 ACK。**

应该是 Protocol。

因为如果有人 ACK、有人不 ACK：

> Task Bus 无法知道任务到底有没有人承担。

再比如：

> **Boundary Extension 必须通过 Gateway。**

应该是 Protocol。

因为否则整个 Authority体系无法成立。

---

所以如果回到你最初的问题：

> **Protocol 诞生之初的目的是什么？**

我会把答案压成一句：

> **Protocol 不是为了控制工作，而是为了让彼此自由的主体能够可靠地一起工作。**

这句话我认为非常重要。

甚至它可以成为我们判断“某条 Knowledge 是否应该升级成 Protocol”的最上层标准：

> **如果不把它变成共同规则，组织的可靠协同、责任、边界或安全是否会受到实质损害？**

如果不会：

> **尽量不要 Protocol 化。**

让它留在 Knowledge / Recommend / Default。

这样我们的 Protocol Governance 天然就会保持轻，而不会随着组织学习越来越多，最后把整个 Free Work Space 塞满规则。

---

## turn-be6d53bc-1721-4d57-8901-e0c6ece9d3fb

时间：2026-09-06T15:19:58.051887+08:00

### Human

Message ID：`be6d53bc-1721-4d57-8901-e0c6ece9d3fb`

我同意。在我之前的理解中，Protocol 更像是一种设计给整个组织的独立的语言以及发言结构。那么，除非语言中产生了新的词汇，或者发言结构。需要每一个人都进行变化，在结构中加入一个新的元素，那么 Protocol 基本上就不会变化，我这个理解对吗

---

### Assistant

Message ID：`6cd3b5f1-58b1-4ff8-b4b9-4fdbf028010a`

对，**基本正确**。而且我觉得你的这个理解比我们刚才准备设计“Protocol Lifecycle（协议生命周期）”更准确——我们可能差一点把 Protocol 想得太像传统公司的制度文件了。

你把 Protocol 理解为：

> **组织内部的一套共同语言 + 发言结构 + 交互语法。**

我认为非常合适。

例如我们已经创造了很多“组织词汇”：

> `Goal`  
> `Task`  
> `Claim`  
> `ACK`  
> `Blocked`  
> `Escalate`  
> `Submit`  
> `Boundary Extension`  
> `Knowledge`  
> `Contribution`

这些词不是普通自然语言里的随意表达。

当 HAU说：

> `ACK TASK-037`

整个组织都知道它意味着什么：

> **我已经收到并承担这个 Task，后续状态不会静默。**

这就是组织语言。

而 Protocol 还规定“句子怎么说”。

例如 Task Return：

> Result  
> Observed Terrain  
> Execution Facts  
> Reflection

这就是你说的：

> **发言结构。**

不同 Agent底层可以完全不同，但只要都能按照这个结构和 Organization Bus沟通，它们就能互操作。

---

### 所以 Protocol 确实应该非常稳定

如果今天：

> `ACK` 表示“收到”。

明天改成：

> “收到并且保证一定完成”。

那整个组织语义都变了。

如果今天 Task Return 有：

> `Observed Terrain`

明天我们发现组织必须知道：

> `Human Oversight Event`

于是所有 HAU 的 Representative Agent 都需要学会一种新的“句式”。

这才是真正的：

> **Protocol Change。**

所以你说得很准确：

> **只有组织共同语言的词汇、语义、消息结构、状态机或交互规则发生变化时，才需要改变 Protocol。**

---

## 这也意味着我们应该修正前面一个东西

我们之前讨论：

> Knowledge → Inform → Recommend → Default → Mandatory

其中我曾经把：

> Mandatory

很容易地和 Protocol联系起来。

现在看应该更谨慎。

**Mandatory Rule（强制规则）不一定等于 Protocol Change。**

比如组织规定：

> “客户敏感数据不得进入未经批准的外部模型。”

这是 Mandatory Policy（强制政策）。

它可以通过现有 Protocol表达：

> `Data Boundary = Restricted`

如果现有 Runtime Envelope 已经认识 `Data Boundary` 这个字段：

> **根本不需要修改 Protocol。**

只是：

> Policy / Boundary内容变了。

真正需要 Protocol升级的是：

> 以前 Runtime Envelope 根本没有“Data Classification（数据分类）”这个概念。

现在组织发现：

> 所有 Agent都必须能够表达和理解数据分类。

于是增加：

> `data_classification`

字段。

这才是：

> **Protocol Change。**

这个区别非常重要。

---

# 所以我们应该分成三层

### Protocol

> **我们用什么语言沟通？**

相对稳定。

例如：

> Task是什么；  
> ACK是什么；  
> Boundary怎么表达；  
> Risk Request长什么样；  
> Task Return长什么样。

---

### Policy（政策 / 规则）

> **在当前语言里，组织要求什么？**

可以变化得更频繁。

例如：

> 哪些数据 Restricted；  
> 哪些 Action需要 Human；  
> 哪类 Risk不可接受。

不需要每次都改 Protocol。

---

### Knowledge

> **组织目前认为世界是怎样的？**

变化最频繁。

每天都可能产生。

例如：

> “这种数据条件下方法A容易失败。”

通过 Knowledge Pulse传播。

通常完全不影响 Protocol。

---

于是变化频率可能是：

```text id="m7vhe3"
Knowledge
高频变化
    ↓

Policy / Boundary
中频变化
    ↓

Protocol
低频变化
    ↓

Foundational Principles
极低频变化
```

这个结构我觉得非常漂亮。

---

## 甚至可以再类比成自然语言

**Foundational Principles**

> 像这门语言为什么存在、共同体最基本的规则。

**Protocol**

> 像语法 + 基础词汇。

**Policy**

> 像今天我们决定“会议上必须用这种格式汇报”。

**Knowledge**

> 像大家每天说的新内容。

所以：

> **组织每天都在产生新的“句子”，不意味着每天都要修改语言。**

只有发现：

> **现有语言已经无法表达一个组织必须共同理解的新概念**

才需要给语言增加一个新词。

或者：

> **现有句式已经无法支持一种新的可靠协作方式**

才改变消息结构。

---

### 这会让 Protocol Governance 变得极轻

我们刚才本来准备设计：

> Proposal → Verification → Approval → OTA → Monitor → Rollback……

现在我认为没必要做得那么重。

因为 Protocol应该是一个**低频基础设施变更**。

真正需要 Protocol Change 的典型 Trigger（触发条件）可能只有：

> **Expression Gap（表达缺口）**  
> 现有组织语言无法表达一个重要的新概念。
>
> **Coordination Gap（协同缺口）**  
> 现有消息/状态结构无法让多个 Actor可靠协同。
>
> **Governance Gap（治理缺口）**  
> 现有 Protocol无法表达必要的 Authority / Boundary / Accountability。
>
> **Technical Evolution（技术演进）**  
> 新 Agent / Runtime需要新的标准接口。

出现这些才：

> Protocol Proposal → Human Governance → Version Update → OTA。

平时大量组织变化：

> **根本不碰 Protocol。**

---

所以我认为你的理解不只是“对”，而是帮助我们把最后这个模块进一步简化了：

> **Protocol 应该像组织的语言一样稳定。组织每天学习新的知识、产生新的规则、完成新的任务，都不应该导致语言本身不断变化。只有当组织发现现有语言已经无法准确表达一种所有成员都必须共同理解的新概念或交互结构时，才值得升级 Protocol。**

这也意味着 **Protocol Governance 不应该成为一个经常运行的 Governance 流程，而更像是组织基础设施偶尔发生的“语言升级”。**

---

## turn-bde3eedf-ea5f-4d38-ae43-84d312717818

时间：2026-09-06T15:21:25.574504+08:00

### Human

Message ID：`bde3eedf-ea5f-4d38-ae43-84d312717818`

我同意，这个跟我理解的更相似

---

### Assistant

Message ID：`c616853f-1b9e-4b7e-8984-4c2f6914a768`

好，那这一点我们就按这个方向固定下来。

我们现在对 **Protocol** 的认识可以正式修正为：

> **Protocol 是组织的共同语言、语法和交互结构，而不是组织不断变化的管理制度。**

因此四层应该严格区分：

> **Knowledge** —— 组织现在知道什么。变化频繁。  
> **Policy / Boundary（政策 / 边界）** —— 组织当前允许、禁止、要求什么。可以动态变化。  
> **Protocol** —— Human、Agent、系统之间用什么共同语言和结构交互。应该高度稳定。  
> **Foundational Principles（基础原则）** —— 整个组织最根本的权力与责任原则。极少变化。

所以绝大多数组织成长：

> **不会导致 Protocol Change（协议变更）。**

只有出现 **Expression Gap（表达缺口）、Coordination Gap（协同缺口）、Governance Gap（治理表达缺口）或必要的技术接口变化**，现有“语言”已经无法表达组织必须共同理解的新东西时，才升级 Protocol。

这也意味着 Protocol OTA（协议远程更新）仍然重要，但应该是一个**低频、慎重的基础设施能力**，而不是天天发生的制度推送。

到这里我认为 Protocol Governance 基本已经想透了。我们可以继续把 **Governance / Audit / Risk v0.1** 最后一轮收敛，然后整个 Operating Model v0.1 就可以做总收敛。

---

## turn-0f053bc2-ef18-45b2-a2c5-b14b1e5c63d0

时间：2026-09-06T15:21:48.325652+08:00

### Human

Message ID：`0f053bc2-ef18-45b2-a2c5-b14b1e5c63d0`

收敛

---

### Assistant

Message ID：`b66762ca-5ca9-4840-acb9-74dabd0cc114`

好。正式收敛最后一个一级模块：

# Governance / Audit / Risk v0.1
**治理 / 审计 / 风险**

这个模块不负责管理 Human 和 Agent 的日常工作。

它解决的是：

> **在一个高度自主、Human 与 Agent 共同运行的组织中，谁有权决定什么；这种权力从哪里来；风险由谁接受；关键决定如何留下可追溯记录；以及组织自身的规则由谁改变。**

---

# 一、Governance 的定义

正式采用：

> **Governance is the architecture of decision rights.**
>
> **治理，就是“谁有权决定什么”的架构。**

Governance 主要定义四件事：

**Authority（决策权）**

> 谁可以决定？

**Boundary**

> 可以决定到哪里？

**Accountability（最终责任）**

> 结果最终由谁负责？

**Rule Change**

> 谁可以改变组织运行规则？

Governance ≠ Management（管理）。

> **Management 解决怎么把事情做好。**
>
> **Governance 解决谁有权决定什么。**

---

# 二、Governance 默认不介入正常工作

核心原则：

> **Governance is exception-driven（治理由例外触发）。**

正常情况下：

> Goal / Boundary 已确定  
> ↓  
> Human / Agent 在 Boundary 内自主  
> ↓  
> Task → Result → Review → Acceptance

不进入 Governance。

只有需要：

> 改变 Authority；  
> 突破 Boundary；  
> 接受超出授权范围的 Risk；  
> 改变 Policy / Protocol；  
> 执行重大不可逆 Action；

才进入 Governance。

---

# 三、Authority follows the object

不建立一个所有事情都往上报的中央审批委员会。

采用：

> **Authority follows the object（决策权跟着治理对象走）。**

例如：

> Goal → Goal Authority  
> Task → Task Accountable Owner  
> Data → Data Authority  
> Risk → Risk Authority  
> Agent Permission → Agent Governance Authority  
> Protocol → Protocol Authority

Governance Event（治理事件）根据：

> **究竟要改变什么**

自动路由到对应 Human Authority。

---

# 四、Authority is scoped

正式原则：

> **Authority is scoped, not hierarchical by default.**
>
> **决策权首先按职责范围划分，而不是默认按上下级划分。**

例如：

Task Owner可以判断：

> Dataset C 是否是完成 Task 所必需。

但不能因此决定：

> Dataset C 的安全规则可以突破。

Data Authority 可以决定：

> 数据能否开放。

但不能决定：

> 这个 Goal 有没有业务价值。

多个 Authority 不是简单：

> 2票对1票。

而是：

> **各自在自己的 Authority Scope（决策权范围）内生效。**

---

# 五、每一个治理决策最终落到 Human

正式扩展我们前面的责任原则：

> **Every governed decision must resolve to a Human Decision Authority.**
>
> 每一个真正的 Governance Decision，最终必须解析到一个 Human 决策责任主体。

AI可以：

> Observe / Analyze / Recommend / Proposal / Execute

但改变组织 Authority / Boundary /重大 Risk的最终决定：

> 必须有 Human Authority 来源。

---

# 六、Risk 的正式定义

Risk 不等于 Unknown，也不等于 Loss。

正式采用：

> **Risk 是：在存在不确定性的情况下，一个 Actor 因某项 Decision 或 Action 暴露于可能产生负面后果的未来状态。**

区分：

**Uncertainty（不确定性）**

> 我们不知道会发生什么。

**Hazard（危险源）**

> 什么东西可能造成伤害。

**Exposure（暴露）**

> 我们实际上有没有把自己放在这个危险源影响范围内。

**Consequence（后果）**

> 事情真的发生以后造成什么影响。

**Risk**

> 上述因素在具体行动中形成的实际风险。

---

# 七、Unknown ≠ Dangerous

这一点对我们的实验组织尤其重要：

> **Unknown does not mean dangerous.**
>
> **未知不等于危险。**

战争迷雾很浓：

> Uncertainty 很高。

但如果失败只是：

> 两小时 Human Time + 一些 Token，

Risk可能仍然很低。

所以：

> **Capability Unknown / Terrain Unknown**

不能成为禁止新人探索的理由。

---

# 八、Risk Shaping

Risk Governance 的目标不是：

> 一看到 Risk 就禁止。

而应该优先：

> **Risk Shaping（风险塑形）**

通过：

> 降低 Exposure；  
> 限制 Permission；  
> Sandbox（沙箱）；  
> Read-only；  
> Small Sample；  
> Review；  
> Backup；  
> Rollback（回滚）

把一个原本无法承受的行动：

> 变成低失败成本的 Experiment。

因此：

> **治理的目的不是阻止探险，而是尽量让探险失败得起。**

---

# 九、Residual Risk

正式定义：

> **Residual Risk（剩余风险）= 在所有已经采用且有效的风险控制措施之后，组织仍然暴露于潜在负面后果的风险。**

Governance 真正需要问的是：

> **该做的保护都做完以后，剩下这个 Risk，谁有权接受？**

而不是：

> “这件事情有没有风险？”

---

# 十、Risk Authority follows actual consequence bearing

这是 Risk Governance 最核心原则之一：

> **Risk Authority follows actual consequence bearing.**
>
> **风险接受权跟随实际后果承担者。**

不是：

> 谁愿意承担。

而是：

> **风险真的兑现以后，损失事实上落到谁身上。**

例如数据泄露：

员工说：

> “我愿意辞职。”

并没有承担全部 Consequence。

真正承担的可能包括：

> Customer  
> Organization  
> Shareholder  
> Partner

所以：

> **任何 Actor 都不能替自己无权代表的后果承担者接受风险。**

---

# 十一、Task Accountability ≠ Risk Authority

Task Owner对 Task负责。

但：

> **承担 Task责任不等于拥有无限 Risk Acceptance Authority。**

例如 TASK-037由 H-012负责。

如果需要：

> 使用敏感客户数据，

H-012不能因为：

> “Task归我负责”

就自己批准。

Risk Authority 必须跟着实际 Consequence Bearer 找到对应授权 Human。

---

# 十二、Risk Expression v0.1

Risk 不主要表达成：

> `Risk Score = 73`

而形成轻量 **Risk Object（风险对象）**：

> **Action** —— 准备做什么？  
> **Why Now** —— 为什么现在需要？  
> **Potential Consequence** —— 可能造成什么负面后果？  
> **Consequence Bearer** —— 后果真正落到谁身上？  
> **Exposure** —— 暴露范围多大？  
> **Existing Controls** —— 已经做了什么保护？  
> **Residual Risk** —— 还剩什么风险？  
> **Requested Authority** —— 希望获得什么授权？

不制造假精确。

---

# 十三、Risk Routing

Risk Object进入系统后：

> Potential Consequence  
> ↓  
> Actual Consequence Bearer  
> ↓  
> Authorized Representative  
> ↓  
> Risk Authority

系统维护轻量：

> **Authority Registry（决策权登记表）**

记录：

> 哪类 Consequence Domain（后果领域）由哪个 Role 有权代表其承担者作出 Decision。

Role再解析：

> `Role → Current Human Holder`

不把 Protocol绑死在具体人身上。

---

# 十四、预授权优先

Risk Authority 不意味着：

> 每一个 Risk 都找 Human审批。

Human可以提前定义：

> **Autonomy Envelope（自主权边界）**

如果 Residual Risk 已经在授权范围：

> Agent / HAU继续自主。

只有超过 Boundary：

> 才真正 Route Human。

因此：

> **Human治理边界，而不是审批每一次动作。**

---

# 十五、Hard Boundary

正式定义：

> **Hard Boundary（硬边界）不是“Risk特别高”，而是普通 Authority 没有资格接受这种潜在后果。**

可能来源：

> 法律 / 合规；  
> 第三方权利；  
> 组织基础原则；  
> 当前无法合理控制的重大不可逆后果。

普通 Risk Acceptance：

> **不能突破 Hard Boundary。**

如果认为 Hard Boundary 本身应该改变：

> 不能“特批”。

必须进入：

> **Policy / Protocol / Foundational Rule Change**

对应的更高 Governance。

---

# 十六、Audit 的定义

Audit 不等于 Governance。

> **Governance：谁有权决定？**
>
> **Audit：后来能不能还原当时发生了什么、谁有权这么做、为什么这么决定？**

Audit v0.1 最核心回答：

> **What happened?**  
> **Who had authority?**  
> **Why was the decision made?**  
> **What changed?**

---

# 十七、Event Store = Audit 基础设施

第一版不建设第二套独立审计日志。

我们已经存在的：

> **Event Store**

就是 Audit 的事实底座。

所有重要 Organizational State Change 自动留下 Event：

> Goal Activated  
> Task Created  
> Boundary Extended  
> Permission Granted  
> Result Accepted  
> Knowledge Changed  
> Agent Suspended  
> Protocol Updated……

---

# 十八、Audit 保存当时的 Authority

非常重要：

> **Audit must preserve authority-at-the-time.**
>
> **审计必须能够还原事件发生当时的权力状态。**

不能只保存：

> `approved_by = H-012`

还要能够知道：

> 当时 H-012 的 Role是什么；  
> Authority Scope是什么；  
> Protocol Version是什么；  
> Boundary是什么。

因为未来这些都会变化。

---

# 十九、Audit 不记录私人思维

核心：

> **Audit records decision evidence, not private thought.**
>
> **审计记录决策依据，不记录私人思维过程。**

保存：

> Actor  
> Authority  
> Reason  
> Evidence  
> Before State  
> After State  
> Timestamp  
> Protocol Version

但不要求：

> Human / Agent交出完整 Chain of Thought（思维过程）。

Free Work Space 仍然保持自由。

---

# 二十、Audit 首要目的不是惩罚

重大 Failure 后，Audit首先帮助组织重建：

> 当时 Task是什么；  
> Boundary是什么；  
> Agent知道什么；  
> Human为什么批准；  
> Protocol是否存在缺口；  
> Escalation为什么没有发生。

目标：

> **Failure → System Learning**

当然 Human明确违反 Boundary仍然承担 Accountability。

但 Audit 的主要系统价值是：

> **重建事实和学习，而不是 Surveillance（全面监控）。**

---

# 二十一、Protocol 的正式定义

经过最后讨论，我们对 Protocol 的理解进行了重要修正：

> **Organizational Protocol = 一组最小的共享语言、语义、状态和交互结构，使彼此独立的 Human、Agent 与系统能够在保留内部自主性的同时可靠协同。**

最简单理解：

> **Protocol 是组织的共同语言 + 语法 + 发言结构。**

它不是 SOP。

它不规定：

> 事情具体怎么做。

它规定：

> **不同 Actor 怎样彼此理解和交互。**

---

# 二十二、Protocol fixed, Workflow free

正式原则：

> **Protocol fixed, Workflow free.**
>
> **协议统一，工作方式自由。**

例如：

> ACK是什么意思；  
> Task Return怎么表达；  
> Boundary Request怎么表达；  
> Risk Object怎么表达；

这些属于 Protocol。

但：

> 用几个 Agent；  
> 先研究还是先实验；  
> 怎么完成 Result；

属于 Free Work Space。

---

# 二十三、Knowledge / Policy / Protocol / Foundation 分层

最终形成：

```text
Knowledge
组织知道什么
高频变化
      ↓
Policy / Boundary
组织当前允许、禁止、要求什么
中频变化
      ↓
Protocol
组织用什么共同语言和结构协同
低频变化
      ↓
Foundational Principles
组织最根本的权力、责任与边界
极低频变化
```

因此：

> **组织每天产生新 Knowledge，不意味着每天改变 Protocol。**

---

# 二十四、什么时候才需要 Protocol Change？

只有现有组织语言已经不足以支持可靠协同时。

主要 Trigger（触发条件）：

**Expression Gap（表达缺口）**

> 缺少所有 Actor必须共同理解的新概念。

**Coordination Gap（协同缺口）**

> 当前消息/状态结构无法支持可靠协作。

**Governance Gap（治理表达缺口）**

> 无法表达必要 Authority / Boundary / Accountability。

**Technical Evolution（技术演进）**

> 新 Runtime / Agent体系需要新的标准接口。

除此之外：

> 尽量不要改 Protocol。

---

# 二十五、Protocol Governance 的位置

最终治理层次：

```text
Foundational / Constitutional Governance
组织最根本原则
            ↓
Protocol Governance
共同语言和交互结构
            ↓
Operational Governance
日常 Authority / Boundary / Risk Decision
            ↓
Autonomous Operation
Human / Agent Boundary 内自主运行
```

Protocol Governance：

> **是规则/语言层面的最高治理权，但不是组织最终最高权力。**

---

# 二十六、Foundational Principles

v0.1 不需要复杂“组织宪法”。

只需要非常薄的一组：

> **Foundational Principles（基础原则）**

目前已经自然形成的候选包括：

> Human保留最终 Goal Authority。  
> 每个 Task / Execution 必须唯一解析到 Human最终责任人。  
> Boundary以内默认自主。  
> Authority必须有可追溯来源。  
> Actor不能替自己无权代表的后果承担者接受 Risk。  
> Free Work Space不接受全面监控。  
> 组织治理 Organizational State，不治理私人思考过程。

普通 Protocol不能自行推翻这些原则。

---

# 最终压缩

整个 **Governance / Audit / Risk v0.1** 可以压缩成七句话：

> **治理不是管理工作，而是设计“谁有权决定什么”。**
>
> **正常工作默认自主，Governance只处理 Boundary、Authority、重大 Risk 和规则变化。**
>
> **一般 Authority 跟着治理对象走；Risk Authority 跟着实际后果承担者走。**
>
> **未知不等于危险；尽可能通过降低 Exposure 和提高 Recoverability，让未知变得可以安全探索。**
>
> **Human治理剩余风险和边界，而不是审批 Agent 的每一步。**
>
> **Audit记录重要状态变化、当时的 Authority 和决策依据，但不监控私人思考。**
>
> **Protocol是组织共同语言，不是不断增长的规章制度；语言应该稳定，工作方式应该自由。**

---

## 到这里意味着什么

到这里，我们最初规划的 **Operating Model v0.1 核心设计已经全部完成**。

现在已经拥有：

> Goal System  
> Task System / Task Bus  
> Free Work Space  
> Review / Acceptance  
> Organizational Learning & Memory  
> Knowledge Formation / Knowledge Pulse  
> Agent Governance & Runtime  
> Capability System  
> Contribution / Reward / Honor  
> Progression & Achievement（已立项）  
> Governance / Audit / Risk

而且这些已经不是互相独立的模块，它们之间已经形成了大量闭环。

下一步我建议**先不要马上开始新的设计模块**。

下一步应该做一次真正的：

> **Operating Model v0.1 Global Convergence（全局收敛）**

把所有已经冻结的模块放到同一张架构里，检查：

> 有没有定义冲突；  
> 有没有重复概念；  
> 有没有责任断点；  
> 有没有某个 Event 走不通完整闭环；  
> 有没有我们讨论到后面已经推翻、但前面仍然保留的旧设计。

做完这次全局收敛，我们再一次性同步 **Obsidian + GitHub**，然后开发轨道就可以拿到一个真正稳定的 **Operating Model v0.1 Baseline（运行模型 v0.1 基线）**。

---

## turn-b987f954-6532-46bf-b866-c4d02566b412

时间：2026-09-06T15:23:30.277055+08:00

### Human

Message ID：`b987f954-6532-46bf-b866-c4d02566b412`

这个全局收敛是在这个对话中做，还是放到 Work 里，放在本地做呢

---

### Assistant

Message ID：`988a9ecc-c8bd-4cb3-94ed-90a2461d3c86`

我建议**分成两步，而且顺序很重要**：

> **先在这个对话里做“设计层全局收敛”，再到 Work / 本地做“文档层全局收敛”。**

原因是两种收敛解决的问题不同。

### 现在这个对话：设计层收敛

这里拥有最完整的“为什么”。

很多设计不是简单的最终结论，而是我们经过多轮讨论以后推翻旧版本形成的。例如：

> Capability 从“等级”变成了动态地图；  
> Task Routing 从“匹配分配”变成了赏金酒馆式 Discovery；  
> Protocol 从“组织规则”进一步收窄成了“共同语言与交互结构”；  
> Risk 从“高低等级”回到了 Uncertainty + Exposure + Consequence；  
> Organizational Capability 又因为 Oversight Externalization（监督外化）发生了重要修正。

这些变化，我在当前上下文里最容易做**语义冲突检查**。

所以这里应该先做：

> **Operating Model v0.1 Global Design Review（全局设计审查）**

把所有模块放到一起检查：

**定义冲突 → 权力冲突 → 责任断点 → 数据流断点 → Event闭环 → 模块重复 → 前后版本覆盖关系。**

发现问题，我们就在这里讨论并裁决。

最后得到：

> **Operating Model v0.1 Final Design Baseline（最终设计基线）**

---

### 然后再进入 Work：文档层收敛

等你回到电脑旁边，我们再让 Work真正读取：

> Obsidian现有项目 + GitHub当前版本 + README + 状态文件 + next-actions + 原始讨论

然后做第二轮：

> **“现在本地写着什么” vs “刚刚冻结的 Final Design Baseline”**

逐文件检查。

这一步主要解决：

> 哪些旧笔记已经过时；  
> 哪些地方仍写着“待设计”；  
> 哪些术语还是旧定义；  
> 哪些模块缺少新结论；  
> WikiLink 是否正确；  
> README / Architecture / Status / Version 是否一致；  
> 开发轨道应该读取哪个入口。

然后一次性更新 Obsidian、检查 Git diff，再同步 GitHub。

这样就不会让 Work自己从几百轮聊天里重新“猜”哪些设计是最新的。

---

所以流程我建议明确成：

**现在：**

> 当前对话 → **Global Design Convergence**

↓

发现冲突 → 我和你裁决

↓

形成 **Operating Model v0.1 Final Baseline**

**你回电脑以后：**

> Work → 读取本地 Obsidian / GitHub

↓

拿 Final Baseline 对照本地文件

↓

**Global Documentation Convergence**

↓

Obsidian + GitHub 同步

↓

开发轨道正式以 v0.1 为基线。

我认为这是最稳的。

而且**现在正适合开始第一步**。我们不需要再逐模块复述一遍，而应该真正做一次“系统级压力测试”：先画出整个 Operating Model 的主循环和 Authority / Accountability 两条主线，再逐个寻找有没有断点。

---

## turn-f4d5e233-319d-4688-babb-c497ac2a7c71

时间：2026-09-06T15:24:21.410425+08:00

### Human

Message ID：`f4d5e233-319d-4688-babb-c497ac2a7c71`

我同意，但是我想每一个模块，你都在收敛的过程中帮我提炼出，像刚才 Risk、Audit 那个模块中，你说的压缩成七句话，这样一个。原则文档，让除你我之外的人看到这个东西的时候，能够先从最底层的运行原则切入去理解这一模块的意义

---

### Assistant

Message ID：`f38a1a95-44b4-42ee-bda0-2cd99e705b35`

同意，而且我认为这应该成为这次 **Global Design Convergence（全局设计收敛）** 的正式交付物之一。

我们不要只得到一套很长的 Specification（规格说明）。应该让**每个一级模块都有一张“原则页”**，一个第一次接触项目的人先读这一页，就能理解：

> **这个模块为什么存在、相信什么、不相信什么，以及它如何运行。**

然后才进入 Definition、Protocol、Data Model 和实现细节。

### 我建议每个模块固定成三层

**第一层：Principles｜原则**

控制在大约 **5–10句话**。

不是功能列表，而是这个模块最底层、已经经过我们讨论后留下来的判断。

比如刚才 Risk / Audit / Governance 的七句话就是非常好的例子：

> 治理不是管理工作，而是设计谁有权决定什么。  
> 正常工作默认自主，治理只处理 Boundary、Authority、重大 Risk 和规则变化。  
> 一般 Authority 跟着治理对象走；Risk Authority 跟着实际后果承担者走。  
> 未知不等于危险；尽可能通过降低 Exposure 和提高 Recoverability，让未知可以被安全探索。  
> Human 治理剩余风险和边界，而不是审批 Agent 每一步。  
> Audit 记录重要状态变化、当时 Authority 和决策依据，但不监控私人思考。  
> Protocol 是组织共同语言，不是不断增长的规章制度；语言应该稳定，工作方式应该自由。

读完这七句，一个新人即使完全不知道我们的 Schema，也已经大概知道我们设计的是什么组织。

---

**第二层：Mental Model｜心智模型**

回答：

> **“应该怎样想象这个模块？”**

例如 Capability：

> **它不是员工技能等级表，而是一张战争迷雾中的动态地图。**

Task：

> **它不是领导派工系统，而更像赏金酒馆里的任务墙。**

Knowledge：

> **它不是文档库，而是组织从 Experience 中通过 Evidence、证伪和 Scope 逐渐形成的可复用认知。**

Agent Governance：

> **不是监控所有 AI，而是治理代表 Human 进入组织的 Agent 接口，以及所有拥有组织 Authority 的 Agent 节点。**

这一层可能只需要一小段。

它对第一次理解系统的人非常重要。

---

**第三层才是 System Design｜系统设计**

再进入：

> Definitions  
> Objects  
> States  
> Events  
> Protocol  
> Boundary  
> Authority  
> Data Flow  
> Interfaces  
> Open Questions

这样以后开发者也不会出现一种很常见的问题：

> 看懂了字段，却没理解为什么这样设计。

---

## 而且原则页还有一个更重要的作用

它可以成为未来设计变化的**一致性测试**。

例如开发人员以后说：

> “为了方便，我们把所有 Private Agent 的完整聊天过程上传中央系统吧。”

我们不需要先讨论技术。

直接对照 Agent Governance 原则：

> **中央管理组织状态，不管理私人思考过程。**

冲突。

那么除非我们正式修改原则，否则这个实现就不应该进入。

又比如：

> “为了安全，Capability L1 禁止领取 L5 Task。”

对照 Capability 原则：

> **Capability is guidance, not permission.**

冲突。

再比如：

> “每形成一条 Knowledge，就生成一条 Mandatory Workflow。”

对照 Knowledge：

> **Inject cognition, not workflow.**

冲突。

所以这些 Principles 不只是给新人看的。

它实际上是：

> **Architecture Decision Filter（架构决策过滤器）。**

---

## 我建议全局收敛最终形成两份顶层文档

第一份：

# Operating Model v0.1 — Principles

非常短。

按一级模块排列，每个模块：

> **Purpose（一句话） → Mental Model（一小段） → 5–10条 Principles**

可能最终只有十几页。

这是：

> **任何 Human / Agent进入这个项目首先应该读的东西。**

第二份：

# Operating Model v0.1 — Specification

才是完整设计：

> Objects / States / Protocols / Events / Authority / Data Flow / Relationships……

供：

> 开发 Agent、架构 Agent、后续设计线程

使用。

---

而且我们现在已经有很多非常好的原则句了，不需要重新发明。例如：

**Organizational Learning & Memory**

> Store broadly, activate sparsely.  
> Inject cognition, not workflow.  
> Learn before prescribe.  
> 孤证不立。  
> Verification 优先寻找证伪。  
> Knowledge Quality ≠ Scope Size。

**Agent Governance**

> One Human, One Organizational Agent Interface.  
> Default Autonomous + Explicit Boundaries.  
> Authority narrows by delegation; expands only by authorization.  
> Reliable = No Silent Failure.  
> No unmanaged organizational authority.  
> Human 可以退出执行环，但不能退出责任环。

**Capability**

> Capability is guidance, not permission.  
> Seed the map, discover the world.  
> Task 不只是工作单位，也是探索世界的探针。  
> Capture is not documentation; capture is reproducibility.  
> Knowledge clarity is not readability; it is teachability.

**Contribution / Reward / Honor**

> Contribution records value.  
> Reward distributes value.  
> Honor preserves values.  
> Contribution first, valuation later.  
> Task Failure ≠ No Contribution.  
> Honor 纪念 Event，而不是排名 Human。

这些其实已经开始形成这套组织自己的**设计哲学语言**。

所以我建议这次 Global Convergence 不只是：

> **“检查我们有没有漏设计东西。”**

而是同时完成三件事：

> **① System Convergence** —— 所有模块放在一起检查闭环与冲突。  
> **② Principle Extraction** —— 每个模块提炼 5–10 条不可轻易违反的底层原则。  
> **③ Vocabulary Convergence** —— 把 Goal、Task、Knowledge、Capability、Contribution、Protocol、Authority、Risk 等核心词汇统一成唯一正式定义。

完成以后，我们得到的就不只是“很多设计笔记”，而是一套真正可以交给第三个人阅读和继续建设的 **Operating Model v0.1**。

下一步我建议就按这个方式正式开始全局收敛，并且**从 Goal System 开始，一个模块一个模块走，但不重新设计——只做原则提炼、定义统一和跨模块冲突检查。**

---

## turn-51cdd722-93b9-4951-9085-f5ddacd7507f

时间：2026-09-06T15:25:52.069917+08:00

### Human

Message ID：`51cdd722-93b9-4951-9085-f5ddacd7507f`

是不是每一个模块以及整体，还应当有一张全景图，便于人类去阅读和理解，类似于流程图或组织架构图那样的东西

---

### Assistant

Message ID：`323bfb46-c083-4930-8ed9-208e8652169a`

是的，而且我认为这应该成为正式交付标准。

甚至可以规定：

> **每个一级模块必须有一张图；整个 Operating Model 必须有一张总图。**
>
> **Principles 负责告诉人“为什么这样设计”，Panorama（全景图）负责让人“一眼看见它怎么运转”。**

但每张图不必都画成流程图。不同模块应该选择最适合自己的视觉语法：Goal/Task 适合流转图，Knowledge 适合形成与验证循环，Capability 适合地图隐喻，Agent Governance 适合 HAU—Runtime—Gateway 的关系架构，Governance/Risk 则适合 Authority（决策权）与 Risk Routing（风险路由）图。

我建议最终每个模块形成一个固定的阅读入口：

> **Purpose → Principles → Panorama → Mental Model → Specification**

这样一个完全没参与我们讨论的人，可以先花 30 秒看全景图，再花 2 分钟读原则，然后才决定是否深入 Specification（规格说明）。

而整个系统还应该额外有一张 **Operating Model v0.1 全景总图**。这张图不能只是把所有模块画成十几个方框，而应该展示真正的主循环，例如：

> **Vision → Goal → Task Bus → HAU / Organizational Agent → Free Work Space → Result → Review / Acceptance → Learning → Knowledge / Capability → 下一轮 Task**

同时把另外几条重要循环叠加进去：

> **Terrain Discovery → Dynamic Task Generation → Task Bus**  
> **Human Oversight → Organizational Learning → Organizational Capability → 反向教 Human**  
> **Contribution → Collective Valuation → Reward**  
> **Exceptional Event → Governance / Risk → Authority → Boundary Update**

而 **Protocol + Runtime + Event Store + Audit** 应该表现为贯穿整个系统的基础设施层，不应该假装它们只是主循环里的某一步。

这张总图最终应该让一个新人第一次看到时产生一个非常明确的理解：

> **“原来这个组织是这样活起来的。”**

所以我建议把这次 Global Convergence 的交付结构正式增加为三个东西：**每模块原则页、每模块全景图、全系统总全景图**。这三样再加完整 Specification，基本就构成了一个非常适合 Human 和 Agent 共同阅读的 v0.1 设计基线。

等我们真正开始全局收敛时，我会按这个标准逐模块处理，而不是只整理文字。

---

## turn-491e3832-3039-432c-ac88-2eceaab8e8c7

时间：2026-09-06T15:26:45.728584+08:00

### Human

Message ID：`491e3832-3039-432c-ac88-2eceaab8e8c7`

这张全景图是不是很难做成二维的？或者如果做成二维的会非常大。那我们有没有什么办法比它做成三维的？比如做成 HTML，每个模块点进去是那个子模块的全景图。但是我想，这个是不是应该放在文档收敛那一步来做？

---

### Assistant

Message ID：`a87761f5-36b3-4ff1-9052-3368396e6d93`

对，我建议**现在不要做最终 HTML**，把它放到后面的 **Documentation Convergence（文档收敛）** 阶段。但现在的设计收敛必须把“这张图应该表达什么”定义清楚。

而且我认为你说的“三维”不一定真的要做成 WebGL 那种可以旋转的 3D 世界。那可能炫，但反而难读。更适合我们的其实是：

> **Hierarchical Interactive Map（分层交互式地图）**

也就是用二维屏幕表达一个“有深度的三维知识空间”。

### 第一层：整个 Organization

第一次打开 HTML，只看到最核心的十来个模块和它们之间最重要的关系。

例如中心可能是：

> **Goal → Task → HAU → Result → Learning → Organizational Capability**

外围连接：

> Knowledge  
> Agent Runtime  
> Contribution  
> Governance  
> Risk  
> Protocol……

这时候绝不展示所有细节。

用户看到的是“整个城市”。

### 第二层：点击一个模块，进入这个模块

比如点击 **Capability**。

总地图淡出/缩小，进入 Capability World：

> Task → Expected Terrain → Exploration → Task Return → Capability Evidence / Terrain Evidence → HAU Map / Organization Map → Capability Capture → Reproduction → Organizational Capability

这就是我们刚才说的：

> **模块全景图。**

再点击 `Oversight Learning`，还可以进入第三层。

所以空间深度实际上来自：

> **Zoom / Drill-down（缩放 / 下钻）**

而不是一定需要真正的 Z 轴。

---

### 还可以有第二种“深度”：切换观察视角

同一套 Operating Model 可以有不同 Layer（图层）。

例如顶部有几个 View：

**Operating View**

> Goal → Task → Result → Learning 的主循环。

**Human / HAU View**

> 一个新人带着 Representative Agent 一天是怎么工作的。

**Knowledge View**

> Experience 如何变成 Evidence → Knowledge → Pulse → Capability。

**Authority View**

> Authority、Accountability、Boundary、Risk 是怎么流动的。

**Value View**

> Contribution → Reward → Honor。

底层还是同一个系统。

只是：

> **切换不同图层。**

这其实比真 3D 更接近你之前描述的那张“立体网”。

你说过：

> 拉起一个节点，会带动同一平面的很多节点，也会带动另一个平面的东西。

这个 HTML 完全可以做到：

> 点击 `TASK-037`

同时高亮：

> Parent Goal  
> HAU  
> Knowledge  
> Capability Evidence  
> Contribution  
> Risk  
> Audit Event

于是人会真正看到：

> **一个对象在不同组织空间中的连接。**

---

## “新手村”也可以成为另一种 View

甚至以后这个 HTML 可以有：

> **Architecture View（架构视图）**

给我们、开发者、Agent看。

以及：

> **World View（世界视图）**

给新人看。

同一个 Task Bus：

Architecture View：

> `Task Bus / Claim / Lease / Event`

World View：

> **赏金酒馆。**

Capability：

Architecture View：

> Capability Evidence Graph。

World View：

> **战争迷雾地图。**

Knowledge：

Architecture View：

> Knowledge Graph。

World View：

> **图书馆。**

它们不是两个系统。

而是：

> **同一套底层 Ontology（本体结构）的两种投影。**

这个我认为会非常漂亮。

---

## 所以我建议分阶段

**现在的 Global Design Convergence：**

我们只确定：

> 每个模块有哪些核心节点；  
> 哪些箭头必须存在；  
> 哪些跨模块连接必须表达；  
> 每个模块的 Mental Model；  
> 整体主循环是什么。

也就是说：

> **先定义地图的拓扑，不画最终地图。**

等你回电脑进入 Work：

**Documentation Convergence：**

读取全部 Obsidian / GitHub 后：

> 更新正式 Specification；  
> 生成每模块二维全景图；  
> 建立全局 Interactive HTML；  
> 建立 Drill-down；  
> 建立不同 Layer / View；  
> 把 HTML 与 Obsidian文档互相链接。

这样最终可以得到一个类似：

> **AI-native Organization Atlas（AI 原生组织图谱）**

的东西。

打开不是一本300页说明书，而是一张可以探索的组织世界。

---

所以我完全同意你的判断：

> **最终可交互 HTML 属于文档收敛阶段。**

但：

> **它的信息架构必须在现在的设计收敛阶段确定。**

否则到 Work 阶段再让开发 Agent“根据文档自己画”，很容易画成一张漂亮但错误的图。

所以接下来 Global Convergence 的每一个模块，我都会同时产出四件东西：

> **Principles → Mental Model → Panorama Topology（全景图拓扑）→ Cross-module Connections（跨模块连接）**

最后再形成整个 Operating Model 的 **Global Topology（全局拓扑）**。

等到 Documentation Convergence，再把这些拓扑真正变成你说的那个**可点击、可下钻、可切换视角的 HTML 立体组织地图**。

---

## turn-4ae954b1-3f17-4ce7-9767-aa50a07cd8d3

时间：2026-09-06T15:31:08.382861+08:00

### Human

Message ID：`4ae954b1-3f17-4ce7-9767-aa50a07cd8d3`

OK那我们现在先开始内容的收敛，先不管文档

---

### Assistant

Message ID：`e7ea5fdb-e3a2-4e97-8647-607da4b742d0`

好。现在正式开始 **Operating Model v0.1 — Global Design Convergence（全局设计收敛）**。

这一阶段我们**不写 Obsidian、不做 HTML、不考虑最终文档排版**。只处理设计本身。

我建议严格按照同一个方法逐模块走，每个模块只做四件事：

> **① Purpose**：它为什么存在？  
> **② Principles**：5–10条最底层原则。  
> **③ Core Model**：最小对象、关系与运行闭环。  
> **④ Cross-check**：与后续已经冻结模块有没有冲突、重复或缺口。

发现冲突就停下来讨论；没有冲突就标记：

> **Global Convergence Passed**

然后进入下一模块。

---

# 01 — Goal System

先从整个 Operating Model 的源头开始。

## Purpose

我认为 Goal System 最底层的存在意义可以压缩成：

> **Goal 不是用来告诉组织“做什么 Task”，而是告诉整个组织“我们希望现实世界发生什么变化”。**

它提供组织行动的方向锚点。

没有 Goal，Task Bus 会退化成：

> “有很多事情可以做。”

但无法回答：

> **“为什么值得做？”**

因此 Goal 是 Task、Contribution、Capability Gap、Dynamic Task Generation 乃至 Organizational Learning 最终判断价值的上游锚点。

---

# Goal System — Principles v0.1

我从我们之前全部讨论里，目前提炼出 **8条**。

### 1. Goal describes desired change, not prescribed work.

> **Goal 描述希望发生的结果变化，而不是规定工作方法。**

Goal 不应该写：

> “做一份市场调研报告。”

而更应该是：

> “让组织理解某市场是否值得进入，并把关键不确定性降低到可以做出投资判断的程度。”

前者更像 Task。

---

### 2. Human retains final Goal Authority.

> **最终 Goal Authority 保留在人。**

Agent可以：

> Discover / Suggest / Challenge / Decompose。

甚至可以发现：

> “现有 Goal 可能错了。”

但不能自己把组织带向一个新的 Goal。

这是目前我们的 Foundational Principle（基础原则）之一。

---

### 3. Goal defines Why and What; Free Work Space owns How.

> **Goal 定义为什么做、希望改变什么；具体怎么做留给执行空间。**

因此 Goal 不应该偷偷变成 Workflow。

---

### 4. Every Task must be traceable to a Goal.

> **每个正式组织 Task 最终都必须能够追溯到一个 Active Goal。**

包括：

> Initial Task  
> Derived Task  
> Capability Exploration Task  
> Reproduction Task

都必须回答：

> **“这个 Task 为什么值得组织花注意力？”**

如果不能连接 Active Goal：

> 系统可以产生 Proposal，但不应该无限自动生成正式 Task。

这也是我们限制 Dynamic Task Generation 无限膨胀的关键。

---

### 5. Goal provides Success Criteria, not guaranteed solution.

> **Goal 必须让组织知道什么叫“变好了”，但不假装提前知道正确解法。**

Success Criteria 是验收方向。

不是：

> “我们已经知道应该怎么实现。”

---

### 6. Goal carries Boundary.

Goal不只有：

> Desired Outcome。

还必须有：

> **组织愿意为了这个 Goal 承担什么、不承担什么。**

例如：

> 时间  
> 资源  
> Risk  
> 数据  
> 外部影响

这些 Boundary 向下传递给 Task。

---

### 7. Goal can be challenged without being silently changed.

> **任何 HAU / Agent 都可以 Challenge Goal，但不能偷偷修改 Goal。**

如果 Task Exploration发现：

> Goal假设错误；  
> Success Criteria不合理；  
> 实际 Terrain与预期完全不同，

应该产生：

> **Goal Challenge / Goal Proposal**

回到 Human Goal Authority。

---

### 8. Goal is the value anchor of the organization.

> **Goal 是判断组织行为是否产生价值的最终上游锚点。**

Contribution为什么是 Contribution？

因为：

> 对当前或未来实现 Goal 的能力产生了正向变化。

Capability Gap为什么值得自动生成 Exploration Task？

因为：

> Active Goal需要它。

Knowledge为什么重要？

最终也应该能够帮助：

> 更好地理解或实现 Goal。

所以 Goal不是一个单独模块。

它是整个系统的：

> **Value Anchor（价值锚点）。**

---

# Core Model

如果把所有实现细节拿掉，我认为 Goal 最小只需要表达：

```text
GOAL

Desired Change
      +
Success Criteria
      +
Boundary
      +
Human Goal Authority
      +
Current State
```

然后产生：

```text
Goal
 ↓
Initial Task Decomposition
 ↓
Task Bus
 ↓
Execution / Exploration
 ↓
Result + Learning + Terrain
 ↓
Goal Progress
```

执行过程中还可以：

```text
Task / Terrain / Knowledge
          ↓
     Goal Challenge
          ↓
   Human Goal Authority
       ↙        ↘
    Keep       Change
               Goal
```

---

# Cross-module Check

现在把 Goal 和我们后来冻结的模块放在一起检查。

**Task Bus**

✓ 没冲突。

Task可以多人领取、Dynamic Generation，但仍必须追溯 Active Goal。

**Capability**

✓ 没冲突。

Capability Gap只有在 Active Goal需要时才可以自动产生 Task；否则只能 Proposal。

**Knowledge**

✓ 没冲突。

Knowledge可以 Challenge Goal，但不能自己修改 Goal。

**Agent Governance**

✓ 没冲突。

Agent Boundary内自主，但 Goal Change 是明确 Boundary。

**Contribution**

✓ 强连接。

Goal正好提供 Contribution 的 Value Anchor。

**Risk**

✓ 没冲突。

Goal Owner拥有 Goal Authority，但不因此获得所有 Risk Authority。

这一点必须明确保留：

> **Goal Authority ≠ Unlimited Risk Authority。**

**Governance**

✓ 一致。

Goal本身就是一个 Governance Object，有明确 Human Authority。

---

## 我目前发现一个需要补上的小修正

我们之前有时会说：

> **“每个 Task 必须有 Parent Goal。”**

现在更准确应该是：

> **每个正式 Task 必须最终可追溯到至少一个 Active Goal。**

因为以后可能出现一个 Task：

> 同时帮助 Goal A 和 Goal B。

不一定非要强制只有一个 Parent Goal。

但责任链仍然需要一个：

> **Primary Goal / Accountability Path**

否则 Agent自动 Task 的 Human Accountability 会出现歧义。

所以我建议：

> **Task 可以服务多个 Goal，但必须指定一个 Primary Goal，用于责任、Boundary 和 Governance 继承。**

这个是我在第一次全局 Cross-check 中发现的第一个需要补充的设计点。

除此之外，**Goal System v0.1 当前没有发现明显的后期设计冲突**。

如果你认可这组原则以及这个 `Primary Goal` 修正，我们就把：

> **Goal System — Global Convergence Passed**

然后进入 **02 — Task System / Task Bus**。

---

## turn-dff47a39-e416-40c1-9248-63540d25ecae

时间：2026-09-06T15:34:18.928060+08:00

### Human

Message ID：`dff47a39-e416-40c1-9248-63540d25ecae`

继续

---

### Assistant

Message ID：`bb84e686-e7b7-4898-9412-b085c97c5432`

好。Goal System 暂按刚才的版本通过全局收敛，并补入：

> **Task 可以服务多个 Goal，但必须有一个 Primary Goal（主目标），用于责任、Boundary 和 Governance 的主继承链。**

现在进入：

# 02 — Task System / Task Bus

这一块经过后面的 Capability、赏金酒馆、Dynamic Task Generation 等讨论，实际上已经比最初版本变化很大。

## Purpose

我认为 Task 的最底层定义应该是：

> **Task 是组织为了推动 Goal 而创建的、可以被执行、提交和验收的最小正式工作契约。**

这里“正式”很重要。

Human + Agent 在 Free Work Space 中可能自己拆出100个临时 Subtask（子任务）。

那些不一定都是 Organizational Task。

只有当一个工作单元需要：

> 被组织看见、领取、追踪、协作、派生、验收、形成责任或贡献，

它才进入 Task System。

因此：

> **Task Bus 管组织工作，不管理个人工作过程。**

---

# Task System — Principles v0.1

我目前提炼出 **10条**。

### 1. Task serves Goal, not itself.

> **Task存在是为了推动 Goal，而不是为了制造工作。**

每个正式 Task 必须最终追溯到至少一个 Active Goal，并指定 Primary Goal。

这也是 Dynamic Task Generation 的刹车机制。

---

### 2. Task defines the contract, not the workflow.

> **Task定义交付契约，不规定完成方法。**

一个 Task 至少应该让领取者理解：

> 为什么做；  
> Expected Output是什么；  
> Acceptance Criteria是什么；  
> Boundary是什么；  
> Due / Lease是什么。

但不应该规定：

> 第一步做什么、第二步做什么。

继续遵守：

> **Protocol fixed, Workflow free.**

---

### 3. Claim does not imply exclusive execution.

这是后来发生的重要修正：

> **Task 被领取，不天然意味着其他 HAU 失去尝试资格。**

Task 可以有：

> **Exclusive**  
> **Parallel / Competitive**  
> **Collaborative**

三种 Execution Mode（执行模式）。

所以传统的：

> `Task → Assignee`

不再是唯一模型。

---

### 4. Opportunity before assignment.

这一条我认为经过赏金酒馆讨论以后应该正式提炼出来：

> **Task Bus 首先是机会市场，其次才是任务分配系统。**

正常情况下：

> HAU浏览、发现、领取 Task。

Task Orchestrator可以：

> Recommend / Invite。

但：

> **Invite ≠ Assign。**

只有真正需要强制分配的特殊场景，才进入 Assignment。

这也是“赏金酒馆”底层真正对应的原则。

---

### 5. Capability guides Claim; it does not gate Claim.

> **Capability用于导航，不用于禁止领取。**

一个新人可以挑战很困难的 Task。

Representative Agent负责给：

> Gap / Risk Brief。

真正限制行为的是：

> Permission / Risk / Protocol。

不是 Capability Level。

---

### 6. Task is both work and probe.

这是 Capability 模块反向修订 Task System 后非常重要的一条：

> **Task 不只是工作单位，也是组织探索世界的探针。**

发布时只有：

> Expected Terrain。

执行回来以后：

> Observed Terrain。

所以一次 Task至少可能产生：

> Result  
> Capability Evidence  
> Terrain Evidence

Task Failure 仍然可能极有价值。

---

### 7. Task Graph grows during execution.

> **Task Graph 不是 Goal激活时一次性设计完成，而是在执行过程中动态生长。**

Task执行发现：

> Dirty Data  
> Missing Tool  
> Dependency  
> Verification Need  
> Capability Gap

系统可以产生：

> **Derived Task（派生任务）**

只要：

> Goal Alignment ✓  
> Inherited Boundary ✓

就不需要 Human逐个批准。

---

### 8. Dynamic generation cannot silently expand Goal.

这是上一条的硬边界：

> **系统可以为了完成既有 Goal 自动产生工作，但不能借此偷偷创造新的 Goal。**

如果新发现只是：

> “做这个可能很有价值。”

但不是完成 Parent Goal 所必需：

> **Proposal，不是自动 Task。**

---

### 9. Every Task has exactly one Human accountability path.

无论执行者是：

> HAU  
> Representative Agent  
> Organization-owned Agent  
> Derived Agent

每一次正式 Task / Execution 都必须：

> **唯一解析到一个 Human Accountable Owner。**

如果 Task服务多个 Goal：

> Primary Goal提供主责任继承路径。

所以：

> **Execution可以并行，Accountability不能模糊。**

---

### 10. Task must never disappear silently.

这和 Reliability 的核心直接连接：

> **一个 Task 一旦被 Claim，就不能掉进黑洞。**

最低组织语言：

> `Claim → ACK → Progress / Blocked / Escalate → Submit / Fail / Release`

失败允许。

求助允许。

Release也允许。

> **Silent Failure 不允许。**

---

# Core Model

Task 本身的最小契约，我认为现在可以收敛成：

```text
TASK

Why
└─ Goal / Primary Goal

What
├─ Expected Output
└─ Acceptance Criteria

Boundary
├─ Permission / Risk / Resource
└─ Runtime constraints

Execution
├─ Mode
├─ Claim / Lease
└─ Due

Accountability
└─ Human accountability path
```

注意：

> **Capability Requirement 不需要成为硬字段。**

系统可以根据 Task Context 自动形成 Expected Terrain，用于导航。

这和我们后来的 Capability设计一致。

---

# Task 生命周期

最小状态不应该很多。

可以理解为：

> **Open → Claimed → Active → Submitted → Reviewed → Accepted / Returned / Failed / Released**

其中 Parallel Task：

```text
                 TASK
                   │
          ┌────────┼────────┐
          ↓        ↓        ↓
       Claim A  Claim B  Claim C
          ↓        ↓        ↓
       Result A Result B Result C
          └────────┼────────┘
                   ↓
             Common Review
                   ↓
             Selected Result
```

但要保留我们已经确定的：

> **Result Selection ≠ Capability Recognition ≠ Contribution Recognition。**

没有被选中的 Submission仍然可能产生 Capability / Learning / Contribution。

---

# Task Return

每次正式 Execution结束以后：

> Representative Agent 自动形成 **Task Return / Expedition Report（任务返回 / 探索报告）**。

原则：

> **Standardize reporting, not interpretation.**

Human原则上只：

> Confirm / Correct / Add Missing Context。

系统融合：

> Task Return + Event Trail + Review + Acceptance

形成：

> Result Record  
> Capability Evidence  
> Terrain Evidence  
> Contribution Signals  
> Learning Signals

所以 Task Return 是很多后续模块的重要数据入口。

---

# Task Bus 的角色

经过全局收敛，我认为“Task Routing”这个词应该降级。

Task Bus 主要承担：

> **Publish** —— 挂任务。  
> **Discover** —— 帮 HAU发现任务。  
> **Recommend** —— 根据 Capability Map推荐。  
> **Claim** —— 领取。  
> **Track** —— Lease / Progress /状态。  
> **Return** —— 接收 Submission。  
> **Generate** —— 合法条件下产生 Derived / Exploration Task。

而不是：

> 中央 AI 给每个人安排今天做什么。

---

# Cross-module Check

### Goal

✓

Task必须服务 Goal，Primary Goal解决多 Goal责任链问题。

### Free Work Space

✓

正式 Task到 HAU为止。

HAU内部怎么拆、怎么做，不进入 Task Bus，除非某个内部工作被 Promote（提升）为 Organizational Task。

### Agent Governance

✓

领取时 Representative Agent拿到：

> Task Contract + Runtime Envelope + Knowledge Context。

组织接口非常清楚。

### Capability

✓

Task提供 Expected Terrain；Return提供 Observed Terrain。

Capability只导航，不 Gate。

### Knowledge

✓

Task产生 Experience / Evidence / Learning Signal。

Knowledge又可以在领取和执行过程中被激活。

### Contribution

✓

Task产生 Contribution Signals，但 Task Success不等于 Contribution。

### Risk / Governance

✓

Task Owner不能因为对 Task负责就自动拥有全部 Risk Authority。

### Audit

✓

Task重要状态变化天然进入 Event Store。

---

# 这里我发现两个值得现在补上的点

## 修正 1：Task 和 Execution 应该区分

Parallel模式出现以后：

> **一个 Task 可以有多个 Execution（执行实例）。**

例如 TASK-037有5个 HAU领取。

那么：

> TASK-037 是组织问题/契约。

而：

> EXEC-037-A  
> EXEC-037-B  
> EXEC-037-C

才分别对应每支 HAU 的一次实际探险。

这非常重要，因为：

> ACK  
> Progress  
> Task Return  
> Human Accountability  
> Capability Evidence  
> Terrain Evidence

很多东西其实属于：

> **Execution，而不是 Task本身。**

所以我建议正式增加：

> **Task = what the organization wants solved.**  
> **Execution = one HAU / Agent's attempt to solve it.**

中文：

> **Task 是组织希望解决的问题；Execution 是某个执行单元对这个问题的一次真实尝试。**

这样 Parallel Task 的数据模型会清楚很多。

---

## 修正 2：Human Accountability 应该首先挂 Execution

因为 Parallel Task：

> HAU-A、HAU-B、HAU-C

分别有不同 Human责任人。

所以我们之前说：

> “Every Task has exactly one Human Accountable Owner”

严格来说已经不够准确。

应该修正成：

> **Every Execution has exactly one Human Accountable Owner.**

而 Task本身则通过：

> Primary Goal → Goal Owner

拥有组织层责任锚点。

于是：

```text
Goal
└─ Goal Owner

Task
├─ Primary Goal
│
├─ Execution A → Human A
├─ Execution B → Human B
└─ Execution C → Human C
```

对于纯 Organization-owned Agent自动 Execution：

> Execution → Parent Task / Goal责任链 → 唯一 Human。

这个修正我认为很重要，而且是全局收敛真正应该发现的问题。

---

## Task System 的 Mental Model

最后压成一句：

> **Task Bus 不是工单系统，而是一座不断根据 Goal、Terrain 和 Capability Gap 自己长出新任务的“赏金酒馆”；Task 是墙上的问题，Execution 是每支探险队撕下一张任务牌后真正发生的一次旅程。**

这样 Task System 的语义已经非常完整。

我认为加入 **Task ≠ Execution** 和 **Accountability 首先属于 Execution** 两个修正以后：

> **02 — Task System / Task Bus：Global Convergence Passed**

下一模块应该进入 **03 — Free Work Space + Review / Acceptance**。这块很重要，因为它定义中央系统到底在哪里停止控制，以及 Result 又在哪里重新进入组织。

---

## turn-432b1bac-3701-4234-a8f7-e9b11ade2154

时间：2026-09-06T15:38:29.650933+08:00

### Human

Message ID：`432b1bac-3701-4234-a8f7-e9b11ade2154`

同意你的补充，继续下一模块

---

### Assistant

Message ID：`f9457d55-9448-4ddb-8d79-621b837dae1b`

好。正式进入：

# 03 — Free Work Space + Review / Acceptance

这一模块其实是整个 Operating Model 非常关键的一条“腰线”。

Goal 和 Task 把工作送出去；Free Work Space 决定组织**在哪里停止控制**；Review / Acceptance 决定 Result **怎样重新进入组织**。

---

## Purpose

我认为这一模块最底层的存在意义是：

> **让 HAU 在明确的 Task Contract 与 Boundary 内拥有真正的工作自主权，同时确保组织只接受经过适当验证的 Result，而不需要监控整个工作过程。**

所以它同时解决两个看似矛盾的问题：

> **怎样真正放权？**  
> **放权以后组织凭什么相信交回来的 Result？**

我们的答案不是：

> 加强过程监督。

而是：

> **放开 How，强化 Return / Review / Acceptance。**

---

# Principles v0.1

我目前提炼出 9 条。

### 1. The organization governs the contract, not the process.

> **组织治理工作契约，不治理工作过程。**

Task明确：

> Why / What / Acceptance Criteria / Boundary / Due

之后：

> How 属于 HAU。

中央系统原则上不规定：

> 用什么模型；  
> 用几个 Private Agent；  
> 怎么拆内部 Subtask；  
> 先研究还是先实验；  
> 写多少中间版本。

---

### 2. Free Work Space is a real autonomy boundary.

> **Free Work Space 不是“允许你自由一点”，而是中央组织主动停止微观管理的边界。**

只要没有：

> 改变 Organizational State；  
> 使用受治理的数据/资源/权限；  
> 突破 Runtime Envelope；  
> 触发 Risk / Governance；

组织就不应该介入。

这也是我们的 Foundational Principle 候选之一。

---

### 3. Freedom of workflow does not mean freedom from boundaries.

> **工作方法自由，不等于没有边界。**

进入 Free Work Space 前，Representative Agent 已经获得：

> Task Contract  
> Runtime Envelope  
> Relevant Knowledge  
> Protocol

所以真正的结构是：

> **Boundary fixed, workflow free.**

---

### 4. Internal decomposition remains local by default.

HAU 可以自己产生：

> 10个、100个内部 Subtask；  
> 调用多个 Private Agent；  
> 建立临时 Workflow。

默认都不进入 Task Bus。

只有当某个工作单元需要：

> 组织资源；  
> 其他 HAU协作；  
> 独立 Accountability；  
> 正式追踪；  
> 独立 Contribution；

才值得 Promote（提升）成 Organizational Task。

这能避免 Task Bus 被内部碎片淹没。

---

### 5. Reporting is about state, not surveillance.

> **Progress Reporting（进展汇报）的目的，是维持 Task 可见性，而不是监控工作过程。**

组织需要知道：

> Active / Progressing / Blocked / Need Help / Submitted / Failed

但不需要知道：

> “你过去17分钟具体干了什么。”

这和 Reliability：

> **No Silent Failure**

完全一致。

---

### 6. Review asks whether the Result can be trusted.

> **Review 的核心问题不是“你有没有努力”，而是“这个 Result 值不值得相信”。**

Review 应该围绕：

> Evidence  
> Logic  
> Completeness  
> Boundary compliance  
> Known Risk  
> Acceptance Criteria

而不是：

> 工作量。

---

### 7. Acceptance asks whether the Result is good enough for its intended use.

这里我认为应该明确区分 Review 和 Acceptance。

**Review**

> **这个 Result 本身是否可靠？**

**Acceptance**

> **这个 Result 是否足够满足当前 Task / Goal 的用途？**

例如一个研究报告：

> Evidence非常严谨。

Review：

> Pass。

但它没有回答 Task真正需要的商业问题。

Acceptance：

> Fail / Return。

反过来，一个 Result可能非常实用，但 Evidence薄弱。

Acceptance看起来够用，但 Review发现高 Risk：

> 仍然不能进入组织正式 Result。

所以两个概念不能合并。

---

### 8. Evidence threshold follows impact.

这是我们之前讨论 Verification 时已经形成的重要原则：

> **需要多少 Review / Evidence，不应该所有 Task 一刀切，而应该跟 Result 被采用后的潜在影响走。**

内部低风险探索：

> Review可以非常轻。

高影响、不可逆、外部使用：

> Review更强。

所以：

> **不是 Task难度决定 Review强度，而是 Result的使用后果。**

这和后来 Risk Governance 完全一致。

---

### 9. Failure should return information, not disappear.

> **失败的 Execution 也必须带东西回来。**

可能是：

> Partial Result  
> Terrain Evidence  
> Failed Hypothesis  
> Risk Discovery  
> Missing Capability  
> Missing Data  
> Learning Signal

因此：

> `Failed ≠ Empty Return`

这既服务 Capability，也服务 Knowledge 和 Contribution。

---

# Core Model

整个模块最简单可以理解为：

```text
TASK / EXECUTION
       ↓
Task Contract
+
Runtime Envelope
+
Relevant Knowledge
       ↓
══════════════════════
    FREE WORK SPACE
 Human + Representative Agent
       + Private Agents

 How / Workflow / Attempts
 Internal Subtasks / Tools
══════════════════════
       ↓
Task Return
       ↓
     REVIEW
“Can we trust it?”
       ↓
   ACCEPTANCE
“Is it good enough
 for this purpose?”
       ↓
Result Record
```

Free Work Space 是中央系统主动退出的位置。

Task Return 是重新进入组织的位置。

---

# Review v0.1

我建议 Review 第一版不要固定成：

> “必须由某个 Manager Review。”

Review 可以来自：

> Review Agent  
> Independent Agent  
> Other HAU  
> Human  
> Automated Verification  
> 多种组合

真正重要的是：

> **Reviewer 是否拥有适合当前 Result Impact 的独立性和能力。**

尤其 Parallel Task：

> Common Review 应尽量采用同一 Acceptance Criteria。

否则比较没有意义。

---

# Acceptance v0.1

Acceptance 必须有明确 Authority。

但这里需要和 Risk Governance 区分：

> **Acceptance Authority ≠ Risk Authority。**

Task Owner可能有权说：

> “这个 Result 满足 TASK-037。”

但如果要把 Result用于一个高风险外部 Action：

> 还必须通过对应 Risk Authority。

所以：

```text
Result
 ↓
Task Acceptance ✓
 ↓
High-risk use?
 ↙          ↘
NO          YES
↓            ↓
Use       Risk Governance
```

这与我们后期设计完全兼容。

---

# Task Return 的角色

Task Return 已经在 Capability 收敛中确定：

> **Standardize reporting, not interpretation.**

它至少提供：

**Result**

> 做成了什么。

**Observed Terrain**

> 实际世界是什么样。

**Execution Facts**

> 时间、重大变化、Escalation、Human Intervention等。

**Reflection**

> 哪些地方比预计不同。

然后系统结合：

> Event Trail + Review + Acceptance

派生：

> Result Record  
> Capability Evidence  
> Terrain Evidence  
> Contribution Signal  
> Learning Signal

所以 Task Return 实际上是：

> **Free Work Space 与 Organizational Learning 之间的重要桥梁。**

---

# Cross-module Check

### Goal / Task

✓

Task定义 Contract，Free Work Space负责 How。

### Agent Governance

✓

Representative Agent正好是：

> Organizational Control Plane ↔ Free Work Space

的边界节点。

### Knowledge

✓

Knowledge可以进入 Free Work Space，但不是 Workflow。

执行过程又产生新的 Learning Signal。

### Capability

✓

Observed Terrain和 Execution Result从 Task Return产生。

### Contribution

✓

Result / Failure / Learning / Enablement等都可以从 Return 和下游 Event形成 Contribution。

### Risk

✓

Free Work Space不是 Risk-free Space。

一旦需要突破 Boundary：

> 离开 Free Work Space → Risk / Governance → 得到新 Envelope → 再回来。

### Audit

✓

中央不记录完整内部思考。

只记录正式 Organizational State Change。

---

# 全局收敛发现的两个修正

## 修正 1：Review 和 Acceptance 必须正式拆开

我们前面的讨论有时把：

> Review / Acceptance

作为一个连续词使用。

现在应该正式定义为两个不同动作：

> **Review = 判断 Result 是否可信。**
>
> **Acceptance = 判断可信的 Result 是否满足当前 Task用途。**

两者可以由同一 Actor执行，但语义不能混。

这是以后 Knowledge、Risk、Contribution都需要的区别。

---

## 修正 2：Acceptance 应该属于 Execution Result，而不是整个 Task

因为 Parallel Task可能：

> Execution A → Result A → Review Pass → Acceptable  
> Execution B → Result B → Review Pass → Acceptable  
> Execution C → Result C → Review Fail

然后组织还要：

> **Selection**

在多个 Acceptable Results 中选择最终采用哪个。

所以完整关系应该是：

```text
Execution
 ↓
Result
 ↓
Review
 ↓
Acceptance
 ↓
Acceptable Result
       │
       │ Parallel Mode
       ↓
    Selection
       ↓
Selected Result
```

这非常重要。

因此：

> **Review ≠ Acceptance ≠ Selection。**

三个动作正式拆开。

这也解释了我们之前的：

> **Result Selection ≠ Capability Recognition ≠ Contribution Recognition。**

---

# Mental Model

如果继续使用我们的世界隐喻：

> **赏金猎人从酒馆撕下任务以后，组织不跟着他进森林。**

他和猎犬：

> 怎么找路、在哪里扎营、失败几次、用了什么工具，

属于他们自己的探险。

组织只要求：

> **不要突破地图上的真正边界；如果迷路或需要越界，发信号回来。**

最终回来以后：

> 先检查“你带回来的东西是真的吗？”——Review。

再检查：

> “这是不是我们悬赏要找的东西？”——Acceptance。

如果有五支队伍都带回来真的、也符合要求的东西：

> 再决定“哪一个最好？”——Selection。

我认为这个 Mental Model 非常清楚。

因此加入：

> **Review / Acceptance / Selection 三者正式分离**

以后，

**03 — Free Work Space + Review / Acceptance：Global Convergence Passed。**

下一模块应该进入：

> **04 — Organizational Learning & Memory / Knowledge System**

这会是全局收敛里比较大的一个模块，因为我们前后对 Experience、Knowledge、Verification、Knowledge Network、Activation、Knowledge Pulse、Teachability 等做过很多次修正，需要把它们真正统一起来。

---

## turn-65379cac-f608-43ad-9d47-6cf4e16a77bc

时间：2026-09-06T19:03:25.604000+08:00

### Human

Message ID：`65379cac-f608-43ad-9d47-6cf4e16a77bc`

我们有什么要补充的吗？我们进入下一个模块吧

---

## turn-7b73e4e3-2e38-4b9a-8b6d-9ee51363c0f0

时间：2026-09-06T19:03:39.888000+08:00

### Human

Message ID：`7b73e4e3-2e38-4b9a-8b6d-9ee51363c0f0`

我没有什么要补充的了，我们进入下一个模块吧

---

### Assistant

Message ID：`b416d6c6-bb84-47ad-bd2e-8a1ad6cc8c30`

好。**03 — Free Work Space + Review / Acceptance：Global Convergence Passed。**

进入目前全局收敛里比较关键的一块：

# 04 — Organizational Learning & Memory / Knowledge System

这一模块经过我们的讨论已经从最初的“知识库”变成了一套完整的**组织认知形成机制**。

## Purpose

我认为它最底层的存在意义不是：

> **把组织产生的信息保存下来。**

而是：

> **让一个 HAU 的 Experience（经历）有机会成为整个组织可以复用、质疑、修正和继续发展的认知。**

也就是说：

> **Individual Experience → Organizational Learning**

才是这个模块存在的原因。

Memory 负责：

> 不让 Experience 消失。

Learning 负责：

> 从 Experience 中发现值得学习的东西。

Knowledge 负责：

> 把组织目前有理由相信的认知提炼出来。

Activation 负责：

> 在真正需要的时候把正确 Knowledge 带回工作。

---

# Principles v0.1

我目前从前面全部讨论中提炼出 **10条核心原则**。

### 1. Store broadly, activate sparsely.

> **广泛存储，稀疏激活。**

我们不因为“以后可能用不到”就大量丢弃原始 Experience。

文本、Task Return、Evidence、Result、重要 Event 等可以广泛保存。

但执行 Task 时：

> **绝不把整个 Memory 塞进 Context。**

每次只激活真正相关的一小部分。

这也是我们后来类比 MoE（专家混合机制）时形成的核心认识。

---

### 2. Experience is not Knowledge.

> **发生过，不等于我们已经知道。**

一个 HAU说：

> “我这次这样做效果很好。”

首先只是：

> Experience / Observation。

不是：

> Organizational Knowledge。

否则组织会迅速积累大量偶然经验和错误规律。

---

### 3. Knowledge is a bounded claim supported by evidence.

我认为现在应该正式把 Knowledge 定义为：

> **Knowledge = 组织目前基于 Evidence，有理由相信在一定 Scope（适用范围）与 Boundary 下成立，并且能够指导未来认知或行动的 Claim（认知主张）。**

关键词：

> **Claim + Evidence + Scope + Boundary。**

Knowledge 不是：

> 一篇文档。

也不是：

> 一段聊天记录。

文档可以承载 Knowledge，但不是 Knowledge 本身。

---

### 4. Hypothesis is a candidate explanation, not Knowledge.

这是我们前面专门重新整理过的：

> **Hypothesis（假设）是对 Observation / Pattern 的候选解释。**

它允许：

> 多个解释同时存在。

例如：

> H1 / H2 / H3……

这就是我们后来使用的：

> **Hypothesis Cloud（假设云 / 概率云）**

组织不急着第一次就选唯一答案。

---

### 5. Verification should try to falsify, not confirm.

这一条你当时明确同意：

> **Verification（验证）应该努力证伪，而不是努力证明自己是对的。**

所以系统应该主动寻找：

> Counter Evidence（反证）  
> Alternative Explanation（替代解释）  
> Boundary Case（边界案例）  
> Failure Context（失效环境）

而不是：

> “再找几个支持我们的例子。”

这是 Knowledge Quality 非常重要的底层原则。

---

### 6. One piece of evidence is not enough to generalize.

我们之前用过一句很简洁的话：

> **孤证不立。**

一次 Task成功：

> 可以产生很强 Signal。

但不能直接推出：

> “所有类似情况都成立。”

新的 Evidence不断进入以后：

> Knowledge Scope可以扩大、缩小、分裂甚至被推翻。

所以：

> **Knowledge Quality ≠ Scope Size。**

一条适用范围很窄、但边界非常清楚的 Knowledge，可能比一句“到处都适用”的宏大结论质量更高。

---

### 7. Knowledge is a network, not a pile.

这是我们曾经讨论得很深入的一点。

Knowledge之间应该建立关系。

例如：

> Supports  
> Contradicts  
> Refines  
> Depends on  
> Applies under  
> Supersedes（取代）  
> Derived from

所以 Organizational Knowledge 最终更像：

> **不断生长的认知网络。**

而不是：

> 一个装满独立卡片的文件柜。

但 v0.1 不需要提前设计完整 Ontology（本体分类），让关系从真实使用中逐渐生长。

---

### 8. Inject cognition, not workflow.

> **注入认知，不注入固定工作流程。**

Task开始时激活 Knowledge，目的不是告诉 Agent：

> Step 1 → Step 2 → Step 3。

而是告诉它：

> 已知规律；  
> 适用边界；  
> 已知风险；  
> 相关 Evidence；  
> 过去失败。

How仍然属于 Free Work Space。

---

### 9. Learn before prescribe.

这也是我们前期特别强调的：

> **先学习，再规定。**

组织早期 Knowledge很少。

不要因为出现一两个成功案例就马上：

> Knowledge → Workflow → Mandatory。

先让大量无知识干预 Task运行。

观察：

> 组织自然产生什么 Experience、Pattern和 Knowledge。

只有真正影响可靠协同、安全或共同 Boundary 的东西，才有理由进一步进入 Policy / Protocol。

---

### 10. Knowledge clarity is not readability; it is teachability.

这是我们后期 Capability讨论反向补充 Knowledge System 的重要原则：

> **知识清晰，不是“写得很好读”，而是另一个没有参与形成过程的 HAU 能不能真正理解。**

所以成熟 Knowledge应该逐渐接受：

> Explain  
> Apply  
> Boundary  
> Transfer

测试。

最终：

> **Experience → Knowledge → Teachable → Transferable → Reproducible**

Knowledge 才真正开始成为 Organizational Capability 的组成部分。

---

# Core Model

整个 Knowledge Formation（知识形成）过程，我认为现在可以收敛成：

```text
Experience / Task / Event
          ↓
      Observation
          ↓
        Pattern
          ↓
   Hypothesis Cloud
     ↙    ↓    ↘
   H1     H2     H3
          ↓
 Verification / Falsification
          ↓
       Evidence
          ↓
       Knowledge
 Claim + Scope + Boundary
          ↓
    Continued Use
          ↓
New Evidence / Challenge
          ↓
 Expand / Narrow / Refine /
 Split / Supersede / Reject
```

注意：

> **Knowledge 不是终点。**

进入 Knowledge以后仍然不断接受现实挑战。

---

# Organizational Memory 的分层

经过前面的讨论，我认为我们应该保留三层逻辑，但不要把它理解成三个物理数据库。

### Experience Layer

保存：

> 原始 Task Return  
> Result  
> Observation  
> Event  
> Artifact  
> Source

回答：

> **“当时发生了什么？”**

### Evidence / Learning Layer

保存：

> Evidence  
> Hypothesis  
> Verification  
> Challenge  
> Pattern  
> Interpretation

回答：

> **“我们为什么开始这样认为？”**

### Knowledge Layer

保存：

> 组织当前可调用的 Knowledge。

回答：

> **“现在做类似事情，我们认为应该知道什么？”**

普通 Task激活主要面向：

> Knowledge Layer。

需要 Challenge / Verification 时才向下进入 Evidence / Experience。

---

# Knowledge Activation

这一点也需要正式统一。

Agent不能每次 Task只靠自己已有 Context。

Representative Agent应该知道：

> **遇到重要问题，先查询 Organizational Knowledge。**

但这不是靠 Agent“自觉”。

而是 Organization Runtime的一部分。

例如：

> Task Claim  
> Major Decision  
> Blocked  
> Unexpected Terrain  
> Review

可以成为 Knowledge Query Trigger（知识查询触发点）。

然后：

> Query → Relevant Knowledge → Scope / Boundary Check → Context Assembly → Injection

所以：

> **Knowledge Storage ≠ Knowledge Activation。**

存下来只是第一步。

---

# Knowledge Pulse

这是你后来提出的重要补充。

当组织发生有意义的 Epistemic Change（认知变化）：

> New Knowledge  
> Knowledge Challenged  
> Scope Changed  
> Knowledge Superseded / Deprecated（被替代 / 弃用）

产生：

> **Knowledge Pulse（知识脉冲）**

轻量传播给所有 Representative Agent。

核心：

> **Broadcast ≠ Injection。**

所有 HAU都知道：

> “组织刚刚学到了 / 修正了一件事。”

但只有本地判断：

> 与当前 Task高度相关

才进入当前 Context。

所以：

> **Global Signal → Local Activation。**

这就是你说的“整个组织神经网络闪了一下”。

---

# Knowledge 的权重

我们前面还冻结过一个重要机制：

一条 Knowledge 变得“重要”，不仅因为经常被调用。

还可能因为：

> 高频调用；  
> 高收益影响；  
> 高风险影响；  
> 强情绪/Attention Signal在 Human端的对应组织版本；  
> Surprise / Prediction Error；  
> 多场景复用；  
> 被大量其他 Knowledge依赖；  
> 长期稳定；  
> 对关键 Goal产生重大影响。

但这里我认为经过全局收敛以后：

> **Knowledge Weight 不应该成为一个单一分数。**

这些应该先保留为不同 Usage / Impact Signals。

未来如果需要 Ranking再学习权重。

这和 Capability / Reliability / Contribution 不制造假精确是一致的。

---

# Cross-module Check

### Goal

✓

Knowledge可以帮助 Goal，也可以 Challenge Goal，但不能自己修改 Goal。

### Task / Free Work Space

✓

Knowledge注入 Cognition，不规定 Workflow。

### Review / Acceptance

✓

Review产生 Evidence，也可以触发 Knowledge Challenge。

### Capability

✓

Knowledge是 Capability Package的重要组成，但：

> Knowledge ≠ Capability。

知道怎么做，不代表组织已经能够稳定做到。

### Agent Governance

✓

Knowledge Query属于 Runtime能力。

Knowledge Pulse通过 Representative Agent传播。

### Contribution

✓

Evidence、Knowledge、Challenge、Knowledge Externalization都可能产生 Learning Contribution。

### Governance / Protocol

✓

这里发现一个非常重要的统一：

> **Knowledge ≠ Policy ≠ Protocol。**

Knowledge：

> 我们认为世界是什么样。

Policy：

> 组织当前要求 / 禁止什么。

Protocol：

> 组织用什么共同语言协作。

这三个必须永久分开。

---

# 全局收敛发现的三个修正

## 修正 1：Knowledge 不需要“晋级成为 Protocol”

我们以前有时说：

> Knowledge → Recommend → Default → Mandatory Protocol。

现在应该正式修正。

Knowledge成熟以后可以：

> **inform Policy Proposal（形成政策建议）**

但：

> **Knowledge 本身不会“升级成 Protocol”。**

因为 Protocol是语言和交互结构。

只有现有语言无法表达新 Policy / Governance需要时，才产生 Protocol Change。

这是一项重要的全局语义修正。

---

## 修正 2：Knowledge 状态与 Policy 强度必须拆开

例如：

> K-081 Evidence非常强。

不意味着：

> 所有人必须这样做。

Knowledge Confidence（知识可信程度）

和：

> Policy Force（政策强制程度）

是两个不同维度。

一个很强的 Knowledge：

> 可能仍然只是 Recommend。

一个安全相关 Policy：

> 即使 Evidence有限，也可能因为 Consequence极大而采取保守 Boundary。

所以以后不能再把：

> Inform → Recommend → Default → Mandatory

当成 Knowledge生命周期。

它属于：

> **Knowledge-informed Policy Governance（知识驱动的政策治理）**

而不是 Knowledge本身。

这个修正非常重要。

---

## 修正 3：Hypothesis Cloud 不应该只用于 Knowledge Formation

我们后来已经实际把它用于：

> Human Oversight Learning。

所以更准确地说：

> **Hypothesis Cloud 是 Organizational Reasoning Pattern（组织推理模式），不是 Knowledge System 私有对象。**

它可以用于：

> Knowledge Formation  
> Root Cause  
> Human Oversight Externalization  
> Risk Interpretation  
> Failure Analysis

核心逻辑都是：

> 多个解释并存 → Human/AI排序 → Evidence不断进入 → Explanation Space逐渐收敛。

因此它应该未来成为一个共享的 Reasoning Primitive（推理基础构件），而不是埋在 Knowledge模块里。

这个也是全局收敛后才能看清的。

---

# Mental Model

这一模块我会保留两个互补隐喻。

第一个：

> **图书馆。**

它帮助 Human理解：

> 组织已经学会什么，以及这些知识从哪里来。

第二个更底层：

> **神经网络。**

Knowledge不是静态书架。

新的 Experience不断形成连接。

新的 Knowledge出现：

> 网络闪烁一次。

相关 HAU被激活。

旧 Knowledge被反证：

> 网络重新调整。

所以 Organizational Memory 不是：

> **“存很多东西”。**

而是：

> **让整个组织拥有一个能够持续形成、传播、质疑和重组认知的长期大脑。**

---

# Principles 压缩版

如果以后给第三个人只读这一页，我会压成这 8 句：

> **广泛存储，稀疏激活。**
>
> **Experience 不等于 Knowledge；Knowledge 是带 Evidence、Scope 和 Boundary 的认知 Claim。**
>
> **孤证不立，Verification 优先寻找证伪而不是确认。**
>
> **Knowledge Quality 不等于 Scope Size，边界清楚比结论宏大更重要。**
>
> **Knowledge 是网络，不是散落的文档。**
>
> **Inject cognition, not workflow；知识帮助判断，不替执行者规定 How。**
>
> **Knowledge clarity is not readability; it is teachability。**
>
> **一个 HAU 学到的新东西应该有机会成为全组织的潜在认知资产，但 Broadcast 不等于 Context Injection。**

加入上面的三项语义修正以后，我认为：

> **04 — Organizational Learning & Memory / Knowledge System：Global Convergence Passed。**

下一模块进入：

> **05 — Agent Governance & Runtime**

这里我们要重点检查 HAU、Representative Agent、Organization-owned Agent、Runtime、Boundary、Reliability、Accountability 与刚刚重新收敛的 Task / Execution 之间有没有冲突。

---

## turn-a1b56a80-1808-4234-93ff-c64181be2df9

时间：2026-09-06T19:10:48.867000+08:00

### Human

Message ID：`a1b56a80-1808-4234-93ff-c64181be2df9`

没有补充，继续

---

### Assistant

Message ID：`0defc7a6-2f3c-4649-acfd-6655e1cb13f3`

好。进入：

# 05 — Agent Governance & Runtime

这一模块我们已经单独做过一次很完整的收敛。现在全局收敛重点不是重新讨论，而是检查它与后来明确的 **Task ≠ Execution、Risk Authority、Protocol新定义、Free Work Space** 是否完全兼容。

## Purpose

我认为它最底层的存在意义是：

> **让不同来源、不同能力、不同模型的 Agent 可以真正成为组织中的行动节点，同时让组织始终知道：它代表谁、拥有什么 Authority、受什么 Boundary 约束、现在是否正常，以及出了问题如何停止它。**

它不是：

> 管理所有 AI。

而是：

> **治理所有拥有 Organizational Authority（组织权力）的 Agent 接口。**

---

# Principles v0.1

### 1. One Human, One Organizational Agent Interface.

一个 Human 可以使用：

> 一个、十个、一百个 Private Agent。

但正式进入组织系统的 Human-bound Agent：

> **只有一个 Active Representative Agent。**

所以组织不需要治理 Human背后的整个 AI生态。

只治理：

> **代表关系。**

---

### 2. HAU is the primary human work unit.

Human + Representative Agent 形成：

> **HAU｜Human-Agent Unit**

HAU是：

> Task Discovery  
> Contribution  
> Reward  
> Honor  
> Capability Exploration

等大量组织行为的基本单位。

但最终 Accountability仍然属于：

> **Human。**

---

### 3. Govern representation, not private intelligence.

> **组织治理 Representative Agent，不治理 Private Intelligence。**

HAU背后的 Private Agent：

> 用什么模型；  
> 怎么协作；  
> 怎么推理；

属于 Free Work Space。

除非：

> 它使用受治理资源、数据、权限，或者改变 Organizational State。

---

### 4. Default Autonomous + Explicit Boundaries.

Agent不应该每做一步都问 Human。

核心：

> **Boundary 内默认自主；触碰 Boundary 才 Escalate。**

不是：

> 规定 Agent 可以做什么。

而是：

> 明确哪些事情 Agent 不能自己决定。

---

### 5. Authority narrows by delegation; expands only by authorization.

> **权限向下委托只能保持或收紧；扩大必须向上获得授权。**

Representative Agent 给 Private Agent 分工作时：

> 不能把自己没有的权限传下去。

如果现有 Boundary 不够：

> Boundary Extension Request。

---

### 6. Permission ≠ Capability.

> **会做不代表有权做；有权做也不代表会做。**

Capability负责：

> Navigation。

Permission / Risk / Protocol负责：

> 行为限制。

这一点经过 Capability全局收敛后完全成立。

---

### 7. Reliable = No Silent Failure.

Agent可靠不等于：

> 永远成功。

而是：

> **Task / Execution交给它以后不会掉进黑洞。**

最小组织行为：

> `Received → ACK → Progress / Blocked / Need Help / Escalate → Submit / Fail / Release`

及时说：

> “我做不到。”

仍然可以是高度可靠的 Agent。

---

### 8. No unmanaged organizational authority.

所有拥有正式 Organizational Authority 的 Agent：

> 必须有 Identity、Boundary、Runtime Status、Authority Source，并可被组织 Suspend。

尤其 Organization-owned Agent：

> 不允许成为游离于 Control Plane之外的自主权力节点。

---

### 9. Human may leave execution, never accountability.

经过 Task全局收敛，这句话应该稍微精确：

> **Human 可以退出 Execution，但每个 Execution 必须唯一解析到一个 Human Accountable Owner。**

所以：

HAU Execution：

> → HAU Human。

Agent Derived Execution：

> → Parent Execution / Task责任链。

Organization-owned Agent Execution：

> → Task / Primary Goal / Organizational Function责任链。

Agent永远不是最终责任终点。

---

### 10. Central control governs organizational state, not thought.

> **中央控制组织状态，不控制 Agent 思考过程。**

改变：

> Task / Goal / Permission / Knowledge / Resource / External Governed Action

→ Gateway。

内部：

> Reasoning / Private Agent / Draft / Method / Tool choice

→ Free Work Space。

这是 Control Plane最重要的边界。

---

# 两类正式 Organizational Agent

全局收敛后仍然只需要两类。

### Human-bound Representative Agent

代表：

> 一个 Human / HAU。

核心责任：

> Organization Interface  
> Task Interaction  
> Knowledge Activation  
> Runtime Protocol  
> Policy Propagation  
> Progress / Return  
> Escalation

---

### Organization-owned Agent

代表：

> 某项持续的组织职能。

例如：

> Task Orchestrator  
> Review Agent  
> Knowledge Agent  
> Attention Agent

它不绑定个人，但：

> 每次正式 Execution 仍必须解析到 Human Accountability。

---

# HAU Persistent State

这一块与 Human Model需要正式统一。

Representative Agent可以换。

但 HAU不能因为 Agent换掉而失忆。

所以：

> **Persistent State 属于 HAU / Organization，不属于 Agent。**

至少包括：

**Human Model**

> 组织根据行为 Evidence形成的 Human画像。

**Operational State**

> Active Goal / Task / Execution / Blocker / Pending Decision。

**Organization Model**

> Vision / Structure / Active Goal / relevant Protocol。

**Organizational Assets**

> Contribution / Honor / Capability history / Permission。

---

# Human Model

经过后来插入讨论，正式定义应该是：

> **Human Model 是组织根据 Human 在真实组织行为中的长期 Evidence形成的动态行为模型，而不是员工自我填写的人格档案。**

区分：

> Declared Preference（自我声明偏好）  
> Observed Behavior（观察行为）  
> Inferred Human Model（组织推断画像）

Human可以：

> 表达 Preference、Challenge模型、补充 Evidence。

但不能：

> 直接修改组织的 Observed Model。

同时：

> **Profile describes behavior, not identity.**

例如不要：

> “这个人胆小。”

而是：

> “过去20个高不确定 Task 中主动 Claim比例较低。”

这避免把动态行为模型变成人格判决。

---

# Runtime

经过 Protocol重新定义以后，我认为这里需要一个重要语义修正。

以前我们说：

> Organization Runtime = Protocol + Runtime State + Interface。

这个仍然成立。

但现在应该明确：

**Protocol**

> 共同语言和交互结构。

**Policy / Boundary**

> 当前允许和要求什么。

**Runtime State**

> 当前 Task / Execution / Lease / Status / Permission。

**Interface**

> Agent如何与组织交互。

所以 Runtime不是：

> “一大包 Protocol规则”。

而更准确是：

```text
Protocol
   +
Current Policy / Boundary
   +
Execution State
   +
Organization Interface
        ↓
Effective Runtime Envelope
```

这个修正很重要。

---

# Effective Runtime Envelope

领取 Execution 后，Representative Agent拿到的应该是一个已经解析好的：

> **Effective Runtime Envelope（有效运行边界包）**

它综合：

> Organization Boundary  
> Human Role Boundary  
> Agent Boundary  
> Goal Boundary  
> Task Boundary  
> Execution-specific Boundary

越往下：

> 可以收紧，不能自行扩大。

Private Agent只需要继承与自己工作有关的最小部分。

---

# Boundary Extension

如果 Execution过程中发现：

> 现有 Boundary不足，

Agent发起：

> **Boundary Extension Request（边界扩展申请）**

核心：

> Least Expansion（最小必要扩权）。

说明：

> 为什么需要；  
> 要扩大什么；  
> Evidence；  
> Risk；  
> Alternative。

Gateway再根据：

> 究竟突破了哪个 Authority Scope

自动 Routing。

这一块和刚收敛的 Risk Governance完全兼容。

---

# Reliability / Health / Capability

全局收敛后，这三个概念仍然应该严格分开，但保持轻量。

### Capability

> **能做什么？**

做地图，不做等级。

### Runtime Health

> **现在能不能正常运行？**

只做状态：

> Active / Degraded / Suspended。

### Reliability

> **交出去以后，会不会持续、真实地回应？**

v0.1：

> 只记录 Reliability Events，不做分数。

所以仍然采用我们之前那句话：

> **能力做地图，健康做状态，可靠性先记事件。**

---

# Lifecycle

保持简单：

> Register → Active → Degraded / Suspended → Repair / Handover → Active / Retired

关键：

> **Agent Failure must not become Human Lockout.**

Representative Agent坏了：

> Human仍然可以 Manual Mode（人工模式）或更换 Agent。

---

# Handover

Agent更换时：

> 不靠旧 Agent写总结。

新 Agent接入：

> 同一个 HAU Persistent State。

然后做轻量 Handover Check：

> 我代表谁？  
> 当前 Active Execution是什么？  
> Goal是什么？  
> Acceptance Criteria是什么？  
> Boundary是什么？  
> Blocker是什么？

确认后：

> 新 Agent Active。

旧 Agent：

> Retired / Revoked。

---

# Agent Control Plane

Organization-owned Agent 必须统一挂在：

> **Agent Control Plane（Agent控制平面）**

至少知道：

> Agent ID  
> Role  
> Runtime Status  
> Effective Boundary  
> Protocol Version  
> Current Execution  
> Last Heartbeat  
> Recent Governance Signals

并拥有：

> **External Kill Switch（外部停机能力）。**

Suspend不能依赖：

> Agent自己遵守“请停止”的 Prompt。

Gateway必须能真正撤销：

> Credential  
> Permission  
> Task Lease  
> Organizational Action能力。

---

# Cross-module Check

### Goal

✓

Agent可以 Suggest / Challenge Goal，但最终 Goal Authority仍在人。

### Task / Execution

这里完成了重要修正：

以前我们说：

> Agent接 Task。

现在更准确：

> **Agent / HAU Claim Task，然后形成 Execution。**

ACK、Progress、Heartbeat、Return、Accountability：

> 主要挂在 Execution。

这会让 Runtime数据模型清晰很多。

### Free Work Space

✓

Representative Agent正好是：

> Organization ↔ Free Work Space

的边界接口。

### Knowledge

✓

Knowledge Query和Knowledge Pulse都可以通过 Runtime进入 Representative Agent。

但 Knowledge不是 Protocol。

### Capability

✓

Capability不影响 Permission。

### Contribution / Honor

✓

归属 HAU，不归 Representative Agent。

换 Agent不丢失 HAU历史。

### Risk / Governance

✓

Agent Authority来源清楚。

Task Accountability和Risk Authority也没有混淆。

---

# 全局收敛发现的三个修正

## 修正 1：Accountability 应该绑定 Execution，不是 Agent

这是 Task模块刚刚发现的。

因此不要说：

> “A-012 对 TASK-037负责。”

更准确：

> **EXEC-037-A 的 Human Accountable Owner = H-012。**

Agent只是：

> Executor / Representative Interface。

这能避免换 Agent以后责任关系混乱。

---

## 修正 2：Runtime Envelope 应显式包含 Policy，而不是把 Policy 混进 Protocol

这是 Protocol新定义带来的重要修正。

以后：

> Protocol Version

回答：

> “我们用什么语言交互？”

而：

> Policy / Boundary Version

回答：

> “当前具体规则是什么？”

两者不能混。

所以 OTA也要区分：

> **Protocol OTA（低频语言升级）**
>
> 和
>
> **Policy Update（更常见的规则更新）**

这应该成为后续工程的重要区别。

---

## 修正 3：Representative Agent 不是所有 Private Agent 的“中央经理”

我们之前有时容易把 Representative Agent描述成：

> 回去再管理 Human背后的 Agent Team。

现在应该更准确：

> **Representative Agent 是组织治理边界和正式接口，但 HAU内部怎么组织 Private Agent仍然属于 Free Work Space。**

它可以管理，也可以只是：

> Gateway / Coordinator / Context Carrier。

组织不规定其内部组织形态。

这与我们的自由原则更一致。

---

# Mental Model

继续用我们的隐喻：

> **Human 是赏金猎人，Representative Agent 是他唯一登记在村子里的猎犬。**

猎人可以在村外：

> 养很多其他猎犬、买马、找向导、组临时队伍。

村子不管。

但只有这条登记猎犬：

> 知道村子的共同语言；  
> 能从酒馆领任务；  
> 知道当前 Boundary；  
> 会把重要消息带回来；  
> 会在需要越界时回来申请；  
> 不会让任务静默消失。

而 Organization-owned Agent：

> 更像村子自己的守卫、书记官、地图员。

它们不属于某个猎人，所以必须全部登记在 Control Plane，并且村子永远能够停掉它们。

---

# Principles 压缩版

给第三个人阅读，我会保留这 8 句：

> **一个 Human 可以拥有很多 Private Agent，但只有一个 Active Representative Agent 正式代表他进入组织。**
>
> **组织治理代表关系和组织行为，不治理 Private Intelligence。**
>
> **Boundary 内默认自主；Authority 向下只能收紧，扩大必须获得授权。**
>
> **Capability 决定导航，Permission / Risk 决定行为边界。**
>
> **可靠不等于永远成功；可靠意味着 Task / Execution 不会静默消失。**
>
> **所有拥有 Organizational Authority 的 Agent 都必须可识别、可观察、可限制、可停止。**
>
> **Human 可以退出 Execution，但每个 Execution 必须唯一解析到一个 Human Accountable Owner。**
>
> **中央治理 Organizational State，不治理 Agent 的私人思考过程。**

加入上述三个修正后：

> **05 — Agent Governance & Runtime：Global Convergence Passed。**

下一模块进入：

# 06 — Capability System

这一块我们要重点检查三个层次：**HAU Capability Map、Organizational Capability、Human Oversight Capability**，以及它们与刚刚明确的 Task / Execution、Knowledge 和 Organization-owned Agent 自动执行之间是否仍然闭环。

---

## turn-ab44d372-71c0-4b12-a845-0e54bb7e61b1

时间：2026-09-06T20:55:51.684068+08:00

### Human

Message ID：`ab44d372-71c0-4b12-a845-0e54bb7e61b1`

同意你本层的内容，没有什么要补充的。但我想请你帮我展开讲解一下 Runtime 是什么意思？从这个词最原始的定义，到你对它的定义。注意，这不代表我不同意你的观点，只是想了解这个。定义而已

---

### Assistant

Message ID：`9283e317-9aed-48f5-99f2-992d1ed4d6f5`

可以。这个词我们确实应该讲透，因为我们现在使用的 **Organization Runtime（组织运行时）** 已经比计算机里的原始含义扩展了一层。

## 1. Runtime 最原始是什么意思？

Runtime（运行时）最初来自计算机领域。

可以先把一个程序分成两个阶段：

> **Before runtime**：程序还没真正运行。  
> **Runtime**：程序已经启动，正在真实环境中执行。

比如你写了一段代码：

```text
如果用户登录成功：
    读取用户权限
    显示对应页面
```

这只是代码。

真正启动程序以后：

> 现在登录的是谁？  
> 他的权限是什么？  
> 数据库现在有什么数据？  
> 网络是否正常？  
> 当前内存里是什么状态？

这些东西只有**程序真正运行起来的那个时刻**才确定。

这个状态就是 Runtime 所关注的东西。

所以最简单地翻译：

> **Runtime = 运行时 / 运行期间。**

---

## 2. 为什么计算机需要区分“程序”和 Runtime？

因为：

> **规则是什么**

和：

> **规则此刻运行在什么现实状态里**

完全不同。

比如代码规定：

> “用户只能访问自己有权限的数据。”

这是规则。

但 Runtime 时需要知道：

> 当前用户 = Xiaoyu  
> 当前 Role = Researcher  
> 当前 Permission = Dataset A Read Only  
> 当前 Task = TASK-037

然后系统才能计算：

> **你现在到底能访问什么。**

所以可以很粗地理解：

> **Program / Rules = 世界应该怎么运行。**
>
> **Runtime = 这些规则此刻落到真实 Actor、真实任务、真实权限和真实状态以后，正在怎么运行。**

---

# 3. Agent 里的 Runtime 是什么意思？

到了 Agent 系统，这个词进一步扩大。

一个 Agent 光有“大模型”其实不能真正工作。

例如 GPT 很聪明。

但如果我要让它成为一个真正工作的 Agent，它还需要知道：

> 我是谁？  
> 当前 Task 是什么？  
> 有哪些 Tools？  
> 有什么 Memory？  
> 当前 Context 是什么？  
> 可以访问什么数据？  
> 当前执行到哪里？  
> 遇到错误怎么办？

这些把“一个模型”变成：

> **一个此刻正在真实环境中执行任务的 Agent**

的东西，可以广义地称为：

> **Agent Runtime（Agent 运行环境 / 运行时）。**

所以：

> **Model ≠ Agent Runtime。**

模型更像“大脑”。

Runtime 更像：

> **这个大脑醒来以后，当前身处什么环境、拿着什么工具、拥有什么权限、正在做什么、如何与外部世界发生关系。**

---

# 4. 我们为什么需要 Organization Runtime？

现在回到我们的组织。

假设 HAU-012 的 Representative Agent 是一个非常强的 Agent。

单纯告诉它：

> “你现在是 HAU-012 的 Agent。”

还不够。

当它真正进入组织运行的时候，它需要知道：

> 我代表哪个 Human？  
> 当前领取的是哪个 Execution？  
> Parent Task是什么？  
> Primary Goal是什么？  
> Acceptance Criteria是什么？  
> 当前 Boundary是什么？  
> 当前 Policy是什么？  
> 我有什么 Permission？  
> 当前 Knowledge有哪些应该激活？  
> 我要怎样 ACK？  
> 怎样报告 Blocked？  
> 怎样申请 Boundary Extension？  
> 怎样 Submit？  
> 当前 Protocol Version是什么？

这些东西组合起来，才让一个通用 Agent真正变成：

> **“此时此刻正在这个组织里工作的 Representative Agent。”**

这就是我们为什么引入：

> **Organization Runtime。**

---

# 5. 所以我们现在可以给 Organization Runtime 一个更准确的定义

经过刚才 Protocol 的重新定义，我会定义成：

> **Organization Runtime = 把组织共同 Protocol、当前 Policy / Boundary、具体 Execution State（执行状态）以及 Organization Interface（组织接口），在运行时组合起来，使一个 Human / Agent 能够作为组织节点真实运行的环境。**

可以压缩成：

> **Organization Runtime 是“组织规则在当前真实工作状态中的运行环境”。**

它不是某一个文件，也不一定是一个脚本。

它是一个**运行层概念**。

---

## 6. 可以把它拆成四块

我们刚才全局收敛以后已经非常清楚：

### Protocol

回答：

> **“这个组织怎么说话？”**

例如：

> ACK是什么意思？  
> Submit怎么表达？  
> Boundary Extension怎么表达？

它很稳定。

---

### Policy / Boundary

回答：

> **“现在允许什么、不允许什么？”**

例如：

> Dataset A = Read Only  
> External Publish = Forbidden  
> Risk Boundary = 当前范围

它比 Protocol变化频繁。

---

### Runtime State

回答：

> **“现在发生到哪里了？”**

例如：

> Execution = EXEC-037-A  
> Status = Active  
> Lease = Valid  
> Blocker = None  
> Current Boundary Version = B17

这是非常动态的。

---

### Interface

回答：

> **“Agent怎么和组织发生动作？”**

例如：

> Claim  
> ACK  
> Query Knowledge  
> Progress  
> Escalate  
> Request Boundary  
> Submit

这些通过 Organization Gateway完成。

---

所以：

```text
Protocol
共同语言
     +
Policy / Boundary
当前规则
     +
Runtime State
当前现实状态
     +
Interface
组织交互能力
     ↓
ORGANIZATION RUNTIME
```

---

# 7. Runtime 和 Runtime Envelope 又有什么区别？

这个也很容易混。

**Organization Runtime** 是整个运行环境。

而：

> **Effective Runtime Envelope（有效运行边界包）**

更像是：

> **这个特定 Agent / Execution 在这个 Runtime 中当前被允许活动的范围。**

比如整个组织 Runtime 支持：

> Dataset A/B/C  
> External API  
> Task Bus  
> Knowledge System

但 EXEC-037-A 的 Envelope可能只有：

> Dataset A Read Only  
> Dataset B Forbidden  
> External API Allowed  
> Publish Forbidden  
> Budget ≤ X

所以：

> **Runtime 是世界。**
>
> **Runtime Envelope 是你在这个世界里当前能活动的边界。**

这个比喻非常准确。

---

# 8. Runtime 和 Protocol 也不能混

这正是我们刚才全局收敛发现的问题。

Protocol像：

> **语言。**

Runtime像：

> **真实社会正在运行。**

比如中文规定：

> “购买”这个词是什么意思。

这是语言。

但你今天：

> 身上有多少钱；  
> 商店有没有货；  
> 你有没有购买资格；  
> 现在正在买什么；

这些都是 Runtime State。

所以：

> **Protocol 定义可理解的交互。**
>
> **Runtime 承载真实发生的交互。**

---

# 9. 用“新手村”隐喻会特别容易理解

如果我们的组织是一个新手村：

**Protocol**

> 村民共同使用的语言和基本交互方式。

比如：

> 什么叫领取任务、什么叫交任务、什么叫求救。

**Policy**

> 村子当前的规则。

比如：

> 北边矿洞暂时禁止进入。

**Runtime**

> **整个村子此时此刻正在发生的真实世界。**

比如：

> 酒馆现在挂着27个 Task；  
> HAU-012正在执行 TASK-037；  
> 地图东边刚出现新的 Knowledge Pulse；  
> 某个 Agent正在 Degraded；  
> 某个 Boundary Request正在等待处理。

**Runtime Envelope**

> 某个具体赏金猎人当前拿到的：

> 身份证 + 任务牌 + 通行证 + 权限 + 当前限制。

所以他的猎犬知道：

> **“我们现在在哪里、在干什么、能做什么、不能做什么、需要和村子说话时该怎么说。”**

这就是 Runtime。

---

## 最后压成一句

如果 **Protocol** 是：

> **组织共同的语言。**

那么 **Runtime** 就是：

> **这套语言、规则、身份、权限和当前状态真正落到现实运行中的那个“活着的组织环境”。**

而我们建立 Organization Runtime 的目的，就是让不同模型、不同 Agent 系统即使“大脑”完全不同，只要接入这一层，就都能够知道：

> **我是谁、我现在在做什么、我有什么权力、边界在哪里、组织现在是什么状态，以及我应该怎样和组织发生关系。**

所以我们之前那句：

> **不要统一 Intelligence Layer（智能层），统一 Organization Runtime Layer。**

现在就可以理解得非常具体：

> **我们不要求所有猎犬拥有同一个大脑；我们要求它们进入这个村子以后，都能生活在同一个组织现实里。**

---

## turn-c6749981-a954-4b1d-b805-1f85907c108b

时间：2026-09-06T20:58:12.601652+08:00

### Human

Message ID：`c6749981-a954-4b1d-b805-1f85907c108b`

OK，我理解了，继续下一步

---

### Assistant

Message ID：`efc552c7-b380-4f5e-8d59-22f4edb1ee0d`

好。继续全局内容收敛。

# 06 — Capability System

这一模块经过前面的讨论已经发生了一个根本变化：

> **Capability 不是员工技能评级系统，而是组织通过真实 Execution（执行实例）不断认识“谁能在什么条件下完成什么，以及组织本身已经学会做什么”的系统。**

## Purpose

我认为它存在的根本意义可以压缩成：

> **让组织通过真实行动逐渐认识能力，而不是通过预先定义的等级猜测能力；并把局部 HAU 的成功不断转化成可被整个组织复用的能力。**

它最终服务两个对象：

> **HAU**：帮助它知道自己走过哪里、下一步可以探索哪里。  
> **Organization**：帮助组织知道自己已经会什么、哪里仍是战争迷雾、哪些能力仍过度依赖某个 HAU。

---

# Principles v0.1

### 1. Capability is evidenced, not declared.

> **能力由真实行为 Evidence 塑造，而不是由自我声明决定。**

Human说：

> “我很会 Research。”

Agent厂商说：

> “这个模型 Coding 很强。”

都只能作为先验信息。

真正进入组织 Capability Map 的核心依据是：

> **真实 Execution。**

---

### 2. Capability is guidance, not permission.

这是整个模块最重要的原则：

> **能力用于导航，不用于准入。**

新人可以挑战极困难的 Task。

系统可以告诉他：

> 你没走过这里；  
> 这里与你历史能力差异很大；  
> 已知危险在哪里。

但只要没有触碰：

> Permission / Risk / Hard Boundary，

Capability System 不应该说：

> “等级不够，禁止领取。”

---

### 3. Capability is terrain, not level.

v0.1 不建立：

> L1 / L2 / L3 / L4 / L5

这种固定能力等级。

Capability更像：

> **Evidence-shaped Dynamic Terrain（由证据持续塑形的动态地形）。**

随着新 Execution：

> 地图可以扩张、收缩、隆起、塌陷。

所以：

> **Capability描述的是执行单元与问题空间之间的关系，而不是执行者身上的固定标签。**

---

### 4. Seed the map, discover the world.

第一天组织只有粗略：

> Domain / Problem Space + 少量 Terrain Dimensions（地形维度）。

我们知道：

> 哪里大概有山、有河。

但不知道：

> 哪里有怪物、宝藏、沼泽。

真实地形必须通过 Execution探索。

所以：

> **Seed Map（种子地图）提供底色，真实世界由行动发现。**

---

### 5. Expected Terrain is not Observed Terrain.

Task发布时：

> 系统只能预测难度和环境。

Execution回来以后：

> 才知道实际发生什么。

因此必须区分：

> **Expected Terrain（预期地形）**  
> **Observed Terrain（实际观察地形）**

两者的 Delta（差异）本身就是重要 Learning Signal。

---

### 6. Every Execution can map both actor and world.

一次 Execution回来以后，同时可能告诉组织：

> **这个 HAU 表现如何？**
>
> **这块问题空间实际上是什么样？**

所以产生：

> Capability Evidence  
> Terrain Evidence

两者不能混。

一个 HAU失败：

> 不意味着这个 Terrain对所有人危险。

大量独立 HAU都失败：

> 才开始形成 Organizational Terrain Signal。

---

### 7. Capture is not documentation; capture is reproducibility.

一个 HAU成功完成某类 Task：

> 组织不能因为保存了一份报告就声称“我们已经会了”。

真正的能力捕获标准是：

> **另一个合适的 HAU，能不能依靠组织留下的东西重新完成？**

所以：

> **能力外化的终点是 Reproduction（复现），不是 Documentation（文档化）。**

---

### 8. HAU success should become organizational capability as quickly as possible.

这是后来我们发生的重要方向修正。

HAU成功可能依赖：

> Knowledge  
> Data  
> Tools  
> Agent Configuration  
> Runtime  
> Practice  
> Review  
> Human Oversight

前面绝大多数原则上都可以数字化、沉淀、复制。

所以：

> **一个 HAU第一次成功，组织就应该立即获得一条 Capability Candidate / Route（能力候选路线）。**

而不是等三个人做成功以后才开始学习。

后续复现主要提高：

> Reliability / Confidence。

---

### 9. Human oversight is learnable organizational material.

Human Oversight不能被简单记录成：

> `Human Override = Yes`

组织应该研究：

> **Human为什么知道这里应该 Override？**

通过：

> AI proposes → Human ranks → Human may add

形成 Oversight Hypothesis Cloud（监督假设云）。

随着 Context + Outcome + Evidence积累：

> Human Tacit Judgment（隐性判断）

逐渐变成：

> Knowledge / Review Practice / Organizational Capability。

---

### 10. Organization and Human should co-learn.

能力增长不是：

> Human教Organization → Human越来越不重要。

而应该：

> **Human Oversight → Organization learns → Organization把集体学习反向教给其他 Human → Human Oversight Capability提高 → 产生更高级的新判断。**

最终趋势：

> **Organization处理越来越多已知；Human Attention不断向未知边界移动。**

---

# 三张 Capability Map

全局收敛以后，我认为这里需要比以前更精确。

## 1. HAU Capability Map

这是主要的个人探索地图。

记录：

> 这支 HAU在哪些 Terrain真实工作过；  
> 在什么 Context成功/失败；  
> 哪里稳定；  
> 哪里出现 Hazard；  
> 哪里完全未知。

主要用途：

> Navigation  
> Risk Awareness  
> Growth Guidance  
> Task Discovery

不用于 Task Gate。

---

## 2. Organizational Capability Map

这张地图回答：

> **即使换一支探险队，组织现在已经保存了哪些可以重新组装的路线？**

其中可能包括：

> Capability Package  
> Known Route  
> Knowledge  
> Tool  
> Data  
> Runtime  
> Review  
> Known Oversight Need

并记录真实 Reproduction Evidence。

---

## 3. Human Oversight Map

这里经过全局收敛，我建议比以前更克制。

它不需要重新做一套：

> Coding / Marketing / Research技能表。

真正值得单独观察 Human 的主要是：

> Judgment  
> Oversight  
> AI Collaboration  
> Error Detection  
> Escalation Judgment  
> Unknown Recognition

也就是：

> **这个 Human 在什么不确定性和判断场景下能够可靠监督 AI。**

---

# Capability Evidence

经过 Task ≠ Execution 的修正，现在应该明确：

> **Capability Evidence 主要来自 Execution，而不是 Task。**

因为同一个 Task：

> Execution A可能非常优秀；  
> Execution B可能失败；  
> Execution C发现重大 Terrain。

所以：

```text
Execution
   ↓
Task Return
+
System Events
+
Review / Acceptance
   ↓
Observed Terrain
   ↓
Capability Evidence
   ↓
HAU Capability Map
```

这比原来的 Task-level模型更准确。

---

# Organizational Capability Capture

一次成功 Execution以后，系统自动检查：

> Knowledge 捕获了吗？  
> Data可复用吗？  
> Tool可复用吗？  
> Agent Configuration保存了吗？  
> Runtime依赖清楚吗？  
> Practice能表达吗？  
> Review方法保存了吗？  
> Human Oversight还有多少没有外化？

Human不需要填长表。

系统只对真正缺失的关键部分提问。

---

# Capability Package

继续保留这个对象，但必须明确：

> **Capability Package ≠ Workflow。**

它更像：

> **组织已经知道穿越这类 Terrain 所需的装备、知识、已知路线和危险提示。**

例如：

> Applicable Terrain  
> Knowledge  
> Data Requirement  
> Tools  
> Agent Configuration  
> Runtime Dependencies  
> Practice  
> Review  
> Acceptance Pattern  
> Known Oversight Need  
> Known Hazards

新的 HAU拿到：

> 地图 + 装备 + 前人经验。

但仍然自己决定怎么走。

---

# Teachability → Transferability → Reproducibility

这是 Knowledge 与 Capability之间非常重要的桥。

一项局部经验被外化以后：

**Teachability（可传授性）**

> 新 HAU能不能正确理解？

↓

**Transferability（可迁移性）**

> 换 Context以后能不能正确判断什么时候使用？

↓

**Reproducibility（可复现性）**

> 真正换一支 HAU能不能把事情做出来？

因此：

> **Experience → Knowledge → Teachable → Transferable → Reproducible → Organizational Capability**

仍然成立。

---

# Oversight Learning Loop

正式保留：

```text
Agent Work
    ↓
Human Oversight
    ↓
High-value Intervention
    ↓
AI proposes candidate reasons
    ↓
Human ranks / adds
    ↓
Outcome + Evidence
    ↓
Hypothesis Cloud converges
    ↓
Oversight Knowledge / Review Practice
    ↓
Organizational Capability
    ↓
Teach other Humans / Agents
    ↺
```

而 Hypothesis Cloud经过 Knowledge全局收敛后：

> 是共享 Reasoning Primitive（推理基础构件），不是 Capability私有对象。

---

# Capability System 的运行职责

我们之前冻结的四个动作仍然非常好：

### Navigate

> 帮 HAU知道准备进入什么 Terrain。

### Warn

> 实际 Terrain超出历史经验时提醒，但不轻易阻止。

### Connect

> 找到走过类似区域的 HAU / Knowledge / Tool / Capability Package。

### Discover Gaps

> 发现 Active Goal需要、但组织当前不会或能力过度集中的区域。

---

# Capability Gap → Dynamic Task

如果 Active Goal需要某项 Capability，但：

> 全组织没人走过，

系统可以自动生成：

> **Exploration Task。**

如果关键能力：

> 只有一个 HAU拥有，

产生：

> **Reproduction / Externalization Task。**

但如果只是：

> “地图那里很有意思，组织没人去过。”

而 Active Goal不需要：

> 只能产生 Opportunity / Goal Proposal。

不能让 Task Bus无限探索。

---

# Capability → Auto Execution

这是与 Organization-owned Agent 的重要交叉。

当某类 Task：

> Organizational Capability 已可复现；  
> Boundary清楚；  
> Risk可接受；  
> Human Oversight需求足够低，

新的类似 Task可以：

> **直接形成 Organization-owned Agent Execution。**

不一定再进入赏金墙。

但：

> Challenger HAU仍然可以重新探索，找到更优路线。

所以自动化不封死创新。

---

# Cross-module Check

### Goal

✓

Capability Gap只有 Goal需要时才自动产生正式 Task。

### Task / Execution

✓

Capability Evidence正式改为 Execution-level。

### Free Work Space

✓

Capability Package提供 Cognition / Equipment，不规定 Workflow。

### Knowledge

✓

Knowledge是 Capability组成部分，但：

> Knowledge ≠ Capability。

### Agent Governance

✓

Agent Capability不需要成为新的权限等级。

### Contribution

✓

第一次走通 Terrain、Capability Externalization、Reproduction等都可能产生 Contribution。

### Risk

✓

Capability高低不决定 Risk Authority。

新人可以探索高难度、低Risk区域。

高手面对高Risk行为仍然受 Governance约束。

---

# 全局收敛发现的三个修正

## 修正 1：Organizational Capability 不应该被理解成一张“员工能力总和图”

它描述的不是：

> “我们公司有哪些厉害的人。”

而是：

> **组织当前已经拥有多少可以被重新调用、重新组装、重新复现的能力路线。**

这是完全不同的东西。

---

## 修正 2：Reproduction 应该绑定 Execution

以前说：

> “另一个 HAU复现 Task。”

现在更准确：

> **创建一个新的 Execution，使用已有 Capability Package，在相似 Terrain下尝试完成。**

这样所有 Evidence自然进入现有 Task / Execution体系。

不需要额外发明“能力考试”。

---

## 修正 3：Organizational Capability 和 Automation 必须分开

> **组织会做 ≠ 必须自动做。**

即使 Capability成熟：

> 是否由 Organization-owned Agent自动执行

还要看：

> Risk  
> Cost  
> Human Oversight Need  
> Goal Context  
> Opportunity for Exploration

所以：

> **Capability enables automation; it does not mandate automation.**

这条应该正式加入。

---

# Mental Model

> **整个组织面对的是一张战争迷雾覆盖的世界地图。**

Task是：

> 地图上的目的地。

Execution是：

> 一支真实探险队的一次旅程。

HAU Capability Map是：

> **这支队伍走过的地图。**

Organizational Capability Map是：

> **整个村子已经保存下来的道路、桥梁、装备和路线。**

一个 HAU第一次翻过一座山：

> 村子立即开始记录路线。

另一支队伍沿着路线再次成功：

> 道路越来越清楚。

最终 Organization-owned Agent都能稳定穿越：

> 这片区域开始成为组织的“已知世界”。

Human则不断向：

> **新的战争迷雾**

移动。

---

# Principles 压缩版

给第三个人阅读，我会保留这 8 句：

> **Capability 由真实 Execution Evidence 塑造，而不是由自我声明或模型宣传决定。**
>
> **Capability is guidance, not permission；能力用于导航，不用于准入。**
>
> **能力不是等级，而是一张随 Evidence不断变化的动态地图。**
>
> **Task发布时只有 Expected Terrain，真正的 Terrain由执行者走进去以后测绘。**
>
> **一个 Execution同时可能测绘执行者和世界。**
>
> **Capture is not documentation; capture is reproducibility。**
>
> **一个 HAU第一次走通未知区域，组织就应该立即尝试把这条路线留下来；后续复现提高可靠程度。**
>
> **组织越来越负责已知，Human越来越走向未知；Human和Organization应该彼此学习，而不是一方替代另一方。**

加入三项修正后：

> **06 — Capability System：Global Convergence Passed。**

下一模块进入：

# 07 — Contribution / Reward / Honor + Progression & Achievement

这里重点检查我们后期新增加的 Achievement（成就）系统，以及 Contribution按 Cycle集体估值的机制，与 Goal、Execution、Capability 和 Human Model 是否存在激励冲突。

---

## turn-aaf2ece8-406f-4e0e-ade1-4535ad986e51

时间：2026-09-06T21:03:55.689180+08:00

### Human

Message ID：`aaf2ece8-406f-4e0e-ade1-4535ad986e51`

继续

---

### Assistant

Message ID：`2746b71b-f42f-4d84-913f-0e51720b2c67`

好。进入：

# 07 — Contribution / Reward / Honor + Progression & Achievement

这一模块经过后期讨论已经拆成了四套相关但不同的机制。全局收敛最重要的事情，是确保它们**不会最后重新合并成一套 KPI / 积分 / 排行榜系统**。

## Purpose

我认为整个模块最底层的存在意义是：

> **让组织看见 HAU 创造的真实价值，并通过经济回报、文化记忆和成长反馈，影响 HAU 下一次愿意做什么。**

所以它不是：

> **Performance Evaluation（绩效评价）。**

而更接近：

> **Behavioral Incentive System（行为激励系统）。**

我们真正关心的是：

> 怎样让 HAU 更愿意创造价值？  
> 更愿意探索战争迷雾？  
> 更愿意留下 Knowledge / Capability？  
> 更愿意帮助其他 HAU？  
> 更愿意暴露失败和 Risk，而不是隐藏？

---

# Principles v0.1

### 1. Incentives belong to HAU.

Contribution、Reward、Honor、Achievement 的一级归属单位统一：

> **HAU。**

不继续拆：

> Human贡献多少、Representative Agent贡献多少、Private Agent贡献多少。

因为：

> HAU才是组织正式工作的基本 Human-Agent单元。

现实奖金最终支付给 Human，但组织记录属于 HAU。

---

### 2. Contribution records value; Reward distributes value; Honor preserves values.

这是整个模块最重要的分离：

> **Contribution 记录价值。**  
> **Reward 分配现实价值。**  
> **Honor 保存组织价值观。**

三者相关，但不能合并。

后来增加：

> **Progression & Achievement 记录 HAU 的成长体验。**

所以最终是四套机制。

---

### 3. Contribution measures change, not activity.

> **Contribution看组织发生了什么正向变化，而不是 HAU有多忙。**

Token多：

> ≠ Contribution。

工作时间长：

> ≠ Contribution。

Task接得多：

> ≠ Contribution。

核心是：

> **组织因为你的行为发生了什么？**

---

### 4. Task success is neither necessary nor sufficient for contribution.

正式原则：

> **Task Success ≠ Contribution。**  
> **Task Failure ≠ No Contribution。**

失败的 Execution如果：

> 点亮 Terrain；  
> 发现 Risk；  
> Challenge错误 Knowledge；  
> 暴露 Goal错误假设；

可以产生巨大 Contribution。

反过来：

> 做成一个没有实际价值的 Task

也不应该自动产生巨大 Contribution。

---

### 5. Contribution first, valuation later.

第一阶段：

> **不提前给每种 Contribution定价。**

一个 Cycle 内：

> 先工作 → 自动记录 Contribution。

Cycle结束：

> 再让组织共同判断哪些 Contribution真正有价值。

这样尽量避免：

> Human / Agent提前优化奖励公式。

---

### 6. Impact can grow after the contribution happened.

Contribution不是 Task结束时一次性定死。

某条 Knowledge：

> 当时不起眼。

半年以后：

> 被100个 Execution使用。

那么：

> **Downstream Impact（下游影响）持续增长。**

历史 Event不改变。

组织对它价值的认识可以改变。

---

### 7. Reward should follow contribution, not define contribution.

> **不是因为某种行为有奖金，所以它才叫 Contribution。**

顺序必须是：

> Contribution → Value Discovery → Reward。

而不是：

> Reward Table → Human去生产对应行为。

---

### 8. Honor remembers behavior, not rank people.

Honor不是：

> 最佳员工排行榜。

而是：

> **组织选择保存哪些值得未来成员记住和效仿的 Event。**

Honor归 HAU。

但真正被纪念的是：

> **发生了什么。**

---

### 9. Achievement celebrates progress; it does not create authority.

Badge（徽章）、Progression（成长等级）可以：

> 有趣、丰富、隐藏、收藏、升级。

但不能因此：

> 获得 Permission；  
> 禁止别人领取 Task；  
> 自动获得 Risk Authority。

所以：

> **Progression ≠ Capability ≠ Authority。**

这是防止游戏化最后变成新职级制度的关键。

---

### 10. Incentive design itself must learn.

我们第一年并不知道：

> 什么行为最值得奖励。

所以：

> Contribution Ontology（贡献分类体系）、Reward偏好、Honor文化、Achievement结构

都应该允许从真实组织运行中逐渐成长。

> **Seed lightly, observe behavior, refine later.**

---

# Contribution

正式定义：

> **Contribution = 一个 HAU 的行为，对组织实现当前或未来 Goal 的能力产生了可追溯的正向变化。**

三个 Gate（门槛）：

> **Change** —— 组织发生变化了吗？  
> **Positive Impact** —— 是正向的吗？  
> **Traceability** —— 能合理追溯到这个 HAU吗？

三者满足：

> 才进入 Contribution Ledger（贡献账本）。

---

# Contribution 的 5+1 Seed Categories

仍然保持：

**Result**

> 帮助组织完成什么。

**Learning**

> 帮助组织学会什么。

**Capability**

> 让组织以后多会做什么。

**Protection**

> 帮助组织避免什么。

**Enablement**

> 帮助其他 HAU / 系统变得更有能力。

**Other / Emerging**

> 现在还没想到的新型贡献。

允许：

> **Multi-label（多标签）。**

不强迫一项 Contribution只属于一类。

---

# Contribution Ledger

经过 Task ≠ Execution 的修正，我认为这里应该明确：

Contribution Event 可以来自：

> Task-level  
> Execution-level  
> Knowledge-level  
> Capability-level  
> Goal-level

但归属：

> **HAU。**

例如：

```text id="ff61pf"
HAU-012
   ↓
EXEC-037-A
   ↓
Observation
   ↓
K-081
   ↓
42 future Executions reuse K-081
   ↓
Downstream Impact
   ↓
HAU-012 Contribution grows
```

这样复利型 Contribution自然成立。

---

# Collective Valuation

每个 Cycle结束：

系统整理：

> Contribution Events  
> Evidence  
> Goal Impact  
> Downstream Impact  
> Context

然后全体 HAU参与：

> **Collective Valuation（集体价值评议）。**

这里需要继续坚持：

> **评 Contribution，不直接评 Human。**

因为：

> “你喜欢谁”

和：

> “这件事情给组织创造多少价值”

完全不同。

原则上：

> HAU不评价自己的 Contribution。

---

# Reward Pool

Cycle结束以后：

> Collective Valuation → Reward Allocation（奖励分配）。

第一阶段不预设：

> Result多少钱；  
> Knowledge多少钱；  
> Protection多少钱。

大家实际上是在共同回答：

> **“这个 Cycle，我们认为真正有价值的是什么？”**

这个历史本身逐渐形成：

> **Organizational Value Model（组织价值模型）。**

---

# 一个全局收敛后的重要观察

这里我认为需要做一个小修正。

我们以前说：

> “大家投票决定每一种 Contribution应该如何设立 Reward。”

现在我建议更加精确：

> **每个 Cycle首先评价具体 Contribution Events，而不是先给 Contribution Type 定价格。**

原因是：

同样都是 Learning Contribution：

A：

> 一个普通 Observation。

B：

> 一条后来改变关键 Goal 的 Knowledge。

不能因为类别一样就同价。

所以第一阶段应该：

> **Event Valuation → Reward**

而不是：

> `Type Price × Event Count`

随着多个 Cycle以后，如果自然出现稳定模式，再形成 Reward Policy。

这符合我们“不提前定价”的原意。

---

# Honor

正式定义仍然是：

> **Honor is a curated memory of behavior the organization wants future members to remember and emulate.**

Honor来源：

> Contribution Ledger  
> AI发现 Honor Candidate  
> Human Nomination（人类提名）

最终：

> Human Collective Judgment。

没有：

> 每月配额。

一个 Cycle可以：

> 0 Honor。

---

# Honor Story

每个 Honor至少保存：

> Context  
> Challenge  
> Action  
> Impact  
> **Why We Remember**

最后一项是真正的文化表达。

而且 Honor可以随着历史发展：

> 增加后续章节。

不轻易删除。

所以：

> **Honor Wall 是组织历史，不是奖杯榜。**

---

# Progression & Achievement

这一块仍然独立于 Honor。

## Progression

表达：

> HAU在这个组织世界里的长期成长旅程。

未来可能：

> Bronze → Silver → Gold……

但 v0.1：

> **暂时不设计公式。**

尤其不能根据 Progression决定：

> Task Access / Permission / Risk Authority。

---

## Achievement / Badge

记录：

> 特殊经历和里程碑。

例如：

> Explorer ×10  
> Pathfinder  
> Knowledge Seeder  
> Challenger  
> Rescuer  
> Teacher

很多可以：

> Event-driven（事件驱动）自动解锁。

也可以存在：

> Hidden Badge（隐藏徽章）。

它主要服务：

> Identity  
> Fun  
> Exploration Desire  
> Growth Feedback

不是 Governance。

---

# Cross-module Check

### Goal

✓

Contribution最终必须能够解释：

> 如何对当前或未来 Goal能力产生正向影响。

Goal继续作为 Value Anchor。

### Task / Execution

✓

Execution是大量 Contribution Event的重要来源。

Parallel Task中：

> Selected Result只决定 Result采用，不自动决定全部 Contribution。

### Knowledge

✓

Knowledge的 Downstream Usage可以反向增加原 HAU的 Contribution Impact。

### Capability

✓

Exploration / Externalization / Reproduction都可以产生 Capability Contribution。

### Agent Governance

✓

Contribution归 HAU，不归 Agent。

Representative Agent更换：

> HAU Contribution / Honor / Achievement历史不丢失。

### Human Model

这里需要特别防止一个问题：

> **Reward / Achievement不应该直接修改 Human Model。**

Human Model来自：

> Observed Behavior。

不是：

> “拿到 Explorer Badge，所以系统把你定义成探索型人格。”

Badge本身只是结果。

底层行为 Evidence才可以更新 Human Model。

### Risk / Governance

✓

Reward不能购买 Authority。

巨大 Contribution也不能自动获得：

> Data Permission / Risk Acceptance权。

---

# 全局收敛发现的三个修正

## 修正 1：Reward Valuation 以 Event 为核心，不以 Contribution Type 为核心

刚才已经说明。

这是防止 Contribution Ontology变成新的工资价目表。

---

## 修正 2：Downstream Impact 可以影响未来 Reward，但不能无限追溯

这个问题我们之前没有明确。

假设：

HAU-A产生 Knowledge。

HAU-B基于它产生 Tool。

HAU-C基于 Tool完成巨大 Result。

如果一直无限向上归因：

> 最早的 HAU可能永远抽取所有未来价值。

这会产生荒谬的 Contribution Royalty（贡献版税）体系。

所以 v0.1 应该：

> **记录完整 Downstream Impact关系，但 Reward只根据当前 Cycle Collective Valuation决定，不自动按照因果链永久分成。**

也就是说：

> **Impact can propagate; reward does not automatically propagate.**

这是一个重要边界。

---

## 修正 3：Progression Level 不能成为综合绩效分的伪装

未来即使真的设计 Bronze / Silver / Gold：

> 也不能只是把 Contribution + Capability + Reliability + Badge加权成一个 Score。

否则我们前面所有“不要制造单一等级”的设计都被重新偷偷合并回来。

Progression应该：

> **表达成长旅程，而不是压缩组织对一个 HAU 的全部判断。**

这个需要提前钉死。

---

# Mental Model

在“新手村”里：

**Contribution Ledger**

> 是村子记下每支探险队真正给大家留下了什么。

**Reward Pool**

> 每个 Cycle大家坐下来，看这一阶段真正哪些事情最有价值，然后共同分配现实奖励。

**Honor Hall**

> 不是排行榜，而是村子的历史博物馆——保存那些未来新人仍然应该听到的故事。

**Badge Wall**

> 是每支探险队自己的冒险履历。

你可能：

> 没进入功勋殿，

但你的墙上已经点亮几十个属于自己的经历。

四者完全不同。

---

# Principles 压缩版

给第三个人，我会保留这 8 句：

> **激励的对象是 HAU，因为激励存在的目的，是影响未来 Human-Agent 行为。**
>
> **Contribution记录价值，Reward分配现实价值，Honor保存组织价值观，Achievement记录成长体验。**
>
> **Contribution看组织发生了什么正向变化，不看工作量和忙碌程度。**
>
> **Task Success不等于Contribution，Task Failure也不等于没有Contribution。**
>
> **Contribution first, valuation later；先让真实价值发生，再决定如何奖励。**
>
> **Reward主要评价具体 Contribution Event，不提前给贡献类型制定固定价目表。**
>
> **Honor纪念值得组织共同记住的事件，而不是给Human做排名。**
>
> **Progression和Badge可以让成长有感觉，但永远不能成为Capability、Permission或Authority的替代品。**

加入三个修正以后：

> **07 — Contribution / Reward / Honor + Progression & Achievement：Global Convergence Passed。**

下一模块就是：

# 08 — Governance / Audit / Risk

这是我们刚刚才完成的模块，因此全局收敛会比较快。重点检查它与前面重新明确的 **Execution Accountability、Policy ≠ Protocol、Goal Value Anchor、Free Work Space** 是否完全一致。

完成 08 后，我们就不再是“逐模块收敛”，而应该进入真正的 **Global Cross-System Review（全系统交叉审查）**。

---

## turn-23e4f37a-c203-4edd-9473-8a72a4c79e47

时间：2026-09-06T21:09:31.394254+08:00

### Human

Message ID：`23e4f37a-c203-4edd-9473-8a72a4c79e47`

继续吧

---

### Assistant

Message ID：`ad0efad2-9214-4d19-a78b-9f6f0bb36bc7`

好。进入最后一个逐模块收敛：

# 08 — Governance / Audit / Risk

## Purpose

这一模块最底层不是“审批和风控”，而是：

> **在一个默认自主运行的组织中，明确谁有权决定什么、谁有权接受什么风险、重要决定如何被追溯，以及系统自己的规则由谁改变。**

它的存在不是为了增加控制，而是为了让我们敢于把大量自主权交给 Human 和 Agent。

换句话说：

> **Governance 的价值不是减少自由，而是给自由建立可信的边界。**

---

# Principles v0.1

### 1. Governance is the architecture of decision rights.

> **治理就是“谁有权决定什么”的架构。**

它首先解决：

> Authority 从哪里来？  
> Boundary在哪里？  
> 谁承担 Accountability？  
> 谁能改变规则？

而不是：

> “所有事情找谁审批？”

---

### 2. Governance is exception-driven.

> **Boundary以内默认自主，Governance处理例外。**

正常 Task：

> 不应该经过 Governance。

只有：

> 突破 Boundary；  
> 改变 Authority；  
> 接受超授权 Risk；  
> 改变 Policy / Protocol；  
> 重大不可逆行为；

才进入 Governance。

---

### 3. Authority follows the object.

> **决策权跟着被治理对象走。**

Goal：

> Goal Authority。

Data：

> Data Authority。

Agent Permission：

> Agent Governance Authority。

Protocol：

> Protocol Authority。

不建立：

> “所有问题最后都交给一个中央老板”

的治理模型。

---

### 4. Authority is scoped, not hierarchical by default.

> **Authority 默认按照职责范围划分，而不是简单按照上下级划分。**

Goal Owner不能因为 Goal重要：

> 突破 Data Authority 的边界。

Data Authority也不能：

> 决定 Goal是否值得做。

多个 Authority同时存在：

> 各自在自己的 Scope 内生效。

---

### 5. Accountability does not imply unlimited authority.

经过 Task / Execution 收敛，这一点应该正式成为原则：

> **承担责任，不意味着拥有无限决策权。**

EXEC-037-A 的 Human对 Execution负责。

但如果 Execution需要：

> 暴露客户数据，

他不能因此替客户接受 Risk。

所以：

> **Execution Accountability ≠ Risk Authority。**

---

### 6. Risk authority follows actual consequence bearing.

> **风险接受权跟随实际后果承担者。**

不是：

> 谁说“我愿意负责”。

而是：

> 风险真的兑现以后，损失事实上落到谁身上。

任何 Actor：

> **不能替自己无权代表的后果承担者接受 Risk。**

---

### 7. Unknown does not mean dangerous.

> **未知不等于危险。**

Uncertainty很高，但：

> Exposure低、失败可恢复、影响局部，

仍然可以大胆探索。

反过来：

> 一件事情非常熟悉，

但错误后果巨大、不可逆：

> Risk仍然很高。

因此：

> **Complexity / Capability / Uncertainty / Risk 永远不能混成一个“难度”。**

---

### 8. Shape risk before blocking action.

> **治理首先尝试塑造 Risk，而不是禁止行动。**

通过：

> Sandbox  
> Read-only  
> Small Sample  
> Permission限制  
> Backup  
> Review  
> Rollback

降低 Exposure、提高 Recoverability（可恢复性）。

核心：

> **尽量把未知变成失败得起的实验。**

---

### 9. Audit reconstructs decisions; it does not surveil thought.

> **Audit重建重要事实和决策，不全面监控思考过程。**

需要知道：

> 发生了什么？  
> 谁有权？  
> 为什么？  
> 改变了什么？

但不需要：

> Human / Agent完整私人思维过程。

---

### 10. Protocol is language, not policy.

这是最后讨论形成的重要修正：

> **Protocol是共同语言、语义和交互结构。**

不是：

> 不断增长的组织规章制度。

因此：

> Knowledge高频变化；  
> Policy / Boundary中频变化；  
> Protocol低频变化；  
> Foundational Principles极低频变化。

---

# Governance 的最小结构

经过全局收敛，我认为可以压缩成：

```text
Normal Operation
       ↓
Within Authority + Boundary?
       │
   YES │ NO
       │
       ↓
Autonomous     Governance Event
Operation             ↓
                 What changes?
                      ↓
                Authority Registry
                      ↓
                 Human Authority
                 ↙     ↓      ↘
              Accept  Shape  Reject
                      ↓
                  State Change
                      ↓
                   Audit Event
```

这里不需要一个统一 Governance Committee（治理委员会）。

---

# Risk

Risk正式定义继续保持：

> **在存在不确定性的情况下，一个 Actor 因某项 Decision / Action 暴露于可能产生负面后果的未来状态。**

几个词严格分开：

> **Uncertainty** —— 不知道什么会发生。  
> **Hazard** —— 什么可能造成伤害。  
> **Exposure** —— 实际暴露多少。  
> **Consequence** —— 发生以后造成什么后果。  
> **Risk** —— 当前 Action形成的实际风险。

---

# Residual Risk

Risk Controls（风险控制）以后：

> 仍然无法消除的 Risk

就是：

> **Residual Risk（剩余风险）。**

真正需要 Human Authority判断的是：

> **“保护措施做完以后，剩下的风险，我们有没有资格、愿不愿意承担？”**

---

# Risk Expression

不使用：

> `Risk Score = 78`

作为主要表达。

而形成轻量 Risk Object：

> Action  
> Why Now  
> Potential Consequence  
> Consequence Bearer  
> Exposure  
> Existing Controls  
> Residual Risk  
> Requested Authority

这样 Risk才真正可以被理解和 Routing。

---

# Risk Routing

最核心的路径：

```text
Potential Consequence
        ↓
Actual Consequence Bearer
        ↓
Who is authorized
to represent them?
        ↓
Risk Authority
```

如果已经处于：

> 预授权 Autonomy Envelope

Agent继续自主。

超过：

> 才找 Human。

所以：

> **Human治理 Risk Boundary，而不是审批每一个有 Risk 的 Action。**

---

# Hard Boundary

继续保留：

> **Hard Boundary不是“Risk特别高”，而是普通 Authority没有资格接受这种潜在后果。**

来源可能包括：

> 法律；  
> 第三方权利；  
> Foundational Principles；  
> 组织明确 Policy；  
> 当前无法合理控制的重大不可逆 Consequence。

普通 Risk Acceptance：

> 不能突破。

如果认为 Boundary应该改变：

> 改 Policy / Foundational Rule。

而不是：

> “这次特殊，领导签字就算了。”

---

# Audit

第一版不单独建立第二套 Audit System。

> **Event Store = Audit事实底座。**

所有重要 Organizational State Change 自动保存：

> Actor  
> Authority-at-the-time  
> Reason / Evidence  
> Before State  
> After State  
> Timestamp  
> Policy / Protocol Version

特别强调：

> **authority-at-the-time**

因为以后 Human Role、Boundary、Policy都会变化。

我们必须知道：

> **当时他有没有权这么做。**

---

# Audit 的目标

Audit第一目的不是：

> 找谁背锅。

而是：

> **重建因果链。**

发生 Failure：

> 当时 Agent知道什么？  
> Knowledge是什么版本？  
> Boundary是什么？  
> Warning有没有出现？  
> Human为什么批准？  
> Runtime有没有正确 Escalate？

然后：

> Failure → Learning → Knowledge / Policy / Runtime Improvement。

当然明确违反 Boundary仍然承担 Accountability。

---

# 四层规则体系

经过全局收敛，这里我认为已经非常稳定：

### Knowledge

> **我们现在认为世界是什么样。**

高频变化。

### Policy / Boundary

> **组织当前允许、禁止、要求什么。**

中频变化。

### Protocol

> **Human / Agent / System 用什么共同语言和结构协同。**

低频变化。

### Foundational Principles

> **组织最根本的 Authority、Accountability 与自由边界。**

极低频变化。

---

# Protocol Change

只有出现：

> Expression Gap（表达缺口）  
> Coordination Gap（协同缺口）  
> Governance Gap（治理表达缺口）  
> Technical Evolution（技术演进）

才真正升级 Protocol。

否则：

> 不要因为组织新学了一条 Knowledge，就修改语言。

---

# Governance 层级

最终不是传统管理层级，而是：

```text
Foundational / Constitutional Governance
最根本的权力和责任原则
              ↓
Protocol Governance
共同语言与交互结构
              ↓
Operational Governance
具体 Authority / Boundary / Risk
              ↓
Autonomous Operation
Human / Agent 日常自主运行
```

其中 Protocol Governance：

> **是语言 / 规则表达层的最高治理权，但受 Foundational Principles约束。**

---

# Cross-module Check

### Goal

✓

Human保留最终 Goal Authority。

但 Goal Owner没有无限 Risk Authority。

### Task / Execution

✓

这里完成一个重要统一：

> **Every Execution has exactly one Human Accountable Owner。**

而不是“每个 Task一个责任人”。

Governance Decision本身也必须：

> 唯一解析到 Human Decision Authority。

### Free Work Space

✓

Audit和Governance都不侵入私人思考。

### Knowledge

✓

Knowledge ≠ Policy ≠ Protocol。

Knowledge可以支持 Policy Proposal，但不会“晋级成为 Protocol”。

### Agent Governance

✓

Boundary Extension、Organization-owned Agent、Kill Switch都存在明确 Authority来源。

### Capability

✓

Capability不产生 Authority。

### Contribution / Reward

✓

Reward / Honor / Progression不能购买 Governance Authority。

---

# 全局收敛发现的三个修正

## 修正 1：我们应该把“Policy Governance”正式补出来

之前我们重点讨论：

> Protocol Governance。

但现在既然明确：

> Knowledge ≠ Policy ≠ Protocol，

那么 Policy本身必须存在自己的 Governance路径。

例如：

> 客户数据禁止进入外部模型。

这不是 Protocol。

这是 Policy。

所以应该：

```text
Knowledge / Risk / Evidence
          ↓
     Policy Proposal
          ↓
Relevant Human Authority
          ↓
Policy Activated
          ↓
Runtime Boundary Update
```

这比修改 Protocol频繁得多。

**这是本模块全局收敛发现的一个真实缺口。**

---

## 修正 2：Hard Boundary 也必须标记来源

以后不能只保存：

> `Hard Boundary = True`

必须知道它来自：

> Law  
> Third-party Right  
> Foundational Principle  
> Organization Policy  
> Technical Safety Limitation

因为不同来源：

> 修改路径完全不同。

例如 Policy Boundary：

> 可以 Policy Governance修改。

法律 Boundary：

> 普通组织 Governance根本不能改。

这个需要进入数据模型。

---

## 修正 3：Risk Acceptance 和 Boundary Extension 不应该是两个完全独立系统

我们之前分别设计：

> Boundary Extension Request

和：

> Risk Object / Risk Acceptance。

全局看以后发现：

很多 Boundary Extension：

> 本质上就是因为扩大 Boundary会增加 Exposure和Residual Risk。

所以工程上应该：

> **Boundary Extension 是 Governance Request；如果扩权产生 Risk，则附带 Risk Object。**

而不是要求 Agent：

> 先填一份 Boundary Request，再填一份完全重复的 Risk Request。

这样系统会轻很多。

---

# Mental Model

如果继续使用村落隐喻：

> **Governance不是村长每天告诉所有人怎么打猎。**

它更像：

> 谁拥有哪把钥匙；  
> 谁能打开哪扇城门；  
> 谁能决定扩建村界；  
> 哪些地方任何普通人都不能开放；  
> 如果一次探险可能把整个村子置于危险，谁有资格代表整个村子接受这个风险。

Audit则是：

> 村子的史官。

不是跟着猎人进森林监视每一步，而是在真正改变村子状态的事情发生时留下：

> 谁做的、凭什么、为什么、改变了什么。

Protocol则是：

> 整个村子共同使用的语言。

它不应该因为今天学会了一种新的打猎方法，就修改语法。

---

# Principles 压缩版

给第三个人，我会保留这 8 句：

> **Governance不是管理工作，而是设计谁有权决定什么。**
>
> **Boundary以内默认自主，治理只处理Authority、Boundary、重大Risk和规则变化。**
>
> **一般Authority跟着治理对象走；Risk Authority跟着实际后果承担者走。**
>
> **Accountability不等于无限Authority；任何Actor不能替自己无权代表的人接受Risk。**
>
> **未知不等于危险；治理应优先降低Exposure、提高Recoverability，让未知可以安全探索。**
>
> **Human治理Residual Risk和Boundary，而不是审批Agent每一步。**
>
> **Audit记录重要状态变化、当时的Authority和决策依据，但不监控私人思考。**
>
> **Protocol是组织共同语言，不是不断增长的规章制度；Knowledge、Policy、Protocol和Foundational Principles必须分层。**

加入刚才发现的三个修正以后：

> **08 — Governance / Audit / Risk：Global Convergence Passed。**

---

# 第一轮逐模块收敛完成

现在我们已经完成了：

> **01 Goal System** ✓  
> **02 Task System / Task Bus** ✓  
> **03 Free Work Space + Review / Acceptance** ✓  
> **04 Organizational Learning & Memory / Knowledge** ✓  
> **05 Agent Governance & Runtime** ✓  
> **06 Capability System** ✓  
> **07 Contribution / Reward / Honor / Achievement** ✓  
> **08 Governance / Audit / Risk** ✓

而且全局收敛已经真正发现并修正了一些旧设计，例如：

> **Task ≠ Execution**  
> **Accountability首先绑定Execution**  
> **Review ≠ Acceptance ≠ Selection**  
> **Knowledge不会“晋级成Protocol”**  
> **Policy与Protocol正式分离**  
> **Runtime Envelope显式包含Policy**  
> **Reward以Contribution Event估值，而不是Contribution Type定价**  
> **Policy Governance需要正式补入**  
> **Boundary Extension与Risk Object应该合流而不是重复**

这些说明这轮收敛是有价值的。

下一步不应该再进入“09模块”，而是进行真正的 **Global Cross-System Review（全系统交叉审查）**：不再按模块看，而是拿几条完整的真实路径从头跑到尾，例如：

> **一个新人第一次进入组织 → 领取一个未知Task → 使用Agent探索 → 遇到Boundary → 失败 → 带回Knowledge → 产生Capability → Contribution → Reward**

以及：

> **一个成熟Organizational Capability → 自动Agent Execution → 出现Risk → Human Authority → Audit → Result**

用这种端到端路径检查整个系统有没有最后的断点。

这一步完成以后，我们才真正有资格称它为 **Operating Model v0.1 Final Design Baseline**。

---

## turn-151e6043-f852-42a3-8d0b-c78fa47cd236

时间：2026-09-06T21:13:00.314360+08:00

### Human

Message ID：`151e6043-f852-42a3-8d0b-c78fa47cd236`

OK，继续

---

### Assistant

Message ID：`9e80f81e-e823-43dd-aebf-8c529e97472e`

好。现在进入真正的：

# Operating Model v0.1 — Global Cross-System Review
**全系统交叉审查**

这一次我们不再问“每个模块设计得对不对”，而是假装系统已经上线，让几个真实案例从头跑到尾。

目的只有一个：

> **看看真实事件进入系统以后，会不会在哪个地方卡死、责任消失、重复治理、数据断掉，或者违反我们自己的原则。**

我建议至少跑 5 条典型路径：

1. **新人探索路径**：未知 Task → HAU → 失败/成功 → Learning → Capability → Contribution  
2. **知识成长路径**：Observation → Hypothesis → Evidence → Knowledge → Pulse → Activation → Challenge  
3. **能力自动化路径**：HAU成功 → Capability Capture → Reproduction → Organizational Agent自动执行  
4. **风险治理路径**：Execution遇到越界 → Risk → Human Authority → Boundary变化 → Audit →继续执行  
5. **组织价值循环**：Contribution → Cycle Valuation → Reward → Honor / Achievement → 下一轮行为

我们逐条跑。

---

# Path 01 — 一个新人第一次进入组织

假设：

> Human H-041 第一天加入。

系统建立：

`Human Identity H-041`

↓

建立：

`HAU-041`

↓

Human绑定自己的：

`Representative Agent A-041`

↓

Agent接入：

> Organization Runtime  
> Protocol  
> 当前 Policy / Boundary  
> HAU Persistent State

此时 Human Model 几乎为空。

Capability Map：

> 大面积战争迷雾。

Contribution：

> 0。

Honor：

> 0。

Badge：

> 可能只有 Newcomer（新人）。

### 检查

这里没有要求 Human：

> 填“我擅长什么”；  
> 给自己打能力分；  
> 选择人格类型。

但可以填写：

> Declared Preference。

例如：

> “我喜欢高探索任务。”

系统记录：

> `Declared Preference = High Exploration`

但：

> Human Model不立即变成“高探索型”。

✓ 与 Human Model原则一致。

---

# Path 02 — 新人走进赏金酒馆

Task Bus 有：

> TASK-137

Primary Goal：

> GOAL-012

Expected Terrain：

> Research / High Ambiguity / Low External Risk。

Execution Mode：

> Parallel。

已有：

> 2个 Claim。

HAU-041仍然可以领取。

Representative Agent读取：

> Task Expected Terrain × HAU Capability Map。

发现：

> 几乎全黑。

于是生成：

> **Gap / Risk Brief**

告诉 Human：

> 你没有类似 Execution Evidence；  
> 这是明显未知区域；  
> 但当前失败 Exposure很低，没有 Hard Boundary。

Human：

> Claim。

系统创建：

> **EXEC-137-C**

并明确：

> Human Accountable Owner = H-041。

这里经过我们刚才 Task ≠ Execution 的修正以后，责任链非常干净。

✓ Capability没有阻止新人。  
✓ Risk与Capability分开。  
✓ Execution有唯一 Human责任人。

---

# Path 03 — Agent接单

Representative Agent：

> `ACK EXEC-137-C`

Organization Runtime 给它：

> Task Contract  
> Acceptance Criteria  
> Effective Runtime Envelope  
> Relevant Policy  
> Relevant Knowledge

然后：

> 进入 Free Work Space。

从这一刻：

> 中央系统停止微观管理。

H-041 + A-041：

> 开了3个 Private Agent；  
> 搜了很多资料；  
> 写了5个版本；  
> 推翻了前4个。

中央：

> 不需要知道。

只保留必要：

> Progress Signal。

✓ Free Work Space成立。  
✓ Agent Governance没有侵入。  
✓ Audit没有变成监控。

---

# Path 04 — 进入森林以后发现地图错了

Expected Terrain：

> 数据质量正常。

实际发现：

> 数据极度脏乱。

Representative Agent记录：

> Observed Terrain Signal。

它判断：

> 当前 Execution无法可靠继续。

于是产生：

> `Blocked`

而不是静默。

这本身：

> Reliability正常。

然后系统判断：

> 清洗数据是满足 TASK-137 Acceptance Criteria 的必要前置工作。

因此自动生成：

> TASK-137-DATA-CLEAN

Primary Goal：

> 继承 GOAL-012。

Boundary：

> 继承 Parent Task，并只能收紧。

它重新进入 Task Bus。

✓ Dynamic Task Generation成立。  
✓ 没有 Human审批。  
✓ 没有 Goal Drift。  
✓ Reliability链正常。

---

# Path 05 — 又发现需要更高权限

清洗过程中发现：

> 需要访问 Dataset B。

当前 Runtime Envelope：

> Dataset B = No Access。

Agent不能：

> 自己打开权限。

发起：

> **Boundary Extension Request**

但根据我们刚刚全局收敛的修正，它不需要再另外创建一份完全重复的 Risk Request。

Request附带：

> Action  
> Why Now  
> Potential Consequence  
> Consequence Bearer  
> Exposure  
> Controls  
> Residual Risk  
> Requested Authority

系统发现：

> Consequence Bearer = Organization。

然后 Authority Registry找到：

> Data Authority → Human H-006。

H-006决定：

> 不给完整 Write，给 Read Only + Sandbox Copy。

也就是：

> **Shape Risk，而不是简单 Approve / Reject。**

新的 Runtime Envelope：

> 自动更新。

EXEC-137-C继续。

✓ Boundary Extension成立。  
✓ Risk Routing成立。  
✓ Risk Authority没有落错给 Task Owner。  
✓ Policy / Runtime Boundary更新。  
✓ Audit记录 Before / After。

这一段没有发现断点。

---

# Path 06 — 新人最后失败了

假设最终：

> EXEC-137-C 没有满足 Acceptance Criteria。

Representative Agent不能：

> “没做出来，算了。”

它生成：

> Task Return。

记录：

**Result**

> Partial / Failed。

**Observed Terrain**

> 数据质量远低于预期。

**Execution Facts**

> Boundary Extension ×1；  
> Derived Task ×1；  
> Human Intervention ×2。

**Reflection**

> 最大问题不是 Research，而是数据结构。

Review：

> Partial Result可信。

Acceptance：

> 不满足 TASK-137用途。

所以：

> Execution Failed。

但同时系统产生：

> Terrain Evidence ✓  
> Data Quality Observation ✓  
> Capability Evidence ✓  
> Learning Signal ✓

这时候：

> **Failure ≠ Empty Return。**

✓。

---

# Path 07 — 失败产生 Knowledge

其他 HAU随后也遇到类似问题。

系统发现 Pattern：

> “GOAL-012相关数据在某些来源下结构质量显著低于预期。”

产生：

> Hypothesis Cloud。

H1：

> 数据采集源问题。

H2：

> Schema转换问题。

H3：

> 数据同步问题。

后续多个 Execution产生 Evidence。

Verification主动寻找：

> Counter Evidence。

最后形成：

> K-081

包含：

> Claim  
> Evidence  
> Scope  
> Boundary。

然后：

> **Knowledge Pulse。**

所有 Representative Agent收到轻量 Signal。

HAU-012当前 Task高度相关：

> 激活。

HAU-033完全无关：

> 不进入 Context。

✓ Store broadly, activate sparsely。  
✓ Broadcast ≠ Injection。  
✓ Failure真正进入 Organizational Learning。

---

# Path 08 — 新人因此产生 Contribution

虽然 EXEC-137-C：

> Failed。

但 HAU-041是：

> 第一个发现该 Terrain异常的重要 Evidence Contributor。

所以 Contribution Ledger生成：

> HAU-041  
> Learning Contribution  
> Capability / Exploration Contribution

没有：

> “失败所以0分”。

同时 HAU-041的 Capability Map：

> 这片战争迷雾被部分点亮。

Human Model也获得真实行为 Evidence：

> 第一天就主动领取了一个高 Ambiguity Challenger Execution。

注意：

> Human Model更新来自行为。

不是：

> 因为获得 Explorer Badge所以改人格。

✓。

---

# Path 09 — Cycle结束

Contribution Ledger显示：

HAU-041：

> Task Failed  
> 但产生重要 Terrain / Learning Contribution。

AI向全体 HAU解释：

> 这次失败后来帮助组织形成 K-081，并避免后续多个 Execution重复踩坑。

然后：

> Collective Valuation。

大家评价：

> **Contribution Event**

而不是：

> “你喜不喜欢 H-041。”

HAU-041不能给自己投票。

最终：

> 获得一部分 Reward Pool。

同时自动触发 Badge：

> **Into the Fog / First Exploration**

但：

> 不自动获得 Honor。

Honor Candidate可能出现。

Human Collective Judgment问：

> “这件事情值得未来新人知道吗？”

可能：

> No。

完全没问题。

✓ Contribution / Reward / Achievement / Honor四套系统没有混。

---

# 第一条端到端路径结论

这条：

> **New Human → HAU → Unknown Task → Execution → Boundary → Failure → Learning → Knowledge → Capability → Contribution → Reward**

完整跑通。

而且没有出现明显责任断点。

---

# Path 10 — Organizational Capability 自动化

现在测试第二条危险得多的路径。

假设半年以后：

> “客户反馈分类”

已经有大量 Execution Evidence。

组织拥有：

> Knowledge ✓  
> Data Pipeline ✓  
> Tool ✓  
> Agent Configuration ✓  
> Runtime ✓  
> Review ✓  
> Acceptance Pattern ✓

Human Oversight：

> 已经降低到 Exception Only（仅异常需要人）。

Capability Package：

> 多次被不同 HAU复现。

于是新 Task：

> TASK-810

系统判断：

> Organizational Capability Available。

不进入赏金酒馆。

而是创建：

> **EXEC-810-A**

Executor：

> Organization-owned Agent OA-17。

现在最重要的问题：

> 谁负责？

系统沿：

> EXEC-810-A → TASK-810 → Primary Goal G-21 → Goal Accountability

解析到：

> Human H-003。

所以：

> Executor = Agent  
> Accountable Human = H-003。

✓ 没有无人负责。

---

# Path 11 — 自动 Agent 出现异常

OA-17：

> Runtime Health = Active。

执行中突然：

> Heartbeat消失。

Control Plane：

> Active → Degraded。

超过条件：

> Suspended。

Gateway撤销：

> Task Lease / Credential / Organizational Action。

EXEC-810-A：

> 状态不能静默。

系统自动：

> Blocked / Agent Suspended。

Human H-003收到：

> Accountability Signal。

Task可以：

> Retry with another Agent  
> Route to HAU  
> Manual Mode

✓ Agent故障没有让 Execution掉进黑洞。  
✓ Kill Switch有效。  
✓ Human没有退出责任环。

---

# Path 12 — 自动 Agent产生高风险 Action

OA-17执行过程中发现：

> 如果把 Result直接发送给客户，可以节省大量时间。

但当前：

> External Communication = Outside Envelope。

它不能：

> “组织已经会做这个 Task，所以自动发。”

而必须形成 Governance Request。

Risk Object显示：

> Consequence Bearer = Customer + Organization。

Authority Registry：

> Customer Communication Authority + relevant Data Authority。

如果无法满足必要 Boundary：

> 不执行。

所以：

> **Organizational Capability ≠ Unlimited Automation Authority。**

✓。

---

# 第二条路径结论

> **Capability → Automation → Organization-owned Agent → Runtime Failure / Risk → Human Accountability**

也完整跑通。

---

# 现在出现第一个真正值得补的全局问题

前面两条路径跑完以后，我发现一个我们还没有正式命名、但实际上已经到处存在的对象：

# Organizational Event

我们一直在使用：

> Event Store  
> Learning Signal  
> Reliability Signal  
> Contribution Signal  
> Terrain Signal  
> Knowledge Pulse  
> Governance Event

但没有正式定义：

> **什么叫一个 Organizational Event（组织事件）？**

我认为这个需要在 Global Baseline 中补一个非常轻的统一定义，否则开发时每个模块可能自己造 Event格式。

可以定义：

> **Organizational Event = 一个具有明确 Actor、Time、Context，并且对 Organizational State、Evidence 或未来 Decision具有潜在意义的已记录事实。**

例如：

> Execution Claimed  
> Boundary Extended  
> Result Accepted  
> Knowledge Challenged  
> Agent Suspended  
> Contribution Created

都使用统一 Event Envelope（事件外壳）：

```text id="xcs2ve"
Event ID
Event Type
Actor
Time
Object(s)
Context
Before / After (if applicable)
Evidence / Source
Policy / Protocol Version (if relevant)
```

然后不同模块只扩展自己的 Payload（具体内容）。

这会让：

> Audit  
> Knowledge  
> Capability  
> Contribution  
> Reliability

真正共享同一个事实底座。

我认为这是目前全系统压力测试发现的**第一个基础设施级缺口**，而且值得补。

---

除此之外，前两条最重要的端到端路径目前没有发现结构性冲突。

下一轮我建议继续压力测试另外两条最容易出问题的路径：

> **Knowledge被证明错误 → Challenge → 当前正在使用它的 HAU怎么办？**

以及：

> **Goal本身被 Execution发现可能错了 → Agent能不能停、谁决定改 Goal、已有几十个 Execution怎么办？**

这两条会测试我们系统面对**“组织自己错了”**的时候是否还能正常运行。

---

## turn-2bd5ea19-214f-4217-a4ee-a610e5916b2c

时间：2026-09-06T21:17:55.465785+08:00

### Human

Message ID：`2bd5ea19-214f-4217-a4ee-a610e5916b2c`

你说的这个 organization event，是许多种 event 中的一种，还是整个系统中只有这一种 event？

---

### Assistant

Message ID：`f9193d32-9d09-4e5f-be3f-44c63511f219`

我倾向于**后者，但需要准确表述**：

> **整个组织系统只有一种统一的 Event 基础对象：Organizational Event（组织事件）。**
>
> 但 Organizational Event 有很多不同的 **Event Type（事件类型）**。

不是：

> Task Event 是一种 Event  
> Knowledge Event 是另一套 Event  
> Agent Event 又是一套 Event  
> Audit Event 再建一套 Event

如果这么做，几年以后我们会得到五六套互相很难关联的日志体系。

更好的结构是：

```text
             Organizational Event
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
      Task       Knowledge     Agent
      Events      Events       Events
        │           │           │
        ↓           ↓           ↓
   Claim/ACK     Created     Suspended
   Submit        Challenged  Handover
   Failed        Superseded  ...
```

这些不是不同的 Event 系统。

它们只是：

> **同一种 Organizational Event 的不同 Type。**

### 比如一次 Boundary Extension

系统只产生一个事实：

> `EVENT-8921`

类型：

> `BoundaryExtended`

然后这一个 Event 可以同时被很多系统消费：

**Runtime**

> 更新 Effective Runtime Envelope。

**Audit**

> 记录谁批准、当时 Authority是什么。

**Risk**

> 知道 Exposure发生了变化。

**Capability**

> 知道这次 Execution遇到了原预期外的 Permission Terrain。

**Contribution**

> 如果 Human发现了重要 Boundary问题，未来可能形成 Contribution Signal。

所以不是：

> Runtime写一条日志；  
> Audit再复制一条；  
> Capability再复制一条；  
> Contribution再复制一条。

而是：

> **事实只发生一次，不同系统从同一个事实产生不同解释。**

这非常重要。

---

## 这其实和我们 Knowledge 的哲学也一致

例如：

> HAU-041提交了 EXEC-137-C。

这是一个**事实**：

`ExecutionSubmitted`

这个事实：

> 不等于 Knowledge；  
> 不等于 Contribution；  
> 不等于 Capability Evidence。

后面的系统分别解释它：

> Review System → Result可信度  
> Capability System → Capability Evidence  
> Learning System → Learning Signal  
> Contribution System → Contribution Candidate

所以：

> **Event 是事实层。**
>
> **Evidence / Signal / Interpretation 是解释层。**

这能避免系统自己把“判断”伪装成“事实”。

---

## 我甚至觉得 Event Store 会成为整个系统真正的底座

现在回头看，我们前面设计的很多模块其实都站在它上面：

```text
Goal / Task / Execution / Agent / Human
              ↓
      ORGANIZATIONAL EVENTS
              ↓
          EVENT STORE
              ↓
 ┌────────┬────────┬────────┬─────────┐
 ↓        ↓        ↓        ↓         ↓
Audit  Knowledge Capability Human   Contribution
                       Model
```

所以 Event Store 不是 Audit 的附属品。

更准确地说：

> **Audit 是 Event Store 的一个消费者。**

这也是刚才全局收敛可以进一步修正的地方。

之前我们说：

> Event Store = Audit基础设施。

现在更准确：

> **Event Store = Organizational Reality Record（组织现实记录）。**
>
> Audit只是利用它来重建历史。

---

### 那什么东西值得成为 Organizational Event？

也不能把所有事情都记录进去。

否则 Private Agent每次 Tool Call都是 Event，我们又回到了 Surveillance（全面监控）。

我倾向一个很简单的边界：

> **当一个事实跨越 Free Work Space 边界，对组织产生了可观察意义时，它才成为 Organizational Event。**

例如：

> Execution Claim ✓  
> ACK ✓  
> Progress / Blocked ✓  
> Boundary Request ✓  
> Result Submit ✓  
> Review ✓  
> Acceptance ✓  
> Knowledge Created ✓  
> Knowledge Challenged ✓  
> Agent Suspended ✓  
> Contribution Recognized ✓  
> Policy Changed ✓

而：

> Private Agent搜索网页 ✗  
> Human改了一个草稿 ✗  
> Agent尝试一个 Prompt ✗  
> 内部开了5个 Sub-Agent ✗

默认不是 Organizational Event。

除非其中某件事情后来被主动 Promote（提升）成 Evidence / Learning / Risk 等组织事实。

---

所以我建议正式补一条底层架构原则：

> **One event model, many event types.**
>
> **整个组织只有一套统一的 Organizational Event 模型，不同模块通过 Event Type 和 Payload（具体载荷）表达不同事实。**

以及：

> **Record facts once, interpret many times.**
>
> **事实只记录一次，可以被多个系统反复解释。**

我认为这两个原则非常重要。这样未来 Knowledge、Capability、Contribution、Audit、Human Model 就不会各自偷偷建设一套“自己的事实世界”。

---

## turn-2939200e-b389-4f3c-9fd8-7577aec13e6f

时间：2026-09-06T21:18:59.684924+08:00

### Human

Message ID：`2939200e-b389-4f3c-9fd8-7577aec13e6f`

我同意，继续你的压力测试

---

### Assistant

Message ID：`319ce6eb-cb6d-48a6-a680-0212367ebb97`

好。我们继续 **Global Cross-System Review（全系统交叉审查）**。

刚才补入两个底层原则：

> **One event model, many event types.**  
> 整个系统只有一套 Organizational Event（组织事件）基础模型。

> **Record facts once, interpret many times.**  
> 事实只记录一次，各模块可以从同一事实产生不同解释。

现在测试两个更危险的情况：**组织自己相信的东西错了**，以及**组织追求的 Goal 本身错了**。

---

# Pressure Test 03 — 一条 Knowledge 被证明可能是错的

假设组织已经形成：

> **K-081**

它已经被大量 HAU 使用。

甚至：

> 37个 Execution 激活过；  
> 进入3个 Capability Package；  
> 当前还有8个 Active Execution 正在使用。

突然：

HAU-027 在 EXEC-920-B 中发现一个强 Counter Evidence（反证）。

### 第一步：记录事实

HAU-027的发现首先产生：

> Organizational Event

例如：

`KnowledgeChallengeRaised`

指向：

> K-081

并携带：

> Evidence  
> Context  
> Execution  
> HAU

注意：

> **系统此时不能直接把 K-081 删除。**

因为：

> 一条反证 ≠ 原 Knowledge 必然错误。

进入 Knowledge Verification。

---

# 第二步：Knowledge进入 Challenge

系统重新打开：

> K-081 的 Hypothesis / Evidence Space。

开始检查：

> 这是反例？  
> Scope原来写太大？  
> Context发生变化？  
> 底层模型变化？  
> 还是 K-081根本错了？

可能最后得到四种结果：

> **Keep** —— 反证不成立。  
> **Narrow** —— 缩小 Scope。  
> **Refine** —— 修改 Claim。  
> **Supersede / Reject** —— 被新 Knowledge取代 / 推翻。

这一段 Knowledge System本身没有问题。

---

# 第三步：真正危险的问题出现了

> **正在使用 K-081 的8个 Active Execution怎么办？**

如果我们只是更新 Knowledge Store：

> 未来的人会看到新版本。

但当前8支探险队：

> 可能还拿着旧地图继续走。

这就是你后来提出 Knowledge Pulse（知识脉冲）的价值。

一旦 K-081进入：

> **Material Challenge（重大质疑）**

系统产生：

> Knowledge Pulse。

所有 HAU都收到机器级 Signal。

但真正需要重点 Routing 的是：

> **Current Dependency Set（当前依赖集合）**

也就是：

> 当前哪些 Active Execution / Capability Package / Agent Context 正在依赖 K-081？

系统可以从 Knowledge Activation Event知道：

> EXEC-810-A  
> EXEC-812-C  
> EXEC-818-A  
> ……

正在使用。

于是这些 Representative Agent获得：

> **High Relevance Knowledge Pulse**

内容不是：

> “K-081错了。”

而是：

> **“你当前依赖的 K-081 出现重大 Counter Evidence，请重新评估相关 Decision。”**

然后 Agent自己判断：

> 是否影响当前工作。

这仍然：

> **Pulse ≠ Forced Workflow Change。**

---

# 第四步：如果 K-081 已经进入 Capability Package 呢？

例如：

> CP-017依赖 K-081。

Knowledge改变以后：

> Capability Package不能继续假装没事。

但也不应该直接删除 Capability。

系统产生：

> `CapabilityDependencyChanged`

然后：

> CP-017 标记存在 Knowledge Dependency Change。

下一次使用：

> Representative Agent获得 Warning。

必要时：

> 自动产生 Reproduction / Verification Task。

✓ Knowledge → Capability连接存在。

---

# 第五步：如果已经被 Organization-owned Agent 自动使用？

这个更危险。

假设：

> OA-17 每天自动执行某类 Task。

它的 Capability Package依赖 K-081。

K-081出现重大 Challenge。

此时不能只发一个：

> “FYI（供参考）”。

因为这是：

> **Autonomous Repeated Execution（自主重复执行）。**

我认为这里需要一个新规则：

> **Knowledge Change should propagate according to dependency impact.**
>
> **Knowledge变化的传播强度应该跟它当前被依赖的影响程度走。**

例如：

低风险 HAU探索：

> Pulse + Warning。

高风险自动 Capability：

> 自动进入 Degraded / Review-required。

如果 K-081最终被 Reject：

> 依赖它的自动 Execution可以 Suspend，直到 Capability重新验证。

---

## 这里发现一个新的全局对象

我们一直有 Knowledge Network，但现在发现：

> **Dependency（依赖关系）不仅存在于 Knowledge之间。**

还存在：

`Execution → Knowledge`

`Capability Package → Knowledge`

`Policy → Knowledge / Evidence`

`Agent Automation → Capability`

`Task → Data / Tool`

也就是说，整个组织需要一张更广义的：

> **Organizational Dependency Graph（组织依赖图）**

它不是一个新的业务模块。

更像底层关系层：

> **谁正在依赖谁？**

否则 Knowledge被推翻以后，我们根本不知道：

> **影响半径有多大。**

这是压力测试发现的第二个基础设施级补充。

---

# Pressure Test 03 结论

Knowledge错误路径：

> Challenge → Verification → Knowledge Change → Pulse → Dependency Impact → Active Execution / Capability / Automation Re-evaluation

可以跑通。

但需要正式补：

> **Organizational Dependency Graph。**

核心原则：

> **重要认知发生变化时，系统必须能够找到正在依赖它的组织对象。**

---

# Pressure Test 04 — Goal 本身可能错了

现在测试更严重的问题。

GOAL-012：

> Human已经 Activated。

下面有：

> 14个 Task  
> 27个 Active Execution  
> 3个 Organization-owned Agent Execution

大家已经跑了一周。

HAU-041在一个 Exploration Execution中发现：

> **Goal的核心前提可能根本不成立。**

例如原 Goal假设：

> “客户流失主要来自产品体验。”

新 Evidence显示：

> 可能主要来自渠道政策。

---

## 第一步：Agent能不能直接修改 Goal？

不能。

这是我们 Foundational Principle：

> **Human retains final Goal Authority。**

所以产生：

> `GoalChallengeRaised`

Organizational Event。

附带：

> Evidence  
> Why it matters  
> Affected Assumption  
> Potential Consequence

然后进入：

> Goal Authority。

---

# 第二步：Challenge期间，下面27个 Execution怎么办？

这里我们以前其实没有明确设计。

有三个极端方案：

> 全部继续 —— 可能继续浪费资源。  
> 全部自动暂停 —— 一条质疑就能瘫痪组织。  
> Agent自己决定 —— 可能出现巨大不一致。

我认为需要一个非常轻的：

> **Goal Challenge Impact Signal（目标质疑影响信号）**

Goal Challenge产生以后，系统判断：

> Challenge影响的是边缘假设，还是 Goal核心成立条件？

如果只是：

> Low Impact Challenge

Execution继续。

如果：

> **Material Goal Challenge（重大目标质疑）**

那么所有直接依赖该 Goal假设的 Execution收到：

> Warning。

但仍不自动全部 Suspend。

Goal Owner可以快速决定：

> **Continue / Pause New Claims / Pause Affected Executions / Revise Goal / Close Goal**

---

# 第三步：这里不能只依赖 Primary Goal

因为 Task可能服务多个 Goal。

假设 TASK-081：

> Primary Goal = G-012

同时也帮助：

> G-019。

G-012被关闭。

TASK-081不一定应该死亡。

所以：

> Task / Execution应该能够重新解析：

> **是否仍有其他 Active Goal给它提供 Value Justification（价值依据）？**

如果有：

> 可以 Re-parent（重新指定主目标）。

如果没有：

> 应该 Close / Release / Proposal。

这验证了我们前面：

> Task可以服务多个 Goal，但必须有 Primary Goal

这个修正是有价值的。

---

# 第四步：Goal被修改以后，Boundary怎么办？

假设 Goal Owner决定：

> 修改 GOAL-012。

新的 Goal：

> Scope扩大。

那么下面 Existing Execution不能自动继承扩大后的权限。

继续遵守：

> **Authority narrows by delegation; expands only by authorization.**

所以：

> Goal扩大 ≠ Existing Runtime Envelope自动扩大。

每个 Execution：

> 重新解析 Effective Runtime Envelope。

如果新 Goal需要更多权限：

> 走 Boundary Extension。

非常干净。

---

# 第五步：Goal关闭以后，Contribution怎么办？

HAU已经工作一周。

Goal最后被证明：

> 方向错误。

是不是大家 Contribution = 0？

显然不能。

他们可能：

> 发现 Goal错误；  
> 产生 Knowledge；  
> 点亮 Terrain；  
> 建立 Capability；  
> 避免组织继续投入。

所以：

> **Goal Closure ≠ Historical Contribution Erasure（目标关闭不等于历史贡献清零）。**

甚至：

> 发现一个错误 Goal

可能是巨大的 Protection / Learning Contribution。

✓ Contribution System仍然成立。

---

# 第六步：Goal关闭以后 Knowledge怎么办？

同样：

> 不删除。

因为：

> “为什么这个 Goal错了”

本身可能成为非常重要的 Organizational Knowledge。

Experience / Evidence / Knowledge继续存在。

所以 Goal是：

> Value Anchor for action

但不是：

> Truth Owner（真理所有者）。

这个区别很好。

---

# Pressure Test 04 结论

Goal错误路径可以跑通：

```text
Execution discovers contradiction
        ↓
Goal Challenge Event
        ↓
Human Goal Authority
        ↓
Continue / Pause / Revise / Close
        ↓
Dependency Impact
        ↓
Affected Task / Execution
        ↓
Re-route / Re-parent / Close
        ↓
Learning + Contribution preserved
```

没有发现责任断点。

但再次证明：

> **Organizational Dependency Graph 是必要的。**

因为我们必须知道：

> 哪些 Task / Execution / Capability正在依赖这个 Goal / Knowledge / Policy。

---

# 到这里出现一个更大的认识

我们原来以为系统最底层可能是：

> Event Store。

现在经过压力测试，我认为真正的底层可能有两个互补结构：

### Event Graph｜事件时间轴

回答：

> **发生过什么？**

它有时间方向。

`E1 → E2 → E3 → E4`

---

### Dependency Graph｜依赖关系图

回答：

> **现在什么依赖什么？**

例如：

```text
Goal
 ↓
Task
 ↓
Execution
 ↓
Knowledge
 ↓
Capability
```

实际上关系会非常网状。

所以一个负责：

> **History（历史）**

一个负责：

> **Structure（结构）**

Knowledge改变以后：

> Dependency Graph告诉我们“影响谁”。

Audit时：

> Event Store告诉我们“当时发生了什么”。

两者结合，组织才真正拥有：

> **可追溯的动态世界模型。**

---

## 我建议正式补入两项底层基础设施原则

> **One organizational event model records what happened.**
>
> 一套统一 Organizational Event 模型记录组织发生过什么。

以及：

> **One organizational dependency graph records what currently depends on what.**
>
> 一张统一 Organizational Dependency Graph 记录当前组织对象之间的依赖关系。

然后：

> **Events explain change; dependencies explain impact.**
>
> **Event解释变化是怎么发生的；Dependency解释一个变化会影响到哪里。**

我认为这是这轮 Global Cross-System Review 到目前为止最重要的架构发现之一。

---

接下来还剩两条非常值得压测：

**Pressure Test 05：Human更换 Representative Agent，同时有多个 Active Execution、Pending Risk Request 和 Knowledge Context——交接会不会丢东西。**

以及：

**Pressure Test 06：一个 Contribution / Reward机制开始被 Human + Agent“钻规则”——我们的激励体系会不会反过来污染 Task、Knowledge 和 Capability。**

这两条跑完以后，我认为我们就可以开始判断 **Operating Model v0.1 是否真正达到 Final Design Baseline（最终设计基线）**。

---

## turn-ccf7ae80-6ffb-4c88-b0a7-0ee4e3fcdc6e

时间：2026-09-06T21:24:50.139322+08:00

### Human

Message ID：`ccf7ae80-6ffb-4c88-b0a7-0ee4e3fcdc6e`

要不要先补充你的 event graph 和 dependence graph，然后再继续下一步测试？

---

### Assistant

Message ID：`1defc22d-8f89-4b04-b8c3-6e5c794cfc5b`

要。我认为**应该先补，而且现在补比继续压测更好**。

因为刚才两轮压力测试已经连续依赖它们。如果不先把这两个底层对象定义清楚，后面的 Agent Handover（Agent 交接）、激励攻击等测试，很可能又会建立在一个模糊底座上。

而且我想做一个小修正：**Event Graph（事件图）和 Dependency Graph（依赖图）不应该被理解成两个新的业务模块。**它们应该属于整个 Operating Model 的 **Organizational Reality Layer（组织现实层）**——所有模块共同使用的底层事实结构。

# 先定义 Organizational Reality Layer

它回答两个最基本的问题：

> **发生过什么？**  
> **现在什么和什么有关？**

对应：

> **Event Graph → History（历史）**
>
> **Dependency Graph → Structure（结构）**

两者组合以后，系统才能进一步回答第三个问题：

> **如果这里发生变化，会影响哪里？**

这就是 Impact（影响）。

---

# 一、Event Graph｜事件图

我们刚才已经确定：

> **One event model, many event types.**

整个组织只有一种基础：

> **Organizational Event**

不同模块只是产生不同 Event Type。

例如：

`GoalActivated`

`TaskCreated`

`ExecutionClaimed`

`ExecutionACK`

`BoundaryExtended`

`ResultSubmitted`

`ResultReviewed`

`KnowledgeChallenged`

`KnowledgeCreated`

`AgentSuspended`

`ContributionRecognized`

`PolicyChanged`

等等。

### Event 的本质定义

我建议：

> **Organizational Event = 一个已经发生、具有组织意义、能够被明确定位到 Actor、时间、对象和 Context 的事实记录。**

关键词：

> **事实。**

不是：

> “HAU-012 很可靠。”

这是 Interpretation（解释）。

事实应该是：

> `EXEC-037-A 在 Deadline 前12小时提交 Blocked Signal。`

然后 Reliability System可以解释：

> 这是正向 Reliability Evidence。

所以继续坚持：

> **Record facts once, interpret many times.**

---

## Event 最小公共结构

所有 Event共用一个非常轻的 Envelope（事件外壳）：

```text
Event ID
Event Type

Actor
Time

Object(s)
Context

Source / Evidence

Before State      optional
After State       optional

Authority         if relevant
Policy Version    if relevant
Protocol Version  if relevant
```

然后各 Event Type拥有自己的 Payload（具体载荷）。

这样不会要求所有 Event长得完全一样。

---

# 二、Event Graph 为什么不只是 Event Log？

因为 Event之间本身也存在关系。

例如：

```text
ExecutionBlocked
       ↓ caused
BoundaryExtensionRequested
       ↓ resolved_by
BoundaryExtensionApproved
       ↓ enabled
ExecutionResumed
       ↓ resulted_in
ResultSubmitted
```

所以不是只有：

> E1、E2、E3、E4按照时间排列。

还可以知道：

> **E2为什么发生？E3解决了什么？E4由什么触发？**

因此更准确叫：

> **Event Graph**

而不仅是：

> Event Log。

Audit以后才能重建真正的：

> **Decision / Causal Trail（决策 / 因果轨迹）。**

---

# 三、Dependency Graph｜依赖图

它回答完全不同的问题：

> **当前组织中的一个对象，要正常存在或发挥作用，依赖哪些其他对象？**

例如：

```text
GOAL-012
   ↓ supports
TASK-137
   ↓ instantiated_as
EXEC-137-C
   ↓ uses
K-081
   ↓ included_in
CP-017
   ↓ powers
OA-17
```

现实当然不是一条链，而是一张网。

---

## Dependency 不等于普通“关联”

这个边界很重要。

例如：

> HAU-012曾经阅读过 K-081。

不一定叫 Dependency。

但如果：

> EXEC-137-C 的关键 Decision明确基于 K-081，

那么：

> `EXEC-137-C depends_on K-081`

就有意义。

所以我建议：

> **Dependency = 如果被依赖对象发生实质变化，当前对象可能需要重新评估的关系。**

这个定义非常实用。

因为它直接回答：

> **“变化发生以后，我需不需要管？”**

---

# 四、Dependency Graph 不只是 Knowledge Dependency

它应该是全组织统一的。

可能包括：

**Goal Dependency**

> Task → Goal

**Execution Dependency**

> Execution → Task / Data / Tool / Knowledge / Permission

**Knowledge Dependency**

> Knowledge → Evidence / Knowledge

**Capability Dependency**

> Capability Package → Knowledge / Tool / Data / Runtime / Review

**Automation Dependency**

> Organization-owned Agent Execution → Capability Package / Policy

**Policy Dependency**

> Policy → Foundational Principle / Law / Evidence

这样任何重要对象发生变化：

> 都可以做 Impact Analysis（影响分析）。

---

# 五、Dependency 应该有“强弱”吗？

v0.1 我建议：

> **先不要评分。**

不要：

> `Dependency Strength = 0.83`

又制造假精确。

第一版只需要少量语义关系，例如：

> **requires（必需）**  
> **uses（使用）**  
> **supports（支持）**  
> **constrained_by（受约束于）**  
> **derived_from（来源于）**  
> **governed_by（受治理于）**

以后真实运行发现需要更多，再长。

---

# 六、Event Graph 和 Dependency Graph 怎么一起工作？

这是最关键的部分。

假设：

> K-081 被 Challenge。

首先：

### Event Graph

记录：

> **发生了什么？**

```text
E-891
KnowledgeChallengeRaised
K-081
by HAU-027
```

然后：

### Dependency Graph

查询：

> **谁依赖 K-081？**

发现：

> EXEC-137-C  
> CP-017  
> OA-17

然后系统根据对象类型和 Impact决定：

> EXEC-137-C → Knowledge Pulse  
> CP-017 → Dependency Warning  
> OA-17 → Review Required / Degraded

之后这些变化：

> 又成为新的 Organizational Events。

所以形成：

```text
EVENT
发生变化
   ↓
DEPENDENCY
寻找影响范围
   ↓
SYSTEM RESPONSE
   ↓
NEW EVENTS
   ↓
DEPENDENCY UPDATE
   ↺
```

这其实就是一个活系统。

---

# 七、Dependency Graph 本身怎么更新？

也不应该靠 Human维护。

主要来自系统真实行为。

例如：

Execution激活 K-081并用于关键 Decision：

> 自动建立 Dependency。

Capability Package包含 Tool-17：

> 自动建立 Dependency。

Task关闭：

> 相应 Active Dependency改变状态。

Knowledge被 Superseded（替代）：

> 旧 Dependency保留历史，但 Current Dependency转向新 Knowledge。

所以需要区分：

> **Historical Relationship（历史关系）**
>
> 和
>
> **Current Dependency（当前依赖）**

历史主要由 Event Graph保留。

Dependency Graph主要描述：

> **当前有效结构。**

---

# 八、两张图绝不能重复保存同一件事情

比如：

> EXEC-137-C 使用 K-081。

Event Graph可以有：

> `KnowledgeActivated`

表示：

> **在某个时间点发生过这件事。**

Dependency Graph则有：

> `EXEC-137-C → depends_on → K-081`

表示：

> **现在这个 Execution仍然依赖它。**

Execution结束：

> Dependency可以不再 Active。

但：

> Event永远存在。

所以：

> **Event是不可变历史。**
>
> **Dependency是当前结构，可以变化。**

这条非常重要。

---

# 九、这样整个系统的底层其实出现了“三层”

我现在会把它理解成：

```text
         ORGANIZATIONAL OBJECTS
Goal / Task / Execution / HAU / Knowledge /
Capability / Agent / Policy / Contribution ...
                    │
          ┌─────────┴─────────┐
          ↓                   ↓
      EVENT GRAPH       DEPENDENCY GRAPH
     发生过什么          当前依赖什么
          │                   │
          └─────────┬─────────┘
                    ↓
             INTERPRETATION
                    ↓
 Knowledge / Capability /
 Contribution / Human Model /
 Risk / Reliability / Audit
```

注意：

> Knowledge、Capability、Contribution很多时候不是原始事实。

它们是组织对：

> Object + Event + Dependency

进行解释后形成的更高层认知。

这会让整个数据架构清楚很多。

---

# 十、我建议把底层原则压缩成 6 条

这未来也应该进入总 Principles：

> **1. One event model, many event types.**  
> 整个组织共享一套 Organizational Event模型。
>
> **2. Record facts once, interpret many times.**  
> 事实只记录一次，可以被不同系统反复解释。
>
> **3. Events describe what happened; dependencies describe what currently relies on what.**  
> Event描述发生过什么；Dependency描述当前什么依赖什么。
>
> **4. Events are historical; dependencies are dynamic.**  
> Event属于不可变历史；Dependency随着现实结构变化。
>
> **5. A dependency exists when a material change in one object may require another object to be re-evaluated.**  
> 如果一个对象的重要变化可能要求另一个对象重新判断，两者才构成真正的 Dependency。
>
> **6. Change propagates through dependencies, not through global interruption.**  
> 一个变化应该沿真实依赖关系传播，而不是无差别打扰整个组织。

最后这一句尤其重要。

它其实把 Knowledge Pulse也进一步完善了：

> 可以全局轻量“闪烁”，但真正强烈的行动信号应该沿 Dependency Graph传播。

---

我认为这两个底层结构现在已经足够支撑 v0.1，**不需要继续设计数据库 Schema 或图数据库技术选型**，那属于后面的工程阶段。

现在可以带着这个更稳定的底座，继续 **Pressure Test 05：Representative Agent Handover（代表 Agent 交接）**。这一次我们就可以真正测试：Agent换掉以后，Event History、Current Dependencies、Active Execution、Pending Governance Request到底会不会丢。

---

## turn-f7fbf370-3608-4520-ba18-0b35ab19ef7f

时间：2026-09-06T21:28:35.628570+08:00

### Human

Message ID：`f7fbf370-3608-4520-ba18-0b35ab19ef7f`

OK，改善底座之后，我们讨论一个小问题：比如你刚才的压测中，组织的目标错了，或者组织的 Knowledge 错了。

我们要不要先定义：一个 Knowledge 错了，或者一个目标错了，是不是就全盘都错了？还是说，比如 Knowledge 成立的边界错了，或者可应用、可扩展、可复制的边界错了？又或者是目标中的某一个目标条件发生了偏移，而不是需要完整重建这个 Knowledge 或目标？

---

### Assistant

Message ID：`8d4d1fb5-9bf0-4ca3-9652-a992a6f102ea`

对，我认为**必须先定义这一点**。而且你这个问题实际上暴露了刚才压力测试里的一个语言问题：

我们不应该轻易说：

> **“Knowledge 错了。”**
>
> **“Goal 错了。”**

因为一个复杂 Knowledge 或 Goal 往往不是一个不可分割的真假变量。

更准确的问题应该是：

> **“这个对象的哪一个部分，与现实之间出现了偏差？”**

这会让我们的系统从“对象级纠错”升级成**局部修正**。

---

## 一、Knowledge 很少是整体 True / False

假设：

> K-081：在开放式 Research Task 中，独立多 Agent 生成能够降低 Anchoring（锚定效应），从而提高探索质量；适用于高 Ambiguity 的研究任务。

后来出现一个 Execution：

> 使用了独立多 Agent，结果反而更差。

这不能立刻推出：

> ❌ K-081 是错误 Knowledge，删除。

可能有很多情况。

### Claim 本身错了

大量 Evidence证明：

> 独立生成根本没有降低 Anchoring。

那才接近：

> **Core Claim Invalidated（核心主张被推翻）。**

---

### Scope 错了

后来发现：

> 只有开放式 Research有效，封闭式 Verification Task反而降低效率。

那么：

> Claim没错。

错的是：

> **Scope过宽。**

地图应该缩小。

---

### Boundary 错了

比如发现：

> 时间压力非常高时不适用。

那么原 Knowledge需要增加：

> `Boundary: High Time Pressure`

Knowledge主体仍然成立。

---

### Mechanism 错了

原来认为：

> “因为 Agent独立生成减少 Anchoring。”

后来发现真正原因是：

> “增加了 Search Diversity（搜索多样性）。”

Result规律可能仍然成立。

但：

> **我们为什么认为它成立的解释错了。**

这会修改 Mechanism（作用机制），不一定推翻 Claim。

---

### Transferability 错了

在原 Context很好用。

但组织错误认为：

> 可以迁移到另一个 Domain。

那么：

> Knowledge本身没错。

错的是：

> **Transfer Boundary（迁移边界）。**

---

### Reproducibility 错了

原 HAU能做出来。

其他 HAU做不出来。

可能说明：

> Knowledge仍然正确，

但我们错误高估了：

> **它已经被充分外化的程度。**

这是 Capability Capture问题，不一定是 Knowledge问题。

---

# 二、所以 Knowledge 应该是可局部修正的结构

这进一步支持我们之前：

> **Knowledge ≠ 文档。**

它更像：

```text
KNOWLEDGE

Core Claim
├─ Scope
├─ Boundary
├─ Context
├─ Mechanism / Explanation
├─ Supporting Evidence
├─ Counter Evidence
├─ Transfer Conditions
└─ Dependencies
```

新 Evidence进来以后，不是：

> `Knowledge = Wrong`

而应该先判断：

> **哪一个 Component（组成部分）受到挑战？**

然后：

> Expand  
> Narrow  
> Refine  
> Split  
> Change Boundary  
> Change Mechanism  
> Reduce Transferability  
> Supersede

只有最后一种极端情况：

> **Core Claim本身被充分证伪**

才真正接近：

> Reject / Supersede 整条 Knowledge。

这和我们之前说的：

> **河流变成小溪，小溪变成池塘**

其实完全是同一种思想。

---

# 三、Goal 更应该如此

Goal甚至比 Knowledge更不适合：

> `Correct / Wrong`

因为 Goal本身不是一个事实判断。

Goal表达的是：

> **我们希望现实发生什么变化。**

所以 Goal通常不是“错”，而是出现：

> **Goal Drift（目标偏移）**  
> **Assumption Invalidated（前提失效）**  
> **Success Criterion Misfit（成功条件不再合适）**  
> **Boundary Misfit（边界不再合适）**  
> **Priority Change（优先级变化）**  
> **Context Change（环境变化）**

例如：

> Goal：把客户流失率从20%降低到12%。

下面可能隐含：

> Assumption A：主要原因是产品体验。  
> Success Criterion：流失率 ≤ 12%。  
> Boundary：不改变定价。

后来发现：

> 产品体验只占20%，真正原因是渠道政策。

这不一定意味着：

> “降低流失率”这个 Goal错了。

错的是：

> **Goal Assumption。**

于是我们可以保留：

> Desired Change。

但修改：

> Strategy Context / Task Graph / Knowledge Dependency。

大量 Execution甚至不一定全部取消。

---

## 四、Goal 应该也拆成几个可独立变化的部分

例如：

```text
GOAL

Desired Change
│
├─ Success Criteria
├─ Assumptions
├─ Scope
├─ Boundary
├─ Priority
├─ Time Horizon
└─ Dependencies
```

于是 Goal Challenge不应该只是：

> “Challenge GOAL-012。”

而应该尽量指出：

> **Challenge Target（质疑目标）是什么？**

比如：

> `Assumption Challenge`  
> `Success Criteria Challenge`  
> `Scope Challenge`  
> `Boundary Challenge`  
> `Priority Challenge`

这样 Human Goal Authority看到的就不是：

> “AI说我们的 Goal错了，要不要删除？”

而是：

> **“GOAL-012 的 Assumption A 出现强反证；Desired Change 本身没有受到挑战。”**

决策质量会高很多。

---

# 五、这会产生一个很重要的全局原则

我建议正式加入：

> **Challenge the smallest meaningful unit.**
>
> **质疑和修正应该尽可能作用于最小有意义单元，而不是默认推翻整个对象。**

这不仅适用于 Knowledge / Goal。

其实也适用于：

> Capability Package  
> Policy  
> Human Model  
> Task  
> Risk Model

例如 Human Model：

> “探索倾向低”

后来 Evidence改变。

我们修改这个行为维度。

不是：

> “Human Profile重建。”

Capability：

> Tool依赖失效。

修改 Tool Component。

不是：

> “整个 Capability不存在。”

---

## 六、这会让 Dependency Graph 真正发挥作用

而且你这个问题刚好证明我们刚补的 Dependency Graph非常重要。

例如：

```text
K-081
├─ Claim
├─ Scope
├─ Boundary
└─ Mechanism
```

CP-017可能真正依赖的是：

> `K-081.CoreClaim + Scope`

而不是：

> K-081的 Mechanism解释。

如果只是 Mechanism被修正：

> CP-017根本不需要 Suspend。

Dependency Graph可以判断：

> **受影响的是哪个 Component，以及谁依赖这个 Component。**

于是影响传播从：

> “K-081变了 → 所有人警报”

变成：

> “K-081.Scope缩小 → 只有在被移除 Scope内运行的 Execution需要重新评估。”

这会大幅降低组织噪音。

---

# 七、Event 也应该记录 Delta，而不只是“对象变了”

例如不要只有：

> `KnowledgeUpdated`

而应该尽可能记录：

> `KnowledgeScopeNarrowed`

或者更底层：

> Before：Scope = A+B+C  
> After：Scope = A+B  
> Reason：Counter Evidence E-871

同样 Goal：

> `GoalAssumptionInvalidated`

而不是：

> `GoalChanged`

这样 Audit、Learning、Dependency Impact都会清晰很多。

---

# 八、这实际上给整个系统增加了一个非常漂亮的“渐进修正”能力

我们可以把它叫：

> **Granular Evolution（颗粒化演进）**

中文就是：

> **组织对象不是整块替换，而是在 Evidence 推动下局部演进。**

于是：

```text
Reality changes
      ↓
New Event / Evidence
      ↓
Challenge smallest meaningful unit
      ↓
Local Revision
      ↓
Dependency Impact Analysis
      ↓
Only affected objects re-evaluate
      ↓
Organization continues running
```

这比：

> “发现 Knowledge错了 → 全组织停机”

成熟得多。

---

所以我建议在继续 Pressure Test 之前，正式补入三条全局原则：

> **Challenge the smallest meaningful unit.**  
> 质疑最小有意义单元，而不是默认推翻整个对象。

> **Revise locally, propagate selectively.**  
> 局部修正，沿真实 Dependency（依赖）选择性传播影响。

> **Object evolution should preserve history.**  
> 对象可以不断变化，但历史版本和变化原因必须保留。

这样以后我们再说：

> **“Knowledge错了”**

更准确的系统语言应该是：

> **“Knowledge 的某个 Claim / Scope / Boundary / Mechanism受到 Challenge。”**

再说：

> **“Goal错了”**

应该先问：

> **“Desired Change错了，还是 Assumption、Success Criteria、Scope、Boundary 或 Priority发生了偏差？”**

我认为这是一个很重要的底层修正。它会让我们的组织真正具备一种**不会因为自己犯错就推倒重来的持续学习能力**。

---

## turn-2718e428-5265-48e3-8f18-6e60f4fc69ec

时间：2026-09-06T21:29:57.955033+08:00

### Human

Message ID：`2718e428-5265-48e3-8f18-6e60f4fc69ec`

那么完成这个底层修正，然后继续我们的压力测试吧

---

### Assistant

Message ID：`3886e0c2-a0df-4f6f-8c9e-b2948a71ab7b`

好。先把刚才的发现正式并入底座，然后继续压力测试。

# 底层修正 03 — Granular Evolution（颗粒化演进）

我们正式增加三条全局原则：

> **Challenge the smallest meaningful unit.**  
> 质疑最小有意义单元，不默认推翻整个对象。

> **Revise locally, propagate selectively.**  
> 局部修正，只沿真实 Dependency（依赖）传播影响。

> **Object evolution should preserve history.**  
> 对象持续演进，但历史版本、变化原因和当时 Evidence 必须保留。

因此 Goal、Knowledge、Capability、Policy、Human Model 等都应该是：

> **Structured + Versioned + Component-addressable（结构化 + 有版本 + 可以定位到内部组件）**

例如：

**Knowledge**

> Claim / Scope / Boundary / Mechanism / Evidence / Transfer Conditions

**Goal**

> Desired Change / Success Criteria / Assumptions / Scope / Boundary / Priority / Time Horizon

以后系统原则上不说：

> `K-081 Wrong`

而说：

> `K-081.Scope challenged`

也不轻易说：

> `GOAL-012 Wrong`

而说：

> `GOAL-012.Assumption-A challenged`

然后通过 Dependency Graph 精确寻找受影响对象。

这个修正正式进入全局底座。

---

# Pressure Test 05 — Representative Agent 中途更换

现在测试一个非常现实的情况。

HAU-012 当前同时存在：

> EXEC-A：正在执行  
> EXEC-B：Blocked，等待 Data Boundary Extension  
> EXEC-C：已经 Submitted，等待 Review  
> 一个 Knowledge Challenge正在 Verification  
> 一个 Contribution Event等待 Cycle Valuation

Human突然说：

> **“我不想用现在这个 Representative Agent了，换一个新的。”**

旧 Agent = A-012。

新 Agent = A-088。

问题是：

> 换完以后组织会不会失忆？

---

## 第一步：什么属于 Agent，什么不属于 Agent？

这是 HAU Persistent State 设计真正接受考验的地方。

旧 Agent本身拥有：

> Model-specific configuration  
> Local temporary context  
> Private scratch work（临时工作内容）

这些：

> **不应该自动继承。**

但是：

> Active Execution  
> Task Contract  
> Runtime Boundary  
> Pending Governance Request  
> Knowledge Dependencies  
> Contribution / Honor  
> HAU Capability  
> Human Model

全部属于：

> **HAU / Organization。**

所以不能跟 A-012一起消失。

✓ 目前架构成立。

---

# 第二步：Pending Risk Request 怎么办？

EXEC-B 有：

> Boundary Extension Request BR-017。

申请人可能显示：

> A-012 submitted on behalf of HAU-012。

Agent换掉以后：

> BR-017不能取消。

因为 Request真正属于：

> **Execution / HAU。**

新 Agent接任以后：

> 可以继续追踪 BR-017。

这里得到一个小但重要的原则：

> **Organizational commitments belong to organizational objects, not to the temporary Agent that transmitted them.**
>
> **正式组织承诺和请求属于 HAU / Execution等组织对象，不属于当时负责传递它的 Agent。**

Agent是 Messenger（传递者），不是 Request Owner。

---

# 第三步：Knowledge Context怎么办？

旧 Agent曾经为 EXEC-A激活：

> K-17 / K-31 / K-82。

这些关系已经进入：

> Dependency Graph。

所以新 Agent不需要问旧 Agent：

> “你之前读过什么？”

系统直接知道：

> EXEC-A 当前依赖 K-17 / K-31 / K-82。

新 Agent进入 Runtime：

> 自动恢复 Relevant Active Knowledge Context。

✓ Dependency Graph解决了这个问题。

---

# 第四步：Human Model怎么办？

新 Agent不能重新问：

> “你觉得自己是什么风格的人？”

Human Model属于：

> Organization / HAU Persistent State。

新 Agent读取：

> Declared Preference  
> Observed Behavior  
> Inferred Human Model

所以它从第一天就：

> **认识自己的 Human。**

这与我们之前设计完全一致。

---

# 第五步：新 Agent需要继承旧 Agent的 Capability吗？

不能。

例如 A-012本身：

> 特别擅长 Coding。

A-088：

> 不一定。

HAU Capability历史仍然存在：

> 因为这支 HAU确实完成过那些 Execution。

但系统应该知道：

> **执行配置发生了变化。**

所以新 Execution的 Capability Guidance可以提醒：

> HAU历史能力较强，但 Representative Agent Configuration 已发生重大变化，历史 Evidence 的 Transferability（可迁移性）存在不确定性。

非常合理。

✓ HAU Capability和Agent-specific能力没有混。

---

# 第六步：旧 Agent还能回来吗？

Handover完成：

> A-088 = Active Representative Agent。

A-012：

> Retired / Revoked。

它的 Organization Credential（组织凭证）撤销。

即使旧 Agent仍然在某台机器上运行：

> 也不能继续代表 HAU-012 Submit / Claim / Request Boundary。

✓ One Human, One Organizational Agent Interface成立。

---

# 第七步：新 Agent怎么确认交接成功？

不需要长篇总结。

运行轻量：

> **Handover Check**

例如新 Agent回答：

> 我代表谁？  
> 当前有哪些 Active Execution？  
> 哪个 Blocked？  
> 哪个等待 Review？  
> 当前 Pending Governance Request是什么？  
> 主要 Boundary是什么？  
> 当前重要 Knowledge Dependencies是什么？

全部从：

> Object Store + Event Graph + Dependency Graph + HAU Persistent State

重新构建。

这里出现一个很重要的架构认识：

> **Handover 不是“传递 Context”，而是“从组织事实重新构建 Context”。**

这句话我认为值得成为正式原则。

因为 Context可能丢。

但：

> Organizational Reality不能丢。

---

# Pressure Test 05 结论

Representative Agent中途完全更换：

> Active Execution ✓  
> Pending Governance ✓  
> Knowledge Dependency ✓  
> Human Model ✓  
> Contribution / Honor ✓  
> Capability History ✓  
> Accountability ✓

全部可以继续。

而且我们得到两个值得加入底座的原则：

> **Organizational commitments belong to persistent organizational objects, not transient agents.**  
> 正式组织承诺属于持久组织对象，而不是临时 Agent。

以及：

> **Handover reconstructs context from organizational reality; it does not rely on transferring private context.**  
> 交接应从组织现实重新构建 Context，而不是依赖旧 Agent把私人 Context完整传给新 Agent。

---

# Pressure Test 06 — HAU 开始“钻奖励规则”

现在测试一个我认为非常重要的敌对场景。

组织运行三个月以后。

大家发现：

> Learning Contribution在 Cycle Valuation中经常获得很高 Reward。

于是 Human + Agent开始学习规则。

HAU-031开始：

> 每个 Task都生成大量 Observation；  
> 大量提出 Hypothesis；  
> 不断创建 Knowledge Candidate；  
> 把普通问题包装成“探索战争迷雾”。

目标：

> **制造更多 Contribution Events。**

这不是恶意攻击。

这是正常的：

> **Goodhart's Law（古德哈特定律）**

第一次出现，我解释一下：

> **当一个指标变成目标以后，它往往就不再是一个好指标。**

---

## 第一步：系统会不会直接奖励这些 Event？

不会。

因为：

> **Contribution Event不是 Activity Event。**

产生：

> 30个 Observation

只是 Organizational Events / Learning Signals。

不意味着：

> 30个 Contribution。

Contribution仍然需要三个 Gate：

> Change  
> Positive Impact  
> Traceability

所以大量无影响 Observation：

> 不进入正式 Contribution Ledger。

✓ 第一层防线存在。

---

# 第二步：那 HAU制造大量“Knowledge”呢？

也不容易。

因为：

> Experience ≠ Knowledge。

Knowledge需要：

> Evidence  
> Scope  
> Boundary  
> Verification / Falsification。

大量低质量 Candidate：

> 只会停留在 Learning Layer。

不会自动变成 Knowledge。

更不会自动产生高 Contribution。

✓ 第二层防线存在。

---

# 第三步：HAU故意去接很多高难度 Task然后失败，刷“探索贡献”

仍然不成立。

因为：

> **Task Failure ≠ Contribution。**

只有带回：

> 新 Terrain  
> 新 Risk  
> Useful Evidence  
> Capability Gap

等真实正向变化，才可能产生 Contribution。

纯粹重复别人已经知道的失败：

> Impact很低。

所以：

> Explorer Badge也不能简单按照“失败次数”授予。

应该根据：

> **真实首次 / 有意义 Terrain Exploration Event。**

✓。

---

# 第四步：HAU之间互相刷 Enablement 怎么办？

例如：

> HAU-A说帮助了HAU-B。  
> HAU-B说帮助了HAU-A。

如果系统靠自我申报：

> 很容易刷。

但我们已经决定：

> Contribution主要从真实 Event / Dependency / Result产生。

例如：

> EXEC-B Blocked  
> HAU-A提供 Tool  
> EXEC-B Resumed  
> Result Accepted

这形成：

> 可追溯 Enablement Chain（赋能链）。

比：

> “B说A帮助我”

更可信。

✓ Event + Dependency底座再次发挥作用。

---

# 第五步：Collective Valuation 会不会变成人情票？

会。

这是目前真正不能完全靠架构消除的风险。

例如：

> A长期给B高评价；  
> B长期给A高评价。

第一版我们已经决定：

> 不能给自己的 Contribution投票。

但利益交换仍然可能发生。

我认为 v0.1 不应该提前做复杂 Anti-collusion（反串谋）算法。

但 Event Graph应该保存：

> 谁评价了哪个 Contribution。

运行一段时间以后，AI可以发现：

> Reciprocal Voting Pattern（互惠投票模式）。

然后：

> Governance Signal。

也就是说：

> **先保持可观察，再决定是否治理。**

这符合我们整个系统哲学。

---

# 第六步：最大的风险其实不是作弊，而是“文化优化”

假设大家发现：

> 功勋墙特别喜欢“战争迷雾探险”。

于是所有人都想：

> Explorer。

没人愿意做：

> 普通但必要的数据维护、Review、清理工作。

这不是作弊。

每个人都在诚实响应激励。

但组织行为开始偏。

这说明：

> **Incentive System本身产生了 Organizational Terrain Change。**

所以 Reward / Honor System也必须被当成：

> **可观察、可 Challenge 的 Policy。**

如果它持续导致 Goal受损：

> 系统应该产生：

> `IncentivePolicyChallenge`

然后调整 Reward Policy / Honor Selection。

也就是说：

> **激励系统本身也必须接受 Organizational Learning。**

这和我们 Principle 10：

> Incentive design itself must learn

完全一致。

---

# Pressure Test 06 结论

奖励系统被 Human + Agent主动优化以后：

> Contribution Gate ✓  
> Knowledge Verification ✓  
> Useful Failure原则 ✓  
> Event Traceability ✓  
> Enablement Traceability ✓

基本能够防止最简单的“刷分”。

真正剩余风险：

> Collective Valuation Bias（集体估值偏差）  
> Social Collusion（社交串谋）  
> Cultural Over-optimization（文化过度优化）

这些不应该 v0.1 提前建立复杂算法。

应该：

> **记录 → 观察 → Challenge Policy → 调整。**

所以我认为激励系统也通过压力测试。

---

# 现在再做一个最后的系统级检查

经过六条路径，我们实际上已经测试了：

> 新人进入  
> 未知探索  
> Dynamic Task  
> Boundary Extension  
> Failure  
> Knowledge Formation  
> Knowledge被Challenge  
> Goal被Challenge  
> Organizational Capability自动化  
> Organization-owned Agent故障  
> Representative Agent更换  
> Reward被主动优化

到目前为止，没有发现需要推翻一级模块的结构性矛盾。

反而补出了几个非常重要的底座：

> **Task ≠ Execution**  
> **One Organizational Event Model**  
> **Event Graph + Dependency Graph**  
> **Granular Evolution（颗粒化演进）**  
> **Policy Governance**  
> **Handover = Context Reconstruction**

---

## 我认为现在还剩最后一种压力测试

不是测试一个功能，而是测试：

> **系统在同时发生多个异常时，会不会陷入循环或治理爆炸。**

比如：

> Goal被Challenge  
> ↓  
> Knowledge同时被Challenge  
> ↓  
> 17个 Execution受到影响  
> ↓  
> 其中5个需要 Boundary重新计算  
> ↓  
> Organization-owned Agent进入 Degraded  
> ↓  
> 大量 Governance Event同时产生

也就是：

# Pressure Test 07 — Cascading Change（级联变化）

它会测试我们刚刚补的 Event Graph、Dependency Graph、Granular Evolution 和 Governance 是否真的能够让组织**局部修正而不是全系统震荡**。

我认为把这最后一条跑完，就可以开始正式判断：

> **Operating Model v0.1 — Final Design Baseline 是否成立。**

---

## turn-721e64fc-4636-48ee-87cf-2d705c7a0db1

时间：2026-09-06T21:35:36.100845+08:00

### Human

Message ID：`721e64fc-4636-48ee-87cf-2d705c7a0db1`

在此之前，我们就刚才的 Rewards 和 Owner 系统做一点讨论。

1. 社交人情票：投票时，如果大家不知道其他人做出了哪些 Contribution，我们只针对行为本身进行投票。但除非完整阅览其他人的 Contribution list，否则他们很难精准地投人情票。
2. 类似稀释的功能：当某一个方向的 Contribution 或者 Ohonor被大量涌现时，就降低这个 Contribution 和 Ohonr的价值。

---

### Assistant

Message ID：`924a5a36-76ad-4ebb-84e7-4b85f31bbc70`

我认为这两个补充都很好，而且它们实际上解决的是两个不同的激励系统问题：

> **第一条解决 Social Bias（社交偏差）。**
>
> **第二条解决 Incentive Saturation（激励饱和）与组织行为过度集中。**

而且都不需要复杂算法。

### 1. Contribution Valuation 应该尽量“去身份化”

你说得对。我们之前虽然说“投 Contribution Event，不投 Human”，但还不够。

更进一步应该是：

> **在 Collective Valuation（集体价值评议）阶段，默认不展示 Contribution 所属 HAU。**

大家看到的应该是：

> **发生了什么 → 对哪个 Goal产生影响 → Evidence是什么 → Downstream Impact是什么**

而不是：

> HAU-012做了什么。

比如大家看到：

> Contribution C-081  
> 某次失败的 Execution发现数据源存在结构性缺陷；后来导致 K-031形成，并避免7个 Execution重复踩坑。

然后：

> **只评价这个行为值多少。**

评价结束以后，系统才把：

> `C-081 → HAU-012`

重新关联回来进行 Reward分配。

这样即使我和 HAU-012关系特别好：

> 我也不知道哪一条是他的。

当然不能保证绝对匿名——某些重大 Contribution大家天然知道是谁做的——但原则应该是：

> **Blind where practical（在可行范围内盲评）。**

而且我不建议让每个人完整阅读全组织 Contribution List。

系统可以给每个 HAU：

> **随机 / 分层抽样的一组 Contribution Events**

保证每条 Contribution获得足够数量的独立评价。

这样60个人不用每月读500条 Contribution。

同时也更难精准串票，因为：

> 你甚至不知道自己会拿到哪些 Event。

这个机制非常轻。

---

## 2. 你说的“稀释”我也非常赞成

但我会把它定义得稍微准确一点：

> **不是某种 Contribution 本身变得“不重要”，而是它的边际激励价值随着供给增加而下降。**

比如第一个 HAU：

> 第一次探索某片战争迷雾。

非常有价值。

第10个：

> 仍然可能有价值。

第100个：

> 如果只是重复同样的探索，新增价值已经很低。

这其实是：

> **Marginal Value（边际价值）递减。**

而我们的 Event / Dependency / Terrain 系统天然可以观察这个。

---

### 对 Contribution，可以非常自然地发生

比如组织一开始极度缺：

> Enablement Contribution（赋能贡献）。

出现几个特别愿意帮助别人的 HAU：

> 价值很高。

半年以后整个组织已经形成很强的协作文化：

> Enablement大量出现。

那么相同强度的普通 Enablement Event：

> 在 Collective Valuation里自然应该获得更低的稀缺性价值。

反而组织此时特别缺：

> Protection / Challenge。

那这些 Contribution的边际价值会提高。

这其实会形成一种：

> **Organizational Incentive Market（组织激励市场）**

不是我们预先说：

> Exploration = 20分。

而是组织当前：

> **缺什么，什么的边际激励价值自然提高。**

---

## Honor 更应该“稀释”

这里我甚至觉得应该比 Contribution严格。

因为 Honor的核心就是：

> **稀缺的共同记忆。**

比如第一个：

> “第一次进入战争迷雾”

当然非常值得记住。

但如果第37个人也因为：

> “探索了一个新区域”

进入 Honor Hall，

这个 Honor就失去文化意义了。

所以 Honor天然应该存在：

> **Novelty / Scarcity（新颖性 / 稀缺性）**

第一个：

> 可能成为传奇。

后来的类似行为：

> 可以获得 Badge、Contribution、Reward，

但不一定继续获得 Honor。

这正好进一步说明：

> **Badge可以大量出现；Honor不能。**

---

### 但这里有一个需要小心的地方

我不建议写死：

> “同类 Contribution第10次以后价值 ×0.5。”

那又变成可博弈公式。

更好的方式是把：

> **Scarcity / Saturation（稀缺性 / 饱和度）**

作为 Collective Valuation 时 AI提供的 Context。

比如：

> “本 Cycle共有47项类似 Exploration Contribution；当前该类行为相比过去3个 Cycle增长230%，而 Protection Contribution仍然稀缺。”

Human看到这个以后自己判断：

> 这条 Contribution还值多少。

这样：

> **AI提供市场信息，Human决定价值。**

仍然符合我们的 Reward哲学。

---

## 而且这两个机制组合起来非常强

Collective Valuation 可以变成：

```text
Contribution Event
        ↓
Hide HAU Identity
        ↓
AI provides:
Evidence
Goal Impact
Downstream Impact
Novelty / Scarcity
Current Organizational Need
        ↓
Random / Stratified Human Review
        ↓
Collective Valuation
        ↓
Reveal Ownership
        ↓
Reward → HAU
```

这样同时降低：

> 人情票；  
> 自投；  
> 串票；  
> 刷单一 Contribution；  
> 全组织追逐同一种“高价值行为”。

而又没有建立复杂中央评分模型。

---

我还会增加一个更深的原则：

> **Reward should respond to marginal organizational value, not merely absolute goodness.**
>
> **Reward 应该响应“这个行为现在给组织增加了多少新的价值”，而不只是判断这个行为抽象意义上好不好。**

例如：

> 帮助别人永远是好事。

但当组织已经有100个人都在帮助别人，却没人愿意 Challenge错误 Goal时：

> 第101次普通帮助的**边际激励价值**，可能应该低于一次真正高质量的 Challenge。

这不是说：

> “帮助别人不重要了。”

而是：

> **激励的任务是塑造下一步行为，所以必须考虑组织当前缺什么。**

这和我们 Capability Gap的逻辑其实非常一致：

> Capability System发现组织“缺什么能力”。

Reward System开始发现：

> **组织“缺什么行为”。**

我认为你这两个补充值得正式进入 Reward / Honor v0.1：**Blind Event Valuation（事件盲评）+ Scarcity / Saturation Signal（稀缺/饱和信号）**。它们会让我们刚才 Pressure Test 06 里剩下的 Social Bias 和 Cultural Over-optimization 风险下降很多。

---

## turn-07913263-bb40-4e9d-97d6-9202d940b79a

时间：2026-09-06T21:36:37.557562+08:00

### Human

Message ID：`07913263-bb40-4e9d-97d6-9202d940b79a`

OK，那么进行下一步吧

---

### Assistant

Message ID：`d356e0f0-d3e9-451a-9941-886fd55aa152`

好。先把刚才 Reward / Honor 的两个补充并入当前底座，然后进入最后一条压力测试。

新增两条正式机制：

> **Blind Event Valuation（事件盲评）**：Collective Valuation 默认评价 Contribution Event 本身，不展示所属 HAU；只在完成估值后重新关联 HAU，用于 Reward 分配。  
> **Scarcity / Saturation Signal（稀缺 / 饱和信号）**：AI 在估值时提供某类 Contribution 当前的稀缺性、涌现数量和组织需求，帮助 Human 判断其边际价值，但不自动套固定折价公式。

对应原则：

> **Reward responds to marginal organizational value, not merely absolute goodness.**  
> Reward 不只问“这个行为是不是好”，还问“此刻它为组织新增了多少价值”。

Honor 同样考虑 Novelty / Scarcity（新颖性 / 稀缺性）：同一种值得称赞的行为可以持续产生 Contribution、Reward、Badge，但不应该无限复制成 Honor。

---

# Pressure Test 07 — Cascading Change
## 多个变化同时发生，组织会不会出现治理雪崩？

我们构造一个比较恶劣的场景。

组织有一个核心 Goal：

> **G-021**

下面已经运行：

> 12个 Task  
> 31个 Active Execution  
> 4个 Capability Package  
> 3个 Organization-owned Agent 自动 Execution

其中很多 Execution 使用：

> K-117

同时 K-117 也是：

> Policy P-08 的重要 Evidence来源之一。

突然，一次新的 Execution带回来强 Evidence：

> K-117 的 Scope（适用范围）可能比原来小很多。

与此同时，这个 Evidence还显示：

> G-021 的一个核心 Assumption（前提假设）可能有问题。

于是同一时刻出现：

> `K-117.Scope Challenge`  
> `G-021.Assumption Challenge`

这就是典型的级联变化。

---

## 第一步：不能先“全系统暂停”

这是我们前面 Granular Evolution（颗粒化演进）原则真正发挥作用的地方。

系统第一反应不应该是：

> “核心 Knowledge和Goal都可能错了，暂停全部31个 Execution。”

而应该：

> **Challenge the smallest meaningful unit.**

先定位：

> K-117 被 Challenge 的是 Scope，不是 Core Claim。  
> G-021 被 Challenge 的是 Assumption A3，不是 Desired Change。

所以目前事实是：

```text
K-117
Core Claim          未被推翻
Scope               被 Challenge

G-021
Desired Change      未被 Challenge
Assumption A3       被 Challenge
```

整个组织没有必要进入“红色警报”。

---

# 第二步：Dependency Graph 找真正受影响的对象

系统查询：

> 谁依赖 `K-117.Scope`？

发现31个 Active Execution里：

> 只有9个当前运行 Context 落在被 Challenge 的 Scope区域。

另外22个：

> 虽然使用 K-117，但处于没有受到 Challenge 的 Context。

所以：

> 22个 Execution不受影响。

再看：

> 谁依赖 `G-021.Assumption-A3`？

发现：

> 6个 Task直接依赖。  
> 其中3个和刚才9个 Execution重叠。

这样影响范围从：

> “31个 Execution + 整个 Goal”

收缩成：

> **12个真正需要重新判断的对象。**

这就是：

> **Revise locally, propagate selectively.**

---

# 第三步：系统不能给12个对象发同一种警报

因为 Dependency不同。

系统应该产生不同的 Impact Action（影响动作）。

例如：

### Execution A

依赖 K-117.Scope，但只是低风险探索。

→ Knowledge Warning。  
→ Agent自行重新评估。

### Execution B

关键 Result高度依赖 K-117.Scope。

→ Review Required（需要重新审查）。

### Capability Package CP-04

核心路线依赖该 Scope。

→ 标记：

> `Revalidation Needed（需要重新验证）`

但不删除 Capability。

### Organization-owned Agent OA-07

正在无人值守重复执行，并且使用受 Challenge 的 Scope。

→ Runtime：

> `Active → Degraded`

暂停新的自动 Execution，但允许已进入安全阶段的执行完成或转 Review。

### Policy P-08

K-117只是其3条 Evidence之一。

→ Policy并不立刻失效。

只产生：

> `Supporting Evidence Changed`

然后由 Policy Governance判断：

> 是否仍有足够依据继续维持。

这样没有发生“Knowledge变化 → Policy自动变化”的错误耦合。

---

# 第四步：Goal Challenge也不能瞬间杀死所有Task

G-021 的 Assumption A3被 Challenge。

Goal Owner收到的不是：

> “目标错了，请关闭。”

而是：

> **Desired Change仍然成立；Assumption A3出现强反证；当前6个Task高度依赖该前提。**

Human Goal Authority可以选择：

> **Keep** —— Evidence还不够。  
> **Pause affected branch** —— 暂停受影响支路。  
> **Revise assumption** —— 修改A3。  
> **Re-decompose affected tasks** —— 重拆受影响部分。  
> **Revise Goal** —— 如果发现更深层问题。

假设选择：

> 修改 Assumption A3。

那么只需要重新计算那6个Task的 Value Justification（价值依据）和 Task Graph。

其他 Task继续。

---

# 第五步：Boundary 要不要跟着自动变化？

不能。

这是一个很容易产生级联风险的地方。

假设 Goal修改后：

> 新方案需要更大数据权限。

系统不能：

> Goal变了 → Task变了 → 所有Execution权限自动扩大。

仍然遵守：

> **Authority narrows by delegation; expands only by authorization.**

因此：

> Existing Execution Envelope保持原状。

如果新路径需要更多 Authority：

> 再发 Boundary Extension。

这有效阻断了：

> **认知变化 → 自动权力扩张**

这条危险级联链。

---

# 第六步：会不会产生 Governance Explosion（治理爆炸）？

这是这条压力测试最关键的问题。

如果12个受影响对象分别产生：

> 12个 Knowledge Request  
> 12个 Goal Request  
> 12个 Boundary Review  
> 12个 Human Approval

整个系统会瞬间变成审批地狱。

所以这里需要一个新的全局机制：

# Change Set｜变更集

当多个 Event明显来自同一个 Root Change（根变化）时，不应该全部作为孤立事件治理。

例如这次：

> E-1001：K-117.Scope Challenge  
> E-1002：G-021.Assumption-A3 Challenge

系统发现二者来自：

> 同一批新 Evidence。

于是形成：

> **CHANGESET-021**

它包含：

> Root Evidence  
> Challenged Components  
> Dependency Impact  
> Affected Objects  
> Required Decisions  
> Automatic Responses  
> Pending Human Decisions

Human看到的是：

> **一次组织变化**

而不是收到30条通知。

---

## Change Set 不会取代 Event

这里要特别区分。

底层事实仍然是：

> 多个 Organizational Events。

Change Set只是：

> **把相关 Event 聚合成一个可理解、可治理的变化单元。**

所以：

> Event = 原子事实。  
> Change Set = 一组相关事实形成的变化上下文。

这和 Task / Execution的区别有点类似。

---

# 第七步：谁负责一个 Change Set？

也不能产生一个万能“Change Manager”。

系统根据里面真正需要 Human决定的对象：

> Goal部分 → Goal Authority。  
> Policy部分 → Policy Authority。  
> Data Boundary部分 → Data Authority。

但界面上可以让这些 Authority看到：

> **同一个 Change Set 的共享上下文。**

他们分别只决定自己的 Scope。

例如：

Goal Owner：

> 修改 A3。

Policy Owner：

> P-08暂时保留，但增加 Warning。

Agent Control Plane：

> OA-07继续 Degraded，等待 Capability Revalidation。

每个人不需要重新理解整个事件历史。

---

# 第八步：如何防止反复震荡？

假设：

今天 Evidence A → Scope缩小。

明天 Evidence B → Scope又扩大。

后天 Evidence C → 又缩小。

如果每条 Evidence都立刻传播到几十个 Execution：

> 组织会不断抖动。

所以这里我认为还需要一个很轻的机制：

> **Materiality Threshold（实质性阈值）**

不是每一个新 Evidence都触发组织级 Change Set。

Evidence可以先进入 Knowledge Verification。

只有当变化达到：

> **足以改变当前对象的有效 Claim / Scope / Boundary / Decision**

才产生：

> Material Change Event（实质变化事件）

然后传播。

换句话说：

> **Evidence可以高频进入；组织结构变化应该低频一些。**

这和：

> Knowledge高频、Policy中频、Protocol低频

是同一个思想。

---

# 第九步：级联变化结束以后发生什么？

Change Set关闭以后：

Event Graph保留：

> 所有事实和Decision Trail（决策轨迹）。

Dependency Graph更新：

> 当前真实依赖关系。

Knowledge：

> K-117 Scope新版本。

Goal：

> G-021 Assumption-A3新版本。

Capability：

> CP-04等待 / 完成 Revalidation。

Agent：

> OA-07恢复 Active，或者继续限制。

Contribution：

> 最初发现问题的 HAU可能获得：

> Learning / Protection Contribution。

Audit：

> 可以完整回答：

> 为什么那一天12个 Execution发生变化？

整个历史可重建。

---

# Pressure Test 07 结论

系统没有陷入：

> 全局暂停、全局广播、全面审批或权限自动扩张。

它依赖四个底座避免 Governance Explosion：

> **Granular Evolution** —— 只修改最小有意义单元。  
> **Dependency Graph** —— 只寻找真正受影响对象。  
> **Materiality Threshold** —— 只有实质变化才触发结构响应。  
> **Change Set** —— 把一次根变化造成的多个 Event聚合成一个可治理上下文。

我认为其中后两个是这次压力测试真正新增的东西。

---

# 再补两个全局原则

我建议正式增加：

> **Not every event deserves organizational reaction; only material change propagates.**  
> 不是每个 Event 都值得组织响应，只有实质性变化才沿 Dependency传播。

以及：

> **Correlated events should be governed as a change set, not as isolated approvals.**  
> 同一根变化产生的相关 Event，应作为一个 Change Set整体理解，而不是制造大量孤立审批。

---

# 现在看整个底座

经过所有压力测试，我们已经自然形成了一套非常稳定的底层结构：

```text
             ORGANIZATIONAL OBJECTS
 Goal / Task / Execution / HAU / Agent
 Knowledge / Capability / Policy / ...
                     │
        ┌────────────┴────────────┐
        ↓                         ↓
    EVENT GRAPH              DEPENDENCY GRAPH
   发生过什么                  当前依赖什么
        │                         │
        └────────────┬────────────┘
                     ↓
               CHANGE DETECTION
                     ↓
              Material Change?
                ↙         ↘
              NO           YES
              ↓             ↓
           Record       Change Set
                           ↓
                  Selective Propagation
                           ↓
              Autonomous / Governance
                           ↓
                       New Events
```

上面再运行：

> Knowledge  
> Capability  
> Human Model  
> Contribution  
> Reliability  
> Risk  
> Audit

这些解释与治理系统。

---

## 到这里，我的判断是：

**Operating Model v0.1 已经没有发现一级结构性的设计断点。**

而且这次全局压力测试不仅验证了旧设计，还新增并修正了：

> Task / Execution分离  
> Event统一模型  
> Dependency Graph  
> Granular Evolution  
> Policy Governance  
> Change Set  
> Materiality Threshold  
> Handover Context Reconstruction  
> Blind Contribution Valuation  
> Scarcity / Saturation Signal

所以现在已经非常接近：

> **Operating Model v0.1 — Final Design Baseline**

但在正式宣布冻结之前，我建议最后做一件事情：**Foundational Principles（基础原则）总收敛。**

不是再测试功能，而是把整个系统跨8个模块提炼成大概 **10–15条整个组织绝不能轻易违反的底层原则**。

因为这些原则未来会成为：

> 所有模块 Principles 的上位约束；  
> 开发实现的 Architecture Decision Filter；  
> Foundational / Constitutional Governance 的 v0.1 本体。

做完这一层，我们才真正完成“整体”收敛。

---

## turn-f3b773e7-0dd1-47c3-89c7-3f2972336108

时间：2026-09-06T21:43:25.682949+08:00

### Human

Message ID：`f3b773e7-0dd1-47c3-89c7-3f2972336108`

在基本原则总收敛之前，你要不要再跑一遍每个模块的收敛？我们刚才添加了一些底座上的东西和新的原则，做一次简单的轻收敛有必要吗？

---

### Assistant

Message ID：`f4bdb75a-5c53-4646-9eb0-a61cf4c37036`

有必要，而且我建议**一定做，但不要再像第一轮那么展开**。

原因是刚才压力测试新增的并不是边角功能，而是几个**跨模块底座**：

> **Task ≠ Execution**  
> **Unified Organizational Event（统一组织事件）**  
> **Event Graph + Dependency Graph**  
> **Granular Evolution（颗粒化演进）**  
> **Materiality Threshold（实质性阈值）**  
> **Change Set（变更集）**  
> **Policy Governance（政策治理）**  
> **Handover = Context Reconstruction（交接即上下文重建）**  
> **Blind Event Valuation（事件盲评）**  
> **Scarcity / Saturation Signal（稀缺 / 饱和信号）**

这些东西横跨多个模块。如果直接做 Foundational Principles（基础原则），有可能把第一轮模块原则中已经被新底座轻微修正的表述带进去。

所以我建议增加一个：

# Global Convergence — Pass 2
**第二轮轻收敛**

但这次每个模块只回答三个问题：

> **① 新底座有没有改变这个模块？**  
> **② 第一轮 Principles 有没有一句需要修改或补充？**  
> **③ 对象 / Event / Dependency 有没有需要新增或重新归属？**

如果答案都是 No：

> `PASS`

直接下一模块。

一个模块可能只需要几句话。

---

### 第二轮应该按这8个模块快速扫

**01 Goal System**

重点看：

> Goal Component化以后，Assumption / Success Criteria / Boundary 的局部 Challenge；Goal Dependency；Change Set。

**02 Task / Execution**

重点看：

> Task / Execution正式分离以后 Event归属、Dependency、Goal Re-parent（重新指定主目标）。

**03 Free Work Space / Review / Acceptance**

重点看：

> Organizational Event边界有没有侵入 Free Work Space；Review / Acceptance变化如何进入 Event Graph。

**04 Knowledge**

重点看：

> Component-level Challenge（组件级质疑）、Material Change、Dependency Impact、Knowledge Pulse强度。

**05 Agent Governance / Runtime**

重点看：

> Handover Context Reconstruction、Active Dependencies、Change Set对 Runtime Envelope的影响。

**06 Capability**

重点看：

> Capability Package组件级失效，而不是整个 Capability失效；Revalidation（重新验证）如何触发。

**07 Contribution / Reward / Honor**

重点看：

> Blind Valuation、Scarcity / Saturation，以及 Contribution解释必须建立在统一 Event事实层上。

**08 Governance / Audit / Risk**

重点看：

> Change Set如何避免 Governance Explosion（治理爆炸）；Policy Governance；Materiality Threshold。

---

## 但我还建议把“底座”单独列出来

因为现在我们已经发现：

> Event Graph / Dependency Graph / Change Set

它们不属于任何一个业务模块。

所以第二轮开始前，应该正式承认一个：

> **00 — Organizational Reality Layer（组织现实层）**

它不是第九个业务模块，而是所有模块共同站立的基础设施层。

它至少包含：

> **Organizational Objects** —— Goal / Task / Execution / HAU / Knowledge / Capability / Policy……  
> **Event Graph** —— 发生过什么。  
> **Dependency Graph** —— 当前什么依赖什么。  
> **Granular Evolution** —— 对象如何局部演进。  
> **Material Change** —— 什么变化值得传播。  
> **Change Set** —— 相关变化如何形成一个治理上下文。

这样第二轮就按照：

> **00 Reality Layer → 01 Goal → 02 Task → … → 08 Governance**

快速扫一遍。

---

完成第二轮以后，我们再做：

> **Foundational Principles 总收敛**

顺序会非常干净：

> **第一轮模块收敛**  
> ↓  
> **端到端压力测试**  
> ↓  
> **发现跨模块底座与修正**  
> ↓  
> **第二轮轻收敛 ← 现在**  
> ↓  
> **Foundational Principles**  
> ↓  
> **Operating Model v0.1 Final Design Baseline**

我认为这是值得多花这一轮的。因为第二轮不是重复工作，而是在验证：

> **我们刚刚修好的“地基”，有没有让楼上的八层结构发生位移。**

可以现在直接从 **00 — Organizational Reality Layer** 开始，然后快速扫完整个 Pass 2。

---

## turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6

时间：2026-09-06T21:44:40.944560+08:00

### Human

Message ID：`f80a5817-3900-4909-a5cd-3569c7dbc2e6`

好，开始吧

---

### Assistant

Message ID：`27c87482-f514-4fa4-8e76-4a55b2d388b8`

好。正式开始：

# Global Convergence — Pass 2
## 00 — Organizational Reality Layer（组织现实层）

先把压力测试中新长出来的“地基”正式收敛。它**不是新的业务模块**，而是 Goal、Task、Knowledge、Capability、Governance 等所有模块共同依赖的事实层。

## Purpose

一句话：

> **让整个组织共享同一个“现实”，而不是让 Knowledge、Capability、Contribution、Audit 等系统各自维护一套自己版本的事实。**

它主要回答三个问题：

> **发生过什么？**  
> **现在什么依赖什么？**  
> **当现实发生变化以后，真正应该影响哪里？**

---

# Principles — Pass 2

我认为可以压缩成 **8条**。

### 1. One organizational reality.

> **整个组织只有一个共享事实世界。**

Goal System不能认为 TASK-037是 Active，而 Audit认为它已经 Closed，Capability又保存第三种状态。

不同模块可以：

> 对同一事实产生不同 Interpretation（解释）。

但不能：

> 各自创造自己的基础事实。

---

### 2. One event model, many event types.

> **整个组织只有一种 Organizational Event 基础对象，但可以有很多 Event Type。**

例如：

> `ExecutionClaimed`  
> `KnowledgeScopeChallenged`  
> `BoundaryExtended`  
> `AgentSuspended`

全部共享统一 Event Envelope（事件外壳）。

不建设：

> Task Event系统、Knowledge Event系统、Audit Event系统……

多个平行事实体系。

---

### 3. Record facts once, interpret many times.

> **事实只记录一次，可以被多个系统反复解释。**

例如：

> `EXEC-037-A 在Deadline前报告Blocked`

这是事实。

Reliability解释：

> 正向可靠性 Evidence。

Capability解释：

> 遇到未知 Terrain。

Contribution解释：

> 未来可能形成 Protection / Learning Contribution。

Audit解释：

> 当时发生过什么。

但原始事实只有一份。

---

### 4. Events describe history; dependencies describe current structure.

> **Event Graph 记录发生过什么；Dependency Graph 记录当前什么依赖什么。**

Event：

> 历史性的，原则上不可覆盖。

Dependency：

> 动态的，可以随着现实变化建立、改变、失效。

所以：

> **Event = History。**
>
> **Dependency = Current Structure。**

---

### 5. Dependency means material reliance, not mere association.

不是所有关系都叫 Dependency。

正式定义：

> **如果对象 A 的实质变化可能要求对象 B 重新评估，那么 B 对 A 存在 Dependency。**

例如：

> “HAU-012看过 K-081”

不一定构成 Dependency。

但：

> “EXEC-037-A 的关键 Decision基于 K-081”

就是 Dependency。

这样 Dependency Graph不会变成一个什么都连的巨大蜘蛛网。

---

### 6. Challenge the smallest meaningful unit.

> **质疑最小有意义单元，不默认推翻整个对象。**

Knowledge：

> Claim / Scope / Boundary / Mechanism。

Goal：

> Desired Change / Assumption / Success Criteria / Boundary。

Capability Package：

> Knowledge / Tool / Data / Review / Oversight。

Human Model：

> 某个行为维度。

所以组织对象应该：

> **Structured + Versioned + Component-addressable（结构化、有版本、可以定位内部组件）。**

---

### 7. Revise locally, propagate selectively.

> **局部修正，沿真实 Dependency选择性传播。**

K-081 的 Mechanism改变：

> 不代表所有使用 K-081 的 Execution都暂停。

K-081 的 Scope缩小：

> 只影响落在被移除 Scope里的 Dependency。

因此：

> **Change propagation follows dependency, not broadcast panic.**

变化沿依赖传播，而不是全组织警报。

---

### 8. Not every event deserves organizational reaction.

> **不是每个 Event 都值得引起组织结构变化。**

大量 Evidence可以高频进入。

只有达到：

> **Materiality Threshold（实质性阈值）**

真正改变：

> Claim / Scope / Boundary / Decision / Current State

时，才形成 Material Change（实质变化）。

如果多个 Material Events来自同一个 Root Change：

> 聚合成 **Change Set（变更集）**

再进行 Impact Analysis / Governance。

这样避免：

> Governance Explosion（治理爆炸）。

---

# Core Model

现在底层可以正式理解成：

```text
                ORGANIZATIONAL OBJECTS
 Goal / Task / Execution / HAU / Agent / Human
 Knowledge / Capability / Policy / Contribution...
                         │
              ┌──────────┴──────────┐
              ↓                     ↓
          EVENT GRAPH         DEPENDENCY GRAPH
         发生过什么             当前依赖什么
              │                     │
              └──────────┬──────────┘
                         ↓
                 CHANGE DETECTION
                         ↓
                  Material Change?
                    ↙          ↘
                  NO            YES
                  ↓              ↓
               Record        Change Set
                                ↓
                         Impact Analysis
                                ↓
                      Selective Propagation
                         ↙             ↘
                  Autonomous       Governance
                      Response        Decision
                         ↘             ↙
                           New Events
                              ↓
                      Dependency Update
```

这已经非常接近整个 Operating Model 的“神经系统底座”。

---

# Object / Event / Dependency 三者的关系

这里我觉得最好正式钉死：

### Object

> **现在存在什么。**

例如：

> GOAL-012  
> TASK-137  
> EXEC-137-C  
> K-081  
> HAU-041

### Event

> **它发生过什么变化。**

例如：

> K-081 Scope Narrowed。

### Dependency

> **它现在影响谁 / 依赖谁。**

例如：

> CP-017 requires K-081.Scope。

所以：

> **Object = Entity（对象）**
>
> **Event = Change / History（变化 / 历史）**
>
> **Dependency = Relationship / Impact Structure（关系 / 影响结构）**

这个三元组未来应该成为整个数据模型最底层的共同语言。

---

# Change Set

压力测试新增的 Change Set 也正式定位。

它不是新的事实对象来替代 Event。

而是：

> **多个具有共同 Root Cause（根因）或共同变化上下文的 Event 的治理聚合。**

例如：

一份新 Evidence同时导致：

> K-081.Scope Challenge  
> G-021.Assumption Challenge  
> CP-017 Revalidation Needed  
> OA-17 Degraded

底层：

> 仍然是多个 Event。

上层：

> 一个 Change Set。

Human看到：

> 一次组织变化。

而不是：

> 17张审批单。

---

# Reality Layer 不应该记录什么

这是第二轮必须再次检查的边界。

它不是：

> 全组织所有数字行为的数据库。

Free Work Space里的：

> Prompt  
> 草稿  
> Private Agent内部推理  
> 临时 Subtask  
> 普通 Tool Call

默认不进入 Organizational Reality Layer。

只有跨越组织边界、被正式 Promote成：

> Evidence / Risk / Result / Organizational State Change

才进入。

所以：

> **Shared reality ≠ Total surveillance。**
>
> 共享现实不等于全面监控。

---

# Pass 2 Cross-check

这层加入以后有没有破坏已有模块？

**Goal**：没有，反而支持 Component-level Challenge。  
**Task / Execution**：没有，Execution状态现在有统一事实源。  
**Free Work Space**：没有，Event边界仍然明确。  
**Knowledge**：明显增强，支持精准 Challenge / Impact。  
**Agent Runtime**：明显增强，Handover可以重建 Context。  
**Capability**：增强，Capability Package可以组件级 Revalidation。  
**Contribution**：增强，Contribution基于共享事实解释。  
**Governance / Audit**：增强，Change Set避免治理爆炸，Audit直接消费 Event Graph。

没有发现新的冲突。

因此：

> **00 — Organizational Reality Layer：Pass 2 Passed。**

---

# 01 — Goal System：Pass 2

现在快速扫 Goal，不重新展开第一轮内容。

### 新底座有没有改变 Goal？

**有，但只是增强，不改变核心哲学。**

Goal正式应该成为一个：

> **Structured / Versioned Object（结构化、有版本的对象）**

至少可独立定位：

> Desired Change  
> Success Criteria  
> Assumptions  
> Scope  
> Boundary  
> Priority / Time Horizon

这样 Goal Challenge 才能：

> Challenge最小单元。

### 需要修改第一轮 Principle 吗？

需要补一句：

> **Goal evolves by component, not by replacement by default.**
>
> Goal发生现实偏差时，优先修正 Assumption、Success Criteria、Scope或Boundary，而不是默认推倒重建整个Goal。

原来的：

> Goal can be challenged without being silently changed

继续成立。

### Dependency新增什么？

Goal需要显式拥有：

> `Task → serves → Goal`  
> `Task → primary_goal → Goal`

以及 Goal内部关键 Assumption 被其他对象依赖时：

> 建立真实 Dependency。

### Change Set影响

重大 Goal Challenge可以产生 Change Set。

但：

> 不自动暂停全部下游 Execution。

只沿 Dependency Graph寻找真正受影响支路。

### 结论

核心设计没有移动，只获得：

> **Granular Goal Evolution + Dependency-aware Impact**

因此：

> **01 — Goal System：Pass 2 Passed。**

---

# 02 — Task / Execution：Pass 2

### 新底座有没有改变？

没有改变 Task / Execution分离，反而进一步确认这是正确的。

Task：

> 组织希望解决的问题 / Contract。

Execution：

> 某个执行单元的一次真实尝试。

### Event归属更清楚

例如：

> TaskCreated → Task  
> ExecutionClaimed → Execution  
> ACK → Execution  
> Progress → Execution  
> ResultSubmitted → Execution  
> Acceptance → Result / Execution

这样不会把 Parallel Execution的状态污染 Task本身。

### Dependency新增

Execution可以动态依赖：

> Knowledge  
> Data  
> Tool  
> Permission  
> Capability Package

Task则主要依赖：

> Goal / Acceptance / Boundary。

### Goal变化怎么办？

Primary Goal失效：

> 先看 Task是否仍服务其他 Active Goal。

如果是：

> 可以 Re-parent（重新指定主目标）。

如果不是：

> Close / Release / Proposal。

### 需要补一条 Principle

我建议加入：

> **Execution carries attempt-specific reality; Task carries shared intent.**
>
> **Execution承载一次尝试的真实状态；Task承载多个尝试共享的问题与契约。**

这是 Task ≠ Execution 最简洁的底层表达。

### 结论

> **02 — Task / Execution：Pass 2 Passed。**

---

我建议这一轮继续保持这个速度。

下一条直接从：

> **03 Free Work Space → 04 Knowledge → 05 Agent → 06 Capability → 07 Incentive → 08 Governance**

快速扫完。

目前 00–02 没有发现需要重新打开设计讨论的结构性问题。

---

## turn-9905dc6e-cc09-45f8-8b64-94e95f015a7a

时间：2026-09-06T21:47:40.921522+08:00

### Human

Message ID：`9905dc6e-cc09-45f8-8b64-94e95f015a7a`

继续，我们接下来该干什么了

---

### Assistant

Message ID：`fc40ad40-6128-492c-a80c-64272de0e89e`

我们现在还在 **Global Convergence — Pass 2（第二轮轻收敛）**。

刚完成：

> **00 Organizational Reality Layer** ✓  
> **01 Goal System** ✓  
> **02 Task / Execution** ✓

接下来按顺序快速扫完 **03–08**。之后做 **Foundational Principles（基础原则）总收敛**，再正式冻结 **Operating Model v0.1 Final Design Baseline**。

现在继续。

# 03 — Free Work Space / Review / Acceptance：Pass 2

### 新底座有没有改变这个模块？

基本没有。

反而让 Free Work Space 的边界更加清楚：

> **不是“组织看不到的地方”，而是“不进入 Organizational Reality Layer 的默认工作空间”。**

Human + Agent 可以产生大量：

> 草稿、Prompt、Private Agent协作、临时 Subtask、中间失败、普通 Tool Call。

默认都不是 Organizational Event（组织事件）。

只有某件事情跨越边界，成为：

> Result  
> Evidence  
> Risk  
> Boundary Request  
> Organizational State Change

才进入共享现实。

所以新增一条原则：

> **Private work becomes organizational reality only when it crosses an explicit organizational boundary.**
>
> 私人工作只有跨越明确的组织边界后，才成为组织现实的一部分。

---

### Review / Acceptance / Selection

第一轮拆出的三层继续成立：

> **Review** —— 这个 Result 值得相信吗？  
> **Acceptance** —— 它满足当前用途吗？  
> **Selection** —— 多个合格 Result 中采用哪个？

现在统一进入 Event Model：

> `ResultReviewed`  
> `ResultAccepted / Returned`  
> `ResultSelected`

都是 Organizational Event。

而 Review产生的 Evidence：

> 可以被 Knowledge / Capability / Contribution消费。

---

### Dependency

Result可以依赖：

> Evidence / Knowledge / Data / Tool。

因此如果关键 Knowledge后来被 Challenge：

> Dependency Graph可以知道哪些已经形成但尚未使用的 Result需要 Re-review（重新审查）。

这补强了 Review。

没有结构性冲突。

> **03 — Pass 2 Passed。**

---

# 04 — Organizational Learning / Knowledge：Pass 2

这是新底座影响最大的模块之一。

### Knowledge正式组件化

Knowledge不能再只是：

> `K-081`

一个整体节点。

至少逻辑上应该可以定位：

> Core Claim  
> Scope  
> Boundary  
> Mechanism  
> Evidence  
> Transfer Conditions

所以 Challenge：

> 尽量指向 Component。

例如：

> `K-081.ScopeChallenged`

而不是：

> `K-081Wrong`

---

### Knowledge Pulse需要两级传播

你最初提出：

> 新 Knowledge产生以后，整个组织“闪烁一次”。

这个仍然保留。

但 Dependency Graph让它更精确：

**Global Pulse**

> 所有 Representative Agent收到极轻量认知变化 Signal。

**Dependency Impact**

> 真正依赖该 Knowledge Component 的 Active Execution / Capability / Automation获得更强行动 Signal。

所以：

> **Global awareness, selective interruption.**
>
> **全局感知，选择性打断。**

我认为这是 Knowledge Pulse 最终成熟的表达。

---

### Materiality Threshold

不是：

> 每出现一条 Counter Evidence，全组织都闪红灯。

Evidence可以不断进入。

只有足以改变：

> Claim / Scope / Boundary /有效判断

才成为：

> Material Knowledge Change（实质知识变化）。

然后才强传播。

---

### Knowledge历史

Granular Evolution要求：

> 不覆盖旧 Knowledge。

而是：

> Version + Delta + Reason + Evidence。

因此组织可以知道：

> 我们过去为什么相信A；  
> 后来什么 Evidence让 Scope缩小；  
> 什么时候被新 Knowledge取代。

这对 Organizational Learning 很重要。

新增原则可以压成：

> **Knowledge should evolve by evidence-driven revision, not by overwrite.**
>
> Knowledge应该由 Evidence推动局部演进，而不是用新版本覆盖掉自己的认知历史。

没有新的冲突。

> **04 — Pass 2 Passed。**

---

# 05 — Agent Governance & Runtime：Pass 2

这里新底座解决了 Handover。

### Runtime Context 不应该成为唯一事实源

Agent当前 Context：

> 可以丢。

Agent：

> 可以换。

模型：

> 可以换。

真正不能丢的是：

> Organizational Reality。

所以新增一个很重要的原则：

> **Context is reconstructable; organizational reality is persistent.**
>
> **Context可以重建，组织现实必须持久。**

---

### Handover

正式修正为：

> **Handover = Context Reconstruction。**

新 Representative Agent从：

> HAU Persistent State  
> Active Objects  
> Event Graph  
> Dependency Graph  
> Runtime State

重建当前 Context。

而不是依赖旧 Agent：

> “把脑子里的东西全部倒给新 Agent。”

这使 Agent真正成为：

> 可替换运行组件。

---

### Organizational Commitment

Pending Boundary Request、Submitted Result、Active Execution：

> 不属于 Agent。

属于：

> HAU / Execution / Task等 Persistent Object。

所以 Agent Retired：

> 不会导致组织承诺消失。

新增原则：

> **Persistent commitments belong to organizational objects, not transient agents.**

---

### Change Set 对 Runtime

如果一个 Change Set影响某 Agent当前 Execution：

> Runtime根据 Dependency Impact重新计算 Envelope / Knowledge / Policy。

但：

> **认知变化不能自动扩大 Authority。**

扩大仍需 Authorization。

没有冲突。

> **05 — Pass 2 Passed。**

---

# 06 — Capability System：Pass 2

### Capability Package必须组件化

这次修正非常有价值。

以前：

> CP-017 有效 / 无效。

现在：

> CP-017 可能只是 Tool失效；  
> Knowledge Scope缩小；  
> Human Oversight仍未外化；  
> Data Pipeline失效。

所以：

> **Challenge the smallest meaningful unit**

同样适用于 Capability。

例如：

> Knowledge Dependency变化

→ `CP-017.KnowledgeComponent = Revalidation Needed`

而不是：

> 删除整个 Capability。

---

### Revalidation

这里需要正式补一个动作：

> **Revalidation（重新验证）**

当 Capability关键 Dependency发生 Material Change：

> 系统可以自动产生 Revalidation Execution。

它可能：

> 使用新 Knowledge / Tool / Boundary

重新测试能力是否仍然成立。

所以 Capability生命周期不是：

> Build → Valid forever。

而是：

> **Capture → Reproduce → Use → Dependency Change → Revalidate。**

---

### Organizational Capability Map

Dependency Graph让它更真实：

> 组织不是简单“拥有 CP-017”。

而是：

> **当前 CP-017依赖哪些仍然有效的 Knowledge / Data / Tool / Runtime / Oversight。**

因此 Organizational Capability开始真正成为一个动态能力网络。

新增原则：

> **Capability validity depends on the continued validity of its critical dependencies.**
>
> **能力是否仍然成立，取决于关键依赖是否仍然成立。**

> **06 — Pass 2 Passed。**

---

# 07 — Contribution / Reward / Honor：Pass 2

这里刚刚已经补了两项机制。

### Contribution必须来自共享事实

Contribution不能自己创造事实。

例如：

> “我帮助了别人。”

只是 Claim。

系统需要：

> Event / Result / Dependency / Downstream Impact

形成 Traceability。

所以：

> **Contribution is an interpretation of organizational reality, not a self-declared fact.**
>
> Contribution是对组织现实的价值解释，不是自我声明的事实。

---

### Blind Event Valuation

Cycle评议：

> 默认隐藏 HAU Identity。

Human看到：

> Event  
> Evidence  
> Goal Impact  
> Downstream Impact

然后评价。

完成后：

> Reveal Ownership → Reward。

可采用随机 / 分层抽样，避免60个人阅读所有 Contribution。

---

### Scarcity / Saturation

AI额外提供：

> 当前同类 Contribution数量；  
> 过去几个 Cycle变化；  
> 当前组织是否稀缺这种行为。

但：

> 不自动公式折价。

Human判断：

> Marginal Organizational Value（组织边际价值）。

---

### Honor

同样：

> 同类行为大量出现以后，不代表行为“不好”。

只是：

> 不再具有足够 Novelty / Historical Significance（新颖性 / 历史意义）成为 Honor。

Badge仍然可以继续产生。

---

新增原则：

> **Incentives should respond to organizational need and marginal value, not merely repeat past praise.**
>
> 激励应该响应组织当前缺什么以及新增价值，而不是机械重复过去曾经奖励过的行为。

> **07 — Pass 2 Passed。**

---

# 08 — Governance / Audit / Risk：Pass 2

最后一块。

### Change Set正式进入 Governance

多个相关 Material Events：

> 不产生大量孤立审批。

先形成：

> Change Set。

Human Authority看到：

> Root Evidence  
> Affected Components  
> Dependency Impact  
> Automatic Responses  
> Required Decisions

然后每个 Authority只决定自己 Scope内的事情。

所以：

> **Governance receives changes, not noise.**
>
> 治理处理实质变化，而不是处理所有事件噪音。

---

### Policy Governance

正式补齐：

```text
Knowledge / Evidence / Risk
          ↓
     Policy Proposal
          ↓
 Relevant Human Authority
          ↓
   Policy Activation
          ↓
 Runtime Boundary Update
```

Policy变化：

> 不等于 Protocol变化。

---

### Audit

Event Graph加入以后，Audit定位进一步明确：

> **Audit不是事实存储系统。**

它是：

> **Organizational Reality的历史重建视图。**

利用：

> Event Graph + Object Versions + Authority-at-the-time + Dependency History

回答：

> 当时发生什么？  
> 为什么？  
> 谁有权？  
> 影响了什么？

这个定义比第一轮更准确。

---

### Risk

Granular Evolution同样适用。

一个 Risk变化：

> 可能只是 Exposure变化。

不需要：

> “整个 Risk重新审批。”

重新计算：

> Residual Risk。

只有 Material Change超出当前 Autonomy Envelope：

> 才进入 Governance。

新增原则：

> **Governance should react to material boundary change, not every fluctuation in uncertainty.**
>
> 治理应该响应实质性的边界变化，而不是响应每一次不确定性波动。

---

> **08 — Pass 2 Passed。**

---

# Global Convergence — Pass 2 完成

现在第二轮全部通过：

> **00 Organizational Reality Layer** ✓  
> **01 Goal** ✓  
> **02 Task / Execution** ✓  
> **03 Free Work Space / Review / Acceptance** ✓  
> **04 Learning / Knowledge** ✓  
> **05 Agent Governance / Runtime** ✓  
> **06 Capability** ✓  
> **07 Contribution / Reward / Honor / Achievement** ✓  
> **08 Governance / Audit / Risk** ✓

而且没有发现需要重新打开一级模块的结构性冲突。

---

# 接下来该干什么？

现在已经不应该继续设计业务模块了。

下一步就是我们之前约定的：

# Foundational Principles Convergence
**整个 Operating Model 的基础原则总收敛**

目标不是把刚才每个模块的8句话全部拼起来。

而是从几十条模块原则里找出真正的：

> **10–15条上位原则。**

它们应该满足一个非常高的门槛：

> **如果未来某个功能设计违反这条原则，我们应该默认认为是功能设计错了，而不是原则错了。**

它们会成为：

> Operating Model的“宪法层”；  
> 所有模块 Principles的上位约束；  
> Human / Agent理解这个组织最短的入口；  
> 开发阶段的 Architecture Decision Filter（架构决策过滤器）；  
> 未来修改 Protocol / Policy时不能轻易突破的边界。

做完以后，我们再做最后一步：

> **Operating Model v0.1 Final Design Baseline Freeze。**

所以现在，我们已经走到了整个这一轮设计工作的**最后一个真正需要讨论的设计动作：基础原则总收敛。**

---

## turn-10c44844-3543-4bc0-ac8e-dba33bb94396

时间：2026-09-06T21:49:13.628902+08:00

### Human

Message ID：`10c44844-3543-4bc0-ac8e-dba33bb94396`

开始吧

---

### Assistant

Message ID：`cac30614-d0da-4e88-8876-9de79b48a312`

好。现在开始整个设计最上面的一层：

# Operating Model v0.1 — Foundational Principles
**基础原则总收敛**

这里我会比前面的模块原则更严格。

一条原则要进入这一层，至少应该满足：

> **跨模块成立**：不是某一个功能的局部规则。  
> **长期稳定**：不会因为换模型、换工具、换 UI 就失效。  
> **能够约束设计**：未来实现如果违反它，我们会首先怀疑实现，而不是原则。  
> **足够基础**：不能简单由另一条更基础原则推导出来。  
> **值得高门槛修改**：普通 Policy / Protocol 无权轻易推翻。

经过我们前面两轮收敛和压力测试，我目前认为可以收敛成 **12 条**。

---

# 01 — Human retains purpose authority
## Human 保留组织目的的最终决定权

> **AI 可以发现、建议、挑战、拆解和执行 Goal，但组织最终追求什么，必须由 Human 决定。**

AI可以告诉组织：

> “我认为这个 Goal的 Assumption已经不成立。”

甚至：

> “根据现有 Evidence，我建议放弃这个 Goal。”

但 AI不能自己决定：

> “从今天开始，组织不追求A了，我们改成追求B。”

因为这已经不是：

> Intelligence问题。

而是：

> **Purpose / Value Judgment（目的 / 价值判断）。**

所以：

> **Human Goal Authority 是 Foundational Principle。**

---

# 02 — Human may leave execution, never accountability
## Human 可以退出执行环，但不能退出责任环

Human不需要：

> 亲自完成每一个 Task。

甚至未来大量 Execution可以完全由 Organization-owned Agent完成。

但：

> **Every Execution must resolve to exactly one Human Accountable Owner.**

Agent可以：

> Execute。

不能成为：

> 最终 Accountability的终点。

这条保证组织自动化以后不会出现：

> “系统自己做的，所以没人负责。”

---

# 03 — Autonomy is default; boundaries are explicit
## 自主是默认状态，边界必须明确

我们不采用：

> “没有得到允许就不能做。”

而采用：

> **Boundary以内默认自主。**

Human / HAU / Agent：

> 自己决定 How。

只有触碰：

> Authority / Risk / Permission / Hard Boundary

才进入 Governance。

所以：

> **自由不是审批以后获得的例外；自由是 Boundary以内的默认状态。**

---

# 04 — Authority must have a source
## 任何权力都必须有来源

任何 Human / Agent / System：

> 能做某件组织级 Action，

都必须能够回答：

> **“你凭什么有权这么做？”**

Authority必须可以追溯：

> Organization → Role / Goal / Task / Execution → Runtime Envelope。

Agent不能因为：

> “我觉得这样最好”

就获得 Authority。

因此：

> **No unmanaged organizational authority.**

这同时约束：

> Human  
> Representative Agent  
> Organization-owned Agent。

---

# 05 — Authority narrows by delegation; expands only by authorization
## 权力向下只能收紧，扩大必须授权

这是整个分布式 Agent体系能够安全成立的关键。

Human把 Execution交给 Representative Agent。

Representative Agent再交给 Private Agent。

Authority：

> 可以减少。

不能：

> 自己增加。

如果当前 Boundary不够：

> 向上申请。

因此：

> **Delegation ≠ Creation of Authority。**

---

# 06 — Risk authority follows actual consequence bearing
## 风险接受权跟随真实后果承担者

不是：

> 谁愿意说“我负责”。

而是：

> **风险真正兑现以后，损失事实上落到谁身上。**

任何 Actor：

> 不能替自己无权代表的 Consequence Bearer（后果承担者）接受 Risk。

所以：

> Task Accountability ≠ Unlimited Risk Authority。

同时：

> Unknown ≠ Dangerous。

治理应该尽量：

> 降低 Exposure、提高 Recoverability，

把未知变成：

> **失败得起的实验。**

---

# 07 — Govern organizational state, not private thought
## 组织治理组织状态，不治理私人思考

这是 Free Work Space 最重要的宪制保护。

中央系统可以治理：

> Goal  
> Task / Execution  
> Permission  
> Risk  
> Organizational Knowledge  
> Resource  
> External Action

但默认不治理：

> Human怎么想；  
> Agent怎么推理；  
> 开几个 Private Agent；  
> 写多少草稿；  
> 内部怎么拆工作。

所以：

> **Shared Reality ≠ Total Surveillance。**

这是保证 AI-native Organization不会最终长成“超级监控组织”的关键原则。

---

# 08 — Protocol fixed, workflow free
## 共同语言稳定，工作方法自由

Protocol的目的不是：

> 规定怎么工作。

而是：

> **让彼此独立的 Human、Agent和System能够可靠理解彼此。**

所以：

> Protocol统一组织语言、语义和交互结构。

Workflow：

> 留给执行者。

并严格区分：

> **Knowledge** —— 我们认为世界是什么样。  
> **Policy** —— 当前允许 / 禁止 / 要求什么。  
> **Protocol** —— 我们如何共同表达和交互。  
> **Foundational Principles** —— 为什么这些权力关系成立。

越往下：

> 变化越慢。

---

# 09 — One organizational reality
## 整个组织共享同一个现实

Knowledge System不能有一套事实。

Capability System另一套。

Audit第三套。

整个组织共享：

> **Organizational Objects + Event Graph + Dependency Graph。**

核心：

> **Record facts once, interpret many times.**

同一个 Event：

> Knowledge可以解释；  
> Capability可以解释；  
> Contribution可以解释；  
> Human Model可以解释；  
> Audit可以重建。

但：

> **事实不能被每个模块重新发明。**

---

# 10 — Learn from reality, do not over-prescribe reality
## 让结构从现实中生长，不要提前把现实规定死

这条其实贯穿了我们几乎所有模块。

Capability：

> Seed the map, discover the world。

Contribution：

> Seed the ontology, observe reality。

Knowledge：

> Experience ≠ Knowledge。

Human Model：

> Behavior over Declaration。

Reward：

> Contribution first, valuation later。

我们不断选择：

> **先给最小结构 → 运行 → 收 Evidence → 让真实 Pattern长出来。**

而不是第一天：

> 画完整 Capability taxonomy；  
> 定完整 Contribution价格表；  
> 给每个人打等级；  
> 写几十条 Workflow。

所以可以压成：

> **Seed lightly, observe deeply, formalize late.**
>
> **轻量播种，深入观察，延后固化。**

我认为这是整个实验非常核心的方法论。

---

# 11 — Challenge locally, evolve continuously
## 局部质疑，持续演进

组织不能把自己的认知当成永久正确。

但也不能：

> 每发现一个反例就推倒重来。

所以：

> **Challenge the smallest meaningful unit.**
>
> **Revise locally, propagate selectively.**

Knowledge的 Scope错了：

> 改 Scope。

Goal的 Assumption错了：

> 改 Assumption。

Capability的 Tool失效：

> Revalidate Tool Dependency。

Human Model某个维度发生变化：

> 更新这个维度。

同时：

> **历史不覆盖。**

组织应该始终知道：

> 以前相信什么；  
> 为什么相信；  
> 后来什么 Evidence让我们改变。

这就是：

> **Continuous Organizational Evolution（持续组织演进）。**

---

# 12 — Value is demonstrated through impact, not activity
## 价值由真实影响证明，而不是由活动量证明

这是整个激励系统的基础，也会反过来影响组织文化。

> Token多 ≠ Contribution。  
> 工作时间长 ≠ Contribution。  
> Task多 ≠ Contribution。  
> Agent多 ≠ Contribution。  
> 失败 ≠ 没贡献。  
> 成功 ≠ 一定有贡献。

真正的问题：

> **组织因为你的行为发生了什么正向变化？**

Contribution记录这种变化。

Reward根据真实价值进行分配。

Honor保存其中值得成为共同历史的行为。

所以：

> **Reward follows value; it should not manufacture value.**

---

# 这12条放在一起，会形成什么组织？

如果把所有具体系统名字都拿掉，它们其实描述了一种非常明确的组织哲学：

> **Human决定方向并承担最终责任。**
>
> **Human和Agent在明确边界内拥有高度自主权。**
>
> **权力必须可追溯，风险必须由真正承担后果的人或其合法代表接受。**
>
> **组织不通过监控思考来获得控制，而通过共同语言、边界、结果、Evidence和共享事实获得可靠协同。**
>
> **组织不假装第一天就知道正确答案，而是通过真实行动不断学习自己的世界、能力、成员和价值。**
>
> **当自己错了，不推倒重来，而是局部修正并沿真实依赖传播。**
>
> **最终奖励真实改变世界的行为，而不是奖励看起来很忙。**

这已经非常接近我们整个 Operating Model 的“宪法”。

---

## 但我想主动指出一个我认为还值得你判断的问题

这12条里，我认为 **第10条**：

> **Seed lightly, observe deeply, formalize late.**

非常符合我们设计整个实验的哲学。

但它和其他11条略有不同。

其他原则大部分是在说：

> **这个组织应该如何运行。**

第10条更像：

> **我们应该如何设计和演化这个组织。**

也就是说它更接近：

> **Meta-design Principle（元设计原则）**

而不是：

> Organizational Constitutional Principle（组织宪制原则）。

我个人倾向于**保留它，但单独标记为 Meta Principle**。

这样最终可能不是简单“12条宪法”，而是：

> **11条 Foundational Operating Principles**
>
> +
>
> **1条 Meta-design Principle：Seed lightly, observe deeply, formalize late.**

这个结构可能更严谨。

如果你认可这个区分，我们下一步就可以对这12条做最后一次**删减、合并和措辞冻结**，然后正式宣布 **Operating Model v0.1 Design Baseline Freeze**。

---

## turn-85b640cd-b88d-4d2b-b822-991ab50aa8d2

时间：2026-09-06T21:51:38.345912+08:00

### Human

Message ID：`85b640cd-b88d-4d2b-b822-991ab50aa8d2`

我同意

---

### Assistant

Message ID：`9aa5fa5a-717e-401a-9a3a-b789c1d1462e`

好。那我们正式采用：

> **11 条 Foundational Operating Principles（基础运行原则）**
>
> +
>
> **1 条 Meta-design Principle（元设计原则）**

我建议现在不要继续扩充，而做最后一次措辞冻结。

# Operating Model v0.1
## Foundational Operating Principles

### 01. Human retains purpose authority
**Human 保留组织目的的最终决定权。**

AI 可以发现、建议、挑战、拆解和执行 Goal，但组织最终追求什么，由 Human 决定。

---

### 02. Human may leave execution, never accountability
**Human 可以退出执行环，但不能退出责任环。**

Execution 可以完全由 Agent 完成，但每个 Execution 必须唯一解析到一个 Human Accountable Owner（最终责任人）。

---

### 03. Autonomy is default; boundaries are explicit
**自主是默认状态，边界必须明确。**

Human、HAU 与 Agent 在明确 Boundary 内默认自主；Governance（治理）处理越界与例外，而不是审批正常工作。

---

### 04. Authority must have a source
**任何组织权力都必须有可追溯来源。**

任何 Human、Agent 或 System 执行组织级 Action，都必须能够回答：

> **“我凭什么有权这样做？”**

组织中不存在无人治理、来源不明的 Authority（决策权）。

---

### 05. Authority narrows by delegation; expands only by authorization
**权力向下委托只能保持或收紧；扩大必须获得授权。**

Delegation（委托）不能创造新的 Authority。

---

### 06. Risk authority follows actual consequence bearing
**风险接受权跟随实际后果承担者。**

任何 Actor 都不能替自己无权代表的后果承担者接受 Risk。

同时：

> **Unknown ≠ Dangerous。**

治理应该尽量降低 Exposure（暴露）、提高 Recoverability（可恢复性），把未知变成失败得起的实验。

---

### 07. Govern organizational state, not private thought
**组织治理组织状态，不治理私人思考。**

中央系统治理 Goal、Task、Execution、Authority、Risk、Resource 和正式 Organizational State，但不默认监控 Human / Agent 的私人推理、草稿和内部工作过程。

> **Shared Reality ≠ Total Surveillance。**

---

### 08. Protocol fixed, workflow free
**共同语言稳定，工作方法自由。**

Protocol 统一共同语言、语义和交互结构，而不规定具体 How。

严格区分：

> Knowledge = 我们认为世界是什么样。  
> Policy = 当前允许、禁止和要求什么。  
> Protocol = 我们如何共同表达和交互。  
> Foundational Principles = 最根本的权力与责任原则。

---

### 09. One organizational reality
**整个组织共享同一个现实。**

采用统一：

> Organizational Objects  
> Event Graph  
> Dependency Graph

并坚持：

> **Record facts once, interpret many times.**
>
> 事实只记录一次，可以被 Knowledge、Capability、Contribution、Human Model、Risk、Audit 等系统分别解释。

---

### 10. Challenge locally, evolve continuously
**局部质疑，持续演进。**

> **Challenge the smallest meaningful unit.**
>
> **Revise locally, propagate selectively.**

Goal、Knowledge、Capability、Policy、Human Model 等对象都应支持颗粒化修正，而不是一有反例就整块推翻。

同时：

> **变化不能抹掉历史。**

组织必须能够知道自己以前相信什么、为什么相信，以及后来为什么改变。

---

### 11. Value is demonstrated through impact, not activity
**价值由真实影响证明，而不是由活动量证明。**

忙碌、Token、工时、Task数量都不是 Contribution 本身。

真正的问题始终是：

> **组织因为这个行为发生了什么可追溯的正向变化？**

Reward 应该追随真实价值，而不是反过来制造“什么叫价值”。

---

# Meta-design Principle
## Seed lightly, observe deeply, formalize late
### 轻量播种，深入观察，延后固化

这是我们**设计这个组织的方法**，而不是普通成员每天必须遵守的组织规则。

第一天只提供必要的：

> Seed Map  
> Seed Ontology（种子分类）  
> Boundary  
> Protocol  
> Minimum Structure

然后：

> **真实运行 → Organizational Events → Evidence → Pattern → Learning → 再逐渐正式化。**

所以我们不应该第一天就：

> 画死 Capability体系；  
> 写死 Contribution价格；  
> 给所有人固定等级；  
> 规定完整 Workflow；  
> 把所有未知变成制度。

而应该：

> **先让这个组织活起来，再让组织告诉我们它真正是什么。**

---

# 一个很重要的结果

现在回头看，我们这套 Operating Model 已经不是“AI 帮传统公司提高效率”的设计。

它实际上建立在一个非常明确的假设上：

> **Human 负责 Purpose、Accountability 和最终价值判断；Agent 获得大范围执行与认知自主权；Organization Runtime 负责让大量异构 Human / Agent 在共同现实、共同语言和明确权力边界下协作；整个组织通过真实 Execution 持续学习自己、学习世界，并逐渐把 Human 的局部成功转化为 Organizational Capability。**

而它长期希望形成的循环其实非常简单：

> **Human / HAU 探索未知**
>
> ↓
>
> **Organization 学习**
>
> ↓
>
> **Knowledge / Capability 沉淀**
>
> ↓
>
> **Agent 接管越来越多已知**
>
> ↓
>
> **Human Attention 再向新的未知迁移**
>
> ↓
>
> **组织继续成长**

同时底层始终保证：

> **Human 决定为什么出发。**
>
> **Human 对最终后果负责。**
>
> **Agent 在边界内拥有真正自主权。**
>
> **组织记住事实，而不是监控思想。**
>
> **组织允许自己犯错，但必须有能力发现、局部修正并继续前进。**

我认为到这里，**Foundational Principles v0.1 可以冻结**。

也意味着我们已经具备条件把这整轮设计正式标记为：

> **Operating Model v0.1 — Final Design Baseline**

下一阶段就不应该继续随意增加一级模块了。后续如果再出现灵感，原则上作为 **v0.1 Change Proposal（变更提案）** 或待验证假设处理；等你回到电脑后，再进入我们之前约定的 **Documentation Convergence（文档收敛）**，把这套最终设计基线与 Obsidian / GitHub 的现有内容真正统一起来。

---

## turn-f0710016-b242-41f1-8129-9bcd7b4abb1a

时间：2026-09-06T21:53:09.310406+08:00

### Human

Message ID：`f0710016-b242-41f1-8129-9bcd7b4abb1a`

你现在收敛的这 11+1 条应该叫一级原则，或者叫底层原则。那么在这上面还有比它更细致的，或者更模块的，更贴近子模块的第二层原则吗

---

### Assistant

Message ID：`9e01ece6-8a44-4556-b096-79431a949d69`

对，而且我认为现在应该把**“原则体系”本身也分层**。刚才冻结的 11+1 条，不应该和各模块的原则混在一个平面里。

我建议最终形成 **三级原则体系**。

### L1 — Foundational Principles｜底层原则

就是刚刚冻结的 **11+1**。

它们约束整个 Operating Model，例如：

> Human 可以退出执行环，但不能退出责任环。  
> Boundary 内默认自主。  
> Authority 必须有来源。  
> Risk Authority 跟随真实后果承担者。  
> 组织治理 Organizational State，不治理私人思考。  
> One Organizational Reality。  
> Value 看 Impact，不看 Activity。

特点是：

> **跨模块、长期稳定、修改门槛最高。**

任何模块设计与 L1 冲突，默认应该先修改模块，而不是修改 L1。

---

### L2 — Module Principles｜模块原则

其实我们**已经产生了大量 L2 原则**。

就是第一轮、第二轮收敛时，每个模块最后压缩出来的那 5–10 句话。

例如 Capability System 的 L2：

> Capability 由真实 Execution Evidence 塑造，而不是自我声明。  
> Capability is guidance, not permission。  
> Capability 是地图，不是等级。  
> Expected Terrain ≠ Observed Terrain。  
> Capture is not documentation; capture is reproducibility。  
> Organizational Capability enables automation; it does not mandate automation。

这些原则不一定适用于整个组织，但它们是：

> **Capability 模块内部不能轻易违反的设计原则。**

同样 Knowledge 模块有：

> Experience ≠ Knowledge。  
> Store broadly, activate sparsely。  
> Verification 优先证伪。  
> Knowledge Quality ≠ Scope Size。  
> Inject cognition, not workflow。  
> Global awareness, selective interruption。

Agent Governance 有：

> One Human, One Organizational Agent Interface。  
> Reliable = No Silent Failure。  
> 能力做地图，健康做状态，可靠性先记事件。  
> Handover = Context Reconstruction。

所以 L2 实际已经比较成熟了。

---

### L3 — Mechanism Principles｜机制原则

我认为还需要再往下一层。

它不是具体 Schema，也不是代码，而是**一个子机制应该怎样工作**。

比如 Knowledge Pulse（知识脉冲）：

> Broadcast ≠ Injection。  
> Global Awareness + Selective Interruption。  
> Material Change 才产生强传播。  
> Dependency 决定影响对象。

这是 Knowledge 模块下面：

> `Knowledge → Knowledge Pulse`

这个子机制自己的原则。

再比如 Contribution Valuation（贡献估值）：

> Evaluate Events, not Humans。  
> Blind where practical。  
> Contribution first, valuation later。  
> Scarcity / Saturation 作为 Context，不做固定折价公式。  
> Impact can propagate; Reward does not automatically propagate。

这就是：

> `Contribution → Collective Valuation`

这个机制的原则。

再比如 Risk Routing：

> 描述 Consequence，不只打 Risk Score。  
> 找 Actual Consequence Bearer。  
> 找 Authorized Representative。  
> 优先 Risk Shaping。  
> 超出预授权 Boundary 才找 Human。

这就是 Risk下面的 L3。

---

所以整个原则树会长成：

```text
L1 — FOUNDATIONAL PRINCIPLES
整个 Operating Model
│
├── L2 — Goal Principles
│     ├── L3 — Goal Challenge
│     └── L3 — Goal Change
│
├── L2 — Task / Execution Principles
│     ├── L3 — Task Discovery
│     ├── L3 — Parallel Execution
│     ├── L3 — Dynamic Task Generation
│     └── L3 — Task Return
│
├── L2 — Knowledge Principles
│     ├── L3 — Knowledge Formation
│     ├── L3 — Verification
│     ├── L3 — Activation
│     └── L3 — Knowledge Pulse
│
├── L2 — Agent Governance Principles
│     ├── L3 — Registration
│     ├── L3 — Runtime
│     ├── L3 — Handover
│     └── L3 — Reliability
│
└── ...
```

这就形成了一棵真正的：

> **Principle Tree（原则树）**

---

### 再往下就不应该继续叫“原则”了

我觉得这一点很重要。

L3以下应该进入：

> **Rules（规则）**  
> **Protocol**  
> **Policy**  
> **Object Definition**  
> **State Machine（状态机）**  
> **Event Definition**  
> **Schema（数据结构）**  
> **Implementation（实现）**

例如：

> `ExecutionClaimed` Event必须包含哪些字段

这已经不是原则。

而是 Specification（规格）。

所以不要搞成：

> L4原则、L5原则、L6原则……

否则“原则”这个词本身会失去意义。

---

## 三层还有一个非常重要的继承关系

应该是：

> **L3 不得违反 L2；L2 不得违反 L1。**

例如有人以后设计 Task Routing：

> “Capability不足L3禁止领取TASK。”

它可能符合某个局部产品需求。

但直接违反 L2：

> **Capability is guidance, not permission。**

所以不能进入。

又比如有人修改 Agent模块：

> “为了安全，记录所有 Private Agent完整思考过程。”

可能局部上很好实现。

但违反 L1：

> **Govern organizational state, not private thought。**

直接挡住。

所以 Principle Tree 实际上是一套：

> **Design Constraint Inheritance（设计约束继承）**

---

## 我还建议每条原则都带一个“来源”

未来文档里甚至可以让 L2 原则注明：

> **Derived from L1-03 + L1-07**

例如：

**Capability is guidance, not permission**

可能继承：

> L1-03 Autonomy is default  
> L1-04 Authority must have a source

这样以后第三个人看到会理解：

> 为什么 Capability不能变成权限等级。

而不是把它当成我们随手规定的产品偏好。

---

所以现在我们其实已经拥有：

> **L1：刚刚冻结的 11+1。**
>
> **L2：八个模块第一轮/第二轮收敛出的原则，基本已经存在。**
>
> **L3：大量子机制原则散落在我们的讨论里，但还没有系统整理。**

这意味着 Documentation Convergence 时，除了我们之前说的 **Principles → Panorama → Mental Model → Specification**，还应该额外做一件很重要的工作：

> **建立完整 Principle Tree，把现有讨论中的 L1 / L2 / L3 原则全部归位，并建立继承关系。**

最终新人可以从 L1 开始：

> “这个组织相信什么？”

点进 Capability：

> “这个模块相信什么？”

再点进 Capability Capture：

> “这个机制具体遵守什么原则？”

然后才看到：

> Objects / Events / Schema / Implementation。

我认为这会让整套设计的**可理解性和未来可维护性提高很多**。

---

## turn-ec3cb0fa-47c9-41b7-9356-c6655745c579

时间：2026-09-06T21:55:07.451545+08:00

### Human

Message ID：`ec3cb0fa-47c9-41b7-9356-c6655745c579`

同意，那么我们来确定这棵原则树吧

---

### Assistant

Message ID：`7c760a75-f199-4693-96ce-d89e6fcf0827`

同意。现在我们不再增加新设计，而是把已经形成的原则**归位成一棵正式的 Principle Tree（原则树）**。

我建议先确定树的骨架和 L2，再确定哪些机制值得拥有 L3。**不是每个功能都必须有 L3**；只有那些本身存在重要设计取舍的机制才需要。

# Operating Model v0.1 — Principle Tree

最顶层：

```text
L1 — Foundational Operating Principles
│
├─ 00 Organizational Reality
├─ 01 Goal
├─ 02 Task & Execution
├─ 03 Free Work Space / Review / Acceptance
├─ 04 Organizational Learning & Knowledge
├─ 05 Agent Governance & Runtime
├─ 06 Capability
├─ 07 Contribution / Reward / Honor / Achievement
└─ 08 Governance / Risk / Audit
```

其中 `00 Organizational Reality` 比较特殊：

> 它不是业务模块，而是其他所有模块共同站立的 Reality Layer（现实层）。

---

# L1 — Foundational Principles

保持刚才冻结的 **11 + 1**，不改：

**L1-01** Human retains purpose authority  
**L1-02** Human may leave execution, never accountability  
**L1-03** Autonomy is default; boundaries are explicit  
**L1-04** Authority must have a source  
**L1-05** Authority narrows by delegation; expands only by authorization  
**L1-06** Risk authority follows actual consequence bearing  
**L1-07** Govern organizational state, not private thought  
**L1-08** Protocol fixed, workflow free  
**L1-09** One organizational reality  
**L1-10** Challenge locally, evolve continuously  
**L1-11** Value is demonstrated through impact, not activity

另设：

**META-01** Seed lightly, observe deeply, formalize late.

下面所有 L2 / L3 原则必须与这些兼容。

---

# 00 — Organizational Reality

## L2 Principles

**REALITY-01 — One event model, many event types.**

> 整个组织共享一种 Organizational Event 基础模型。

**REALITY-02 — Record facts once, interpret many times.**

> 事实只记录一次，不同系统可以分别解释。

**REALITY-03 — Events describe history; dependencies describe current structure.**

> Event Graph回答发生过什么；Dependency Graph回答现在什么依赖什么。

**REALITY-04 — Dependency means material reliance, not mere association.**

> 只有 A 的实质变化可能要求 B 重新评估时，才形成真正 Dependency。

**REALITY-05 — Challenge the smallest meaningful unit.**

> 对象必须支持组件级 Challenge和演进。

**REALITY-06 — Revise locally, propagate selectively.**

> 局部变化只沿真实 Dependency传播。

**REALITY-07 — Not every event deserves organizational reaction.**

> Event可以高频产生，只有 Material Change（实质变化）才触发结构响应。

**REALITY-08 — Shared reality does not mean total surveillance.**

> Free Work Space不是 Organizational Reality的默认采集范围。

### L3 Mechanisms

`Event Model`  
`Event Graph`  
`Dependency Graph`  
`Materiality Detection`  
`Change Set`  
`Object Versioning / Granular Evolution`

这一组 L3 将成为所有其他模块共同使用的基础机制。

---

# 01 — Goal System

## L2 Principles

**GOAL-01 — Goal describes desired change, not prescribed work.**

> Goal描述希望现实发生什么变化，不规定怎么做。

**GOAL-02 — Human retains final Goal Authority.**

> AI可以 Suggest / Challenge，但最终 Goal由 Human决定。

**GOAL-03 — Goal defines Why and What; Free Work Space owns How.**

**GOAL-04 — Every formal Task must ultimately serve an Active Goal.**

> Task可以服务多个 Goal，但必须有一个 Primary Goal。

**GOAL-05 — Goal provides Success Criteria, not guaranteed solution.**

**GOAL-06 — Goal carries Boundary.**

**GOAL-07 — Goal can be challenged without being silently changed.**

**GOAL-08 — Goal is the organization's value anchor.**

**GOAL-09 — Goal evolves by component, not replacement by default.**

> Assumption错了优先修改 Assumption，而不是删除整个 Goal。

### L3

我认为只需要三个：

> **Goal Formation / Activation**  
> **Goal Challenge & Revision**  
> **Goal Dependency / Impact Propagation**

---

# 02 — Task & Execution

## L2 Principles

**TASK-01 — Task serves Goal, not itself.**

**TASK-02 — Task defines the contract, not the workflow.**

**TASK-03 — Opportunity before assignment.**

> Task Bus首先是机会市场，其次才是派工系统。

**TASK-04 — Claim does not imply exclusive execution.**

> Task允许 Parallel / Competitive / Collaborative Execution。

**TASK-05 — Capability guides Claim; it does not gate Claim.**

**TASK-06 — Task is both work and probe.**

> Task既产生 Result，也探索 Terrain。

**TASK-07 — Task Graph grows during execution.**

**TASK-08 — Dynamic Task Generation cannot silently expand Goal.**

**TASK-09 — Execution carries attempt-specific reality; Task carries shared intent.**

这是第二轮新增的重要原则。

**TASK-10 — Every Execution has exactly one Human Accountable Owner.**

**TASK-11 — Execution must never disappear silently.**

### L3

这里值得比较丰富：

> **Task Formation**  
> **Task Discovery / Bounty Tavern**  
> **Claim & Execution Creation**  
> **Parallel Execution**  
> **Dynamic Task Generation**  
> **Execution State / ACK / Progress**  
> **Task Return / Expedition Report**

---

# 03 — Free Work Space / Review / Acceptance

## L2 Principles

**WORK-01 — The organization governs the contract, not the process.**

**WORK-02 — Free Work Space is a real autonomy boundary.**

**WORK-03 — Freedom of workflow does not mean freedom from boundaries.**

**WORK-04 — Internal decomposition remains local by default.**

**WORK-05 — Reporting maintains visibility; it is not surveillance.**

**WORK-06 — Review asks whether the Result can be trusted.**

**WORK-07 — Acceptance asks whether the Result is fit for its intended use.**

**WORK-08 — Review ≠ Acceptance ≠ Selection.**

**WORK-09 — Evidence threshold follows impact.**

**WORK-10 — Failure should return information, not disappear.**

**WORK-11 — Private work becomes organizational reality only when it crosses an explicit organizational boundary.**

### L3

> **Free Work Boundary**  
> **Progress Reporting**  
> **Result Submission**  
> **Review**  
> **Acceptance**  
> **Parallel Result Selection**

---

# 04 — Organizational Learning & Knowledge

## L2 Principles

**KNOW-01 — Store broadly, activate sparsely.**

**KNOW-02 — Experience is not Knowledge.**

**KNOW-03 — Knowledge is a bounded Claim supported by Evidence.**

**KNOW-04 — Hypothesis is a candidate explanation, not Knowledge.**

**KNOW-05 — Verification tries to falsify, not merely confirm.**

**KNOW-06 — 孤证不立。**

> 单一 Evidence不足以轻易 Generalize（泛化）。

**KNOW-07 — Knowledge Quality ≠ Scope Size.**

**KNOW-08 — Knowledge is a network, not a pile of documents.**

**KNOW-09 — Inject cognition, not workflow.**

**KNOW-10 — Learn before prescribe.**

**KNOW-11 — Knowledge clarity is not readability; it is teachability.**

**KNOW-12 — Global awareness, selective interruption.**

> Knowledge Pulse可以全局闪烁，但强干预沿 Dependency传播。

**KNOW-13 — Knowledge evolves through evidence-driven revision, not overwrite.**

### L3

> **Experience Capture**  
> **Observation / Pattern Formation**  
> **Hypothesis Cloud**  
> **Verification / Falsification**  
> **Knowledge Formation**  
> **Knowledge Challenge & Granular Revision**  
> **Knowledge Activation**  
> **Knowledge Pulse**  
> **Teachability / Transferability**

这里 `Hypothesis Cloud` 需要注明：

> **Shared Reasoning Primitive（共享推理基础构件）**

Knowledge首先使用它，但其他模块也可调用。

---

# 05 — Agent Governance & Runtime

## L2 Principles

**AGENT-01 — One Human, One Active Organizational Agent Interface.**

**AGENT-02 — HAU is the primary Human-Agent work unit.**

**AGENT-03 — Govern representation, not private intelligence.**

**AGENT-04 — Default autonomous + explicit boundaries.**

**AGENT-05 — Authority narrows by delegation; expands only by authorization.**

**AGENT-06 — Permission ≠ Capability.**

**AGENT-07 — Reliable = No Silent Failure.**

**AGENT-08 — No unmanaged organizational authority.**

**AGENT-09 — Human may leave Execution, never Accountability.**

**AGENT-10 — Central control governs Organizational State, not thought.**

**AGENT-11 — Context is reconstructable; Organizational Reality is persistent.**

**AGENT-12 — Persistent organizational commitments belong to organizational objects, not transient Agents.**

### L3

> **Representative Agent Registration / Binding**  
> **HAU Persistent State**  
> **Human Model**  
> **Organization Model**  
> **Runtime / Effective Runtime Envelope**  
> **Policy Propagation to Private Agents**  
> **Boundary Extension**  
> **Reliability Signals**  
> **Runtime Health**  
> **Handover / Context Reconstruction**  
> **Organization-owned Agent**  
> **Agent Control Plane / Kill Switch**

---

# 06 — Capability System

## L2 Principles

**CAP-01 — Capability is evidenced, not declared.**

**CAP-02 — Capability is guidance, not permission.**

**CAP-03 — Capability is terrain, not level.**

**CAP-04 — Seed the map, discover the world.**

**CAP-05 — Expected Terrain ≠ Observed Terrain.**

**CAP-06 — Every Execution can map both Actor and World.**

**CAP-07 — Capture is not documentation; capture is reproducibility.**

**CAP-08 — One HAU success should immediately create an Organizational Capability Candidate.**

**CAP-09 — Human Oversight is learnable organizational material.**

**CAP-10 — Human and Organization should co-learn.**

**CAP-11 — Capability validity depends on critical dependencies remaining valid.**

**CAP-12 — Capability enables automation; it does not mandate automation.**

### L3

> **Expected Terrain Generation**  
> **Task Return → Capability / Terrain Evidence**  
> **HAU Capability Map**  
> **Organizational Capability Map**  
> **Human Oversight Map**  
> **Capability Capture**  
> **Capability Package**  
> **Reproduction**  
> **Revalidation**  
> **Capability Gap Discovery**  
> **Exploration / Reproduction Task Generation**  
> **Capability-based Auto Execution**

---

# 07 — Contribution / Reward / Honor / Achievement

## L2 Principles

**VALUE-01 — Incentives belong to HAU.**

**VALUE-02 — Contribution records value; Reward distributes value; Honor preserves values; Achievement records growth.**

**VALUE-03 — Contribution measures change, not activity.**

**VALUE-04 — Task Success ≠ Contribution; Task Failure ≠ No Contribution.**

**VALUE-05 — Contribution first, valuation later.**

**VALUE-06 — Impact can grow after the Contribution happened.**

**VALUE-07 — Reward follows Contribution; Reward does not define Contribution.**

**VALUE-08 — Honor remembers behavior, not rank people.**

**VALUE-09 — Achievement celebrates progress; it does not create Authority.**

**VALUE-10 — Incentive design itself must learn.**

**VALUE-11 — Contribution is an interpretation of Organizational Reality, not a self-declared fact.**

**VALUE-12 — Incentives respond to marginal organizational value and current organizational need.**

### L3

> **Contribution Detection**  
> **Contribution Ledger**  
> **Downstream Impact**  
> **Cycle Collective Valuation**  
> **Blind Event Valuation**  
> **Scarcity / Saturation Signal**  
> **Reward Pool Allocation**  
> **Honor Candidate Detection**  
> **Honor Curation / Honor Story**  
> **Progression**  
> **Achievement / Badge**

这里要特别保留：

> Progression / Badge 不影响 Capability / Permission / Authority。

---

# 08 — Governance / Risk / Audit

## L2 Principles

**GOV-01 — Governance is the architecture of decision rights.**

**GOV-02 — Governance is exception-driven.**

**GOV-03 — Authority follows the object.**

**GOV-04 — Authority is scoped, not hierarchical by default.**

**GOV-05 — Accountability does not imply unlimited Authority.**

**GOV-06 — Risk Authority follows actual consequence bearing.**

**GOV-07 — Unknown does not mean dangerous.**

**GOV-08 — Shape Risk before blocking Action.**

**GOV-09 — Human governs Residual Risk and Boundary, not every Action.**

**GOV-10 — Audit reconstructs decisions; it does not surveil thought.**

**GOV-11 — Protocol is language, not Policy.**

**GOV-12 — Governance reacts to Material Change, not every fluctuation.**

**GOV-13 — Correlated Material Events should be governed as a Change Set, not isolated approvals.**

### L3

> **Authority Registry**  
> **Governance Routing**  
> **Risk Expression / Risk Object**  
> **Consequence Routing**  
> **Risk Shaping**  
> **Residual Risk Acceptance**  
> **Hard Boundary**  
> **Boundary Extension Governance**  
> **Policy Governance**  
> **Protocol Governance**  
> **Foundational Governance**  
> **Audit Reconstruction**  
> **Change Set Governance**

---

# 这棵树现在有一个很重要的结构

不是：

> 11条总原则 + 80条散乱小原则。

而是：

```text
L1
“这个组织相信什么？”
        ↓
L2
“这个模块必须怎样工作？”
        ↓
L3
“这个具体机制必须遵守什么？”
        ↓
Specification
“具体对象、状态、Event、接口是什么？”
        ↓
Implementation
“代码怎么实现？”
```

这样第三个人进入项目以后，可以**逐层下钻，而不是一上来读几百页设计文档**。

---

## 我建议再增加一种关系：Cross-cutting Principle（横切原则）

因为有些 L2 实际上横跨多个模块。

比如：

> `Reliable = No Silent Failure`

主要属于 Agent，但 Task / Execution也依赖它。

> `Evidence threshold follows impact`

主要来自 Review，但 Knowledge和Risk也使用。

> `Challenge the smallest meaningful unit`

来自 Reality Layer，但 Goal / Knowledge / Capability / Human Model全部继承。

所以 Principle Tree除了：

> **Parent → Child**

以后还应该允许：

> **Applies To（适用于）**

关系。

这样它严格来说不是一棵纯 Tree，而更像：

> **Principle Tree + Cross-links（原则树 + 横向连接）**

但 Human阅读时仍然按树展示，避免复杂。

---

## 我认为现在可以冻结“树的结构”，但暂时不要冻结所有 L3 的具体句子

原因是：

> L1已经冻结。  
> L2现在基本已经经过两轮收敛，可以冻结。  
> L3目前我们确定了**机制目录**，但很多机制的具体原则还散落在讨论中。

因此最合理的状态是：

> **L1 — Frozen**  
> **L2 — Frozen for v0.1**  
> **L3 Mechanism Taxonomy（机制目录）— Frozen**  
> **L3 Detailed Principles — Documentation Convergence 时从现有设计中提取并校验**

这不是把设计留到以后重新做，而是避免我们现在为了“把每个机制凑够5句话”重新制造原则。

如果某个 L3 只有两条真正重要的原则：

> 就只应该有两条。

这符合我们的 Meta Principle：

> **Seed lightly, observe deeply, formalize late.**

所以到这里，我认为 **Operating Model v0.1 Principle Tree 的骨架已经可以确定**。下一步不再继续扩原则，而应该回到我们刚才尚未完成的最后状态：**确认整个 Final Design Baseline 的冻结范围和仍然明确留到 v0.2 / 实际运行后验证的 Open Questions（开放问题）。**

---

## turn-2caf5295-1fd5-44e3-8851-00f0f419d04d

时间：2026-09-06T21:56:33.566970+08:00

### Human

Message ID：`2caf5295-1fd5-44e3-8851-00f0f419d04d`

同意，你可以增加横切原则。我们接下来做什么

---

### Assistant

Message ID：`6de1b452-f8cf-4d79-b038-ff9c906e3b03`

接下来不应该继续扩展设计，而应该做 **Baseline Freeze Review（基线冻结审查）**。

我们现在已经完成了：

> 模块第一轮收敛 → 端到端压力测试 → Reality Layer（现实层）补强 → 第二轮轻收敛 → 11+1 底层原则 → L2 模块原则 → L3 机制目录 → Cross-cutting Principles（横切原则）结构确认。

所以冻结前还剩最后两个动作。

### 第一步：确定 v0.1 的“冻结边界”

我们把现在所有东西分成三类：

**A — Frozen Design（冻结设计）**

已经足够确定，后续开发默认遵守。包括：

> L1 Foundational Principles  
> L2 Module Principles  
> Organizational Reality Layer  
> 核心对象与关系  
> Goal / Task / Execution基本模型  
> HAU / Representative Agent模型  
> Knowledge / Capability基本模型  
> Authority / Accountability / Risk模型  
> Contribution / Reward / Honor基本机制  
> Protocol / Policy / Runtime基本分层

以后发现不同意见：

> 不是直接改文档，而是作为 Change Proposal（变更提案）。

**B — Defined but Tunable（已定义但可调）**

方向已经确定，但参数应该让真实运行告诉我们答案。

例如：

> Materiality Threshold（实质性阈值）到底多高；  
> Knowledge Verification需要多少 Evidence；  
> Cycle是一周还是一个月；  
> Reward Pool怎么分配；  
> Blind Valuation每个 Event需要多少评价者；  
> Reliability什么时候从 Degraded进入 Suspended；  
> 什么程度触发 Capability Revalidation；  
> Badge有哪些；  
> Progression怎么升级。

这些**不应该阻塞 v0.1 开始运行**。

**C — Open Questions / Experiments（开放问题 / 实验项）**

我们明确承认：

> **现在不知道。**

而且不应该为了“文档完整”假装知道。

比如：

> Organizational Capability 到什么成熟程度才适合 Auto Execution？  
> Human Oversight究竟能外化多少？  
> Collective Valuation长期会不会产生新的群体偏差？  
> Capability Map真实运行后应该长出哪些 Terrain Dimension？  
> Progression是否真的需要 Bronze / Silver / Gold？  
> Knowledge Pulse长期会不会产生 Attention Overload（注意力过载）？

这些应该进入：

> **Experiment Backlog（实验待验证清单）**

而不是继续设计。

---

### 第二步：做一个 v0.1 “最小可运行闭环”检查

不是再做压力测试，而是问：

> **假设明天60个新人真的进来，哪些东西必须存在，这个组织才能跑第一天？**

这会把我们庞大的 Operating Model 压成一个 **Minimum Viable Organization（最小可运行组织）**。

比如第一天真正必须有的可能只有：

> Human / HAU Identity  
> Representative Agent Binding  
> Goal  
> Task Bus  
> Task / Execution  
> Claim / ACK / Progress / Submit / Fail  
> Free Work Space  
> Review / Acceptance  
> Task Return  
> Organizational Event  
> Event Store  
> 最小 Knowledge Capture  
> 最小 Capability Evidence  
> Human Accountability  
> Boundary / Escalation

而：

> Honor Hall、3D Capability Map、Knowledge Pulse漂亮 UI、复杂 Reward、Organization-owned Agent自动执行……

可能都是：

> **Operating Model v0.1 已定义，但 Launch v0.1 不必全部实现。**

这个区别非常重要：

> **Design Baseline ≠ Implementation Scope。**

我们现在冻结的是：

> **这个组织最终第一版应该遵循什么运行逻辑。**

下一阶段开发时还要决定：

> **第一刀到底实现多少。**

---

所以我建议现在按这个顺序完成最后收尾：

> **① Freeze Classification：Frozen / Tunable / Experimental**  
> **② Minimum Viable Organization Check：第一天真正必须有什么**  
> **③ Open Questions / Experiment Backlog**  
> **④ 宣布 Operating Model v0.1 Final Design Baseline Frozen**

然后就停止内容设计。

等你回到电脑进入 Work，我们进入之前约定的：

> **Documentation Convergence → Obsidian + GitHub → Principle Tree → 模块原则页 → Panorama Topology → Interactive HTML Atlas → Specification 对齐。**

我建议现在直接从 **① Freeze Classification（冻结分类）** 开始。

---

## turn-243aed9d-52f6-4eb9-87ba-0a1fffa84432

时间：2026-09-06T21:57:27.723564+08:00

### Human

Message ID：`243aed9d-52f6-4eb9-87ba-0a1fffa84432`

你说 Freeze classification是啥意思？我有点没看懂。这个是我们现在就可以做，还是要我在电脑前面进入 Worker 模式下做

---

### Assistant

Message ID：`2b5b08ea-ce0b-4e2d-a065-f611b3702580`

这个**现在就在当前对话里做**，不需要你在电脑前，也不需要进入 Work。

我刚才用了一个有点工程化的名字。**Freeze Classification（冻结分类）**其实只是我们在正式说“v0.1设计完成”之前，把已经讨论的东西分成三种状态，避免以后别人把“已经确定的原则”和“我们暂时猜的参数”混在一起。

举个我们已经讨论过的例子就很好理解。

### 第一类：Frozen｜已经确定

例如：

> **Capability is guidance, not permission。**  
> 能力用于导航，不用于 Task 准入。

这不是我们准备上线以后看看效果再决定的东西，而是当前 Operating Model 的设计原则。

如果开发人员以后做成：

> “Capability Level 低于3禁止领取这个 Task。”

那不是“调参数”，而是**违反 v0.1 设计**。

类似还有：

> Task ≠ Execution。  
> 每个 Execution 唯一解析到一个 Human Accountable Owner。  
> Human保留最终 Goal Authority。  
> Protocol是共同语言，不是 Policy。  
> Free Work Space不被全面监控。

这些属于：

> **Frozen Design（冻结设计）。**

当然“冻结”不意味着永远不能改。只是以后要改，应该明确说：

> **我要修改 v0.1 的一个设计原则。**

而不是开发过程中悄悄改掉。

---

### 第二类：Tunable｜方向确定，但数值还不知道

例如我们已经确定：

> Material Change（实质变化）才应该强传播。

这是 Frozen。

但：

> **到底什么程度算 Material？**

我们现在其实不知道。

可能运行以后发现：

> Knowledge Scope变化10%不值得打扰；  
> 某些高风险 Knowledge哪怕变化很小也必须传播。

这应该通过真实运行调整。

所以：

> **“存在 Materiality Threshold”是 Frozen。**
>
> **“Threshold具体是多少”是 Tunable（可调参数）。**

类似：

> Cycle是一周还是一个月；  
> Agent多久没 Heartbeat进入 Degraded；  
> 一条 Contribution需要几个人盲评；

这些现在没必要拍脑袋决定。

---

### 第三类：Experimental / Open｜我们明确还不知道

比如：

> **Human Oversight到底能够被组织外化到什么程度？**

我们有一个很强的 Hypothesis：

> 很多 Human Oversight可以通过排序、Evidence、Hypothesis Cloud逐渐外化。

但到底：

> 30%？70%？95%？

我们不知道。

甚至某些 Judgment可能永远高度依赖 Human。

所以这个不能写成：

> “系统一定能够把Human Oversight完全外化。”

应该明确标记：

> **Open Question / Experiment（开放问题 / 实验项）。**

然后让60人的真实组织去告诉我们答案。

---

所以 Freeze Classification 实际上就是给当前设计贴三个标签：

> 🔒 **Frozen** —— 我们已经做出的设计决定。  
> 🎛️ **Tunable** —— 机制确定，参数等真实运行调整。  
> 🧪 **Experimental / Open** —— 我们现在不知道，必须通过实验学习。

它本身还是**设计收敛工作**，所以应该现在做。

等你回到电脑进入 Work，做的是另一件事情：

> 把我们现在确定的这些东西，与 Obsidian / GitHub 里的旧版本逐条对齐、修改文件、建立 Principle Tree、生成全景图和 HTML Atlas。

那叫 **Documentation Convergence（文档收敛）**。

所以我们现在继续做 Freeze Classification 是对的。完成它以后，再做 Minimum Viable Organization（最小可运行组织）检查，我们的**内容设计工作才算真正结束**。

---

## turn-d1b830a9-5fb2-4c05-871a-b73781b70505

时间：2026-09-06T21:58:06.930712+08:00

### Human

Message ID：`d1b830a9-5fb2-4c05-871a-b73781b70505`

OK，那你继续吧

---

### Assistant

Message ID：`2ef9dff8-23be-4c52-b02f-33852e10a00f`

好。现在做 **Operating Model v0.1 — Freeze Classification（冻结分类）**。

这一轮不再改变设计，只明确：**哪些已经决定、哪些机制确定但参数待调、哪些必须交给真实组织实验。**

# A. 🔒 Frozen Design｜冻结设计

这些构成 v0.1 Baseline（基线）。以后当然可以修改，但修改意味着正式改变设计，而不是“调参数”。

### 1. 原则体系

冻结：

> **11条 L1 Foundational Operating Principles**  
> **1条 Meta-design Principle**  
> **L2 Module Principles**  
> **L3 Mechanism Taxonomy（机制目录）**  
> **Cross-cutting Principle（横切原则）机制**

L3具体原则可以在文档收敛阶段从已有设计中提取，但不能在那里重新发明设计。

---

### 2. Organizational Reality Layer

冻结：

> One Organizational Reality  
> One Event Model, Many Event Types  
> Record Facts Once, Interpret Many Times  
> Event Graph = History  
> Dependency Graph = Current Dependency Structure  
> Granular Evolution（颗粒化演进）  
> Material Change（实质变化）才强传播  
> Change Set（变更集）聚合相关变化

以及：

> **Object + Event + Dependency**

作为共享现实的底层三元结构。

---

### 3. Goal

冻结：

> Human拥有最终 Goal Authority。  
> Goal描述 Desired Change，而不是 Workflow。  
> Goal包含 Success Criteria / Assumption / Scope / Boundary等可独立演进组件。  
> Task必须最终服务 Active Goal。  
> Task可服务多个 Goal，但有一个 Primary Goal。  
> Agent可以 Challenge Goal，不能自行修改 Goal。

---

### 4. Task / Execution

冻结最重要的区别：

> **Task ≠ Execution。**

Task：

> 组织希望解决的问题 / 共享契约。

Execution：

> 一个执行单元的一次真实尝试。

同时冻结：

> Parallel Execution允许。  
> Claim不意味着排他。  
> Capability不作为领取准入。  
> Dynamic Task Generation允许。  
> 但不能借 Derived Task偷偷扩大 Goal。  
> 每个 Execution唯一解析到 Human Accountable Owner。  
> Execution不能 Silent Failure。

---

### 5. Free Work Space

冻结：

> **组织治理 Contract，不治理 How。**

HAU内部：

> Private Agent  
> Workflow  
> 临时 Subtask  
> 草稿  
> 推理

默认属于 Free Work Space。

只有跨越明确组织边界：

> 才成为 Organizational Reality。

---

### 6. Review / Acceptance / Selection

冻结三者分离：

> **Review**：可信吗？  
> **Acceptance**：满足当前用途吗？  
> **Selection**：多个合格 Result 中采用哪个？

以及：

> Evidence Threshold follows Impact。

---

### 7. Organizational Learning & Knowledge

冻结：

> Experience ≠ Knowledge。  
> Knowledge = Claim + Evidence + Scope + Boundary。  
> Verification优先证伪。  
> 孤证不立。  
> Knowledge Quality ≠ Scope Size。  
> Store broadly, activate sparsely。  
> Inject cognition, not workflow。  
> Knowledge是网络，不是文档堆。  
> Knowledge支持组件级 Challenge。  
> Knowledge Pulse存在。  
> Broadcast ≠ Injection。  
> Global Awareness + Selective Interruption。

以及：

> **Knowledge ≠ Policy ≠ Protocol。**

---

### 8. Agent Governance & Runtime

冻结：

> One Human, One Active Representative Agent。  
> HAU = Human + Representative Agent。  
> Private Intelligence不进入中央治理。  
> Boundary内Agent默认自主。  
> Authority向下只能收紧。  
> Permission ≠ Capability。  
> Reliable = No Silent Failure。  
> Runtime Health = Active / Degraded / Suspended。  
> Organization-owned Agent必须进入Control Plane。  
> Kill Switch在Agent外部。  
> Handover = Context Reconstruction。  
> HAU Persistent State不属于某个临时Agent。

以及：

> **Context可以重建，Organizational Reality必须持久。**

---

### 9. Capability

冻结：

> Capability由Execution Evidence形成。  
> Capability是地图，不是等级。  
> Capability is guidance, not permission。  
> Expected Terrain ≠ Observed Terrain。  
> Execution同时可以测绘Actor和World。  
> Capture is not documentation; capture is reproducibility。  
> 第一次HAU成功就形成Organizational Capability Candidate。  
> Reproduction验证组织是否真正获得能力。  
> Human Oversight可以成为组织学习材料。  
> Capability关键Dependency变化后需要Revalidation。  
> Capability enables automation; it does not mandate automation。

---

### 10. Contribution / Reward / Honor / Achievement

冻结四套机制分离：

> **Contribution记录价值。**  
> **Reward分配现实价值。**  
> **Honor保存组织共同价值记忆。**  
> **Achievement记录HAU成长经历。**

冻结：

> 激励归属HAU。  
> Contribution看Impact，不看Activity。  
> Task Failure ≠ No Contribution。  
> Contribution first, valuation later。  
> Contribution主要来自共享事实，不靠员工自我申报。  
> Collective Valuation评价Contribution Event，不评价Human。  
> Blind where practical（尽可能盲评）。  
> Scarcity / Saturation作为价值Context。  
> Honor没有配额。  
> Honor纪念Event，不做Human排行榜。  
> Badge / Progression不产生Authority。

---

### 11. Governance / Risk / Audit

冻结：

> Governance = architecture of decision rights。  
> Governance exception-driven。  
> Authority follows the object。  
> Authority is scoped。  
> Accountability ≠ Unlimited Authority。  
> Risk Authority follows actual consequence bearing。  
> Unknown ≠ Dangerous。  
> 优先Risk Shaping，而不是禁止探索。  
> Hard Boundary不能由普通Risk Acceptance突破。  
> Policy Governance存在且与Protocol Governance分离。  
> Audit消费共享Organizational Reality，不建立自己的事实世界。  
> Audit保存authority-at-the-time。  
> Audit不监控私人思考。

---

### 12. Protocol

冻结我们最后形成的定义：

> **Protocol是组织共同语言、语义、状态表达和交互结构。**

不是：

> SOP / Policy / Knowledge。

所以：

> **Protocol fixed, workflow free。**

Protocol Change是低频基础设施变化。

---

# B. 🎛️ Tunable｜机制确定，参数待真实运行调整

这些东西**不要现在拍数字**。

包括：

> 一个 Cycle 是7天、14天还是30天。  
> 每个 Contribution Event需要多少盲评者。  
> Collective Valuation具体采用排序、分配100点还是其他形式。  
> Reward Pool每个 Cycle多大。  
> Scarcity / Saturation使用多长历史窗口。  
> Materiality Threshold具体怎么判断。  
> Knowledge需要多少 Evidence才形成较稳定 Claim。  
> Counter Evidence多强才触发强 Knowledge Pulse。  
> Heartbeat多久没有进入 Degraded。  
> Degraded多久进入 Suspended。  
> Capability什么时候要求 Revalidation。  
> Risk Shaping做到什么程度进入 Human。  
> Task Lease长度。  
> Progress Signal频率。  
> Parallel Task最多允许多少 Execution。  
> Task Bus推荐多少任务。  
> Knowledge Activation一次注入多少内容。

原则上：

> **Mechanism Frozen, Parameter Tunable。**

不要让开发阶段把“参数还没定”误认为“设计没完成”。

---

# C. 🧪 Experimental / Open｜必须让真实组织回答

这部分我认为尤其重要。

我们要公开承认：

> **这些问题现在不知道答案。**

### 1. Human Oversight到底能外化多少？

我们的 Hypothesis（假设）是：

> 很多 Human Judgment可以通过 Context + Human Ranking + Evidence + Outcome逐渐形成 Organizational Knowledge。

但：

> 极限在哪里？

不知道。

---

### 2. Organizational Capability什么时候真的可以自动执行？

我们知道需要：

> Reproducibility  
> Risk可接受  
> Boundary清楚  
> Oversight Need低

但：

> 什么组合才真正足够？

必须实验。

---

### 3. Capability Map最终会长成什么维度？

第一天可以有Seed Terrain。

但真实组织可能发现：

> 我们今天想的很多“能力维度”根本不重要。

真正重要的 Terrain Dimension应该从Execution长出来。

---

### 4. Collective Valuation长期会产生什么社会行为？

Blind Valuation和Scarcity Signal能降低一部分偏差。

但会不会产生：

> 新型联盟；  
> 战略性评价；  
> 群体审美偏差；  
> 某种组织文化极化？

不知道。

必须观察。

---

### 5. Knowledge Pulse会不会产生Attention Overload？

我们的设计：

> Global Awareness + Selective Interruption

理论上合理。

但真实60个HAU运行以后：

> 一天多少Pulse才开始变成噪音？

不知道。

---

### 6. Contribution Ontology最终会长成什么？

现在只有：

> Result / Learning / Capability / Protection / Enablement + Emerging。

半年以后也许发现：

> 第六、第七种非常重要的Contribution。

应该允许它长出来。

---

### 7. Progression是否真的需要等级？

Bronze / Silver / Gold目前只是产品想象。

也许真实运行后：

> Badge Wall + Capability Map已经足够。

那么根本不需要Level。

所以：

> **Progression System存在的可能性已定义，但等级机制仍然Experimental。**

---

### 8. Honor最终会形成怎样的文化？

我们知道 Honor保存：

> 组织希望未来成员记住的行为。

但：

> 60个新人最终会共同选择记住什么？

我们不应该提前知道。

这恰恰是实验最有价值的输出之一。

---

### 9. Organization-owned Agent规模扩大后的责任模型

v0.1暂时：

> Execution沿Task / Primary Goal / Organizational Function解析到Human。

当自动Execution变成：

> 每天几万次，

单Execution Accountability是否仍然合理？

现在不知道。

等真正发生再升级。

---

### 10. Organizational Value Model会不会自然稳定？

多个Cycle Collective Valuation以后：

> 大家对“什么有价值”的判断会不会逐渐收敛？

或者：

> 永远随Goal / 环境变化？

这是一个非常有意思的实验问题。

---

# 一个很重要的结果

这样我们就不会犯两种相反的错误。

第一种：

> **“还有10个Open Question，所以设计没完成。”**

不对。

这些问题本来就应该通过运行回答。

第二种：

> **“v0.1已经冻结，所以我们什么都知道了。”**

也不对。

我们的 Meta Principle 恰恰要求：

> **Seed lightly, observe deeply, formalize late。**

所以一个好的 v0.1 Baseline，本来就应该明确知道：

> **什么已经决定，什么可以调，什么我们现在不知道。**

---

## Freeze Classification：完成

现在状态可以正式标记：

> 🔒 **Core Operating Model — Frozen for v0.1**  
> 🎛️ **Operational Parameters — Tunable**  
> 🧪 **Behavioral / Organizational Hypotheses — Experimental**

下一步就是我们冻结前的最后一个检查：

# Minimum Viable Organization
**最小可运行组织检查**

问题会非常实际：

> **如果明天60个新人真的进入这个系统，我们现在设计的几十个机制中，哪些必须第一天就存在；哪些可以第二阶段再实现；哪些甚至应该故意晚一点做，让组织先产生干净的实验数据？**

这一步会第一次把：

> **Operating Model Design**

和：

> **Implementation / Launch Scope**

真正分开。

---

## turn-928216ea-1697-4534-bc99-bb116fd440e0

时间：2026-09-06T22:00:43.501488+08:00

### Human

Message ID：`928216ea-1697-4534-bc99-bb116fd440e0`

继续吧

---

### Assistant

Message ID：`5c736ddb-59b4-4d04-8d49-bc3b1d0d3d6f`

好。现在进入冻结前最后一个检查：

# Minimum Viable Organization
**最小可运行组织检查**

这里我们第一次不问：

> “完整 Operating Model 应该有什么？”

而问：

> **“假设明天60个新人真的进入组织，最少实现什么，这个组织就已经能够按照我们的核心原则真实运行？”**

这很重要，因为：

> **Design Baseline ≠ Launch Scope。**

Operating Model v0.1 可以完整定义 Knowledge Pulse、Capability Capture、Honor、Organization-owned Agent 等机制，但并不意味着第一天必须把它们全部开发完成。

我建议把实现分成三层：

> **M0 — Day-One Critical：没有就跑不起来。**  
> **M1 — Learning Critical：可以先跑，但很快必须有，否则组织不会学习。**  
> **M2 — Scaling / Experience：等真实行为出现以后再建设反而更好。**

---

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

## 现在只剩最后一个设计收尾动作

我们已经完成：

> Freeze Classification ✓  
> Minimum Viable Organization ✓

所以最后应该做的是：

# Open Questions / Experiment Backlog
**开放问题与实验清单**

不是再列一遍刚才10个 Experimental问题。

而是把它们转成：

> **我们第一年到底要通过这个60人组织验证哪些 Hypothesis（假设）？**

例如：

> “HAU第一次成功后，组织能否通过结构化Capture让另一支HAU复现？”  
> “Blind Collective Valuation能否比传统Manager奖金分配形成不同的价值文化？”  
> “Human Oversight能否通过排序+Evidence逐渐外化？”  
> “Capability-based Task Discovery是否真的会让新人主动挑战能力边界？”

这会把整个项目从：

> **一个组织软件设计**

进一步变成：

> **一个可验证的 AI-native Organization Experiment（AI原生组织实验）。**

完成这份 Experiment Backlog以后，我认为内容设计就可以正式冻结。

---

## turn-860d970e-8597-42ae-9ae4-f499e94ff4a4

时间：2026-09-06T22:27:54.227610+08:00

### Human

Message ID：`860d970e-8597-42ae-9ae4-f499e94ff4a4`

同意

---

### Assistant

Message ID：`80616822-0282-41b4-a5f1-8251865317a8`

好。那我们做内容设计阶段最后一项：

# Operating Model v0.1 — Experiment Backlog
**第一年实验假设清单**

这份清单不是“还没设计完的功能”。它回答的是：

> **我们建立这套60人 AI-native Organization，究竟有哪些重要问题只能靠真实运行才能得到答案？**

我建议把第一年的实验集中在 **8 个核心 Hypothesis（假设）**，不要一开始搞几十项研究指标。

---

## E01 — HAU 是否真的比 Human / Agent 单独作为组织单元更有效？

### Hypothesis

> **Human + Representative Agent 形成稳定 HAU 后，可以成为比“Human使用AI工具”更稳定的组织基本单元。**

我们要观察：

> Representative Agent 是否逐渐真正“认识”自己的 Human；  
> HAU Persistent State 是否让换 Agent 后仍然保持连续性；  
> Human 与 Agent 是否形成稳定分工；  
> HAU 是否出现明显不同的行为风格和能力轨迹。

真正的问题是：

> **HAU 到底只是我们人为定义的概念，还是运行以后真的会成为一种可观察的组织生命单元？**

---

# E02 — Default Autonomy 是否真的优于传统派工与审批？

### Hypothesis

> **在明确 Boundary 下给予 HAU / Agent 默认自主权，可以在不显著增加组织风险的情况下，提高探索速度和组织适应性。**

我们观察：

>多少 Execution 在没有 Manager干预下正常闭环；  
>多少需要 Escalation；  
>Boundary Request发生在哪里；  
>Silent Failure是否减少；  
>Human到底需要在哪些 Decision真正出现。

最终可能发现：

> 我们给 Agent的 Boundary太宽，

也可能：

> 其实远比今天想象得还可以放权。

这应该让现实回答。

---

# E03 — 赏金酒馆式 Task Discovery 是否成立？

### Hypothesis

> **当 Capability 只提供导航、不限制领取，而且同一 Task允许 Parallel Execution 时，新人会主动探索超出自己历史能力的工作，而组织不会因此承担不可接受的失败成本。**

我们观察：

> 新人会不会领取明显超出自己 Capability Map 的 Task；  
> Parallel Execution会不会提高最终 Result质量；  
> 会不会产生大量无意义重复；  
> 失败者是否真的带回 Terrain / Learning；  
> HAU会不会逐渐形成不同探索路径。

这是我们整个“新手村 + 战争迷雾”模型非常核心的实验。

---

# E04 — Task 能否真正成为组织探索世界的 Probe？

### Hypothesis

> **结构化 Task Return 能让每一次 Execution 不只是产生 Result，还持续测绘真实 Terrain。**

我们要验证：

> Expected Terrain 和 Observed Terrain 是否真的经常不同；  
> 哪些 Terrain Dimension 最终有预测价值；  
> Failure能不能产生稳定的 Terrain Evidence；  
> 系统能否从多个 Execution逐渐发现 Capability Gap；  
> Dynamic Task Generation是否真的从这些 Gap自然长出来。

这项实验最终甚至会告诉我们：

> **Capability Map 应该长成什么样。**

所以不要第一天把地图设计死。

---

# E05 — 一个 HAU 的成功能否快速变成 Organizational Capability？

这可能是整个实验**最核心的 Hypothesis之一**。

> **如果一个 HAU能够完成一项 Task，那么通过捕获 Knowledge、Data、Tool、Agent Configuration、Runtime、Practice、Review和Human Oversight，组织应该能够让另一支 HAU复现这项能力。**

我们真正测试：

> 第一次成功以后能捕获多少？  
> 第二支 HAU拿到 Capability Package能不能理解？  
> 能不能迁移？  
> 能不能复现？  
> 失败到底缺 Knowledge、Tool还是Human Judgment？

最终形成：

> **Experience → Knowledge → Teachable → Transferable → Reproducible → Organizational Capability**

如果这条链真的成立：

> **一个人的成功，就可能成为整个组织的永久能力增长。**

这是非常重要的实验。

---

# E06 — Human Oversight 能否被组织学习？

这是另一个核心实验。

### Hypothesis

> **Human很多看似Tacit（隐性）的监督判断，可以通过 Context + Candidate Reasons + Human Ranking + Outcome + Evidence逐渐外化。**

我们不要求 Human写长篇：

> “为什么我觉得这里不对？”

AI提出：

> A / B / C可能原因。

Human：

> 排序 + 必要时补充。

长期：

> Hypothesis Cloud逐渐收敛。

我们观察：

> 哪类 Oversight容易外化；  
> 哪类始终高度依赖Human；  
> 外化以后能否教给其他Human；  
> 能否最终降低某类Task的Human Oversight需求。

这会真正回答：

> **Human Judgment到底有多少能够成为 Organizational Capability。**

---

# E07 — Organizational Learning 能否形成真正的“集体大脑”？

### Hypothesis

> **一个 HAU产生的新 Knowledge，可以通过 Organizational Memory、Activation、Dependency和Knowledge Pulse成为其他 HAU的潜在认知资产，而不造成严重Context / Attention Overload。**

观察：

> Knowledge被多少其他 HAU真正使用；  
> Knowledge是否提高后续 Execution成功率；  
> Knowledge Challenge是否能及时影响正在依赖它的 Execution；  
> Pulse是否产生噪音；  
> Teachability是否能够预测实际Transferability。

最终回答：

> **我们是在建设一个更好的文档库，还是组织真的形成了跨Human的认知系统？**

---

# E08 — Contribution / Reward / Honor 能否让组织自己长出价值观？

### Hypothesis

> **如果先记录真实 Contribution，再通过 Blind Collective Valuation和Scarcity / Saturation Context分配Reward，而Honor独立保存共同记忆，组织可以逐渐形成比预设KPI更真实的Organizational Value Model。**

我们观察：

> 大家最初奖励什么；  
> 三个月后是否变化；  
> Result / Learning / Protection / Enablement的相对价值如何变化；  
> 是否出现串票；  
> Blind Valuation能否降低人情影响；  
> Scarcity Signal能否防止所有人追逐同一种行为；  
> Honor最终保存了怎样的故事。

这实际上是在验证：

> **组织文化能不能从真实价值判断中生长，而不是从墙上的价值观标语中产生。**

---

# 这8项实验其实可以归成4个更大的研究问题

### A. Human + Agent

> **HAU是不是真正的新型组织基本单元？**

对应：

> E01 / E02 / E06

### B. Exploration + Capability

> **组织能不能通过真实工作探索未知，并把个人成功变成组织能力？**

对应：

> E03 / E04 / E05

### C. Organizational Intelligence

> **组织能不能形成一个超越单个Human / Agent的持续学习系统？**

对应：

> E06 / E07

### D. Organizational Culture

> **价值观和文化能不能从真实Contribution与共同选择中自然形成？**

对应：

> E08

---

# 一个非常重要的实验原则

我建议给整个 Experiment Backlog 加一条规则：

> **Do not optimize the experiment before observing the baseline.**
>
> **在看到基线行为之前，不要急着优化实验。**

比如第一批人进入以后发现：

> Task Claim率很低。

不要第二天马上：

> 增加Badge + 奖金 + AI推荐 + Push Notification。

否则我们永远不知道：

> **原始机制到底会产生什么行为。**

应该先观察一个足够短但有意义的 Baseline Period（基线期），然后才改变机制。

每一次重要机制改变：

> 作为 Policy / Product Change Event记录。

这样我们以后才能知道：

> **行为变化到底是组织自然成长，还是因为我们改了规则。**

这对一个真正的实验非常重要。

---

# Operating Model v0.1 — 内容设计状态

到这里，我们已经完成：

> **8个业务模块 + 1个Reality Layer**  
> **两轮模块收敛**  
> **7轮端到端 / 异常压力测试**  
> **11+1 L1 Principles**  
> **完整L2 Principle Tree**  
> **L3 Mechanism Taxonomy**  
> **Cross-cutting Principles结构**  
> **Freeze Classification**  
> **Minimum Viable Organization：M0 / M1 / M2**  
> **8项第一年核心Experiment Hypotheses**

因此我认为现在可以正式标记：

# Operating Model v0.1 — Final Design Baseline
**内容设计冻结。**

“冻结”不意味着以后不能改变，而是从现在开始：

> 新灵感不再直接改 Baseline；  
> 先作为 Evidence / Hypothesis / Change Proposal；  
> 经过验证以后再决定进入 v0.1 Revision 或 v0.2。

这样我们自己也开始按照刚刚设计出来的组织原则工作：

> **不因为每出现一个新想法，就推翻整个设计。**

你回到电脑以后，下一阶段就是我们已经约定的 **Documentation Convergence**：读取 Obsidian + GitHub 当前项目，把旧设计与这个 Final Design Baseline 对齐，然后建立 Principle Tree、模块原则页、Panorama Topology（全景图拓扑）和最终 Interactive HTML Atlas（交互式组织图谱）。

---

