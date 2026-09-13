# M04 远程测试入口部署决策包

更新时间：2026-09-13

状态：**Draft / NO-GO until blockers close**
目的：为 3–5 人理解与可用性测试提供隔离、可回滚、非生产的网页入口。

本文件不是部署授权。GitHub 状态收敛已完成；当前未安装 systemd 服务、未修改 Nginx/域名、未迁移数据、未创建真实账号。

## 推荐拓扑

```text
测试用户 / 外部 Agent
        │ HTTPS
        ▼
独立测试域名或隔离入口
        │ TLS termination + exact Host
        ▼
现有 Nginx 中新增隔离 location/server
        │ reverse proxy to 127.0.0.1:18876
        ▼
ai-native-test.service（单进程、独立系统用户）
        │
        └── /srv/ai-native-test/data/portal.sqlite3
```

建议保持应用只监听 `127.0.0.1:18876`，不直接暴露公网端口；代码、数据、日志和备份均不得复用现有 AEGPC 项目。

## 已有候选实现

- `deploy/test-portal/ai-native-test.service`：独立用户、`NoNewPrivileges`、`PrivateTmp`、只允许数据目录写入、失败重启。
- `organization.portal`：精确 Origin/Host 校验、CSRF、Secure/HttpOnly/SameSite Cookie、8 小时会话、scrypt 密码哈希、注册/登录限速。
- 单进程 SQLite 写入约束已声明；备份要求使用 SQLite 在线 backup 或停服后的完整复制。
- 普通用户入口不要求安装 Python/Node 或手动启动后端。

这些是代码和模板证据，不是运行中服务证据。

## 部署前阻断项

| 项目 | 当前证据 | 状态 | 关闭条件 |
|---|---|---|---|
| 入口与域名 | 尚未指定 | BLOCKED_DECISION | 选择独立测试域名或明确隔离路径，确认不覆盖现有站点 |
| Nginx/TLS | 只有应用侧 Origin 约束 | BLOCKED_ENGINEERING | 形成最小配置、配置检查、证书路径和回滚片段 |
| 健康检查 | 未发现显式 `/health` | BLOCKED_ENGINEERING | 增加不泄露数据的 readiness/liveness 检查并测试 |
| 请求日志 | `log_message` 当前被抑制 | BLOCKED_ENGINEERING | 定义访问/错误日志、request id、保留期和敏感字段脱敏 |
| 反代来源地址 | 限速目前使用 socket client IP | BLOCKED_ENGINEERING | 明确信任代理边界并验证限速不会把所有用户合并或信任伪造头 |
| 数据迁移 | 当前声明使用新库、无旧库迁移 | READY_WITH_CONDITION | 首轮坚持全新隔离库；禁止导入旧实验或公司数据 |
| 备份恢复 | 有原则，无脚本与演练回执 | BLOCKED_ENGINEERING | 提供在线备份/停服备份命令、校验、恢复演练与 RPO/RTO |
| 资源限制 | systemd 有隔离，无 CPU/内存/文件数上限 | BLOCKED_ENGINEERING | 给出保守限制并完成压力与失败恢复检查 |
| 版本与回滚 | 建议 release 目录，但未固定 artifact | BLOCKED_ENGINEERING | 固定 commit/artifact/hash，保留上一版，只切换 `current` 链接 |
| 监控与告警 | 未定义 | BLOCKED_ENGINEERING | 定义进程、HTTP、磁盘、备份失败和异常登录的最小告警 |
| 远端代码状态 | 2026-09-13 远端 `main` 已读回验证到 `d6025e0`，必要 annotated checkpoint tags 已推送 | READY | 后续提交继续执行审计、push 和远端读回；Git 交付不冒充服务部署 |

## 建议部署单元

- 系统用户：`ai-native-test`，禁止交互登录。
- 根目录：`/srv/ai-native-test/`。
- 发布目录：`releases/<commit>/`；`current` 仅指向一个已校验发布。
- 数据：`data/portal.sqlite3`，权限仅属于服务用户。
- 配置：`portal.env` 只含非秘密 Origin；任何秘密进入独立受限配置，不进 Git、聊天或日志。
- 监听：`127.0.0.1:18876`；公网只经 HTTPS 反代。
- 首轮用户：仅 3–5 位测试者，关闭公开注册或使用受控邀请码后方可开放。

## 部署前验证

- 171 项本地回归继续通过；新增健康、反代、日志和备份测试。
- 在隔离环境完成双账号、Agent pending/approve/revoke、跨账号拒绝、CSRF/Origin/Host 拒绝。
- 验证凭据不进入事件、URL、网页截图、Nginx/应用日志。
- 验证服务重启后账号、任务、事件和 Agent 授权保持一致。
- 验证备份可恢复到新目录，恢复前后记录数量与关键事件指纹一致。
- 验证停止服务和回滚不会修改现有 AEGPC 项目、Nginx 其他 server 或数据库。

## 建议发布步骤（仅供审查）

1. Human 选择入口并批准精确变更范围。
2. 核验远端 commit/tag，构建带 SHA-256 的发布包。
3. 在隔离目录安装新 release 和全新数据库，不导入旧数据。
4. 安装但暂不公开入口；本机回环执行健康与安全 smoke。
5. 新增独立 Nginx 配置，先做配置检查，再 reload。
6. 通过 HTTPS 执行双账号与 Agent 全闭环测试。
7. 创建并校验首个备份，完成一次恢复演练。
8. 只向 3–5 位指定测试者开放；记录时间、版本和回执。

## 停止与回滚

- 立即停止入口：撤下独立 Nginx server/location 或切换为维护响应，再停止 `ai-native-test.service`。
- 应用回滚：停止服务，将 `current` 切回上一已验证 release，保持数据库不变；若 schema 不兼容则使用部署前备份恢复到新文件，禁止覆盖唯一副本。
- 数据回滚前必须保留故障库和审计日志；不得删除真实测试证据。
- 回滚后重新执行健康、登录、权限隔离和只读事件核对。

## Human 决策

进入部署前仍需用户明确选择并批准：

1. 精确入口（域名或路径）；
2. 精确服务器、目录、端口和 Nginx 配置文件；
3. 是否允许 push 指定 commit/tag；
4. 维护窗口、可接受停机和回滚阈值；
5. 首批测试者与注册方式。

在上述选择与工程阻断项关闭前，裁决保持 **NO-GO**。
