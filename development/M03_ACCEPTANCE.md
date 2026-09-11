# M03 最小学习闭环本地验收

2026-09-11：S01–S04 全部本地 PASS，未推送、未部署。仅覆盖 [M03 规格](milestones/M03_LEARNING_ORGANIZATION.md) 声明的最小工程子集。

## 已交付与验证

- Evidence 关系及正式 Return/Task/Execution/Review/Acceptance 来源快照；第一份成功自动捕获能力候选。
- 候选解释 → 明确反证/替代解释/独立性说明 → 有界 Knowledge；新版本保留组件差异和历史，反证不被支持票数淹没。
- Agent 在显式授权 Task/Boundary 内查询摘要并采用/拒绝知识；能力包不提供额外权限。
- 新任务/另一 HAU 的正式结果关联使用记录，单独审查验收后记录复现。版本替代或复用失败触发 challenged/stale，保留原始历史。
- 中文网页覆盖七步操作及对象来源下钻。修复选择框无障碍名称；桌面和窄屏浏览器检查通过。
- 完整套件 **152 项通过**，其中本轮学习相关测试 16 项。已有 HTTP 测试会输出 ResourceWarning，无失败。
- 实际 Edge 浏览器＋独立 Agent 进程跑通跨 Task 复用，**38 条合成事件**，replay 与状态一致；模型调用 0、真实 Human 参与者 0。源文件摘要与浏览器证据一致。
- Review/Audit 是独立进程确定性反例检查，非独立 LLM/真人语义认证；L1/L2 冻结摘要不变。

## 检查点

| Stage | Commit | Tag | Artifact |
|---|---|---|---|
| S01 | `359b6f7` | `autodev/M03/S01/v1` | [代码包](autodev/runs/M03/S01/1/artifact.zip) |
| S02 | `ffbb7e2` | `autodev/M03/S02/v1` | [代码包](autodev/runs/M03/S02/1/artifact.zip) |
| S03 | `18cad9b` | `autodev/M03/S03/v1` | [代码包](autodev/runs/M03/S03/1/artifact.zip) |
| S04 | `c2439d2` | `autodev/M03/S04/v1` | [代码包](autodev/runs/M03/S04/1/artifact.zip) |

四个标签指向已核验提交，代码包摘要与 [持久状态](autodev/M03.state.json) 一致。交接文档提交不覆盖这些历史标签。

[浏览器报告](autodev/learning-demo/report.json) · [事件与状态](autodev/learning-demo/evidence.json) · [学习页截图](autodev/learning-demo/learning-focus.png)。

## 试用与恢复

准备了独立本地示例：http://127.0.0.1:8879 。来源为实际执行的合成测试命令，包含已确认的测试知识 K1 和 route/R1 复现结果，与浏览器 demo 为不同测试实例。

专用数据 `.autodev/learning-workspace.sqlite3`，控制密钥 `.autodev/learning-workspace.key`，均不入 Git。用该密钥连接后打开“学习与复用”，展开对象查看来源/版本/采用/结果链。示例 H1/H2/H3 是合成控制身份。

本地进程不保证跨会话常驻。关闭后恢复：

```console
python -m organization.agent_gateway --port 8879 --db .autodev/learning-workspace.sqlite3 --operator-key-file .autodev/learning-workspace.key
```

自动验收与复现命令见 M03 规格；恢复 AutoDev 用 `python -m autodev.runtime run --plan development/autodev/M03.json`，已通过阶段不重复覆盖标签。

## 限制与下一步

两个来源 HAU、独立上游声明是本机保守门槛，不能自动证实科学独立性。范围/迁移条件需要 Human 判断；程序只强制 Task 白名单和操作 Boundary。能力复现是合成工程记录，不代表真实组织能力已形成。

尚未包含完整 Hypothesis Cloud、自动发现/语义抽取、自动知识激活与 Pulse、外部 Tool/Data/Runtime 依赖监听、自动重验调度或真实效果实验。下一步先试用来源链，并补充反证/版本变化的可操作复验体验，不自动进入 Human Pilot。

现有域名/生产服务未改动，云端写回仍暂停。正式推送/部署/真实业务权限和冻结原则变更需另行 Human 确认。本地后续工程可继续，无需新增账户或凭据。

回滚需使用升级前数据库备份或独立新实验室；不要让旧代码直接打开新增 M03 对象的数据库。通过新 revert 或独立 checkout 恢复代码，不覆盖 Git 历史。
