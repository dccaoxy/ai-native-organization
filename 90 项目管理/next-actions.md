# 待办与下一步

- 状态：当前有效
- 复核日期：2026-09-04

## 优先输入

1. 确定 2–3 个真实任务例子，或提供后续关于组织将做什么的讨论材料。
2. 明确技术与数据边界：允许使用的平台、公司 Agent、可进入 AI 的数据、禁止范围、现有协作系统。
3. 明确第一阶段 Human-Agent 协作实验变量与最小安全边界。

## 设计工作

1. 继续 [[Knowledge to Behavior - Behavioral Authority|Knowledge→Behavior]]：由谁治理 Inform / Recommend / Default / Mandatory 的晋升；同步展开 [[Agent Governance & Runtime]] 的 Capability / Lifecycle / Performance / Revocation / Shared Agent 治理。
2. 用真实任务检验 Organizational Attention、Hypothesis Cloud、Evidence 与 Verification v0.1，并记录用于后续模型化的数据。
3. 设计 Audit Protocol v0.1，覆盖关键事件、版本、Override、权限与追溯。
4. 在已确认的 Free Work Space 定位下，研究 Executor / Orchestrator / Supervisor 的动态切换。
5. 从真实任务反推 Ontology / Organizational Graph v0.1、Evidence Provenance Graph 与完整 Reference Workflow。
6. 设计实验分期与测量框架，纳入 Review Cost / Error Detection Rate、MTTD / MTTR、Verification Economics 和组织自我实验。

## 暂不做

- 不先开发完整平台。
- 不先选数据库、Agent Framework 或 Graph 技术栈。
- 不拍脑袋制定 Contribution Score。
- 不把 Task Decomposition 粒度写进强制 Protocol。
- 不把讨论中的研究问题误写成已确认结论。

## 已完成

- Goal Protocol v0.1。
- Task Protocol v0.1。
- Goal + Task 接口检查与 4 项补丁。
- Operating Loop v0.2 与 Free Work Space 定位。
- Free Work Space Protocol v0.1（六类 Escalation Triggers）。
- Time & Recovery Protocol v0.1。
- Task Lease & Progress Protocol v0.1。
- Review Protocol v0.1。
- Acceptance Protocol v0.1；Goal Measure 已修订为 Success Criteria。
- Knowledge、Ontology、Contribution 的架构级原则。
- Organization Runtime & Protocol OTA 核心架构。
- Organizational Learning / Knowledge Formation 主干。
- Organizational Attention Mechanism 的三类来源与七项 Organization Lens。
- Pattern 与 Hypothesis Cloud 的核心定义。
- Evidence 核心定义、Independent Evidence Principle 与 Evidence Threshold follows Impact。
- Organizational Knowledge 的核心定义、原子化原则与类型划分。
- Verification Protocol v0.1。

来源：[[05项目/AI Native组织/80 原始讨论/探讨AI原生组织-raw-conversation|原始对话]]。

## 本次完成（2026-09-04）

- [[Organizational Knowledge Formation Protocol v0.1]] 冻结，[[Generalization & Scope]] 核心设计已完成。
- [[organizational-memory]] 核心架构与所列 v0.1 子机制状态同步；Knowledge→Behavior 治理未冻结。
- [[Agent Governance & Runtime]] 正式列为一级模块，骨架已确认。
- DESIGN-ISSUE-001：`Resolved — baseline sync gap, not protocol contradiction`。

## 本轮新增收敛

Generalization / Scope 与 Knowledge Formation v0.1、三层 Memory、Cognitive Routing、Context Assembly v0.1、Knowledge Consolidation & Salience v0.1、Intervention v0.1 核心框架、Usage Feedback 与 Agent Governance 骨架。详见 [[设计状态与版本]]。

原文新增及历史乱码缺口见 [[阶段同步报告 2026-09-04]]。

## 新增续接工作

- 后续一级模块继续推进 Capability & Human Learning、Contribution / Honor、Governance / Audit / Risk。
- 用真实任务验证 Context Assembly、Intervention 与 Usage Feedback；前期增加无 Learned Knowledge 干预样本，不预设比例。
- 按 [[设计与开发轨道]] 准备 Schema、Event Store、Task Bus、Gateway、Adapter 与最小模拟器；发现未定义边界回传 Design Issue。
