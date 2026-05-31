# Roadmap

Goal: build a repeatable investment KOL machine that can research, publish, learn,
and convert audience pain points into useful AI-assisted MVP products.

This file holds product/business milestones. Engineering milestones (templates,
scripts, commands, branch strategy) live in
[docs/IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md).

## Operating Model (artifact-first overlay)

Direction anchor: [docs/NORTH_STAR.md](NORTH_STAR.md). Core unit:
[docs/ARTIFACT_SYSTEM.md](ARTIFACT_SYSTEM.md).

The repo is now read artifact-first. The loop we optimize for is:

```text
Artifact -> Public content -> Audience signal -> Research deepening -> Product
```

Milestone vocabulary (read this to avoid confusion):

- **Artifact-track labels use the `A` prefix (A0.5, A1, A2, ...).** They describe
  the artifact-first re-prioritization in this overlay.
- **Engineering / dashboard milestones keep the `M` prefix (M0-M6).** Those are
  the existing milestones in this file below, in
  [docs/IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md), and in the generated
  `ops/current.md` / `ops/dashboard.html`. They remain valid and unchanged.

The `A` overlay re-orders priority; it does not renumber or replace the `M`
milestones.

The original milestones below (M0-M6) remain valid as the research-quality and
infrastructure layer. They are no longer the immediate next step on their own;
they serve the artifact loop. The deep source-backed research milestones
(IMPLEMENTATION_PLAN M1.1/M1.2-style work) are the research-quality layer and
must not block public artifact testing.

Artifact-first milestone order going forward:

```text
A0.5 Repo Refinement          (this overlay + operating layer)
A1   Artifact Engine MVP       (5 publishable artifacts)
A2   Research Packet Lite       (deepen only the artifacts that performed)
A3   Public Distribution Loop   (steady weekly publishing cadence)
A4   Landing Page + Private Traffic
A5   First Interactive Prototype
```

These reuse, not replace, the systems below: content production runs through
[content/CONTENT_OPERATING_SYSTEM.md](../content/CONTENT_OPERATING_SYSTEM.md) and
[content/templates/](../content/templates/); publishing uses the two-tier gate in
[docs/HUMAN_GATES.md](HUMAN_GATES.md) (Gate A for educational artifacts, Gate B
for investment views); metrics use
[ops/METRICS.md](../ops/METRICS.md) and the post-publish checklist in
`ops/decisions/`. Working backlog and milestone specs live in
[ops/backlog.md](../ops/backlog.md).

## A0.5 - Repo Refinement (artifact track)

Outcome: the repo reads as an artifact-led KOL operating system, not a
research-only workflow. Additive only; no existing system removed.

- Add the direction layer: [docs/NORTH_STAR.md](NORTH_STAR.md).
- Add the artifact model: [docs/ARTIFACT_SYSTEM.md](ARTIFACT_SYSTEM.md) with
  L1-L4 tiers.
- Add the daily/weekly operating layer: [NEXT_ACTIONS.md](../NEXT_ACTIONS.md)
  and `ops/weekly/`.
- Add public distribution templates: IG carousel, YouTube Shorts, lightweight
  artifact brief.
- Add the two-tier publish gate (Gate A vs Gate B) to
  [docs/HUMAN_GATES.md](HUMAN_GATES.md).
- Reframe AI Server Supply Chain as the first public artifact series.

Exit criteria:

- A newcomer can open the repo and know what the project is.
- `NEXT_ACTIONS.md` tells the user what to do today.
- Each artifact has a clear lifecycle and Definition of Done.
- A weekly review ritual exists.
- The research workflow stays available but no longer blocks public testing.

## Milestone 0 - Foundation and Agentic Harness

Outcome: the repo becomes the source of truth and runs on a defined harness.

- Define positioning: who the account helps and what it refuses to be.
- Create the content operating system and publishing cadence.
- Create investment analysis quality gates.
- Create basic metrics tracking.
- Decide primary platforms for the first 30 days.
- Stand up the agentic harness:
  [docs/AGENTIC_HARNESS.md](AGENTIC_HARNESS.md),
  [docs/WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md),
  [docs/CONTEXT_STRATEGY.md](CONTEXT_STRATEGY.md),
  [docs/HUMAN_GATES.md](HUMAN_GATES.md),
  [ops/AGENTIC_RUNBOOK.md](../ops/AGENTIC_RUNBOOK.md).
- Confirm `AGENTS.md` enforces workflow-first behavior.

Exit criteria:

- One clear account positioning statement.
- One weekly publishing workflow.
- One metrics sheet or markdown tracker.
- One analysis template that can be reused.
- One canonical workflow per area (algorithm-research, audience-discovery,
  investment-analysis, content-production, mvp-demo, postmortem) defined and
  routable from the runbook.

## Milestone 1 - Audience and Platform Research

Outcome: stop guessing what to post. Run all research through the harness.

- Run the algorithm-research workflow on X, Threads, YouTube Shorts, Instagram
  Reels, and long-form blog/newsletter with structured swipe entries.
- Collect 30 strong investment/AI creator examples through the same workflow.
- Identify hooks, formats, interaction patterns, and content angles using the LLM
  on structured data, never raw screenshots.
- Run the audience-discovery workflow for 10-20 people who do not use AI agents.
- Extract repeated pains: investing, research, news overload, portfolio review,
  automation anxiety, tool setup friction.
- Apply Gate AR1 before adopting any tactic and Gate AD1 before picking the next
  MVP pain.

Exit criteria:

- 20 content hypotheses with workflow tags.
- 5 audience pain clusters in structured form.
- 3 MVP demo candidates ready for the mvp-demo workflow.

## Milestone 2 - Content Sprint 1

Outcome: publish enough to learn from the market through the content-production
workflow.

- Pick one audience: retail investors who want better research but do not know how
  to use agents.
- Pick two formats: market analysis thread and AI workflow demo.
- Run investment-analysis → content-production for the analysis posts.
- Run content-production directly for the AI workflow demos.
- Publish 3-5 posts per week for 4 weeks.
- Apply Gate IA1 before any post that contains a market claim.
- Track hook, format, topic, CTA, impressions, engagement, saves, comments,
  follows, and clicks via [ops/METRICS.md](../ops/METRICS.md).
- Review weekly and double down on the best format.

Exit criteria:

- 12-20 published posts.
- 3 proven content patterns recorded as algorithm-research hypotheses.
- 1 clear audience segment worth serving, encoded in CONTENT_STRATEGY.

## Milestone 3 - MVP Demo Lab

Outcome: turn attention into a useful product loop using the mvp-demo workflow.

- Run the mvp-demo workflow on the chosen pain.
- Each demo must define data input, programmatic checks, LLM judgment, and human
  review.
- Build one fast demo website for the strongest pain point.
- Keep it narrow: one user, one workflow, one result.
- Examples:
  - Market regime explainer from simple inputs.
  - AI-assisted earnings/news digest.
  - Portfolio risk checklist.
  - Beginner-friendly "ask an investing agent" guided form.
  - Backtest sanity checker for non-quants.
- Add waitlist or feedback capture.
- Apply Gate MVP1 before building, MVP2 before launching, IA1 if the launch post
  carries any investment claim.
- Run content-production for the launch post immediately after MVP1.

Exit criteria:

- One working demo.
- One feedback form.
- 20+ users or conversations.
- Decision: improve, pivot, or archive, recorded as a kill-criterion check.

## Milestone 4 - Analysis Credibility System

Outcome: make the account trustworthy by hardening the investment-analysis and
postmortem workflows.

- Tighten the investment-analysis workflow: every public claim mapped to a source.
- Add source tracking for charts, data, and claims.
- Create disclosure rules for holdings, watchlists, and uncertainty.
- Build a "what would change my mind" section into analysis posts as a workflow
  artifact requirement.
- Run the postmortem workflow on wrong calls and missed scenarios; apply Gate PM1
  before any public postmortem.

Exit criteria:

- Market weekly template.
- Theme deep dive template.
- Trade/idea postmortem template.
- Public disclaimer and source policy.
- Strategy/backtest content always passes Gate IA2 before publishing.

## Milestone 5 - Content Production Pipeline

Outcome: reduce friction from idea to publish by tightening the
content-production workflow.

- Build a weekly planning workflow that uses the content-sprint-pack and the
  weekly rhythm in `CONTENT_OPERATING_SYSTEM.md`.
- Create templates for articles, threads, carousels, short videos, thumbnails,
  and demo launch posts.
- Create asset checklist for charts, screenshots, visuals, and captions.
- Encode the review checklist (accuracy, clarity, compliance, CTA, formatting)
  inside the workflow's LLM step.
- Batch content production by theme.
- Decide which gates are mandatory vs optional this sprint and record the
  configuration.

Exit criteria:

- 2-week content calendar.
- Repeatable publish checklist as part of the workflow.
- Asset folder convention.
- Weekly review ritual that updates `ops/METRICS.md`.

## Milestone 6 - Product and Community Flywheel

Outcome: connect content, demos, and community while keeping every public
artifact behind the right gate.

- Build email/waitlist capture (governed by audience-discovery and mvp-demo
  workflows).
- Create one free lead magnet: market checklist, prompt pack, or mini tool.
- Invite users into a structured feedback loop, logged via audience-discovery.
- Turn repeated questions into content and product improvements via the
  postmortem and content-production workflows.
- Explore paid product only after repeated demand appears, and only after a
  dedicated workflow + gate is added to this repo.

Exit criteria:

- 100 email/waitlist subscribers or clear niche signal.
- 3 product requests that repeat.
- One improved demo based on user feedback.
- A defined paid-product workflow before any monetization step.

## First 7 Days

1. Finish repo docs and rules, including the agentic harness layer.
2. Pick primary platform and target audience.
3. Create 10 content hypotheses through the algorithm-research workflow.
4. Publish first 3 posts through the content-production workflow.
5. Start algorithm swipe file with structured entries.
6. Interview 3 people who do not use AI agents through the audience-discovery
   workflow.
7. Select one MVP demo candidate via Gate AD1.
