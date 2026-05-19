---
artifact_type: readiness-audit
workflow: thesis-card
related_artifact: content/cards/2026-05-13_ai-server_fundamentals-mediatek-2b_002.md
related_decision: ops/decisions/2026-05-13_workflow-rule-audit-card-001.md
created_at: 2026-05-19
reviewer: agent
trigger: "Validate new content-thesis-card / content-card-voice rules and card-source-readiness skill against Card #002 before drafting."
---

# Card #002 Readiness Dry-Run

> Purpose: run the new
> [card-source-readiness](../../.cursor/skills/card-source-readiness/SKILL.md)
> skill against Card #002 without drafting the card. The output validates the
> new workflow and tells the user what to produce next.

## Card Frontmatter (resolved)

| Field | Value |
|---|---|
| Path | [content/cards/2026-05-13_ai-server_fundamentals-mediatek-2b_002.md](../../content/cards/2026-05-13_ai-server_fundamentals-mediatek-2b_002.md) |
| lens | 基本面 |
| counter_direction | bear-falsify |
| backbone_ref | [content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md](../../content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md) |
| backbone_section | "第二條 / MediaTek 在 ASIC 故事裡的位置（4 個具體風險）" |
| sources | 3 entries (see below) |
| risk | high |
| public_status | outline |

## Audit Steps

### Step 1 — Resolve Card

OK. Frontmatter complete. `lens`, `counter_direction`, `backbone_ref`,
`backbone_section`, `sources`, `risk`, `public_status` all populated.

### Step 2 — Backbone Reference

OK. Backbone file exists and section anchor `## 第二條：ASIC / MediaTek 這條
的風險我想拆清楚` plus subsection `### MediaTek 在 ASIC 故事裡的位置（4 個
具體風險）` are present in lines 112-156 of the backbone document. The card's
`backbone_section` value points at the subsection — exact match.

### Step 3 — Source Labels

Mixed.

| Source | Label | Status |
|---|---|---|
| MediaTek Q1 2026 earnings call transcript | `reported-fact for $2B framing` | OK |
| MediaTek Analyst Day 2025 | `forward-looking-target` | OK |
| Stock price + valuation 歷史（自行驗算） | _no claim-type label_ | MISSING |

Action: relabel source #3 as `agent-inference` (since the card derives the
price-in claim from self-computed valuation) or split it into two entries
(`stock-price-source` + `agent-inference for z-score derivation`). The Pre-
publish TODO already flags both numbers for fact-check, which reinforces the
label requirement.

### Step 4 — Domain Primer (Conditional)

OK. Theme primer already exists from the Card #001 cycle:

- Markdown canonical:
  [research/notes/2026-05-13_ai-server-components-primer.md](../../research/notes/2026-05-13_ai-server-components-primer.md)
- Paired HTML:
  [research/knowledge/ai-server-supply-chain/primers/ai-server-components.html](../../research/knowledge/ai-server-supply-chain/primers/ai-server-components.html)

The primer covers the ASIC concept at the level the user already absorbed
during Card #001. No new primer is required for Card #002 because the topic
stays inside the same theme.

### Step 5 — Source Tutor Coverage

NOT READY. Source count = 3 → **cross-source-synthesis mode required** per
[.cursor/rules/source-tutor-reading.mdc](../../.cursor/rules/source-tutor-reading.mdc).

Existing artifacts:

| Artifact | Path | Status |
|---|---|---|
| Source packet (MediaTek Q1 2026 earnings) | [research/sources/ai-server-supply-chain/earnings/2026-05-10_mediatek-q1-2026-source-packet.md](../../research/sources/ai-server-supply-chain/earnings/2026-05-10_mediatek-q1-2026-source-packet.md) | OK |
| Source reading HTML | [research/knowledge/ai-server-supply-chain/sources/mediatek-q1-2026.html](../../research/knowledge/ai-server-supply-chain/sources/mediatek-q1-2026.html) | OK |
| Intake HTML | [research/knowledge/ai-server-supply-chain/intakes/mediatek-q1-2026.html](../../research/knowledge/ai-server-supply-chain/intakes/mediatek-q1-2026.html) | OK |
| Cross-source tutor note | `research/source-tutor/ai-server-supply-chain/2026-05-19_mediatek-asic-cross-source_reading.md` (expected path) | MISSING |
| Paired HTML reading view | `research/knowledge/ai-server-supply-chain/readings/mediatek-asic-cross-source.html` (expected path) | MISSING |
| MediaTek Analyst Day 2025 source packet | (expected under `research/sources/ai-server-supply-chain/analyst-day/`) | MISSING |

The Analyst Day 2025 cite is not yet packetized, so source-collector step
must run before cross-source tutor.

### Step 6 — IA1 Gate

NOT READY. `risk: high`, but no `ops/decisions/*` file references Card #002
or MediaTek. IA1 gate must be opened **after** the cross-source tutor is in
place, not before.

### Step 7 — Pre-Ready Structural Checks

Snapshot of card body issues to address before `public_status: ready`:

- `## Draft Post` block is absent. The card currently only carries the
  internal structured sections. Per
  [.cursor/rules/content-thesis-card.mdc](../../.cursor/rules/content-thesis-card.mdc)
  and the
  [thesis-card-writing](../../.cursor/skills/thesis-card-writing/SKILL.md)
  skill, the shipping artifact is the `## Draft Post` block in 起承轉合 voice.
- Card contains `**TODO**` markers for stock-price and P/E z-score numbers.
- Position disclosure wording marked TODO.
- 4-risks structure is two-mechanism-adjacent (track record + subsystem
  confusion + expectation reset + price-in). This is acceptable for a
  risk-themed card as long as all four risks compose into one mechanism
  ("priced 雙重劇本任一條沒兌現 → 估值倍數 re-rate"). The card already states
  this on lines 82-83 — keep that as the single mechanism summary in the
  public draft.

## Readiness Report

```text
Card #002 readiness: NOT READY

Resolved:
- Backbone: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md#第二條 [ok]
- Source labels: 2/3 labeled
- Primer: skipped (theme primer already present) [ok]
- Source tutor: cross-source-synthesis required [missing]
- IA1 gate: required (risk: high) [missing]
- ## Draft Post block: required [missing]

Missing artifacts (in order to produce):
1. Source packet for MediaTek Analyst Day 2025 under
   research/sources/ai-server-supply-chain/analyst-day/
2. Label source #3 in card frontmatter with a claim-type tag.
3. Cross-source tutor note + paired HTML at
   research/source-tutor/ai-server-supply-chain/ and
   research/knowledge/ai-server-supply-chain/readings/.
4. Pre-publish facts: stock-price move from 2025 mid, P/E z-score, gross
   margin ranges. Resolve TODO markers in the card body.
5. Position disclosure resolved in CTA footer.
6. `## Draft Post` block drafted in 起承轉合 voice per
   .cursor/rules/content-card-voice.mdc.
7. content/cards/reviews/2026-05-19_card-002-mediatek-2b_review.html paired
   review page.
8. IA1 decision file ops/decisions/<YYYY-MM-DD>_ia1_card-002-mediatek-2b.md
   after the above are in place.

Next action:
Stage the MediaTek Analyst Day 2025 source packet and run cross-source-
synthesis tutor across the three sources. Do not draft `## Draft Post`
until the tutor note exists.
```

## Validation Notes

This dry-run is intentionally not a draft. It exercises the new components:

- [.cursor/rules/content-thesis-card.mdc](../../.cursor/rules/content-thesis-card.mdc)
  → caught the missing `## Draft Post` block and the missing source label.
- [.cursor/rules/content-card-voice.mdc](../../.cursor/rules/content-card-voice.mdc)
  → identified the public surface gap (no 起承轉合 block yet).
- [.cursor/skills/card-source-readiness/SKILL.md](../../.cursor/skills/card-source-readiness/SKILL.md)
  → produced the readiness report in the expected shape.
- [.cursor/skills/thesis-card-writing/prerequisites.md](../../.cursor/skills/thesis-card-writing/prerequisites.md)
  → enforced the cross-source tutor requirement at 3+ sources.
- [docs/WORKFLOW_PATTERNS.md#thesis-card-workflow](../../docs/WORKFLOW_PATTERNS.md)
  → confirmed the strict sequence (source packet → primer skipped → tutor →
  draft → review → IA1 → reflection → ready).

If Card #002 is the next card to ship, the work order is set. Drafting the
`## Draft Post` block should not start until items 1-3 above are complete.
