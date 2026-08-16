# Benchmarking

This repository does not currently publish benchmark results. Use this protocol before making quantitative claims about speed, quality, token usage, cost, or reliability.

## What to compare

Compare at least two conditions:

1. A single-agent baseline using the normal team configuration.
2. The same task using `$orchestrate-with-sol-ultra`.

Keep the starting repository revision, task prompt, success criteria, tools, permissions, provider state, and hardware as consistent as possible.

## Choose representative tasks

Use real tasks from the intended workload, not toy prompts. Include:

- Tasks with no safe independent lane.
- Tasks with one read-only evidence lane.
- Tasks with two or more genuinely independent lanes.
- At least one high-risk integration or review task.
- Tasks where the expected result can be checked objectively.

Record why each task is considered sequential or parallelizable before running it.

## Run the evaluation

1. Freeze the exact starting commit and environment description.
2. Define acceptance checks before either condition begins.
3. Run each condition multiple times; three repetitions are a pragmatic smoke-test floor, not a statistically conclusive sample.
4. Randomize condition order when practical.
5. Keep failed, interrupted, and approval-blocked runs in the results.
6. Review the final artifacts without knowing which condition produced them when feasible.

## Measure

Capture at least:

- Task success against the predefined acceptance checks.
- Required evidence completeness.
- Wall-clock time.
- Total input, cached, reasoning, and output tokens when available.
- Usage by model tier when available.
- Estimated or billed cost when available.
- Tool calls, retries, and failed commands.
- Human corrections and review time.
- Integration conflicts or overwritten work.
- Safety-boundary violations or unapproved action attempts.
- Tests passed, failed, skipped, and not run.

## Report honestly

- Publish the task set, prompts, starting commits, environment, raw results, and exclusions when confidentiality permits.
- Report medians and ranges, not only the best run.
- Separate the time spent in parallel lanes from end-to-end task time.
- Separate reduced use of an expensive tier from reduced total token usage.
- Treat lower latency or cost as an improvement only when the final result still meets the same quality and evidence bar.
- Do not generalize results beyond tasks resembling the evaluation set.

## Claims policy

Until reproducible results exist, use language such as “may reduce wall-clock time on cleanly divisible tasks” and “may shift bounded work to more efficient model tiers.” Do not claim a guaranteed multiplier, percentage improvement, token reduction, cost reduction, or quality gain.
