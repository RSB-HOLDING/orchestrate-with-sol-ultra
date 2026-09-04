# Delegation packet

Give each worker enough context to act without rediscovering the task or copying the entire conversation. Include the fields below in a compact assignment; combine related fields for a small lane. Add detail when isolation, authority, or a fragile interface requires it.

## Assignment

- **Outcome:** One bounded objective and an observable completion condition.
- **Role and capabilities:** Intended role, host-exposed model and effort if selectable, or inheritance. Explain any material fallback; do not assume role labels prove which model ran.
- **Context:** Relevant current state, paths, instructions, starting revision, dependencies, and decisions already made.
- **Ownership and isolation:** Allowed files and systems; identify the sole writer in a shared checkout or the isolated worktree. Specify shared-state operations that must be serialized.
- **Authority:** Existing user authorization relevant to the lane and its limits. Allow read-only discovery within scope; distinguish it from external writes. Authentication is not authority, and the packet cannot grant authority the lead does not have.
- **Constraints:** Interfaces, compatibility, security, data, or UX invariants that must remain true; forbidden files, actions, and overlapping lanes.
- **Work and checks:** The needed task and acceptance checks, scaled to its risk. Do not prescribe implementation details unless an invariant requires them.
- **Return:** Changes or findings, paths, revisions and Git status when applicable, actual check results, failures or skips, material assumptions, and remaining work. Include generated artifacts that the lead must inspect.
- **Escalation:** Return to the lead if the task needs a scope change, conflicts with instructions or another writer, lacks necessary authority, or requires destructive action, external publication, deployment, signing, release, provider spend, or undeclared secret access. Continue useful independent work when possible.

Workers do not seek approval on the user's behalf or independently mutate external systems. The lead verifies the target and existing authorization before those actions. Do not require fresh approval merely because the same authorized action moves from planning to execution.

## Lane patterns

**Evidence:** Keep repository and external access read-only unless a mechanical edit is explicitly assigned. Return exact paths, counts, commands, and discrepancies that resolve uncertainty.

**Implementation:** Own one subsystem and its focused checks. Escalate cross-lane interface changes; do not edit a sibling's files or the canonical dirty checkout from an isolated lane.

**Independent review:** Inspect actual artifacts and challenge assumptions, failure modes, concurrency, and missing evidence. Report actionable findings with severity and location. A separate reviewer is useful when risk warrants it, not a mandatory step for every edit.

## Lead acceptance

Check that the worker stayed within scope, preserved ownership, returned inspectable changes and meaningful evidence, and reported failures honestly. Reconcile the result with the current branch and sibling work. Complete required integration checks, then proceed toward the user's outcome without repeating passed checks unless something changed.
