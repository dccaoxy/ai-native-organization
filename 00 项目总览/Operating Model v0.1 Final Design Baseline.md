# Operating Model v0.1 — Final Design Baseline

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](Principle%20Tree%20v0.1.md) · [来源索引](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 860d970e](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-860d970e-8597-42ae-9ae4-f499e94ff4a4) · [源文 d1b830a9](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-d1b830a9-5fb2-4c05-871a-b73781b70505) · [源文 ec3cb0fa](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## 阅读顺序

[11+1基础原则](Foundational%20Principles%20v0.1.md) → [Principle Tree](Principle%20Tree%20v0.1.md) → [全局拓扑](Global%20Panorama%20Topology%20v0.1.md) → 模块Purpose/Principles/Mental Model/Panorama/Specification → 机制与来源。

## 00 + 01–08

- [00 Organizational Reality](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20README.md)
- [01 Goal](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/01%20Goal/01%20README.md)
- [02 Task and Execution](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20README.md)
- [03 Free Work Review Acceptance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20README.md)
- [04 Learning and Knowledge](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20README.md)
- [05 Agent Governance and Runtime](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20README.md)
- [06 Capability](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20README.md)
- [07 Contribution Reward Honor Achievement](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20README.md)
- [08 Governance Risk Audit](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20README.md)

## 设计、上线与实验

- [Frozen/Tunable/Experimental](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Freeze%20Classification%20v0.1.md)
- [M0/M1/M2](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Minimum%20Viable%20Organization%20v0.1.md)
- [E01–E08实验](../20%20%E7%A0%94%E7%A9%B6%E8%AE%AE%E9%A2%98/Experiment%20Backlog%20v0.1.md)
- [统一术语](%E6%9C%AF%E8%AF%AD%E8%A1%A8%20v0.1.md)
- [79项机制](L3%20Mechanism%20Taxonomy%20v0.1.md)
- [来源与原文](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)
- [版本状态](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/%E8%AE%BE%E8%AE%A1%E7%8A%B6%E6%80%81%E4%B8%8E%E7%89%88%E6%9C%AC.md)
- [下一步](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/next-actions.md)

新灵感不直接改基线，先记录Evidence/Hypothesis/Change Proposal，再决定v0.1 Revision或v0.2。当前是文档设计基线，非运行系统验收。
