---
workflow: investment-analysis
artifact_type: source-packet
risk: medium
created_at: 2026-05-13
theme: ai-server-supply-chain
layer: component-passive
company: Yageo (Kemet), Walsin (華新科), Samsung Electro-Mechanics, Murata, TDK, Nichicon (NDB)
ticker: 2327.TW, 2492.TW, 009150.KS, 6981.T, 6762.T
source_class: news
source_quality: secondary
status: draft
---

# Source Packet: AI Server Passive Components Tightness (MLCC + Tantalum, 2026)

## Source Metadata

- Source class: news
- Source quality: secondary (DigiTimes industry coverage)
- Title (multi-source):
  - "Yageo subsidiary Kemet hikes tantalum capacitor prices for third time as strong AI server demand continues"
  - "Passive component demand splits in 2026; AI and autos hold firm"
  - "MLCC, inductor prices climb as AI demand meets cost pressure"
  - "AI demand tightens supply of high-end MLCCs; Nichidenbo sees limited US-Iran impact on tantalum capacitors"
  - "Demand for AI infrastructure spreads shortages beyond memory chips to MLCCs"
- Publisher: DigiTimes
- Date published: 2026-03 to 2026-04 range
- URL:
  - <https://www.digitimes.com/news/a20260302PD239/yageo-tantalum-capacitor-price-increase-ai-server-demand.html>
  - <https://www.digitimes.com/news/a20260414PD202/passive-components-demand-walsin-yageo-2026.html>
  - <https://www.digitimes.com/news/a20260416VL204/demand-cost-component-passive-price.html>
  - <https://www.digitimes.com/news/a20260311PD208/ndb-demand-high-end-passive-price.html>
  - <https://www.digitimes.com/news/a20260410PD214.html>
- Captured at: 2026-05-13

## Why This Source Matters

被動元件在 EP659 是「敘事尚未啟動」的 candidate，但 2026 data 顯示已啟動：
Kemet 3 連漲、Samsung Electro-Mechanics 考慮 +5-10%、Walsin / Yageo 都報強
AI demand。這是 M2.1 公開化必須補的 layer，也提供台廠故事的 source-backed
版本。

Caveat: DigiTimes 是台灣產業媒體權威，但所有 5 篇都是 DigiTimes 自家報導，
evidence chain 沒有跨 publisher 獨立來源；公開引用前最好對 Yageo / Walsin
官方法說做 primary 對齊。

## Raw Facts

- Yageo's subsidiary Kemet has raised tantalum polymer capacitor prices for
  the **third time** in 2026 cycle; cited "strong AI server demand".
- AI server MLCC orders have doubled capacity demand.
- MLCC and inductor prices climbing globally, led by Japanese suppliers,
  driven by both higher raw material costs and AI-driven demand.
- Samsung Electro-Mechanics weighing MLCC price hikes of 5-10% as supply
  tightens.
- High-end MLCC supplies tightening as AI infrastructure buildout consumes
  capacity.
- Yageo reports strong demand in early 2026 driven by AI orders.
- Passive component demand "splitting in 2026": strong AI + autos vs weaker
  consumer segments.
- Supply-demand gap in tantalum polymer capacitors continues to widen as AI
  server applications consume large quantities (Yageo / Kemet observation).
- Nichicon (NDB / Nichidenbo) sees limited impact from US-Iran geopolitical
  tensions on tantalum capacitors (so the price hikes are demand-driven, not
  raw-material-driven shock).

## Claim Classification

| Exact source wording | Plain meaning | Claim type | Confidence |
|----------------------|---------------|------------|------------|
| "Kemet hikes tantalum capacitor prices for third time" | reported price action | reported-fact (secondary) | inferred |
| "AI server MLCC orders have doubled capacity demand" | reported demand framing | secondary-interpretation (no specific 2x baseline given) | uncertain |
| Samsung Electro-Mechanics weighing 5-10% MLCC price hike | management consideration | management-expectation (Samsung not committed) | inferred |
| Yageo strong early-2026 AI demand | management commentary | management-expectation (Yageo IR) | inferred |
| Passive demand "splitting" AI+auto vs consumer | industry framing | secondary-interpretation | inferred |
| Tantalum polymer supply-demand gap widening | qualitative framing | secondary-interpretation | inferred |
| Nichicon: limited US-Iran impact on tantalum | management observation | management-expectation (Nichicon) | inferred |

## Key Numbers

| Number | Unit | Metric | Period | Source wording |
|--------|------|--------|--------|----------------|
| 3 | times | Kemet tantalum polymer price hikes in 2026 cycle | 2026 | DigiTimes |
| 5-10 | % | Samsung Electro-Mechanics MLCC price hike consideration | 2026 | DigiTimes |
| ~2x | x | AI server MLCC orders vs capacity | 2026 | DigiTimes (no specific baseline) |

## Direct Quotes

- "Strong AI server demand continues" — context for Kemet's third 2026 price hike (DigiTimes).
- Yageo reported "strong demand in early 2026 driven by AI orders" (DigiTimes).
- Nichidenbo "sees limited US-Iran impact on tantalum capacitors" — meaning price hikes are demand-driven, not supply-shock (DigiTimes).

## Source Reliability Notes

- All 5 captured sources are DigiTimes — **single-publisher evidence chain**.
  DigiTimes is industry-respected for Asian passive / IC reporting, but for
  public quoting we should:
  - cross-check Kemet / Yageo / Walsin earnings call commentary (primary)
  - find at least one non-DigiTimes secondary source (Nikkei / Bloomberg /
    Reuters)
- No primary press release from Yageo / Kemet on the 3rd tantalum price
  hike captured here.
- 信昌電 (mentioned in EP659 as having a delivery-extension notice) is NOT
  appearing in the 2026 coverage we found. This is a gap — EP659 reference
  needs an explicit 信昌電 announcement or news source to back the original
  claim. Listed in follow-up.
- The "AI server MLCC orders doubled capacity demand" phrasing is generic;
  no specific baseline. Use with caveat.

## Follow-up Needed

- Pull Yageo / Kemet / Walsin Q1 2026 earnings transcripts (primary).
- Find non-DigiTimes secondary coverage (Nikkei Asia / Bloomberg / Reuters)
  to break single-publisher evidence chain.
- **Verify 信昌電 (Sino-American Silicon related? Or another co?) delivery-
  extension claim from EP659**. The 5 DigiTimes pieces did not mention it.
  This is an explicit M2.1 gap.
- Pull Samsung Electro-Mechanics Q1 2026 earnings on MLCC pricing.
- Pull Murata / TDK Q1 2026 earnings on MLCC and AI exposure.
- Open: does the "AI + auto + IoT" demand also reach mid-tier MLCC (Walsin
  / 華新科), or only premium MLCC (Murata / Samsung)?

## Linked Artifacts

- Theme map: integrates with
  [research/knowledge/ai-server-supply-chain/passive-components.html](../../knowledge/ai-server-supply-chain/passive-components.html)
  (currently has EP659 narrative, needs source-backed update)
  and the index `known-narrative` table item on 信昌電.
- Cross-references:
  - `research/sources/ai-server-supply-chain/reports/2026-05-13_ai-chip-supply-tightness-source-packet.md` (passive component shortage referenced from CNAS angle)
