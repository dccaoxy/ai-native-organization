# Principle Tree v0.1

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](Principle%20Tree%20v0.1.md) · [来源索引](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 ec3cb0fa](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579) · [源文 85b640cd](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-85b640cd-b88d-4d2b-b822-991ab50aa8d2)。

L1、101条模块L2与79项L3机制目录已冻结；L3详细原则在本轮从既有设计提取。META-01是设计方法，不是第十二条日常运行原则。

[11+1 L1 完整措辞](Foundational%20Principles%20v0.1.md) · [L3机制目录与详细原则](L3%20Mechanism%20Taxonomy%20v0.1.md)

| 模块 | L2条数 | L3项数 | 入口 |
|---|---:|---:|---|
| 00 Organizational Reality | 8 | 6 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Principles.md) |
| 01 Goal | 9 | 3 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/01%20Goal/01%20Principles.md) |
| 02 Task and Execution | 11 | 7 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Principles.md) |
| 03 Free Work Review Acceptance | 11 | 6 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Principles.md) |
| 04 Learning and Knowledge | 13 | 9 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Principles.md) |
| 05 Agent Governance and Runtime | 12 | 12 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Principles.md) |
| 06 Capability | 12 | 12 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Principles.md) |
| 07 Contribution Reward Honor Achievement | 12 | 11 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Principles.md) |
| 08 Governance Risk Audit | 13 | 13 | [原则正文](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Principles.md) |

## Cross-cutting / Applies To

树表达主属关系，Applies To表达横切适用，不复制一套有独立版本的同义原则。以下对应是对冻结语义的文档整理，非新增L1。

| 主属原则 | 适用范围 |
|---|---|
| AGENT-07 No Silent Failure | 02 Execution、05 Runtime |
| WORK-09 Evidence threshold follows impact | 03 Review、04 Verification、08 Risk |
| REALITY-05/06 最小组件质疑与选择性传播 | Goal、Knowledge、Capability、Policy、Human Model |
| AGENT-05 权限委托只能保持或收紧 | 01 Goal Boundary、02 Execution、05 Runtime、08 Governance |
| WORK-11 正式组织边界 | 00 Reality、03 Free Work、04 Experience、05 Control Plane、08 Audit |
| VALUE-11 共享事实的价值解释 | 00 Event、02 Execution、04 Knowledge、06 Capability、07 Contribution |

Hypothesis Cloud 为共享推理构件，可由 Knowledge、Oversight、Root Cause、Risk与Failure Analysis使用。

## 00 Organizational Reality

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

## 01 Goal

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

## 02 Task and Execution

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

## 03 Free Work Review Acceptance

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

## 04 Learning and Knowledge

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

## 05 Agent Governance and Runtime

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

## 06 Capability

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

## 07 Contribution Reward Honor Achievement

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

## 08 Governance Risk Audit

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
