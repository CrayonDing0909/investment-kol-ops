---
workflow: algorithm-research
artifact_type: platform-ranking-pass
created_at: 2026-05-14
platforms: x, threads
target_artifact: content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md
risk: medium
status: draft
---

# X + Threads Official Platform Pass — Card #001

> Goal: understand X / Threads ranking mechanics enough to adapt Card #001
> before publishing. This is **not** the swipe file phase yet. It uses official
> sources first, then converts platform mechanics into draft-level formatting
> hypotheses.
>
> Human-facing review surface:
> [research/swipe/reviews/2026-05-14_x-threads-card-001-platform-pass_review.html](./reviews/2026-05-14_x-threads-card-001-platform-pass_review.html)
>
> Supplemental Threads UI pass:
> [research/swipe/2026-05-15_threads-ui-patterns-card-001.md](./2026-05-15_threads-ui-patterns-card-001.md)

## Source Set

| # | Source | Class | What it contributes |
|---|---|---|---|
| 1 | [X Recommendation Algorithm README](https://raw.githubusercontent.com/twitter/the-algorithm/main/README.md) | official open-source repo | Feed architecture: candidate sources, ranking, filtering; user signals and model components |
| 2 | [X Retrieval Signals](https://raw.githubusercontent.com/twitter/the-algorithm/main/RETREIVAL_SIGNALS.md) | official open-source repo | Candidate sourcing signals: follow, favorite, retweet, quote, reply, share, bookmark, click, video watch, negative feedback |
| 3 | [X Heavy Ranker README](https://raw.githubusercontent.com/twitter/the-algorithm-ml/main/projects/home/recap/README.md) | official open-source repo | Predicted engagement outputs and example weights from 2023 |
| 4 | [Meta Transparency Center — Threads Feed](https://transparency.meta.com/features/explaining-ranking/ig-threads-feed) | official transparency doc | Threads feed: inventory, signals, ranking predictions; time spent, clicks, replies, profile taps |
| 5 | [Meta Transparency Center — approach to ranking](https://transparency.meta.com/features/explaining-ranking) | official transparency doc | General Meta AI ranking explanation: models, input signals, personalized experience, user controls |

## Important Caveats

- X open-source algorithm release is from 2023 and may not exactly match current production. Use it as a direction of signal design, not a live formula.
- X weights in Heavy Ranker are historical examples (`April 5, 2023`) and can change. Do not overfit to exact weights.
- Threads ranking docs are official but intentionally broad. They say what predictions and signals matter, not exact weights.
- This pass is **mechanics-only**. Real content examples / swipe entries come next.

## X — What The Official Docs Say

### Ranking pipeline

X For You timeline roughly follows:

```text
candidate sourcing → ranking / heavy ranker → filtering / heuristics → timeline
```

From the README:

- ~50% of candidate posts can come from in-network sources (people you follow).
- Out-of-network candidates come through systems like tweet-mixer / graph traversal / follow recommendations.
- Heavy Ranker predicts different engagement probabilities and combines them into a final score.
- Filtering removes or downranks low-quality / unsafe / unwanted content.

### Signals that matter for text posts

Official retrieval signals include:

- Favorite / like
- Retweet
- Quote tweet
- Reply
- Share
- Bookmark
- Tweet click / detail-page view
- Profile visits / profile-related interaction
- Negative feedback (`not interested`, report, block, mute)

Heavy Ranker example outputs include:

| Prediction | Practical meaning |
|---|---|
| favorite | Will the user like it? |
| retweet | Will the user repost? |
| reply | Will the user reply? |
| good profile click | Will user open author profile and like / reply? |
| good click | Will user click into conversation and engage? |
| good click v2 | Will user click in and stay at least 2 minutes? |
| reply engaged by author | Will author engage with the reply? |
| negative feedback / report | Will user downrank/report? |

Historical example weights strongly favored:

- reply engaged by author
- reply
- good profile click
- good click / dwell

Again: do not treat exact weights as current truth. But directionally, X rewards posts that create conversation and profile curiosity, not only likes.

## Threads — What Official Meta Docs Say

Threads Feed uses an AI system with multiple ML models. Official flow:

```text
gather inventory → leverage signals → rank content
```

Inventory includes:

- public Threads content
- content from accounts you follow
- text posts, photos, videos passing quality/integrity rules

Important prediction targets / signals include:

- likelihood you like a post
- likelihood you scroll past it
- likelihood you click the author's profile
- likelihood you click post → another post
- likelihood you create a reply
- likelihood you click a post
- permalink / post viewing time
- recent viewer engagement over 1 day / 1 week / 1 month
- engagement with similar accounts / content
- descendant engagement (replies, likes, replies-to-replies)

Threads emphasizes personalization and dynamic models. This means we should not assume one universal trick. But official docs point to:

- dwell / viewing time
- profile taps
- replies
- post clicks
- reply chains
- recentness and user history

## Platform Implications For Card #001

### Shared principle

The post cannot only be a polished essay. It should create at least one of:

- reply
- save / bookmark
- profile click
- link click to library
- dwell / read-through

## Signal → Content Change Map

這一段才是這份研究最重要的輸出：不是「X / Threads 有哪些 signals」，
而是「因為這些 signals，我們實際改 Card #001 哪裡」。

| Platform | Official signal / prediction | 我們推導出的內容動作 | 改到 Card #001 哪裡 | Why |
|---|---|---|---|---|
| X | `reply`, `reply engaged by author` | 結尾要有可回答的問題，不只放 link | X version 結尾加「你會把散熱這條放在基本面升級還是題材輪動？」 | 回覆是 X 官方模型明確預測的 engagement；作者之後回覆早期留言，也比較符合 reply-engaged-by-author 的方向 |
| X | `good profile click`, `good click`, `good click v2` | 第一行要讓人停下來、點進去、想看作者是誰 | 第一行保留「GB300 一櫃要花接近 $50K 在液冷上」 | 一個具體數字比「最近整理散熱」更容易產生 curiosity / profile click |
| X | `bookmark`, `tweet click` | 內容要有可保存的框架，而不是只有一句觀點 | 保留「AI 算力需求 → GPU power density → cooling BOM → supplier ASP / volume → 財報驗證」鏈條 | 這種鏈條是讀者會收藏的東西，比單純 ticker list 更有保存價值 |
| X | negative feedback / report | 不要寫成喊單或誇大確定性 | 加持倉揭露、保留「watchlist / 驗證訊號」語氣 | 降低被視為 stock pumping 的風險 |
| Threads | likelihood to create reply | 用分段 conversational format，讓每段都像可以被回覆 | Threads version 拆成 11 段，最後問同一個分類問題 | Threads 官方 ranking 看 reply creation；分段降低回覆門檻 |
| Threads | post click / profile click / viewing time | 每段只講一個概念，讓人容易連續看完 | Threads version: number → rack → heat → liquid cooling → BOM → companies → watchlist → counter | 長文直接貼會壓縮閱讀；分段能增加 dwell / post click |
| Threads | engagement with similar accounts/content | 不要過度金融黑話，保持白話研究口吻 | 保留「先翻成人話」「這不是看到名字就買」 | 讓非專業投資者也能進入，不只服務既有金融圈讀者 |
| Both | user controls / negative feedback | 不要為演算法犧牲 trust | source caveat 留在 library / review，不把 `42%` 寫進公開稿 | 如果被發現算術不通，信任會受損；比短期 reach 更重要 |

### Practical implication

這次平台調整不是把文章變短而已，而是把同一個內容分成兩種任務：

```text
X: 用強第一句 + 完整推理鏈 + 可回覆問題，測 conversation / profile click。
Threads: 用分段教學 + 每段一個概念 + 低門檻問題，測 read-through / reply。
```

## What We Still Need Real Swipe To Validate

官方文件只能告訴我們「平台大概看哪些 signals」，不能告訴我們「投資 / AI infra
內容在 2026 現場長什麼樣」。所以下一步要看真實案例。

### X examples should answer

- 強第一行通常是數字、反直覺、還是個人觀察？
- 長文裡 link 通常放哪裡？最後一行、回覆、還是 profile？
- 投資內容的 CTA 是問問題、請收藏、還是直接引導 newsletter？
- 有 source caveat 的文章，會不會降低互動？
- 作者是否在早期留言互動？互動方式是補充資料還是聊天？

### Threads examples should answer

- 好的 Threads 長文是一則長 post，還是多則串？
- 每則最佳長度大概多長？
- 分段標號（1/、2/）是否常見？
- 投資 / 科技內容在 Threads 上要不要放 ticker？
- CTA 問題更像「你怎麼看」還是「你會怎麼分類」？

### Swipe acceptance criteria

每個 swipe 不是抓爆文截圖而已，必須能回到這個問題：

```text
這個例子會讓我們改 Card #001 的哪一段？
```

### X adaptation

X should optimize for:

- strong first line
- dense but readable argument
- reply-worthy question at end
- no early link
- author replying to early comments

Recommended shape:

```text
1. First line: one memorable number / claim
2. 1 short context paragraph
3. compact causal chain
4. company mapping
5. 3 verification signals
6. counter
7. question CTA
8. library link last
```

Why:

- first line affects stop / click
- replies and profile clicks matter
- link early can pull attention away from conversation
- X users tolerate longer posts if the first line is strong and paragraphs are short

### Threads adaptation

Threads should optimize for:

- conversational feel
- shorter paragraphs
- one idea per post segment
- reply prompt that invites people to share how they classify the theme
- less dense source caveat in-line; move deeper caveat to reply or library

Recommended shape:

```text
1. Post 1: memorable number + simple human translation
2. Post 2: why rack-level system changes the analysis
3. Post 3: liquid cooling components in plain Chinese
4. Post 4: company mapping
5. Post 5: what would confirm this thesis
6. Post 6: what would make me cool down on it
7. CTA: ask for classification / save / read library
```

Why:

- Threads official docs emphasize replies, clicks, profile taps, post viewing time.
- Threads feels more conversational; highly compressed X-style threads may feel too dense.
- A chain of short posts can invite replies without forcing readers through one long block.

## Persona / Account Hypothesis

Working persona for this sprint:

```text
工程師式拆解 + 白話教學 + 投資研究紀律
```

Working nickname:

```text
直男巧虎工程師
```

Meaning:

- explain like an engineer who is also learning
- keep raw inner voice
- show uncertainty and what would change the view
- do not sell signals
- do not copy 股癌's exact voice

What to borrow from 股癌:

- recognizable personality
- spoken-language rhythm
- willingness to say obvious things plainly

What not to copy:

- financial-old-hand posture
- over-joking
- source discipline shortcuts

## Card #001 Publish Hypothesis

Hypothesis:

```text
資金 lens + concrete GB300 cooling BOM number will generate better saves / replies / profile clicks than a generic AI server supply-chain post.
```

Primary success metrics for first 72h:

1. Replies with real questions or pushback
2. Saves / bookmarks
3. Profile clicks / follows
4. Link clicks to library

Secondary metrics:

- likes
- reposts
- impressions

What we are testing:

- Does a concrete BOM number make the AI server thesis easier to enter?
- Do people care about supplier mapping if the post does not sound like a stock tip?
- Does raw research voice outperform polished explainer voice for this account?

## Platform Versions To Produce Next

This official-doc pass supports creating:

- X long post version
- Threads segmented version

Completed after this artifact:

- 5+5 real swipe synthesis:
  - [X real swipe pass](./2026-05-15_x-real-swipe-card-001.md)
  - [Threads real swipe pass](./2026-05-15_threads-real-swipe-card-001.md)
  - [HTML review](./reviews/2026-05-15_real-swipe-card-001_review.html)
- Threads native long-form / collapsed-preview direction:
  - [Threads UI patterns](./2026-05-15_threads-ui-patterns-card-001.md)

Not yet done:

- post-publish metric capture

- Card #001 now includes both X version and Threads native long-form version.

## Next Step

Create a platform-adapted version in Card #001:

```text
## Platform Ship Versions
### X Version
### Threads Version
### Publish Hypothesis
### Success Metrics
```

Then, in a following PR or follow-up task, collect 5 real swipe examples to validate or adjust these assumptions.
