# Contributing

Thank you for helping improve Orchestrate with Astra (installed as `orchestrate-with-sol-ultra`).

## Before you begin

- Read [`SKILL.md`](SKILL.md) and the required [`delegation packet`](references/delegation-packet.md).
- Keep `SKILL.md` at the repository root with valid YAML frontmatter.
- Keep the skill instruction-only unless a deterministic, repeatedly needed resource clearly justifies a script or asset.
- Preserve user, host, and repository instructions as higher authority than this skill.
- Preserve one-writer, isolation, evidence, and actual authorization boundaries. Audit changes to these rules with realistic scenarios; do not add repeated approval demands for work already authorized.
- Do not include credentials, private prompts, customer data, generated binaries, or unrelated dependencies.

## Propose a change

1. Describe the concrete problem in a focused pull request; open an issue first only when design discussion would help.
2. Fork the repository and create a focused branch.
3. Make the smallest coherent change.
4. Validate the structure and behavior.
5. Open a pull request using the repository template.

## Validate locally

At minimum:

```bash
python3 scripts/validate.py
git diff --check
git status --short
```

The validator checks that:

- The frontmatter contains only `name` and `description`.
- The skill name is `orchestrate-with-sol-ultra`.
- Every relative link resolves.
- `agents/openai.yaml` has valid required metadata and explicitly mentions `$orchestrate-with-sol-ultra` in its default prompt.
- The delegation packet remains reachable directly from `SKILL.md`.

Review manually that UI metadata still summarizes the skill accurately and that documentation distinguishes host capability preferences from guarantees.

You may also invoke Codex’s built-in `$skill-creator` for authoring guidance and an independent review. Changes to delegation, model routing, safety, approvals, or integration rules should include a realistic forward test using [the behavioral scenarios](docs/BEHAVIORAL-CHECKS.md). Report the prompt, environment, models actually used, result, failures, and any fallback.

## Pull-request expectations

Explain:

- The problem being solved.
- The behavior before and after the change.
- Files changed and why.
- Checks run, including failures and skips.
- Effects on model fallback, permissions, concurrency, and shared-checkout safety.
- Any claim that still lacks benchmark evidence.

Keep discussions respectful and focused. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Licensing note

The repository does not yet have a legal license. Maintainers may defer contributions that require redistribution rights until RSB-HOLDING selects one. Do not assume that public visibility grants reuse permission.
