---
artifact_type: session-status
created_at: YYYY-MM-DD
last_updated: YYYY-MM-DD
status: active | paused | handed-off | completed
---

# Session Status: <short name>

## Boundary

- Owner / session: <human-readable label>
- Workflow: <workflow name or intent>
- Branch / worktree: <branch name and path, or "shared workspace">
- Mode: read-only | draft-only | write-capable
- Started at: <timestamp>

## Goal

<One or two sentences describing the current task.>

## File Scope

Expected to touch:

- `<path>`

Must avoid:

- `<path>`

## Current Progress

- <completed or observed item>

## Files Touched

- `<path>` - <what changed and why>

## Blockers / Risks

- <blocker, overlap risk, or "none">

## Next Step

<The next concrete action for this session.>

## Handoff Note

<What another session should know before continuing this work. Include links to
artifacts, not raw transcript assumptions.>
