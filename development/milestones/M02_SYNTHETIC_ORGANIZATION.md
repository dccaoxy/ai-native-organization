# M02 — Synthetic Organization

Phase 4 / M0 robustness. Entirely synthetic; no Human Pilot or real company data.
The frozen Final Design Baseline and existing M01 semantics remain authoritative.

Local status: S01–S04 PASS within the declared synthetic engineering coverage.
Full suite: 122 tests. Integrated scale: 536 events, 16 assertions. No push or
deployment. See `development/M02_ACCEPTANCE.md` for commits, evidence and limits.

## Stages

| Stage | Engineering outcome | Required evidence |
|---|---|---|
| S01 Scale fixture | 10 HAU, 3 Goal, 30 Task, 60 Execution | Actual event trail, formal Returns, distinct decisions, restart and command replay |
| S02 Concurrency and invalid input | Concurrent distinct claims, duplicate delivery, conflicting idempotency payload, cross-task selection | Independent negative tests; rejected operations leave no event |
| S03 Goal Challenge core and workbench | Evidence-based challenge; Human Keep/component Modify; version/diff/direct impact | Authority, concurrency, rollback and HTTP tests; actual browser interaction |
| S04 Integrated acceptance | Goal Challenge integrated with 60 attempts; cumulative regression and audit | 536 actual synthetic events; 16 assertions; 122 tests; local artifact |

Executable plan: `development/autodev/M02.json`. Current state is the local
`M02.state.json` when present. Tests are independent processes; model worker is
not required for these preimplemented engineering inputs. No M01 tags are changed.

## Exit and gaps

The originally combined S03 was divided into S03 core/UI and S04 cumulative
acceptance so new UI/API evidence remains independently reviewable. No frozen
semantics changed. The declared engineering slice has passed; this does not
implement full Goal lifecycle, reparenting or a multi-goal dependency graph.
A blocked boundary scenario alone does not implement a capability system;
learning remains M03 scope. The current scale run is sequential
command traffic with overlapping attempts, not a throughput benchmark. S02 adds
bounded real thread concurrency but does not certify production load capacity.

No push, deployment, existing-domain change or auto-writeback reactivation is
allowed without explicit user confirmation. Local checkpoints and isolated tests
are allowed. The existing Aliyun website and database are outside test scope.
