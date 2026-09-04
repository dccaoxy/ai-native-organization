# AI-Native Organization Fundamentals Backlog

> 状态：开放研究议题
>
> 用途：保留那些决定组织设计方向、但尚不能写入 Protocol 的“漂亮问题”。

## 使用规则

- 未知问题留在此处，不伪装成已确定原则。
- 每个问题最终应形成：当前假设、竞争性解释、可观察指标、实验设计和 Evidence。
- 形成稳定结论后，把结论提炼进入组织协议，同时保留研究过程。

## A. 人与 AI 的分工

### [[人与 AI 的分工/AI 获得默认执行权后，人应该扮演什么角色]]

Human 应成为 Executor、Orchestrator、Supervisor、Acceptor，还是根据 Task 动态切换？“AI 执行、人验收”在哪些条件下成立？

### [[人与 AI 的分工/AI-Native 时代 Junior 如何成长为 Senior]]

新人能否通过观察 AI、预测结果、审查错误和改进工作流形成判断力？哪些能力必须通过亲自执行获得？

## B. 组织运行机制

### [[组织运行机制/当任务可以动态调度，还需要传统 Manager 吗]]

如果系统能够拆解、Routing、Monitoring、Failover 和 Escalation，管理还剩下什么不可替代的职责？

### [[组织运行机制/Protocol 固定而 Workflow 动态是否可行]]

动态路径在多大程度上能保持质量、合规和组织对齐？哪些最小协议不可省略？

### [[组织运行机制/Task Bus 能否替代人肉 Router]]

Pull、Push、能力匹配和 Failover 能否替代传统主管派活？会不会产生无人领取、局部最优或责任稀释？

### Task 异常的发现与恢复效率

MTTD（Mean Time to Detect）与 MTTR（Mean Time to Recover）应如何定义、建立基线并优化？它们是否比单纯按时完成率更能反映组织响应能力？

## C. 学习与能力形成

### [[学习与能力形成/观察和审查 AI 能否替代亲自执行形成判断力]]

“观察 AI 做 100 次”与“亲自做 100 次”产生的能力有何差异？

### [[学习与能力形成/Learning Trace 能否成为新的能力发展机制]]

Task 理解、AI 方案、Human 选择、Reviewer 反馈、Retry 和最终通过形成的轨迹，能否可靠诊断 Capability Gap 并支持个性化学习？

## D. 组织智能与创新

### [[组织智能与创新/任务知识能力反馈结构化后组织能否加速进化]]

当 Task、Knowledge、Capability、Evidence 和 Feedback 都可被系统读取，组织面对下一任务是否会越来越快、越来越好？

### [[组织智能与创新/AI Factory 与 AI Lab 如何同时存在]]

追求速度、成本和稳定性的 Execution Engine，如何与追求假设、反例和新方向的 Exploration Engine 共存？

### [[组织智能与创新/如何衡量效率之外的 Innovation Yield]]

如何衡量组织产生新问题、新假设、新方法、有效实验和意外发现的能力，而不是只计算吞吐量？

### 组织自我实验与因果学习

组织能否从 Task、Routing、Review、Acceptance 与 Capability 数据中发现候选因果关系，并形成 `Observation → Causal Hypothesis → Experiment → Evidence → Validation → Knowledge`？如何避免把相关性误当因果，并控制伦理、风险、样本偏差与指标漂移？

### Review Cost 与 Error Detection Rate

如何以尽可能低的 Review 成本获得足够高的错误发现概率？不同风险与可验证性任务应采用抽样、交叉验证、关键重算还是完整复核？

### Verification Economics / Value of Information

如何根据 Information Gain、Decision Impact、Reuse / Scale 与 Human Time、Compute、Elapsed Time、Opportunity Cost、Experiment Risk 决定验证优先级？第一阶段仅使用 Low / Medium / High；待积累真实 Verification Proposal、成本、Belief Update、Decision Change、Knowledge Reuse 与结果价值后，再研究 Expected Value of Verification。

### Evidence Independence 与知识可信状态

如何通过 Provenance Graph 判断多个 Evidence 是否真正独立？Source Reliability、Measurement Quality、Reproducibility、Counter Evidence 与 Temporal Relevance 应如何影响 Knowledge 的 Supported、Validated、Challenged、Deprecated 与 Superseded 状态？

### Generalization / Scope

一条在局部条件下验证的 Claim，凭什么迁移到新的 Task、Human、Agent、时间与环境？哪些反例意味着 Claim 错误，哪些意味着 Scope 需要收窄？

## E. 人与组织关系

### [[人与组织关系/AI 会降低表达门槛还是削弱真实交流]]

AI 能否帮助内向者整理和表达观点？它是否也会让人逃避真实沟通、冲突和关系建立？

### [[人与组织关系/哪些 Human Friction 不应该被消除]]

争论、解释、被误解、重新解释、求助和共同克服困难，哪些看似低效的互动实际上在形成 Trust？

### [[人与组织关系/高效率但缺乏人际连接的组织是否算成功]]

如果 Task 完成率很高、每个人都频繁与 AI 互动、成员彼此却不认识，这个实验应如何评价？

## 初始观测维度

- 单位高质量组织产出的综合成本；
- Innovation Yield；
- 新人达到能力标准的时间；
- Human Oversight Capability；
- Task Retry、Reject、Blocked 与 Escalation 模式；
- MTTD 与 MTTR；
- Review Cost 与 Error Detection Rate；
- Knowledge 复用率与失效修正；
- Verification 的 Information Gain、Decision Impact、成本与后续复用价值；
- Goal Drift 与 Goal Challenge；
- Human-to-Human interaction、心理安全、信任与连接质量。

## F. Knowledge → Behavior 与组织实验

- Exploration vs Exploitation：更多 L0 Observe / 无 Learned-Knowledge 干预任务如何帮助知识自然生长？比例和实验分期尚未确定。
- Intervention 的采用/拒绝、Override 和 Outcome 如何形成新的 Evidence？如何控制选择偏差和自我强化？
- Behavioral Authority 从 Inform、Recommend、Default 到 Mandatory 的晋升与降级权限是什么？
- Human 与 Agent 治理有哪些共同机制与本质区别？Shared Agent 的责任和撤销如何处理？

因果学习、Review Cost vs Error Detection、MTTD/MTTR、Verification Economics / Value of Information 保留原研究条目；Scope 核心设计已完成，研究继续关注迁移与失效检测。

## 2026-09-04 基线澄清

Generalization / Scope 核心设计已完成并纳入 [[Organizational Knowledge Formation Protocol v0.1]]（冻结）；上文相关问题保留为真实 Work 的研究与验证议题，不表示核心设计仍待设计。当前治理主线见 [[Knowledge to Behavior - Behavioral Authority]] 与 [[Agent Governance & Runtime]]。
