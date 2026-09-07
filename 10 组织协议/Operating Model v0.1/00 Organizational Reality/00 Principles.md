# 00 Principles

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

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

L3：[机制原则](00%20Mechanisms.md)。横切适用见 [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md)。
