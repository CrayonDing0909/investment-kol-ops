---
artifact_type: tooling-survey
created_at: 2026-05-13
last_updated: 2026-05-13T19:10+08:00
---

# Tooling Options for Status Dashboard

> Survey of external tools that might replace or augment the repo-native
> `ops/current.md` + `ops/dashboard.html` cockpit.
>
> **Decision today**: keep the repo-native dashboard as source of truth. Do
> not adopt any external tool as a hard dependency yet. Revisit when manual
> updates become friction.

## Constraints This Workflow Has

Before judging tools, list what this repo actually needs to track:

- **Milestones (M1-M5)** from `docs/IMPLEMENTATION_PLAN.md` — not just generic
  tasks; each milestone has Definition of Done.
- **Sessions** — chat boundary + branch + scope + status, with handoff notes.
- **Cards** — `outline | draft | ready | scheduled | published | archived`,
  per-card Counter direction, per-card IA1 gate state.
- **Source quality** — `primary / secondary / unverified` + tutor claim types
  (`reported-fact`, `management-expectation`, etc.).
- **IA1 / IA2 / AR1 gates** — human review surface with `approve | edit |
  reject | defer`.
- **PRs and branches** as ship state.
- **Metrics** (later milestone).

Any external tool should help with at least one of those without forcing us to
abandon the markdown / HTML canonical layer.

## Candidates

### GitHub Projects

Pros:

- Native to GitHub. Syncs issues + PRs automatically.
- Roadmap view supports milestones and dates.
- Custom fields up to 50 (status, iteration, single-select).
- Free for personal repos.

Cons:

- Lives outside the repo. Not part of git diff history. Can drift from the
  markdown source of truth.
- Cannot model card-level fields like `lens`, `Counter direction`,
  `source quality`, or `IA1 gate state` without overloading single-select
  fields.
- "Session" concept does not map cleanly to issues.

Verdict: good for PR / issue tracking, weak for repo-internal artifact state.
Useful as a secondary view, not as the primary cockpit.

### Markdown Kanban (VS Code / Cursor extension)

Pros:

- Visualizes markdown files as Kanban directly inside the editor.
- Two-way sync, drag-and-drop between columns.
- File stays in git, so the markdown remains canonical.

Cons:

- Workflow is column-based, which fits cards but not milestones / sessions /
  source quality at the same time.
- One file = one board; would need separate boards for sessions, cards, etc.,
  losing the integrated cockpit view.

Verdict: nice for the cards lane (`outline -> draft -> ready -> scheduled ->
published`). Could be added later as a per-lane viewer, not as a replacement
for the dashboard.

### md2do (VS Code / Cursor extension)

Pros:

- Aggregated dashboard of markdown TODOs with stats (total / complete /
  overdue / due today).
- Task explorer sidebar with grouping by file, assignee, tag, priority.
- Optional Todoist sync.

Cons:

- Designed for TODO syntax inside markdown, not for the milestone /
  session / card schema this repo uses.
- Adds another schema to maintain on top of existing frontmatter.

Verdict: overkill for current scope. Skip unless we start producing many
`- [ ]` action items across files.

### TODO.md Editor / Taskboard

Pros:

- Lightweight, file-backed task views.
- Filtering, sorting, simple rendering.

Cons:

- No native concept of milestones, sessions, source quality, or gates.
- Largely the same trade-off as md2do.

Verdict: skip.

### Cursor Session Manager

Pros:

- Tracks Cursor chat sessions with status (`TODO`, `In Progress`, `PR Created`,
  `Merged`, etc.) and tagging.
- Associates branches with sessions.
- Exports as Markdown / JSON.

Cons:

- Scope is Cursor session lifecycle, not repo-level milestones or content
  pipeline.
- Would duplicate the session log files we already maintain under
  `ops/sessions/`.

Verdict: useful only if we find ourselves losing track of which chat goes
with which branch. Not a dashboard.

### Cursor Agents Window (built-in)

Pros:

- Native multi-workspace agent management; can run agents across local,
  cloud, remote SSH.
- Built-in PR review surface.

Cons:

- Operational, not strategic. Does not show milestone state or content card
  pipeline.

Verdict: complementary, but does not replace the cockpit.

### Notion / external doc app

Pros:

- Rich UI, easy linking.

Cons:

- Lives outside the repo. Cannot be a source of truth for a workflow that
  insists on git as the durable record.
- Hard to keep in sync with markdown frontmatter without an export pipeline.

Verdict: skip.

### Generated dashboard from markdown frontmatter

Pros:

- Avoids manual sync between `ops/current.md` and `ops/dashboard.html`.
- Can render milestone / session / card state from canonical frontmatter
  (e.g. via a small Python or Node script + GitHub Action).

Cons:

- Adds a build step. Current milestone says "static HTML, no JS, no
  framework, no external assets."
- Until manual maintenance actually hurts, generation is premature
  abstraction.

Verdict: hold for M4. If the manual cockpit becomes annoying to keep in
sync, the generator can be added as part of `M4 - Triggers and Collectors`.

## Decision Summary

```text
Primary cockpit:        ops/dashboard.html + ops/current.md  (repo-native)
Secondary, optional:    GitHub Projects                     (PR / issue view)
Optional later:         Markdown Kanban                     (cards lane only)
Future automation:      script-generated dashboard          (M4)
Skip:                   md2do, TODO.md Editor, Notion, Session Manager
```

Reconsider when any of these happens:

- Manual update of dashboard.html starts being skipped more than once.
- Sessions or cards grow beyond ~15 simultaneous active items.
- We start needing a public-facing status page.
