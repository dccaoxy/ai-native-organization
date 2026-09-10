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

## HUMAN DECISION REQUIRED — unattended code authoring

Current cloud backend can build, test, review, audit, checkpoint and resume
prepared Stage inputs. No unattended model Builder/Repair account is configured.
To autonomously author unimplemented milestones beyond M01, Human must choose
the provider/account, allowed code/model access, spending limit and secret
provisioning mechanism. Do not infer cloud model access from desktop login.

The argv adapter protocol is already generic; this decision does not block local
engineering or cloud verification. Until supplied, a missing implementation or
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
