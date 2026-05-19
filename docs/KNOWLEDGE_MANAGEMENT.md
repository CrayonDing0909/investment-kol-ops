# Knowledge Management

Purpose: define this repo's lightweight, file-first version of the LLM Wiki
pattern (inspired by Karpathy's idea file). Knowledge here lives as git-tracked
Markdown + HTML, not in a database, vector store, or external CMS. This doc
explains the layered model so future agents and skills do not invent parallel
storage.

This is the design layer. The day-to-day rules and workflows that act on it
live in:

- [docs/WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md)
- [docs/CONTEXT_STRATEGY.md](CONTEXT_STRATEGY.md)
- [docs/HTML_READING_UI_GUIDE.md](HTML_READING_UI_GUIDE.md)
- [docs/HUMAN_GATES.md](HUMAN_GATES.md)
- [.cursor/rules/**](../.cursor/rules)
- [.cursor/skills/**](../.cursor/skills)

## Why a Wiki Pattern, Not RAG

We deliberately avoid RAG-style "retrieve fragments at query time, regenerate
on every question" workflows for personal research. Reasons:

- Investment research compounds; the same sources support many cards, briefs,
  and postmortems. Re-deriving synthesis every time loses prior judgment.
- Claim-type discipline (`reported-fact` vs `forward-looking-target`) must be
  applied once, not re-inferred per query.
- Human gates need stable artifacts to point at; vector chunks are not
  reviewable.

Instead, the repo maintains a wiki-like layered structure where each layer has
a single owner and a clear purpose.

## Layered Model

```text
Layer 1: Raw sources       (immutable)
Layer 2: Maintained wiki   (LLM-edited, human-reviewed)
Layer 3: Schema / config   (rules, workflows, skills, templates)
Layer 4: Indexes & logs    (file-first, parseable, generated where possible)
```

### Layer 1 — Raw Sources (immutable)

Curated source documents the LLM may read but must not modify.

Paths:

- `research/sources/<theme>/<source-id>-source-packet.md` — primary source
  packets (filings, transcripts, IR decks, articles, papers).
- `research/intake/<source-id>.md` — original intake notes when present.

Rules:

- Sources are append-only. Corrections happen via new packets with
  `supersedes:` frontmatter, never by editing the original.
- No claim-type interpretation lives at this layer.

### Layer 2 — Maintained Wiki

LLM-built, human-reviewed knowledge that compounds over time. This is the
"wiki" in Karpathy's sense for this repo.

Paths:

- `research/notes/` — canonical Markdown for primers, briefs, and topic
  notes.
- `research/source-tutor/<theme>/` — canonical Markdown for source tutor
  notes (single-source and cross-source).
- `research/knowledge/<theme>/` — paired HTML reading surfaces:
  - `index.html` — theme map.
  - `primers/<primer>.html` — domain primers.
  - `readings/<source-id>.html` — source tutor reading views.
  - `<topic>.html` — topic pages.
  - `sources/<source>.html` — individual source reading views.
- `content/cards/<card>.md` — published-style thesis cards (synthesis output
  that other cards may reference).
- `content/cards/reviews/*.html` — paired HTML review pages.
- `content/drafts/*.md` — backbone internal articles that thesis cards
  extract from.

Rules:

- Every artifact that a human is expected to read, review, or revisit must
  have a reading surface. Self-contained HTML is the current default; see
  [docs/HTML_READING_UI_GUIDE.md](HTML_READING_UI_GUIDE.md).
- Markdown remains canonical for machine state and metadata. HTML links must
  label Markdown fallbacks as `md source`, `markdown intake`, or `markdown
  canonical`.
- New evidence updates the wiki, not just a single artifact. When a thesis
  card learns something new, the backbone document and the affected tutor
  note must be updated.

### Layer 3 — Schema / Config

The configuration that makes the LLM a disciplined maintainer instead of a
generic chatbot. This is the "AGENTS.md" in Karpathy's framing — but
unbundled into focused files.

Paths:

- [AGENTS.md](../AGENTS.md) — top-level agent instructions.
- [docs/WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md) — canonical workflows.
- [docs/CONTEXT_STRATEGY.md](CONTEXT_STRATEGY.md) — context packs.
- [docs/HUMAN_GATES.md](HUMAN_GATES.md) — gate definitions.
- `.cursor/rules/*.mdc` — narrow, file-scoped invariants.
- `.cursor/skills/<skill-name>/SKILL.md` — task-shaped procedures.
- Templates under `content/templates/`, `research/templates/`,
  `ops/templates/`.

Rules:

- Rules express short invariants; skills express step-by-step procedures.
- One concern per file. Use cross-references instead of copying text.
- Schema changes are system-affecting and must be flagged per the
  session-isolation rule before editing.

### Layer 4 — Indexes & Logs

Lightweight catalogs and timelines that let humans and agents navigate the
wiki without scanning every file.

Paths:

- `content/cards/_index.md` — thesis card registry (status, lens, counter
  direction, metrics).
- `ops/sessions/_index.md` — session registry.
- `research/knowledge/<theme>/index.html`,
  `research/knowledge/<theme>/readings/index.html` — theme-level navigation.
- `ops/current.md` — generated rollup of "now" state.
- `ops/dashboard.html` — generated cockpit.
- `docs/IMPLEMENTATION_PLAN.md` — Progress Log entries.
- `ops/decisions/*.md` — append-only gate decisions (act as an audit log).

Rules:

- Prefer generated indexes over hand-maintained ones when the source-of-truth
  data is in frontmatter or `ops/data/*.toml`. See
  [ops/build_dashboard.py](../ops/build_dashboard.py).
- Hand-maintained indexes must declare their canonical source so future
  agents do not duplicate it.

## Operations

The wiki supports three core operations. Each maps to existing workflows.

### Ingest (new source enters the repo)

```text
Source Collector → Source Tutor (single or cross-source)
  → updates wiki: tutor note (md), reading HTML, theme index
  → may trigger primer if domain is new
  → may trigger backbone update when claim changes a thesis line
```

A single ingest may touch 5-10 files: tutor note, paired HTML, readings
index, theme index, backbone draft, and any card whose source set changed.

### Query (the user asks a question)

```text
Pick workflow → load matching context pack → answer
  → if the answer is reusable, file it back as a wiki artifact
```

Reusable answers should not stay in chat. They should land as:

- A new primer or addendum under `research/notes/`.
- A claim-ledger update in the relevant tutor note.
- A new thesis card under `content/cards/`.
- A decision file under `ops/decisions/` if a gate fired.

### Lint (periodic health check)

Open questions to ask the agent on a cadence:

- Which cards reference sources that have not been through source tutor?
- Which tutor notes lack paired HTML?
- Which `_index.md` rows disagree with their source frontmatter?
- Which forward-looking claims are now testable against new earnings data?
- Which backbone sections were superseded by new cards but never updated?

A linter script is **not** required yet; the
[card-source-readiness](../.cursor/skills/card-source-readiness/SKILL.md)
skill covers per-card readiness today.

## Explicit Deferrals

The following are out of scope until concrete scale forces them:

- Vector embeddings or external RAG infrastructure.
- A database for cards, sessions, or decisions.
- An external CMS or headless content layer.
- Auto-generated Markdown-to-HTML pipelines for the knowledge surfaces.

Triggers that would justify revisiting:

- 15+ active cards or sessions concurrently
  (see [ops/README.md](../ops/README.md) Phase 2).
- A second human contributor working on the same wiki.
- The number of paired HTML pages exceeding what a human can maintain by
  hand within a normal week.

## Mapping to Karpathy's LLM Wiki

| Karpathy concept | This repo |
|---|---|
| Raw sources | `research/sources/**`, `research/intake/**` |
| The wiki | `research/notes/**`, `research/source-tutor/**`, `research/knowledge/**`, `content/cards/**`, `content/drafts/**` |
| The schema | `AGENTS.md` + `docs/*` + `.cursor/rules/**` + `.cursor/skills/**` + templates |
| index.md | `content/cards/_index.md`, `ops/sessions/_index.md`, theme `index.html` |
| log.md | `ops/decisions/**` (gates), `docs/IMPLEMENTATION_PLAN.md` Progress Log |
| Obsidian | Cursor + browser (HTML reading surfaces) |
| qmd / search | Deferred; existing indexes are enough at current scale |

This mapping is informative, not prescriptive. The repo intentionally diverges
where investment-content discipline (claim-type labels, human gates, dual
public/internal voice) requires more structure than a personal note system.
