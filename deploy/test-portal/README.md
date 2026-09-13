# 部署候选包：账号式测试门户（尚未安装）

本包供开发/运维使用。试用者只打开网址、注册账号、登录，不安装 Python/Node，不执行命令。

- 独立路径建议 `/srv/ai-native-test/`，独立系统用户 ai-native-test，数据仅 data/portal.sqlite3；禁止复用旧实验库。
- 单进程服务监听 127.0.0.1:18876。systemd 模板提供失败重启和开机启动能力，但未安装/启用。
- 运行需要服务器 Python 3.11+ 标准库；Node/Playwright 只用于开发验收，不是平台运行依赖。
- portal.env 必须设置明确的 HTTPS `PORTAL_ORIGIN`（不带路径或结尾斜线）；反向代理需保留匹配的 Host。TLS 终止和访问入口须另行确定，不擅自改现有 AEGPC.CN、Nginx 或端口映射。
- 单一共享测试组织，注册页明确提示协作记录对成员可见。不是多租户生产产品；暂无邮箱校验、找回密码、邀请域限制或外部模型托管。不能导入真实公司/个人敏感资料。
- 密码 scrypt+随机盐；会话只存 token 哈希，8 小时过期；HTTPS Cookie Secure/HttpOnly/SameSite=Strict；请求 Origin/CSRF 校验；注册/登录限速；账号身份由服务端确定。
- 注册和会话保存在 SQLite 中；进程重启继续。只允许一个服务进程写此数据库，不能使用多 worker。
- 备份使用 SQLite 在线 backup 或停服务后复制完整数据库；不要直接复制正在写入且带 WAL 的单个主文件。
- 回滚：停止本独立服务，恢复上一代码目录；账号数据库保留，勿覆盖旧库。停用服务不应触碰既有域名项目。数据库 schema 此次只有新独立库新增表，无旧库迁移。

正式推送、云端安装、启动常驻服务或配置入口之前，提交具体主机/目录/端口/访问 URL/备份回滚步骤，取得用户确认。当前模板不是部署完成的证据。

## 2026-09-13 Gate B 本地工程补充

- `GET /health` 执行 SQLite `quick_check`，只返回服务状态，不返回账号、事件或版本数据。
- 应用日志只记录 request id、方法、无查询参数的路径、状态、耗时和客户端 IP；不记录 Header、Cookie、Authorization 或请求正文。
- 仅当 socket peer 在重复提供的 `--trusted-proxy` 列表内时，才使用 `X-Forwarded-For` 的首个合法 IP；示例 service 只信任 `127.0.0.1`。
- `nginx.example.conf` 必须复制成独立配置并替换占位符。配置会覆盖客户端传入的 `X-Forwarded-For`，不得改成追加不可信链。
- 在线备份：`python -m organization.portal_backup backup SOURCE.sqlite3 DEST.sqlite3`。
- 校验备份：`python -m organization.portal_backup verify DEST.sqlite3`。
- 恢复演练：`python -m organization.portal_backup restore DEST.sqlite3 NEW.sqlite3`；目标已存在时拒绝覆盖。
- systemd 模板新增 journal 输出、30 秒停止窗口、512 MB 内存、100% 单核 CPU、64 tasks 和 4096 文件描述符上限及额外内核保护。

以上仅通过 Windows 本地自动化测试；Nginx 语法、systemd sandbox、证书、真实反代 IP、journal、资源上限与定时备份必须在目标 Linux 隔离环境重新验证。
