# Development Milestones

## 2026-09-13 当前里程碑投影

当前位于 **Phase 1 收尾 / M04 Pilot Readiness**。这不是新增 L1/L2，也不表示 M04 已启动；它是从已通过的本地合成工程跨向远程可用性和真人证据之前的门槛。

| Readiness workstream | 状态 | 完成条件 |
|---|---|---|
| R1 状态与证据收敛 | In progress | 当前入口、验收包、测试结果和未授权边界一致 |
| R2 远程部署决策包 | Planned | TLS、身份、持久化、备份、监控、停机与回滚均有可审查方案 |
| R3 3–5 人理解/可用性测试 | Planned | 真实参与者完成测试并留下原始观察与结论 |
| R4 5–10 人 Pilot 方案 | Planned | 范围、权限、指标、停止条件和 Human Gate 明确 |
| R5 Readiness Review | Planned | 阻断项关闭并形成是否启动 M04 的决策包 |

完整 Gate 见 [M04 Pilot Readiness](milestones/M04_PILOT_READINESS.md)。下方历史表保留原 checkpoint 语境；其中“当前 Milestone = AA01”的旧描述已被本节取代。

## 当前：PA02 Agent 接入说明与默认权限

2026-09-11：S01 本地 PASS，7d71e90 / autodev/PA02/S01/v1。网页可复制包含真实地址/一次性凭据/动作与边界的完整 Agent 接入文本；独立客户端确认连接回执，pending 不获执行权限。基础操作默认预选、中文解释、高级折叠，Human 仍选择任务并确认；授权后可网页调整，变更立即生效且不改 Execution owner/boundary。171 项完整回归、8 项账号/权限测试、实际网页与独立客户端通过；17 条合成事件，0 位真实参与者，无模型调用。见 development/PA02_ACCEPTANCE.md、autodev/PA02.state.json。

8876 本地门户已更新，原事件指纹不变并已有一致性备份；未推送、未云端部署。复制说明不能让纯文字或无法访问本机 localhost 的云端 Agent 自动获得网络能力；下一步仍是确认云端隔离入口与常驻部署，正式用户试验尚未启动。

## 当前：PA01 普通用户网页门户

2026-09-11：用户要求不再安装依赖或执行命令，正式用户试用推迟至网页入口完善之后。PA01 S01/S02 已本地 PASS，账号注册/登录、服务端固定 Human 身份、目标任务创建发布、所属 Agent 凭据/授权、网页协议客户端及分离审查验收可用。169 项完整回归，最终网页双账号流程 16 条合成事件，后续 6 项安全回归通过；0 位真实参与者、未调用模型。检查点 6a25577 / autodev/PA01/S01/v1、a1ce994 / autodev/PA01/S02/v1。见 development/PA01_ACCEPTANCE.md、PORTAL_USER_GUIDE.md 与 autodev/PA01.state.json。

普通用户本地入口改为 http://127.0.0.1:8876 ，独立账号库和开发侧后台进程；8877 旧合成控制台保留。下一步核验并提交云端隔离入口/TLS/常驻服务部署方案供确认，再做正式用户测试；不要再要求用户运行 Python/Node 或手动启动后端。deploy/test-portal 是未部署的候选包。未 push、未云端部署、未改现有域名；当前不是关机后仍可用的云端服务。

## 当前：UX02 连续验收与恢复

2026-09-11：UX02 S01 已本地 PASS。从零 Execution/Knowledge 的隔离库连续完成 4 个 HTTP Agent 注册、浏览器授权/验收、知识形成、失效与新任务重验；80 条合成事件，2 次服务实例重启，幂等重试与事件 replay 通过。163 项完整回归、独立确定性 Review/Audit 通过；首次 Review 配置错误及修复记录保留。新增所属 Human 确认 Agent 恢复入口、执行待办及中文知识状态。见 development/UX02_ACCEPTANCE.md 与 development/CONTINUOUS_TRIAL.md；状态 development/autodev/UX02.state.json。checkpoint 18c0761 / autodev/UX02/S01/v1。统一入口仍为 8877，旧试用数据未导入本轮测试记录。未推送、未部署，不代表真人试点或云端持续运行。

下一步：按试用指南在统一入口亲自走查角色待办与知识变化，收集具体交互问题再修复；不要因本轮合成 PASS 自动启动真人 Pilot、接入公司数据或恢复云端写回。

## 当前：UX01 统一试用入口

2026-09-11：统一启动器、关联字段带入、按 Human 隔离的页面内存草稿及待办导航已实现，S01 已本地 PASS，163 项回归及实际浏览器验证通过；见 development/UX01_ACCEPTANCE.md，状态见 development/autodev/UX01.state.json，规格见 development/milestones/UX01_UNIFIED_WORKSPACE.md。后续使用固定本地 8877 入口；旧实验室保留。未推送、未部署。

## 当前：R01 知识失效与新任务重验

2026-09-11 用户已确认此轮工程。影响记录、Agent 问题报告、修订理由、新重验任务、替代能力包和完成记录已实现；实际网页＋独立 Agent 流程已跑通。S01–S03 已本地 PASS，完整测试 161 项，实际浏览器＋独立 Agent 运行 65 条合成事件；验收和恢复入口见 development/R01_ACCEPTANCE.md；范围见 development/milestones/R01_REVALIDATION.md。仅本地，不推送/部署，不进入真人 Pilot。

## 当前：M03 最小可追溯学习闭环

2026-09-11 用户已确认开发 M03。先读 development/milestones/M03_LEARNING_ORGANIZATION.md 与 development/autodev/M03.state.json；S01–S04 已本地 PASS，152 项测试通过，实际浏览器＋独立 Agent 跨任务复用产生 38 条合成事件；见 development/M03_ACCEPTANCE.md。范围为 Evidence 关系/快照、独立验证的有界 Knowledge 版本、授权复用和 Capability 候选/复现/重验信号。不是完整学习组织或真实效果验证；未推送/部署。下一步试用可追溯来源链并补充反证/版本变化的复验体验，暂不跳入 Human Pilot。

## 2026-09-11 · AA02 联合工作台

当前用户授权优先项：AA02 Human × Agent 网页联合工作台，插入 M03 前。注册审批、任务/执行、边界决策、正式 Return 与分离验收页面已实现；136 项回归及实际 Edge 浏览器＋独立 Agent 进程联调通过（18 条合成事件，0 位真实 Human）。AA02 S01 本地 PASS：63d92f3 / autodev/AA02/S01/v1；验收及试用入口见 development/AA02_ACCEPTANCE.md。操作说明：development/milestones/AA02_HUMAN_AGENT_WORKSPACE.md。未推送、未部署；原域名项目不变。


最后更新：2026-09-10。

| Milestone | Priority / Phase | 状态 | Outcome |
|---|---|---|---|
| M00 — Design Handoff | P0 / Phase 0 | Complete | 冻结设计、文档与视觉语义可被新开发者接续 |
| AD00 — Autonomous Development Runtime | Cross-phase through Phase 8 | **Harness + local Codex smoke PASS / Cloud host pending** | 持久状态、独立校验、恢复、检查点及真实模型提案验证 |
| M01 — Minimum Organization | P0 / Phase 2–3 | **Complete — M0 simulation engineering; delivery verified** | 3 HAU 围绕 1 Goal 跑通多 Execution 的完整 M0 闭环 |
| M02 — Synthetic Organization | P1 / Phase 4 | Local S01–S04 PASS within declared coverage; not pushed/deployed | 60 Execution / 536 事件；Goal Challenge、并发/恢复与本机工作台验证；见 M02_ACCEPTANCE |
| AA01 — Independent Agent Access | P1 / Phase 4, M0 | Local S01–S03 PASS; not pushed/deployed | 注册/受控授权/独立客户端；133 项测试及模型辅助协议联调；见 AA01_ACCEPTANCE |
| M03 — Learning Organization | P1 / Phase 5 | Minimal S01–S04 local PASS; full learning mechanisms incomplete | 152 tests / 38 synthetic events; see M03_ACCEPTANCE.md |
| M04 — Human Pilot | P2 / Phase 6 | Planned | 5–10 人、2–4 Cycle 的真实行为基线 |
| M05 — Value & Culture | P2 / Phase 7 | Planned | Contribution → Reward / Honor 的可验证机制 |
| M06 — Bounded Automation | P3 / Phase 8 | Planned | 低风险、可复现能力的 Organization-owned Agent 执行 |
| M07 — 60-person Experiment | P3 / Phase 9 | Planned | 约 60 人一年实验与 E01–E08 研究运行 |

状态词只描述实现进度，不替代 Frozen/Tunable/Experimental 或 M0/M1/M2 分类。

## 当前 Milestone

[`AA01 — Independent Agent Access`](milestones/AA01_AGENT_ACCESS.md) 已完成本地验收；下一工程 M03 规格。

Milestone 只有在定义的 Outcome、验收情景、证据和接续条件全部满足时才能标记 Complete；文档存在不等于实现完成。

<!-- AUTODEV:START -->
## AutoDev repository projection

| Stage | Status | Checkpoint tag |
|---|---|---|
| S01 Specification Freeze | PASS | autodev/M01/S01/v1 |
| S02 Reality Foundation | PASS | autodev/M01/S02/v1 |
| S03 Goal + Task + Execution Core | PASS | autodev/M01/S03/v1 |
| S04 HAU + Representative Agent + Runtime | PASS | autodev/M01/S04/v2 |
| S05 Free Work Space + Progress + Boundary/Escalation | PASS | autodev/M01/S05/v1 |
| S06 Return + Review + Acceptance + Selection | PASS | autodev/M01/S06/v1 |
| S07 End-to-End Integration | PASS | autodev/M01/S07/v1 |
| S08 Simulation + Audit + Final Acceptance Package | PASS | autodev/M01/S08/v3 |

Source: `development/autodev/M01.state.json`. Simulation evidence is not Human Pilot or E01–E08 evidence. Phase 9 requires real Humans, time and experimental results.
<!-- AUTODEV:END -->
