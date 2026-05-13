# `ops/` — Operating Cockpit

Single place to track active milestones, sessions, cards, blockers, and PRs.
Open `ops/dashboard.html` in a browser; that is the cockpit you read first.

## File Map

```text
ops/
├── dashboard.html              GENERATED visual cockpit (open this in browser)
├── current.md                  GENERATED markdown summary (canonical, git-diffable)
├── build_dashboard.py          generator script (run after editing data)
├── data/
│   ├── now.toml                hero "next action" + do-not list
│   ├── milestones.toml         milestone state (done / active / todo)
│   └── blockers.toml           current blockers and decisions
├── templates/
│   └── dashboard.css           all styles for the dashboard
├── sessions/
│   ├── _index.md               session registry (drill-down)
│   └── 2026-05-13_session-*.md per-session logs (frontmatter drives dashboard)
├── decisions/
├── METRICS.md
├── AGENTIC_RUNBOOK.md
└── tooling-dashboard-options.md   tool / framework survey for the cockpit
```

`dashboard.html` and `current.md` are produced from data; do not edit them by
hand. Edit the data instead and re-run the generator.

## Quickstart

```bash
# rebuild dashboard
make dashboard

# rebuild + open in browser
make open-dashboard

# or invoke directly
python3 ops/build_dashboard.py
```

Zero third-party dependencies. Requires Python 3.11+ (uses stdlib `tomllib`).

## How To Update State

Decide where the change belongs:

| What changed? | Edit this | Then re-run |
|---|---|---|
| Hero "next action" or "do not" list | `ops/data/now.toml` | `make dashboard` |
| Milestone status (M1-M5) | `ops/data/milestones.toml` | `make dashboard` |
| Blockers (add / remove / re-word) | `ops/data/blockers.toml` | `make dashboard` |
| Session status, branch, scope, active card | frontmatter of `ops/sessions/<file>.md` | `make dashboard` |
| Card status, lens, counter | frontmatter of `content/cards/<file>.md` | `make dashboard` |
| Recently merged / open PRs | nothing — the script reads `gh pr list` live | `make dashboard` |

The dashboard derives:

- **Active milestone** = the milestone with `status = "active"` in
  `milestones.toml`.
- **Active session** = the first session with `status: active` in its
  frontmatter.
- **Active branch** = the `branch:` field on the active session
  (falls back to `git rev-parse --abbrev-ref HEAD`).
- **Active card** = the card whose id matches `active_card:` on the active
  session, otherwise the first card with `public_status: draft`.
- **Open / merged PRs** = live results from `gh pr list --json …` (skipped
  silently if `gh` is not available).

## Linking Strategy

Dashboard links use a mixed scheme so you can stay in one window:

- Source files (`.md`, `.py`, `.toml`, `.yaml`) open in Cursor via
  `cursor://file/<absolute path>`.
- HTML reading pages (`.html`) open in the browser via relative path.
- PR links go to GitHub.

Override the editor scheme if you prefer VS Code:

```bash
CURSOR_EDITOR_SCHEME=vscode python3 ops/build_dashboard.py
```

## Working Loop

```text
1. Open ops/dashboard.html in your browser. Read the Hero (top box).
2. Click the active session / card link — opens in Cursor.
3. Do exactly one next action on the active branch.
4. Update the relevant frontmatter or ops/data/*.toml file.
5. Run: make dashboard
6. Refresh the browser. Verify state reflects reality.
7. If you are about to open a new research branch or worktree → STOP,
   re-read the "do not" list in the Hero.
```

## When To Upgrade (Phase 2)

Move to a Vite + React + shadcn cockpit (Phase 2 in
[`tooling-dashboard-options.md`](./tooling-dashboard-options.md)) only after
one of these is true:

- You want drag-and-drop status changes.
- You want a command palette (Cmd+K) to jump between artifacts.
- The number of cards or sessions exceeds ~15 active at once.
- The dashboard needs to be hosted publicly.

Until then, keep this generator-based cockpit. It is intentionally small.
