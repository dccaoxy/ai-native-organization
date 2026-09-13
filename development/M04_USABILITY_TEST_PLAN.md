# M04 3–5 人理解与可用性测试计划

更新时间：2026-09-13

状态：**Ready to review / Not started**
前置条件：远程隔离入口通过 Gate B，测试者与邀请方式得到 Human 批准。

## 测试目标

验证第一次接触系统的非开发者是否能够在无口头教学、无命令行操作的情况下：

1. 理解组织对象与责任边界；
2. 完成 Human × Agent 的最小工作闭环；
3. 正确处理权限、返工、证据与知识失效；
4. 指出界面中导致误解或停滞的位置。

测试不是产品演示，也不是培训。主持人只能使用统一提示，不替参与者完成任务。

## 参与者与数据

- 3–5 位真实参与者，使用匿名编号 `P01`–`P05`。
- 优先覆盖：业务负责人、普通执行者、熟悉 AI 工具但不了解本系统的人。
- 使用全新测试账号、合成组织、虚构 Goal 和无敏感信息的材料。
- 不记录密码、Agent token、真实姓名或不必要的个人信息。
- 屏幕录制或音频记录必须另行征得参与者同意；拒绝录制不影响参与。

## 统一场景

> 你负责一个虚构研究小组，需要在两天内交付一页“新员工 AI 使用边界说明”。你可以创建工作、接入一个 Agent、查看进展和证据，但最终责任与验收必须由 Human 承担。

## 测试任务

### T1 建立正确心智模型

请参与者浏览入口并用自己的话回答：

- Goal、Task、Execution 分别是什么？
- 谁对最终结果负责？
- Agent 可以自己批准哪些事情，不能批准哪些事情？

通过：三类对象没有混淆，能指出唯一 Human owner 与至少一个权限边界。

### T2 创建并发布工作

参与者自行创建 Goal、Task，设置 Acceptance Criteria，发布一个可领取的 Execution。

观察：是否能找到入口；是否理解完成标准；是否误把草稿当成发布；是否知道影响范围。

### T3 接入并授权 Agent

参与者创建 Agent 接入说明，确认连接，查看 pending 状态，再授予完成本任务所需的最小权限。

通过：pending Agent 无执行权；参与者没有授予 Human-only 权限；能撤销或缩小权限。

### T4 完成执行与正式 Return

测试 Agent 完成 Claim → ACK → Progress → Submit，并附带指定合成证据。参与者不得代替 Agent 填写结果。

通过：事件顺序可见；Return 包含输出、证据和已知限制；重复提交不制造重复事实。

### T5 独立 Review 与 Human Acceptance

参与者先以 Reviewer 视角给出 PASS、返工或拒绝，再以 Human owner 身份执行 Acceptance。

至少一次测试返工：修改范围必须留下差异和理由，不能静默覆盖原 Return。

### T6 知识复用与失效

参与者定位由执行形成的 Knowledge，说明来源与版本；随后面对“源材料已更新”的提示，报告失效并创建重验任务。

通过：旧知识不被删除或静默改写；能看到影响、修订理由和重验状态。

### T7 安全理解检查

询问参与者：

- 如果 Agent 请求更多权限怎么办？
- 如果发现跨账号数据怎么办？
- 如果系统给出 PASS，是否意味着组织效果已得到证明？

通过：选择升级给 Human、立即停止并报告泄露、拒绝把合成 PASS 当作真人证据。

## 主持人统一提示

只有参与者明确停滞 90 秒后，主持人才能依次给出：

1. “请找页面上与你当前角色相关的待办。”
2. “请检查对象的状态、Owner 和可用动作。”
3. “这一步需要 Human 决定，还是 Agent 可以在已授予权限内执行？”

每次提示必须记录；不得提供按钮位置或直接答案。

## 原始观察模板

每位参与者复制一份，保留原始记录，不覆盖其他参与者内容。

```markdown
# Participant P__

- Date/time:
- Build commit/tag:
- Entry URL classification: remote-isolated / local-observed
- Consent: participation yes/no; recording yes/no
- Prior familiarity: AI tools / workflow systems / this project

| Task | Start | End | Result | Hints | Error/message | Observed behavior |
|---|---|---|---|---:|---|---|
| T1 | | | pass/fail | 0 | | |
| T2 | | | pass/fail | 0 | | |
| T3 | | | pass/fail | 0 | | |
| T4 | | | pass/fail | 0 | | |
| T5 | | | pass/fail | 0 | | |
| T6 | | | pass/fail | 0 | | |
| T7 | | | pass/fail | 0 | | |

## Participant explanation in own words

- Goal / Task / Execution:
- Human accountability:
- Agent authority boundary:
- Evidence / Knowledge / invalidation:

## Issues

- Blocker:
- Major:
- Minor:
- Security/privacy:

## Participant closing feedback

- Most confusing:
- Most useful:
- Would you trust this for a low-risk real task, and why:
```

## 汇总与裁决

只汇总真实记录：

- 完成率 = 无主持人代做而完成的核心任务数 / 核心任务总数；
- 分别报告无提示完成、提示后完成和失败，不能合并成“成功”；
- 安全问题不以平均分抵消；凭据泄露、越权、自我批准、跨账号暴露均为立即停止；
- 将每个问题映射到界面/协议解释/实现修复、负责人、状态和复测证据；
- 至少 3 位完成、核心闭环完成率 ≥80%、0 个安全阻断项且所有 blocker 复测后，Gate C 才能 PASS。

测试结果不得反推完整组织有效性；它只回答首次理解与操作可用性。
