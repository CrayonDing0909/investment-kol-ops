---
workflow: investment-analysis
artifact_type: source-packet
risk: medium
created_at: 2026-05-13
theme: ai-server-supply-chain
layer: manufacturing-capacity
company: Intel, Apple
ticker: INTC, AAPL
source_class: news
source_quality: secondary
status: draft
---

# Source Packet: Apple-Intel Foundry Preliminary Agreement (May 2026)

## Source Metadata

- Companies: Intel Corporation; Apple Inc.
- Tickers: INTC; AAPL
- Source class: news
- Source quality: secondary (WSJ origin → CNBC / TheStreet / CNBC analyst commentary; no joint press release yet)
- Title:
  - "Intel shares fly on Apple chip deal report. Here's why it's a big deal" (CNBC)
  - "Apple and Intel have reached preliminary chip-making agreement" (WSJ origin)
  - "Apple Strikes Deal with Intel Foundry Services for Chip Production in the U.S." (TechPowerUp)
- Publisher:
  - CNBC (Kif Leswing)
  - Wall Street Journal (origin reporting)
  - TheStreet
  - TechPowerUp
- Date published:
  - 2026-05-08 (CNBC; reflects WSJ Friday report)
- URL:
  - https://www.cnbc.com/2026/05/08/intel-stock-apple-chip-deal.html
  - https://www.wsj.com/tech/apple-intel-have-reached-preliminary-chip-making-agreement-69eb9370
  - https://www.techpowerup.com/348924/apple-strikes-deal-with-intel-foundry-services-for-chip-production-in-the-u-s
  - https://www.thestreet.com/latest-news/apple-signs-chipmaking-deal-with-intel-joining-microsoft-amazon-and-tesla
- Captured at: 2026-05-13

## Why This Source Matters

Apple's near-total reliance on TSMC for advanced chip manufacturing has been the
single largest design-system anchor inside global advanced foundry supply. A
preliminary Apple-Intel agreement marks the first credible second-source path
for the world's most advanced node demand. Combined with hyperscaler supply
constraints, it potentially reroutes wafer capacity assumptions across the AI
server supply chain.

For our theme, this packet sits in the **Manufacturing Capacity** layer:
who can fabricate leading-edge silicon, and whether Intel Foundry is a real
TSMC alternative.

## Raw Facts

- Apple and Intel reportedly reached a preliminary chip-making agreement, per
  WSJ reporting (Friday before 2026-05-08).
- Both companies declined to comment publicly as of 2026-05-08.
- Intel shares rose ~14% on the day of the WSJ report; up 200%+ year-to-date as
  of 2026-05-08. Apple shares added ~2%.
- Talks have been ongoing for more than a year before reaching preliminary
  status "in recent months".
- Apple currently relies solely on TSMC for the most advanced chips in iPhones,
  Macs, and related devices. Apple is TSMC's second-largest customer behind
  NVIDIA (per Creative Strategies analyst Ben Bajarin).
- Targeted Intel process node: 18A (1.8nm-class). Analyst Bajarin expects Apple
  may wait for the improved 18A-P variant scaling as soon as 2027.
- Manufacturing site: Intel's high-volume 18A fab in Chandler, Arizona.
  Additional advanced packaging facilities in Arizona and Nevada; new
  facilities under construction in Ohio for future nodes.
- TSMC is also scaling Arizona fabs; Apple has previously committed to making
  some silicon at TSMC Arizona.
- Apple executives reportedly also visited Samsung's new chip manufacturing
  plant under construction in Texas (Bloomberg, 2026-05-05).
- Intel's other major external foundry commitment (Elon Musk's $119B Terafab in
  Austin, Texas, for Tesla / SpaceX / xAI) targets Intel 14A node; volume
  production not expected until 2029.
- Existing Intel advanced-packaging external customers include Amazon and Cisco
  (per CNBC).
- TSMC CEO C. C. Wei recently referred to Intel as a "formidable competitor"
  during commentary.

## Claim Classification

| Exact source wording | Plain meaning | Claim type | Confidence |
|----------------------|---------------|------------|------------|
| "Apple and Intel are reportedly closing in on a deal that would see Intel make some of the chips for the iPhone maker's devices." | preliminary deal, not finalized | reported-fact (secondary; both companies declined to comment) | inferred (no primary press release) |
| "Talks between the two companies have been brewing for more than a year, with a preliminary agreement reached in recent months." | multi-year negotiation, preliminary stage | reported-fact (per WSJ sourcing) | inferred |
| "Intel shares soared nearly 14% on Friday." | market reaction | reported-fact | known |
| "Apple is most likely to wait to make chips on Intel's next node, called 18A-P, which could scale as soon as next year." — Bajarin | analyst expectation | secondary-interpretation (analyst, not company) | inferred |
| "Intel is the only place that can scale up capacity as a viable second source." — Bajarin | analyst framing | secondary-interpretation | inferred |
| "[Intel has] got through the rough patch and can now be considered validated as a credible second source." — Bajarin | analyst conclusion | secondary-interpretation | inferred |
| "An Apple-Intel deal won't impact TSMC because they're already printing wafers as fast as they can." — Bajarin | analyst conclusion (TSMC supply state) | secondary-interpretation | inferred |
| TSMC CEO C. C. Wei called Intel a "formidable competitor". | TSMC CEO acknowledgement | reported-fact (secondary report of public commentary) | inferred |

## Key Numbers

| Number | Unit | Metric | Period | Source wording |
|--------|------|--------|--------|----------------|
| ~14 | % | INTC daily share price gain | 2026-05-08 | CNBC |
| 200+ | % YTD | INTC year-to-date share gain | 2026-05-08 | CNBC |
| 2 | % | AAPL daily share price gain | 2026-05-08 | CNBC |
| 18A | node | targeted Intel process node | first signing | Multiple |
| 18A-P | node | possible production node | 2027 | Bajarin via CNBC |
| 119 | B USD | Musk Terafab cost (separate Intel external customer) | planned | CNBC |
| 14A | node | Terafab targeted node | 2029 (volume) | CNBC |

## Direct Quotes

- "I 100% believe this is going to happen. I don't know when." — Ben Bajarin, Creative Strategies (CNBC).
- "Intel is the only place that can scale up capacity as a viable second source." — Bajarin.
- "They've got through the rough patch and can now be considered validated as a credible second source." — Bajarin.
- "An Apple-Intel deal won't impact TSMC because they're already printing wafers as fast as they can." — Bajarin.
- "If you're about to have one of your largest customers probably sign a deal with a competing foundry, that would be the kind of thing you say to perhaps soften the blow." — Bajarin, on TSMC CEO's "formidable competitor" framing.
- TSMC CEO C. C. Wei publicly described Intel as a "formidable competitor" (no full quote).

## Source Reliability Notes

- No primary press release from Apple or Intel as of 2026-05-13. Both declined
  to comment when WSJ broke the story.
- The WSJ origin reporting is well-sourced by industry track record; CNBC is a
  major secondary outlet. Still, this should be treated as a **preliminary
  agreement reported by media**, not a confirmed contract.
- Analyst quotes (Bajarin) are secondary-interpretation; reference but do not
  cite as fact.
- Strong forward-looking element: actual node selection (18A vs 18A-P),
  volume timing, USD revenue impact, and whether the deal survives final
  negotiation are all open.

## Follow-up Needed

- Watch for official joint Apple-Intel press release or 8-K disclosure from
  Intel.
- Verify whether Apple's commitment includes mobile (iPhone) chips or only
  Mac / accessory chips; sources do not specify.
- Pull Intel Q2 2026 earnings commentary on Foundry external pipeline.
- Track TSMC Q2 2026 commentary on whether Apple wafer allocation shifts.
- Check Bloomberg follow-up on Apple-Samsung Texas plant exploration.
- Open question: what advanced-packaging share does Intel pull in addition to
  wafer (EMIB / Foveros), and how does that intersect with NVIDIA / Cisco
  existing customers?

## Linked Artifacts

- Theme map layer (new): Manufacturing Capacity (`research/knowledge/ai-server-supply-chain/foundry-capacity.html`, to be created)
- Companion source packets:
  - `research/sources/ai-server-supply-chain/policy/2026-05-13_intel-chips-act-source-packet.md`
  - `research/sources/ai-server-supply-chain/news/2026-05-13_intel-foundry-external-customer-source-packet.md`
