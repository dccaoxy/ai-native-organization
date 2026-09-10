# ChatGPT-authenticated model adapter

Status (2026-09-10): local live model smoke PASS, cloud model worker NOT deployed.
See `CODEX_SMOKE.json` and `codex-smoke-artifact.zip`. Smoke commits/tags belong
to a disposable test repository, not the main repository. M01 tags are unchanged.

## Execution contract

Use `autodev.codex_adapter` for a future, reviewed Stage's build and repair argv:

```json
{
  "model_write_paths": ["organization/new_module.py", "tests/test_new_module.py"],
  "timeout_seconds": 900,
  "commands": {
    "build": ["{python}", "-m", "autodev.codex_adapter"],
    "repair": ["{python}", "-m", "autodev.codex_adapter"]
  }
}
```

This fragment is not a complete executable plan. Supply the normal inputs,
outputs, scope, dependencies, tests, independent review/audit commands, principle
checks and gates. Both model_write_paths and scope must cover each edited file.
Keep M01's passed plans unchanged; define new work with new plan/stage IDs.

The adapter receives AUTODEV_PLAN/STAGE/ROLE/REPORT/SOURCE_DIGEST/NONCE from the
harness. It invokes Codex with saved account auth, read-only sandbox, ephemeral
session, ignored personal config/plugins, and structured output. No explicit
model override is selected. The adapter applies full-text file replacements
after validating all paths. It cannot delete files or edit the harness, runtime
records, Git metadata, workflow files, AGENTS.md or frozen baseline. A new stage
requiring harness changes is implemented/reviewed through ordinary engineering.

The model only proposes edits; its success is not Stage PASS. Tests, separate
review/audit processes, frozen hashes and checkpoint rules still apply. Built-in
review/audit remain deterministic, not independent LLM certification. Full file
replacement replay is idempotent; partial interrupted writes are revalidated on
resume. Model timeouts and quota/auth failures block engineering with receipts.

A model Human decision is nonce-bound, persisted, and never sent to automatic
repair. Resume remains paused until a human decision is recorded and the reviewed
stage sets `model_gate_resolution` to that exact gate nonce. Do not populate that
field automatically. Technical failures use BLOCKED_ENGINEERING instead.

## Local verification

```console
codex login status
python -m unittest tests.test_codex_adapter -v
python -m autodev.codex_smoke
```

The last command consumes real account usage and creates an isolated synthetic
Git repository. It retains only a summary and source artifact, never account
caches or raw model transcripts. It validates model generation, deterministic
acceptance, checkpoint, automatic next-stage gate and idempotent resume.
It does not claim live-model repair or real organizational acceptance. Failure
repair is separately exercised by the offline harness tests.

## Cloud deployment decision package

GitHub repository API verified this project as PUBLIC, with current GitHub
connection admin permission. Official account-auth CI guidance excludes public
or open-source repositories. Do not add the ChatGPT auth cache to this repository's
Actions secrets or enable an account-auth self-hosted Actions job here.

The remaining required input is an identified trusted remote execution host or
an approved private execution environment. No such host/account endpoint has
been supplied or provisioned. The project's visibility has not been changed.
Existing public-repository Actions continues account-free verification.

For a selected independent trusted host, prepare an isolated OS user/container,
Python 3.11+, Git and Codex CLI; authenticate on the host using device login:

```console
codex login --device-auth
codex login status
```

Keep credentials in that host's protected account storage outside source,
artifacts and logs. Authentication must be tested on the destination. Browser
confirmation may require the user; laptop operation is not needed afterwards.
Before enabling an unattended service, verify host isolation and source trust,
run the live smoke, configure a durable scheduler/queue and a reviewed model
stage plan, and test checkpoint push and restart on that actual host. Website
intake/queue integration is separate work and is not enabled by this adapter.

Do not equate this preparation with deployed persistence or claim the current
chat will continue after exit. No cloud purchase or remote account credential
copy occurred. Resource/repository authorization is already granted; ask only
for the missing destination/login or an actual change of deployment choice.

Sources checked: [Authentication](https://learn.chatgpt.com/docs/auth),
[Non-interactive execution and account-auth CI restriction](https://learn.chatgpt.com/docs/non-interactive-mode).
