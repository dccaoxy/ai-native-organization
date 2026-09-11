# UX02 — 连续验收与中断恢复

用户已授权连续验收和修复。本轮仅本地开发，依赖 UX01 本地 PASS，不改旧实验库、统一试用数据库或既有域名。不推送、部署或启用云端自动写回。

## S01 规格

输入：organization/specs/tests、Final Design Baseline 完整性锁、UX01 入口及工作台、source-bound 实际浏览器报告。输出：连续验收 runner、Agent 状态恢复入口、可读状态标签、试用指南及本地 commit/tag/artifact。

临时数据库只预置明确的合成 Human/HAU 和两个任务，起始 Execution/Knowledge 均为零。四个 Agent 通过独立 Python 客户端进程 HTTP 注册，由实际 Edge 浏览器选择合成 Human 批准指定任务与操作。所有结果和知识版本均在同一数据库连续产生，不导入已有知识/Return。

退出条件：注册→执行→Review→Acceptance→Selection→知识形成→新 Agent 采用→离线/Execution interruption→所属 Human 确认 Agent 恢复及恢复 Execution→失败/问题报告→修订/独立验证→新任务和替代能力包→新 Agent 执行→分离审查验收→复现/重验完成。非所属 Human 的恢复按钮须禁用。

两次停止并重建 HTTP 服务实例，复用同一路径数据库、端口和密钥；浏览器重载后事件逐条一致。第一次重启后重复 claim/ack 幂等键不得产生新事件。最终 event replay 等于投影，旧知识 superseded、旧路线 stale、新路线 reproduced；测试控制密钥和 Agent token 不进入证据。

这是同一测试进程内重建服务实例，不宣称机器崩溃、断电恢复或云端持续运行。Agent 离线信号由客户端显式发送，不宣称实现了新的自动心跳失联检测。

## UI 修复

所属 Human 可点击“确认 Agent 已恢复”，记录 online 后再恢复 Execution。这个动作记录已确认的运行状态，不会启动真实客户端进程。待办导航显示离线 Agent 与尚未完成的 Execution。知识、能力包、采用等状态以中文显示；候选解释标为历史判断，当前有效性应看知识版本，不抹掉旧证据。

## 验证与治理

`python -m organization.continuous_demo` 创建临时隔离数据并运行实际浏览器；`--node`/`--modules` 可指定 Node/Playwright，`LAB_BROWSER_CHANNEL=msedge` 使用 Edge。

`python -m organization.workspace_demo` 验证原有字段带入、按 Human 隔离草稿、刷新与退出行为。证据在 development/autodev/continuous-demo 与 workspace-demo，含源文件摘要。

`python -m autodev.runtime run --plan development/autodev/UX02.json` 运行完整套件、独立进程 Review、冻结完整性和原则 Audit。repair budget=1，超出后持久化 BLOCKED_ENGINEERING；生产权限、真人试点、冻结 L1/L2 改动另设 Human Gate。

确定性脚本执行 Agent 协议，浏览器自动选择合成 Human；0 位真实参与者，未调用模型。Review/Audit 是独立确定性进程，不是独立 LLM 或真人语义认证。

回滚用独立 checkout 或新 revert；标签/历史不覆盖，不 force-push。此轮未迁移数据库 schema，所有连续测试数据在临时目录，旧实验室和统一试用数据保持原样。恢复本阶段依据 UX02.state.json、run receipts 和源码，不依赖聊天。

## 本地完成记录

S01 PASS：18c0761 / autodev/UX02/S01/v1；163 项完整回归、80 条连续合成事件和两次服务实例重启验证通过。机器状态见 development/autodev/UX02.state.json；范围、首次配置失败和 attempt 2 回执见 development/UX02_ACCEPTANCE.md。未推送或部署。
