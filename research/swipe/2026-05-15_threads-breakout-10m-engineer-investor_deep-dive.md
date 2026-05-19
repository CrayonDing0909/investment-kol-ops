---
workflow: algorithm-research
artifact_type: breakout-account-case-study
created_at: 2026-05-15
platform: threads
subject_account: "@10m.engineer.investor"
subject_label: "爆肝工程師的投資筆記"
target_artifact: content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md
risk: medium
status: draft
evidence_quality: mixed (public posts + public mentions; no internal analytics)
access_note: Threads pages partially accessible without login; some posts return only outer view
---

# Deep Dive — Threads Breakout Case: `@10m.engineer.investor`

> Single-account, history-trace investigation. Goal is not to swipe one viral
> post; goal is to reconstruct why this account went from a few hundred to
> ~24K followers in **one month**, what kept it growing, and what is reusable
> for our own first card.

## Why This Account

Selected by user (Dylan) who personally tracked it from a "few hundred
followers" stage. User memory: the Threads algorithm "kept pushing" his posts
in the early weeks. The account today (May 2026) sits around 33K followers
with consistent 100–300 likes per long post.

This makes it a usable **launched-hot** case study rather than a slow-growth
case. Most "small account breakout" research focuses on a single viral post.
This case is structurally different: the breakout was the *first month of
content*, not a single post.

## Reconstructed Timeline

Dates are inferred from publicly available post text and Threads post IDs.
Treat the month-level dating as load-bearing; treat day-level dating as
approximate.

| Period | Event | Evidence |
|---|---|---|
| ~2025 Sep | Account created | Inferred from 1-month anniversary post timing |
| 2025 Sep – Oct | Quantum Computing Series, 9 episodes | Episode 1 = post `DPg_swsgXFI`; Episode 9 = post `DP6uG8OksQ6`, dated **2025-10-17** |
| ~2025 Oct | 1-month milestone: **~4M views / 24K followers** | Post `DPIfsSvEbYc` |
| 2025 Oct – 2026 Apr | Slow growth from 24K → 33K | Comparing pinned thank-you (33K) to 1-month post (24K) |
| 2026 Apr 3 | Recent short repost (`DWsQ32_iaMF`, 555 views) | Date stamp visible on post page |
| 2026 Apr | Newsletter spin-off account `@10m_investment` launches | Daily YouTube finance recap format |
| 2026 May | Deep dives on $GLW (Corning) and $RKLB (Rocket Lab) | Recent feed |

Growth shape:

```text
followers
 33K -|                                            *  (May 2026)
      |                                       *
      |                              *
 24K -|             *  (1-month mark, ~Oct 2025)
      |          *
      |       *
      |    *
  0K -|  *  (~Sep 2025)
      +-------------------------------------------------> time
       Sep  Oct  Nov  Dec  Jan  Feb  Mar  Apr  May
```

Implication: the **first month did ~70% of the lifetime follower growth**.
Anything written after Oct 2025 happened on top of an audience the algorithm
had already pre-supplied.

## What The First Month Actually Looked Like

The dominant artifact of the first month is the **Quantum Computing Series**.
9 episodes, numbered "第一集" through "第九集". Available samples:

### Episode 1 — `DPg_swsgXFI`

Hook and first paragraph (verbatim):

```text
【量子系列：第一集 – 量子計算到底是什麼？】

傳統電腦，我們的數位世界，都建立在最基本的單位——「位元」（Bit）之上，
非0即1，就像開關一樣，只有開或關兩種狀態。你現在看到的這篇文章，背後
也是無數個0和1的組合。傳統電腦就像一台超高速的計算機，一個步驟一個
步驟地計算出答案。

但「量子計算」或「量子電腦」卻從根本上顛覆了這個概念！它最基本的單位
是「量子位元」（Qubit），它不再單純是0或1，而是可以同時是0、是1，
我們可以理解成每一個量子位元代表的，是一個概率，比方說30%是1，70%是0。
所以一個量子位元，就已經代表了兩個可能性了。
```

Visible engagement on outer post: **61 / 3 / 12** (likes / replies / reposts).

Pattern present in this single paragraph:

- **No ticker, no investment claim.**
- Familiar mental model first ("開關"), then surprise ("但...").
- Probabilistic analogy for qubit ("30% 是 1, 70% 是 0") instead of formal
  superposition definition.
- "我們" inclusive voice, not teacher voice.
- Series header makes the post scannable in the feed.

### Episode 9 — `DP6uG8OksQ6` (dated 2025-10-17)

This is where the series shifts from pure explainer into investment thesis:

```text
【量子系列：第九集 – 量子投資的終極思考：展望與策略】

第一部分：我對量子技術的想法

在撰寫這個系列之前，我對量子技術其實只有一個模糊的概念...

我認為，量子技術更像是一種專門的計算機器...這有點像現在的 GPU，它在
處理矩陣運算或機器學習、AI 計算時，能提供特別的效能飛躍...如果它主要
擅長的確實是這類問題，那麼它是否真的會徹底改變整個計算生態，就存在
很大的疑問了。這完全取決於最終 QPU 的價格能降到多低...
```

Critical pattern: he **opens the investment thesis episode by admitting his
initial ignorance** ("我對量子技術其實只有一個模糊的概念") and gives a
*counter-position* (skeptical that QPU will redefine compute) before any buy
recommendation.

So the series arc is:

```text
Episode 1-8: 量子計算到底是什麼，為什麼這個技術值得理解 (no investment)
Episode 9:   學完之後我自己怎麼想 (counter-take + nuanced investment frame)
```

By Episode 9, the reader has spent enough cognitive time on the explainer to
trust him. He cashes that trust by offering a **measured** view, not a buy
call. That measured tone itself becomes brand.

## The 1-Month Anniversary Post

Post `DPIfsSvEbYc`, full text:

```text
一個月了！今天就是這個帳戶成立一個月的日子，在這段日子裡，我們得到了
將近400萬次的瀏覽次數，兩萬四千多的追蹤，在心裡只有無限的感恩。
很感謝大家對我這樣一個非財務專業的工程師的想法感興趣！

商業邏輯、商業分析一直是我很感興趣的一塊，也一直想找到同好，沒想到
這個帳戶讓我找到這麼多對公司商業模式、營利模式以及行業趨勢感興趣的
朋友！

(...)
```

Engagement on this post: **181 / 5 / 1 / 5**. Notably **lower** than the
deep dives that came right before. Meaning: gratitude / meta posts get
*less* engagement than analysis posts. The algorithm-pushed content here was
the **explainer series, not the personality post.**

## The Eight Patterns Driving Breakout

Each pattern is named, justified by evidence above, and rated for how reusable
it is for our own first card.

### Pattern 1 — Niche identity: engineer + investor

Bio: "早上是工程師，晚上(想)是巴菲特". 1-month post repeats: "我這樣一個
非財務專業的工程師". This combination is rare in Mandarin investing content.
Algorithm sees a topic cluster with low supply and high demand.

Reusable for Card #001: **high** — our author is also an engineer, this is
the exact same niche slot.

### Pattern 2 — Explainer first, thesis later

8 of 9 first-month episodes contain zero ticker. The thesis episode (9) is
about *uncertainty*, not a buy call.

Reusable for Card #001: **high if we restructure** — current Card #001 is a
thesis card with no explainer prequel.

### Pattern 3 — Series structure as retention engine

Numbered "第一集" through "第九集". Reader who likes Ep 1 has a reason to
return for Ep 2. Algorithm sees compounding profile click / follow / save.

Reusable for Card #001: **high if we restructure** — Card #001 can become
"散熱系列 第一集" with Card #002 / #003 already planned as continuation.

### Pattern 4 — Familiar mental model + small surprise

Bit = 開關 (familiar) → Qubit = 30/70 probability (surprise). No formal
math. No jargon.

Reusable for Card #001: **high** — concrete worked example user already
mentioned: "為什麼一台 AI server 一個月電費比一台 Model S 還貴". Model S
is the familiar anchor, the answer is the surprise.

### Pattern 5 — "我們" voice, not teacher voice

"我們的數位世界". "我們可以理解成". This is collaborative discovery, not
lecture.

Reusable for Card #001: **already partially in place** in our
`content-voice-raw-research` rule, but the *we-discover-together* framing
deserves a stronger explicit slot.

### Pattern 6 — Numbered long posts, not text-attachment

His long content runs as **multiple numbered posts in a single thread**, not
as one outer post + collapsed long-form attachment. Each numbered post is
independently likeable, repostable, quotable.

Reusable for Card #001: **high** — this contradicts our earlier conclusion
from the Threads UI pattern pass (which favored long-form attachment). The
case here is: when the content is dense and educational, *numbered posts*
beat a single attachment because each segment can be discovered, quoted, and
saved on its own.

This is the most important *direction-changing* finding of this case study.

### Pattern 7 — Trust-building before monetization

Newsletter spin-off `@10m_investment` did not appear until ~6 months after
the main account hit 24K. The main account stays as deep dives; the
newsletter does daily YouTube recap. Two distinct value props, no early
overlap.

Reusable for Card #001: **medium / later** — relevant for the broader
funnel, less relevant for the first card itself.

### Pattern 8 — Counter-position increases credibility

Episode 9 opens with a counter ("我對量子計算會改變世界...持有保留態度").
The pinned message warns about scammers impersonating him. Both moves
sacrifice short-term hype for medium-term trust.

Reusable for Card #001: **high** — our current draft already includes the
"先不要急著喊散熱概念股" counter. This case validates the move.

## Direction-Changing Findings vs. Earlier Research

These specifically *override* conclusions from the earlier real swipe and
official platform pass:

| Earlier conclusion | New finding | Reason to update |
|---|---|---|
| Threads long-form = outer post + text attachment | Numbered long-form posts can outperform attachments for educational content | This account's entire breakout was numbered posts, not attachments |
| Card #001 should ship as a single thesis post | Card #001 should be Episode 1 of a series, where Episode 1 is pure explainer | The 9-episode arc this account used is a proven structure on Threads |
| Hook = a strong number ($50K cooling BOM) | Hook = vivid cross-domain analogy with a number (Model S / AI server electricity) | The Quantum Series hook (30/70 probability) shows analogy beats raw number |

## Implications for Card #001

Three concrete moves we should evaluate:

1. **Rename Card #001 to "散熱系列：第一集"** and reserve "第二集 / 第三集"
   slots for BOM-and-supplier mapping and thesis. Reframe the artifact as
   the opening of a planned arc.

2. **Rewrite Card #001 Episode 1 as pure explainer:**
   - Hook: "為什麼一台 AI server 一個月電費比一台 Model S 還貴"
   - Mental model: rack = a small power plant living in a building
   - Bridge: heat density, why air cooling stops working
   - Tease: 下一集會拆「這筆錢具體流去哪裡」
   - No ticker. No supplier. No position disclosure (because no claim).

3. **Hold the existing BOM thesis as Episode 2 draft** — content is good,
   the audience just doesn't trust us enough yet to consume it as Episode 1.

## What I Could Not Verify

- Exact account creation date (only inferred from anniversary post).
- Whether the algorithm push was assisted by paid boosts or external
  cross-promotion.
- Cantonese / HK origin (search results were ambiguous; not load-bearing for
  our reuse plan).
- Whether the early episodes were posted daily, every-other-day, or
  irregularly; cadence may matter and is currently unknown.

## Source List

| Source | URL |
|---|---|
| Account home | `https://www.threads.com/@10m.engineer.investor` |
| Quantum Episode 1 | `https://www.threads.com/@10m.engineer.investor/post/DPg_swsgXFI` |
| Quantum Episode 9 | `https://www.threads.com/@10m.engineer.investor/post/DP6uG8OksQ6` |
| 1-month milestone | `https://www.threads.com/@10m.engineer.investor/post/DPIfsSvEbYc` |
| Recent short post | `https://www.threads.com/@10m.engineer.investor/post/DWsQ32_iaMF` |
| Newsletter spin-off | `https://www.threads.com/@10m_investment` |
| Blog stub | `https://10mblog.com/` (calendar UI, no public articles indexed) |

## Next Step

Extract patterns 1-8 into a reusable rule at
`.cursor/rules/series-narrative-architecture.mdc` so future cards
automatically receive series structure / explainer-first treatment when
appropriate. Then decide on Card #001 series restructure.
