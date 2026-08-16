---
name: orchestrate-with-sol-ultra
description: Coordinate complex coding and operational work with GPT-5.6 Sol in a host-exposed Ultra configuration as the preferred lead, planner, integrator, and reviewer, while delegating bounded lanes to GPT-5.6 Terra or Luna. Use when the user asks for Sol Ultra, highest reasoning, multi-agent delegation, model-tiered orchestration, or a complex repository task with several independent workstreams and integration risk. Do not use for simple questions, tiny edits, or work that cannot be divided safely.
---

# Orchestrate With Sol Ultra

Use the strongest available reasoning where judgment compounds, and more efficient models where the work is bounded and independently verifiable. Keep one accountable lead from problem framing through final evidence.

## Establish the operating contract

1. Restate the concrete outcome, scope, constraints, approval boundaries, and definition of done.
2. Read all repository and task instructions before planning or delegating. Inspect the current state and preserve existing work.
3. Treat the active user request as authoritative. Do not replace a goal, change another task, or widen scope unless the user explicitly asks.
4. Keep external mutations, deployment, publication, signing, paid-provider use, destructive actions, and secret handling behind their existing approval boundaries.
5. Never claim that the active coordinator was upgraded to a model or reasoning level unless the host explicitly confirms it.
6. Let host, repository, and user instructions override this skill. Spawn workers only when the user explicitly requests or invokes multi-agent orchestration, or when host policy explicitly authorizes proactive delegation.

## Select the model topology

Inspect the models, reasoning levels, collaboration tools, and concurrency exposed by the host. Use these preferences only when they are actually available:

| Role | Preferred configuration | Assign |
| --- | --- | --- |
| Lead and final integrator | `gpt-5.6-sol` with a host-exposed `ultra` configuration | Goal framing, architecture, decomposition, risk decisions, integration, final review, and release judgment |
| Critical independent reviewer | `gpt-5.6-sol` with a host-exposed `ultra` configuration | Security, concurrency, native boundaries, migrations, irreversible operations, and adversarial review |
| Bounded implementation worker | `gpt-5.6-terra` with `high` or `max` reasoning | A clearly owned subsystem, diagnosis, implementation, focused tests, and evidence collection |
| Evidence worker | `gpt-5.6-luna` with `medium` or `high` reasoning | Repository inventory, searches, status snapshots, documentation cross-checks, test execution, and low-risk mechanical work |

If the active coordinator is not confirmed as Sol Ultra, do not pretend otherwise. Only after the delegation gate above passes, and when collaboration tools allow it, ask a `gpt-5.6-sol`/`ultra` subagent to produce the plan or independent final review, while the active coordinator remains transparent about its role.

Verify capabilities only from host-exposed metadata. If a preferred model or reasoning level is unavailable, choose the strongest named substitute the host actually exposes, disclose the fallback once, and continue. If collaboration tools are unavailable or a spawn is rejected, continue single-agent unless the task truly requires parallel execution. Do not retry with invented identifiers or claim that a requested role participated when it did not.

## Decide whether to delegate

Delegate only when at least one lane can run independently and its result will remain useful even if another lane changes. Good candidates include:

- Read-only inventory alongside implementation planning.
- Separate backend, frontend, test, or documentation ownership with non-overlapping files.
- Independent security or migration review after a proposed design exists.
- Parallel verification on different platforms or test suites.

Stay single-agent when the task is small, tightly sequential, requires constant shared context, or would create overlapping edits. Delegation overhead must be smaller than the work delegated.

Respect the host concurrency limit. Reserve enough capacity for the coordinator, and never spawn more workers than there are genuinely independent lanes.

## Build the lead plan

1. Map the critical path, parallel lanes, risks, and gates.
2. Separate facts already verified from assumptions that still need evidence.
3. Assign one accountable owner per file, subsystem, or decision boundary.
4. Keep high-coupling architecture and cross-lane integration with the accountable lead.
5. Define the evidence required to accept each lane: diffs, commands, test results, screenshots, logs, or cited source material.
6. Share a concise user update naming the active lanes and why they are separated before spawning workers.

## Delegate bounded packets

Read [references/delegation-packet.md](references/delegation-packet.md) before sending the first worker assignment.

Give every worker a self-contained packet containing:

- One objective and a measurable completion condition.
- The selected model role and why it fits.
- Relevant context, paths, instructions, and known constraints.
- Explicit allowed and forbidden files or systems.
- Required checks and evidence.
- Stop conditions and escalation rules.

Use one writer at a time in a shared checkout; keep all other lanes read-only. Parallel writers require isolated worktrees or equivalent isolated environments, non-overlapping ownership, and the lead as the sole integrator. Serialize commands that can mutate shared state, including dependency installation, formatting, code generation, tests with writable fixtures or snapshots, Git index operations, and lockfile updates.

Do not delegate user approvals, final scope decisions, destructive actions, external publication, provider spending, signing, release authority, or the final truth claim. An authenticated tool or remote is not authority: without fresh exact approval and a verified target, workers must not run `gh`, push, open or update a pull request, comment, merge, tag, release, publish, deploy, sign, or mutate an external system.

## Supervise without micromanaging

1. Continue useful coordinator work while workers run.
2. Prefer compact progress snapshots; read full worker output only when needed.
3. Redirect a lane when new evidence invalidates its assumptions.
4. Stop duplicate or stale work quickly.
5. Tell the user if a worker uncovers a material risk, permission boundary, or change to the critical path.

## Integrate centrally

The lead remains accountable for the combined result.

1. Inspect every worker's evidence and actual changes; do not accept a summary on trust alone.
2. Reconcile interfaces, invariants, naming, migrations, error handling, and documentation across lanes.
3. Review the final diff for unintended or unrelated changes.
4. Run the highest-value focused checks first, then the appropriate broader suite.
5. Distinguish clearly between source present, locally integrated, installed, staged, and production-proven states.
6. If verification fails, assign the smallest correction lane and repeat integration checks.

## Close with an evidence-based result

Report:

- The outcome and whether the original definition of done was met.
- Which roles and models actually participated, what each completed, and whether Sol Ultra was unavailable.
- Files or systems changed.
- Checks passed, failed, skipped, or not run.
- Remaining blockers, risks, approval gates, and exact next action.
- Any model or reasoning fallback that materially affected confidence.

Do not equate a large amount of code with a working product. Never describe deployment, signing, provider execution, staging, or release as complete without direct evidence.

## Example triggers

- "Use Sol Ultra to lead this migration and delegate the independent work."
- "Run the strongest multi-agent setup for this repository."
- "Have GPT-5.6 plan everything, then use more efficient models for bounded implementation."
- "Split this complex feature across agents, integrate it, and prove it works."

Do not trigger for requests such as "rename this variable," "explain this function," or "run one test."
