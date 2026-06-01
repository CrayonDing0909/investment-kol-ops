# Content Conversion Pipeline

The missing layer between **raw research** and **public artifacts**. This file
defines the mandatory stages, the gates between them, and the rules that stop the
repo from shipping a knowledge map straight to an audience.

Bilingual mirror: [docs/CONTENT_CONVERSION_PIPELINE.zh.md](CONTENT_CONVERSION_PIPELINE.zh.md)
(this English file is the LLM-primary version).

Direction anchor: [docs/NORTH_STAR.md](NORTH_STAR.md). Artifact model:
[docs/ARTIFACT_SYSTEM.md](ARTIFACT_SYSTEM.md). Gates:
[docs/HUMAN_GATES.md](HUMAN_GATES.md). Voice:
[docs/VOICE_PROFILE.zh.md](VOICE_PROFILE.zh.md).

## Why this exists

A1-001 failed because it was generated **directly from the knowledge map**: it
rendered a complete supply-chain diagram, dumped 10+ unexplained terms on the
first screen, had no single takeaway, and used an AI-explainer voice instead of
the owner's. See
[ops/postmortems/2026-06-01_a1-001-ep1-one-map_postmortem.md](../ops/postmortems/2026-06-01_a1-001-ep1-one-map_postmortem.md).

The root cause was not bad writing. It was a **missing conversion layer**. The
repo had "research → ??? → public artifact" with nothing in the middle. This
pipeline fills the gap with two owner-approved contracts: a **Series Bible** and
an **Episode Contract**.

## Core principle

**Artifact-led means comprehension-first, not completeness-first.**

- Internal artifacts may be complete and dense (they serve research).
- Public artifacts must be understandable and worth reading (they serve an
  audience). A public artifact is a *re-authoring*, never a render, of internal
  material.

## The pipeline

```text
Raw research / sources
  → Internal artifact        (knowledge map, primer, source-tutor, brief)   [completeness-first]
  → Series Bible             (audience, arc, per-episode takeaway, voice, jargon policy)   [owner-approved]
  → Episode Contract         (one takeaway, what-not-to-say, metaphor, jargon budget)      [owner-approved, per episode]
  → Public outputs           (HTML / IG / Shorts / public thread)            [comprehension-first]
  → Gate A                   (Safety Check + Owner Comprehension Check)
  → Publish
```

Each arrow is a real step. You may not skip arrows.

## Stage definitions

### 1. Internal artifact (completeness-first)
Knowledge maps, primers, source-tutor readings, briefs. Lives in `research/**`.
Optimized for correctness and coverage. **Not** audience-facing. It is an input
to the pipeline, never a public output.

### 2. Series Bible (owner-approved)
One per content series, from
[content/templates/series-bible.md](../content/templates/series-bible.md).
Defines: audience, promise, the three-phase arc
(explainer / mechanism / thesis), the single takeaway for each planned episode,
the voice reference, the jargon policy, and the link-placement phase. The Series
Bible is the boundary between "what we know" and "what we will teach."

### 3. Episode Contract (owner-approved, per episode)
One per episode, from
[content/templates/episode-contract.md](../content/templates/episode-contract.md).
Formalizes the narrative contract: the one sentence the reader must remember,
what the episode will NOT say, the metaphor, the first-screen jargon budget, and
the comprehension target (what the reader can repeat afterward). **It must be
owner-approved before any public output is generated.**

### 4. Public outputs (comprehension-first)
HTML reading surface, IG carousel, Shorts, public thread. Generated **only after**
the Episode Contract is approved, and only within that contract's limits.

### 5. Gate A (Safety + Comprehension)
See [docs/HUMAN_GATES.md](HUMAN_GATES.md). Gate A now requires **both** a Safety
Check and an Owner Comprehension Check. Safe does not mean publishable.

## Hard rules (pipeline invariants)

1. **A public artifact cannot be generated directly from a knowledge map.** It
   must pass through a Series Bible and an Episode Contract first.
2. **The Episode Contract must be owner-approved before generating HTML / IG /
   Shorts / public thread.** No outputs before contract sign-off.
3. **Gate A = Safety Check + Owner Comprehension Check.** Both are required.
4. **Safe does not mean publishable.** Passing the safety checklist is necessary
   but not sufficient.
5. **Artifact-led means comprehension-first, not completeness-first.**
6. **If the owner says "I did not learn anything," Gate A cannot approve.** The
   artifact returns to rebuild (re-open the Episode Contract), not to a light
   edit.

## What changed vs. before

| Before | After |
|--------|-------|
| research → public artifact (no middle) | research → internal artifact → Series Bible → Episode Contract → public output |
| Gate A = safety only | Gate A = safety + comprehension |
| "complete and correct" was the bar | "understandable and worth reading" is the public bar |
| knowledge map could be rendered to public HTML | public artifact must be re-authored, never rendered |

## Relationship to other docs

- Artifact classes (internal vs public): [docs/ARTIFACT_SYSTEM.md](ARTIFACT_SYSTEM.md).
- Gate A comprehension check: [docs/HUMAN_GATES.md](HUMAN_GATES.md).
- Series arc + voice: [.cursor/rules/series-narrative-architecture.mdc](../.cursor/rules/series-narrative-architecture.mdc),
  [docs/VOICE_PROFILE.zh.md](VOICE_PROFILE.zh.md).
- Brief precondition: [content/templates/artifact-brief.md](../content/templates/artifact-brief.md).
