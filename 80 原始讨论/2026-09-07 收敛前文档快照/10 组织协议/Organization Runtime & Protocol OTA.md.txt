# Organization Runtime & Protocol OTA

> 状态：**核心架构已确认，协议细节初步设计**  
> 确认日期：2026-09-03；阶段更新：2026-09-04
> 所属一级模块：[[Agent Governance & Runtime]]  
> 当前不冻结版本；等待真实接入场景与 Schema 验证。

## 核心判断

Agent 接入 Organization Gateway，不只是获得 API 或数据访问权，而是获得并遵守当前有效的 **Organization Runtime / Protocol Package**。

> **Connection = Access + Rules + Responsibilities + Updateability**

只有能够加载、执行、回报协议版本并接受更新的 Agent，才可作为正式 Organizational Agent；否则仍可作为个人工具，但中央系统只能管理持有 Task Lease 的 Human。

## Runtime / Protocol Package

### 组织规则

- Goal、Task、Free Work Space、Review、Acceptance；
- Learning Signal、Knowledge Commit、Ontology；
- Identity、Permission、Risk Boundary 与待设计的 Audit。

### 运行时义务

`Task Lease → ACK → Heartbeat / Progress Signal → Checkpoint → Submit → Task Close Reflection`

Agent 必须知道何时报告进展、何时检查协议版本、何时升级风险或边界问题。运行机制与 [[Task Lease & Progress Protocol v0.1]]、[[Time & Recovery Protocol v0.1]] 联动。

### Protocol OTA

Gateway 发布新的 Protocol Package 后，接入 Agent 应：

1. 查询当前版本；
2. 下载并校验适用更新；
3. 应用新规则；
4. 回报已应用版本；
5. 当更新改变 Human 的行为、权限或责任时，向所属 Human 提醒差异。

## Agent 接入分层

- **Managed Agent**：组织可以直接控制 Runtime、Lease、事件和协议版本。
- **Connected Agent**：通过 Gateway/Connector 接收任务与协议，并回传标准化状态。
- **Unmanaged Personal Agent**：组织无法直接观测其运行；由 Human 持有 Task Lease，并对提交、边界和状态负责。

## 组织自我进化闭环

```text
Work → Data / Evidence → Organizational Learning
→ Protocol Improvement → OTA
→ Human / Agent Behavior Change → New Work
```

## 待设计

- Package Schema、版本依赖、签名与完整性校验；
- 强制更新、渐进发布、回滚与兼容窗口；
- 不同 Agent 平台的最小统一接口；
- 协议不兼容、离线、拒绝升级时的 Fail-safe；
- Human 通知、确认与责任变化的最低标准；
- 与 [[Audit Layer 待设计]] 的留痕边界。

关联：[[Operating Loop v0.2]] · [[Task Protocol v0.1]] · [[organizational-memory]] · [[Organizational Learning & Knowledge Formation]]

## Runtime = Protocol + State + Interface

- Protocol Package：Goal / Task / Boundary / Review / Acceptance / Learning Signal / Knowledge Query / Audit / Permission。
- Runtime State：当前 Task、Lease、Due Time、Checkpoint、Protocol Version。
- Runtime Interface / Actions：ACK、Heartbeat / Progress、Query Knowledge、Escalate、Submit、Check OTA。

Context Injection 负责知道规则；Runtime Tooling 负责执行规则；Organization Gateway 负责接收和观察动作。薄 Runtime Adapter 不负责思考。优先验证支持 API/MCP/插件/CLI 的可执行接入，但不把 Prompt 软约束等同于工具级强执行。

**不要统一 Intelligence Layer，统一 Organization Runtime Layer。** Human 与 Agent 都应受相应组织治理。

Task / Knowledge / Protocol 是不同通道：Task Contract、ACK、Progress、Submit；Claim Push、Checkpoint Delta Push、On-demand Pull；Protocol OTA、Rules、Version Sync。普通知识不自动晋升为强制规则。见 [[Knowledge Injection 与同步边界]]。

## 一级模块归属（2026-09-04）

本架构纳入 [[Agent Governance & Runtime]]，该一级模块骨架已确认、待详细设计。统一 Organization Runtime Layer；Runtime = Protocol + State + Interface；Human 和 Agent 都需要治理。已有 OTA 细节的待设计状态保持。
