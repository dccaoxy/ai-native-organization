# M02 — Synthetic Organization

Phase 4 / M0 robustness. Entirely synthetic; no Human Pilot or real company data.
The frozen Final Design Baseline and existing M01 semantics remain authoritative.

## Stages

| Stage | Engineering outcome | Required evidence |
|---|---|---|
| S01 Scale fixture | 10 HAU, 3 Goal, 30 Task, 60 Execution | Actual event trail, formal Returns, distinct decisions, restart and command replay |
| S02 Concurrency and invalid input | Concurrent distinct claims, duplicate delivery, conflicting idempotency payload, cross-task selection | Independent negative tests; rejected operations leave no event |
| S03 Goal Challenge and final acceptance | Define Goal Challenge against frozen sources, implement and validate it, then assemble full Phase 4 report | Not yet implemented; no invented Goal Challenge schema or PASS |

Executable plan: `development/autodev/M02.json`. Current state is the local
`M02.state.json` when present. Tests are independent processes; model worker is
not required for these preimplemented engineering inputs. No M01 tags are changed.

## Exit and gaps

S01/S02 are intermediate engineering checkpoints. M02 cannot be marked complete
until S03 covers Goal Challenge, capability gaps and dirty-data scenarios against
the frozen design with sufficient explicit tests. A blocked boundary scenario
alone does not implement a capability system. The current scale run is sequential
command traffic with overlapping attempts, not a throughput benchmark. S02 adds
bounded real thread concurrency but does not certify production load capacity.

No push, deployment, existing-domain change or auto-writeback reactivation is
allowed without explicit user confirmation. Local checkpoints and isolated tests
are allowed. The existing Aliyun website and database are outside test scope.
