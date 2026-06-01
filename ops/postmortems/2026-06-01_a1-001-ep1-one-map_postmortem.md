---
artifact_type: postmortem
scope: internal-process
subject: A1-001 EP1 "AI Server 一張圖看供應鏈" (first HTML public artifact)
artifact_ref: research/knowledge/ai-server-supply-chain/series/overview/ep1-one-map.html
created_at: 2026-06-01
status: internal (not a public postmortem; Gate PM1 not required)
related: docs/CONTENT_CONVERSION_PIPELINE.md
---

# Postmortem — Why the first HTML artifact (A1-001 EP1) failed

> Internal process postmortem. This is **not** a public postmortem of a wrong
> investment call, so Gate PM1 does not apply. Purpose: explain the failure and
> tie each cause to the control that now prevents it.

## What happened

A1-001 EP1 ("AI Server 一張圖看完整供應鏈") was built as an HTML reading page,
then reviewed by the owner. The owner's verdict:

- "看了之後好像不會覺得學到了什麼，就是一張圖滑過去。"
- "重點模糊，看不到該看哪裡，也不知道學到什麼。"
- Threads draft: "完全不像我，看起來就像 AI 整理出來的話。"
- "一堆專有名詞沒解釋，連 owner 本身的我都看不懂。"

The artifact passed a naive safety bar (sources labeled, no buy/sell) but was
**not publishable** because a human read it and learned nothing.

## Root cause

**The public artifact was generated directly from the knowledge map.** There was
no conversion layer between "what we know" and "what we teach." Concretely:

1. **Completeness-first, not comprehension-first.** The page rendered the full
   6-layer stack + upstream/midstream/downstream + money-flow — the internal
   primer's structure — instead of teaching one idea.
2. **Jargon dump on the first screen.** hyperscaler capex, ODM, HBM, CoWoS, ABF,
   MLCC, cold plate, CDU, manifold, UQD — none explained. The owner (the target
   reader's proxy) could not parse the first screen.
3. **No single takeaway.** Nothing the reader could repeat in one sentence.
4. **Wrong voice.** Media-explainer tone, not the owner's raw-research voice
   (no first person, no uncertainty, no parenthetical inner voice), violating
   `docs/VOICE_PROFILE.zh.md` and `.cursor/rules/content-voice-raw-research.mdc`.
5. **Number-first / company-first framing.** `$600K` and NVIDIA appeared up
   front, presuming an investment frame the explainer phase should avoid
   (`.cursor/rules/series-narrative-architecture.mdc`).

The deeper cause: the repo had **no Content Conversion Pipeline**. "research →
public artifact" had nothing in the middle, so an internal artifact was shipped
as a public one.

## What the owner got right (the real Gate A review)

The owner's reaction — "I did not learn anything" — was the most valuable Gate A
signal in the project so far. It exposed that **safe ≠ publishable**, and that
**the problem was the artifact, not the reader.**

## Controls added (A0.7)

| Failure | Control that now prevents it |
|--------|------------------------------|
| Public artifact rendered from knowledge map | Pipeline forbids it; must pass Series Bible + Episode Contract — `docs/CONTENT_CONVERSION_PIPELINE.md` |
| Completeness-first | "Artifact-led = comprehension-first" principle; internal vs public artifact split — `docs/ARTIFACT_SYSTEM.md` |
| Jargon dump | Episode Contract first-screen jargon budget (explainer = 0) — `content/templates/episode-contract.md` |
| No single takeaway | Series Bible + Episode Contract require one-takeaway per episode |
| Wrong voice | Voice locked in Series Bible / Episode Contract before any output |
| Safe-but-unpublishable | Gate A now = Safety Check + Owner Comprehension Check — `docs/HUMAN_GATES.md` |
| "I did not learn anything" ignored | Hard rule: that statement blocks Gate A approval; artifact returns to rebuild |

## Status of A1-001

- EP1 HTML (`ep1-one-map.html`) is **not approved** and **not published**; Gate A
  remains `defer`.
- The EP1 Threads voice has since been re-locked by the owner (save point
  `content(a1): lock EP1 thread voice draft` on `feat/a1-001-ai-server-one-map`).
- The EP1 **rebuild** will be redone *through* the new pipeline (Series Bible →
  Episode Contract → outputs → Gate A), not by patching the old page.

## Lesson (one line)

Do not render research into public artifacts. Re-author them through a contract
that guarantees a human learns one thing.
