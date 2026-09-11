# M03 — 可追溯学习层 / 最小工程闭环

Phase 5 / M1；只验收下列工程子集，不代表完整 Learning Organization 或学习效果验证。

## 冻结语义映射

依据 Final Design Baseline 的 04 Specification、04 Principles、06 Specification、06 Principles 及 Evidence Core Principles：Experience ≠ Knowledge；Evidence 是来源相对于 Claim 的关系；反证优先、孤证不立；知识有 Scope/Boundary/Transfer Conditions；Capability 是证据，不是权限；第一份成功立即捕获候选，跨 HAU 复现及依赖有效性另行验证。冻结正文未修改。

## 对象与命令

机器契约 `specs/M03.learning.json` 是新增实现字段，不修改 M01 冻结契约。

- LearningClaim：来源 Return、核心主张、范围、机制、迁移条件、Task 白名单、作者和单独指定的验证 Human。候选不是 Knowledge。
- LearningEvidence：claim/return 关系 supports/contradicts/discriminates/inconclusive；显式上游来源、理由，以及 Return/Execution/Task/Review/Acceptance 在关联时的快照。相同 Return 不能重复计数。
- LearningVerification：包括全部当前证据、反证尝试、替代解释、局限及独立性说明。验证 Human 不得是作者。
- KnowledgeRevision：确认后的有界知识；版本、前一版本、组件 delta、证据引用、validated/challenged/superseded。改进新建候选并独立验证，历史不覆盖。
- CapabilityRoute：每次成功 submit 在同一正式事件中自动捕获候选，不宣称已复现。补齐 Knowledge/Data/Tools/Agent Configuration/Runtime/Practice/Oversight 后仍是候选。
- KnowledgeUse：live Execution 中显式 adopted/rejected，固定引用知识版本和可选能力包；不规定工作步骤，也不提升权限。
- LearningOutcome / CapabilityReproduction：同一次使用对应的正式 Return，另一 HAU 成功且单独 Review/Acceptance 后可记录 reproduced；不以单次成败推断因果。依赖版本被替代/质疑或复用失败会失效/要求重验。

Human 命令：propose_claim、capture_evidence、verify_claim、assemble_route、record_learning_outcome、record_reproduction；use_knowledge 支持显式委托给 Representative Agent。来源关联要求该 Return 的 Human owner；验证要求指定 Human；能力包由其捕获 owner 整理和核对。沿用现有 Task Review/Acceptance Authority。

## 本地操作化边界

为防止本机合成测试轻易泛化，确认门槛采用至少两个来源 HAU、无共同声明上游、支持 Return 已 Review/Acceptance、没有未解决反证。此门槛是保守的本地工程规则，不是科学独立性判定或冻结证据阈值；上游真实性和验证文字质量仍须 Human 判断。不能以填写两份表格宣称真实规律成立。单一事实的特殊确认、因果证据强度评分均未实现。

明确 Task 白名单和所需 Boundary 是当前人工 Scope 判定的操作化；自然语言 scope/transfer 不由程序证明。GET /v1/knowledge 仅返回已授权 Task 的有效知识摘要，不返回来源快照/他人 Return；POST use_knowledge 再核对委托、所属 Execution、live 状态、Task 和 runtime boundary。候选能力包可以被明确采用做复现尝试，但不会赋予领取许可或自动启动执行。

强反证与非成功复用先触发 challenged，代表需要重验，不代表知识导致失败。关键 Knowledge 依赖自动失效；Tool/Data/Runtime 的外部变更监听尚未实现，不宣称完整 CAP-11。当前 bound package 不可改绑，重验须新版本/新候选路线；已有记录保留。

## Stages

| Stage | Dependencies | Inputs / Outputs | Exit criteria / tests |
|---|---|---|---|
| S01 Evidence and candidate capture | M01/AA02 本地通过 | 冻结基线、Return → 来源关系/快照/首成功候选 | 来源不可重复、owner 约束、幂等、自动候选；test_learning |
| S02 Bounded knowledge and verification | S01 | 候选/证据 → 独立验证/版本/组件差异 | 单一及共同上游拒绝、反证不能遗漏、自验拒绝、历史可追溯；test_learning |
| S03 Scoped reuse and capability | S02 | 版本/包/新 Execution → use/outcome/reproduction | Task/Boundary/委托、跨 HAU、失败/版本失效；test_learning_gateway + test_learning |
| S04 Browser integration and acceptance | S03 | 网页/独立 Agent/持久证据 → 验收包 | 完整套件、源代码绑定的真实浏览器证据、replay、artifact/tag |

每阶段有限 repair budget=1；失败保留日志后 BLOCKED_ENGINEERING。通过才 commit/tag/artifact 并推进，状态与恢复入口为 `development/autodev/M03.json` / `M03.state.json`。四阶段用于验收同一最小实现的递进覆盖，不冒充四次独立设计审查。Review/Audit 为分离进程确定性反例校验，不等同独立 LLM/真人认知认证。

## 网页及再现

现有专用 Agent lab 的“学习与复用”页提供七步表单及对象下钻。控制密钥与合成 Human 规则沿用 AA02，不能开放公网作为真实登录系统。先准备有来源 Return 的实验室；来源 owner 提出候选/关联证据，指定 Human 验证，另一 HAU 执行复用再提交正式反馈。

```console
python -m unittest tests.test_learning tests.test_learning_gateway -v
python -m organization.learning_demo
python -m autodev.runtime run --plan development/autodev/M03.json
```

浏览器命令需已有 Node/Playwright/browser；用 --node、--modules 和 LAB_BROWSER_CHANNEL=msedge 指定本机安装。demo 创建独立临时数据库和合成身份，运行实际网页和独立 Agent 进程，结束关闭；输出保留至 development/autodev/learning-demo，报告绑定 organization/specs 源摘要。没有调用模型或真实公司系统。

## 未包含及 Human Gate

未实现完整 Hypothesis Cloud、Pattern 发现、因果检验、自动语义提取、语义搜索/Context Assembly、Pulse 全局传播和组件级依赖路由、非 Knowledge 外部依赖监听、完整三张 Capability Map、自动 Revalidation Task 或真实学习实验。网页当前提供明确字段与下钻，后续可减轻输入负担；不采集 Free Work Space 私有过程。

正式推送、部署、恢复云端写回；真实 Human Pilot/公司权限与数据；Policy Force/Authority 扩大、冻结 L1/L2 改动均 HUMAN DECISION REQUIRED。上述行为不在 runner 命令中。本地工程无需新增批准。

回滚：停止专用本地服务，保留数据库；用已有标签独立 checkout 或新 revert 提交修复。旧版本代码不应直接打开带 M03 对象的新数据库；使用升级前备份或新建实验室。不能 reset 历史、覆盖标签或 force-push。
