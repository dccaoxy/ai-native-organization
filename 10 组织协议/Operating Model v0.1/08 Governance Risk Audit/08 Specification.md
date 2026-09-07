# 08 Specification

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 23e4f37a](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-23e4f37a-c203-4edd-9473-8a72a4c79e47) · [源文 9905dc6e](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-9905dc6e-cc09-45f8-8b64-94e95f015a7a) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## Authority 与治理触发

Governance is the architecture of decision rights。Authority 必须有可追溯来源，跟随治理对象与 Scope，不默认形成中央审批金字塔。Goal、Data、Agent Permission、Protocol 等各有相关 Authority，不能互相取代。Accountability ≠ Unlimited Authority；Execution Human Owner 不因此有权代表所有后果承担者。

正常行动在 Authority + Boundary 内自主。突破边界、改变权力、接受超授权 Risk、改变 Policy/Protocol 或重大不可逆行动才进入适当治理。Authority Registry 支持按 What changes 路由至对应 Human Authority，由其在 Scope 内 Accept/Shape/Reject，结果形成共享状态变化事件。

## Risk、表达与路由

Risk 是在不确定性下，Actor 因 Decision/Action 暴露于可能产生负面后果的未来状态。Uncertainty、Hazard、Exposure、Consequence、Risk 分开；Complexity、Capability、Unknown 不能合为一个难度分。Unknown ≠ Dangerous。

轻量 Risk Object 表达 Action、Why Now、Potential Consequence、Consequence Bearer、Exposure、Existing Controls、Residual Risk、Requested Authority，不用假精确总分替代解释。

Potential Consequence → Actual Consequence Bearer → Who is authorized to represent them → Risk Authority。风险接受权跟随实际后果承担者，而非谁愿意口头负责；不能替无权代表者接受后果。已在预授权 Envelope 内继续自主，Human 治理剩余风险和边界，而非每个有风险动作。

## Risk Shaping、Hard Boundary 与扩权

先用 Sandbox、Read-only、Small Sample、Permission 限制、Backup、Review、Rollback 降低 Exposure、提高 Recoverability，再判断剩余 Residual Risk。尽量把未知变为失败得起的实验。

Hard Boundary 不是“分数很高”，而是普通 Authority 无权接受这种后果。必须标明来源：Law、Third-party Right、Foundational Principle、Organization Policy、Technical Safety Limitation。修改路径由来源决定；普通组织治理无权改法律或第三方权利，不能靠一次风险签字绕过。

Boundary Extension 是 Governance Request，说明最小必要扩大；增加 Exposure/Residual Risk 时附 Risk Object，不再形成两套重复请求。授权只能由覆盖对应 Scope 的 Authority 给出，委托不创造新权力。

## Knowledge、Policy、Protocol、Foundational Governance

Knowledge 表达认知；Policy/Boundary 表达当前要求；Protocol 表达共同语言、语义、状态和交互结构；Foundational Principles 表达根本权责与自由。变化频率从高到低，不把 Policy 都归为 Protocol。

Knowledge/Risk/Evidence → Policy Proposal → Relevant Human Authority → Policy Activation → Runtime Boundary Update。Policy Force 与知识可信度分离；Policy 变化、版本与理由进入事件历史。

只有 Expression Gap、Coordination Gap、Governance Expression Gap 或 Technical Evolution 才需 Protocol Change。Protocol Governance 是共同语言/表达层的治理权，受 Foundational/Constitutional Governance 约束；不是组织最终无限权力。新灵感先进入 Evidence/Hypothesis/Change Proposal，再决定 v0.1 Revision 或 v0.2。

## Material Change 与 Change Set Governance

只有实质 Boundary/有效判断变化超出当前 Envelope 才需治理，不对每次不确定性波动送审。Exposure 变化先局部重算 Residual Risk，不默认整个 Risk 重批。

相关 Material Events 聚为 Change Set，呈现 Root Evidence、Affected Components、Dependency Impact、Automatic Responses、Required Decisions。各 Authority 处理自己 Scope，避免重复审批。Change Set 不代替底层事实，治理决定与后续依赖更新继续写入 Event Graph。

## Audit Reconstruction

Audit 是 Organizational Reality 的历史重建视图，不是另一套事实存储。使用 Event Graph + Object Versions + Authority-at-the-time + Dependency History 回答当时发生什么、为何、谁有权、影响什么。

重要状态变化保留 Actor、当时 Authority、Reason/Evidence、Before/After State、Timestamp、Policy/Protocol Version。当前权限不能替代当时权限；相关 Knowledge 版本、Warning、Human 决策依据和 Runtime Escalation 是重建材料。

Audit 主要支持 Failure → Learning → Knowledge/Policy/Runtime Improvement；明确违反 Boundary 仍承担责任。私人推理与完整草稿不默认采集。Review/Acceptance/Selection 各留独立语义事件，验收权不替代高风险使用权。

## 级联影响的差异化响应

同一Material Change不能给所有对象发送同一种警报：低风险探索可以Warning后自主重评；关键Result可要求Re-review；Capability组件标记Revalidation Needed而不删除整个能力；无人值守自动执行可进入Degraded并限制新尝试。Policy的一条Supporting Evidence变化，不代表Policy立刻失效，应由Policy Governance判断剩余依据。

Goal Assumption受Challenge时，Human Goal Authority可Keep、Pause affected branch、Revise assumption、Re-decompose affected tasks或在必要时Revise Goal。改变认知与方案不自动扩大现有Execution Envelope；需要新增权力仍须Boundary Extension。

Change Set关闭后保存所有事件与Decision Trail，更新当前Dependency；各对象分别保留新版本、重验或限制状态，最初发现问题的HAU可形成Learning/Protection Contribution。无关支路继续，不重写历史。

来源：原始讨论turn-07913263-bb40-4e9d-97d6-9202d940b79a。上述为冻结的响应语义，非本次运行记录。
