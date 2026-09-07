# 04 Specification

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 7b73e4e3](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-7b73e4e3-2e38-4b9a-8b6d-9ee51363c0f0) · [源文 9905dc6e](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-9905dc6e-cc09-45f8-8b64-94e95f015a7a) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## Memory、Learning、Knowledge、Activation

Memory 防止正式经验消失；Learning 发现值得学习的现象；Knowledge 提炼目前有理由相信的认知；Activation 在需要时带回工作。Experience ≠ Knowledge。

Knowledge 是基于 Evidence，在特定 Scope 与 Boundary 下有理由成立并可支持未来认知或行动的 Claim。不是文档或聊天记录本身；文档只是载体。Knowledge 至少支持 Core Claim、Scope、Boundary、Mechanism、Evidence、Transfer Conditions 的组件定位。

## 三层与认知形成

Experience Layer 保存 Task Return、Result、Observation、Event、Artifact、Source；Evidence/Learning Layer 保存 Evidence、Hypothesis、Verification、Challenge、Pattern 与 Interpretation；Knowledge Layer 保存可调用的知识。这是逻辑分层，不规定三个物理数据库。普通任务优先知识层，需要解释、质疑或重验时下钻。

正式经验 → Attention/Observation → Pattern → Hypothesis Cloud ⇄ Evidence ⇄ Verification/Falsification → Generalization/Scope → Knowledge → Continued Use → New Evidence/Challenge → Expand/Narrow/Refine/Split/Supersede/Reject。Pattern 表达重复结构，Hypothesis 是候选解释，不能混同因果或已知事实。

Verification 优先反证、替代解释、边界案例与失效环境；孤证不立，独立证据比重复转述重要。Minimum Validated Scope 起步，随真实使用扩张/收缩；Knowledge Quality ≠ Scope Size。已有 Evidence、Verification、Generalization 细则继续适用，操作化评分与字段不是冻结结论。

Hypothesis Cloud 是 Shared Reasoning Primitive，可用于知识形成、Root Cause、Human Oversight Externalization、Risk Interpretation、Failure Analysis；多个解释并存，Human/AI 排序与新 Evidence 推动解释空间收敛。

## Activation、Context 与反馈

Task Claim、Major Decision、Blocked、Unexpected Terrain、Review 是 Runtime 知识查询接触点。Query → Relevant Knowledge → Scope/Boundary Check → Context Assembly → Injection。Activation ≠ Injection；Inject cognition, not workflow。提供已知规律、边界、风险、依据和失败背景，How 仍属 Free Work Space。

保留 Cognitive Routing、Context Assembly、Consolidation & Salience、Intervention、Usage Feedback、Claim Push/Checkpoint Delta Push/On-demand Pull 的既有细则。可信度与显著性分开；频率、收益、风险、Surprise、复用、依赖、稳定性、Goal 影响作为不同信号，不压成未经验证的总分。Activated → Exposed → Adopted/Rejected → Outcome → New Evidence，使用与结果的关联不自动证明因果。

## Knowledge Pulse 与局部演进

New Knowledge、Challenge、Scope Change、Superseded/Deprecated 等有意义认知变化产生轻量 Pulse。Broadcast ≠ Injection；Global awareness, selective interruption。所有 Representative Agent 接收轻量变化信号，相关知识再按本地 Context 激活；真正依赖改变组件的 Active Execution、Capability、Automation 接收更强行动信号。

Evidence 高频进入，只有改变 Claim/Scope/Boundary/有效判断的 Material Change 才强传播。按组件保存 Version + Delta + Reason + Evidence；相关实质变化加入 Change Set。禁止以新摘要覆盖旧认知历史，禁止全组织无差别中断。

## Knowledge、Policy、Protocol

Knowledge 表达目前认为世界怎样；Policy 表达当前允许、禁止与要求；Protocol 是共同语言和交互结构。Knowledge 不晋级成为 Protocol。Inform/Recommend/Default/Mandatory 表达行为影响/Policy Force，不是 Knowledge 生命周期。

成熟 Knowledge 可支持 Policy Proposal；Relevant Human Authority 决定 Policy Activation，随后更新 Runtime Boundary。只有共同语言无法表达协同/治理需要时才涉及 Protocol Change。Evidence 强不自动带来 Mandatory 或扩大 Authority。

## Teachability 与实验边界

知识清晰以另一 HAU 能否 Explain、Apply、识别 Boundary 与 Transfer 判断；Teachability → Transferability → Reproducibility 连接 Capability。学到方法不等于组织已能复现。

Learn before prescribe：前期保留低 Learned Knowledge 干预的基线观察，不因个别成功就固化 Workflow/强制 Policy。Pulse 负载、干预比例、激活预算、证据阈值与排序权重留待调参与实验。广泛存储仍受明确组织边界约束，不默认吸收全部私人过程。

## 保留的子机制详细正文

- [Organizational Knowledge Formation Protocol v0.1](../../Organizational%20Knowledge%20Formation%20Protocol%20v0.1.md)
- [Evidence Core Principles](../../Evidence%20Core%20Principles.md)
- [Verification Protocol v0.1](../../Verification%20Protocol%20v0.1.md)
- [Generalization & Scope](../../Generalization%20%26%20Scope.md)
- [Cognitive Routing 与 Knowledge Activation](../../Cognitive%20Routing%20%E4%B8%8E%20Knowledge%20Activation.md)
- [Context Assembly v0.1](../../Context%20Assembly%20v0.1.md)
- [Knowledge Consolidation & Salience v0.1](../../Knowledge%20Consolidation%20%26%20Salience%20v0.1.md)
- [Knowledge Intervention v0.1](../../Knowledge%20Intervention%20v0.1.md)
- [Knowledge Usage Feedback](../../Knowledge%20Usage%20Feedback.md)
- [Knowledge Injection 与同步边界](../../Knowledge%20Injection%20%E4%B8%8E%E5%90%8C%E6%AD%A5%E8%BE%B9%E7%95%8C.md)
