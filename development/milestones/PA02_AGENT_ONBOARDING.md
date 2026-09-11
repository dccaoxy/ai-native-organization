# PA02 — Agent 完整接入说明与可调整默认权限

用户授权改进 Agent 接入：复制一段文本就能让具备 HTTP 能力且网络可达的 Agent 理解并完成接入；默认基础权限、中文解释、后续网页调整。依赖 PA01 本地 PASS，旧测试环境和部署边界保持。

## S01 规格

输入 organization/specs/tests、PA01 Portal、冻结基线。输出完整文本、接入回执、中文默认权限表单、权限调整命令与测试；完整回归/独立 Review/Audit 后本地 commit/tag/artifact。

接入文本包含真实 URL、一次性凭据和注册编号、网络可达性限制、HTTP 头、身份核对、POST /v1/connect、pending/approved/revoked 分支、任务读取/执行/正式 Return、幂等重试和禁止越权规则。平台已创建待授权记录，Agent 不重复注册。纯文字 Agent 或云端访问本机 localhost 不能完成，文本须如实说明阻碍。

POST /v1/connect 在验证凭据和注册编号后记录首次连接回执；重复幂等、跨服务实例重启保留，不自动授予权限或改变运行状态。该回执存于本地账号数据库，属于传输接入记录，不伪称实际模型持续在线，不伪造正式组织事件。

默认预选 claim/ack/progress/submit/fail/blocked/release/resume/escalate。网页以中文显示操作意义，高级选项折叠；Human 仍明确选择任务并确认授权。request_boundary/challenge_goal/use_knowledge/report_knowledge_issue 默认不选；审查、验收、选择、批准扩权永不作为 Agent 可授予权限。

新增 update_agent_access 仅当前绑定的所属 Human 可调用。同步更新 AgentRegistration 与 RepresentativeAgent.permissions，单个 AgentAccessUpdated 事件记入正式 Trail，立即生效。可收回全部任务/命令，旧 Execution owner/boundary/status 不被重绑或自动改变；已收回操作不能继续。被替换/撤销/外来 Human/Agent 自授/未知任务/Human-only 命令均拒绝。没有自动扩权。

## 验收条件

实际 Edge 浏览器生成说明；独立 HTTP 客户端从文本 JSON 配置核验身份、重复连接幂等、未授权领取被拒绝；页面接入状态可见。默认复选项正确、后续修改保留；原双账号目标任务→授权→Return→Review/Acceptance/Selection 全链通过。新测试验证权限收回即时生效、不能自授、外来 Human 被拒绝、owner/boundary 保留、回执重启恢复。

确定性客户端不是 LLM 理解能力实验；测试账号/任务明确 synthetic，0 位真实参与者。所有源摘要、事件与截图不得含接入 token。

repair budget=1；工程失败持久化修复，Frozen/Human Authority/Risk 变化进入 HUMAN_DECISION_REQUIRED。本地开发不需重复确认；push、云端常驻安装、域名改动仍须另行确认。

恢复看 PA02.state.json 和运行回执；回滚代码以独立 checkout/revert，新增 portal_connections 表可保留，旧事件历史不能删除。旧版代码可能不识别 AgentAccessUpdated，应保留 PA02 版本读取已产生该事件的数据或使用变更前的一致性备份，不对活跃账号库直接降级。
