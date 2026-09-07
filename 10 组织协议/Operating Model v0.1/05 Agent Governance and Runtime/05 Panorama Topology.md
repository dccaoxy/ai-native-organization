# 05 Panorama Topology

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 a1b56a80](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-a1b56a80-1808-4234-93ff-c64181be2df9) · [源文 9905dc6e](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-9905dc6e-cc09-45f8-8b64-94e95f015a7a) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

本页是设计信息拓扑，不是正在运行的实例图。节点ID为文档定位，箭头类型区别流程、事实、依赖、约束与授权。

## 节点

| ID | 节点 |
|---|---|
| 05-N01 | Human |
| 05-N02 | HAU Persistent State |
| 05-N03 | Representative Agent |
| 05-N04 | Private Agents |
| 05-N05 | Effective Runtime Envelope |
| 05-N06 | Execution |
| 05-N07 | Control Plane |
| 05-N08 | Context Reconstruction |

## 必需关系

| 起点 | 关系 | 终点 |
|---|---|---|
| 05-N01 | one-active-binding | 05-N03 |
| 05-N01 | persistent-unit | 05-N02 |
| 05-N03 | bounded-interface-not-fixed-management | 05-N04 |
| 05-N05 | constrains | 05-N06 |
| 05-N07 | governs-authority | 05-N03 |
| 05-N02 | rebuild | 05-N08 |
| 05-N08 | handover | 05-N03 |
| 05-N03 | represents | 05-N06 |

## 跨模块接口

- [00 持久事实与依赖历史](../00%20Organizational%20Reality/00%20README.md)
- [01 Human 目的权](../01%20Goal/01%20README.md)
- [02 Execution 责任与可靠回应](../02%20Task%20and%20Execution/02%20README.md)
- [03 自由工作边界](../03%20Free%20Work%20Review%20Acceptance/03%20README.md)
- [04 激活与 Policy 分离](../04%20Learning%20and%20Knowledge/04%20README.md)
- [07 HAU 资产连续性](../07%20Contribution%20Reward%20Honor%20Achievement/07%20README.md)
- [08 授权与外部停权](../08%20Governance%20Risk%20Audit/08%20README.md)

## 下钻

[Mechanism](05%20Mechanisms.md) → [对象/状态/交互规格](05%20Specification.md) → [原文证据](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)。全局返回：[Global Panorama](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Global%20Panorama%20Topology%20v0.1.md)。
