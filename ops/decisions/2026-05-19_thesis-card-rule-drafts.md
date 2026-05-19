---
artifact_type: rule-draft
status: draft / not-yet-promoted
workflow: content-production
related_artifacts:
  - ops/decisions/2026-05-13_workflow-rule-audit-card-001.md
  - ops/decisions/2026-05-14_card-writing-voice-lessons.md
  - ops/decisions/2026-05-19_card-002-readiness-dry-run.md
created_at: 2026-05-19
reviewer: CrayonDing0909
promotion_gate: "ship Ep1 → review Ep1 metrics → ship Ep2 → confirm same structure → reconcile with series-narrative-architecture.mdc from PR #20 → only then promote to .cursor/rules/"
reconciliation_note: |
  PR #20 (sibling worktree at /Users/dylanting/personal/investment-kol-ops-card001-pr,
  branch research/x-threads-card-001-platform-pass) already carries
  .cursor/rules/series-narrative-architecture.mdc. The two drafts below were
  written in the docs/reading-surface-rule branch before that fact was clear.
  Do not promote either draft to .cursor/rules/ in this workspace without
  reconciling against series-narrative-architecture.mdc first.
---

# Thesis Card Rule Drafts (not promoted)

## Why this file exists

I drafted two `.cursor/rules/*.mdc` files in this branch during the article-
stability pass — but it is too early to freeze them as rules:

- Ep1 (Card #001 cooling-BOM) just shipped its review pass; Ep2 / Ep3 have
  not been drafted yet.
- PR #20 carries a separate `series-narrative-architecture.mdc` rule that
  needs reconciliation before either of these drafts is promoted here.
- The voice lessons in
  [2026-05-14_card-writing-voice-lessons.md](2026-05-14_card-writing-voice-lessons.md)
  explicitly say to wait 2-3 cards before promotion.

So the drafts are stored here as decisions, not enforced as rules. They will
either be promoted, merged with `series-narrative-architecture.mdc`, or
dropped after Ep2 / Ep3.

## Draft 1 — content-thesis-card (structure invariants)

Intended target: `.cursor/rules/content-thesis-card.mdc`.

```markdown
---
description: Thesis card structure rule for public investment cards
globs: "content/cards/**/*.md"
alwaysApply: false
---

# Thesis Card Rule

A thesis card is a single-mechanism public artifact extracted from a backbone
internal article. This rule governs **structure invariants** so cards stay
consistent across cycles, regardless of voice or domain.

The full template lives in content/templates/thesis-card.md. The rule below
is the smaller, enforceable subset.

## Required Structure

One card carries one chain:

    1 Observation (with source label)
    → 1 Mechanism (plain language, falsifiable)
    → 1 Implication (company + signal + timeframe)
    → 1 Counter (threshold + time-window + direction)

If a card needs two mechanisms or two Counters, split it into two cards.

## Required Frontmatter

Every card under content/cards/ must declare:

- workflow: content-production
- artifact_type: thesis-card
- lens: one of 資金 | 為什麼 | 基本面 | 啟動 | 破局 | meta.
- counter_direction: one of bull-kill | bear-falsify | n/a (n/a only for meta lens).
- backbone_ref: relative path to the backbone document this card extracts from.
- backbone_section: the section anchor inside the backbone.
- sources: at least one entry with a claim-type label per
  .cursor/rules/source-tutor-reading.mdc.
- public_status: one of outline | draft | ready | scheduled | published | archived.
- risk: high if the card carries an investment claim, otherwise medium or low.
  risk: high must route through IA1 before public_status: ready.

## Mandatory Counter

Counter is required, not optional. Counter wording must include:

- Direction tag: （bull-case kill） or （bear-case falsification）. Meta-lens
  cards may use （method-level caveat） instead.
- A concrete threshold (number, event, or design win).
- A time-window (quarter, year, or named milestone).

A Counter that only says "if conditions change" is incomplete.

## Internal vs Public Surface

Internal section names — Hook, Observation, Mechanism, Implication, Counter,
bull-case kill, bear-case falsification — are the working frame for drafting
and review. The published surface must not expose them as visible labels.
Use prose (起承轉合, plain Chinese) per content-card-voice.

The card file may carry both layers: structured sections for review, plus a
## Draft Post block for the public version. The ## Draft Post block is the
shipping artifact.

## Source Discipline

- Every Observation cites a source with claim-type label
  (reported-fact, management-expectation, forward-looking-target,
  secondary-interpretation, agent-inference).
- Forward-looking targets must not be presented as current facts in the
  public draft. This is a hard line per the source tutor rule.
- A card that references three or more sources should be backed by a
  cross-source tutor note before public_status: ready.

## Pre-Ready Checklist

Before flipping public_status: ready:

- [ ] Card carries one Observation → Mechanism → Implication → Counter chain.
- [ ] Counter has direction + threshold + time-window.
- [ ] Public draft (## Draft Post) does not expose internal section labels.
- [ ] All Observation citations have claim-type labels.
- [ ] If risk: high, an IA1 decision file exists under ops/decisions/.
- [ ] Source tutor and (if needed) domain primer artifacts exist for the
      sources cited.
- [ ] Card frontmatter backbone_ref and backbone_section resolve to a real
      backbone path/anchor.
```

## Draft 2 — content-card-voice (public surface voice)

Intended target: `.cursor/rules/content-card-voice.mdc`. Supersedes the voice
checklist in `2026-05-14_card-writing-voice-lessons.md` once 2-3 cards
validate it.

```markdown
---
description: Public thesis-card voice rule for investment cards
globs: "content/cards/**/*.md"
alwaysApply: false
---

# Card Voice Rule

A thesis card is read by an outside audience but must still sound like the
user's research thought process. This rule governs the **public surface**
(the ## Draft Post block and anything that ships), not the internal sections.

Working voice for research notes is governed by
.cursor/rules/content-voice-raw-research.mdc. Canonical examples live in
docs/VOICE_PROFILE.zh.md and
ops/decisions/2026-05-14_card-writing-voice-lessons.md.

## Required Behavior

- First line is a memory anchor: a number, company, or specific event the
  reader can hold onto.
- The opening paragraph must say why the user is stopping on this topic ("這
  是我最近整理 ... 時，覺得最有記憶點的一個數字"), not "今天要解釋 X 是什麼".
- Public flow follows 起承轉合, not the internal Observation → Mechanism →
  Implication → Counter labels.
- Keep parenthetical inner-voice notes (e.g. "（算一種利多出盡吧）"). They are
  intentional, not noise.
- Source caveats must lead to a judgment: "因為 source 還是二手拆解，所以我
  暫時不會 ... 但它至少讓我知道 ..." — never end on the caveat alone.
- End the card with a "所以統整完..." conclusion that names what the user
  currently understands and what would change that view.

## Avoid

Recurring AI-explainer phrases that broke Card #001 drafts:

- 不再只是 A，而是 B
- 這不是 primary source，是 secondary ...
- 為什麼 X 會變成 Y？ as a standalone teaching frame.
- Reader takeaway / 核心 thesis / 底層原因 / 重新定價 /
  投資機會正在擴散 / 這個方向值得關注.
- Generic disclaimer-style caveats that do not feed into a judgment.

## Preferred Shape

    起：一句記憶點（具體數字 / 公司 / 事件）
    承：先翻成人話，這個記憶點為什麼存在
    轉：誰會被卡住？什麼會讓這條線斷掉？
    合：所以統整完上面這些資料，我目前理解是什麼，什麼會讓我改觀

## Review Checklist

Before flipping public_status: ready:

- [ ] First line is a concrete memory anchor, not a generic hook.
- [ ] No banned AI-explainer phrases in the public draft.
- [ ] Public surface uses 起承轉合, not internal section labels.
- [ ] Every caveat ends in a judgment, not a disclaimer.
- [ ] Closing paragraph says what the user currently understands and what
      would break that view.
```

## Promotion gate

Do **not** copy either draft into `.cursor/rules/` until:

1. Ep1 (Card #001) has shipped publicly.
2. Ep1 metrics + replies reviewed.
3. Ep2 drafted and shipped.
4. Ep2 confirms the same structure / voice pattern works.
5. PR #20 merged; `series-narrative-architecture.mdc` reviewed in this
   workspace.
6. Manual reconciliation pass: decide whether each draft above lives as a
   standalone rule, merges into `series-narrative-architecture.mdc`, or
   gets dropped.

## Linked

- [ops/decisions/2026-05-13_workflow-rule-audit-card-001.md](2026-05-13_workflow-rule-audit-card-001.md)
- [ops/decisions/2026-05-14_card-writing-voice-lessons.md](2026-05-14_card-writing-voice-lessons.md)
- [ops/decisions/2026-05-19_card-002-readiness-dry-run.md](2026-05-19_card-002-readiness-dry-run.md)
- [ops/decisions/2026-05-19_ep1-prepublish-checklist.md](2026-05-19_ep1-prepublish-checklist.md)
- PR #20 worktree: `/Users/dylanting/personal/investment-kol-ops-card001-pr`
  on `research/x-threads-card-001-platform-pass` carries
  `.cursor/rules/series-narrative-architecture.mdc`.
