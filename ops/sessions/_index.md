---
artifact_type: sessions-index
created_at: 2026-05-13
last_updated: 2026-05-14T22:30+08:00
---

# Session Status Index

> **Read first**: open the [Now Page (HTML cockpit)](../dashboard.html) or its
> markdown canonical [`ops/current.md`](../current.md) before this index.
> The Now Page tells you the active milestone, branch, task, and what not to
> start. This file is the deeper drill-down into individual sessions.

Use this folder when multiple Cursor sessions, agents, worktrees, or cloud agents
are active around the same repo.

## Why This Exists

Chat transcripts are not the operating record. The durable record is the repo:
files, diffs, branches, worktrees, and explicit status artifacts. A session status
file makes concurrent work visible without requiring one agent to read another
agent's private chat history.

## When To Create A Status File

Create `ops/sessions/YYYY-MM-DD_<short-task>.md` when:

- Two or more sessions may edit this repo at the same time.
- A task spans more than one chat or agent.
- A session touches system-affecting files such as `.cursor/rules/**`,
  `AGENTS.md`, workflow docs, or shared templates.
- A handoff is needed before commit, merge, or review.

Use `ops/templates/session-status.md` as the template.

## Status Values

- `active`: currently being worked on.
- `paused`: waiting for user input, external result, or another session.
- `handed-off`: ready for another session to continue.
- `completed`: work is done and ship check has been summarized.

## Operating Rules

- Prefer separate worktrees or cloud agent branches for two write-capable
  sessions.
- Keep status files short. Link to artifacts and diffs instead of pasting long
  transcripts.
- Update the file when goal, file scope, branch, blocker, or handoff state
  changes.
- Do not use status files to bypass human gates for publishing, investing,
  launching, committing, or pushing.

## Active Sessions

| Session | Status | Branch / Worktree | Scope | Last Updated |
|---|---|---|---|---|
| [Session A — Source Tutor / AMD](./2026-05-13_session-a-source-tutor.md) | paused | Gap A PR #15 merged; Gap B PR #16 merged; no active research branch | AMD `>50% server CPU revenue share` gap closure + Q1 2026 primary-source upgrade | 2026-05-13T18:45+08:00 |
| [Session B — Thesis Cards Scaffold](./2026-05-13_session-b-thesis-cards.md) | completed | PR #14 merged to `main` | Thesis-card template + 6 outline cards scaffolded | 2026-05-13T18:58+08:00 |
| [Session C — Card #001 Cooling BOM](./2026-05-13_session-c-card-001.md) | completed | `feat/card-001-learning-ready` | Card #001 moved from outline to IA1-approved ready state; not yet published | 2026-05-14T22:30+08:00 |
