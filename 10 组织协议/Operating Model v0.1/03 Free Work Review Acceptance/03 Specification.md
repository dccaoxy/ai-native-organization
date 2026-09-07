# 03 Specification

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 432b1bac](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-432b1bac-3701-4234-a8f7-e9b11ade2154) · [源文 9905dc6e](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-9905dc6e-cc09-45f8-8b64-94e95f015a7a) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## 自由工作的真实边界

Execution 进入工作空间时具有 Task Contract、Effective Runtime Envelope、Relevant Knowledge 与 Protocol。HAU 自主选择模型、私人 Agent、工具、Workflow、临时 Subtask、研究和实验方法。组织治理 Contract，不微观管理 How。

工作不得偏离契约或越过边界，结束时必须带回可检查结果或失败信息。私人 Prompt、草稿、推理、内部失败、普通 Tool Call 默认不进入 Reality；正式 Result、Evidence、Risk、Boundary Request 或组织状态变化才越过采集边界。Reporting 维持执行可见性，不监控私人过程。

## 返回与升级

正常出口为 Task Return；异常或发现出口按对象路由。需要突破 Resource/Time/Permission/Data/Risk Boundary 时先停止受影响行动并申请最小扩展；不能合理监督或判断时报告能力/监督缺口，不能将能力不匹配一概做成 Claim Gate。

内部工作需要独立执行、资源、Acceptance、跨 HAU 协作、责任或正式追踪时 Promote to Task Proposal。无法推进现有 Goal 或发现新方向时 Goal Challenge/Proposal。候选经验进入 Experience/Evidence/Knowledge Formation；候选提交不等于已验证 Knowledge。重大未识别风险或不可逆行动按当前 Envelope 处理与升级，不把每次不确定性波动都送审。

## Review

Review 回答 Result 是否值得相信，检查 Evidence、Logic、Completeness、Boundary Compliance、Known Risk 与 Acceptance Criteria。可由 Independent/Review Agent、Other HAU、Human、Automated Verification 或组合执行；关键是独立性和适合当前 Result Impact 的判断能力。不能仅靠执行 Agent 自检闭环。

保留 Quality Gate + Learning Gate：质量检查 Completeness、Compliance、Evidence、Correctness、Risk；Confidence 为元数据，不替代证据。Learning Signal 与 Pass/Retry 并行，失败也可产生学习。新 Knowledge 信号先进入候选与验证链，不由 Review 自动变成定论。

## Acceptance 与 Selection

Acceptance 判断可信 Result 是否足以满足当前 Task/Goal 用途，必须有明确 Authority。Acceptance Criteria 前置、从 Goal Success Criteria 推导，使用 Hard Gates + Judgment；硬门槛不能被其他高分抵消。低风险且高可验证的授权范围内可自动接受；高风险或高判断由适当 Human Authority 判断并记录 Reason。标准改变保留版本、理由与历史。

Acceptance 属于每个 Execution 的 Result，不把一次通过等同于整个并行 Task 的所有尝试完成。Execution → Result → Review → Acceptance → Acceptable Result；Parallel Mode 下再 Selection → Selected Result。多个结果可以都合格，未选中不等于失败，也不抹去 Capability 或 Contribution。

Review 与 Acceptance 可以由同一 Actor 承担不同判断，但语义与事件分开；独立性仍须满足影响要求。ResultReviewed、ResultAccepted/Returned、ResultSelected 使用统一 Organizational Event。

## 使用权限与重新审查

Acceptance Authority ≠ Risk Authority。某 Result 对当前用途合格，不代表获得高风险外部使用权；使用后的潜在后果决定 Evidence/Review 强度。低风险探索可轻审，高影响、不可逆或外部使用需更强依据与相应授权。

Result 的关键 Evidence/Knowledge/Data/Tool 依赖发生实质变化时，沿 Dependency Graph 定位需要 Re-review 的结果，尤其已形成但尚未使用的 Result。不得以一条反证无差别否定所有历史结果。

Task Return 至少携带 Result、Observed Terrain、Execution Facts、Reflection，并与事件、Review、Acceptance 共同成为学习与能力证据入口。
