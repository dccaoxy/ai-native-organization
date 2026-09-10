# AA02 联合工作台验收与试用

2026-09-11，本地 PASS；未推送、未部署。

- 完整回归 136 项通过；独立进程 Review/Audit 通过，冻结基线无变更。
- 实际 Edge 浏览器批准 Agent，独立 Python 客户端执行；浏览器完成 H1 Review → H0 Acceptance → H2 Selection，Task 关闭，留下 18 条合成事件。
- 错误 Human 的 Review 按钮禁用；接口测试验证 Agent 凭据、跨源和伪 Host 被拒绝；退出清除页面数据。桌面/390px 窄屏截图已检查，无水平溢出。
- 本轮未调用模型，使用明确标注的固定测试输出；0 位真实 Human，不代表业务结果质量或真人实验。页面使用合成身份控制密钥，不是生产登录。
- Checkpoint：`63d92f3b93b80eda75bcc5967abbbcce6fd654dc`；tag：`autodev/AA02/S01/v1`。
- [代码包](autodev/runs/AA02/S01/1/artifact.zip) SHA-256：`920d3b7399a7426491174753b778b691151034541e3a20c124d4e7b02b15c3bd`，已与状态和 tag 核验。
- [测试报告](autodev/human-web-demo/report.json) · [原始合成证据](autodev/human-web-demo/evidence.json) · [桌面截图](autodev/human-web-demo/desktop.png) · [窄屏截图](autodev/human-web-demo/mobile.png)。

## 已准备的本地试用环境

地址：http://127.0.0.1:8878 。专用数据和密钥在忽略目录 `.autodev/human-workspace.sqlite3`、`.autodev/human-workspace.key`；与旧工作台数据分开。当前有一个 pending Agent，尚未授权。进程关闭后可用下列命令恢复：

```console
python -m organization.agent_gateway --port 8878 --db .autodev/human-workspace.sqlite3 --operator-key-file .autodev/human-workspace.key
```

从本地密钥文件复制控制密钥到网页（不要发给 Agent）。选择 H0，HAU 填 U0，Task 填 T，勾选 claim、ack、progress、submit，点击批准。然后可让开发助手运行下面的独立 Agent，或自行在仓库根目录执行：

```console
python -m organization.agent_client run --url http://127.0.0.1:8878 --identity .autodev/human-workspace-agent.json --task T --run-id human-trial-1
```

刷新页面后，H1 审查、H0 验收、H2 选择；每一步依据所见结果填写理由，不能把合成验收当成真实业务评价。本地网页没有托管后台 Agent，批准后仍需运行客户端。

## 下一步与边界

先由用户进行上述联合试用，再根据体验修正；随后进入 M03 学习层规格。完整契约及回滚见 [AA02 规格](milestones/AA02_HUMAN_AGENT_WORKSPACE.md)。退出专用进程可停止服务；数据库保留以便恢复。正式推送、部署和恢复自动写回仍需另行确认，现有域名项目未修改。
