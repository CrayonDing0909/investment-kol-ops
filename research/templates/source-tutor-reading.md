---
workflow: source-tutor
artifact_type: source-tutor-reading
reading_mode: single-source | cross-source-synthesis
risk: low
created_at: YYYY-MM-DD
theme: <theme>
source_id: <source-id>
source_quality: primary | secondary | unverified | mixed
source_class: filing | earnings-transcript | ir-deck | press-release | news | research-paper | report | podcast | creator-note | cross-source
reading_goal: learn-domain-context | verify-claim | extract-numbers | prepare-brief | public-source-hardening
status: draft | reviewed
supersedes: <optional path to previous reading this run replaces or extends>
---

# Source Tutor Reading: <title>

> Purpose: tutor the user through already-selected source material.
> This is not source discovery and not a generic summary.
> The note must teach how to read the source(s), not only produce safe wording.
>
> Two reading modes are supported. Set `reading_mode` in the frontmatter.
>
> - `single-source`: deep-read one selected source. Use the sentence-level
>   reading chain (source wording → claim type → supports → does-not-prove →
>   verification → downstream use).
> - `cross-source-synthesis`: integrate multiple sources for one company,
>   topic, or thesis. Use the thesis-line reading chain (thesis line →
>   supporting sources → strongest claim type → multi-source consistency →
>   public-quotable?).
>
> Sections marked `[single]` are required for single-source mode only.
> Sections marked `[cross]` are required for cross-source-synthesis mode only.
> Sections without a mode tag are required for both modes.

## Source Metadata

`[single]` Single-source format:

- Source packet:
- Original URL:
- Publisher:
- Date published:
- Captured at:
- Source quality: primary / secondary / unverified
- Source class:
- Related company / ticker:

`[cross]` Cross-source format (table):

| # | Packet | Source class | Source quality | Layer / Angle |
|---|--------|--------------|----------------|---------------|
| 1 | <path> | | | |
| 2 | | | | |
| 3 | | | | |

- Captured at:
- Related company / ticker:

## Reading Goal

<Why are we reading this source / set of sources now? What claim, topic, or
confusion should this run resolve?>

## 這份 Source / Set 在解決什麼問題

<Explain the business, technical, financial, or investor question this source
or set of sources is trying to answer. Do not start with a generic summary.>

`[cross]` In cross-source mode, also map any of the user's prior beliefs to
the source(s) that support, contradict, or extend each belief. Mark the
strongest and weakest support explicitly.

## Reading Lens

`[single]` Single-Source Lens (這類 Source 一般怎麼讀):

<Explain the reading strategy for this source class so the user can reuse it on
other companies and industries. Examples: an earnings release mixes reported
results, segment color, and forward outlook; an IR deck or Analyst Day often
contains long-range targets framed as "expects to achieve"; a transcript adds
management interpretation; a media article adds secondary interpretation.>

- What this source class is good for:
- What this source class is weak at:
- Vocabulary that signals claim type (e.g. "was," "expects," "targets,"
  "guides," "estimates," "plans"):
- Sections to read first vs sections to skim:

`[cross]` Cross-Source Synthesis Lens (跨 source 怎麼整合):

Explain how to read multiple sources as one integrated picture. Cover:

- The 4 cross-source principles:
  1. Independent evidence chain: 同一條原始 leak 被多家轉貼仍只算 1 條
     evidence chain.
  2. Source class hierarchy 不變: primary > high-quality-secondary >
     secondary > tertiary.
  3. 管理層 framing 不能跨源累加: 同一個 framing 出現多次不代表加倍真實。
  4. Forward-looking vs reported-fact 不能因為跨源就升等。
- Company- or topic-specific reading rules that emerge from this set.

## Source Map

`[single]` Sentence-Level Reading Chain:

> One row per important sentence. This is the core of the tutor note.

| # | Exact source wording | Claim type | What it supports | What it does not prove | Verification metric | Downstream use |
|---|----------------------|------------|------------------|------------------------|---------------------|----------------|
| 1 | "<quote>" | reported-fact / management-expectation / forward-looking-target / secondary-interpretation / agent-inference / open | | | | claim-ledger / brief / article block / follow-up source |
| 2 | | | | | | |

`[cross]` Thesis-Line Reading Chain:

> One row per thesis line. Aggregates evidence across sources.

| # | Thesis line | Supporting sources | Strongest claim type | Multi-source consistent? | Public-quotable? |
|---|-------------|-------------------|---------------------|------------------------|-----------------|
| 1 | | Source 1, 4 | reported-fact (primary) | yes / partial / no | yes / with caveats / no |
| 2 | | | | | |

## 哪些句子 / 訊號是事實，哪些是 Management Expectation

| # | Sentence / signal | Category | Source(s) | Why |
|---|-------------------|----------|-----------|-----|
| 1 | "<quote or wording>" | reported-fact / management-expectation / forward-looking-target / secondary-interpretation / agent-inference / open | | |

## 哪些數字不能直接拿去公開寫

| # | Number | Unit | Period / timing | Source | Why risky | Safer wording |
|---|--------|------|-----------------|--------|-----------|---------------|
| 1 | | | | | <Target? estimate? TAM? guidance? secondary interpretation?> | |

## What This Source / Set Proves

- <Claim the source(s) can support directly.>

## What This Source / Set Does Not Prove

- <Common overreach or stronger claim this source / set cannot support.>

## Sub-Thesis Breakdown `[cross]`

> When the subject has multiple independent story lines, break the company /
> topic into 4-6 sub-theses, each with its own source backing and risk.

### Sub-Thesis 1: <name>

- Source backing:
- Reported:
- Forward-looking:
- 角色 / role in overall picture:
- 風險 / what could break it:

### Sub-Thesis 2: <name>

(...)

## What Each Source Adds That Others Don't `[cross]`

| Source | 它獨家貢獻什麼？ | 沒有它就會缺什麼？ |
|--------|---------------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |

## Sources 互相強化 / 互相牴觸 `[cross]`

### 強化（多 source 一致）

- <Thesis line>: which sources independently confirm?

### 牴觸 / 張力（同時為真但方向相反）

- <Where two sources point in different directions, and how to read it.>

## Common Misreads

| Misread | Why it is wrong | Better wording |
|---------|-----------------|----------------|
| | | |

## 如果我是投資人，該看哪 5 句 / 5 條 thesis

`[single]` 5 sentences (single-source):

| # | Sentence | Why it matters | How to read it |
|---|----------|----------------|----------------|
| 1 | "<quote or wording>" | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

`[cross]` 5 thesis lines (cross-source):

| # | Thesis line | Why it matters | Strongest support |
|---|-------------|----------------|-------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Internalization Artifacts

> These four artifacts turn the source(s) into reusable material. They are
> not optional. If a section is empty, mark it `n/a` with one sentence
> explaining why.

### Claim Ledger

| # | Claim | Claim type | Strength (cross only) | Source(s) | Safe public wording |
|---|-------|------------|----------------------|-----------|---------------------|
| 1 | | reported-fact / management-expectation / forward-looking-target / secondary-interpretation / agent-inference / open | strong / medium / weak | | |
| 2 | | | | | |

### Mental Model Update

- <Bullet that changes how the user thinks about the company, industry, or
  thesis after reading this source / set.>
- <Bullet.>
- <Bullet.>

### Verification Watchlist

| # | Signal / metric | Why it matters | Where to look | Cadence |
|---|-----------------|----------------|---------------|---------|
| 1 | | | | weekly / monthly / quarterly / event-driven |
| 2 | | | | |

### Reusable Output Block

<One paragraph the user can drop into a brief or article, with claim types kept
visible. Should explicitly distinguish reported facts from management targets or
forward-looking expectations. In cross-source mode, the block should cover the
multi-line synthesis, not a single source. This is the only place where prose
is allowed.>

## Downstream Routing

| Artifact | Action | Path |
|----------|--------|------|
| Source checklist | append claims to | `research/sources/<theme>/<...>-source-checklist.md` |
| Brief or notes | update section | `research/notes/<...>.md` |
| Knowledge HTML page | refresh section | `research/knowledge/<theme>/<page>.html` |
| Article draft | reuse output block | `content/drafts/<...>.md` |
| Follow-up source tasks | add to source backlog | `research/questions/<theme>/<...>.md` |

## 還不能回答什麼

- <Question this source / set cannot answer.>
- <Missing primary source, metric, time period, or comparison.>

## Tutor Explanation

<Explain the source / set in plain Chinese. Focus on how the user should
think, not on writing a thesis for them. In cross-source mode, also explain
why integrating these particular sources matters more than reading any one
alone.>

## Checkpoint Questions

`[single]`:

- What is one thing here that is definitely a reported fact?
- What is one thing that is only management expectation or target?
- Which sentence would become misleading if we removed "expects" or "targets"?
- What primary source would we need before using the weakest claim publicly?
- Which mental model bullet would I keep even if this company stops being
  interesting?

`[cross]`:

- Which sub-thesis is most source-backed? Which is weakest?
- If I had to compress this company / topic to one sentence, what would it be?
- Which thesis line would collapse if I removed one specific source?
- Which mental model bullet would I keep as a general reading rule (not
  company-specific)?

## Follow-Up Needed

- <Missing source, contradiction, or question to resolve.>

## Update Targets

- Source checklist to update: <path>
- Brief section to update: <path or section>
- HTML source page to update: <path>

## Template Validation (Meta Reflection) `[optional]`

> Use this section when running a new reading_mode for the first time, or when
> the template feels strained. Record what worked, what needed extension, and
> propose template upgrades.

- Sections that held up as-is:
- Sections that needed extension:
- New sections introduced:
- Proposed template upgrade for future runs:
