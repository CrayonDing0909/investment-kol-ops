---
workflow: content-production
artifact_type: internal-article-review
risk: low
created_at: 2026-05-12
target_draft: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
status: raw-voice-review
---

# Review: 最近整理 AI server 相關族群，先拆出的幾條支線

## Verdict

Internal draft is now closer to a raw research voice note.

Do **not** publish yet.

## What Works

- Opening now starts from the user's actual research state: "最近整理 AI server 相關族群..."
- The draft no longer claims that all AI server names belong to one clean "GPU spillover" story.
- CPU / ASIC / HBM / cooling / passive components are split into separate hypothesis branches.
- The draft clearly says the branch map is not fully verified yet.
- The article keeps the key M1 insight: AI server is a system, not a GPU-only trade.
- AMD / Intel / MediaTek are still separated into distinct roles instead of being blended into one generic AI thesis.
- It explicitly says MediaTek is ASIC / subsystem optionality, not server CPU main silicon.
- HBM / cooling / passive components are now marked as under-verified, not treated as source-backed conclusions.
- Data-quality-checker has run with 0 findings: `reports/data_quality_2026-05-12_025848.md`.
- Public blockers are listed inside the draft.

## Raw Voice Changes

- Updated `docs/VOICE_PROFILE.md` and `docs/VOICE_PROFILE.zh.md` to prioritize raw voice before polished article structure.
- Removed the earlier "資金在找還沒漲的東西" framing because it did not match the user's actual view.
- Replaced the teaching-style Hook / Thesis / Framework structure with a research-note sequence:
  current thought → branch map → source-backed CPU line → under-verified branches → next verification.
- Preserved uncertainty phrases such as "感覺", "我想像中", "還沒有補完", and "不能寫太滿".

## What Still Feels Weak

- The draft is intentionally less polished; it still needs a later clarity pass if moving toward public writing.
- It needs one stronger chart or visual if moving toward public post: AI server spend map or company-role table.
- The article still needs source-hardening before public use; this pass did not add new primary sources.
- CTA is still intentionally undefined because this remains an internal draft.
- Some phrasing may still be too organized; the user should read the first 2-3 sections and mark anything that still feels unlike their voice.

## Public Blockers

- AMD `>50% server CPU revenue market share` now has AMD Financial Analyst Day primary source, but public wording must frame it as a forward-looking target.
- MediaTek `AI ASIC $2B Q4 2026` now has official transcript support, but public wording must frame it as management expectation, not realized revenue.
- CPU latency claim now has Georgia Tech / Intel original paper support, but public wording must be workload-specific.
- HBM / cooling / passive component branches still need source-backed research.
- Scenario-analyzer has not been run.
- CTA is missing.

## Suggested Next Pass

Before public publishing:

1. User should read the raw opening and mark sentences that still feel AI-like.
2. Build separate source packets for HBM / cooling / passive components before treating them as a confirmed branch.
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

