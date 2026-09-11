# R01 本地验收：知识失效与新任务重验

2026-09-11，S01–S03 本地 PASS，未推送、未部署；冻结基线不变。

已跑通：独立 Agent 失败上报 → 影响记录 → Human 创建新重验 Task → 带理由修订 Knowledge → 独立验证 → 新能力包 candidate → 新授权 Agent 在新任务试用 → 分离 Review/Acceptance/Outcome/Reproduction → 完成重验。

## 验证

- 完整测试 **161 项通过**，本轮新增重验测试 9 项。包括权限/Boundary、错误任务、缺理由、提前完成、拒绝采用后的失败、晚到新问题及普通使用恢复门槛。
- 实际 Edge 浏览器与两个独立 Agent 进程，**65 条合成事件**；源代码摘要绑定报告，事件 replay 与最终状态一致。固定测试数据，无模型调用，真实 Human 参与者 0。
- 旧 Knowledge 保持 superseded，旧能力包保持 stale；新包在新的重验任务成功后为 reproduced。重验前限制在计划 Task 中试用，完成后仍不超出原授权。
- 独立进程 Review/Audit 通过，不等同独立 LLM/真人语义认证。既有 HTTP 测试 ResourceWarning 没有导致失败。

## 本地检查点

| Stage | Commit | Tag | Artifact |
|---|---|---|---|
| S01 | `677fb86` | `autodev/R01/S01/v1` | [代码包](autodev/runs/R01/S01/1/artifact.zip) |
| S02 | `4432eff` | `autodev/R01/S02/v1` | [代码包](autodev/runs/R01/S02/1/artifact.zip) |
| S03 | `883493c` | `autodev/R01/S03/v1` | [代码包](autodev/runs/R01/S03/1/artifact.zip) |

标签与代码包摘要均已核验，详见 [持久状态](autodev/R01.state.json)。[浏览器报告](autodev/revalidation-demo/report.json) · [事件与状态](autodev/revalidation-demo/evidence.json) · [页面截图](autodev/revalidation-demo/revalidation.png)。

## 查看与恢复

本地独立示例：http://127.0.0.1:8880 。示例来自实际执行的合成测试命令，使用 outcome 失败反馈，与浏览器证据中的 Agent issue 上报是不同实例。

控制密钥在 `.autodev/revalidation-workspace.key`，数据库 `.autodev/revalidation-workspace.sqlite3`；都留在本机忽略目录。用对应密钥连接后查看“学习与复用”的影响卡和步骤 8–11。不会自动提供密钥，也不是生产用户认证。

本地进程停止后可恢复：

```console
python -m organization.agent_gateway --port 8880 --db .autodev/revalidation-workspace.sqlite3 --operator-key-file .autodev/revalidation-workspace.key
```

AutoDev 恢复：`python -m autodev.runtime run --plan development/autodev/R01.json`。不覆盖已通过标签。浏览器复现要求和完整字段见 [R01 规格](milestones/R01_REVALIDATION.md)。

## 限制、下一步和回滚

证明的是本地工程流程，不是知识真实性或真实组织学习效果。尚未实现完整外部 Tool/Data/Runtime 依赖监听、全组织广播、跨不同作者/Goal Authority 的重验发起、真实用户认证。

下一步可统一当前本地试用入口、减轻多步骤表单输入，并做一次连续用户试用；真实 Pilot 另需明确范围和授权，不自动启动。

旧数据库及服务未改动，正式推送/部署/恢复云端写回仍须确认。停止本例进程即可停止试用；保留数据库便于恢复。回退代码须配合升级前数据库备份或新实验室，使用独立 checkout 或新 revert，不 force-push 或覆盖历史。
