# Context Strategy

Purpose: control what the LLM sees at each step. The goal is the smallest context
that can complete the task, not the largest. This file defines named context packs
and the rules for using them.

Aligned with [docs/AGENTIC_HARNESS.md](AGENTIC_HARNESS.md) and
[docs/WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md).

## Why This Matters

- Larger context dilutes the strongest signal.
- Repo-wide context invites the agent to drift between work modes (analysis,
  content, MVP) and lose precision.
- Loading unrelated playbooks invites overconfident, off-mission output.
- Token cost scales with input. Most "smart" answers come from better routing,
  not bigger prompts.

## Rules

- Pick the workflow first, then the context pack. Never the other way around.
- Each pack lists required docs and optional docs. Load required first; only add
  optional docs if the agent asks for them.
- Do not paste full files when a section is enough. Reference the file path and
  let the agent read on demand.
- Never load multiple workflow packs at once. Compose by sequencing, not stacking.
- Strip raw, large, or noisy data before injection. Pass structured summaries.
- Keep secrets, brokerage data, and PII out of every pack.

## Context Packs

### algorithm-research-pack

Use for the algorithm-research workflow.

Required:

- [research/ALGORITHM_RESEARCH.md](../research/ALGORITHM_RESEARCH.md).
- [docs/CONTENT_STRATEGY.md](CONTENT_STRATEGY.md), positioning and pillars only.
- The structured swipe entries collected for this task.

Optional:

- [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md), if the candidate
  posts touch high-risk topics.

Do not load:

- Investment analysis playbook.
- MVP lab.
- Audience discovery raw notes.

### audience-discovery-pack

Use for the audience-discovery workflow.

Required:

- [research/AUDIENCE_DISCOVERY.md](../research/AUDIENCE_DISCOVERY.md).
- The structured interview/observation entries for this task.
- Existing pain clusters, if any.

Optional:

- [mvp/MVP_LAB.md](../mvp/MVP_LAB.md), only when proposing MVP candidates.
- [docs/CONTENT_STRATEGY.md](CONTENT_STRATEGY.md), only when proposing content angles.

Do not load:

- Algorithm swipe file.
- Investment analysis playbook.

### investment-analysis-pack

Use for the investment-analysis workflow.

Required:

- [research/INVESTMENT_ANALYSIS_PLAYBOOK.md](../research/INVESTMENT_ANALYSIS_PLAYBOOK.md).
- [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md).
- Structured data inputs (macro, breadth, leadership, news, technicals, sentiment)
  with sources.

Optional:

- Output of trading skills (market-environment, macro-regime-detector,
  market-breadth-analyzer, etc.) summarized as structured findings.
- Prior week's analysis brief, only when comparing weeks.

Do not load:

- Content drafts.
- MVP specs.
- Algorithm research swipe file.

### content-sprint-pack

Use for the content-production workflow.

Required:

- [content/CONTENT_OPERATING_SYSTEM.md](../content/CONTENT_OPERATING_SYSTEM.md).
- [docs/CONTENT_STRATEGY.md](CONTENT_STRATEGY.md).
- The source artifact being repurposed (analysis brief, MVP spec, postmortem,
  pain cluster).
- Platform-specific format constraints if known.

Optional:

- [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md), required if the
  draft touches a high-risk topic.
- Recent metrics summary from [ops/METRICS.md](../ops/METRICS.md).

Do not load:

- Raw audience interview notes (use the cluster output instead).
- Full investment analysis playbook (the analysis brief is enough).

### mvp-discovery-pack

Use for the mvp-demo workflow.

Required:

- [mvp/MVP_LAB.md](../mvp/MVP_LAB.md).
- The selected pain cluster from audience discovery.
- One-line user, one-line promise, and proposed input/output.

Optional:

- [research/AUDIENCE_DISCOVERY.md](../research/AUDIENCE_DISCOVERY.md), only when
  re-checking the MVP selection filter.
- [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md), required when the
  demo touches financial advice, backtests, or position-related output.

Do not load:

- Algorithm research swipe file.
- Full content operating system.

### postmortem-pack

Use for the postmortem workflow.

Required:

- The original artifact (post, analysis, MVP spec).
- The original hypothesis and success metric.
- Observed metrics and outcome.

Optional:

- The relevant workflow pattern from
  [docs/WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md).
- The playbook the original artifact came from.

Do not load:

- Unrelated playbooks.
- Other ongoing experiments.

### git-pack

Use for the ship workflow. Keep it intentionally small.

Required:

- The "Branch and Commit Strategy" section from
  [docs/IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md).
- The Human Gate Rule and Verification sections from
  [AGENTS.md](../AGENTS.md).
- Live git status output: `git status --short`, `git diff --stat`, current
  branch, remote tracking state.

Optional:

- The Progress Log section of `IMPLEMENTATION_PLAN.md`, only when appending
  a new log line.

Do not load:

- Any workflow-specific playbook.
- Any artifact content (only file paths and diff stats are needed).
- Secrets, credentials, or anything from `.env*`.

## Structured Data Conventions

Always pass the LLM a structured object instead of raw notes when possible.

- Use markdown tables, YAML, or labeled bullet lists.
- Tag each item with: source, timestamp, confidence, workflow.
- Keep numeric fields numeric, not embedded in prose.
- Strip non-essential commentary before injection.

## Context Drift Checks

If any of these happen, the agent must stop and re-route:

- It starts pulling docs not listed in the active pack.
- It mixes investment analysis voice with MVP marketing voice.
- It references metrics that were not loaded.
- It produces output that does not match the workflow's expected artifact.

## Defaults When In Doubt

- One workflow at a time.
- One context pack at a time.
- One artifact at the end.
- If you must compose, finish artifact A before loading pack B.
