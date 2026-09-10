# Next Actions

最后更新：2026-09-10。此页是开发行动权威；不从聊天推断完成情况。

## 已完成的交付与接续核对

1. 核对 `autodev/DELIVERY.json` 中的远端 commit/tags、Actions verify/resume 及 Obsidian 投影回执；缺失项只能记 pending/blocked，不能推断成功。
2. 恢复执行使用 `python -m autodev.runtime run`；已 PASS 的 Stage 不重复创建标签。修复新缺陷需新 revision、重测和新标签。

## 后续工程

3. Codex adapter 本机真实测试已通过。按 `autodev/CODEX_RUNNER.md` 接入明确的可信云端主机/私有执行环境并实际登录；公开仓库不可采用官方账户登录 CI 方案。现有 Actions 继续无模型凭据验证。不要重复索取预算和本仓库权限。
4. 为 M02 / Phase 4 建立机器 Stage Specs，扩大至约 10 HAU、3 Goal、30 Task、50–100 Execution，显式指定 model_write_paths 并保留分离 Reviewer/Auditor、反证检查、摘要绑定、有限失败重试与所有既有 Human Gates。新计划才绑定模型 adapter；不重写 M01 通过标签。
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
