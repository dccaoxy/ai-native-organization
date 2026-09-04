# Knowledge→Behavior：Behavioral Authority

> 状态：当前有效设计；治理未冻结；整体版本未指定。
> 基线同步日期：2026-09-04；来源：[[DESIGN-ISSUE-001 基线同步裁决]]。

| Behavioral Authority | 当前有效规则 |
|---|---|
| Inform | 提供信息 |
| Recommend | 可 Ignore |
| Default | 可 Override，并形成 Learning Signal |
| Mandatory | 仅经授权突破，并审计 |

升级同时考虑 Epistemic Strength、Behavioral Value、Failure Cost。Default 应远多于 Mandatory；认知可信程度不自动等于行为强制程度。

下一问题：由谁治理晋升？本次不指定尚未裁决的晋升角色、审批链或阈值，也不把这部分标记为冻结 Protocol。

关联：[[organizational-memory]] · [[Agent Governance & Runtime]] · [[Organization Runtime & Protocol OTA]]

## 当前主线边界

Behavioral Authority 与 Epistemic Strength、Memory Salience 分开；需平衡 Exploration vs Exploitation。四级行为权力为当前有效设计，但晋升主体、证据门槛、审批、版本、降级与回滚尚未冻结。

[[Knowledge Intervention v0.1]] 的 L0 Observe / L1 Inform / L2 Recommend / L3 Default-Protocol 是实验干预框架，不能与行为权力层级混用数字编号。

原始讨论 `84c44fd9-d4d1-4efb-8c81-63440feaaddd` 中的收益百分比和 Agent 数量为说明示例，非实测或确定阈值。该轮 WIP 示例不自动撤销 [[Task Protocol v0.1]] 已冻结的第一阶段默认 WIP=1；如需更改其权限等级，应单独裁决。

关联：[[Knowledge Usage Feedback]] · [[Governance Audit Risk 待设计]] · [[Free Work Space Protocol v0.1]] · [[探讨AI原生组织-raw-conversation]]。
