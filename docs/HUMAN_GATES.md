# Human Gates

Purpose: define where the human must approve before the agent proceeds. Gates are
designed to catch the moments where the agent does not know it is wrong, not to
slow down every step.

Aligned with [docs/AGENTIC_HARNESS.md](AGENTIC_HARNESS.md),
[docs/WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md), and
[ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md).

## Gate Design Principles

- Gates protect against irreversible or hard-to-reverse actions.
- Gates protect against actions where reputational, financial, or compliance harm
  is possible.
- Gates do not exist to verify low-stakes formatting or vibe.
- Each gate must have: trigger, artifact shown to the human, decision options,
  and post-decision behavior.

## Risk Levels

The risk classifier in the harness tags each output:

| Level | Examples | Default Behavior |
|-------|----------|------------------|
| Low | Internal swipe entries, draft hooks, draft pain clusters, internal notes. | Auto-save artifact. |
| Medium | Public posts on general topics, repurposed content, demo screenshots. | Run pre-publish checklist. Optional human read. |
| High | Investment claims, backtest claims, position-related content, MVP launches, public corrections, paid offers. | Mandatory human gate. |

A workflow may upgrade risk level based on context. For example, a "general"
content draft becomes high risk if it includes a specific buy/sell suggestion.

## Two-Tier Publish Gate: A vs B

Not every public artifact needs the heavy investment-view review. Route by what
the artifact claims, per the artifact tiers in
[docs/ARTIFACT_SYSTEM.md](ARTIFACT_SYSTEM.md).

- **Gate A - Artifact Publish (lightweight, default).** For educational and
  visual artifacts: supply-chain maps, company cards, ETF X-rays, explainers,
  glossary visuals. Most L1/L2 artifacts.
- **Gate B - Investment View (heavy).** For directional or position content:
  market direction calls, single-stock buy/sell judgment, bull/base/bear,
  winner/loser, backtest/strategy results. The existing **IA1** and **IA2** gates
  are the Gate B family.

Router:

```text
Does the artifact make a direction / position / buy-sell / backtest claim?
  No  -> Gate A (publishable once checklist passes)
  Yes -> Gate B (IA1, plus IA2 if strategy/backtest)
```

If unsure, default up to Gate B. An educational artifact that quietly implies a
trade has become a Gate B artifact.

### Gate A - Artifact Publish

Trigger: any public educational/visual artifact that does NOT make a direction,
position, buy/sell, target-price, or backtest claim.

Show to human:

- The artifact (chart/map/card/script) and its public versions.
- The source note: each key claim mapped to at least one source.
- The uncertainty label (what is not yet verified).

Gate A has **two** required checks. **Safe does not mean publishable** — both
must pass.

**Check 1 — Safety Check (all required):**

- [ ] At least one source is present and labeled.
- [ ] No buy/sell call.
- [ ] No price target.
- [ ] No personalized investment advice.
- [ ] Uncertainty is labeled.

**Check 2 — Owner Comprehension Check (all required):**

The owner (or a stand-in target reader) answers these after reading the artifact:

- [ ] 1. Do I know what this teaches within 5 seconds?
- [ ] 2. Can I say what I learned in one sentence?
- [ ] 3. Does the first screen have ≤3 unfamiliar terms? (explainer target: 0)
- [ ] 4. Is this a crafted piece, not a data dump?

**Hard rule:** if the owner says "I did not learn anything," Gate A **cannot
approve**. The artifact returns to **rebuild** (re-open its Episode Contract per
[docs/CONTENT_CONVERSION_PIPELINE.md](CONTENT_CONVERSION_PIPELINE.md)), not a
light edit. A public artifact must also have passed its Episode Contract before
reaching this gate; a knowledge map rendered straight to public form fails Gate A
by construction.

Decisions: approve (publish), edit, reject (rebuild).

Post-decision:

- Approved artifacts can publish without IA1.
- If review reveals a direction/position claim, escalate to Gate B (IA1) instead
  of approving under Gate A.
- Log the decision next to the artifact (or in `ops/decisions/`) like any gate.

## Mandatory Gates

The IA1, IA2, MVP1, MVP2, AR1, AD1, and PM1 gates below are mandatory. IA1 and
IA2 are the Gate B investment-view family referenced above.

These gates cannot be skipped. The agent must wait for the human even if the
content looks ready.

### Gate IA1 - Investment Claim Publish (Gate B)

Trigger: any public artifact that contains a market direction call, a regime
claim, a position implication, a backtest result, or a strategy result.

Show to human:

- The draft post or asset.
- The source checklist with each claim mapped to data.
- The invalidation list.
- The risk and compliance pre-publish checklist.

Decisions:

- Approve.
- Edit (return with notes).
- Reject (archive with reason).

Post-decision:

- Approved drafts move to scheduled.
- Edited drafts re-enter the workflow at the LLM stage, not the start.
- Rejected drafts are kept in `content/drafts/` with the rejection note.

### Gate IA2 - Strategy or Backtest Public Claim

Trigger: any public artifact discussing a strategy, backtest, or quantitative
result, including educational explainers.

Show to human:

- All quality-gate items: lookahead bias, sample size, fees, slippage, OOS or
  walk-forward, drawdown, turnover, exposure, failure conditions.
- Caveat language used in the draft.

Decisions: approve, edit, reject.

Post-decision: same as IA1, plus a note in `ops/METRICS.md` for trust tracking.

### Gate MVP1 - MVP Scope and Safety

Trigger: any new MVP spec, or any change that adds account integrations, payments,
or persistent storage of user data.

Show to human:

- MVP spec.
- Data sources, including any with credentials.
- Trust and safety concerns.
- Build scope and explicit non-goals.
- Kill criterion.

Decisions:

- Approve to build.
- Edit scope.
- Reject (archive idea).

Post-decision:

- Approved spec is moved to `mvp/` with a build milestone list.
- Approved spec triggers a companion launch-post brief for content production.

### Gate MVP2 - Demo Launch

Trigger: any public launch of a demo, including soft launches.

Show to human:

- Demo URL or screenshot.
- Launch post draft.
- Feedback capture mechanism.
- Risk and compliance check on the demo's output.

Decisions: approve, edit, delay.

### Gate AR1 - Adopting a Tactic from Algorithm Research

Trigger: when an algorithm-research workflow recommends adopting a hook, format,
or framing observed from a competitor.

Show to human:

- The candidate post.
- Suggested adaptation.
- The "do not adopt" reason if any.
- Conflict check against `RISK_AND_COMPLIANCE.md`.

Decisions: approve, modify, reject.

### Gate AD1 - Picking the Next MVP Pain

Trigger: when audience-discovery workflow proposes which pain to build for next.

Show to human:

- Pain cluster summary.
- Ranked MVP candidate list.
- Sensitive data flags.
- Existing workaround the user already pays for.

Decisions: approve, defer, reject.

### Gate PM1 - Public Postmortem

Trigger: any public postmortem of a wrong call or failed experiment.

Show to human:

- Original artifact and date.
- Reconstructed assumption, observation, decision.
- Lesson and proposed playbook update.

Decisions: approve, edit, keep internal.

## Optional Gates

These gates are skippable but recommended. The agent may auto-proceed if you have
not configured them as mandatory in a given sprint.

### Gate CP1 - Weekly Content Calendar

Optional human review of the weekly calendar before drafts begin. Worth using
during high-output sprints.

### Gate CP2 - Repurpose Approval

Optional human review when one source artifact is being split into multiple
formats, to prevent over-saturation of one idea.

## Decision Records

Every human gate decision should be logged with:

- Date.
- Workflow.
- Artifact reference.
- Decision.
- Reason in one sentence.

Logs live next to the artifact they decided on, not in a separate database.

## When the Agent Is Unsure

If the agent cannot decide whether a gate applies, default to the gate. Cost of
asking is small. Cost of a wrong public investment claim is large.

If the user explicitly waives a gate for a low-risk task, the agent must record
the waiver next to the artifact, not in chat only.
