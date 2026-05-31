# Artifact System

The core unit of this project is the **artifact**, not the research brief. This
file defines what an artifact is, the tiers that decide how much human work each
one needs, and the lifecycle from idea to published, measured artifact.

Direction anchor: [docs/NORTH_STAR.md](NORTH_STAR.md).

## Definition

An artifact is a finance explainer that an audience can see, understand, save, and
share. A chart, a supply-chain node map, an ETF X-ray, a company card, an AI tool
demo, or a market map.

Research packets and briefs still exist, but they are now the research-quality
layer underneath artifacts, not the deliverable.

## Artifact types

1. Supply Chain Map
2. Company Card
3. ETF X-ray
4. AI Tool Demo
5. Market Map
6. Glossary Visual

These map to the pillars in [docs/NORTH_STAR.md](NORTH_STAR.md).

## Tiering: not everything needs a full brief

The biggest cause of fatigue is treating every idea like a full investment brief.
Use tiers to decide how much human POV is required.

| Tier | Use | Human POV required? | Default gate |
|------|-----|---------------------|--------------|
| L1 Signal Note | A clue, a news item, a chart idea | No | none |
| L2 Artifact Note | One chart, one supply-chain node, one ETF X-ray | 3-5 sentence human note | Gate A |
| L3 Research Brief | Could become a public long-form or product page | Full POV / invalidation | Gate A, or Gate B if directional |
| L4 Investment View | Specific single-stock direction, buy/sell judgment | Full POV + invalidation | Gate B (mandatory) |

Most public artifacts should live at L2. Only escalate to L3/L4 when the artifact
makes a directional or position claim.

Gates are defined in [docs/HUMAN_GATES.md](HUMAN_GATES.md): Gate A is the
lightweight artifact/educational publish gate; Gate B (IA1/IA2) is the heavy
investment-view gate.

## Artifact lifecycle

```text
Idea
-> Research
-> Sketch
-> Visual Draft
-> Source Check
-> Content Package
-> Publish
-> Measure
-> Iterate
```

## Definition of Done

An artifact is done when:

- [ ] It has one clear core question.
- [ ] It has one visual output.
- [ ] It has at least one data source.
- [ ] It has one human insight (not an investment recommendation).
- [ ] It has at least 2 public-content versions (e.g. Threads + IG carousel, or X + Shorts).
- [ ] It has a metrics tracking hook.

Use the lightweight spec in
[content/templates/artifact-brief.md](../content/templates/artifact-brief.md) to
start an L1/L2 artifact. Use
[content/templates/thesis-card.md](../content/templates/thesis-card.md) when the
artifact carries a thesis or directional claim (L3/L4).

## How existing repo work maps onto this model

This system is a reframing, not a rebuild. Existing work already fits:

- `content/cards/**` thesis cards are L3/L4 artifacts (they carry a Counter and
  often an investment claim).
- The thermal explainer series under
  `research/knowledge/ai-server-supply-chain/series/thermal/` is an L2 artifact
  series (educational, no direct buy/sell call).
- `research/knowledge/<theme>/**` HTML pages are the backbone library that
  artifacts link back to.
- `research/sources/**`, `research/intake/**`, and `research/notes/**` are the
  research-quality layer that feeds L2-L4 artifacts.

## First public artifact series: AI Server Supply Chain

The existing AI Server Supply Chain knowledge map becomes the first public
artifact series instead of a single research packet:

```text
EP1  AI Server is not just GPU: the full supply chain in one map
EP2  Does the CPU still matter inside an AI server?
EP3  Why ASIC became a second main line beyond GPU
EP4  Where is HBM / memory actually stuck?
EP5  Why cooling is an unavoidable step in AI servers
EP6  Why passive components draw fund attention
```

Each episode only needs: one map, one core question, three key points, a source
note, and no buy/sell advice. The thermal series already implements EP5; the rest
follow the same L2 pattern. Do not force a full brief on every episode.

## Anti-patterns

- Forcing every idea to L3/L4.
- Writing a full POV before the market has reacted to the artifact.
- Letting the research gate (Gate B) block educational artifacts that only need
  Gate A.
