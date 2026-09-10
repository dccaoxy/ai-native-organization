# M01 acceptance package

Scope: Phase 2–3 / M0 engineering prototype. Every actor and organization datum
in the automated scenarios is explicitly synthetic. No Human Pilot, business
impact, E01–E08 conclusion or production authorization is claimed.

| Required outcome | Executable evidence | Frozen principle |
|---|---|---|
| Typed objects, state machines, event/authority/interface contracts | tests.test_contract / tests.test_contract_review | TASK-09/10, WORK-08 |
| One persistent replayable reality and idempotency | tests.test_store / tests.test_store_review | REALITY-01/02, AGENT-11 |
| 1 Goal, 1 Task, 3 independent accountable attempts | tests.test_core / tests.test_core_review | GOAL-02/04, TASK-04/09/10 |
| Human/HAU/active representative identity; interruption recovery | tests.test_identity / tests.test_identity_review | AGENT-01/05/07/09 |
| Progress, Blocked, Escalation, explicit Human boundary decision | tests.test_work / tests.test_work_review | WORK-02/11, GOV-09 |
| Success, failure, release have formal Return and Human annotations | tests.test_returns / tests.test_returns_review | WORK-10, TASK-11 |
| Review, Acceptance, Selection are different actions and authorities | tests.test_returns_review | WORK-06/07/08 |
| Real loopback HTTP commands and visible working application | tests.test_http / tests.test_http_review | REALITY-01, GOV-04 |
| Complete M01 through HTTP, replay, selection and interruption | tests.test_simulation / tests.test_simulation_review | M01 frozen outcome |

Run `python -m organization.simulation` to generate `development/autodev/simulation/`
with actual executed synthetic events, state and assertion results. Run the
complete suite using `python -m unittest discover -s tests -v`. Stage S08's
tag, bound review/audit receipts and candidate ZIP are the acceptance checkpoint;
this document alone is not a PASS.

## Human/Agent interface and pages

Start `python -m organization.server`; open `http://127.0.0.1:8765`.
The workspace supports labelled synthetic bootstrap, Goal, task publication and
claim, ACK, progress/blocked/escalation, scope request/approval/rejection/modification,
success/failure/release Return, Human Confirm/Correct/Add, review, acceptance,
selection and a common event trail. Actor selection is explicitly a simulation
control, not real user authentication. The API requires the loopback page's
per-process session token and rejects foreign Origin/Host requests.

HTTP/Agent command envelope:

```json
{"actor":"H1","command":"ack","data":{"execution_id":"E1"},"idempotency_key":"unique-command-id"}
```

POST `/api/commands`; GET `/api/state`, `/api/events`, `/api/task-wall`.
Errors are explicit 400/403/409; real mode returns HUMAN_DECISION_REQUIRED (503).
Adapters must map an authenticated real identity to actor before any future
Human Pilot. Never expose the simulation identity selector as production auth.

## Known scope limits

- Standard-library SQLite reference application, loopback only, not a production
  company-system integration or a security boundary against local administrators.
- M01 does not implement an intelligent Agent backend; bindings and runtime
  failures are real application state driven by explicitly synthetic fixtures.
- Reviewed Returns are immutable in v0. Human annotations are accepted before
  Review; later corrections require a separately reviewed change proposal/new
  attempt so old credibility and acceptance judgments cannot silently go stale.
- Free Work Space contains private process outside the event store. Only explicit
  public WorkSignal summaries and formal Returns cross the organizational boundary.
- Boundary cancellation on terminal Return and WorkSignal are additive engineering
  contract revisions 2/3; L1/L2 and the frozen M01 outcome are unchanged.
- ACK/progress timeouts are registered Tunable engineering defaults, not verified
  research conclusions. A sweep records interruptions without fabricating Return.
- Deterministic independent-process review/audit has finite coverage. It is not
  an independent Human/model architecture certification or proof that all L2
  mechanisms across M1/M2 have been implemented.
