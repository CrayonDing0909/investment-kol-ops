# Owner Handoff Protocol

Purpose: make agent responses **owner-readable**, not git-status-first. When a
task reaches a point where the human (the repo owner) must decide something, the
agent must hand off with a plain-language **Owner Handoff Packet** before any
technical output.

Bilingual mirror: [docs/OWNER_HANDOFF_PROTOCOL.zh.md](OWNER_HANDOFF_PROTOCOL.zh.md).
This English file is the LLM-primary version.

## Why this exists

The owner should be able to understand the state of any task without reading a
git diff, a commit graph, or a file tree. Git is the storage layer, not the
communication layer. A response that opens with `git status` forces the owner to
reverse-engineer meaning. This protocol flips the order: **meaning first, machine
detail last.**

## When the protocol triggers

Produce an Owner Handoff Packet whenever **any** of these is true:

- A human gate applies (Gate A, IA1, IA2, MVP1, MVP2, AR1, AD1, PM1) and the
  decision is the human's.
- The agent is blocked and needs the owner to choose a path forward.
- A task produced file changes that the owner must approve before commit /
  publish / push.
- The owner asks "where are we", "what did you do", or "what should I do".
- A role defined in [docs/AGENT_ROLES.md](AGENT_ROLES.md) reaches a step that
  requires a human decision (see the role rule in that file).

If the task is trivial and fully reversible with no decision pending, a normal
short reply is fine. When unsure, produce the packet.

## The Owner Handoff Packet format

Use these six sections, in this order, in plain language. Default to the owner's
working language (Chinese for this repo) unless asked otherwise. Keep it
non-technical: no git verbs, no SHAs, no diff jargon in the body.

```md
## 1. Current Stage
- Track:            <which track, e.g. A-series artifact / research / MVP>
- Item:             <the specific item or ID>
- State:            <plain status, e.g. draft done, awaiting review>
- Gate:             <which gate + current decision (defer / pending / n/a)>
- Public status:    <draft / ready / scheduled / published / n/a>
- Your role now:    <one line: what only the human can do next>

## 2. What was created / changed in plain language
- <≤5 bullets, no git jargon, describe artifacts and meaning>

## 3. What you should review
- <≤3 files, priority order. For each: the one thing to look for.>

## 4. The decision you need to make now
- A. <option>
- B. <option>
- C. <option>
- Recommendation: <one option> — <one-sentence why>

## 5. What is NOT happening yet
- <explicit not-doing list: publish / push / gate approval / GitHub objects / scope expansion>

## 6. Next safest action
- <one sentence the owner can approve as-is>

---

### Appendix (technical, optional)
- git status / diff stat / commit SHA go HERE, never at the top.
```

## Rules

- **Meaning before machine.** The six sections come first. Git output, SHAs,
  diffs, and file trees go only in the Appendix at the end.
- **Three files max** in section 3. If more changed, group them and name the
  three that matter for the decision.
- **One recommendation.** Section 4 always names a single recommended option and
  why, even if the final choice is the owner's.
- **Name what is not happening.** Section 5 must restate the safety boundaries
  (no publish / push / gate approval / remote GitHub objects / scope creep)
  relevant to the task.
- **One approvable sentence.** Section 6 is a single sentence the owner can say
  "yes" to, with no ambiguity about what the agent will then do.
- **Do not flip gates or status inside a handoff.** A handoff reports state; it
  never approves a gate or sets `public_status: ready` on its own.
- **Honesty about saved state.** If the working tree is already clean / saved,
  say so plainly instead of implying a pending action.

## Where handoff records live

Most handoffs are conversational and do not need a file. For concurrent work,
session handoffs, or any decision the owner may revisit, save a record using
[ops/handoffs/_template.md](../ops/handoffs/_template.md) under `ops/handoffs/`.
This complements (does not replace) gate decision logs in `ops/decisions/` and
session status files in `ops/sessions/`.

## Relationship to other docs

- Gates and decisions: [docs/HUMAN_GATES.md](HUMAN_GATES.md),
  `ops/decisions/`.
- Roles that must hand off: [docs/AGENT_ROLES.md](AGENT_ROLES.md).
- Daily focus surface: [NEXT_ACTIONS.md](../NEXT_ACTIONS.md) (its top-level
  Current Stage block mirrors section 1 of this packet).
- Reading-surface rules for human-facing artifacts:
  [docs/HTML_READING_UI_GUIDE.md](HTML_READING_UI_GUIDE.md).
