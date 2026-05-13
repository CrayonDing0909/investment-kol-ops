---
artifact_type: sessions-index
created_at: 2026-05-13
last_updated: 2026-05-13T18:45+08:00
---

# Session Status Index

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
| [Session A — Source Tutor / AMD](./2026-05-13_session-a-source-tutor.md) | paused | Gap A PR #15 merged; Gap B PR #16 merged; log/infra on `chore/session-isolation-cowork` pending PR | AMD `>50% server CPU revenue share` gap closure + Q1 2026 primary-source upgrade; no active research branch | 2026-05-13T18:45+08:00 |
