---
workflow: algorithm-research
artifact_type: ui-pattern-pass
created_at: 2026-05-15
platform: threads
target_artifact: content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md
risk: medium
status: draft
---

# Threads UI Pattern Pass — Card #001

> Goal: understand current Threads long-form / collapsed-preview UI patterns
> before publishing Card #001. This supplements the official ranking pass.
>
> Human-facing review surface:
> [research/swipe/reviews/2026-05-15_threads-ui-patterns-card-001_review.html](./reviews/2026-05-15_threads-ui-patterns-card-001_review.html)

## Source Set

| # | Source | Class | What it contributes |
|---|---|---|---|
| 1 | User screenshot: `photo_2026-05-15_00.23.42...png` | live app observation | Feed preview format: short outer post + gray collapsed long-text card |
| 2 | User screenshot: `photo_2026-05-15_00.23.39...png` | live app observation | Expanded long text reading experience and engagement bar |
| 3 | [Threads official post: long-form text attachments](https://www.threads.com/@threads/post/DPgzLZcAJPr/you-can-share-up-to-10000-characters-in-a-long-form-text-attachment-room-for-ext?hl=en) | official Threads post | 10,000-character text attachment, formatting support |
| 4 | [9to5Mac: Threads long-form posts with text attachments](https://9to5mac.com/2025/08/28/threads-is-testing-long-form-posts-with-support-for-formatted-text/) | high-quality secondary | Gray box preview, read more, formatted text, outward link support |
| 5 | [TechCrunch: Threads tests long-form text](https://techcrunch.com/2025/08/28/threads-tests-a-way-to-share-long-form-text-on-the-platform/) | high-quality secondary | Text attachment replaces multi-post workaround; snippet shown in gray box; click to read full text |

## What We Learned

Threads now supports a native long-form text attachment pattern:

```text
Outer post: short hook / context
↓
Gray text card: preview of long-form body
↓
Tap to open: full long text, scrollable, with engagement bar
```

This means Card #001 should not necessarily be published as an 11-part thread.
For this type of educational / research content, a better Threads-native shape is:

```text
Outer post: one-line hook + why I'm looking at this
Text attachment: full reasoning in one coherent article-like block
CTA: inside outer post or near end of text attachment
```

## Swipe #1 — User Screenshot

### Feed preview

Observed format:

```text
從 5,000 美元開始用 12 年
做到了 1 億美元

[gray collapsed card]
你第一個反應是什麼？
「他一定有什麼秘密武器」
「他一定有內線」
「他一定天賦異稟...
```

What worked:

- Outer post has a simple story hook: `$5,000 → $100M over 12 years`.
- Preview card opens with a psychological question: `你第一個反應是什麼？`
- The gray card creates visual separation in feed.
- The preview ends mid-list, creating open loop.
- Expanded view is a long-form story with paragraphs and plain language.

Adaptation for Card #001:

```text
Outer post:
GB300 一櫃要花接近 $50K 在液冷上。

我原本以為這只是散熱概念股，整理完覺得不是這樣。

Text attachment preview:
你第一個反應可能是：
「又是 AI server 題材？」
「散熱不就是風扇嗎？」
「這種二手拆解能信嗎？」

我一開始也差不多。
```

## Threads Text Pattern Library

### Pattern 1 — Psychological first reaction

Use when readers may have an obvious but shallow first interpretation.

Example structure:

```text
你第一個反應可能是：
「A」
「B」
「C」

我一開始也差不多。
但整理完覺得，真正要看的不是這個。
```

For Card #001:

```text
你第一個反應可能是：
「散熱不就是風扇嗎？」
「又是散熱概念股？」
「AI server 最重要的不還是 GPU？」

我一開始也差不多。
但整理完覺得，真正變化是在 rack-level system。
```

### Pattern 2 — One surprising number + translation

Use when the content has one number that can anchor memory.

For Card #001:

```text
GB300 一櫃要花接近 $50K 在液冷上。

這句話如果直接看，可能很像一個供應鏈數字。
但翻成人話是：NVIDIA 每賣出一台 AI server rack，上面就會綁一套液冷系統。
```

### Pattern 3 — Not a buy list, a watchlist

Use when named companies appear and the post risks sounding like a stock tip.

For Card #001:

```text
對應到公司會看到：

- 奇鋐 / AVC
- 雙鴻 / Auras
- Vertiv

但這不是看到名字就買。
我會先把它們放進 watchlist，看法說有沒有轉成 revenue / margin / backlog。
```

### Pattern 4 — The actual mechanism

Use after the hook, before companies.

For Card #001:

```text
AI 算力需求上升
→ GPU power density 上升
→ rack cooling 從 optional 變 required
→ cooling BOM per rack 上升
→ 對應零件供應商 ASP / volume 有機會上升
→ 最後回到法說驗證
```

### Pattern 5 — Soft conclusion

Use instead of hard recommendations.

For Card #001:

```text
所以我目前不是把它當成「買哪一檔」。

我比較像是把散熱放進 AI server 基本面支線裡追。

如果 rack power 繼續往上，這條線值得繼續看。
如果法說沒有轉成 backlog / margin，那就降級。
```

## Recommended Threads Native Format For Card #001

### Outer post

```text
GB300 一櫃要花接近 $50K 在液冷上。

我原本以為這只是散熱概念股，整理完覺得不是這樣。
```

### Text attachment body

```text
你第一個反應可能是：

「散熱不就是風扇嗎？」
「又是 AI server 題材？」
「最重要的不還是 GPU？」

我一開始也差不多。

但整理完 GB300 這條，感覺真正的變化不是「散熱突然很重要」，而是 AI server 已經變成一櫃一櫃的系統在賣。

GB300 NVL72 不是一張 GPU。

它是一台 rack-level system。一櫃裡面有 72 顆名字叫 B300 的 GPU，滿載功耗大概 132-140kW。

140kW 對我來說不是工程數字。

它比較像是在提醒：這一櫃本質上就是一個很貴、很密集的熱源。

熱排不出去，GPU 會 thermal throttle，也就是自己降速保命。

你買了很貴的算力，但跑不滿，就是在浪費錢。大企業當然不會讓這種事發生。

所以液冷開始從 optional 變 required。

拆開看，大概有幾段：

- cold plate：貼在晶片上，把熱帶到冷卻液
- CDU：整櫃冷卻液循環的主機
- manifold：把冷卻液分到不同 tray
- UQD：快接頭，讓 tray 可以維修又不漏液

公開拆解資料給的量級是：

- GB300 NVL72 單櫃液冷 BOM 約 $49,860
- GB200 約 $41,500

BOM 是零件成本表。

這不是某家公司直接賺到的營收，但它說明一件事：每一櫃 AI server 裡，散熱這個 category 的 content 變大了。

也就是說，NVIDIA 每賣出一台 AI server rack，上面就會綁一套液冷系統。

對應到公司，先粗分：

- 奇鋐 / AVC：cold plate、液冷模組
- 雙鴻 / Auras：manifold、液冷 solution
- Vertiv：rack / data center 層級 cooling infrastructure

但這不是看到名字就買。

我會先把它們放進 watchlist，看後面法說有沒有真的轉成 revenue / margin / backlog。

所以這條線我目前會這樣理解：

AI 算力需求上升
→ GPU power density 上升
→ rack cooling 從 optional 變 required
→ cooling BOM per rack 上升
→ 對應零件供應商 ASP / volume 有機會上升
→ 最後回到法說驗證

反向檢查點（算一種利多出盡吧）：

如果未來兩年 AI rack 還是以過渡型液冷為主，沒有更快走向 direct-to-chip / 全液冷，那 cold plate、manifold、CDU 這些零件的成長速度可能就沒有想像中快。

但目前看到的產業資料，方向是 OK 的。

所以我目前不是把它當成「買哪一檔」。

我比較像是把散熱放進 AI server 基本面支線裡追。

如果 rack power 繼續往上，這條線值得繼續看。
如果法說沒有轉成 backlog / margin，那就降級。
```

### CTA

```text
你會先追散熱、HBM，還是 ASIC 這幾條線？

完整 AI server 供應鏈地圖：
https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/

持倉揭露：作者可能持有文中提及個股，內容僅作研究紀錄，不構成投資建議。
```

## Why This Is Better Than The 7-Part Thread

- It matches current Threads long-form UI: short outer post + gray text attachment.
- It keeps the article-like learning flow intact.
- It avoids forcing readers through 7-11 separate numbered posts.
- It still creates a strong feed hook.
- It keeps CTA and source link at the end, not before the reader understands the point.

## What Still Needs Real Swipe

Before publishing, collect examples to verify:

- Do current high-performing Threads long-form posts use outer hook + text attachment?
- How long is the preview before collapse?
- Do they use psychological first-reaction openings?
- Do creators place links in the attachment body or outer post?
- Do finance / investing Threads posts use tickers in the outer post or inside the attachment?
