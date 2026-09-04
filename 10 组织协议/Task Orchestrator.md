# Task Orchestrator

> 状态：职责已纳入冻结的 Task Lease & Progress v0.1；此页为职责索引，不另立冲突协议版本。

监控 ACK、Lease、可信 Progress、Checkpoint、Submit；识别 Stalled Candidate，诊断依赖、资源、定义、响应或能力问题。在线不等于推进，heartbeat 不自动证明有进展。

恢复顺序及权限以 [[Task Lease & Progress Protocol v0.1]] 和 [[Time & Recovery Protocol v0.1]] 为准：最低层先处理，必要时 Human Executor，再由 Human Authority 决定突破 Boundary、重大延期/风险、资源追加或标准变化。到期先 Overdue Review，不能直接等同 Failed 或自动改派。

支持 Context Delta Detection 与异常时 Knowledge Query，但不控制 Free Work Space 的每一步。恢复动作仍是 Extend / Re-scope / Reassign / Escalate / Terminate。

实现待澄清：Lease 更新者、Progress 失效时间、重派后旧 Executor 提交权、状态转换与并发一致性。开发发现未定义边界应形成 Design Issue，不擅自改协议。

关联：[[Task Protocol v0.1]] · [[Knowledge Injection 与同步边界]] · [[设计与开发轨道]]
