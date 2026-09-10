# Cloud runner and Human decision boundary

Backend: GitHub-hosted Linux runner (`.github/workflows/autodev.yml`), Python
standard library + Git. Push and manual dispatch run immediately; scheduled
wakeups occur every six hours on the default branch, subject to GitHub scheduler
availability. No local chat or laptop must remain open for these jobs.

The workflow separates read-only validation from default-branch checkpoint
writeback. Pull requests cannot enter the writeback job. Action dependencies are
pinned to upstream verified commit IDs. GitHub's repository-scoped GITHUB_TOKEN
is sufficient for ordinary commits/tags if repository policy allows workflow
writes. No PAT, paid model subscription or company-system secret is assumed.
Push conflicts fail visibly and retain CI artifacts; force-push is forbidden.

GitHub does not generally retrigger push workflows for GITHUB_TOKEN-generated
commits; the runtime advances stages in the same job, with schedule/manual
dispatch as the durable next wakeup. Scheduling is best effort, not a timing SLA.
Sources: [GITHUB_TOKEN](https://docs.github.com/en/actions/concepts/security/github_token),
[workflow events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows).

## AUTHORIZED_PENDING_PROVISIONING — unattended code authoring

Current cloud backend can build, test, review, audit, checkpoint and resume
prepared Stage inputs. No unattended model Builder/Repair account is configured.
On 2026-09-10 the user selected ChatGPT-authenticated Codex, authorized full
permissions for dccaoxy/ai-native-organization, and set no additional resource
ceiling. Do not ask for those decisions again. Platform quotas still apply.
Existing finite retry/repair budgets prevent failure loops; they are not a new
spending ceiling. Frozen-design, real-world authority and non-destructive Git
rules remain in force.

Local `codex login status` was verified as `Logged in using ChatGPT`.
`codex exec` can reuse saved CLI authentication; a separate API account is not
required for this selected route. A cloud worker still needs its own working
authentication and durable execution environment. No credentials have been
copied and no cloud model execution has been verified.

Next: implement and verify the Codex adapter locally, then provision a trusted
persistent model runner. Prefer device login on that runner. Account-auth CI is
an advanced option requiring secure persistence of refreshed credentials; the
official guide excludes public/open-source repositories from that CI workflow.
Verify repository visibility and runner trust before choosing that deployment.
Never store account credentials in Git, artifacts or logs.
Sources: [Authentication](https://learn.chatgpt.com/docs/auth),
[Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode).

The argv adapter protocol is already generic; provisioning does not block local
engineering or cloud verification. Until implemented, a missing implementation or
repair remains BLOCKED_ENGINEERING with persistent evidence, not a fictional
completed milestone. Enabling a model worker must retain independent Reviewer
and Auditor roles, digest-bound receipts, bounded retries and explicit gates.

Further real Human Pilot, company data/actions, reward policy, residual risk and
Frozen L1/L2 changes each require their own scoped Human decision. No such real
authority was exercised by M01's labelled synthetic scenario.

## Verification status

First verified run: [34427710307](https://github.com/dccaoxy/ai-native-organization/actions/runs/34427710307),
verify and resume both successful on Linux, including test execution, frozen
baseline provenance, simulation, artifact upload and ordinary Git push.

`CLOUD_RECEIPT.json` records a real cloud worker observation and is committed by
the cloud job. It is refreshed only when the candidate or Stage status changes,
avoiding unchanged scheduled-run commits. Final delivery checks fetch the bot
commit back from origin, rather than treating a local receipt as remote proof.
