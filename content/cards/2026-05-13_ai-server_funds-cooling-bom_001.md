---
workflow: content-production
artifact_type: thesis-card
risk: high
lens: 資金
platform_target: x+threads
counter_direction: bull-kill
backbone_ref: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
backbone_section: "第三條 / 散熱：GPU power 突破空氣冷卻物理上限"
sources:
  - LianLi Work / Morgan Stanley supply-chain estimate (secondary, cooling BOM)
  - EE Times China cooling system breakdown (secondary, component mix)
  - Taipei Times / TrendForce GB300 shipment and cooling adoption comments (secondary)
created_at: 2026-05-13
public_status: ready
target_word_count: 350-450
position_disclosure: "generic disclosure; author may hold mentioned names"
---

# Card #001 — GB300 一櫃液冷 BOM 接近 $50K，先別急著喊散熱概念股

> Ready 狀態：已把原 outline 的「42% of rack cost」降級為 unresolved，
> 不在 public draft 內使用；IA1 gate 已 approve。下一步是排程 / 發布。

## Hook

> 資金 lens：GB300 NVL72 一櫃液冷 BOM，公開拆解有一個很刺眼的數字：
> 接近 **$50K / 櫃**。我想先拆的是：這筆錢到底分到 cold plate、CDU、
> manifold、UQD 哪幾段。

### Hook Variants

1. 數字型：`GB300 一櫃液冷 BOM 接近 $50K，這筆錢 2026 流去哪幾家？`
2. 反直覺型：`AI server 最貴的不只 GPU，還有一整套防止 GPU 變烤箱的液冷管路。`
3. 資金流型：`一櫃 AI rack 變成 130kW+ 熱源後，散熱開始有自己的 BOM 線。`

## Observation

公開資料目前能支撐的說法：

- LianLi Work 引 Morgan Stanley / supply-chain data：GB300 NVL72 單櫃液冷
  BOM 約 **$49,860**，GB200 約 $41,500，約 +20%。
- EE Times China 拆 cooling system 成本結構：cold plate 40-45% / CDU 30-35% /
  UQD 15-20% / manifold 5-10%。
- Taipei Times 引 TrendForce：GB300 今年預計占 global AI server rack
  shipments 70-80%；2026 仍以 liquid-to-air 過渡方案為主，liquid-to-liquid
  會在 2027 更明顯。

Source label：以上是公開拆解 / secondary estimate，還沒對到 NVIDIA 或供應商
primary disclosure。原 outline 的「$49,860 占 $600K 機櫃 42%」有明顯
arithmetic conflict；$49,860 / $600,000 = 8.31%，所以 draft 不使用
「42% of rack cost」這句。

## Mechanism

NVIDIA rack 的問題很直接：功耗變成熱。LianLi Work 的拆解寫到，GB300
NVL72 滿配 rack 功耗約 132-140kW，單顆 B300 GPU TDP 到 1400W。空氣冷卻
要帶走這個熱量，風量、噪音、風扇耗電都會變得不合理。

簡化看，功耗路徑是這樣：

```text
Hopper H100   700W
Blackwell B200 / B300 1000-1400W
Vera Rubin 方向仍往更高 rack power density
```

一旦 rack power density 穿過風冷舒適區，散熱就從風扇 + heat sink 變成
整套 plumbing：cold plate 貼晶片、CDU 分配冷卻液、manifold 管路分流、
UQD 讓 tray 可維修不漏液。這就是為什麼散熱從旁料變成系統級 BOM。

## Implication

具體受惠要拆零件，不要只講「散熱概念股」：

- **奇鋐 / AVC**：cold plate、液冷模組 exposure，最直接連到 direct-to-chip。
- **雙鴻 / Auras**：manifold / liquid cooling solution。
- **Vertiv**：rack / data center 層級 cooling infrastructure。
- **建準 / Sunon**：仍有 hybrid air/liquid 設計時受惠，但純液冷主鏈條較弱。

觀察訊號：

1. NVDA 下一代架構 power envelope（如果 Rubin 往 160kW+ rack power 走，
   液冷必要性更高）
2. 奇鋐 / 雙鴻 / Vertiv 接下來 2 季法說，明確 disclose NVDA 平台暴露
   百分比
3. Vertiv backlog 變化（先行指標）

時間框架：3-5 年結構性，不是 1-2 季題材。

## Counter

> 必填欄位，必須帶 threshold + time-window，必須標明 direction。

反向檢查：如果 2026-2027 主流 AI rack 還是以過渡型液冷為主，沒有更快走向
direct-to-chip / 全液冷，那 cold plate、manifold、CDU 這些零件的成長速度
可能就沒有想像中快。

第二個 Counter：如果 immersion cooling（浸沒式）成為主流，cold plate +
manifold 受惠結構會被打散，受惠對象換成不同供應鏈（化學材料 + tank 供應
商而非 cold plate / manifold 廠）。**Threshold：immersion 在新建 AI data
center 滲透率 > 20%，目前 < 5%。Time-window：2027-2028 才需要重新評估。**

## Caveat

> 1 句話 acknowledge 1 個具體 gap。voice profile 那種「我目前覺得 / 還沒
> 驗證」語氣。

我目前還沒驗證的是 BOM 口徑：`$49,860 / 櫃`、`$380K / 櫃`、`42%` 這幾個
公開拆解數字彼此不完全一致，所以發布前我只會用「接近 $50K / 櫃」這個較可
追溯說法，不寫「占整櫃 42%」。

## Draft Post（X Long Post）

GB300 一櫃要花接近 **$50K** 在液冷上。

這是我最近整理 AI server 供應鏈時，覺得最有記憶點的一個數字。

我先從整櫃這件事講起。

GB300 NVL72 不是一張 GPU，而是 NVIDIA 新一代 AI server rack。
一櫃裡面有 72 顆名字叫 B300 的 GPU，滿載功耗大概 132-140kW。

140kW 是什麼概念？

你可以先不用管工程細節，只要知道：這一櫃本質上就是一個很貴、很密集的熱源。

熱排不出去，GPU 會 thermal throttle，也就是自己降速保命。你買了很貴的算力，但跑不滿，就是在浪費錢。大企業當然不會讓這種事發生。

所以液冷開始從 optional 變 required。
這就是為什麼散熱開始從「風扇」變成「一整套水路」。

拆開看，大概有幾段：

- cold plate：貼在晶片上，把熱帶到冷卻液
- CDU：整櫃冷卻液循環的主機
- manifold：把冷卻液分到不同 tray
- UQD：快接頭，讓 tray 可以維修又不漏液

公開拆解資料給的量級是：GB300 NVL72 單櫃液冷 BOM 約 **$49,860**，GB200 約 $41,500。

BOM 就是零件成本表。這個數字不是某家公司直接賺到的營收，但它告訴我：每一櫃 AI server 裡，散熱這個 category 的 content 變大了。

對應到公司，先粗分會是：

- 奇鋐 / AVC：cold plate、液冷模組
- 雙鴻 / Auras：manifold、液冷 solution
- Vertiv：rack / data center 層級 cooling infrastructure

所以這條線我會這樣看：

AI 算力需求上升
→ GPU power density 上升
→ rack cooling 從 optional 變 required
→ cooling BOM per rack 上升
→ 對應零件供應商的 ASP / volume 有機會上升
→ 最後回到法說驗證 revenue、margin、backlog

我目前比較想追三個訊號：

1. NVIDIA 下一代 rack power envelope 有沒有繼續往上
2. 奇鋐 / 雙鴻法說有沒有講 AI rack / NVDA 平台 exposure
3. Vertiv 的 cooling infrastructure backlog 有沒有真的放大

這條線我會先放一個反向檢查點（算一種利多出盡吧）：如果未來兩年 AI rack 還是以過渡型液冷為主，沒有更快走向 direct-to-chip / 全液冷，那 cold plate、manifold、CDU 這些零件的成長速度可能就沒有想像中快。

但至少目前看到的產業資料，方向是 OK 的。

所以統整完上面這些資料，我目前得到的結論是：

散熱開始被市場重新看見，我現在理解比較像是：AI server 變成一櫃一櫃的系統在賣，所以它上面的散熱組件也會被一起綁進去。只要 rack-level system 出貨，cold plate、CDU、manifold 這些東西就會跟著有連帶關係。

如果未來一切都很美好，AI rack 繼續往更高功耗走，這條線會繼續值得追。反過來，如果液冷 adoption 卡在過渡方案，或供應商法說沒有轉成 backlog / margin，那就要小心一點。

但我目前覺得本質沒有變。只要算力還在短缺，rack power 還在往上，液冷應該就是 AI server 基本面裡一個很好的支撐點。

完整 AI server 供應鏈地圖（CPU / ASIC / HBM / 散熱 / 被動 + 3 條結構性 layer）：
https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/

持倉揭露：作者可能持有文中提及個股，內容僅作研究紀錄，不構成投資建議。

## Platform Ship Versions

> Status: draft platform adaptation based on official X / Threads ranking docs.
> Not yet validated against real swipe examples.
>
> Source: `research/swipe/2026-05-14_x-threads-card-001-official-platform-pass.md`

### X Version

```text
GB300 一櫃要花接近 $50K 在液冷上。

這是我最近整理 AI server 供應鏈時，覺得最有記憶點的一個數字。

先翻成人話。

GB300 NVL72 不是一張 GPU，而是 NVIDIA 新一代 AI server rack。一櫃裡面有 72 顆 B300 GPU，滿載功耗大概 132-140kW。

140kW 是什麼概念？

你可以先不用管工程細節，只要知道：這一櫃本質上就是一個很貴、很密集的熱源。

熱排不出去，GPU 會 thermal throttle，也就是自己降速保命。你買了很貴的算力，但跑不滿，就是在浪費錢。大企業當然不會讓這種事發生。

所以液冷開始從 optional 變 required。
這就是為什麼散熱開始從「風扇」變成「一整套水路」。

拆開看，大概有幾段：

- cold plate：貼在晶片上，把熱帶到冷卻液
- CDU：整櫃冷卻液循環的主機
- manifold：把冷卻液分到不同 tray
- UQD：快接頭，讓 tray 可以維修又不漏液

公開拆解資料給的量級是：GB300 NVL72 單櫃液冷 BOM 約 $49,860，GB200 約 $41,500。

BOM 就是零件成本表。這個數字不是某家公司直接賺到的營收，但它告訴我：每一櫃 AI server 裡，散熱這個 category 的 content 變大了。

也就是說，NVIDIA 每賣出一台 AI server rack，上面就會綁一套液冷系統。這套系統不是只有一顆風扇，而是 cold plate、CDU、manifold、UQD 這些零件加起來的一包 BOM。

對應到公司，先粗分會是：

- 奇鋐 / AVC：cold plate、液冷模組
- 雙鴻 / Auras：manifold、液冷 solution
- Vertiv：rack / data center 層級 cooling infrastructure

所以這條線我就會這樣理解：

現在很明顯大家都在用 AI，算力需求上升這件事應該是不爭的事實
→ GPU power density 上升
→ rack cooling 從 optional 變 required
→ cooling BOM per rack 上升
→ 對應零件供應商的 ASP / volume 有機會上升
→ 最後回到法說驗證 revenue、margin、backlog

如果要進行後續追蹤的話，我目前比較想追三個訊號：

1. NVIDIA 下一代 rack power envelope 有沒有繼續往上
2. 奇鋐 / 雙鴻法說有沒有講 AI rack / NVDA 平台 exposure
3. Vertiv 的 cooling infrastructure backlog 有沒有真的放大

這條線我會先放一個反向檢查點（算一種利多出盡吧）：如果未來兩年 AI rack 還是以過渡型液冷為主，沒有更快走向 direct-to-chip / 全液冷，那 cold plate、manifold、CDU 這些零件的成長速度可能就沒有想像中快。

但至少目前看到的產業資料，方向是 OK 的。

所以統整完上面這些資料，我目前得到的結論是：

散熱開始被市場重新看見，我現在理解比較像是：AI server 變成一櫃一櫃的系統在賣，所以它上面的散熱組件也會被一起綁進去。只要 rack-level system 出貨，cold plate、CDU、manifold 這些東西就會跟著有連帶關係。

如果未來一切都很美好，AI rack 繼續往更高功耗走，這條線會繼續值得追。反過來，如果液冷 adoption 卡在過渡方案，或供應商法說沒有轉成 backlog / margin，那就要小心一點。

但我目前覺得本質沒有變。只要算力還在短缺，rack power 還在往上，液冷應該就是 AI server 基本面裡一個很好的支撐點。

這邊我比較好奇的是：如果你也在看 AI server 供應鏈，你會先追散熱、HBM，還是 ASIC 這幾條線？

完整 AI server 供應鏈地圖：
https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/

持倉揭露：作者可能持有文中提及個股，內容僅作研究紀錄，不構成投資建議。
```

### Threads Version

```text
1/

GB300 一櫃要花接近 $50K 在液冷上。

這是我最近整理 AI server 供應鏈時，覺得最有記憶點的一個數字。

我先從整櫃這件事講起。

GB300 NVL72 不是一張 GPU，而是 NVIDIA 新一代 AI server rack。

一櫃裡面有 72 顆名字叫 B300 的 GPU，滿載功耗大概 132-140kW。

2/

140kW 這件事，對我來說重點不是工程數字，而是它代表這一櫃本質上就是一個很貴、很密集的熱源。

熱排不出去，GPU 會 thermal throttle。你買了很貴的算力，但跑不滿，就是在浪費錢。

3/

所以液冷開始從 optional 變 required。

這也是我覺得「散熱」不能只用風扇概念股去看的原因。

拆開看，它其實有幾段：

- cold plate：貼在晶片上，把熱帶到冷卻液
- CDU：整櫃冷卻液循環的主機
- manifold：把冷卻液分到不同 tray
- UQD：快接頭，讓 tray 可以維修又不漏液

這些東西加起來，才是 AI rack 裡的液冷系統。

4/

BOM 就是零件成本表。

公開拆解資料給的量級是：

- GB300 NVL72 單櫃液冷 BOM 約 $49,860
- GB200 約 $41,500

我不會拿它算很精準的模型，但它至少說明：每一櫃 AI server 裡，散熱這個 category 的 content 變大了。

也就是說，NVIDIA 每賣出一台 AI server rack，上面就會綁一套液冷系統。

這套系統不是只有一顆風扇，而是 cold plate、CDU、manifold、UQD 這些零件加起來的一包 BOM。

5/

對應到公司，先粗分：

- 奇鋐 / AVC：cold plate、液冷模組
- 雙鴻 / Auras：manifold、液冷 solution
- Vertiv：rack / data center 層級 cooling infrastructure

這不是「看到名字就買」，而是先放進 watchlist。

因為真正要驗證的是：它們在 AI rack 裡的 exposure，有沒有轉成 revenue、margin、backlog。

6/

所以這條線我就會這樣理解：

AI 算力需求上升
→ GPU power density 上升
→ rack cooling 從 optional 變 required
→ cooling BOM per rack 上升
→ 對應零件供應商的 ASP / volume 有機會上升
→ 最後回到法說驗證 revenue、margin、backlog

7/

如果要進行後續追蹤，我會看三個訊號：

1. NVIDIA 下一代 rack power envelope 有沒有繼續往上
2. 奇鋐 / 雙鴻法說有沒有講 AI rack / NVDA 平台 exposure
3. Vertiv 的 cooling infrastructure backlog 有沒有真的放大

8/

反向檢查點（算一種利多出盡吧）：

如果未來兩年 AI rack 還是以過渡型液冷為主，沒有更快走向 direct-to-chip / 全液冷，那 cold plate、manifold、CDU 這些零件的成長速度可能就沒有想像中快。

但至少目前看到的產業資料，方向是 OK 的。

9/

所以統整完上面這些資料，我目前得到的結論是：

散熱開始被市場重新看見，我現在理解比較像是：AI server 變成一櫃一櫃的系統在賣，所以散熱組件也被一起綁進 BOM。

只要 rack-level system 出貨，cold plate、CDU、manifold 這些東西就會有連帶關係。

10/

如果未來一切都很美好，AI rack 繼續往更高功耗走，這條線會繼續值得追。

如果液冷 adoption 卡在過渡方案，或供應商法說沒有轉成 backlog / margin，那就要小心一點。

但我目前覺得本質沒有變。

只要算力還在短缺，rack power 還在往上，液冷應該就是 AI server 基本面裡一個很好的支撐點。

11/

完整 AI server 供應鏈地圖：
https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/

如果你也在看 AI server 供應鏈，你會先追散熱、HBM，還是 ASIC 這幾條線？

持倉揭露：作者可能持有文中提及個股，內容僅作研究紀錄，不構成投資建議。
```

### Publish Hypothesis

```text
Concrete BOM number + raw research voice will create more depth signal than a
generic AI server supply-chain post.
```

Expected mechanism:

- X: first-line number drives stop/click; question CTA invites replies; author
  should reply to early comments.
- Threads: segmented explanation increases read-through and reply likelihood;
  conversational CTA asks readers to classify the theme.

### Success Metrics

First 72h primary metrics:

- replies with real questions or pushback
- saves / bookmarks
- profile clicks / follows
- library link clicks

Secondary metrics:

- likes
- reposts
- impressions

## CTA + Footer

```text
完整 8 條支線地圖（CPU / ASIC / HBM / 散熱 / 被動 + 3 條 layer）
在 library：https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/

下一張會拆 MediaTek $2B 為什麼是 management expectation 不是 revenue。

持倉揭露：作者可能持有文中提及個股，內容僅作研究紀錄，不構成投資建議。
```

## Platform Adaptation Notes

- **X long post**：整張 card 一個 post block，hook 第一行強烈，
  Mechanism 用空行分段。Source label 在 Observation 段用括號。
- **Threads carousel**（7 slides）：
  - Slide 1: Hook
  - Slide 2: Observation（4 個 bullet 放這裡）
  - Slide 3-4: Mechanism（兩 slides 分：power 翻倍 / BOM 結構升級）
  - Slide 5: Implication
  - Slide 6: Counter
  - Slide 7: Caveat + CTA

## Review Checklist

- [x] Hook 用 lens 命名（資金）
- [x] Observation 有具體 source + label
- [x] Mechanism 是 plain Chinese
- [x] Mechanism 不是 tautology
- [x] Implication 有 company / supplier category + signal + timeframe
- [x] Counter 有 explicit threshold + time-window
- [x] Counter direction 標明（bull-kill）
- [x] Caveat 是具體 gap
- [x] CTA 連到 backbone library page（投產 URL）
- [x] Disclaimer footer
- [x] 字數 350-500
- [x] 含投資宣稱 → 過 IA1 gate

## Pre-publish TODO

- [x] Resolve public wording for cooling BOM denominator conflict：public draft
      uses `~$50K / rack` and explicitly avoids 「占整櫃 42%」；underlying
      source conflict remains as caveat, not as a blocker to safe wording
- [x] Add generic position disclosure and restore named-company watchlist references（Q1=D revised by user: OK to name companies with disclosure）
- [ ] Fact-check 奇鋐冷板市占（NVDA-only vs all-platform 口徑；internal follow-up only unless named companies return to draft）
- [ ] 找 1 條 primary / investor-relations source cross-check 液冷 demand
      （Vertiv backlog / NVIDIA rack power / supplier call）
- [ ] Polish hook 措辭（測試 3 個變體：問句 / 數字驚嘆 / 直接命題）
- [x] 確認 backbone HTML library 部署 URL — Vercel
      `https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/`
- [x] 過 IA1 gate（含投資宣稱）

## Metrics（發布後填）

```yaml
metrics:
  impressions_24h:
  impressions_72h:
  impressions_7d:
  likes_7d:
  reposts_7d:
  replies_7d:
  saves_7d:
  follows_attributed:
  link_clicks:
  qualitative:
    -
  reflection:
    repeat_pattern:
    drop_pattern:
```
