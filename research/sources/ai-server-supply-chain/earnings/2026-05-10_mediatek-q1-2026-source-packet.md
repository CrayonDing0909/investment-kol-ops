---
workflow: investment-analysis
artifact_type: source-packet
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
company: MediaTek
ticker: 2454.TW
source_class: earnings
source_quality: primary+secondary
status: draft
---

# Source Packet: MediaTek — Q1 2026 + AI ASIC Visibility

## Source Metadata

- Company: MediaTek Inc.
- Ticker: 2454.TW
- Source class: earnings
- Source quality:
  - primary: MediaTek financial information page (Q1 2026 links + monthly revenue table)
  - secondary: Alpha Spread Q1 2026 earnings call summary
  - secondary: Futurum Q1 FY 2026 analysis citing management commentary
- Title:
  - MediaTek Financial Information
  - MediaTek Inc Q1-2026 Earnings Call
  - MediaTek Q1 FY 2026 Earnings Driven by AI ASIC Ramp Visibility
- Publisher:
  - MediaTek Investor Relations
  - Alpha Spread
  - Futurum
- Date published:
  - 2026-04-30 Q1 earnings event (from MediaTek IR page)
  - 2026-05-07 Futurum article
- URL:
  - https://www.mediatek.com/investor-relations/financial-information?hsLang=en
  - https://www.alphaspread.com/security/twse/2454/investor-relations/earnings-call/q1-2026
  - https://futurumgroup.com/insights/mediatek-q1-fy-2026-earnings-driven-by-ai-asic-ramp-visibility/
- Captured at: 2026-05-10

## Why This Source Matters

MediaTek is the Taiwan anchor for the AI server supply-chain story. EP659 framed
it as a company with market excitement but still needing proof: currently more
I/O / memory subsystem and ASIC exposure than true server CPU main silicon.
This source packet checks that narrative against reported revenue, monthly
revenue, and AI ASIC ramp commentary.

## Raw Facts

- MediaTek IR page lists 2026 Q1 materials: earnings call invitation, presentation, press release, financial statements, and transcript.
- MediaTek 2026 monthly revenue:
  - Jan: NT$46.977B, -8.15% YoY.
  - Feb: NT$38.954B, -15.63% YoY.
  - Mar: NT$63.219B, +12.90% YoY.
  - Apr: NT$46.737B, -4.14% YoY.
  - YTD Apr: NT$195.887B, -3.06% YoY.
- Alpha Spread summary says Q1 2026 revenue was NT$149.2B, down 0.7% sequentially and down 2.7% YoY.
- Alpha Spread summary says gross margin was 46.3%, operating margin was 15.3%, net income was NT$24.4B.
- Alpha Spread summary says mobile phone revenue fell 17% QoQ and 15% YoY, accounting for 49% of sales.
- Alpha Spread summary says Smart Edge Platforms grew 23% QoQ and 13% YoY, accounting for 46% of sales.
- Alpha Spread summary says first U.S. hyperscale AI accelerator ASIC project is on schedule for production.
- Alpha Spread summary says MediaTek expects AI ASIC revenue around USD 2B in Q4 2026.
- Alpha Spread summary says cloud ASIC market size is estimated around USD 70B-80B in 2027 and MediaTek targets 10%-15% market share.
- Alpha Spread summary says MediaTek is investing in silicon photonics, CPO, active optical cables with Microsoft Research, high-speed interconnects, custom HBM, and integrated voltage regulators.
- Futurum quotes Rick Tsai saying the first AI accelerator ASIC project for a U.S. hyperscale customer is progressing well and on schedule for production, with expected AI ASIC revenue around $2B in Q4 2026.
- Futurum says MediaTek has a second AI accelerator ASIC project in design, targeting mass production by end of FY2027.

## Key Numbers

| Number | Unit | Metric | Period | Source wording |
|--------|------|--------|--------|----------------|
| 149.2 | B TWD | Q1 2026 revenue | Q1 2026 | Alpha Spread summary; matches Jan-Mar YTD from MediaTek monthly table |
| -2.7 | % YoY | Q1 revenue change | Q1 2026 | Alpha Spread summary / MediaTek monthly table |
| 46.3 | % | Gross margin | Q1 2026 | Alpha Spread summary |
| 15.3 | % | Operating margin | Q1 2026 | Alpha Spread summary |
| 24.4 | B TWD | Net income | Q1 2026 | Alpha Spread summary |
| 2 | B USD | AI ASIC revenue expected | Q4 2026 | Alpha Spread / Futurum secondary summaries |
| 70-80 | B USD | Cloud ASIC market size | 2027 | Alpha Spread summary |
| 10-15 | % | Cloud ASIC share target | current target | Alpha Spread summary |
| 90 | M USD | Air Labs investment | Q1 2026 | Alpha Spread summary |
| 46.977 | B TWD | Monthly revenue | Jan 2026 | MediaTek IR monthly table |
| 38.954 | B TWD | Monthly revenue | Feb 2026 | MediaTek IR monthly table |
| 63.219 | B TWD | Monthly revenue | Mar 2026 | MediaTek IR monthly table |
| 46.737 | B TWD | Monthly revenue | Apr 2026 | MediaTek IR monthly table |
| 195.887 | B TWD | YTD revenue | Jan-Apr 2026 | MediaTek IR monthly table |

## Direct Quotes

- "In Data center, demand momentum is particularly strong." — Rick Tsai, quoted by Futurum.
- "Our first AI accelerator ASIC project for a US Hyperscale customer is progressing fairly well. We are on schedule for production and now expect AI ASICs business to contribute around $2 billion in revenue in the fourth quarter of this year." — Rick Tsai, quoted by Futurum.

## Source Reliability Notes

- MediaTek IR page is primary for the existence of Q1 2026 materials and monthly revenue table.
- Alpha Spread and Futurum are secondary summaries for the Q1 2026 call details and ASIC commentary. They are useful for M1.1 but should be verified against MediaTek's official Q1 transcript / presentation before public use.
- The Q1 revenue number (NT$149.2B) is internally consistent with MediaTek official monthly revenues Jan-Mar 2026: 46.977 + 38.954 + 63.219 = 149.150B.
- AI ASIC Q4 2026 $2B and 2027 cloud ASIC TAM/share targets are secondary until verified from MediaTek official transcript.

## Follow-up Needed

- Download or fetch MediaTek's official Q1 2026 transcript / presentation from the IR page if accessible.
- Verify whether the first U.S. hyperscale ASIC customer is Google or another customer; do not state as fact until source confirms.
- Clarify whether MediaTek's AI ASIC contribution is revenue or run-rate and whether Q4 2026 is quarter-only or annualized.
- Confirm how much of "I/O / memory subsystem" in EP659 maps to MediaTek's stated data center tech: high-speed interconnect, custom HBM, silicon photonics, CPO, voltage regulators.

## Linked Artifacts

- Intake note: `research/intake/2026-05-10_mediatek-q1-2026_cpu-asic.md`
- Knowledge pages updated:
  - `research/knowledge/ai-server-supply-chain/cpu.html`
  - `research/knowledge/ai-server-supply-chain/asic.html`
  - `research/knowledge/ai-server-supply-chain/memory.html`
- Briefs citing this packet: `research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md`
