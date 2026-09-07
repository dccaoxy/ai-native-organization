# Knowledge Injection 与同步边界

> 2026-09-07：本页保留有效子机制细则。整体当前基线见 [04完整规格](Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Specification.md)；行为强度治理见 [08 Policy Governance](Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Specification.md)。知识不晋级为Protocol，认知/显著性/行为权力分离，更新按组件及实质依赖传播。下文未定字段、算法与参数不等于核心设计未冻结。


> 状态：核心架构原则已确认；接口与版本实现待设计。

**Inject cognition, not workflow｜注入认知，不注入流程。** 默认提供 Claim + Scope + Boundary + Epistemic Status，必要时动态给出 Implication / Caution。不能借知识注入规定“第一步、第二步”；更强行为约束必须经过 Governance。

| 同步通道 | 行为 |
|---|---|
| Claim Push | Task Claim / ACK 时提供 Task Contract 与少量 Knowledge Context Package |
| Checkpoint Delta Push | Progress / Checkpoint 后检查 Context 是否实质变化；无变化不注入，有变化才增量传递相关知识 |
| On-demand Pull | Human / Agent 在工作中主动查询组织记忆，按需下钻 |

中央系统不假装持续看见分布式 Free Work Space 的每一步。Knowledge 传递是 Event-driven；具体增量条数是示例，不冻结硬编码配额。

Knowledge Query Trigger 写入 Organization Runtime 的交互义务与当前配置：不确定问题、重要 Decision、异常/Retry/Review Fail、改变工具/并发/方法、Scope 高度相关、Human 明确查询历史经验。触发义务须可执行、可报告，不能只靠模型自己想起。

Protocol OTA同步共同语言与交互结构版本；Policy Update同步经授权的当前规则与Boundary；Knowledge走contextual Push/Pull。三者分离，普通Knowledge更新不自动成为Policy或Protocol发布。

关联：[[Context Assembly v0.1]] · [[Organization Runtime & Protocol OTA]] · [[Agent Governance & Runtime]] · [[Task Lease & Progress Protocol v0.1]]
来源：[[探讨AI原生组织-raw-conversation]]（主设计对话，2026-09-04 阶段同步）。
