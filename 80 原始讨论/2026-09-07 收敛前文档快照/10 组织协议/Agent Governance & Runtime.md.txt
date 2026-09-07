# Agent Governance & Runtime

> 一级模块；状态：骨架已确认，待详细设计。依据 `ed8414ce-48c4-44a6-b366-01aadd028f6f` 与 DESIGN-ISSUE-001 裁决。

Human 与 Agent 都应被组织治理。AI-native 组织由 Human 与经过注册和治理的 Agent 共同构成执行网络。

**不要统一 Intelligence Layer，统一 Organization Runtime Layer。** 组织控制身份、权限、边界、运行义务和审计，不统一 Agent 如何思考。

## Registration & Binding

Register → Identity → Bind → Runtime Connect。每个 Organizational Agent 有唯一 Agent ID；Human ↔ Primary Agent 建立稳定 Human-Agent Unit，同时允许调用其他 Agent，并允许 Shared / Specialist Agent。不要求一人只能使用一个模型。

## Runtime & Control

Organization Gateway / System Bus、Runtime Adapter、Protocol Package、Task ACK / Lease、Progress / Heartbeat、Checkpoint、Knowledge Query、Escalation、Submit、Protocol Version、OTA、Audit。

Runtime 是 **Protocol + State + Interface**，不是只有 Prompt 或脚本。Context 让 Agent 知道规则，Tooling 让它执行义务，Gateway 接收并观察协议动作。Adapter 应薄，不替代模型推理和 Free Work Space。

## Permission & Boundary

Data / Tool / Action / Task / Risk / Knowledge / Delegation 七类边界。Agent 权限不能只由智能强弱决定，还应考虑绑定 Human 的 Capability、Oversight Capability、Role 和 Task Risk。Shared Agent 的归属与责任仍待设计。

## 接入等级与后续

Managed / Connected / Unmanaged 的能力与责任见 [[Organization Runtime & Protocol OTA]]，不把只注入 Prompt 的个人 AI 自动视为受控组织节点。

后续待设计：Capability、Lifecycle、Performance、Revocation（停权/撤销/注销）、Shared Agent 治理，以及升级、授权、审计与责任转移。当前未形成完整 Agent Governance Protocol v0.1。

关联：[[Task Orchestrator]] · [[Capability & Human Learning 待设计]] · [[Governance Audit Risk 待设计]]
来源：[[探讨AI原生组织-raw-conversation]]（主设计对话，2026-09-04 阶段同步）。

基线：[[DESIGN-ISSUE-001 基线同步裁决]]；未指定数字版本。Connection = Access + Rules + Responsibilities + Updateability。既有三段骨架与后续 Capability / Lifecycle / Performance / Revocation / Shared Agent 治理保留。
