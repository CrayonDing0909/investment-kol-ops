---
workflow: source-tutor
artifact_type: source-tutor-reading
risk: low
created_at: YYYY-MM-DD
theme: <theme>
source_id: <source-id>
source_quality: primary | secondary | unverified
source_class: filing | earnings-transcript | ir-deck | press-release | news | research-paper | report | podcast | creator-note
reading_goal: learn-domain-context | verify-claim | extract-numbers | prepare-brief | public-source-hardening
status: draft | reviewed
---

# Source Tutor Reading: <source title>

> Purpose: tutor the user through this already-selected source.
> This is not source discovery and not a generic summary.
> The note must teach how to read the source, not only produce safe wording.
> Every important claim must be mapped to: source wording → claim type → what
> it supports → what it does not prove → verification metric → downstream use.

## Source Metadata

- Source packet:
- Original URL:
- Publisher:
- Date published:
- Captured at:
- Source quality: primary / secondary / unverified
- Source class:
- Related company / ticker:

## Reading Goal

<Why are we reading this source now? What claim, topic, or confusion should this
run resolve?>

## 這份 Source 在解決什麼問題

<Explain the business, technical, financial, or investor question this source is
trying to answer. Do not start with a generic summary.>

## Reading Lens (這類 Source 一般怎麼讀)

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

## Source Map (Sentence-Level Reading Chain)

> One row per important sentence. This is the core of the tutor note.

| # | Exact source wording | Claim type | What it supports | What it does not prove | Verification metric | Downstream use |
|---|----------------------|------------|------------------|------------------------|---------------------|----------------|
| 1 | "<quote>" | reported-fact / management-expectation / forward-looking-target / secondary-interpretation / agent-inference / open | | | | claim-ledger / brief / article block / follow-up source |
| 2 | | | | | | |

## 哪些句子是事實，哪些是 Management Expectation

| # | Sentence / wording | Category | Why |
|---|--------------------|----------|-----|
| 1 | "<quote or wording>" | reported-fact / management-expectation / forward-looking-target / secondary-interpretation / agent-inference / open | |

## 哪些數字不能直接拿去公開寫

| # | Number | Unit | Period / timing | Why risky | Safer wording |
|---|--------|------|-----------------|-----------|---------------|
| 1 | | | | <Target? estimate? TAM? guidance? secondary interpretation?> | |

## What This Source Proves

- <Claim the source can support directly.>

## What This Source Does Not Prove

- <Common overreach or stronger claim this source cannot support.>

## Common Misreads

| Misread | Why it is wrong | Better wording |
|---------|-----------------|----------------|
| | | |

## 如果我是投資人，該看哪 5 句

| # | Sentence | Why it matters | How to read it |
|---|----------|----------------|----------------|
| 1 | "<quote or wording>" | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Internalization Artifacts

> These four artifacts turn the source into reusable material. They are not
> optional. If a section is empty, mark it `n/a` with one sentence explaining
> why.

### Claim Ledger

| # | Claim | Claim type | Source wording | Safe public wording |
|---|-------|------------|----------------|---------------------|
| 1 | | reported-fact / management-expectation / forward-looking-target / secondary-interpretation / agent-inference / open | "<quote>" | |
| 2 | | | | |

### Mental Model Update

- <Bullet that changes how the user thinks about the company, industry, or
  thesis after reading this source.>
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
forward-looking expectations. This is the only place where prose is allowed.>

## Downstream Routing

| Artifact | Action | Path |
|----------|--------|------|
| Source checklist | append claims to | `research/sources/<theme>/<...>-source-checklist.md` |
| Brief or notes | update section | `research/notes/<...>.md` |
| Knowledge HTML page | refresh section | `research/knowledge/<theme>/<page>.html` |
| Article draft | reuse output block | `content/drafts/<...>.md` |
| Follow-up source tasks | add to source backlog | `research/questions/<theme>/<...>.md` |

## 這份 Source 還不能回答什麼

- <Question this source cannot answer.>
- <Missing primary source, metric, time period, or comparison.>

## Tutor Explanation

<Explain the source in plain Chinese. Focus on how the user should think, not on
writing a thesis for them.>

## Checkpoint Questions

- What is one thing here that is definitely a reported fact?
- What is one thing that is only management expectation or target?
- Which sentence would become misleading if we removed "expects" or "targets"?
- What primary source would we need before using the weakest claim publicly?
- Which mental model bullet would I keep even if this company stops being
  interesting?

## Follow-Up Needed

- <Missing source, contradiction, or question to resolve.>

## Update Targets

- Source checklist to update: <path>
- Brief section to update: <path or section>
- HTML source page to update: <path>
