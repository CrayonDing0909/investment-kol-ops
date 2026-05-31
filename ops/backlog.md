# Backlog (draft specs, not yet on GitHub)

> These are draft specs for GitHub milestones, issues, and a project board. They
> live in-repo on purpose. **Do not create remote GitHub objects from this file
> until the user approves a separate follow-up step.**
>
> Direction anchor: [docs/NORTH_STAR.md](../docs/NORTH_STAR.md). Artifact model:
> [docs/ARTIFACT_SYSTEM.md](../docs/ARTIFACT_SYSTEM.md). Milestone overlay:
> [docs/ROADMAP.md](../docs/ROADMAP.md).

> Milestone vocabulary: artifact-track milestones use the `A` prefix
> (A0.5, A1, ...) to stay distinct from the existing engineering / dashboard
> `M`-numbered milestones (M0-M6), which remain valid and unchanged. See
> [docs/ROADMAP.md](../docs/ROADMAP.md).

## Milestones (artifact-first)

```text
A0.5 Repo Refinement          - artifact-first overlay + operating layer (this PR)
A1   Artifact Engine MVP       - 5 publishable artifacts, each with source note + 2 public versions + metrics log
A2   Research Packet Lite       - deepen only the 2 best-performing A1 artifacts into source-backed packets
A3   Public Distribution Loop   - 4 weeks of steady weekly publishing + weekly review + metrics
A4   Landing Page + Private Traffic - one-page site, email signup, first lead magnet
A5   First Interactive Prototype - pick one (ETF X-ray / Supply Chain Map / Company Card), test with 10-30 people
```

Note: the deep source-backed research work (IMPLEMENTATION_PLAN M1.1/M1.2-style)
is reclassified as the research-quality layer under A2; it no longer blocks
public artifact testing.

## Starter issues (≈10)

```text
[A0.5] Add North Star                       -> docs/NORTH_STAR.md (done in A0.5 PR)
[A0.5] Add NEXT_ACTIONS                      -> NEXT_ACTIONS.md (done)
[A0.5] Add Artifact System                   -> docs/ARTIFACT_SYSTEM.md (done)
[A0.5] Add Weekly Review template            -> ops/weekly/_template.md (done)
[A0.5] Add distribution templates            -> content/templates/{ig-carousel,youtube-shorts,artifact-brief}.md (done)
[A0.5] Add two-tier gate (A vs B)            -> docs/HUMAN_GATES.md (done)
[A1]  Convert AI Server Supply Chain into public artifact series
[A1]  Create AI Server Supply Chain Map v0   (one-map overview, L2)
[A1]  Draft 3 Threads posts for AI Server series
[A1]  Create first weekly review + 24h post-publish log for first published artifact
```

First batch of A1 artifacts to consider:

```text
1. AI Server Supply Chain Map v0
2. CPU 在 AI Server 裡到底做什麼？
3. ASIC vs GPU vs CPU 一張圖
4. Cooling 在 AI Server BOM 裡的位置
5. 聯發科是主晶片還是周邊？一張圖看懂
```

## Project board columns (spec)

```text
Backlog -> This Week -> Today -> In Progress -> Review/Gate -> Published -> Measured
```

- `Review/Gate` distinguishes Gate A (artifact publish) vs Gate B (investment view).
- `Measured` requires a post-publish metrics log before an item is closed.

## Issue template (spec)

```md
## Why
## Output
## Scope
## Acceptance Criteria
## AI Instructions
## Done
```

## How to push to GitHub later (only after approval)

When approved, create milestones (`gh api` or `gh issue create --milestone`),
then create issues from the list above with the issue template body, then set up
the project board columns. Do not run any of this without explicit approval.
