# M02 local synthetic engineering acceptance

Status: S01–S04 PASS locally. No GitHub push, remote deployment or real company
systems were used for these changes. Full regression: 122 test executions PASS.

| Stage | Local commit | Immutable local tag |
|---|---|---|
| S01 Scale/replay | e940a5a | autodev/M02/S01/v1 |
| S02 Concurrency/invalid input | 4bcc8cb | autodev/M02/S02/v1 |
| S03 Goal Challenge and workbench | b48b68b | autodev/M02/S03/v1 |
| S04 Integrated acceptance | 02b5d6c | autodev/M02/S04/v1 |

Artifacts, candidate hashes and separate review/audit reports are indexed by
`autodev/M02.state.json` under `autodev/runs/M02/`. The adapters use independent
processes and configured negative checks, not independent Human/LLM certification.

Integrated scenario: 10 synthetic HAU, 3 Goal, 30 Task, 60 Execution, 60 Return,
60 Review, 60 Acceptance, 30 Selection. Actual run produced 536 events and passed
16 assertions including Keep/Modify Goal Challenge, versioned evidence, live
branch impact, failure, blocked/authorized scope gap, runtime interruption,
reopen and exact replay. See `autodev/m02-final/report.json`, `events.json` and
`state.json`. Parallel worker tests separately cover 20 distinct claims and 24
duplicate deliveries on 8 threads, conflicting keys and rejected cross-task
selection. This is not a production performance guarantee.

The local workbench now provides Goal challenge forms, Human Keep/Modify
decisions, revision differences, evidence and directly affected work lists.
Browser interaction was verified against an isolated database: v0 remained
unchanged after proposal and became v1 only after the Human fixture decision;
the page displayed the retained history. See `autodev/M02_UI_VERIFICATION.json`.

## Explicit coverage limits

Goal modification in this slice covers desired_change and success_criteria.
Boundary changes cannot inherit arbitrary risk/data permission from Goal ownership.
Pause/Achieve/Terminate/Supersede, reparenting, full multi-goal dependency graphs
and impact-resolution workflows are not implemented here. Task/Execution
contracts and existing results are retained; impact lists do not silently change
or globally pause downstream work. Synthetic scope/capability gaps exercise
blocked/escalation semantics, not M1 learning or an implemented capability system.

The original frozen design remains intact. These limits are preserved in
`specs/M02.final-coverage.json`; no real Human, culture or E01–E08 outcome is claimed.

## Next and release

Next engineering work is an M03/M1 specification for evidence/knowledge/capability
lineage, with the above lifecycle/dependency gaps retained as an explicit backlog.
Review these local changes and provide a release/rollback package before asking
for push or deployment approval. Do not reactivate the paused cloud writer.
