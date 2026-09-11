# PA01 网页账号门户验收

普通用户网页入口已实现并在本机运行：http://127.0.0.1:8876 。用户不需要安装依赖、执行终端命令、复制控制密钥或选择测试 Human。用户路径见 [PORTAL_USER_GUIDE.md](PORTAL_USER_GUIDE.md)。正式用户测试尚未开始，云端部署未执行。

## 验证结果

S01 完整 169 项 Python 回归通过。真实 Edge 浏览器从空账号库创建两个独立账号，完成目标/任务/责任人配置、发布、创建 Agent 凭据、明确任务和操作授权、浏览器协议客户端提交正式 Return、另一账号 Review、原账号 Acceptance/Selection；16 条明确合成事件，0 位真实参与者，未调用模型。刷新恢复会话、退出、重复执行幂等及窄屏检查通过。

S02 修正门户专用账号提示与移动端通知遮挡，重新跑完整网页路径与 6 项账号安全测试。独立 Review/Audit 均 PASS，findings=[]；冻结完整性不变。历史全套存在 HTTPError 清理 ResourceWarning，未出现失败。

针对身份冒用、跨账号 Agent 操作、CSRF/Origin、密码哈希、会话过期/退出失效、服务实例重建和命令幂等均有自动验证。源摘要和合成事件报告在 development/autodev/portal-demo；截图已清除 Agent token，不含密码。先前脚本曾错误等待隐藏 option 可见、在隐藏面板清理字段，两项测试脚本问题已修正后重跑成功。

## 本地检查点

| Stage | Commit | Tag | Artifact |
|---|---|---|---|
| S01 | 6a255770f757d73255214fea3893530ca1ac6bd7 | autodev/PA01/S01/v1 | development/autodev/runs/PA01/S01/1/artifact.zip |
| S02 | a1ce9940e48da66d29c176c3eaabca6a62af4a5d | autodev/PA01/S02/v1 | development/autodev/runs/PA01/S02/1/artifact.zip |

每个 artifact 的 SHA-256 及恢复事件见 PA01.state.json；均已核对。Review/Audit 是独立进程确定性验证，不是独立 LLM 或真人语义认证。另一个 Agent 可从 AGENTS/CURRENT_STATE/PA01 规格和 run receipts 接续，无需聊天。

## 运行与交付边界

独立门户库 .autodev/portal/portal.sqlite3；开发侧已启动隐藏本地后台进程，并通过 HTTP 读回最终页面资源。进程信息在忽略目录 process.json。未配置 Windows 开机自启，不承诺关机可用；不是云端持久服务。旧 8877 与旧库未迁移、未覆盖。

后台仍需 Python 运行平台，但普通用户无需安装或维护。Node/Playwright 只供开发侧验收。云端单进程 systemd 候选包位于 deploy/test-portal，独立 /srv/ai-native-test、loopback 18876、独立账户/数据库，包含自动重启、安全 Cookie/TLS origin 和回滚说明；尚未在服务器安装、启用或更改反向代理。

外部 Agent 使用网页生成的 Bearer token 和协议说明访问 /v1 API；需要用户已有的 HTTP Agent，不等于平台托管了 ChatGPT 模型。网页自带的是明确标识的确定性协议客户端。账号属于一个共享测试组织，不是多租户生产系统；无邮箱验证/密码找回/现实身份认证。事件继续标记 simulation=true，不把测试账号当真人实验数据。

## 下一步与 Human Gate

不再让用户执行后端命令或跑开发测试。剩余发布动作是确定并确认云端隔离访问入口、TLS 与服务安装，再执行服务器常驻验收；具体主机入口/端口转发未在本轮核验，不能宣称已具备远程访问。正式 push、部署、改域名或反向代理仍须用户确认，未自动执行；现有 AEGPC.CN 项目不变。

回滚仅停止本独立门户并恢复对应代码版本，保留账号库；旧控制台不受影响。部署前按 SQLite 一致性备份规则保存数据库，不直接复制活跃 WAL 主文件，不覆盖历史/tag，不 force-push。
