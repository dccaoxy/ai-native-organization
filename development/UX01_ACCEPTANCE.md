# UX01 统一入口与表单减负验收

2026-09-11，本地 S01 PASS；未推送、未部署。

## 以后使用这个入口

http://127.0.0.1:8877 。本轮从 R01 本地示例复制到独立统一库，原示例数据未覆盖。当前含两个知识版本和一个重验计划。

在仓库根目录启动/恢复：

```console
python -m organization.workspace
```

使用本机 `.autodev/unified/workspace.key` 中的密钥连接。统一数据库为 `.autodev/unified/workspace.sqlite3`。这些本地文件不进入 Git，密钥不出现在网页源码、URL 或报告中。保持启动进程运行；本地进程不保证跨会话常驻。

旧 8878/8879/8880 是历史实验室，不再作为后续默认入口；文件仍保留，没有合并历史。以后注册新测试 Agent 应使用新的身份文件：

```console
python -m organization.agent_client register --url http://127.0.0.1:8877 --identity-file .autodev/unified/agent.identity.json
```

## 本轮改进

- 待办导航根据当前测试 Human 显示审查、验收、选择、验证和重验入口。
- 候选证据、旧版知识内容、重验来源 Goal/Boundary/责任人、能力包组件及唯一匹配的结果引用可带入，提交前仍需核对。
- 授权、判断与理由不自动通过；问题编号需显式带入并解释回应。
- 学习表单按 Human 保存当前页面内存草稿，刷新状态与切换身份不会丢失；退出/页面重载清除。失败重试保留对象编号。

## 验证与边界

完整回归 163 项通过。实际 Edge 浏览器验证字段带入、无自动判断、刷新保留、身份草稿隔离、退出清理和窄屏；测试前后组织事件完全相同。R01 浏览器＋两个独立 Agent 进程的全流程也重新通过，局部回执在忽略目录 `.autodev/workspace-revalidation-check/`。

统一启动器验证一致性备份、保留源事件、禁止覆盖目标、恢复同一密钥。Windows 备份连接占用问题已修复并复测。既有 HTTP 测试仍有 ResourceWarning，无失败。

[源码绑定的浏览器回执](autodev/workspace-demo/report.json) · [页面截图](autodev/workspace-demo/prefill.png) · [机器状态](autodev/UX01.state.json)。

Checkpoint `c0dcd8632ab1b061afc9b1ce2e5d6a614a9480c5`，tag `autodev/UX01/S01/v1`。
[代码包](autodev/runs/UX01/S01/1/artifact.zip) SHA-256 `8aa58ea4f58f5711345544879ff8a833b5e3c524c8f6125a8271901f6bd207bc`，已核验标签和冻结基线。

仍是本地合成身份控制台，不是生产登录系统。此轮草稿覆盖学习表单，尚未覆盖全部原有 Return/Review 表单；没有自动业务判断或学习效果结论。完整范围和回滚见 [UX01 规格](milestones/UX01_UNIFIED_WORKSPACE.md)。

下一步可直接在统一入口连续试用，无需再开发新的实验室入口。发布或真实 Pilot 启动仍要单独确认；现有域名项目未改动。
