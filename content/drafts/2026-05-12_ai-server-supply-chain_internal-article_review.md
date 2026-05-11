---
workflow: content-production
artifact_type: internal-article-review
risk: low
created_at: 2026-05-12
target_draft: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
status: draft-review
---

# Review: AI server 資金從 GPU 外溢後，市場到底在買什麼？

## Verdict

Internal draft is usable as a first article-shaped artifact.

Do **not** publish yet.

## What Works

- Hook is concrete: readers understand the question immediately — GPU 以外，市場到底在買什麼？
- Structure is readable: Hook → Context → Thesis → Framework → Evidence → POV → Invalidation.
- The article keeps the key M1 insight: AI server is a system, not a GPU-only trade.
- AMD / Intel / MediaTek are separated into distinct roles instead of being blended into one generic AI thesis.
- It explicitly says MediaTek is ASIC / subsystem optionality, not server CPU main silicon.
- Public blockers are listed inside the draft.

## What Still Feels Weak

- Voice still feels agent-seeded. It is clear, but not yet uniquely `CrayonDing0909`.
- The article needs a sharper narrative example before public use: e.g. one concrete scenario of a reader misunderstanding CPU as "old chip" and then reframing it as "AI workflow control plane".
- It needs one stronger chart/table if moving toward public post: AI server spend map or company-role table.
- The current draft says "建立觀察清單" but does not include the actual watchlist table yet.

## Public Blockers

- AMD `>50% server CPU share target` still needs primary source.
- MediaTek `AI ASIC $2B Q4 2026` still needs official transcript / presentation.
- Scenario-analyzer has not been run.
- Data-quality-checker has not been run.
- CTA is missing.

## Suggested Next Pass

Before public publishing, run a voice pass:

1. Replace 2-3 generic transition sentences with the user's own phrasing.
2. Add one simple watchlist table:
   - AMD: server CPU growth / Data Center revenue
   - Intel: DCAI / Xeon design wins
   - MediaTek: official ASIC revenue target / customer confirmation
3. Decide article format:
   - long-form blog/newsletter, or
   - X/Threads multi-post thread.

## Decision

Keep as internal article draft.

Next likely milestone:

```text
M2.1 public-readiness hardening
```

or, if the user wants faster content practice:

```text
M3 controlled publish experiment
```

