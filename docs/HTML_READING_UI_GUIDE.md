# HTML Reading UI Guide

Purpose: define how human-facing HTML reading pages should be built in this repo.

This is not a visual design system. The goal is reading quality: fast scanning,
clear confidence labels, source traceability, and low cognitive load.

## Core Principle

```text
Human reading path: HTML first
Canonical source / metadata: Markdown
```

If the user is expected to read, learn, review, or revisit an artifact, it needs
an HTML reading page. Markdown remains the canonical machine-readable source and
the git-friendly metadata layer.

## What Needs an HTML Reading Page

Required:

- Knowledge maps: `research/knowledge/<theme>/index.html`
- Topic pages: `research/knowledge/<theme>/<topic>.html`
- Source reading views: `research/knowledge/<theme>/sources.html`
- Individual source packets that the user may click: `sources/<source>.html`
- Tutor Q&A reading views: `qa.html` and any long Q&A page such as `cpu-qa.html`
- Intake pages that the user may click from a source card: `intakes/<source>.html`

Optional:

- Internal briefs, if they become hard to read as markdown.
- Decision logs, if gate review becomes visually complex.

Not required:

- `.gitkeep`
- raw source packet markdown
- canonical intake markdown
- short metadata-only docs

## Page Types

### Knowledge Map Page

Example: `research/knowledge/ai-server-supply-chain/index.html`

Must include:

- Breadcrumb.
- Title.
- One-paragraph umbrella thesis.
- Status metadata.
- Topic cards.
- Relationship map.
- Known facts / market narratives / unverified assumptions.
- Open questions backlog.
- Reading entry points.
- Sources / Q&A links.

### Topic Page

Example: `cpu.html`, `asic.html`.

Must include:

- Breadcrumb.
- One-line thesis.
- What is it?
- Where is it used?
- Why it matters now?
- Industry trend.
- Companies / tickers.
- Market pricing.
- Open questions.
- Sources.

### Sources Reading View

Example: `sources.html`.

Must include:

- How to read this page.
- One card per source packet.
- Why this source matters.
- Key numbers.
- Direct quote when useful.
- Reliability label.
- Follow-up tasks.
- HTML source / HTML intake links first.
- Markdown source links only as fallback, explicitly labeled `md source`.

### Individual Source Page

Example: `sources/amd-q1-2026.html`.

Must include:

- Source quality: primary / secondary / unverified.
- Why this source matters.
- Key numbers table.
- Direct quotes.
- Reliability notes.
- Follow-up tasks.
- HTML intake link first.
- Markdown source packet link second.

### Tutor Q&A Page

Example: `qa.html`, `cpu-qa.html`.

Must include:

- Question in user language.
- Short answer.
- Mental model.
- Technical explanation.
- Why investors care.
- Companies / tickers.
- What to watch.
- What is still unknown.
- Sources.

## Link Rules

Human-facing HTML pages must prefer HTML links.

Good:

```html
<a href="./sources/amd-q1-2026.html">HTML source</a> ·
<a href="./intakes/amd-q1-2026.html">HTML intake</a> ·
<a href="../../sources/.../amd-q1-2026-source-packet.md">md source</a>
```

Bad:

```html
<a href="../../intake/2026-05-10_gooeye-ep659_cpu.md">intake</a>
```

Rules:

- Never label a Markdown link as just `source`, `intake`, or `Q&A`.
- If a link goes to Markdown, label it `md source`, `markdown intake`, or
  `markdown canonical`.
- If no HTML version exists, link to a higher-level HTML reading view first, then
  the Markdown fallback.

## Status Labels

Use simple text labels. Do not depend on color alone.

Allowed labels:

- `draft`
- `reviewed`
- `needs follow-up`
- `primary`
- `secondary`
- `unverified`
- `do not publish as fact yet`
- `gate-pending`
- `gate-approved`
- `gate-deferred`

For high-risk claims, write the warning in plain language, not only as a badge.

## Layout Rules

- Static HTML only in M1-M2.
- Inline CSS only.
- No framework.
- No external assets.
- No JS unless a later milestone explicitly requires collapsible sections.
- Max content width around `760px-920px`.
- Mobile readable at 375px.
- Use tables for comparable metrics.
- Use cards for source packets, topic summaries, and warnings.
- Keep paragraphs short: 2-4 sentences.
- Use lists for scanability.

## Visual Style

Keep it plain and readable.

Do:

- Comfortable contrast for long reading. Avoid pure black / pure white pairs.
- Clear headings.
- Light borders.
- Consistent spacing.
- Breadcrumbs.
- Source links at the bottom of sections.
- Reliability warnings near claims.

Recommended reading palette:

```css
:root {
  --bg: #f6f7f9;
  --surface: #ffffff;
  --surface-muted: #edf1f5;
  --text: #24272d;
  --muted: #68707d;
  --line: #d8dee6;
  --link: #315f9f;
  --warn-bg: #fff4dc;
  --warn-text: #6b4b00;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #17191d;
    --surface: #20242a;
    --surface-muted: #2a3038;
    --text: #e2e8f0;
    --muted: #a8b1bd;
    --line: #3a424e;
    --link: #91b7ff;
    --warn-bg: #332813;
    --warn-text: #f1d18a;
  }
}
```

Why:

- Neutral off-white background avoids browser-white glare without introducing a strong yellow tint.
- Soft dark mode reduces eye fatigue versus pure black with pure white text.
- Muted text is used for metadata and secondary explanations, not primary claims.
- Warning colors must be readable in both light and dark modes.

Avoid:

- Gradients.
- Decorative animations.
- Heavy shadows.
- Emoji as icons.
- Too many colors.
- Huge hero sections.
- Marketing-style copy.
- Hiding uncertainty.

## Accessibility Checklist

Before delivery:

- [ ] Page has a clear `<title>`.
- [ ] Header has breadcrumb and H1.
- [ ] Links are visible and descriptive.
- [ ] Source confidence is visible in text.
- [ ] Tables have headers.
- [ ] No critical information depends only on color.
- [ ] Page is readable on mobile width.

## Review Checklist

Before committing a new HTML reading page:

- [ ] Does it answer what the user needs to understand?
- [ ] Is the first screen enough to orient the reader?
- [ ] Are primary vs secondary sources clearly separated?
- [ ] Are follow-up questions visible?
- [ ] Are Markdown links explicitly labeled as fallback?
- [ ] Is the page useful without opening the markdown file?

