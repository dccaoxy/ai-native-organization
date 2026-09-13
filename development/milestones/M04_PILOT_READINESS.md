# M04 Pilot Readiness

更新时间：2026-09-13

状态：**In progress — M04 尚未启动**

## Outcome

在不修改 Frozen L1/L2、不接入高风险公司系统的前提下，证明当前本地合成组织可以安全地转化为：

1. 非开发者可访问、无需运行命令的稳定入口；
2. 首次使用者能够理解并完成 Human × Agent 核心闭环；
3. 可由 5–10 位真实参与者在 2–4 个 Cycle 内进行低风险 Pilot 的受控方案。

Readiness 完成只允许提交“是否启动 M04”的 Human 决策包，不自动启动 Pilot。

## 已有基础

- M00 设计交接完成，Frozen L1/L2 仍是约束边界。
- M01 本地最小组织闭环完成。
- M02 在声明范围内完成 60 Execution / 536 合成事件验证。
- AA01/AA02、M03 最小闭环、R01、UX01/UX02、PA01/PA02 已有本地验收证据。
- OpenClaw/MiniMax 已完成一次独立 Agent 的 Claim → ACK → Progress → Submit；尚无 Human Review/Acceptance。
- 2026-09-13 Gate B 本地工程完成后，当前工作树 175 项单元测试通过。

以上均不构成远程部署、真人 Pilot 或组织效果证据。

## Gate A：状态与证据一致性

- [x] `CURRENT_STATE.md` 明确当前阶段、工程成果与未完成边界。
- [x] `NEXT_ACTIONS.md` 只有一个最高优先级行动序列。
- [x] `MILESTONES.md` 不再把 AA01/M03 误写为当前里程碑。
- [x] 最新完整测试通过，并记录测试日期与数量。
- [x] 已核对 PA02、PA01、UX02、R01、M03、AA02、AA01、M02、M01 的本地 checkpoint/tag；PA02 artifact 与相关 state 文件存在。
- [x] GitHub 状态收敛完成：此前 `development/autodev/DELIVERY.json` 只验证到 `d3a4188`；2026-09-13 已将累计本地提交与 annotated checkpoint tags 推送，远端 `main` 读回验证到 `d6025e0`，关键 M04 文档可匿名读取。该证据只证明 Git 交付，不证明远程服务部署。
- [x] 已核对 Obsidian 项目 Dashboard 存在且最后修改时间晚于设计基线，但本轮未同步；继续将其定义为 Human Dashboard / 投影层，不作为开发完成依据。

## Gate B：远程可用性决策包

当前提案与差距见 [M04 Deployment Decision](../M04_DEPLOYMENT_DECISION.md)。该文件是审查材料，不是部署授权或部署回执。

本地工程证据：安全 `/health`、结构化脱敏日志、可信反代来源校验、SQLite 在线备份/校验/非覆盖恢复、Nginx 候选模板和 systemd 资源限制已实现；12 项目标测试与 175 项完整回归通过。目标 Linux、TLS、真实反代、journal、资源限制和恢复演练仍未执行。

- [ ] 明确候选域名或隔离路径，不影响 AEGPC.CN 现有项目。
- [ ] 明确 TLS、反向代理、监听地址和网络隔离。
- [ ] 明确 Human 身份、Agent 一次性凭据、撤销与轮换方式。
- [ ] 明确服务常驻、健康检查、重启和资源上限。
- [ ] 明确数据库位置、迁移、每日备份、恢复演练和保留期。
- [ ] 明确日志、审计事件、敏感字段脱敏和告警。
- [ ] 提供部署、停机、回滚步骤及预计影响范围。
- [ ] 部署前取得单独 Human 批准；未批准时不得执行。

## Gate C：3–5 人理解与可用性测试

每位参与者使用新账户和低风险合成任务，全程不要求安装依赖或运行命令。

执行脚本与原始记录模板见 [M04 Usability Test Plan](../M04_USABILITY_TEST_PLAN.md)。在真实入口和参与者获批前，该计划保持 Ready to run，不填写虚构结果。

必须验证：

- [ ] 能说明 Goal、Task、Execution 的区别。
- [ ] 能找到 Human owner、Agent 权限和 Boundary。
- [ ] 能完成创建/发布、Agent 接入、Claim/ACK/Progress/Submit。
- [ ] 能完成独立 Review 与 Human Acceptance，或正确发起返工。
- [ ] 能找到 Evidence、Knowledge 来源、版本和失效状态。
- [ ] 能识别 Agent 不得自批权限、不得替代 Human Accountability。

通过阈值：

- 至少 3 位真实参与者完成；
- 核心闭环任务完成率不低于 80%；
- 0 个凭据泄露、越权、自我批准或跨账户数据暴露；
- 所有阻断级问题关闭并复测；
- 保存原始观察、时间、错误、参与者匿名编号与修复映射，不补造数据。

## Gate D：Pilot 方案

- [ ] 选择 5–10 位真实参与者及 2–4 个工作 Cycle。
- [ ] 只选择可撤销、低风险且不依赖生产写入的真实任务。
- [ ] 为每个 Goal 指定唯一 Human Accountability Unit/owner。
- [ ] 明确 Agent 权限、禁止 Action、升级路径和紧急停机人。
- [ ] 明确数据分类、最小收集、保存期限和退出/删除办法。
- [ ] 建立基线：现行完成时间、返工、协调次数和质量信号。
- [ ] 定义每 Cycle Review、异常处理和最终 Acceptance。
- [ ] 取得参与者知情同意与单独 Human 启动授权。

建议指标：

- Cycle time 与等待时间；
- Return 一次通过率、返工率和返工原因；
- Boundary/Escalation 次数、响应时间和正确率；
- Evidence 完整度与可追溯性；
- Knowledge 复用、反证、失效与重验次数；
- Human 协调负担、理解偏差和主观可用性；
- 质量、创新产出和风险事件，不能只看效率。

## Gate E：启动裁决

启动 M04 前必须形成一份 Human 决策包，至少包含：

- Gate A–D 的逐项证据和未关闭问题；
- 部署/回滚方案与实际可访问性回执；
- 3–5 人测试的原始记录、汇总和修复复测；
- Pilot 范围、人员、时间、任务、权限、指标与停止条件；
- 明确选择：`GO`、`GO WITH CONDITIONS` 或 `NO-GO`。

以下任一情况直接 `NO-GO`：身份隔离或权限撤销失败；凭据暴露；跨账户数据泄露；无法回滚；无唯一 Human owner；阻断问题未复测；用合成记录冒充真人证据。

## 当前下一步

先补齐 Gate B 决策包中的阻断项，并准备 Gate C 的测试脚本与原始观察模板。部署、push、真实参与者招募、真实数据接入和 Pilot 启动均保留为后续独立 Human Gate。
