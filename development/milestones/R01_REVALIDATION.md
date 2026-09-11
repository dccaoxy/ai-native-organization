# R01 — 知识失效、修订与新任务重验

2026-09-11 用户确认；M03 后续工程，Phase 5 / M1。本地合成测试，不推送/部署。

## 冻结语义与范围

沿用 Final Design Baseline 04/06：反证优先、版本与理由可追溯；Capability 依赖有效性；Revalidation 使用 Active Goal 下新的 Execution，权限不来自知识或能力。状态只表示工程证据，不宣称真实学习效果。

R01 增量契约：specs/R01.revalidation.json。旧对象及标签保留，不覆盖 M03 历史证据。

## 记录和权限

- KnowledgeImpact：每个失效版本的触发原因、受影响能力包、当时正采用该版本的 active Execution；保留历史快照，UI 同时显示对象当前状态。不会自动暂停执行。执行者拒绝采用后的失败不影响未使用知识。
- LearningChallenge：Agent 通过显式委托 report_knowledge_issue 上报自己的 adopted use 和正式 Return；必须在其 HAU/Task 授权内。报告触发重验信号，不证明知识导致失败。新反证和后到问题会质疑依赖该版本的有效后继版本。
- RevisionRationale：修订理由和已回应原因引用；验证前检查是否覆盖最新原因。替代状态标记不是新反证。propose_claim 绕过修订理由时不能验证新版。
- RevalidationPlan：知识作者在其同时拥有 Goal authority 的本地场景下，明确创建并发布一个全新 Task，受现有 Active Goal、Boundary、Review/Acceptance 权限验证约束。创建原子执行；不会复用旧任务冒充新重验。
- RouteRevision：显式新建替代能力包，依赖已验证的后继知识并保留原路线来源，完整记录组件和变化理由；初始仍是 candidate。旧包保持 stale。
- complete_revalidation：只接受计划中新 Task 的跨 HAU 成功复现及正式 Review/Acceptance/Outcome；新知识当前有效、版本关系匹配、最新问题已回应。完成后 impact resolved，旧知识不恢复，旧包不恢复。

存在 pending plan 时，新知识只允许计划任务中的试用（仍须知识 Task 白名单及 Agent 权限）；通过后才恢复到作者声明的其余 Task 范围。完成重验不会扩展白名单或 Runtime Boundary。

Agent GET /v1/knowledge-alerts 仅显示自己已授权 Execution 的 adopted use 和失效版本状态，不泄露其他 HAU 的影响快照。GET /v1/knowledge 继续过滤当前有效、可用 Task 范围。没有自动全局广播或后台监控承诺。

## 网页流程

“学习与复用”新增影响卡与步骤 8–11：建立重验任务 → 带理由修订知识 → 沿用步骤 2/3 关联证据和独立验证 → 创建替代能力包 → 明确授权 Agent 执行新任务 → 审查/验收/结果关联/跨 HAU 复现 → 确认重验通过。

Human 操作者使用独立本地控制密钥和明确的合成身份。UI 不提供真实用户身份认证。本轮自动浏览器由测试代码操作这些 Human 角色，真实参与者为 0。

## Stages 与验收

| Stage | Dependency | Inputs / outputs | Exit criteria |
|---|---|---|---|
| S01 Impact and scoped signals | M03 minimum PASS | M03 / R01 schema → impacts, Agent issues, scoped alerts | Active adopters visible without silent pause; rejected-use failure does not invalidate; owning Agent only |
| S02 Explicit revision and revalidation | S01 | Impact / new Task / revisions → new candidate package / completion | Reasons required; no premature completion; correct task; boundary and authority; late issues invalidate successors |
| S03 Browser and independent Agent acceptance | S02 | UI / two Agent processes / source-bound evidence → local acceptance | Failure report → revised version → newly authorized task → reviewed reproduction; full regression and replay |

tests.test_revalidation、test_learning、test_learning_gateway 是确定性独立进程 Review/Audit；冻结摘要另查。不是独立 LLM 语义认证。每阶段 repair budget=1，工程失败持久化后停止；只有 PASS 才形成 commit/tag/artifact。状态：development/autodev/R01.state.json。

## 复现

```console
python -m unittest tests.test_revalidation -v
python -m organization.revalidation_demo
python -m autodev.runtime run --plan development/autodev/R01.json
```

浏览器需本机 Node/Playwright；--node / --modules 可指定安装，LAB_BROWSER_CHANNEL=msedge 可用现有 Edge。demo 使用临时隔离数据库、实际网页和两个独立 Agent 进程；固定合成任务，无模型调用，结束关闭服务。development/autodev/revalidation-demo 报告绑定 organization/specs 当前源码摘要，代码改动后需重新产生浏览器证据。

## 限制与后续

人工文本和上游独立性声明不等于真实认知验证；只实现显式知识版本依赖，非完整 Tool/Data/Runtime 监听。影响表是单版本的历史集合，不是全组织实时通知系统。知识作者与 Goal authority 分属不同 Human 的跨角色重验发起流程尚待扩展。多个计划可并存，一条计划的通过不应被当成其他计划也通过；剩余 pending plan 仍限制相关试用范围。

晚到新问题会重新打开 impact 并使有效后继版本待重验；原 passed plan 是历史结论，其日期后的问题需要新计划。旧快照不得当成当前有效性。

本地后续无需新账户/资源授权。正式 push、部署、恢复自动写回；真实 Human/公司数据/权限；Frozen L1/L2 修改仍 HUMAN DECISION REQUIRED。没有相关自动命令。

回滚：停止隔离服务，保留数据库；旧版本仅配合升级前备份或新实验室，不能直接打开新对象数据库。使用独立 checkout 或新 revert 提交，不 reset/force-push/覆盖标签。
