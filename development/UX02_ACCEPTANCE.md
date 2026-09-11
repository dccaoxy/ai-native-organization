# UX02 连续验收包

本地工程 S01 PASS；未推送、未部署。试用入口 http://127.0.0.1:8877 ，简短路线见 [CONTINUOUS_TRIAL.md](CONTINUOUS_TRIAL.md)。

- Commit：`18c0761045193d0eaba3883eb4d303f951270920`
- Tag：`autodev/UX02/S01/v1`
- Artifact：`development/autodev/runs/UX02/S01/2/artifact.zip`
- SHA-256：`4eeaa6ff92c6393f78356ba76ac904eed97c578e0b3383feda7bab06d697682a`

## 已验证

163 项完整 Python 测试通过；实际 Edge 浏览器 + 4 个独立 HTTP Agent 注册，在同一临时库从 0 Execution、0 Knowledge 连续产生 80 条合成事件。两个来源 Return 经独立 Review/Acceptance、一个独立 Selection，再形成知识。新 Agent 采用后显式报告离线，所属 Human 确认恢复并恢复 Execution，随后报告失败与知识问题；修订后的知识与替代能力包经新任务、另一个客户端、分离审查和验收后完成重验。

两次停止并重建 HTTP 服务实例，事件分别保持 13→13、53→53；重启后的 claim/ack 重试不重复记事件。最终 replay 与投影完全一致，旧知识 superseded、旧能力包 stale、新能力包 reproduced。非所属 Human 的恢复按钮禁用。原有字段带入、草稿刷新/角色隔离/退出回归通过，页面窄屏未溢出；截图和不含 token 的事件证据已保存。

报告：`development/autodev/continuous-demo/report.json`、`evidence.json`、`continuous-desktop.png`、`revalidation.png`；草稿证据：`development/autodev/workspace-demo`。报告绑定源码摘要。

## 修复与自动 Gate

补齐所属 Human 的“确认 Agent 已恢复”动作，明确只记录运行状态，不启动客户端；待办加入离线 Agent/未完成执行。知识状态中文化，区分候选解释的历史判断与当前知识有效性。

第一次独立 Review 因 plan 引用了不存在的 tests.test_agent_gateway 失败，修正为仓库实际 tests.test_agent_access 后，以 attempt 2 重跑 Build/Test/Review/Audit 并 PASS。没有删除失败回执或放宽 repair budget。测试、配置输出、冻结完整性与列出的原则检查全部自动通过，findings 为空。确定性 Reviewer/Auditor 分进程执行，不是独立 LLM/Human 语义认证。

## 重现命令（本机）

```powershell
$env:LAB_BROWSER_CHANNEL='msedge'
python -m organization.continuous_demo --node C:\Users\caoxy\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe --modules C:\Users\caoxy\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules
python -m organization.workspace_demo --node C:\Users\caoxy\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe --modules C:\Users\caoxy\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\node_modules
python -m autodev.continuous_acceptance
```

重新执行 demo 会生成一批新的合成 ID/报告，请先检查工作树。已 PASS 的 Harness run 会跳过阶段；若修改源码，应创建新 revision 并重新验收，不能沿用旧 PASS。

## 边界与接续

0 位真实 Human，未调用模型。仅重建同一测试进程内的服务实例，非操作系统崩溃/断电测试；显式 Agent 离线信号不等于自动心跳检测。全套测试存在已有的 HTTPError 清理 ResourceWarning，不影响通过结果。

统一试用工作台已用新代码启动并做 HTTP 读回：57 条原有事件、2 个知识版本、1 个 passed 重验计划。临时验收数据未导入其中，未改变旧实验室。运行是本地前台 runner；会话结束或机器关闭后的持续服务没有承诺。若进程结束，`python -m organization.workspace` 恢复同一库。

本轮无待决的 Human Gate；正式推送/部署、恢复云端自动写回、真人试点和真实公司权限仍需另行确认。下一步是按试用指南检查可理解性，不能把工程通过当作真实组织有效性。

恢复读取 UX02.state.json、对应 attempt 2 receipts、规格与本包。回滚使用独立 checkout 或新 revert，保留数据库、历史和标签；本轮无 schema 迁移，不 force-push。
