# Next Actions

最后更新：2026-09-10。此页是开发行动权威；不从聊天推断完成情况。

最高优先级约束：先做本地工程和独立服务器测试；不改现有域名项目。正式推送/部署前提供具体交付与回滚包并取得确认。云端自动写回已暂停，不自动恢复。海外实例不作为当前待用户提供的必备条件；云端模型路线暂缓，不阻断无模型服务依赖的工程验证。

## 已完成的交付与接续核对

1. 核对 `autodev/DELIVERY.json` 中的远端 commit/tags、Actions verify/resume 及 Obsidian 投影回执；缺失项只能记 pending/blocked，不能推断成功。
2. 恢复执行使用 `python -m autodev.runtime run`；已 PASS 的 Stage 不重复创建标签。修复新缺陷需新 revision、重测和新标签。

## 后续工程

3. M02 S01/S02 本地验收已通过（10 HAU / 3 Goal / 30 Task / 60 Execution，531 事件；并发/错误输入测试通过），完整套件 112 项通过。查看 `autodev/M02.state.json` 和本地标签，不将本地结果描述为已推送或已部署。
4. 实现 M02 S03：先读冻结 Goal Specification/Mechanisms，再定义 `specs/M02.goal-challenge.json` 与明确的命令、事件及负面测试。保留 Human Goal Authority，不因 Challenge 静默改目的。补充能力缺口、脏数据与最终覆盖证据；当前 M02 不得标记完成。模型云端路线暂缓，既有 Actions 已暂停。
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
