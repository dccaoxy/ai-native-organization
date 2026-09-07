# 01 Specification

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 4ae954b1](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-4ae954b1-3f17-4ce7-9767-aa50a07cd8d3) · [源文 f80a5817](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-f80a5817-3900-4909-a5cd-3569c7dbc2e6) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## Proposal 与 Activation

Human、Agent 均可提出 Goal Proposal，低门槛说明问题或机会、可能价值与可验证 Outcome。Proposal 不等于组织承诺资源。只有获得授权的 Human Goal Authority 可以 Activate Goal，并成为或指定 Human Owner。Agent 可 Discover、Suggest、Challenge、Decompose，不能自行改变组织目的。

Active Goal 至少表达 Desired Change、Success Criteria、Boundary、Human Goal Authority 与 Current State。Success Criteria 可以是数字、实验结果或可检查证据，不强制 KPI 化。Boundary 根据实际需要表达时间、预算、资源、数据权限、风险及不可触碰事项。Goal Owner 对结果、关键判断、暂停、终止和资源变化负责，不等同于日常派工经理。

## 结构与生命周期

Goal 支持 Desired Change、Success Criteria、Assumptions、Scope、Boundary、Priority/Time Horizon 等组件独立定位与版本演进。历史 Measure 统一使用 Success Criteria；Outcome 在旧协议中的含义与 Desired Change 对应。

既有生命周期保留 Proposed、Active、Achieved、Paused、Failed、Cancelled/Terminated、Superseded。Achieved 要求标准满足并授权确认；Paused 保留恢复可能；Failed 指证据表明未实现且继续投入无合理成功预期；Terminated 不等于失败；Superseded 保留替代关系。

## Goal → Task

每个 Active Goal 有 Decomposition Trigger，确保首批 Task Proposal 实际产生；Decomposer 可为 Human、Agent 或 HAU。Goal 不直接进入 Task Bus。链路为 Active Goal → Decomposition → Task Proposal → Goal Alignment + Boundary Validation → Active Task → Task Bus。

每个正式 Task 最终服务至少一个 Active Goal，可服务多个 Goal，但必须指定一个 Primary Goal，提供组织层责任锚点及 Boundary/Governance 主继承链。Task Acceptance Criteria 必须说明通过后如何帮助 Goal Success Criteria；不要求每个探索 Task 都贡献一个 KPI。

Initial、Derived、Exploration、Externalization、Reproduction Task 均受此约束。仅发现有趣机会而不服务 Active Goal 时形成 Proposal，不自动扩大 Goal。

## Challenge、Revision 与下游影响

Human/HAU/Agent 可以依据 Evidence Challenge 指标、Assumption、Scope、Boundary 或 Desired Change；Human Goal Authority 决定 Keep、Modify、Pause、Achieve、Terminate 或 Supersede。质疑不等于静默修改，优先修正最小有意义组件。

每次实质变更保留版本、差异、理由与证据；以 Dependency Graph 识别受影响支路，必要时加入 Change Set。不再因任一 Goal Challenge 自动暂停全部下游 Execution。

Primary Goal 失效时先检查 Task 是否仍服务其他 Active Goal；可以在相应 Authority 下 Re-parent，否则处理 Close/Release/Proposal。已有 Result、Evidence、Artifact 与有价值投入保留，不能一并抹除。

## Authority 边界

Goal Authority 不等于所有 Risk/Data/Permission Authority。Goal 重要或 Goal Owner 承担责任，都不能代替无权代表的后果承担者接受风险。具体责任解析与治理路由见 08，尝试级 Human Accountability 见 02。
