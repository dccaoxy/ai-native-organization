# AA01 — Independent Agent access and joint protocol testing

Inserted before M03 by explicit user request. Local synthetic engineering only;
formal push and deployment require separate confirmation. No domain/server edits.

Local acceptance: S01–S03 PASS; 133 cumulative tests, including 11 access tests. Actual model-assisted protocol run retained 18 synthetic events. See [acceptance package](../AA01_ACCEPTANCE.md). Not pushed or deployed.

## Contract and trust

An Agent registers id/name/version/declared capabilities with its own randomly
generated bearer credential. Registration is pending and confers no task access.
The operator, acting as an explicitly labelled synthetic Human, approves a HAU,
delegable command list and exact task allowlist. The server binds authenticated
requests to the resulting Agent identity; the client cannot supply an actor.
Each Execution still belongs to one Human. Capabilities are declarations, not
verified ability or permissions. Approval and revocation are formal events.

This gateway runs on loopback with a dedicated database and operator key. It
does not serve the legacy simulation identity-switcher or a public operator key.
Legacy UI refuses to open a database marked as an Agent lab. Do not run another
legacy process against that database before gateway creation. Multiple gateway
processes on one database are unsupported; a process-wide lock serializes
authentication/revocation with commands. Untrusted processes with access to the
same OS account/database can bypass application credentials: this lab is not an
OS sandbox or production Human identity system.

Server stores only SHA-256 of high-entropy Agent credentials. Event receipts
never contain credential plaintext. Credential reservation before registration
event is recoverable by repeating the same id/token; until the formal enrollment
exists authentication fails closed. Replaced/revoked registrations cannot regain
access through replay. Lost credentials require a new registration and explicit
approval; rotation, expiry and recovery UI remain future work.

## Endpoints

| Route | Credential and behavior |
|---|---|
| POST /v1/agents/register | New Agent bearer; id/name/version/capabilities; pending |
| GET /v1/me | Agent bearer; own registration, including pending status |
| GET /v1/tasks | Approved Agent; published tasks in explicit allowlist |
| GET /v1/executions | Approved Agent; own HAU and allowed task attempts |
| POST /v1/commands | command/data/idempotency_key; actor derived server-side |
| POST /control/commands | Separate operator bearer; synthetic Human/bootstrap commands |
| GET /control/state | Separate operator bearer; lab operator state inspection |

No browser Origin requests or non-loopback Host are accepted. Client disables
redirects and refuses to forward an identity file to a different origin.
Agent calls cannot bind/approve/revoke identities, decide boundaries, accept,
select or change Goal authority. New scopes require explicit Human operations.
The protocol returns command events rather than unrelated global state.

## Run locally

From repository root, start a dedicated lab (keep this process running):

```console
python -m organization.agent_gateway --port 8877
```

In another terminal, create explicit synthetic control identities and a task:

```console
python -m organization.agent_operator init-fixture
python -m organization.agent_client register
python -m organization.agent_operator list
```

Review the registration, then substitute its printed id in this approval:

```console
python -m organization.agent_operator approve --registration REGISTRATION_ID --human H0 --hau U0 --tasks T --permissions claim,ack,progress,submit,fail,release,request_boundary,resume
python -m organization.agent_client run --task T --run-id attempt-1
python -m organization.agent_operator state
python -m organization.agent_operator revoke --registration REGISTRATION_ID --human H0
```

The operator and Agent identity files live under ignored `.autodev/`. Treat them
as credentials; do not upload, paste into chat or put into Git/artifacts. Files
are created with restrictive POSIX mode; Windows inherits directory ACLs. Keep
the directory limited to the trusted development account. This is not a public
registration service or production Human authentication.

## Automatic tests and evidence

```console
python -m unittest tests.test_agent_access -v
python -m organization.agent_demo
python -m organization.agent_demo --model --output development/autodev/agent-model-demo
```

The last command consumes the already-authorized ChatGPT/Codex account. It gives
the model only synthetic task context; no Agent/operator credentials. The model
generates Return content, while the independent subprocess client performs the
protocol. Synthetic control actors review shape/trace and close the loop; this
does not claim independent semantic review, business acceptance or autonomous
model planning. The source of all fixture identities is explicit.

Stages: S01 registration/auth/scope; S02 independent client lifecycle and negative
paths; S03 cumulative and live-model evidence validation. Local state, receipts,
tags and artifacts are indexed by `development/autodev/AA01.state.json`.
No chat history is required to reproduce tests or resume this milestone.

Before any server test/package release, recheck dedicated paths/ports and the
user's approval boundary. Before formal push/deployment, show concrete changes,
test evidence and rollback plan and wait for explicit confirmation.


AA02 adds a Human browser shell on the dedicated gateway; same-origin control requests require the independent operator credential. Historical AA01 tests and tags remain unchanged. See [AA02](AA02_HUMAN_AGENT_WORKSPACE.md).
