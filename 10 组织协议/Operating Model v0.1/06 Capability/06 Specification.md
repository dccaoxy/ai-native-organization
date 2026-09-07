# 06 Specification

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](../../../00%20%E9%A1%B9%E7%9B%AE%E6%80%BB%E8%A7%88/Principle%20Tree%20v0.1.md) · [来源索引](../../../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 c6749981](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-c6749981-a954-4b1d-b805-1f85907c108b) · [源文 9905dc6e](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-9905dc6e-cc09-45f8-8b64-94e95f015a7a) · [源文 ec3cb0fa](../../../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

## 证据塑形的地图

Capability is evidenced, not declared；自报能力与厂商宣传只能作为先验。Capability 表达执行单元与问题空间的关系，不是固定等级或领取许可。Seed Map 只提供粗略 Domain/Problem Space 与少量 Terrain Dimensions，真实地形随 Execution 生长。

Expected Terrain 是发布时预测，Observed Terrain 是执行后观察，二者差异本身是学习信号。每次 Execution 同时可能产生 Actor 的 Capability Evidence 与 World 的 Terrain Evidence；一个 HAU 失败不等于所有人面对相同危险。Capability Evidence 来自 Return + System Events + Review/Acceptance，不能压到单一 Task 成败上。

## 三张地图与运行职责

HAU Capability Map 记录在何种 Terrain/Context 成功、失败、稳定、遇到 Hazard 或尚未知，用于 Navigation、Risk Awareness、Growth Guidance、Task Discovery，不作 Task Gate。

Organizational Capability Map 记录可重新组装的 Capability Package/Known Route、Knowledge、Tool、Data、Runtime、Review、Oversight Need 与 Reproduction Evidence，不是员工能力的加总。Human Oversight Map 关注 Judgment、Oversight、AI Collaboration、Error Detection、Escalation Judgment、Unknown Recognition。

系统 Navigate、Warn、Connect、Discover Gaps：帮助理解预期地形，提醒实际环境偏差，连接相关 HAU/Knowledge/Tool/Package，发现 Active Goal 所需而组织不会或过度集中的能力。高难度不自动等于高风险；高手也不能越过权限。

## Capture 与 Capability Package

首次成功 Execution 立即产生 Organizational Capability Candidate/Route 并开始捕获，不等多人成功才学习。Candidate 不等于已验证能力；后续复现提高可靠性和信心。

检查 Knowledge、Data、Tools、Agent Configuration、Runtime、Practice、Review、Human Oversight 是否可保存、复用及表达。系统自动提取，只就关键缺失向 Human 提问，不要求长表。Capture is not documentation; capture is reproducibility。

Package 包含 Applicable Terrain、Knowledge、Data Requirement、Tools、Agent Configuration、Runtime Dependencies、Practice、Review、Acceptance Pattern、Known Oversight Need、Known Hazards。Package ≠ Workflow，提供认知、装备、路线与风险提示，新的 HAU 仍自主决定 How。

## Reproduction 与 Revalidation

Teachability：新 HAU 能理解；Transferability：换 Context 能判断何时适用；Reproducibility：另一合适 HAU 能真正做成。Experience → Knowledge → Teachable → Transferable → Reproducible → Organizational Capability。

Reproduction 创建新的 Execution，使用已有 Package 在相似 Terrain 尝试，不发明独立能力考试体系。Package 组件可 Challenge：Tool 失效、Scope 缩小、Data Pipeline 变化或 Oversight 未外化分别定位，避免整个能力一并删除。

关键 Dependency 发生 Material Change 时要求 Revalidation，可触发 Revalidation Execution；正式执行仍受 Active Goal 与唯一 Human 责任规则约束。Capture → Reproduce → Use → Dependency Change → Revalidate。当前能力是否成立取决于关键依赖持续有效。

## Oversight Learning 与共同学习

高价值 Human Intervention 后，AI 提出 Candidate Reasons，Human 排序并可补充，不强迫给概率。Context + Outcome + Evidence 持续收敛 Oversight Hypothesis Cloud，形成 Oversight Knowledge/Review Practice/Organizational Capability，再教给其他 Human/Agent。不能只记 Override=Yes。

外化多少是实验问题，不假设全部隐性判断都能数字化。Human 与组织相互学习，组织处理越来越多已知，Human Attention 向未知迁移。

## Gap 与自动执行

Active Goal 需要且没人走过的区域可生成 Exploration Task；能力仅集中一个 HAU 时可形成 Reproduction/Externalization Task。单纯有趣但无 Active Goal 需要的区域只形成 Opportunity/Goal Proposal。

可复现、Boundary 清楚、Risk 可接受、Oversight Need 足够低的能力可以支持 Organization-owned Agent Execution，但 Capability enables automation; it does not mandate automation。还要考虑 Cost、Goal Context 与 Exploration Opportunity；自动化不禁止 Challenger HAU 寻找新路线。充分条件组合和规模化责任模型留待实验。
