---
workflow: investment-analysis
artifact_type: source-packet
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
company: AMD
ticker: AMD
source_class: earnings
source_quality: primary+secondary
status: draft
---

# Source Packet: AMD — Q1 2026 Earnings

## Source Metadata

- Company: Advanced Micro Devices, Inc.
- Ticker: AMD
- Source class: earnings
- Source quality:
  - primary: AMD Q1 2026 financial results press release
  - primary: AMD 2025 Financial Analyst Day press release
  - secondary: Motley Fool Q1 2026 earnings call transcript
- Title:
  - AMD Reports First Quarter 2026 Financial Results
  - AMD Unveils Strategy to Lead the $1 Trillion Compute Market and Accelerate Next Phase of Growth
  - AMD Q1 2026 Earnings Call Transcript
- Publisher:
  - AMD Newsroom
  - The Motley Fool Transcribing
- Date published:
  - 2026-05-05 (AMD press release)
  - 2025-11-11 (AMD Financial Analyst Day press release)
  - 2026-05-06 (Motley Fool transcript)
- URL:
  - https://www.amd.com/en/newsroom/press-releases/2026-5-5-amd-reports-first-quarter-2026-financial-results.html
  - https://www.amd.com/en/newsroom/press-releases/2025-11-11-amd-unveils-strategy-to-lead-the-1-trillion-compu.html
  - https://www.fool.com/earnings/call-transcripts/2026/05/06/amd-amd-q1-2026-earnings-call-transcript/
- Captured at: 2026-05-10

## Why This Source Matters

AMD is the cleanest primary source for the CPU revival anchor. It provides direct
numbers on Data Center growth, EPYC demand, server CPU TAM expansion, and why
agentic AI increases CPU compute needs alongside accelerators.

## Raw Facts

- Q1 2026 revenue was $10.253B, up 38% YoY.
- GAAP gross margin was 53%; non-GAAP gross margin was 55%.
- Data Center segment revenue was $5.8B, up 57% YoY.
- AMD said Data Center segment growth was driven by strong demand for AMD EPYC processors and the ramp of AMD Instinct GPU shipments.
- Meta plans to deploy up to 6GW of AMD Instinct GPUs, with a custom MI450-based GPU and AMD EPYC Venice CPUs in the Helios rack-scale platform.
- AMD said AWS, Google Cloud, Microsoft Azure, and Tencent announced new or expanded 5th Gen EPYC-powered cloud instances.
- AMD Q2 2026 revenue guidance is approximately $11.2B +/- $300M, about 46% YoY growth at the midpoint.
- In the transcript, Lisa Su said Data Center revenue increased 57% YoY to a record $5.8B, led by EPYC CPUs and Instinct GPUs.
- Server CPU revenue increased more than 50% YoY in Q1.
- EPYC-powered cloud instances increased nearly 50% YoY to more than 1,600.
- AMD said inference and agentic AI are increasing server CPU compute requirements because these workloads require orchestration, data movement, and parallel execution, in addition to CPU head-node roles for GPUs and accelerators.
- AMD now expects server CPU TAM to grow at greater than 35% annually, reaching over $120B by 2030.
- AMD now expects server CPU revenue to grow more than 70% YoY in Q2 2026.
- AMD expects tens of billions of dollars in annual Data Center AI revenue in 2027.
- AMD Financial Analyst Day 2025 press release says AMD is positioned to lead the server market and expects to achieve more than 50% server CPU revenue market share.

## Key Numbers

| Number | Unit | Metric | Period | Source wording |
|--------|------|--------|--------|----------------|
| 10.253 | B USD | Total revenue | Q1 2026 | Press release: revenue was $10.253B, up 38% YoY |
| 38 | % YoY | Total revenue growth | Q1 2026 | Press release |
| 5.8 | B USD | Data Center revenue | Q1 2026 | Press release / transcript |
| 57 | % YoY | Data Center revenue growth | Q1 2026 | Press release |
| > 50 | % YoY | Server CPU revenue growth | Q1 2026 | Transcript |
| > 1,600 | count | EPYC-powered cloud instances | Q1 2026 | Transcript |
| > 35 | % CAGR | Server CPU TAM expected growth | 3-5 years / to 2030 | Transcript |
| > 120 | B USD | Server CPU TAM | 2030 | Transcript |
| > 70 | % YoY | Expected server CPU revenue growth | Q2 2026 | Transcript |
| > 50 | % | Server CPU revenue market share target | 3-5 years | AMD Financial Analyst Day 2025 press release |
| 11.2 | B USD | Q2 2026 revenue guidance midpoint | Q2 2026 | Press release / transcript |
| 6 | GW | Meta AMD Instinct GPU deployment plan | multi-year | Press release |

## Direct Quotes

- "We are seeing strong momentum as inferencing and agentic AI drive increasing demand for high-performance CPUs and accelerators." — Lisa Su, AMD press release.
- "Data Center segment revenue was $5.8 billion, up 57% year-over-year, driven by strong demand for AMD EPYC processors and the continued ramp of AMD Instinct GPU shipments." — AMD press release.
- "Inferencing and Agentic AI are increasing the need for server CPU compute as these workloads require additional CPU processing for orchestration, data movement and parallel execution in addition to serving as the head nodes for GPUs and accelerators." — Lisa Su, transcript.
- "We now expect the server CPU TAM to grow at greater than 35% annually, reaching over $120 billion by 2030." — Lisa Su, transcript.
- "We now expect server CPU revenue to grow by more than 70% year-over-year in the second quarter." — Lisa Su, transcript.
- "As AMD extends its multi-generational AMD EPYC CPU portfolio, it is positioned to lead the server market and expects to achieve more than 50% server CPU revenue market share." — AMD Financial Analyst Day 2025 press release.

## Source Reliability Notes

- Primary source: AMD press release. Strong for reported financials, segment results, product announcements, and guidance.
- Secondary source: Motley Fool transcript. Useful for management quote extraction, but publish-facing claims should eventually be cross-checked against AMD IR audio/transcript or SEC filings.
- Forward-looking statements: Q2 guidance, TAM growth, server CPU revenue growth, Data Center AI 2027 revenue, MI450/Helios customer forecasts.
- The `>50% server CPU revenue market share` claim is primary-source backed by AMD Financial Analyst Day 2025, but remains a forward-looking target rather than achieved share.

## Follow-up Needed

- Verify whether the EP659 note "AMD 法說估 120B 年增超過 35%" referred to server CPU TAM by 2030, not AMD total revenue in 2026. The AMD primary source supports `server CPU TAM > $120B by 2030`, not `AMD 2026 revenue = $120B`.
- Pull AMD Q1 2026 8-K or earnings slides from SEC/IR for primary transcript-like support.
- If publishing, word the share claim as a forward-looking AMD target: `AMD expects to achieve >50% server CPU revenue market share`, not as current share.

## Linked Artifacts

- Intake note: `research/intake/2026-05-10_amd-q1-2026_cpu.md`
- Knowledge page updated: `research/knowledge/ai-server-supply-chain/cpu.html`
- Briefs citing this packet: `research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md`
