# Delegation Packet

Use this packet for every worker. Every field is mandatory. Write "none" with a reason when a field does not apply; do not remove safety or approval fields.

## Worker assignment

**Objective:** State one bounded outcome.

**Role and model:** Name the intended role, preferred model, and reasoning level. Explain the choice in one sentence.

**Completion condition:** Describe the observable result that makes the lane complete.

**Context:** Include only the task facts, repository instructions, paths, interfaces, and prior decisions needed for this lane.

**Allowed scope:** List owned files, directories, commands, or read-only systems.

**Do not:** List forbidden files, external systems, approvals, overlapping lanes, and unrelated cleanup. State that authentication is not authority and that the worker must not run `gh`, push, open or update a pull request, comment, merge, tag, release, publish, deploy, sign, spend, access undeclared secrets, or mutate an external system without fresh exact user approval and a verified target.

**Workspace isolation:** Name the isolated worktree or environment. If the lane shares a checkout, declare it read-only or the sole writer and list every shared-state command that must be serialized.

**Invariants:** State contracts that must remain true, including compatibility, security, data, migration, and UX constraints.

**Required work:** Give the shortest ordered checklist that still leaves room for expert judgment.

**Verification:** Name exact focused checks and the broader evidence expected. If a check cannot run, require the worker to say why.

**Return:** Require a concise summary with starting and ending revision, final `git status`, exact diff or changed-file inventory, generated and untracked artifacts, commands run, changes, evidence, failures, assumptions, risks, and recommended next action.

**Stop and escalate when:** Define ambiguity, conflict, permission, destructive-action, cost, secret, or architecture thresholds that must return to the lead. Always stop before any destructive action, external mutation, provider spend, undeclared secret access, push, pull-request or issue mutation, merge, signing, publication, deployment, tag, or release. Only the lead may proceed after fresh exact user approval.

## Common lane patterns

### Luna evidence lane

- Make it read-only unless the change is truly mechanical.
- Ask for exact paths, counts, commands, and contradictions.
- Use it to reduce uncertainty before expensive implementation.

### Terra implementation lane

- Give it one subsystem and non-overlapping file ownership.
- Require focused tests and a diff summary.
- Escalate cross-cutting architecture changes to the lead.

### Sol Ultra review lane

- Keep it independent from the implementation author when possible.
- Ask it to attack assumptions, failure modes, security boundaries, concurrency, migrations, and release claims.
- Require severity-ranked findings and concrete evidence, not stylistic preference.

## Acceptance checklist for the lead

- The worker stayed inside scope.
- Starting and ending revisions, final status, exact changes, and generated artifacts are recorded.
- The returned evidence can be independently reproduced.
- No user approval or external mutation was silently assumed.
- The lane integrates with current repository state and sibling lanes.
- Required tests passed, or failures and skips are explicit.
- The final user-facing claim is no stronger than the evidence.
