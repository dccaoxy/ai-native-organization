# 02 Specification

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 dff47a39](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-dff47a39-e416-40c1-9248-63540d25ecae) · [源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## Task ≠ Execution

Task 承载 shared intent / contract，Execution 承载 one attempt。Task 包含 Why/Goal/Primary Goal、Expected Output、Acceptance Criteria、Permission/Risk/Resource Boundary、Runtime constraints、Execution Mode 与 Due 约定；Capability Requirement 不作为领取硬门槛。

Execution 关联 Task、Executor/HAU、唯一 Human Accountable Owner、Status、Runtime Boundary、Time，以及尝试专属 Claim/Lease、ACK、Progress、Blocker、Return、Result 与证据。TaskCreated 归 Task；ExecutionClaimed、ACK、Progress、ResultSubmitted 归 Execution；Acceptance 关联 Result/Execution。不得用某个尝试失败或提交覆盖整个 Task 的共享状态。

Task 的组织责任锚点由 Primary Goal → Goal Owner 提供。HAU Execution 解析到 HAU Human；Derived Execution 沿父执行/任务链；Organization-owned Agent Execution 沿 Task/Primary Goal/Organizational Function 解析到唯一 Human。创建时即解析，Agent 不成为最终责任终点。

## Formation、Discovery 与 Claim

Task Proposal 经 Goal Alignment、Output/Criteria 完整性、重复检查与 Boundary Validation 后激活；边界内允许自动生成/激活。Task Bus 承担 Publish、Discover、Recommend/Invite、Claim、Track、Return、Generate。Invite ≠ Assign，正常以发现和领取为主，特殊派发仍需 ACK，Assigned ≠ Accepted。

Capability Map 提供 Gap/Risk Brief 与导航；实际限制来自 Permission、Risk、Protocol。Exclusive、Parallel/Competitive、Collaborative 为明确 Execution Mode，Claim 不天然排他。并行数量与推荐数量属于 Tunable。

## 执行状态与恢复

最小共同语言为 Claim → ACK → Progress / Blocked / Need Help / Escalate → Submit / Fail / Release。Submitted 不等于完成；Execution Result 仍需 Review/Acceptance，适用时再 Selection。协作模式也必须清晰解析每个 Execution 的唯一责任人。

保留 Due Time、ACK SLA、可信 Progress、Stalled Candidate、Overdue Review 的恢复语义。到期或无进展不直接判失败；Orchestrator 诊断依赖、资源、契约或响应问题，再选择 Extend / Re-scope / Reassign / Escalate / Terminate。Reassign 处理原尝试的释放/终止与新尝试的形成，保留历史，不静默替换 Executor。

Heartbeat/进程在线只说明运行信号，不证明工作有效推进。Progress 以正式状态和可信依据维持可见性，不要求上传所有中间过程。及时 Fail、求助或 Release 可以是可靠行为，Silent Failure 不允许。Lease、ACK/Progress 频率与 Health 门槛不预设数值。

Reject 应附能力缺口、负载、边界、验收不清或重复等理由；连续拒绝可以触发契约质量检查，不无限寻找下一个执行者。旧首阶段 Human WIP=1 保留为既有默认来源，不推导为单 Task 只能有一个 Execution，也不凭新基线自行修改数值；具体多尝试计数需运行规格明确。

## Task Return / Expedition Report

每次正式 Execution 结束都形成 Return：Result（含 Partial Result）、Observed Terrain、Major Execution Facts（时间、重大变化、Escalation、Human Intervention）、Reflection。Representative Agent 自动整理，Human Confirm / Correct / Add Missing Context。Standardize reporting, not interpretation。

Return + Event Trail + Review + Acceptance 支持 Result Record、Capability Evidence、Terrain Evidence、Contribution/Learning Signals。Failed 不等于 Empty Return；记录合理尝试、失败依据、被否定假设、风险、缺少资源与可复用教训。Result Selection 不等于能力认可或贡献认可。

## Dynamic Task Generation 与依赖

执行中发现 Data/Tool/Dependency/Verification Need/Capability Gap，可以形成 Derived Task。仍服务 Active Goal 且继承 Boundary 时允许自主形成；超出 Goal 的机会先形成 Proposal。内部 Subtask 默认留在 Free Work Space，只有独立资源、协作、责任、验收或正式追踪需要时才 Promote。

Task 主要依赖 Goal、Acceptance 契约与 Boundary；Execution 可动态依赖 Knowledge、Data、Tool、Permission、Capability Package。Primary Goal 失效时先检查其他 Active Goal 并按权限 Re-parent，否则 Close/Release/Proposal；沿真实依赖处理受影响尝试。

完整数据库枚举、并行结束策略和 API 尚需工程规格，不把上述语义序列冒充已经实现的状态机。
