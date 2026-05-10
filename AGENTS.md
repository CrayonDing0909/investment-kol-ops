# Agent Instructions

## Mission

Help build an investment KOL operating system for `CrayonDing0909`: audience
research, investment analysis, content production, AI-agent MVP demos, and
publishing operations.

## Operating Model

This repo runs on the agentic harness defined in
[docs/AGENTIC_HARNESS.md](docs/AGENTIC_HARNESS.md). Every meaningful task must
follow it.

Default behavior:

1. Identify intent and pick a workflow from
   [docs/WORKFLOW_PATTERNS.md](docs/WORKFLOW_PATTERNS.md).
2. Collect structured data first. Do not feed raw notes to the LLM.
3. Load only the matching context pack from
   [docs/CONTEXT_STRATEGY.md](docs/CONTEXT_STRATEGY.md).
4. Use the LLM for synthesis, drafting, classification, and review against
   checklists. Do not use it for counting, sorting, filtering, storing state, or
   pretending to run tools.
5. Apply the risk classifier and respect any mandatory human gate from
   [docs/HUMAN_GATES.md](docs/HUMAN_GATES.md).
6. Produce a tangible artifact and save it where the runbook says.
7. Update metrics so the next routing decision is better.

If a task does not map to a workflow, do not improvise. Ask the human or define a
new workflow first.

## Default Priorities

- Quality and learning over speed for personal strategy and investment analysis.
- Speed over polish for MVP demos, but never skip the learning loop.
- Keep outputs practical: every research item should become a content idea,
  product idea, checklist, script, or experiment.
- Do not mix this repo with work projects or work-specific rules.

## Programmatic-First Rule

Anything that can be solved with code, scripts, or deterministic checks must be
done that way before the LLM is involved.

- Validate tickers, units, dates, and day-of-week consistency.
- Aggregate metrics, sort posts, count repeats, and filter clusters before
  summarization.
- Convert raw notes into structured data with: source, timestamp, confidence,
  workflow tag.

## Context Injection Rule

- Pick the workflow first, then load exactly one context pack.
- Do not paste full files when a section is enough.
- Do not load multiple workflow packs at once. Compose by sequencing.
- Strip noisy data before injection. Pass structured summaries.
- Stop and re-route if the agent starts pulling docs not listed in the active
  pack.

## Human Gate Rule

- Never publish or launch high-risk artifacts without a human gate.
- High-risk includes: investment claims, position-related content, backtest
  claims, MVP launches, public corrections, paid offers.
- If unsure whether a gate applies, default to the gate.
- Record every gate decision next to the artifact, not only in chat.

## Investment Analysis Rules

- Use a repeatable process: macro regime, breadth, market leadership,
  sector/theme rotation, news catalysts, technical structure, risk zones, and
  scenario planning.
- Separate observation, interpretation, and action.
- Flag uncertainty and invalidation conditions.
- Never present investment content as guaranteed advice.
- Include fees, liquidity, drawdown, overfitting, and data quality concerns when
  discussing strategies or backtests.

## Content Rules

- Treat every post as an experiment with a hypothesis.
- Always define: target audience, hook, platform, format, CTA, and success
  metric.
- Prefer clear, useful content over vague market commentary.
- Record learnings after publishing.

## HTML Reading UI Rule

- Human-facing knowledge artifacts are HTML-first. Follow
  [docs/HTML_READING_UI_GUIDE.md](docs/HTML_READING_UI_GUIDE.md).
- If the user is expected to read, learn, review, or revisit an artifact, create
  or update an HTML reading page.
- Markdown remains the canonical source / metadata layer and must be labeled as
  fallback (`md source`, `markdown intake`, `markdown canonical`) inside HTML.
- Do not send the user directly from an HTML page into raw Markdown unless it is
  explicitly labeled as fallback.


## MVP Rules

- For non-AI-agent users, start with pain, not technology.
- Build demos that solve one concrete workflow in under 5 minutes.
- Prefer simple web demos, checklists, calculators, and guided workflows before
  large products.
- Treat the demo as a structured workflow: data input, programmatic checks, LLM
  judgment, human review.

## Adaptive Flow Rule

- Workflows are templates, not scripts. The agent may skip, branch, or escalate
  steps based on current evidence and risk.
- If a workflow needs to change mid-task, declare the new chain explicitly and
  update the artifact.

## Ship Workflow Rule

- At the end of any task that produced file changes, run the ship-workflow
  defined in [docs/WORKFLOW_PATTERNS.md](docs/WORKFLOW_PATTERNS.md).
- Never run `git commit`, `git push`, or `git checkout -b` without the user's
  explicit approval. This rule is absolute, even for low-risk doc changes.
- For pushes to `main`, require an extra confirmation.
- Branch and commit decisions follow the strategy in
  [docs/IMPLEMENTATION_PLAN.md](docs/IMPLEMENTATION_PLAN.md).
- After a successful commit, append one line to the Progress Log in
  `IMPLEMENTATION_PLAN.md`.

## Verification

- Before finalizing meaningful changes, run a ship check: changed files, open
  risks, tests or manual checks, and next step.
- Do not claim commands, tests, research, or publishing happened unless they
  actually did.

## Anti-Patterns

- Calling the LLM with the entire repo pasted in.
- Relying on the LLM to remember state across turns.
- Using prompts to enforce rules that should be code or checklists.
- Putting human approval at every step (decision fatigue) or none (unsafe
  output).
- Treating workflows as fixed scripts instead of adaptive templates.
