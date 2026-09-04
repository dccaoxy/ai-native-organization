# Task Bus 能否替代人肉 Router

## 核心问题

Pull、Push、能力匹配、ACK 与 Failover 能否可靠替代主管逐一派活？

## 待验证风险

- 重要但不受欢迎的 Task 无人领取；
- 推荐强化既有优势，减少学习机会；
- 多次 Re-route 掩盖 Task 质量问题；
- 动态调度导致责任稀释。
