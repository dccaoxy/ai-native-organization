# 05 Specification

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 a1b56a80](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-a1b56a80-1808-4234-93ff-c64181be2df9) · [源文 9905dc6e](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-9905dc6e-cc09-45f8-8b64-94e95f015a7a) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## 身份与代表关系

一个 Human 可使用多个 Private Agent，但只有一个 Active Human-bound Representative Agent 正式代表其进入组织。Human + Representative Agent 形成 HAU；HAU 是任务发现、能力探索、贡献、奖励、荣誉等行为的主要单位，最终 Accountability 属于 Human。

两类正式 Organizational Agent：Human-bound Representative Agent 与 Organization-owned Agent。前者承担组织接口、Task Interaction、Knowledge Activation、Runtime Protocol、Policy Propagation、Progress/Return/Escalation；后者代表持续职能，如 Orchestrator、Review、Knowledge。组织 Agent 不绑定单个人，但每次正式 Execution 必须解析到唯一 Human。

Private Agent 的模型、推理、内部协作属于 Free Work Space；使用受治理数据/资源/权限或改变 Organizational State 时才受相应边界约束。Representative Agent 可以是 Coordinator、Gateway 或 Context Carrier，组织不规定它必须管理内部全部 Agent。

## HAU Persistent State 与 Human Model

Persistent State 属于 HAU/Organization，不属于某个临时 Agent。包括 Human Model、Operational State（Active Goal/Task/Execution、Blocker、Pending Decision）、Organization Model（Vision、Structure、Active Goal、相关 Protocol）、Organizational Assets（Contribution、Honor、Capability History、Permission）。

Human Model 区分 Declared Preference、Observed Behavior、Inferred Human Model。画像来自真实组织行为的长期 Evidence，描述行为而非固定身份。Human 可声明偏好、Challenge 模型并补 Evidence，不能直接改写 Observed Model；Reward/Badge 不直接修改模型，底层行为证据才支持修正。行为维度支持组件级版本演进。

## Runtime 与 Effective Runtime Envelope

Runtime 显式组合 Protocol + Current Policy/Boundary + Execution State + Organization Interface，不能把全部管理规则混进 Protocol。Protocol Version 与 Policy/Boundary Version 分开；Protocol OTA 为低频语言升级，Policy Update 为规则变化。Knowledge 更新本身不扩大 Authority。

Effective Runtime Envelope 综合 Organization、Human Role、Agent、Goal、Task、Execution-specific Boundary。Delegation 只能保持或收紧权限；Private Agent 继承相关最小部分。Permission ≠ Capability，前者控制行为权，后者用于导航。

Boundary Extension Request 说明 Why、扩展范围、Evidence、Risk、Alternative，遵循 Least Expansion，按被突破的 Authority Scope 路由。扩展引入风险时附 Risk Object，不重复提交两套请求。相关 Change Set 到来后依 Dependency Impact 重算 Envelope/Knowledge/Policy；授权扩大仍须合法批准。

## Reliability、Health 与生命周期

能力做地图，健康做状态，可靠性先记事件。Runtime Health 为 Active / Degraded / Suspended；Reliability = No Silent Failure，不以永远成功或单一分数定义。正式执行持续真实回应 Received/ACK、Progress、Blocked、Need Help/Escalate、Submit/Fail/Release。

生命周期为 Register → Active → Degraded/Suspended → Repair/Handover → Active/Retired 的语义路径；超时与恢复参数为 Tunable。Agent Failure must not become Human Lockout：故障时 Human 仍可 Manual Mode 或更换 Agent。

## Handover = Context Reconstruction

新 Representative Agent 从 HAU Persistent State、Active Objects、Event Graph、Dependency Graph、Runtime State 重建当前 Context，而非依赖旧 Agent 把全部思考写成总结。检查代表谁、当前 Execution/Goal、Acceptance Criteria、Boundary、Blocker 与 Pending Decisions。确认后新 Agent Active，旧 Agent Retired/Revoked，保持唯一 Active 组织代表。

Pending Boundary Request、Submitted Result、Active Execution 等承诺属于持久 HAU/Execution/Task，对应 Human Accountability，不因旧 Agent 退休消失。Context 可重建，Organizational Reality 必须持久。

## Control Plane 与外部停止能力

所有拥有 Organizational Authority 的 Agent 都须有 Identity、Authority Source、Boundary、Runtime Status，并能被 Suspend。Organization-owned Agent 必须纳入 Control Plane，至少可见 Agent ID、Role、Status、Effective Boundary、Protocol Version、Current Execution、Last Heartbeat、Recent Governance Signals。

Kill Switch 位于 Agent 外部，不能只靠停止 Prompt；Gateway 必须能撤销相应 Credential、Permission、Lease 与 Organizational Action 能力。控制面治理组织状态与受治理外部行动，不监控私人思考。停权后当前 Execution 的责任、恢复与事件仍需闭环。

责任解析：HAU Execution → Human；Derived Execution → Parent Execution/Task；Organization-owned Execution → Task/Primary Goal/Organizational Function → 唯一 Human。Agent 从来不是最终责任人。

## 交接中的能力与私有配置

旧Agent的model-specific configuration、local temporary context、private scratch work不自动继承给新Agent。HAU历史能力证据保留，但Representative Agent配置改变后，历史Evidence的Transferability可能变化；Capability Guidance应提示这一不确定性，不能认为新Agent自动拥有旧Agent的能力。

交接完成撤销旧Agent组织凭证，即使旧进程仍运行，也不得继续代表HAU改变组织状态。Pending Request由Execution/HAU持有，新接口继续追踪，不因传递者退休而取消。

对于依赖被Challenge且无人值守重复执行的组织Agent，级联审查可令其Active→Degraded，暂停新的自动Execution；已进入安全阶段的执行按边界完成或转Review。恢复Active须依相应重验与治理结果，不能把运行健康自动等同于任务成功。

来源：原始讨论turn-2718e428-5265-48e3-8f18-6e60f4fc69ec、turn-07913263-bb40-4e9d-97d6-9202d940b79a。
