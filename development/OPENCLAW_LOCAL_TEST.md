# OpenClaw 本机独立 Agent 测试

2026-09-11 最新结果：**独立审查任务的领取→ACK→Progress→正式Return已通过**。Human Review/Acceptance 未执行。

## 实际执行

- 本机 OpenClaw 2026.9.4 / Node 24.19.0，通过用户指定的 MiniMax-M2.7-highspeed 中国区接口运行。安装与配置位于仓库同级 `.openclaw-runtime`。
- 模型仅获 `org_review` 一个工具；固定平台broker保管Agent凭据，按白名单读取报告/哈希/路径/链接证据，只写 findings.json、review-report.md。无任意shell或文件访问。工具级限制不是操作系统沙箱。
- 用户明确要求由OpenClaw读取正式Return并做独立审查后启动。旧的凭据直读方案已放弃，凭据未放入模型上下文。
- 首次领取及报告生成成功，但后续协议调用失败。受限适配器处理可选null参数并增加安全诊断，主助手给出协议及审查质量反馈后，同一OpenClaw会话自行ACK、Progress、Submit。未由主助手代提交。
- Execution：E-openclaw-review-1；Return：R-openclaw-review-1；状态submitted。
- 4项执行事件均来自AG-e62c7bb13bb78341a7355861baa06cf4，唯一Human Owner保持不变；隔离测试组织simulation=true，真实模型/HTTP/文件审查已执行。

## 审查结论与限制

OpenClaw最终给出PASS，并披露抽样范围。原草稿与修订稿均保留。其结论属于独立Agent建议，尚未Human验收。不能将抽样一致性或原作者自述当作独立重算全部文件的证明。

缺失源链接后续处理未执行；目录命名仅有观察，没有具体整理方案。正式Review/Acceptance仍由Human授权；此轮没有验证退回原Agent、补充任务和再次审查的完整返工链，也没有实现平台自行启动Agent。

## 验证与恢复

- 工具本地测试PASS：分页、路径穿越/链接拒绝、固定输出、凭据安全错误、null参数兼容。
- 模型运行回执证明仅org_review工具，provider=minimax；无模型fallback。
- 独立读取平台状态：12事件、1个submitted Execution、1个Return、0 Review/Acceptance。
- 输入快照和原报告/证据文件哈希未变；无Vault改写、服务器改动或网站部署。
- 私有证据：`.autodev/openclaw-review-test/test-result.json`、verification.json、platform-readback.json、output/、platform-return.png；凭据/日志/私人报告不进Git。
- 隔离64150服务已在验收后停止，8876未改。恢复须先核验已有Execution/Return，避免重复提交。
- 按需本机CLI，非开机自启或云端常驻。未推送，未正式部署。
