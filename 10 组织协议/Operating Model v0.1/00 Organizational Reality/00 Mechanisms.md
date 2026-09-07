# 00 L3 Mechanisms

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## M00-L3-01 Event Model

统一 Organizational Event 基础模型与 Envelope，允许多个 Event Type；不得按业务模块另造事实世界。

[完整对象、边界与交互规格](00%20Specification.md)；[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## M00-L3-02 Event Graph

记录历史事实及事件联系；历史原则上不可覆盖，解释可在各模块演进。

[完整对象、边界与交互规格](00%20Specification.md)；[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## M00-L3-03 Dependency Graph

只表达 Material Reliance；关联或看过不自动成为 Dependency，当前依赖变化保留历史。

[完整对象、边界与交互规格](00%20Specification.md)；[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## M00-L3-04 Materiality Detection

高频 Evidence 不等于强响应；足以改变有效 Claim/Scope/Boundary/Decision 时才产生 Material Change，参数不预定。

[完整对象、边界与交互规格](00%20Specification.md)；[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## M00-L3-05 Change Set

以共同根因或变化上下文聚合相关事件用于治理，不替代底层 Event。

[完整对象、边界与交互规格](00%20Specification.md)；[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## M00-L3-06 Object Versioning / Granular Evolution

质疑最小有意义组件，保留 Version/Delta/Reason/Evidence，沿依赖选择性传播。

[完整对象、边界与交互规格](00%20Specification.md)；[源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。
