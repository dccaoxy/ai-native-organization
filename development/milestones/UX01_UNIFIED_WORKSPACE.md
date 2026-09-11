# UX01 — 统一本地入口与连续操作

用户已授权继续本地工程。单一后续试用入口 http://127.0.0.1:8877，由 `python -m organization.workspace` 启动；不会停止或改写旧 8878/8879/8880 示例。

## 入口与数据

统一数据库 `.autodev/unified/workspace.sqlite3`，独立控制密钥 `.autodev/unified/workspace.key`，无秘密的启动位置记录 workspace.json。首次可明确指定 --seed-from，使用 SQLite 一致性备份复制一份现有本地实验数据；保留事件与历史，不合并多个实验室、不覆盖现有统一数据库、不改源数据库。复制会保留源库的注册和授权记录；旧 Agent 身份文件受原 URL 绑定约束，不应手改 URL 绕过，后续用新的 identity-file 明确注册。

默认目录已存在时直接恢复同一数据库与控制密钥。当前是前台本地进程，未承诺跨会话或关机持续运行；端口占用时退出报错，不自动杀进程或切换到另一个入口。没有生产身份认证或发布行为。

## 页面减负

- 当前测试 Human 的待办入口：注册审批、Review、Acceptance、Selection、候选验证、知识重验；仅导航，不执行决定或自动切换身份。
- 选择候选后带入当前证据编号；修订带入旧内容、指定验证人和待重验 Task；新任务带入来源 Goal/Boundary/责任人，生成新编号。
- 替代能力包带入旧组件供核对；结果使用记录与 Return、重验计划与复现记录在唯一匹配时关联，存在多个候选时仍需选择。
- 影响原因编号需点击“带入待回应问题编号”，并填写逐项回应理由。所有判断、支持/反驳、授权权限、审查结论都不自动通过；服务端验证保持原样。
- 学习表单草稿只存在当前页面内存，按测试 Human 分开。刷新状态及切换身份保留草稿；退出/整页重载清除。提交成功只清除对应表单；失败重试保留请求编号，避免重复新建。

草稿不会写入组织事件或 Free Work Space 记录，也不会写入 localStorage。关联源变化会刷新关联字段；已有草稿优先保留，若后端有新证据，提交时仍须通过完整性检查。此轮未替换所有原有 Review/Return 表单的草稿行为。

## 验收 S01

依赖 R01 本地 PASS。输入 organization/tests/契约及实际浏览器回执；输出统一启动器、表单联动、待办导航、测试及 commit/tag/artifact。

退出标准：备份源记录不变、已有目标不可覆盖、重启保留密钥；实际浏览器验证证据带入、无自动判断、刷新/角色隔离/退出草稿清理；检查前后组织事件完全相同；原 R01 两个独立 Agent＋网页全流程回归；完整 Python 套件与冻结检查通过。

```console
python -m unittest tests.test_workspace -v
python -m organization.workspace_demo
python -m autodev.runtime run --plan development/autodev/UX01.json
```

浏览器仍需 Node/Playwright；--node、--modules、LAB_BROWSER_CHANNEL=msedge 可使用本机安装。source-bound 报告在 development/autodev/workspace-demo。测试是合成环境，不是真实 Human 效果评价。

Review/Audit 是独立进程确定性校验，非独立 LLM 或真人体验认证。repair budget=1；失败持久化后停止。正式推送/部署、恢复自动云端写回、真实系统权限和冻结 L1/L2 改动另需 Human 确认。

回滚：停止统一进程，旧实验室数据完整保留；独立 checkout 或新 revert，配合对应版本数据。不覆盖标签或历史，不 force-push。
