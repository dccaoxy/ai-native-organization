# Knowledge / Organizational Memory 架构

- 状态：核心架构已形成；Context Assembly 与 Consolidation v0.1 已冻结；Knowledge → Behavior 治理尚未冻结，尚未实现
- 关联：[[ontology-and-graph]] · [[Free Work Space Protocol v0.1]] · [[Organizational Learning & Knowledge Formation]] · [[Organization Runtime & Protocol OTA]]

## 核心原则

> Distributed Intelligence + Shared Memory

> Local thinking, global learning.

员工可以使用不同平台、不同 Personal Agent 和私人工作空间；组织不统一个人思考过程，但正式贡献必须进入统一协议与 Organizational Memory。

Organizational Memory 是贯穿 `Work → Review → Acceptance → Result` 的持续学习层，而不是 Result 之后的单一终点。Work、Failure、Review 与 Human Acceptance 都可产生候选信号，原始事件与经验可先进入 Experience Memory；只有提升为正式 Knowledge、Ontology 或 Protocol 时，才需要相应证据与治理闸门。

当前认知形成主干已扩展为：

```text
Raw Events → Organizational Attention Mechanism → Observation → Pattern
→ Hypothesis Cloud ⇄ Evidence ⇄ Verification
→ Generalization / Scope → Knowledge
→ Behavior Change → New Events
```

完整定义与模块状态见 [[Organizational Learning & Knowledge Formation]]、[[Evidence Core Principles]] 与 [[Verification Protocol v0.1]]。

## Knowledge Commit 流程

早期 Knowledge Commit 是候选知识提交入口，不是所有记忆进入系统的唯一通道，也不能仅靠 Human 轻量确认就变成已验证知识。

```text
Work / Review / Acceptance / Result → Experience Memory
→ Attention → Observation → Pattern → Hypothesis Cloud ⇄ Evidence ⇄ Verification
→ Minimum Validated Scope → Knowledge Memory
```

Personal Agent / Human 仍可提交 Candidate Knowledge；Gateway 保留 Schema、Ontology、权限、去重、冲突、Provenance 与审计检查。认知晋升遵循 [[Organizational Learning & Knowledge Formation]]，不把所有原始经验都阻塞在人工审批前。

## 责任分工

- Human：对真实性与价值作轻量确认。
- Personal Agent：发现、提炼、初步结构化候选知识。
- 中央系统：Schema、Ontology、权限、证据、去重、冲突与审计治理。

不能依赖员工“记得上传”，也不能依赖 Agent 自觉总结；需要触发器、接口和审计形成稳定流程。

## Organizational Memory 的对象

长期不应只是文档仓库，而应连接：

Goal、Task、Person、Agent、Capability、Knowledge、Artifact、Evidence、Decision、Experiment、Resource、Risk。

原始媒体或 Artifact、可检索文本、整理后的 Knowledge 应保持层次区分，不把加工结果冒充原始证据。

## 中央标准化与个人自由

| 中央标准化 | 允许自由 |
|---|---|
| Ontology、版本与映射 | 员工如何思考 |
| Task / Knowledge / Evidence Schema | 使用哪个 Personal Agent |
| Identity、Permission、Audit | Agent 如何推理 |
| Knowledge Commit Protocol | Workflow、Prompt、临时笔记 |

正式接口统一在协议和中间层，而不是绑定某个 Agent 产品。

接入 Organization Gateway 的 Agent 还必须加载当前 Organization Runtime / Protocol Package、承担运行时义务并接受协议更新。详见 [[Organization Runtime & Protocol OTA]]。

## 待验证

- 不同 Agent 平台的最小统一接口与可靠触发方式。
- Knowledge Diffusion Latency 的测量。
- 人工确认负担与知识质量之间的平衡。
- 错误知识污染、冲突、取代和回滚机制。
- 隐私、权限和公司数据边界。
- Knowledge Promotion、Challenge、Deprecated、Superseded 状态机。
- Scope 过期、重新验证和迁移的操作化；核心边界已在 [[Generalization & Scope]] 收敛。

来源：[[05项目/AI Native组织/80 原始讨论/探讨AI原生组织-raw-conversation|原始对话]]。

## 三层 Organizational Memory

| 层 | 保存内容 | 何时激活 |
|---|---|---|
| Experience Memory | Raw Events、原始过程、Artifact、结果、失败和经验 | 审计、重验、追溯事实时下钻 |
| Epistemic Memory | Observation、Pattern、Hypothesis Cloud、Evidence 关系、Verification、解释和反证 | 理解为什么、质疑、竞争解释和高风险判断时下钻 |
| Knowledge Memory | 有证据、认知状态和适用边界的可复用 Claim | 通常优先激活，支持当前判断与行动 |

**Store broadly, activate sparsely.** 三层都保存，也都可以按需激活；默认从 Knowledge 层开始，不是下两层永不使用。广泛存储仍受权限与隐私边界约束。

Knowledge 之间可以形成支持、约束、解释、冲突、取代等联系；关联网络是认知关系，不表示每次激活整张图，也不等同于大模型参数空间。

## 使用与反馈

[[Cognitive Routing 与 Knowledge Activation]] 负责想起什么；[[Context Assembly v0.1]] 负责轻量组装；[[Knowledge Injection 与同步边界]] 负责在接触点传递。

**Knowledge Activation ≠ Context Injection**。[[Knowledge Consolidation & Salience v0.1]] 分开可信度与显著性；[[Knowledge Usage Feedback]] 把采用/拒绝和 Outcome 变成新的可检查信号。

主线 [[Knowledge to Behavior - Behavioral Authority]] 继续研究知识的行为影响权。

## 2026-09-04 当前有效架构

以下内容已确认；整体状态为“核心架构已形成 / Knowledge→Behavior 治理未冻结”。本次不为整体 Memory 新增未经裁决的版本号。

- 三层记忆。
- Store broadly activate sparsely。
- Cognitive Routing。
- Knowledge Activation ≠ Context Injection。
- Context Assembly v0.1。
- Knowledge Consolidation & Salience v0.1。
- Knowledge Intervention v0.1。
- Knowledge Usage Feedback。
- Inject cognition not workflow：Claim Push + Checkpoint Delta Push + On-demand Pull。

来源完整性更新：此前基线同步因引用聊天读取超时，仅同步了机制名称。本轮已取得相关新增原始讨论并补齐三层记忆及子机制条文；原始历史乱码缺口仍单独标记。

Knowledge→Behavior 的当前有效设计与下一问题见 [[Knowledge to Behavior - Behavioral Authority]]；接入治理见 [[Agent Governance & Runtime]]。
