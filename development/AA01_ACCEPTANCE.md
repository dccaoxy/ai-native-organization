# AA01 本地验收包

2026-09-10：S01–S03 全部本地 PASS，未推送、未部署。

## 已交付

- 独立 Agent 注册/认证 HTTP 接口：注册默认 pending，Human 明确绑定 HAU、命令权限和 Task 白名单后才可执行。
- 独立进程客户端：领取、ACK、进展、阻塞/失败、正式 Return；相同请求重试不重复产生事件。
- 独立测试控制端：显式合成 Human 批准/撤销、Review、Acceptance、Selection。当前没有为此新增 Human 网页。
- 拒绝客户端伪造 actor、跨 Task/HAU 操作、未委托命令、自行扩权/验收；撤销和替换绑定后旧凭据失效；中断可检测。

## 验证与证据边界

完整 unittest 套件 133 项通过，其中 Agent 接入测试 11 项；AA01 三个 Stage 的确定性独立进程 Review/Audit 通过。冻结基线核验通过，未修改 L1/L2。测试有继承 HTTP 测试的 ResourceWarning，但无失败。

实际调用已登录 ChatGPT 账户的 Codex 生成 Return 内容，由独立进程客户端经真实本地 HTTP 提交，测试控制端完成闭环，共 18 条合成事件。报告与原始状态保留在 [模型测试报告](autodev/agent-model-demo/report.json)。真实 Human 参与数为 0。

模型未取得 Agent/operator 凭据；模型生成内容，协议步骤由客户端执行。本次不宣称模型自主规划、独立语义审查、真实业务验收或真人实验完成。

## 本地检查点

| Stage | Commit | Tag | Package |
|---|---|---|---|
| S01 | `0309d1a` | `autodev/AA01/S01/v1` | [artifact](autodev/runs/AA01/S01/1/artifact.zip) |
| S02 | `969bc1a` | `autodev/AA01/S02/v1` | [artifact](autodev/runs/AA01/S02/1/artifact.zip) |
| S03 | `02bd5d1` | `autodev/AA01/S03/v1` | [artifact](autodev/runs/AA01/S03/1/artifact.zip) |

上述标签均指向所列提交，三个 artifact 的 SHA-256 已与持久状态核对。详情见 [可恢复状态](autodev/AA01.state.json)。后续交接文档提交不覆盖既有标签。

## 使用与下一步

启动方法及接口契约见 [AA01 规格](milestones/AA01_AGENT_ACCESS.md)。默认专用端口 8877，仅 loopback；验收 demo 使用临时服务并在结束后关闭，不代表常驻服务已启用。

凭据文件仅存于忽略目录，不进入 Git 或事件。当前是单进程、本机可信账户下的测试环境：未实现生产 Human 登录、凭据轮换/过期、分布式执行或公网服务。旧工作台不能用于打开 Agent lab 数据库。

下一工程为 M03/M1 学习层规格；Agent Human 审批网页及生产身份机制可另行拆分。现有域名/生产项目保持原状；云端写回暂停。

## 发布与回滚 Gate

本地测试无需新增 Human 决策。正式 push、部署、恢复自动写回须先提供目标提交、变更/测试及回滚包，并取得用户确认。本包尚未发布。

本地 lab 可停止其进程，保留专用数据库与凭据后另建新 lab；不修改旧工作台数据库。需要退回代码时从此前本地提交 43214de 建立独立 checkout，或通过新 revert 提交修正；不覆盖标签、不 reset 历史、不 force-push。生产部署未发生，因此无线上回滚操作。
