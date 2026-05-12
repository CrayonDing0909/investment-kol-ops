# Workflow Patterns

Purpose: define the canonical workflows used in this repo. Each workflow follows the
agentic harness defined in [docs/AGENTIC_HARNESS.md](AGENTIC_HARNESS.md).

Every workflow in this file follows the same shape:

- Trigger.
- Structured input.
- Programmatic checks.
- LLM role.
- Human gate.
- Output artifact.

If a real task does not map cleanly to one of these workflows, the agent must
either (a) compose two workflows in sequence, or (b) ask the human for a new
workflow definition before improvising.

## Index

- [Algorithm Research Workflow](#algorithm-research-workflow)
- [Audience Discovery Workflow](#audience-discovery-workflow)
- [Source Tutor Workflow](#source-tutor-workflow)
- [Investment Analysis Workflow](#investment-analysis-workflow)
- [Content Production Workflow](#content-production-workflow)
- [MVP Demo Workflow](#mvp-demo-workflow)
- [Postmortem Workflow](#postmortem-workflow)
- [Ship Workflow](#ship-workflow)

## Algorithm Research Workflow

Goal: learn what content earns distribution and why, without copying tactics blindly.
Aligns with [research/ALGORITHM_RESEARCH.md](../research/ALGORITHM_RESEARCH.md).

### Trigger

- "Study these competitor posts."
- "What is working on X / Threads / Shorts this week?"
- "Why did this post blow up?"

### Structured Input

Each candidate post must be captured with:

- Platform.
- Creator handle.
- URL or screenshot path.
- Topic.
- Hook (first 1-2 lines).
- Format (thread, chart, carousel, short video, etc.).
- Visible metrics: impressions, likes, replies, reposts, saves, follows.
- Date and time of post.
- Manually noted comments pattern.

### Programmatic Checks

- Reject entries missing platform, hook, or metrics.
- Tag posts by content pillar.
- Group by platform and time window before comparison.
- Sort by depth signal (saves, comments, DMs) separately from reach signal
  (impressions, reposts).

### LLM Role

- Classify hook archetype (pain, contrarian claim, framework, story, demo, list).
- Infer plausible reasons for performance.
- Suggest 3-5 adaptations that fit the account positioning, never blind copies.
- Flag tactics that conflict with [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md).

### Human Gate

- Required: approve which patterns are on-brand and ethical to adapt.
- Required: reject anything that promises returns, hides risk, or copies a
  competitor's specific claim.

### Output Artifact

- Update or create a swipe file entry.
- Produce 3-5 content hypotheses in the format used in
  `research/ALGORITHM_RESEARCH.md`.
- Record one explicit "do not adopt" item with reason.

## Audience Discovery Workflow

Goal: understand non-AI-agent users, then turn pain into MVP candidates and content
angles. Aligns with [research/AUDIENCE_DISCOVERY.md](../research/AUDIENCE_DISCOVERY.md).

### Trigger

- "I just had an interview, log it."
- "Cluster the pains we have so far."
- "Pick the next MVP from current evidence."

### Structured Input

For each interview or observation:

- Source: interview, DM, comment, support ticket, public post.
- User segment (per `CONTENT_STRATEGY.md`).
- Verbatim quotes.
- Current workaround.
- Tools they pay for.
- What would make them share a tool.
- Sensitivity flags (financial data, regulated info).

### Programmatic Checks

- Reject entries without a verbatim quote.
- Tag pain phrases.
- Count repeats across sources before clustering.
- Filter clusters that fail the MVP selection filter (no clear user, no 5-minute
  result, requires sensitive credentials, etc.).

### LLM Role

- Cluster pain statements into themes.
- Convert each theme into 1-2 MVP candidates and 1-2 content angles.
- Draft a one-line "promise" for each MVP candidate.
- Flag clusters that are interesting but unbuildable.

### Human Gate

- Required: choose which pain to build for next.
- Required: confirm sensitive data boundaries (no brokerage, no PII).

### Output Artifact

- Updated pain cluster doc.
- Ranked MVP candidate list with one-line promises.
- 3-5 content angles linked to the same pain.

## Source Tutor Workflow

Goal: help the user get better at reading primary and high-value secondary
sources. The workflow does not search for sources; it tutors already-selected
source material so the user can distinguish facts, management expectations,
forward-looking targets, and secondary interpretation before those claims enter
investment analysis or public content.

The workflow supports two reading modes:

- `single-source`: deep-read one selected source. Use for first contact.
- `cross-source-synthesis`: integrate multiple sources for one company,
  topic, or thesis. Use once 3+ relevant sources exist for the subject.

### Trigger

Single-source mode:

- "Teach me how to read this earnings call / filing / IR deck."
- "Run source tutor on this source packet."
- "Is this a fact, guidance, target, or interpretation?"
- "Help me verify whether this claim can be used in a public post."

Cross-source-synthesis mode:

- "What does our research actually say about <company>?"
- "Combine all sources for <topic> and tell me the integrated picture."
- "Cross-source tutor for <company / thesis>."
- "Do our sources support my prior belief that ...?"

### Structured Input

Each tutor run must capture:

- Source packet path or URL.
- Source quality: primary, secondary, or unverified.
- Source class: filing, earnings transcript, IR deck, press release, news,
  research paper, report, podcast, or creator note.
- Reading goal: learn domain context, verify a claim, extract numbers, prepare a
  brief, or public-source hardening.
- User's open questions.
- Claims or numbers the user is tempted to use.

### Programmatic Checks

- Reject a run without source metadata, date, publisher, and URL or local path.
- Do not search for new sources during the tutoring pass. Missing evidence becomes
  a follow-up task for the Source Collector Role.
- Extract all numbers with units, time periods, and source wording before
  interpretation.
- Tag each claim as one of:
  - `reported-fact`: historical or current fact directly stated by the source.
  - `management-expectation`: management's expectation, outlook, or commentary.
  - `forward-looking-target`: target, plan, aspiration, or long-range model.
  - `secondary-interpretation`: interpretation by media, analyst, podcast, or
    another non-primary source.
  - `agent-inference`: reasoning derived from source evidence but not stated by
    the source.
  - `open`: unclear or missing primary support.
- Flag wording that changes claim type, especially "is" vs "expects," "will" vs
  "targets," and current market share vs future target share.

### LLM Role

Use a tutoring mode adapted from `domain-doc-tutor`, not a summary mode.
Behavior differs by `reading_mode`.

#### Both Modes

- Explain what problem the source / set of sources is trying to answer.
- Separate sentences that are facts from sentences that are management
  expectations, forward-looking targets, or secondary interpretation.
- Flag numbers that should not be copied directly into public writing.
- List what the source / set still cannot answer and turn those gaps into
  follow-up source tasks.
- Produce four internalization artifacts that turn the source(s) into reusable
  material:
  - `Claim Ledger`: one row per claim with claim type, source wording, and safe
    public wording. In cross-source mode, add a `Strength` column.
  - `Mental Model Update`: 2-5 bullets that change how the user thinks about
    the company, industry, or thesis.
  - `Verification Watchlist`: the next data points or future sources that would
    confirm or invalidate the strongest claims.
  - `Reusable Output Block`: one paragraph the user can drop into a brief or
    article with claim types intact. In cross-source mode, the block covers the
    multi-line synthesis.

#### Single-Source Mode

- Explain how this class of source should generally be read (earnings release,
  IR deck, transcript, filing, news, paper, podcast), so the user can reuse the
  lens on other companies and industries.
- For every important sentence, walk the six-step reading chain:
  1. Exact source wording.
  2. Claim type tag (`reported-fact`, `management-expectation`,
     `forward-looking-target`, `secondary-interpretation`, `agent-inference`,
     `open`).
  3. What this sentence can support.
  4. What this sentence does not prove.
  5. Which metric or future event would verify or invalidate it.
  6. Where it should flow next (claim ledger, brief, article block, follow-up
     source).
- Identify the 5 sentences an investor should read most carefully.

#### Cross-Source-Synthesis Mode

- Add a `Cross-Source Synthesis Lens` section stating the 4 principles
  (independent evidence chain, source class hierarchy unchanged, no framing
  accumulation, no forward-looking upgrade across sources) plus reading rules
  specific to this company / topic.
- Use a `Thesis-Line Reading Chain`: one row per thesis line with supporting
  sources, strongest claim type, multi-source consistency, public-quotable
  flag.
- Add a `Sub-Thesis Breakdown` section when the subject has 3+ independent
  story lines.
- Add `What Each Source Adds That Others Don't` and `Sources 互相強化 /
  互相牴觸` sections.
- Map the user's prior beliefs to specific sources and mark strongest /
  weakest support.
- Identify the 5 thesis lines (not sentences) that matter most.

### Human Gate

- Optional for internal learning notes.
- Required before promoting any source-tutor output into public investment
  content if the output supports a market, company, strategy, or position-related
  claim.
- Required if the source distinction changes the thesis materially, for example
  correcting "current share" into "forward-looking market-share target."

### Output Artifact

- Markdown tutor note (canonical source):
  `research/source-tutor/<theme>/YYYY-MM-DD_<source-id>_reading.md`.
  In cross-source mode, use a `<subject>-cross-source` style source-id or a
  `<subject>-v<n>` versioned name; set `supersedes:` in the frontmatter when
  the run replaces or extends a previous note.
- HTML reading view (mandatory, not optional):
  `research/knowledge/<theme>/readings/<source-id>.html`.
  The user reads HTML first; markdown is the fallback. A tutor run is not
  considered complete until the HTML view is shipped and linked from the
  theme `readings/index.html` (and the main theme index when appropriate).
- Updates to the relevant source checklist or brief only after the claim type is
  explicitly marked.
- The note must always contain four `Internalization Artifacts` (claim ledger,
  mental model update, verification watchlist, reusable output block) and a
  `Downstream Routing` section.
- Single-source notes must also contain a `Reading Lens` (single) and a
  sentence-level `Source Map`.
- Cross-source notes must also contain a `Cross-Source Synthesis Lens`, a
  thesis-line `Source Map`, a `Sub-Thesis Breakdown` (when applicable),
  `What Each Source Adds That Others Don't`, and `Sources 互相強化 /
  互相牴觸`.
- A note that only produces "safe wording" without the reading chain is
  incomplete in either mode.

## Investment Analysis Workflow

Goal: produce repeatable, auditable market analysis suitable for public content.
Aligns with [research/INVESTMENT_ANALYSIS_PLAYBOOK.md](../research/INVESTMENT_ANALYSIS_PLAYBOOK.md)
and [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md).

### Trigger

- "Do this week's market analysis."
- "Analyze this news event."
- "Review this strategy or backtest."

### Structured Input

- Question being asked.
- Time horizon.
- Asset universe.
- Data inputs: macro, breadth, leadership, news, technicals, sentiment.
- Source for each data point.
- Position or watchlist conflicts.

### Programmatic Checks

- Validate ticker notation, units, dates, and day-of-week consistency.
- Run available trading skills first (see Skill Mapping in the playbook):
  market-environment, macro-regime-detector, market-breadth-analyzer,
  uptrend-analyzer, market-top-detector, theme-detector, market-news-analyst,
  technical-analyst, scenario-analyzer, backtest-expert, data-quality-checker.
- Block analysis if data quality issues are flagged.

### LLM Role

- Synthesize regime, breadth, leadership, news, technicals, sentiment.
- Produce scenarios with explicit invalidation conditions.
- Draft a public post version using the playbook's public template.
- Detect certainty language and weak sourcing in its own draft.

### Human Gate

- Required before publishing any market claim.
- Required before publishing any position-related content.
- Required before publishing any backtest or strategy claim.

### Output Artifact

- Internal analysis brief.
- Public post draft following the playbook template.
- Source checklist with each claim mapped to a source.
- Invalidation list: what would change my mind.

## Content Production Workflow

Goal: take a content hypothesis and ship a finished post or asset.
Aligns with [content/CONTENT_OPERATING_SYSTEM.md](../content/CONTENT_OPERATING_SYSTEM.md)
and [docs/CONTENT_STRATEGY.md](CONTENT_STRATEGY.md).

### Trigger

- "Plan this week's content."
- "Draft a post about X."
- "Repurpose this analysis into a thread / short / carousel."

### Structured Input

- Content brief fields (date, platform, audience, pain point, pillar, hypothesis,
  hook, main idea, evidence, visual asset, CTA, risk note, success metric).
- Source artifact: an analysis brief, MVP demo, postmortem, or interview cluster.
- Platform format constraints.

### Programmatic Checks

- Reject briefs missing audience, hook, or success metric.
- Check publish calendar for overlap or cadence drift.
- Check whether the post draws on a high-risk topic that needs the investment
  analysis workflow first.

### LLM Role

- Draft 2-3 hook variants.
- Draft body text adapted to the platform.
- Suggest a visual asset and a one-line caption.
- Run the review checklist from `CONTENT_OPERATING_SYSTEM.md` against its own draft.

### Human Gate

- Required for high-risk content per [docs/HUMAN_GATES.md](HUMAN_GATES.md).
- Optional for low-risk educational posts, but a quick human read is recommended.

### Output Artifact

- Final draft saved under `content/drafts/` with date-first naming.
- Asset brief.
- Schedule entry.
- Pre-publish checklist completed.

## MVP Demo Workflow

Goal: turn a chosen pain into a small, shippable demo without building a real
product yet. Aligns with [mvp/MVP_LAB.md](../mvp/MVP_LAB.md).

### Trigger

- "Spec the next demo."
- "Build a small version of this pain."
- "Decide whether to keep, improve, or kill demo X."

### Structured Input

- Pain statement and quote.
- Target user.
- Current workaround.
- Promise: one sentence outcome under 5 minutes.
- Input fields and output fields.
- Data sources, including any that need credentials.
- Trust and safety concerns.
- Build scope and explicit non-goals.

### Programmatic Checks

- Reject if it requires brokerage credentials or sensitive PII.
- Reject if the demo cannot be shown in a single post or short video.
- Reject if there is no clear feedback question.

### LLM Role

- Draft the MVP spec using the template in `MVP_LAB.md`.
- Draft the demo flow.
- Draft the launch post that pairs with the demo.
- Suggest a kill criterion based on observed feedback.

### Human Gate

- Required: approve scope and safety boundaries before any code is written.
- Required: approve any change that adds account integrations, payments, or
  storage of user data.

### Output Artifact

- MVP spec stored under `mvp/`.
- Build milestone list.
- Companion launch-post brief in `content/drafts/`.
- Defined kill criterion and review date.

## Postmortem Workflow

Goal: convert wrong calls, missed scenarios, or weak experiments into structured
learning. Used by both investment analysis and content/MVP areas.

### Trigger

- "This call did not age well."
- "This experiment underperformed."
- "This demo did not get traction."

### Structured Input

- Original artifact (post, analysis, MVP spec).
- Original hypothesis and success metric.
- Observed outcome with data and timestamps.
- Decision points along the way.

### Programmatic Checks

- Pull metrics from the metrics tracker.
- Confirm the original artifact still exists and was not edited after publishing.

### LLM Role

- Reconstruct what was assumed, observed, and decided.
- Identify where the assumption broke.
- Suggest a guardrail update for the relevant playbook or workflow.

### Human Gate

- Required before publishing a public postmortem (counts as high-risk content).
- Required to update playbooks, since changes to defaults affect future workflows.

### Output Artifact

- Postmortem note saved with the original artifact.
- Optional public postmortem draft.
- Suggested edits to playbooks or workflow patterns.

## Ship Workflow

Goal: turn finished work into clean git history. Runs at the end of any other
workflow when an artifact is ready to be saved. Aligns with the branch and
commit strategy in [docs/IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md).

This workflow exists because the agent does not know on its own whether to
commit directly to `main`, open a branch, push, or wait. It also drafts the
commit message in the conventional format used in this repo.

### Trigger

- Any other workflow has produced an artifact and the user signals they are
  done with the current task.
- The user says "ship", "commit", "收尾", or invokes `/ship` (when added).
- A working session is wrapping up and there are uncommitted changes.

### Structured Input

- `git status --short` output.
- `git diff --stat` output.
- Files grouped by area: `docs/`, `scripts/`, `mvp/`, `content/`, `research/`,
  `ops/`, `.cursor/`, root.
- Change-type classification: docs, content, script, mvp, chore, fix.
- Current branch name and remote tracking status.

### Programmatic Checks

- Reject if there is nothing to commit.
- Refuse to operate on detached HEAD without explicit user instruction.
- Refuse to commit files that look like secrets (`.env*`, credential JSON,
  private keys).
- Verify any file referenced as an artifact actually exists.

### LLM Role

- Decide direct-to-`main` vs branch using the rules in
  `IMPLEMENTATION_PLAN.md`.
- Group files into one or more logical commits if the diff mixes concerns.
- Draft conventional commit messages (`feat:`, `docs:`, `script:`, `mvp:`,
  `fix:`, `refactor:`, `chore:`).
- Suggest a branch name if a branch is needed.
- Suggest whether to push, and to which branch.

### Human Gate

- Mandatory: never commit, never push, and never create a branch without the
  user's explicit approval, even if rules say it is safe.
- Show the user the proposed git plan as a single block: branch decision,
  staged files, commit message(s), push targets.
- Decisions: approve, edit, reject.
- For pushes to `main`, require an extra confirmation.

### Output Artifact

- Actual `git commit` and optional `git push`.
- One line appended to the Progress Log in
  [docs/IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md).
- For new branches, a self-PR opened on GitHub when the user requests one.

## Composing Workflows

Most real tasks chain workflows. Examples:

- Weekly publish run: investment-analysis → content-production → ship.
- Source-backed theme learning: source-tutor → investment-analysis → content-production → ship.
- Demo launch: audience-discovery → mvp-demo → content-production → ship.
- Competitor sweep: algorithm-research → content-production → ship.
- Wrong call recovery: postmortem → content-production (transparent post) →
  playbook update → ship.

The agent must declare the chain at the start of the task and update if reality
forces a change in order. The ship workflow is always the final link when there
are file changes.
