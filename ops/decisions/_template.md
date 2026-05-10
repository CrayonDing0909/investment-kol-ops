---
artifact_type: gate-decision-log
gate_id: <IA1 | IA2 | MVP1 | MVP2 | AR1 | AD1 | PM1 | CP1 | CP2>
workflow: <investment-analysis | content-production | algorithm-research | audience-discovery | mvp-demo | postmortem | ship-workflow>
artifact_ref: <relative path to the artifact this decision applies to>
decision: <approve | edit | reject | defer>
created_at: YYYY-MM-DD
reviewer: <github handle, e.g. CrayonDing0909>
mode: <live | dry-run>
---

# Gate Decision: <gate id> — <one-line subject>

> 規則：
> - 一個 gate 一個 decision file。
> - File next to the artifact, not in a separate database.
> - Decision 必須是 approve / edit / reject / defer。
> - 高風險 gate（IA1 / IA2 / MVP1 / MVP2 / PM1）必填 reflection。

## Artifact Under Review

- Path: <e.g. research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md>
- Type: <analysis-brief | content-draft | mvp-spec | postmortem | swipe-tactic | pain-cluster>
- Risk: <low | medium | high>
- Status before gate: <draft | gate-pending>

## Decision

- Decision: <approve | edit | reject | defer>
- Reason (one sentence): <...>

## Edit Notes (only if decision = edit)

- <what to change>
- <where to re-enter the workflow (LLM stage, structured input, etc.)>

## Reject Notes (only if decision = reject)

- Reason category: <factual-error | weak-source | scope-too-broad | compliance-risk | other>
- Archive location: <where the rejected artifact is kept>

## Reflection (mandatory for IA1 / IA2 / MVP1 / MVP2 / PM1)

> 規則：把學習收進來。M1 預設 3 題，可加可減。

1. **Weakest point if challenged publicly:** <...>
2. **Best skill / step in this run:** <...>
3. **What I most want to improve next time:** <...>

## Linked Files

- Source checklist: <path>
- Knowledge pages updated: <paths>
- Subsequent action: <next workflow / artifact>

## Status After Gate

- New artifact status: <gate-approved | gate-edited | gate-rejected>
- Next step owner: <self | agent | external>
