---
workflow: investment-analysis
artifact_type: source-packet
risk: medium
created_at: 2026-05-13
theme: ai-server-supply-chain
layer: component-cooling
company: NVIDIA, Vertiv, Asia Vital Components (奇鋐), Auras Technology (雙鴻), Sunon (建準), Foxconn
ticker: NVDA, VRT, 3017.TW, 3324.TW, 2384.TW, 2354.TW
source_class: report + news
source_quality: high-quality-secondary
status: draft
---

# Source Packet: NVIDIA GB200/GB300 Liquid Cooling Supply Chain

## Source Metadata

- Source class: report + news
- Source quality: high-quality-secondary
- Title (multi-source):
  - "NVIDIA B 系列 GPU 放量在即！液冷散熱供應鏈迎來爆發成長，深入剖析奇鋐、雙鴻和建準成長潛力" — Vocus 產業研究報告
  - "英伟达GB200、GB300散热系统成本分析及核心供应链" — EE Times China
  - "英伟达 GB300单柜比黄金还贵？全面解析其散热系统" — LianLi Work
  - "2026 NVIDIA展望：GB300主流化與液冷趨勢" — TrendForce
  - "Nvidia Corp's GB300 platform to lead AI servers for this year" — Taipei Times
- Publisher: Vocus, EE Times China, LianLi Work, TrendForce, Taipei Times
- Date published: 2025-Q4 to 2026-Q1 range
- URL:
  - <https://vocus.cc/article/6760e08dfd897800011ad609>
  - <https://www.eet-china.com/mp/a468082.html>
  - <https://cn.lianliwork.com/news/nvidia-gb300-liquid-cooling-cost-breakdown-2026>
  - <https://www.trendforce.com.tw/research/download/RP260226EZ>
  - <https://www.taipeitimes.com/News/biz/archives/2026/01/20/2003850873>
- Captured at: 2026-05-13

## Why This Source Matters

Cooling has been flagged `needs follow-up` in our theme map since M1. This
packet closes that gap. Key insight: cooling is no longer a marginal BOM line;
in GB300 NVL72 it accounts for ~42% of total $600K rack cost. Liquid cooling
adoption crossing 50% of AI chips in 2026 makes this a structural — not
cyclical — investment theme.

Also clarifies which Taiwanese suppliers are core (奇鋐 / 雙鴻) vs more
peripheral.

## Raw Facts

- GB200 NVL72 (2025): ~$41,500 cooling BOM per rack.
- GB300 NVL72 (2026): ~$49,860 cooling BOM per rack, ~42% of total rack cost
  (~$600,000).
- Cooling system 4 critical components:
  - Cold plates: 40-45% of cost (~$40,680 for full tray system); high-purity
    copper with precision microchannel engineering.
  - Coolant Distribution Units (CDU): 30-35% of cost; system "heart".
  - Quick Disconnect Couplers (UQD): 15-20% of cost. GB300 reduces per-unit
    cost from $80 to $45 via miniaturization (NVUQD03 standard), though
    total quantity doubles.
  - Manifolds & tubing: 5-10% of cost.
- Vertiv: primary liquid cooling cabinet provider, 35%+ value share in the
  liquid cooling ecosystem.
- 雙鴻 (Auras Technology, 3324.TW): manifold systems and liquid cooling
  solutions.
- 奇鋐 (Asia Vital Components / AVC, 3017.TW): cold plates, 30%+ market share.
- GB300 expected to dominate 70-80% of global AI server rack shipments in
  2026.
- Liquid cooling adoption projected to surpass 50% penetration among AI chips
  by 2026.
- Both air-to-liquid and liquid-to-liquid cooling designs actively deployed.
- 建準 (Sunon, 2384.TW): fan systems, peripheral to liquid cooling but
  relevant to hybrid AI server designs.

## Claim Classification

| Exact source wording | Plain meaning | Claim type | Confidence |
|----------------------|---------------|------------|------------|
| GB200 NVL72 ~$41,500 cooling BOM | reported BOM | reported-fact (secondary) | inferred |
| GB300 NVL72 ~$49,860 cooling BOM, ~42% of $600K rack | reported BOM | reported-fact (secondary) | inferred |
| Cold plates 40-45% / CDU 30-35% / UQD 15-20% / manifolds 5-10% | cost structure breakdown | reported-fact (secondary) | inferred |
| UQD per-unit $80 → $45 in GB300 (NVUQD03) | reported design change | reported-fact (secondary) | inferred |
| Vertiv 35%+ ecosystem value share | reported share estimate | secondary-interpretation (third-party estimate) | inferred |
| 奇鋐 cold plate ~30%+ market share | reported share estimate | secondary-interpretation | inferred |
| GB300 → 70-80% of 2026 AI server rack shipments | forecast | forward-looking-target (industry estimate) | uncertain |
| Liquid cooling >50% AI chip penetration in 2026 | forecast | forward-looking-target (industry estimate) | uncertain |

## Key Numbers

| Number | Unit | Metric | Period | Source wording |
|--------|------|--------|--------|----------------|
| 41,500 | USD | GB200 NVL72 cooling BOM per rack | 2025 | Vocus / EET China |
| 49,860 | USD | GB300 NVL72 cooling BOM per rack | 2026 | Vocus / EET China |
| ~42 | % | cooling % of total GB300 rack cost | 2026 | Vocus |
| 600,000 | USD | GB300 NVL72 total rack cost | 2026 | LianLi Work |
| 40-45 | % | cold plate share of cooling cost | 2026 | EET China |
| 30-35 | % | CDU share of cooling cost | 2026 | EET China |
| 15-20 | % | UQD share of cooling cost | 2026 | EET China |
| 80 → 45 | USD | UQD per-unit price evolution GB200 → GB300 | 2025 → 2026 | EET China |
| 35+ | % | Vertiv ecosystem value share | 2026 | EET China |
| 30+ | % | 奇鋐 cold plate market share | 2026 | Vocus |
| 70-80 | % | GB300 share of 2026 AI server rack shipments | 2026 | Taipei Times / TrendForce |
| 50+ | % | liquid cooling penetration in AI chips | 2026 | Vocus / TrendForce |

## Direct Quotes

- "GB300 NVL72 cooling cost reaches approximately $49,860 per rack, about 42% of the total rack value." — EE Times China.
- "GB300 platform expected to dominate 70-80% of global AI server rack shipments in 2026." — TrendForce.
- "Vertiv controls 35%+ of value in the liquid cooling ecosystem." — EE Times China.

## Source Reliability Notes

- Vocus is Taiwan-focused industry research; useful for Taiwan supplier
  attribution.
- EE Times China + LianLi Work provide cost-structure analysis (good for BOM
  modeling).
- TrendForce + Taipei Times for industry forecast.
- All sources are high-quality-secondary. No primary press release from
  NVIDIA or Vertiv quoted directly; cost numbers are industry-analyst
  reconstructions.
- For public quoting, supplement with NVIDIA GTC keynote (which discusses
  cooling) or Vertiv quarterly investor presentations.
- Caveat: Taiwan supplier "市占" estimates often vary across analyst sources;
  treat 30-35% style figures as approximate.

## Follow-up Needed

- Pull NVIDIA GTC 2026 keynote material on GB300 cooling architecture.
- Pull Vertiv quarterly earnings / IR commentary on liquid cooling backlog.
- Pull 奇鋐 / 雙鴻 / 建準 Q1 2026 法說 transcripts for NVDA platform exposure.
- Cross-check `建準` (Sunon) role: is it really peripheral to liquid cooling,
  or does it have a manifold / fan-hybrid story we're missing?
- Open: GB300 vs GB200 cooling BOM uplift attribution — how much is per-rack
  density (more GPUs) vs per-unit upgrade (cold plate redesign)?

## Linked Artifacts

- Theme map: integrates with
  [research/knowledge/ai-server-supply-chain/cooling.html](../../knowledge/ai-server-supply-chain/cooling.html)
  (currently `needs follow-up`, this packet closes the gap).
- Cross-references:
  - `research/sources/ai-server-supply-chain/reports/2026-05-13_ai-chip-supply-tightness-source-packet.md` (cooling supply also tightening)
  - `research/sources/ai-server-supply-chain/earnings/2026-05-10_amd-q1-2026-source-packet.md` (Meta Helios platform also rack-scale liquid-cooled)
