# Experiment Backlog v0.1

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 860d970e](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-860d970e-8597-42ae-9ae4-f499e94ff4a4)。

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


## 证据登记规则

E01–E08当前均为待运行验证的Hypothesis；样本、观察窗口、基线结果、干预记录、实际Outcome、反证及结论均未填实测值。本次不生成模拟数据。每次重要机制改变记录Policy/Product Change Event，先观察基线再优化。
