# Agentic Runbook

Purpose: a daily operations manual. When you want to do something, this file tells
you which workflow to start, which context pack to load, and which gates apply.

Aligned with [docs/AGENTIC_HARNESS.md](../docs/AGENTIC_HARNESS.md),
[docs/WORKFLOW_PATTERNS.md](../docs/WORKFLOW_PATTERNS.md),
[docs/CONTEXT_STRATEGY.md](../docs/CONTEXT_STRATEGY.md), and
[docs/HUMAN_GATES.md](../docs/HUMAN_GATES.md).

## How to Use

1. Find your task in the table below.
2. Run the listed workflow.
3. Load only the listed context pack.
4. Respect the listed gates.
5. Save the artifact in the listed location.

## Quick Map

| Intent | Workflow | Context Pack | Mandatory Gates | Artifact Location |
|--------|----------|--------------|-----------------|-------------------|
| "Do this week's market analysis" | investment-analysis | investment-analysis-pack | IA1 (and IA2 if strategy/backtest) | analysis brief + draft in `content/drafts/` |
| "Analyze this news event" | investment-analysis | investment-analysis-pack | IA1 | analysis brief in research notes |
| "Review this strategy or backtest" | investment-analysis | investment-analysis-pack | IA2 | review note next to backtest |
| "Plan this week's content" | content-production | content-sprint-pack | CP1 (optional) | calendar entries in `content/` |
| "Draft a post about X" | content-production | content-sprint-pack | IA1 if investment claim, otherwise none | draft in `content/drafts/` |
| "Repurpose this analysis into a thread / short / carousel" | content-production | content-sprint-pack | IA1 if investment claim | drafts in `content/drafts/` |
| "Study competitor / platform posts" | algorithm-research | algorithm-research-pack | AR1 before adopting | swipe entries + hypotheses |
| "Why did this post blow up" | algorithm-research | algorithm-research-pack | AR1 before adopting tactic | swipe entry |
| "Log a new interview" | audience-discovery | audience-discovery-pack | none for raw log | structured interview entry |
| "Cluster current pains" | audience-discovery | audience-discovery-pack | AD1 to pick the next MVP | pain cluster doc |
| "Spec a new MVP" | mvp-demo | mvp-discovery-pack | MVP1 | MVP spec in `mvp/` |
| "Launch a demo" | mvp-demo + content-production | mvp-discovery-pack then content-sprint-pack | MVP2 | demo + launch post |
| "Decide whether to keep / improve / kill demo" | mvp-demo | mvp-discovery-pack | MVP1 if scope changes | decision note |
| "Postmortem a wrong call or failed experiment" | postmortem | postmortem-pack | PM1 if public | postmortem note next to artifact |
| "Ship / commit / wrap up this task" | ship-workflow | git-pack | always user-approve, extra confirmation for `main` push | git history + Progress Log line in `IMPLEMENTATION_PLAN.md` |

## Common Sequences

### Weekly Publish Run

1. investment-analysis: produce the analysis brief.
2. content-production: turn the brief into a thread, blog, and short variant.
3. Gate IA1 before publishing.
4. Save metrics after publishing in `ops/METRICS.md`.

### Demo Launch

1. audience-discovery: confirm the chosen pain.
2. mvp-demo: spec, build a thin version.
3. Gate MVP1.
4. content-production: write the launch post.
5. Gate MVP2 and IA1 if the post implies investment outcomes.

### Competitor Sweep

1. algorithm-research: collect 5-10 strong posts.
2. Gate AR1 to pick which patterns to adapt.
3. content-production: queue 2-3 experiments.

### Wrong Call Recovery

1. postmortem on the bad call.
2. Update the relevant playbook if the lesson is structural.
3. content-production: optional public postmortem.
4. Gate PM1 before publishing.
5. ship-workflow to commit and log progress.

### End of Any Task

1. ship-workflow runs.
2. Agent classifies changes and proposes branch / commit / push plan.
3. User approves, edits, or rejects.
4. Agent executes only the approved git commands.
5. One Progress Log line appended in
   [docs/IMPLEMENTATION_PLAN.md](../docs/IMPLEMENTATION_PLAN.md).

## Daily Routine

- Morning: scan inbox/replies for any audience-discovery hits, log structured
  entries.
- Mid-day: run the workflow for the day's primary task (analysis, content, MVP).
- Evening: post-publish review for any artifact published today.

## Weekly Routine

- Monday: investment-analysis + content-production (plan).
- Tuesday-Thursday: content-production (publish), audience-discovery (log).
- Friday: deeper analysis or demo launch, plus algorithm-research review.
- Weekend: batch tasks, MVP iteration, postmortems if needed.

## When Something Does Not Fit

- If a request does not map to a workflow, do not improvise. Ask the human, or
  define a new workflow in
  [docs/WORKFLOW_PATTERNS.md](../docs/WORKFLOW_PATTERNS.md) before running it.
- If a workflow needs a new context pack, define it in
  [docs/CONTEXT_STRATEGY.md](../docs/CONTEXT_STRATEGY.md) first.
- If a workflow needs a new human gate, define it in
  [docs/HUMAN_GATES.md](../docs/HUMAN_GATES.md) first.

## Anti-Patterns

- Loading multiple context packs to "be safe."
- Skipping a mandatory gate because the draft "looks fine."
- Treating the runbook as a script. It is a routing map, not a recipe.
- Adding new gates without retiring old ones; gate fatigue is real.
