# AA02 — Human × Agent 联合工作台

用户已授权本地开发与联合测试；正式推送、部署、恢复云端写回另需确认。

## 范围

在 AA01 专用 loopback 服务上增加中文网页：注册列表、显式 HAU/Task/命令授权、撤销；Task/Execution/进展/边界申请；正式 Return 四字段；分离 Review、Acceptance、Selection；最近 100 条组织事件。当前 Human 下无权操作的按钮禁用，后端仍验证权限。阻塞或中断可由所属 Human 提交恢复说明，未决边界申请禁止恢复。

这是合成测试控制台，不是生产 Human 登录；操作者持有独立控制密钥并选择合成 Human。网页不自动提供密钥、不持久化到浏览器存储、不将密钥放入 URL；刷新/退出须重新连接。页面以 textContent 显示外部内容，CSP 禁止内联脚本与嵌套框架。同源 control API 允许浏览器调用；跨源、伪造 Host、Agent 凭据访问控制端均拒绝。Agent API 保持直接客户端限制。没有公网/TLS、多租户隔离或真实身份认证声明。

## 启动和实际操作

在仓库根目录运行以下命令（专用 lab 数据库，不连接旧工作台数据库）：

```console
python -m organization.agent_gateway --port 8877
```

另一个终端准备明确标注的合成测试任务和 Agent：

```console
python -m organization.agent_operator init-fixture
python -m organization.agent_client register
```

打开 http://127.0.0.1:8877 ，从本机 `.autodev/agent-operator.key` 文件读取控制密钥并输入页面，不向 Agent 提供。选择 H0，在注册卡填写 U0、Task T，勾选 claim、ack、progress、submit 后批准。再运行：

```console
python -m organization.agent_client run --task T --run-id human-trial-1
```

刷新页面，H1 填写证据并 Review；H0 根据标准 Acceptance；H2 说明理由并 Selection。拒绝和不可信选项默认优先，不自动判定通过。Agent 执行需独立 runner 启动，本页面不托管持续后台 Agent。

## S01 — 集成验收

依赖：AA01 S01–S03 已通过。输入：现有冻结契约、AA01 接口、页面源码及测试。输出：页面、同源受控端点、自动浏览器与独立 Agent 进程联调证据、Git commit/tag/artifact。

Exit criteria：完整 Python 回归通过；实际浏览器完成授权与三个独立结果决策，Task 关闭；错误 Human 的 Review 按钮不可操作；退出清除页面状态；窄屏无水平溢出；Agent/跨源/伪 Host 无法访问 Human 控制接口；冻结基线不变。证据见 `development/autodev/human-web-demo/`。

```console
python -m unittest discover -s tests -q
python -m organization.human_demo
python -m autodev.runtime run --plan development/autodev/AA02.json
```

浏览器验收需要 Node + Playwright 与浏览器，支持 `--node` 和 `--modules` 指定已有运行时；`LAB_BROWSER_CHANNEL=msedge` 可选择本机 Edge。默认 Playwright Chromium 缺失时必须配置现有浏览器或安装后重试，不能将缺失当 PASS。测试使用临时数据库/凭据并关闭服务，固定合成 Agent 输出，未调用模型、无真实 Human 实验。

## 发布与回滚

仅本地实验；不改既有域名/服务器。停止专用 lab 服务即可停止试用，保留其数据库/凭据以便恢复。需要旧版本时从 25e3b9a 创建独立 checkout 或新 revert 提交，不覆盖历史/tag。发布前提供具体目标、验证及回滚包等待用户确认。
