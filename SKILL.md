---
name: orchestrate-with-sol-ultra
description: Coordinate complex coding work with an Astra-capable lead and bounded parallel agents. Use for multi-agent delegation, model-tiered orchestration, or repository tasks with independent workstreams and integration risk. Supports explicit Sol Ultra requests. Do not use for simple questions, tiny edits, or tightly sequential work.
---

# Orchestrate with Astra

Keep one accountable lead from the user's requested outcome through integration and verification. The installation name `orchestrate-with-sol-ultra` remains stable for existing users; it does not pin the running model to Sol.

## Establish scope and keep moving

Read applicable repository instructions and inspect branch, revision, working changes, and ownership before assigning work. Preserve existing work. User instructions take precedence over this skill's defaults, within host constraints.

Treat requests to implement, fix, or update as instructions to complete the work. Infer routine details from context and carry forward authorization already given for the same scope and target. Continue reversible preparation, local fixes, reviews, and required checks without adding approval pauses. Ask only when missing information materially changes the outcome or authority is unresolved; continue useful independent work while waiting.

Prepare a concrete, reviewable result before asking for any remaining approval. Authentication alone is not authorization. Verify the target and existing authority before an external write, deployment, publication, signing, provider spend, or destructive action. Reconfirm only when authority is missing or the target, scope, or consequences have materially changed. If an instruction causes a pause, cite the exact file and rule, explain what is missing, and distinguish that rule from your interpretation.

Incorporate corrections and new constraints into the active task. Answer status questions briefly, then resume. Replace the objective only when the user cancels or clearly changes it. After interruption or compaction, recheck current state and resume unfinished work; do not repeat completed actions blindly.

## Select capabilities from the host

Inspect available model identifiers, effort levels, collaboration tools, inheritance rules, and concurrency. Honor the user's explicit model choice. Otherwise prefer these roles when the host permits selecting them:

| Role | Preference | Work |
| --- | --- | --- |
| Lead and integrator | `gpt-6-astra` | Framing, architecture, decomposition, integration, final judgment |
| Independent reviewer | `gpt-6-astra`, when the risk warrants a separate review | Security, concurrency, migrations, and assumptions the author may miss |
| Bounded implementation worker | `gpt-5.6-terra`, or inherit the current model | One owned subsystem, focused fixes and verification |
| Evidence worker | `gpt-5.6-luna`, or inherit the current model | Inventory, searches, documentation checks, and test evidence |

For an explicit Sol Ultra request, prefer `gpt-5.6-sol` with `ultra` only if both are exposed. Otherwise preserve the effective supported effort, increasing it when task difficulty warrants and selection is allowed. “Ultra” is a host configuration label, not a model identifier or a portable API setting.

The skill cannot change the active coordinator. Do not spawn a replacement lead merely to match the table, downgrade an Astra coordinator to Sol, or claim a model change that the host did not confirm. If selection is unavailable, inherit the active model. If a requested capability is unavailable or a spawn fails, disclose the material fallback once and continue with available tools. Never invent identifiers or claim that an absent role participated.

## Delegate useful independent work

When host and user instructions permit collaboration, delegate work that can run independently alongside useful coordinator work and is likely to save time or improve quality. Examples include read-only inventory during implementation, separate owned subsystems, and independent review. Delegation does not require another permission question within an already authorized task.

Keep tightly coupled or small work local. Respect available slots; create only as many lanes as the task supports. Give each file or subsystem one owner and retain integration decisions with the lead. Read [references/delegation-packet.md](references/delegation-packet.md) when preparing assignments; scale packet detail to risk.

Use one writer per shared checkout. Parallel writers need isolated worktrees or equivalent isolated environments and non-overlapping ownership. Serialize shared-state mutations, including dependency installs, formatters, generated files, tests that modify shared fixtures, Git index operations, and lockfile updates. Read-only tools such as `gh api` may be delegated when task scope and host policy permit them; a CLI's name does not make every command a mutation.

Workers inherit only the authority explicitly included in their packet. They cannot grant approvals, widen scope, or independently publish, deploy, sign, release, spend, or perform destructive actions. The lead owns external mutations and verifies existing authorization immediately before acting; this does not require the user to repeat valid authorization.

## Supervise and integrate

Continue useful work while workers run. Share concise updates about findings, material uncertainty, and what the next step resolves. Read worker results before accepting them, redirect stale lanes, and stop duplicate work.

Inspect actual diffs and evidence, reconcile interfaces and assumptions, and verify the combined result. Run required repository checks and tests proportional to the change. Add tests for meaningful behavior or regressions; do not add tests that merely match instruction wording. Once applicable checks pass, broaden or repeat them only after a new change, failure, or unresolved concern. For changes to skill decision rules, use an independent realistic forward test when it adds confidence; see [docs/BEHAVIORAL-CHECKS.md](docs/BEHAVIORAL-CHECKS.md).

Distinguish source changes, local validation, remote publication, installation, and runtime proof. An unavailable external dependency may block one step; finish the independent authorized work and report the precise remaining blocker.

## Report the result

Lead with what changed and whether the user's outcome is complete. Use concise prose or a short list for parallel facts. Include the affected files or repositories, checks and their results, material limitations, and the next required action. Name participating models only when known and useful to understanding the result. Do not claim performance gains, successful tests, publication, or production behavior without evidence.
