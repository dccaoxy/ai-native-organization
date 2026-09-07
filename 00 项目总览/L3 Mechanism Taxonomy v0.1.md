# L3 Mechanism Taxonomy v0.1

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](Principle%20Tree%20v0.1.md) · [来源索引](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 ec3cb0fa](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

本页只维护机制分类、名称与正文链接；详细原则仅在各模块 Mechanisms 页面维护。

机制名称按冻结原文保留。Mxx-L3-xx 为本次文档索引 ID；详细原则从模块第一轮、Pass 2与最终冻结分类提取，不为每个机制凑固定条数。


## 00 Organizational Reality

- [M00-L3-01 Event Model](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md#m00-l3-01-event-model)
- [M00-L3-02 Event Graph](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md#m00-l3-02-event-graph)
- [M00-L3-03 Dependency Graph](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md#m00-l3-03-dependency-graph)
- [M00-L3-04 Materiality Detection](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md#m00-l3-04-materiality-detection)
- [M00-L3-05 Change Set](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md#m00-l3-05-change-set)
- [M00-L3-06 Object Versioning / Granular Evolution](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md#m00-l3-06-object-versioning--granular-evolution)

## 01 Goal

- [M01-L3-01 Goal Formation / Activation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/01%20Goal/01%20Mechanisms.md#m01-l3-01-goal-formation--activation)
- [M01-L3-02 Goal Challenge & Revision](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/01%20Goal/01%20Mechanisms.md#m01-l3-02-goal-challenge--revision)
- [M01-L3-03 Goal Dependency / Impact Propagation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/01%20Goal/01%20Mechanisms.md#m01-l3-03-goal-dependency--impact-propagation)

## 02 Task and Execution

- [M02-L3-01 Task Formation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md#m02-l3-01-task-formation)
- [M02-L3-02 Task Discovery / Bounty Tavern](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md#m02-l3-02-task-discovery--bounty-tavern)
- [M02-L3-03 Claim & Execution Creation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md#m02-l3-03-claim--execution-creation)
- [M02-L3-04 Parallel Execution](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md#m02-l3-04-parallel-execution)
- [M02-L3-05 Dynamic Task Generation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md#m02-l3-05-dynamic-task-generation)
- [M02-L3-06 Execution State / ACK / Progress](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md#m02-l3-06-execution-state--ack--progress)
- [M02-L3-07 Task Return / Expedition Report](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md#m02-l3-07-task-return--expedition-report)

## 03 Free Work Review Acceptance

- [M03-L3-01 Free Work Boundary](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md#m03-l3-01-free-work-boundary)
- [M03-L3-02 Progress Reporting](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md#m03-l3-02-progress-reporting)
- [M03-L3-03 Result Submission](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md#m03-l3-03-result-submission)
- [M03-L3-04 Review](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md#m03-l3-04-review)
- [M03-L3-05 Acceptance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md#m03-l3-05-acceptance)
- [M03-L3-06 Parallel Result Selection](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md#m03-l3-06-parallel-result-selection)

## 04 Learning and Knowledge

- [M04-L3-01 Experience Capture](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-01-experience-capture)
- [M04-L3-02 Observation / Pattern Formation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-02-observation--pattern-formation)
- [M04-L3-03 Hypothesis Cloud](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-03-hypothesis-cloud)
- [M04-L3-04 Verification / Falsification](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-04-verification--falsification)
- [M04-L3-05 Knowledge Formation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-05-knowledge-formation)
- [M04-L3-06 Knowledge Challenge & Granular Revision](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-06-knowledge-challenge--granular-revision)
- [M04-L3-07 Knowledge Activation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-07-knowledge-activation)
- [M04-L3-08 Knowledge Pulse](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-08-knowledge-pulse)
- [M04-L3-09 Teachability / Transferability](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md#m04-l3-09-teachability--transferability)

## 05 Agent Governance and Runtime

- [M05-L3-01 Representative Agent Registration / Binding](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-01-representative-agent-registration--binding)
- [M05-L3-02 HAU Persistent State](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-02-hau-persistent-state)
- [M05-L3-03 Human Model](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-03-human-model)
- [M05-L3-04 Organization Model](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-04-organization-model)
- [M05-L3-05 Runtime / Effective Runtime Envelope](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-05-runtime--effective-runtime-envelope)
- [M05-L3-06 Policy Propagation to Private Agents](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-06-policy-propagation-to-private-agents)
- [M05-L3-07 Boundary Extension](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-07-boundary-extension)
- [M05-L3-08 Reliability Signals](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-08-reliability-signals)
- [M05-L3-09 Runtime Health](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-09-runtime-health)
- [M05-L3-10 Handover / Context Reconstruction](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-10-handover--context-reconstruction)
- [M05-L3-11 Organization-owned Agent](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-11-organization-owned-agent)
- [M05-L3-12 Agent Control Plane / Kill Switch](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md#m05-l3-12-agent-control-plane--kill-switch)

## 06 Capability

- [M06-L3-01 Expected Terrain Generation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-01-expected-terrain-generation)
- [M06-L3-02 Task Return → Capability / Terrain Evidence](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-02-task-return--capability--terrain-evidence)
- [M06-L3-03 HAU Capability Map](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-03-hau-capability-map)
- [M06-L3-04 Organizational Capability Map](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-04-organizational-capability-map)
- [M06-L3-05 Human Oversight Map](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-05-human-oversight-map)
- [M06-L3-06 Capability Capture](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-06-capability-capture)
- [M06-L3-07 Capability Package](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-07-capability-package)
- [M06-L3-08 Reproduction](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-08-reproduction)
- [M06-L3-09 Revalidation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-09-revalidation)
- [M06-L3-10 Capability Gap Discovery](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-10-capability-gap-discovery)
- [M06-L3-11 Exploration / Reproduction Task Generation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-11-exploration--reproduction-task-generation)
- [M06-L3-12 Capability-based Auto Execution](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md#m06-l3-12-capability-based-auto-execution)

## 07 Contribution Reward Honor Achievement

- [M07-L3-01 Contribution Detection](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-01-contribution-detection)
- [M07-L3-02 Contribution Ledger](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-02-contribution-ledger)
- [M07-L3-03 Downstream Impact](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-03-downstream-impact)
- [M07-L3-04 Cycle Collective Valuation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-04-cycle-collective-valuation)
- [M07-L3-05 Blind Event Valuation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-05-blind-event-valuation)
- [M07-L3-06 Scarcity / Saturation Signal](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-06-scarcity--saturation-signal)
- [M07-L3-07 Reward Pool Allocation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-07-reward-pool-allocation)
- [M07-L3-08 Honor Candidate Detection](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-08-honor-candidate-detection)
- [M07-L3-09 Honor Curation / Honor Story](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-09-honor-curation--honor-story)
- [M07-L3-10 Progression](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-10-progression)
- [M07-L3-11 Achievement / Badge](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md#m07-l3-11-achievement--badge)

## 08 Governance Risk Audit

- [M08-L3-01 Authority Registry](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-01-authority-registry)
- [M08-L3-02 Governance Routing](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-02-governance-routing)
- [M08-L3-03 Risk Expression / Risk Object](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-03-risk-expression--risk-object)
- [M08-L3-04 Consequence Routing](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-04-consequence-routing)
- [M08-L3-05 Risk Shaping](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-05-risk-shaping)
- [M08-L3-06 Residual Risk Acceptance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-06-residual-risk-acceptance)
- [M08-L3-07 Hard Boundary](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-07-hard-boundary)
- [M08-L3-08 Boundary Extension Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-08-boundary-extension-governance)
- [M08-L3-09 Policy Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-09-policy-governance)
- [M08-L3-10 Protocol Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-10-protocol-governance)
- [M08-L3-11 Foundational Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-11-foundational-governance)
- [M08-L3-12 Audit Reconstruction](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-12-audit-reconstruction)
- [M08-L3-13 Change Set Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md#m08-l3-13-change-set-governance)
