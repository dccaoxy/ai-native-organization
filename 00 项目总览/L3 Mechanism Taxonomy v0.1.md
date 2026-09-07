# L3 Mechanism Taxonomy v0.1

> Operating Model v0.1 Final Design Baseline；文档收敛：2026-09-07。设计已冻结，未声称系统已实现或实验已验证。

[总入口](Operating%20Model%20v0.1%20Final%20Design%20Baseline.md) · [原则树](Principle%20Tree%20v0.1.md) · [来源索引](../90%20%E9%A1%B9%E7%9B%AE%E7%AE%A1%E7%90%86/Final%20Design%20Baseline%20%E6%9D%A5%E6%BA%90%E7%B4%A2%E5%BC%95.md)

来源：[源文 ec3cb0fa](../80%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA/2026-09-07%20Final%20Design%20Baseline%20%E5%8E%9F%E5%A7%8B%E8%AE%A8%E8%AE%BA.md#turn-ec3cb0fa-47c9-41b7-9356-c6655745c579)。

机制名称按冻结原文保留。Mxx-L3-xx 为本次文档索引 ID；详细原则从模块第一轮、Pass 2与最终冻结分类提取，不为每个机制凑固定条数。


## 00 Organizational Reality

- [M00-L3-01 Event Model](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md)：统一 Organizational Event 基础模型与 Envelope，允许多个 Event Type；不得按业务模块另造事实世界。
- [M00-L3-02 Event Graph](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md)：记录历史事实及事件联系；历史原则上不可覆盖，解释可在各模块演进。
- [M00-L3-03 Dependency Graph](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md)：只表达 Material Reliance；关联或看过不自动成为 Dependency，当前依赖变化保留历史。
- [M00-L3-04 Materiality Detection](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md)：高频 Evidence 不等于强响应；足以改变有效 Claim/Scope/Boundary/Decision 时才产生 Material Change，参数不预定。
- [M00-L3-05 Change Set](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md)：以共同根因或变化上下文聚合相关事件用于治理，不替代底层 Event。
- [M00-L3-06 Object Versioning / Granular Evolution](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/00%20Organizational%20Reality/00%20Mechanisms.md)：质疑最小有意义组件，保留 Version/Delta/Reason/Evidence，沿依赖选择性传播。

## 01 Goal

- [M01-L3-01 Goal Formation / Activation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/01%20Goal/01%20Mechanisms.md)：Human/Agent 可提 Proposal；只有获授权 Human 激活目的并承担 Goal Authority。
- [M01-L3-02 Goal Challenge & Revision](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/01%20Goal/01%20Mechanisms.md)：可 Challenge，不可静默改 Goal；优先修正组件，Human 决定保持或改变。
- [M01-L3-03 Goal Dependency / Impact Propagation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/01%20Goal/01%20Mechanisms.md)：正式 Task 最终服务 Active Goal 并指定 Primary Goal；实质变化只影响相关依赖支路。

## 02 Task and Execution

- [M02-L3-01 Task Formation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md)：形成共享 Contract，经过 Goal Alignment 与 Boundary Validation；不规定 How。
- [M02-L3-02 Task Discovery / Bounty Tavern](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md)：Task Bus 首先是机会市场；Invite 不等于 Assign，Capability 导航不准入。
- [M02-L3-03 Claim & Execution Creation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md)：Claim 创建尝试，ACK/Progress/Accountability 属于 Execution；创建即解析唯一 Human。
- [M02-L3-04 Parallel Execution](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md)：Claim 不天然排他；明确 Exclusive/Parallel/Collaborative Mode，结果选择不等于能力或贡献认可。
- [M02-L3-05 Dynamic Task Generation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md)：可为 Active Goal 与其 Boundary 内需要自动派生工作；超出目的的机会先形成 Proposal。
- [M02-L3-06 Execution State / ACK / Progress](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md)：持续真实 ACK/Progress/Blocked/Need Help/Submit/Fail/Release；失败允许，静默失联不允许。
- [M02-L3-07 Task Return / Expedition Report](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/02%20Task%20and%20Execution/02%20Mechanisms.md)：标准化 Result/Terrain/Facts/Reflection；Representative Agent 整理，Human 确认修正补充，失败也需 Return。

## 03 Free Work Review Acceptance

- [M03-L3-01 Free Work Boundary](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md)：组织管理 Contract 与正式边界，不默认采集私人推理、草稿和内部 Subtask。
- [M03-L3-02 Progress Reporting](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md)：维持 Execution 状态可见性与可信进展，不监控完整过程。
- [M03-L3-03 Result Submission](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md)：通过正式 Return 提交 Result 与依据，Submitted 不等于已接受。
- [M03-L3-04 Review](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md)：以适合使用后果的独立性和证据判断可信；Quality 与 Learning 信号分开。
- [M03-L3-05 Acceptance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md)：判断 Execution Result 是否满足用途并有适当授权；Acceptance Authority 不等于 Risk Authority。
- [M03-L3-06 Parallel Result Selection](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/03%20Free%20Work%20Review%20Acceptance/03%20Mechanisms.md)：在多个合格 Result 中选择采用者，不抹除未被选择结果的能力、学习与贡献价值。

## 04 Learning and Knowledge

- [M04-L3-01 Experience Capture](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：广泛保存越过正式边界的经验与来源，不把私人全过程默认为组织采集对象。
- [M04-L3-02 Observation / Pattern Formation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：Observation 表达现象，Pattern 表达重复结构；两者不自动证明因果。
- [M04-L3-03 Hypothesis Cloud](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：多个候选解释并存，由排序与 Evidence 收敛；它是跨模块共享推理构件。
- [M04-L3-04 Verification / Falsification](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：优先证伪、替代解释、边界与失效案例；孤证不轻易泛化。
- [M04-L3-05 Knowledge Formation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：形成有 Evidence/Scope/Boundary 的 Claim；Knowledge 不是文档本身，也不是 Policy。
- [M04-L3-06 Knowledge Challenge & Granular Revision](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：定位组件并保留认知历史；Scope 缩小不默认推翻整个知识。
- [M04-L3-07 Knowledge Activation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：稀疏激活，检查相关性与适用边界；Inject cognition, not workflow。
- [M04-L3-08 Knowledge Pulse](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：Broadcast 不等于 Injection；全局轻量感知，强干预沿受影响 Dependency。
- [M04-L3-09 Teachability / Transferability](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/04%20Learning%20and%20Knowledge/04%20Mechanisms.md)：清晰以另一 HAU 能理解、应用、识别边界及迁移判断为准；可教不等于已经可复现。

## 05 Agent Governance and Runtime

- [M05-L3-01 Representative Agent Registration / Binding](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：一个 Human 只有一个 Active Representative Agent；私人 Agent 数量与内部组织不由中央规定。
- [M05-L3-02 HAU Persistent State](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：持久状态属于 HAU/Organization，Agent 更换不丢失承诺、权限与历史。
- [M05-L3-03 Human Model](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：区分声明偏好、观察行为与推断；可 Challenge/补 Evidence，不直接改写观察模型或固化人格标签。
- [M05-L3-04 Organization Model](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：代表接口持有组织 Vision/Structure/Active Goal/相关 Protocol 的认知，并与执行上下文结合。
- [M05-L3-05 Runtime / Effective Runtime Envelope](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：显式组合 Protocol、Policy/Boundary、Execution State、Interface；各级 Envelope 只能保持或收紧。
- [M05-L3-06 Policy Propagation to Private Agents](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：私人 Agent 只继承与工作有关的最小规则和权限；不要求固定内部管理层级。
- [M05-L3-07 Boundary Extension](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：扩权遵循 Least Expansion，说明依据风险与替代，按 Authority Scope 路由。
- [M05-L3-08 Reliability Signals](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：可靠性先记真实响应事件，不造单一分数，不把任务失败等同于不可靠。
- [M05-L3-09 Runtime Health](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：Active/Degraded/Suspended 表达能否正常运行；阈值可调，不替代 Capability Map。
- [M05-L3-10 Handover / Context Reconstruction](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：从持久状态、Active Objects、Event/Dependency Graph、Runtime 重建 Context；旧 Agent 不是唯一信息源。
- [M05-L3-11 Organization-owned Agent](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：持续组织职能必须受 Control Plane 管理，每次 Execution 唯一解析 Human Accountability。
- [M05-L3-12 Agent Control Plane / Kill Switch](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/05%20Agent%20Governance%20and%20Runtime/05%20Mechanisms.md)：拥有 Authority 的 Agent 可识别、限制和停止；外部撤销不能依赖 Agent 自己遵守停止 Prompt。

## 06 Capability

- [M06-L3-01 Expected Terrain Generation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：仅预测地形与风险差距，种子维度可演进，不把预测当实测。
- [M06-L3-02 Task Return → Capability / Terrain Evidence](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：Return 与正式事件、Review/Acceptance 形成 Actor 和 World 两类 Evidence。
- [M06-L3-03 HAU Capability Map](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：记录实际走过的 Terrain/Context/结果，用于导航成长而非等级准入。
- [M06-L3-04 Organizational Capability Map](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：记录可重新组装复现的路线及证据，不是员工能力总和。
- [M06-L3-05 Human Oversight Map](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：关注 Human 判断、错误识别、监督与升级能力，避免重复通用技能评级。
- [M06-L3-06 Capability Capture](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：首次成功即提取路线候选并识别缺失，只对关键缺口向 Human 提问。
- [M06-L3-07 Capability Package](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：包含知识、数据、工具、配置、运行依赖、实践、审查与监督；Package 不强制 Workflow。
- [M06-L3-08 Reproduction](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：用新的 Execution 由另一合适 HAU 检验复现，证据进入共同执行体系。
- [M06-L3-09 Revalidation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：关键依赖发生实质变化时组件级重验，能力不被视为永久有效。
- [M06-L3-10 Capability Gap Discovery](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：发现 Active Goal 所需未知或过度集中能力，不无限扩张任务。
- [M06-L3-11 Exploration / Reproduction Task Generation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：Goal 需要时形成探索/外化/复现工作；仅有趣的未知形成 Opportunity/Goal Proposal。
- [M06-L3-12 Capability-based Auto Execution](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/06%20Capability/06%20Mechanisms.md)：能力可复现不意味着必须自动化，还需 Risk/Boundary/Cost/Oversight/Goal 条件且保留新探索。

## 07 Contribution Reward Honor Achievement

- [M07-L3-01 Contribution Detection](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：通过共享事实发现可追溯正向变化，自我声明只是待核实 Claim。
- [M07-L3-02 Contribution Ledger](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：保留 Change/Positive Impact/Traceability 与 HAU 归属，5+1 种子类别可多标签。
- [M07-L3-03 Downstream Impact](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：影响可以持续传播与重估，奖励不按因果链自动永久分成。
- [M07-L3-04 Cycle Collective Valuation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：评具体 Event，不先给 Type 定价；原则上不评自己的贡献。
- [M07-L3-05 Blind Event Valuation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：尽可能隐藏 HAU 身份，先评 Evidence 与 Impact，再 Reveal Ownership。
- [M07-L3-06 Scarcity / Saturation Signal](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：提供数量、历史变化和组织当前需要的上下文，不做自动公式折价。
- [M07-L3-07 Reward Pool Allocation](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：奖励根据当前周期集体估值分配，池规模与评议参数 Tunable。
- [M07-L3-08 Honor Candidate Detection](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：可由 AI 或 Human 提名有历史意义的事件，没有周期配额。
- [M07-L3-09 Honor Curation / Honor Story](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：Human 集体策展，保存 Context/Challenge/Action/Impact/Why We Remember，可增后续章节。
- [M07-L3-10 Progression](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：表达成长旅程，等级是否必要待实验，不能伪装成综合绩效总分。
- [M07-L3-11 Achievement / Badge](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/07%20Contribution%20Reward%20Honor%20Achievement/07%20Mechanisms.md)：以事件和里程碑反馈经历，不产生 Capability/Permission/Authority，也不直接修改 Human Model。

## 08 Governance Risk Audit

- [M08-L3-01 Authority Registry](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：Authority 有来源与对象 Scope，不能由承担 Execution 责任推导无限权力。
- [M08-L3-02 Governance Routing](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：按改变的对象与权限范围路由，正常边界内无需逐步审批。
- [M08-L3-03 Risk Expression / Risk Object](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：用行动、后果承担者、暴露、控制及剩余风险表达，不用未经验证的总分替代。
- [M08-L3-04 Consequence Routing](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：从实际后果承担者找到有权代表其的人；不能靠口头愿意负责替代授权。
- [M08-L3-05 Risk Shaping](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：先降低 Exposure、提高 Recoverability，再判断未知是否可探索。
- [M08-L3-06 Residual Risk Acceptance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：Human 判断超出预授权范围的剩余风险，不能越过 Hard Boundary。
- [M08-L3-07 Hard Boundary](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：标明法律/第三方权利/根本原则/Policy/技术限制来源；不同来源具有不同修改权。
- [M08-L3-08 Boundary Extension Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：Boundary Extension 为 Governance Request，新增风险时附 Risk Object，避免两套重复审批。
- [M08-L3-09 Policy Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：Knowledge/Risk/Evidence 支持 Proposal，由相关 Human Authority 激活 Policy 并更新运行边界。
- [M08-L3-10 Protocol Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：只因语言、协调、治理表达缺口或技术演进改变共同协议，受基础原则约束。
- [M08-L3-11 Foundational Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：保留根本 Authority/Accountability/自由边界的治理，不让 Protocol Authority 成为无限权力。
- [M08-L3-12 Audit Reconstruction](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：从事件、对象版本、当时权力与依赖历史重建决定，不采集所有私人思考。
- [M08-L3-13 Change Set Governance](../10%20%E7%BB%84%E7%BB%87%E5%8D%8F%E8%AE%AE/Operating%20Model%20v0.1/08%20Governance%20Risk%20Audit/08%20Mechanisms.md)：相关 Material Events 统一呈现影响与待决定项，各 Authority 只裁定自己 Scope。
