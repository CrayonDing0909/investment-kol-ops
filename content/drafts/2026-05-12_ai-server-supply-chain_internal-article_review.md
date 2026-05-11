---
workflow: content-production
artifact_type: internal-article-review
risk: low
created_at: 2026-05-12
target_draft: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
status: voice-pass-review
---

# Review: AI server 資金從 GPU 外溢後，市場到底在買什麼？

## Verdict

Internal draft is now usable as a stronger internal article-shaped artifact after
the voice pass.

Do **not** publish yet.

## What Works

- Hook now starts from a real reader confusion: GPU 之外的 AI server 輪動是不是只是資金亂找東西？
- Structure is readable: Hook → Context → Thesis → Framework → Evidence → POV → Invalidation.
- The article keeps the key M1 insight: AI server is a system, not a GPU-only trade.
- AMD / Intel / MediaTek are separated into distinct roles instead of being blended into one generic AI thesis.
- It explicitly says MediaTek is ASIC / subsystem optionality, not server CPU main silicon.
- The article now includes a small watchlist table instead of saying "建立觀察清單" without showing it.
- Software has been removed from the main investable supply-chain line for this draft.
- Public blockers are listed inside the draft.

## Voice Pass Changes

- Replaced broad market claims like "過去一年 AI 交易幾乎等於 GPU" with a more cautious research question.
- Reframed CPU from "system orchestration" jargon into a plainer "系統調度 / 調度器" explanation.
- Kept first-person judgment language: "我目前會把...", "我會先...", "我暫時不會..."
- Clarified that AMD is the cleanest source-backed line, Intel is a repair/verification line, and MediaTek is optionality.
- Added `docs/VOICE_PROFILE.md` and `docs/VOICE_PROFILE.zh.md` so future drafts have reusable voice constraints.

## What Still Feels Weak

- The draft is more natural, but the final public voice still needs the user's personal touch before publishing.
- It needs one stronger chart or visual if moving toward public post: AI server spend map or company-role table.
- The article still needs source-hardening before public use; the voice pass did not add new primary sources.
- CTA is still intentionally undefined because this remains an internal draft.

## Public Blockers

- AMD `>50% server CPU share target` still needs primary source.
- MediaTek `AI ASIC $2B Q4 2026` still needs official transcript / presentation.
- Scenario-analyzer has not been run.
- Data-quality-checker has not been run.
- CTA is missing.

## Suggested Next Pass

Before public publishing:

1. User should do a personal read-through and replace any sentence that does not
   sound like their own words.
2. Run source hardening on AMD / MediaTek claims.
3. Decide article format:
   - long-form blog/newsletter, or
   - X/Threads multi-post thread.
4. Define CTA only after choosing the public format.

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

