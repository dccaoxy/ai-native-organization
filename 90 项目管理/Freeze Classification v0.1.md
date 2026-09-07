# Freeze Classification v0.1

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 d1b830a9](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-d1b830a9-5fb2-4c05-871a-b73781b70505)。

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


## 使用规则

Frozen、Tunable、Experimental 是设计确定性维度；M0/M1/M2 是实现优先级；运行/验证状态另列。不能互相替代。
