# Next Actions

## 当前：UX01 统一试用入口

2026-09-11：统一启动器、关联字段带入、按 Human 隔离的页面内存草稿及待办导航已实现，S01 已本地 PASS，163 项回归及实际浏览器验证通过；见 development/UX01_ACCEPTANCE.md，状态见 development/autodev/UX01.state.json，规格见 development/milestones/UX01_UNIFIED_WORKSPACE.md。后续使用固定本地 8877 入口；旧实验室保留。未推送、未部署。

## 当前：R01 知识失效与新任务重验

2026-09-11 用户已确认此轮工程。影响记录、Agent 问题报告、修订理由、新重验任务、替代能力包和完成记录已实现；实际网页＋独立 Agent 流程已跑通。S01–S03 已本地 PASS，完整测试 161 项，实际浏览器＋独立 Agent 运行 65 条合成事件；验收和恢复入口见 development/R01_ACCEPTANCE.md；范围见 development/milestones/R01_REVALIDATION.md。仅本地，不推送/部署，不进入真人 Pilot。

## 当前：M03 最小可追溯学习闭环

2026-09-11 用户已确认开发 M03。先读 development/milestones/M03_LEARNING_ORGANIZATION.md 与 development/autodev/M03.state.json；S01–S04 已本地 PASS，152 项测试通过，实际浏览器＋独立 Agent 跨任务复用产生 38 条合成事件；见 development/M03_ACCEPTANCE.md。范围为 Evidence 关系/快照、独立验证的有界 Knowledge 版本、授权复用和 Capability 候选/复现/重验信号。不是完整学习组织或真实效果验证；未推送/部署。下一步试用可追溯来源链并补充反证/版本变化的复验体验，暂不跳入 Human Pilot。

## 2026-09-11 · AA02 联合工作台

当前用户授权优先项：AA02 Human × Agent 网页联合工作台，插入 M03 前。注册审批、任务/执行、边界决策、正式 Return 与分离验收页面已实现；136 项回归及实际 Edge 浏览器＋独立 Agent 进程联调通过（18 条合成事件，0 位真实 Human）。AA02 S01 本地 PASS：63d92f3 / autodev/AA02/S01/v1；验收及试用入口见 development/AA02_ACCEPTANCE.md。操作说明：development/milestones/AA02_HUMAN_AGENT_WORKSPACE.md。未推送、未部署；原域名项目不变。


最后更新：2026-09-10。此页是开发行动权威；不从聊天推断完成情况。

最高优先级约束：先做本地工程和独立服务器测试；不改现有域名项目。正式推送/部署前提供具体交付与回滚包并取得确认。云端自动写回已暂停，不自动恢复。海外实例不作为当前待用户提供的必备条件；云端模型路线暂缓，不阻断无模型服务依赖的工程验证。

## 已完成的交付与接续核对

1. 核对 `autodev/DELIVERY.json` 中的远端 commit/tags、Actions verify/resume 及 Obsidian 投影回执；缺失项只能记 pending/blocked，不能推断成功。
2. 恢复执行使用 `python -m autodev.runtime run`；已 PASS 的 Stage 不重复创建标签。修复新缺陷需新 revision、重测和新标签。

## Agent 接入已完成

AA01 S01–S03 本地 PASS，133 项完整测试通过；独立客户端和真实模型生成 Return 的 HTTP 联调通过，18 条合成事件。先读 `AA01_ACCEPTANCE.md` 与 `milestones/AA01_AGENT_ACCESS.md`；Human 审批目前使用测试控制 CLI，尚未接入生产身份或新网页。

## 后续工程

3. M02 S01–S04 已本地 PASS；完整套件 122 项、整合场景 536 事件/16 断言通过，工作台 Goal Challenge 已浏览器验证。先读 `M02_ACCEPTANCE.md` 与明确的覆盖限制；不要将结果描述为已推送/已部署或完整 Goal 生命周期实现。
4. 准备 M03/M1 Evidence → Knowledge → Capability 的工程规格，继续遵守冻结原则。保留 Goal 完整生命周期、重挂接与多 Goal 依赖图的显式后续项，不用 M02 局部实现冒充这些机制完成。模型云端路线暂缓，既有 Actions 已暂停。
5. 再按 ROADMAP 进入 M1 Learning；不能以 M01 的测试通过代替真实组织学习或文化效果证据。

## Human 决策包

参见 `autodev/HUMAN_DECISIONS.json` 与 `autodev/CLOUD.md`。模型路径、资源政策与仓库权限已由用户决定，不重复请求。尚需完成云端运行环境与安全登录配置；若目标 runner 需要用户交互登录，再提交具体登录操作。未验证前不声称云端无人代码编写已启用。
真人 Pilot、真实公司数据/权限、Risk、Reward 或冻结设计变更各自另设 Gate。

## 不抢占工程主线

Phase 1 理解测试、真实业务任务准备可继续，但不得伪造参与者、样本或实验结果。
Phase 9 不能被 AutoDev 自动标记完成。

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
