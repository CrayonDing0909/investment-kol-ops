---
artifact_type: voice-lessons
workflow: content-production
related_artifact: content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md
created_at: 2026-05-14
status: draft
rule_candidate: content-card-voice
---

# Card Writing Voice Lessons — Card #001

> 目的：把 Card #001 磨出來的寫作語氣與內容邏輯，存成 repo artifact。
> 不靠 chat 記憶。之後 #002 / #003 寫稿時先讀這份，再決定是否升成正式
> `.cursor/rules/**`。

## Why This Exists

Card #001 一開始結構正確，但讀起來不像使用者本人會說的話。主要問題不是
source，也不是邏輯，而是 **voice surface**：太像 AI 在幫讀者解釋，少了
使用者「我正在整理資料」的心聲。

這份文件記錄哪些句型要避開、哪些語氣要保留、公開 card 應該怎麼有起承轉合。

## The Target Voice

不是：

```text
媒體解說文
投研報告
AI 教學文
安全但無個性的摘要
```

而是：

```text
我在整理資料時的內心推理
→ 先抓一個記憶點
→ 把自己真正想理解的支線拆開
→ 承認哪裡還不是很硬
→ 最後說「統整完我目前知道什麼」
```

## Voice Principles

### 1. 開頭要有記憶點，不要只有保守態度

弱：

```text
最近整理 GB300 散熱這條，我覺得先不要急著喊「散熱概念股」。
```

好：

```text
GB300 一櫃要花接近 $50K 在液冷上。

這是我最近整理 AI server 供應鏈時，覺得最有記憶點的一個數字。
```

原因：第一句要讓讀者知道「我為什麼要停下來看這件事」。

### 2. 避免 AI 常用對照句

這些句型容易像 AI：

```text
不再只是 A，而是 B
這不是 primary source，是 secondary...
為什麼 X 會變成 Y？
Reader takeaway...
核心 thesis...
底層原因...
```

更像使用者的寫法：

```text
我現在比較想拆的是...
我先抓一個量級...
這個數字我暫時不會拿來算很精準的模型...
有一個數字我先放掉...
所以統整完上面這些資料...
```

### 3. Source caveat 不要寫成審稿註解

弱：

```text
這不是 primary source，是二手拆解 / industry estimate，所以我只拿它當方向感。
```

好：

```text
這個數字我暫時不會拿來算很精準的模型，因為 source 還是二手拆解。
但它至少讓我知道一件事：液冷已經不是「有就好」的配件，而是每一櫃都要認真算的成本項目。
```

原因：caveat 不是為了顯示自己小心；caveat 要服務於「我因此怎麼判斷」。

### 4. 括號是心理暗示，不是雜訊

使用者明確說，括號是心聲技巧。

保留：

```text
這條線我會先放一個反向檢查點（算一種利多出盡吧）：...
```

不要把它改成：

```text
某種程度也算是利多出盡的觀察
```

後者太報告。

### 5. 需要起承轉合

Card #001 的可用架構：

```text
起：GB300 一櫃要花接近 $50K 在液冷上
承：GB300 是 rack，不是一張 GPU；132-140kW 是熱源
轉：熱排不出去 = GPU 降頻 = 大企業不會接受
合：液冷變必要 BOM → 對應供應鏈 → 財報驗證 → counter
```

不要只列：

```text
Observation → Mechanism → Implication → Counter
```

那是內部推理框架，不是對外文章表面。

### 6. 投資邏輯要有完整鏈條，但語氣不能像教科書

底層鏈條：

```text
需求變化
→ 技術 / 物理 / 供應瓶頸
→ 必要零件 / 能力 / 產能
→ BOM / ASP / content per unit / volume 變化
→ 公司 revenue / margin / backlog 驗證
→ Counter
```

但在公開稿裡要寫成使用者心聲：

```text
所以這條線我會這樣看：

AI 算力需求上升
→ GPU power density 上升
→ rack cooling 從 optional 變 required
→ cooling BOM per rack 上升
→ 對應零件供應商的 ASP / volume 有機會上升
→ 最後回到法說驗證 revenue、margin、backlog
```

### 7. 結尾要讓讀者覺得「有學到」

弱：

```text
完整地圖在 library...
```

好：

```text
所以統整完上面這些資料，我目前得到的結論是：

散熱開始被市場重新看見，我現在理解比較像是：AI server 變成一櫃一櫃的系統在賣，所以它上面的散熱組件也會被一起綁進去。只要 rack-level system 出貨，cold plate、CDU、manifold 這些東西就會跟著有連帶關係。

如果未來一切都很美好，AI rack 繼續往更高功耗走，這條線會繼續值得追。反過來，如果液冷 adoption 卡在過渡方案，或供應商法說沒有轉成 backlog / margin，那就要小心一點。

但我目前覺得本質沒有變。只要算力還在短缺，rack power 還在往上，液冷應該就是 AI server 基本面裡一個很好的支撐點。
```

## Current Accepted Pattern For Card #001

```text
GB300 一櫃要花接近 $50K 在液冷上。

這是我最近整理 AI server 供應鏈時，覺得最有記憶點的一個數字。

先翻成人話。

GB300 NVL72 不是一張 GPU，而是 NVIDIA 新一代 AI server rack。一櫃裡面有 72 顆 B300 GPU，滿載功耗大概 132-140kW。

140kW 是什麼概念？

你可以先不用管工程細節，只要知道：這一櫃本質上就是一個很貴、很密集的熱源。

熱排不出去，GPU 會 thermal throttle，也就是自己降速保命。你買了很貴的算力，但跑不滿，就是在浪費錢。大企業當然不會讓這種事發生。
```

## Checklist Before Drafting Future Cards

Before sending a card draft to user:

- [ ] 第一行有記憶點嗎？
- [ ] 第一段講的是「我為什麼在整理這件事」嗎？
- [ ] 有沒有 AI 句型：`不再只是...而是`、`這不是 primary source...`、`為什麼 X...？`
- [ ] Source caveat 有服務於判斷嗎？還是只是審稿註解？
- [ ] 有沒有保留使用者心聲 / 括號？
- [ ] 是否有起承轉合？
- [ ] 是否有「所以統整完...」的 conclusion？
- [ ] 投資邏輯有沒有走 demand → bottleneck → required capability → BOM/ASP/volume → company → financial verification → counter？
- [ ] 是否避免把 internal framework 字眼直接丟到公開稿（Hook / Observation / Counter / bull-case kill）？

## Rule Promotion Candidate

不要現在立刻升正式 Cursor rule。先用這份 lesson 寫 #002 / #003。

若連續 2-3 張 card 都使用這套 voice pattern 且 user 接受，再新增：

```text
.cursor/rules/content-card-voice.mdc
```

Minimal future rule wording:

```text
Content cards should read like the user's research voice, not an explainer.
Start with a memorable observation, keep the user's uncertainty and parenthetical
inner voice, avoid AI contrast formulas, and end with what the user currently
understands after organizing the evidence.
```

## Linked

- Card #001: [content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md](../../content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md)
- Review page: [content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html](../../content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html)
- Workflow audit: [ops/decisions/2026-05-13_workflow-rule-audit-card-001.md](./2026-05-13_workflow-rule-audit-card-001.md)
