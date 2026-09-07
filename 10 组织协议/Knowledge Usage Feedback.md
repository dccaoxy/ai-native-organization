# Knowledge Usage Feedback

> 2026-09-07：本页保留有效子机制细则。整体当前基线见 [04完整规格](Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Specification.md)；行为强度治理见 [08 Policy Governance](Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Specification.md)。知识不晋级为Protocol，认知/显著性/行为权力分离，更新按组件及实质依赖传播。下文未定字段、算法与参数不等于核心设计未冻结。


> 状态：反馈链骨架已形成；采集 Schema、指标及因果归因方法待设计。

**Activated → Exposed → Adopted / Rejected → Outcome → New Evidence**。

- Activated：Router 判断值得被想起。
- Exposed：真正进入 Human / Agent Context；激活不等于曝光。
- Adopted：实际采用并影响行动；曝光不等于采用。
- Rejected / Ignored：不采用同样是学习信号，不直接判失败；可轻量记录 Not Applicable、Time Pressure、Disagree、Missing Resource、Context Different 等原因，不强制填表。
- Outcome：记录质量、Cycle Time、Retry、Human Time、Compute/成本等实际结果。
- New Evidence：使用/拒绝和结果先形成 Events，再相对于 Claim 构成 Evidence，回到 Attention、Verification 和知识重评。

**采用后成功不等于证明知识导致成功**；需排除 Human Capability、Task Difficulty 等混杂。没有可观测的采用证据时保持未知，不推断 Human/Agent 已采用。

尽量自动采集，避免日常问卷负担。候选观测指标：Activation Rate、Adoption Rate、Successful Reuse、Knowledge Coverage、经实验验证的 Outcome Contribution、Time-to-Knowledge-Reuse。指标尚无真实基线。

关联：[[Knowledge Consolidation & Salience v0.1]] · [[Knowledge Intervention v0.1]] · [[Organizational Learning & Knowledge Formation]]
来源：[[探讨AI原生组织-raw-conversation]]（主设计对话，2026-09-04 阶段同步）。
