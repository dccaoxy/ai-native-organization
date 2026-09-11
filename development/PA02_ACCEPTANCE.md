# PA02 验收与接续

已更新本机 http://127.0.0.1:8876 ，未 push 或云端部署。

- Commit：7d71e90f7fb14f3c6ea30f7f17e39dd5a211f6d2
- Tag：autodev/PA02/S01/v1
- Artifact：development/autodev/runs/PA02/S01/1/artifact.zip
- SHA-256：992939fc4435c2f3a471320fd385a330d7bdb74c41830560f045a92617ca09d1

## 用户流程

填写 Agent 名称 → 生成说明（新建待授权注册）→ 复制完整文本给能执行 HTTP 的 Agent → Agent 核验 /v1/me 并 POST /v1/connect → 网页显示接入回执。默认基础权限已选中，Human 只需选择允许任务并确认授权。pending 时 Agent 可以完成接入，但不能执行任务。approved 后读取真实 permissions/HAU/tasks，再领取、执行、正式 Return。

文本明确包含地址、私密凭据、注册编号、请求头、状态分支、请求格式、幂等/有限重试、失败/扩权边界和报告要求。无需再让用户解释 API。纯文字 Agent 或不能访问 localhost 的云端 Agent 无法仅靠文本完成；当前本机 URL 不代表云端可达。没有测试 LLM 对文本的理解能力，实际验证是独立确定性 HTTP 客户端。

基础权限为领取、确认执行、进度、正式结果/失败、阻塞、放弃/恢复执行、请求协助。高级选项中文解释且默认不勾选；审查、验收、选择、批准扩权不能授予 Agent。当前绑定的所属 Human 可保存权限调整，AgentAccessUpdated 入统一 Trail；收回立即生效，原 Execution owner/boundary/status 不改。

## 验证

完整 171 项测试通过；8 项账号/权限测试含跨用户与自授拒绝、收回即时生效、恢复范围、不可委托 Human-only 权限、执行归属不变、接入回执幂等和服务实例重启保留。独立 Review/Audit 均 PASS 且 findings 为空，冻结基线未改。

实际 Edge 浏览器生成文本，独立客户端从文本中提取配置并连接，未授权 claim 被拒绝；网页验证默认权限、修改权限后保持、两个账号分离审查/验收/选择。17 条合成事件、0 位真实参与者、未调用模型。报告与已清除 token 的截图见 development/autodev/portal-demo。

本地更新前做 SQLite 一致性备份 .autodev/portal/pre-pa02.sqlite3，保存事件指纹；仅重启本任务门户进程后 HTTP 读回最终资源，事件指纹不变。账号/原有组织数据未重置，旧 8877 实验室不变。连接回执是传输层接入记录，不是模型持续运行证明。

## 接续与回滚

读 PA02.state.json、规格与本包恢复；不要沿用旧源码的 PASS 回执。新增 portal_connections 表可保留，权限变更的正式事件不能删除。回退代码需确保仍可读取新事件，或以变更前一致性备份在独立目录恢复，不能覆盖活跃库或历史。

工程范围无待决 Human Gate。云端安装/入口/TLS/域名/正式 push 仍须具体方案获确认后执行。默认权限不等于自动授权所有任务；未启动正式用户实验。

## 独立子 Agent 实接入追加验证

2026-09-11 用户要求建立子 Agent 验证注册接入。使用同一门户代码的隔离实例，通过实际浏览器生成完整说明，将文件交给无主线程历史的独立子 Agent。子 Agent 实际执行 GET /v1/me → POST /v1/connect → GET /v1/me，均 HTTP 200，注册编号匹配；父侧独立读回唯一连接回执。状态 pending，未自行授权、未创建 Execution/Return。结果见 development/autodev/subagent-connect-check.json。
这是独立子 Agent 读取说明并调用真实 HTTP 的一次成功验证；其工具仍在本机，不能证明远端 Agent 能访问 localhost，也不能代表所有 Agent 均可理解执行。仅两条合成组织事件，账号和凭据位于忽略的隔离目录，不改用户门户数据。测试服务已停止，脱敏报告不含 token；没有 push 或云端部署。
