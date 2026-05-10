# Analysis Skill Mapping

How [research/INVESTMENT_ANALYSIS_PLAYBOOK.md](../research/INVESTMENT_ANALYSIS_PLAYBOOK.md)
analysis steps map to concrete trading skills under `~/.claude/skills/trading/`.

The mapping has two profiles because broad-market and theme deep-dive workflows
need different skill sets. Pick one per workflow run, do not mix.

## Profile A: Theme Deep Dive (M1 default)

For the AI Server Supply Chain workflow and any future theme deep dive
(`investment-analysis` workflow with a `theme` field set).

| Order | Playbook step | Skill | Output expected |
|------:|---------------|-------|-----------------|
| 1 | Theme rotation | `~/.claude/skills/trading/theme-detector` | Lifecycle (emerging / accelerating / mature / decaying), key tickers, dominant narrative. |
| 2 | News catalysts | `~/.claude/skills/trading/market-news-analyst` | Last ~10 days of theme-relevant news with impact ranking and source. |
| 3 | Technical structure | `~/.claude/skills/trading/technical-analyst` | Weekly chart structure for the 2-3 anchor tickers only. M1 stays surface-level. |
| 4 | Scenarios | `~/.claude/skills/trading/scenario-analyzer` | 18-month bull/base/bear with explicit invalidation. |
| 5 | Pre-publish gate | `~/.claude/skills/trading/data-quality-checker` | Numbers / dates / units / instrument notation flags before IA1. |

### Constraints

- Each skill writes structured findings to the brief, not long prose.
- Anything the skill says becomes a "claim" in `source-checklist.md`.
- If a skill output cannot be verified, mark `confidence: uncertain` in the brief.

## Profile B: Broad Market (M2+ when needed)

For weekly broad-market environment briefs (regime, breadth, leadership). Not
used in M1.

| Order | Playbook step | Skill |
|------:|---------------|-------|
| 1 | Macro regime | `~/.claude/skills/trading/macro-regime-detector` |
| 2 | Market breadth | `~/.claude/skills/trading/market-breadth-analyzer` |
| 3 | Uptrend health | `~/.claude/skills/trading/uptrend-analyzer` |
| 4 | Top risk / distribution | `~/.claude/skills/trading/market-top-detector` |
| 5 | Synthesizer | `~/.claude/skills/trading/market-environment-analysis` |

## Deferred (not used until later milestones)

| Skill | Why deferred | Earliest milestone |
|-------|--------------|--------------------|
| `~/.claude/skills/trading/portfolio-manager` | Personal position content needs Gate IA1 + position disclosure rules. | M3+ |
| `~/.claude/skills/trading/position-sizer` | Same. | M3+ |
| `~/.claude/skills/trading/backtest-expert` | Strategy / backtest claims trigger Gate IA2. | M4+ |
| `~/.claude/skills/trading/edge-*` | Edge-finding pipeline; relevant for trade-hypothesis-ideator content. | M4+ |
| `~/.claude/skills/trading/macro-regime-detector` (in Profile B) | Broad-market not the M1 audience focus. | M2+ |
| `~/.claude/skills/trading/signal-postmortem` | Postmortem workflow. | M3+ |

## Run-time Convention

- The agent always declares which profile it is using before calling skills.
- The agent records which skill produced which finding, captured in
  `source-checklist.md` under `Source` column with a value like
  `skill:theme-detector` or `skill:market-news-analyst`.
- If a skill is unavailable in the current environment, the agent must mark the
  corresponding finding as `confidence: uncertain` and note `skill missing` in
  the source checklist, instead of fabricating output.
