# AD00 — Autonomous Development Runtime v0

GitHub is the Development Source of Truth. A chat, Work process, laptop, or CI
container is never the authoritative runtime state.

## Names and mission

| Name | Meaning |
|---|---|
| Phase 0–9 | Project lifecycle, including real research and deployment gates |
| M0 / M1 / M2 | Implementation maturity / launch scope |
| Milestone | Independently acceptable engineering outcome, such as AD00 or M01 |
| Stage | Automatic advancement unit inside one Milestone, such as M01 S01 |

AutoDev's engineering mission extends from the current baseline through Phase 8
Organizational Automation. It can build software and run labelled simulations;
it cannot certify Human Pilot results, accept real risk, or complete Phase 9
Scale to 60 through software execution. Phase 9 requires real Humans, elapsed
time and experimental evidence. Existing frozen design terminology is preserved.

## Architecture and trust boundary

`M01.json` is an executable stage plan. Each Stage specifies dependencies,
inputs, outputs, scope, build/test/review/audit/repair argv adapters, exit criteria,
principle checks, finite repair budget and Human gate conditions. The runner
executes subprocesses with a bounded timeout; it has no dependency on a vendor
SDK, model session or cloud API. Local/Work and GitHub Actions execute the same
protocol. Adapters are trusted code, **not a sandbox**; only reviewed default
branch commands may receive scoped cloud write credentials.

Builder compiles checked-in engineering inputs. Test runs positive scenarios.
Reviewer is a separate process running independent negative tests; it tries to
break authority, state, idempotency and accountability assumptions. Auditor is
another process checking pinned frozen files and principle-mapped tests. Both
emit machine-readable findings and readable reports with a candidate digest and
per-attempt nonce. They cannot return Builder's PASS as their own evidence.
These are deterministic review/audit adapters, not claims of independent Human
or LLM review or exhaustive compliance with all 101 L2 principles. A model-based
build/repair/review adapter is replaceable via the same argv/receipt contract;
no model credentials are assumed or inferred from a desktop login.

## Durable protocol

1. Acquire OS lock (shared Git common directory); CI additionally serializes by
   repository concurrency group. A dead process releases the OS lock.
2. Check dependencies, frozen files and active Human gates before Build.
3. Persist attempt and state before running each command. Run Build → Test →
   Review → Audit. Candidate mutation during verification invalidates the run.
4. A failed command triggers a configured Repair, then a complete new attempt,
   including fresh Test, Review and Audit. Default is two repairs / three total
   attempts; interruption consumes an attempt. Budget never resets on resume.
5. Missing inputs, absent repair adapter or exhausted retries are
   `BLOCKED_ENGINEERING`, not invented Human Authority decisions. A new worker
   inspects preserved logs and supplies a repair; a deliberate budget extension
   requires a recorded engineering decision, not a silent infinite loop.
6. Active Purpose/Authority/Risk/external-data/Frozen-L1/L2 conditions yield
   `HUMAN_DECISION_REQUIRED`. No timer, reviewer or empty answer grants approval.
   Record a scoped decision with evidence and update the reviewed stage spec to
   release the gate. This v0 has no automatic Human approval service.
7. PASS candidate produces an artifact ZIP, manifest and exact artifact SHA256,
   then a `CHECKPOINT_PENDING` journal record, scoped Git commit and immutable
   annotated tag. Final state metadata is committed separately. A crash between
   commit/tag/state is reconciled from the tag and durable marker on resume.
8. The next Stage starts automatically. Passed Stages are not rebuilt on routine
   resume. Their evidence applies to their tagged candidate; later Stages rerun
   cumulative suites. Changing a passed outcome requires a new Stage/revision.

Text hashes normalize CRLF to LF across Windows/Linux; binary artifact hashes
are byte-exact. Each attempt retains logs and receipts. Central records include
formal execution evidence, never private reasoning or credentials. Repository
state writes use fsync + atomic rename. Clone/fetch full Git history and tags to
resume. Abrupt cloud loss may discard uncommitted partial work; the last pushed
checkpoint remains recoverable and any repeated command must be idempotent.

## Running and recovery

Python 3.11+ and Git; standard library only. From repository root:

```console
python -m unittest discover -s tests -v
python -m autodev.runtime run
python -m autodev.runtime status
python -m autodev.runtime run --limit 1
python -m autodev.runtime rollback --tag autodev/M01/S01/v1 --destination .autodev/rollback-s01
```

Rollback creates a new detached worktree at a known checkpoint. It never resets
the current branch, deletes history or overwrites a tag. Use `run --limit 1` to
reconcile its pending checkpoint; continuing an alternative history requires a
new plan/revision namespace so existing tags cannot be reused. A forward repair
is a normal new commit. Force-push and automatic history rewrite are forbidden.

All Stage code/scopes must be reviewable before a checkpoint; unrelated staged
files stop checkpoint creation. Runtime metadata is under `development/autodev`.
`CURRENT_STATE`, `NEXT_ACTIONS`, M01, Milestones and `DASHBOARD.md` are projections
updated from the journal. Obsidian receives the Dashboard projection after push;
it never becomes a second development state source.

## Cloud continuity

GitHub Actions uses the same runner on push, scheduled wakeups and manual
dispatch. It persists state commits/tags, then pushes with normal fast-forward
semantics. Artifacts are retained both in Git and as CI artifacts. A failed push
must be visible and must not be converted into a successful checkpoint delivery.
No unreviewed pull request receives write permission. No paid compute/model or
company system is provisioned by this code.

Cloud execution can verify/build prepared inputs and advance their engineering
stages. Unattended invention or repair of new code requires a separately
configured agent/model adapter and its account/budget authority. Without one,
the persistent runtime reports `BLOCKED_ENGINEERING` and waits for a worker;
it does not claim an autonomous coding service is running.
