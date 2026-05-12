---
workflow: investment-analysis
artifact_type: source-packet
risk: medium
created_at: 2026-05-13
theme: ai-server-supply-chain
layer: component-memory + procurement-and-tightness
company: SK Hynix, Samsung Electronics, Micron Technology, NVIDIA, TSMC
ticker: 000660.KS, 005930.KS, MU, NVDA, TSM
source_class: report + news
source_quality: high-quality-secondary
status: draft
---

# Source Packet: HBM Supply / Demand & HBM4 Race (2026)

## Source Metadata

- Source class: report + news
- Source quality: high-quality-secondary
- Title (multi-source):
  - "NVIDIA HBM4 Supply Becomes Three-Way Race" — ChosunBiz English
  - "SK hynix sees HBM demand outpacing supply for three years" — Korea Herald
  - "HBM4 and HBM4E: The Memory Wall Becomes the System Architecture Problem" — Atlas Peak Research
  - "SK Hynix presses ahead on HBM4 despite tightening AI memory supply" — DigiTimes
  - "HBM4 supply race intensifies as SK Hynix, Samsung speed up mass production" — DigitalToday
- Publisher: ChosunBiz, Korea Herald, Atlas Peak Research, DigiTimes, DigitalToday
- Date published: 2026-02 to 2026-03 range
- URL:
  - <https://www.chosun.com/english/industry-en/2026/02/18/3A2GI2LHQ5ARTAESKMOZAQ2SOI/>
  - <https://www.koreaherald.com/article/10723564>
  - <https://www.atlaspeakresearch.com/report/853205>
  - <https://www.digitimes.com/news/a20260318VL208/sk-hynix-hbm4-demand-hbm-production.html>
  - <https://www.digitaltoday.co.kr/en/view/789/hbm4-supply-race-intensifies-sk-hynix-samsung-electronics-speed-up-mass-production>
- Captured at: 2026-05-13

## Why This Source Matters

HBM (High Bandwidth Memory) is the single hardest-binding bottleneck in AI
server output. While Mercury / TrendForce track GPU shipment numbers, HBM
allocation determines who can actually deliver GPUs to customers. This packet
covers the Component-Memory layer (which Mercury / Mercury-style sources only
glance at) and Procurement & Tightness layer (HBM is the most-cited
constraint).

The packet also closes M2.1's HBM source gap — `index.html` has long flagged
HBM as `needs follow-up`.

## Raw Facts

- SK Hynix projects HBM demand will exceed supply for at least the next three
  years.
- Micron CFO stated the company can "only supply between half to two-thirds
  of the volume demanded by some key customers".
- Micron has halted general consumer PC memory production to focus on
  high-margin AI chip memory.
- HBM4 has more than 40% improved data transfer vs HBM3E.
- HBM4 doubles interface to 2,048-bit (HBM3E was 1,024-bit), uses 32-channel
  organization, reaches 2.048 TB/s per stack baseline.
- HBM4E (speed-extended variant) targets 4 TB/s per-stack throughput.
- 2026 HBM4 supply race: Samsung, SK Hynix, Micron all competing.
- SK Hynix currently leads with ~2/3 of NVIDIA's HBM4 volume allocated.
- Market analysis predicts Samsung will obtain certification first (product
  stability advantage); SK Hynix and Micron follow.
- Micron has begun shipping HBM4 and expects verification completion by Q2
  2026.
- Bottlenecks extend beyond DRAM fab to: TSV-enabled DRAM processing, base-
  die foundry capacity, interposer yield, CoWoS-class backend throughput,
  substrate materials, and system qualification.
- Rising DRAM prices have reduced relative HBM supply capacity (companies
  reallocate to more profitable DRAM).
- Micron is investing $50B in two new Boise, Idaho fabs to address shortages.
- SK Hynix plans HBM4E samples in H2 2026; mass production begin 2027.

## Claim Classification

| Exact source wording | Plain meaning | Claim type | Confidence |
|----------------------|---------------|------------|------------|
| "SK hynix sees HBM demand outpacing supply for three years" — Korea Herald | management forward outlook | management-expectation (SK Hynix CEO commentary) | known |
| "Micron can only supply between half to two-thirds of the volume demanded by some key customers" — Micron CFO | management-stated supply constraint | management-expectation (Micron CFO) | known |
| Micron halted general consumer PC memory production to focus on AI memory | reported operational change | reported-fact (secondary) | inferred |
| HBM4: 40%+ data transfer improvement; 2,048-bit interface; 2.048 TB/s/stack | technical spec | reported-fact (industry standard spec) | known |
| SK Hynix has ~2/3 of NVIDIA's HBM4 volume allocated | reported allocation | reported-fact (secondary; market analysis) | inferred |
| Samsung will obtain certification first | analyst expectation | secondary-interpretation (market analysis) | uncertain |
| Micron Q2 2026 verification completion target | management forecast | forward-looking-target | inferred |
| HBM bottlenecks include CoWoS / interposer / substrate / base-die | structural framing | secondary-interpretation (Atlas Peak Research) | known |
| Micron $50B investment in two Boise Idaho fabs | reported capex commitment | reported-fact | known |
| SK Hynix HBM4E mass production from 2027 | forward-looking plan | forward-looking-target | inferred |

## Key Numbers

| Number | Unit | Metric | Period | Source wording |
|--------|------|--------|--------|----------------|
| 3+ | years | HBM demand exceeds supply | 2026-2028+ | SK Hynix via Korea Herald |
| 50-67 | % | Micron supply vs key customer demand | 2026 | Micron CFO via ChosunBiz |
| 40+ | % | HBM4 data transfer improvement vs HBM3E | 2026 | Atlas Peak Research |
| 2,048 | bit | HBM4 interface width | 2026 | Atlas Peak |
| 2.048 | TB/s | HBM4 per-stack throughput baseline | 2026 | Atlas Peak |
| 4 | TB/s | HBM4E per-stack throughput target | 2027+ | Atlas Peak |
| ~67 | % | SK Hynix share of NVIDIA HBM4 allocation | 2026 | ChosunBiz |
| 50 | B USD | Micron Boise Idaho 2-fab investment | multi-year | ChosunBiz |
| 2026 Q2 | quarter | Micron HBM4 verification target | Q2 2026 | ChosunBiz |
| H2 2026 | period | SK Hynix HBM4E sampling | H2 2026 | Korea Herald |
| 2027 | year | SK Hynix HBM4E mass production | 2027 | Korea Herald |

## Direct Quotes

- "Demand will exceed supply for at least the next three years." — paraphrased from SK Hynix commentary (via Korea Herald).
- "Only supply between half to two-thirds of the volume demanded by some key customers." — Micron CFO (via ChosunBiz).
- HBM bottlenecks extend "beyond DRAM fabrication to include TSV-enabled DRAM processing, base-die foundry capacity, interposer yield, CoWoS-class backend throughput, substrate materials, and system qualification." — Atlas Peak Research.

## Source Reliability Notes

- Korea Herald, ChosunBiz, DigiTimes are industry-grade secondary sources with
  good track records on Korean / Taiwan semiconductor reporting.
- Atlas Peak Research is research-grade (think-tank style); useful for the
  multi-layer bottleneck framing.
- For public quoting of specific HBM allocation numbers (e.g. "SK Hynix
  ~2/3 of NVIDIA"), cross-check against TrendForce or company earnings.
- Primary upgrade paths: SK Hynix earnings call transcript (Q1 2026), Micron
  FY Q3 2026 earnings, Samsung memory business segment commentary.
- Forward-looking: HBM4 certification timing, HBM4E ramp, $50B Micron capex
  outcome — all subject to execution risk.

## Follow-up Needed

- Pull TSMC CoWoS capex / yield commentary (CoWoS is the explicit HBM
  packaging bottleneck).
- Pull Samsung Memory Business segment Q1 2026 commentary on HBM4
  certification status.
- Cross-check NVIDIA HBM4 allocation percentages against TrendForce
  publications.
- Verify Micron "half to two-thirds" against Micron earnings transcript.
- Open: how does HBM allocation specifically affect AMD Instinct vs NVIDIA
  Vera Rubin vs Google TPU?

## Linked Artifacts

- Theme map: integrates with
  [research/knowledge/ai-server-supply-chain/memory.html](../../knowledge/ai-server-supply-chain/memory.html)
  (needs HBM section update) and
  [research/knowledge/ai-server-supply-chain/hyperscaler-procurement.html](../../knowledge/ai-server-supply-chain/hyperscaler-procurement.html)
  (HBM 4x/yr demand growth already noted)
- Cross-references:
  - `research/sources/ai-server-supply-chain/reports/2026-05-13_ai-chip-supply-tightness-source-packet.md` (HBM cited as a bottleneck in CNAS)
  - `research/sources/ai-server-supply-chain/earnings/2026-05-10_amd-q1-2026-source-packet.md` (AMD Instinct ramp depends on HBM)
