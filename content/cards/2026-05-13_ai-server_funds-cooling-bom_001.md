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
public_status: draft
target_word_count: 350-450
---

# Card #001 — GB300 一櫃液冷 BOM 接近 $50K，這個錢 2026 流去哪幾家

> Draft 狀態：已把原 outline 的「42% of rack cost」降級為 unresolved，
> 不在 draft post 內使用。這張 card 還需要 IA1 gate 與 BOM 口徑 cross-check
> 才能 ready。

## Hook

> 資金 lens：GB300 NVL72 一櫃液冷 BOM，公開拆解有一個很刺眼的數字：
> 接近 **$50K / 櫃**。這不是「散熱概念股」四個字，而是 AI rack 從
> 風冷切到液冷後，錢開始流進 cold plate、CDU、UQD、manifold。

### Hook Variants

1. 數字型：`GB300 一櫃液冷 BOM 接近 $50K，這筆錢 2026 流去哪幾家？`
2. 反直覺型：`AI server 最貴的不只 GPU，還有一整套防止 GPU 變烤箱的液冷管路。`
3. 資金流型：`當一櫃 AI rack 變成 130kW+ 熱源，散熱就不再是旁料，而是資金流。`

## Observation

公開資料目前能支撐的說法：

- LianLi Work 引 Morgan Stanley / supply-chain data：GB300 NVL72 單櫃液冷
  BOM 約 **$49,860**，GB200 約 $41,500，約 +20%。
- EE Times China 拆 cooling system 成本結構：cold plate 40-45% / CDU 30-35% /
  UQD 15-20% / manifold 5-10%。
- Taipei Times 引 TrendForce：GB300 今年預計占 global AI server rack
  shipments 70-80%；2026 仍以 liquid-to-air 過渡方案為主，liquid-to-liquid
  會在 2027 更明顯。

Source label：以上都屬 **secondary / industry estimate**，不是 NVIDIA 或
供應商 primary disclosure。原 outline 的「$49,860 占 $600K 機櫃 42%」
有明顯 arithmetic conflict；$49,860 / $600,000 = 8.31%，所以 draft 不使用
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

## Counter（bull-case kill）

> 必填欄位，必須帶 threshold + time-window，必須標明 direction。

**（bull-case kill）** 如果 2026-2027 的主流 AI rack 仍長期停在
liquid-to-air 過渡設計，而且 direct-to-chip / liquid-to-liquid 滲透率沒有
突破 50%，純液冷零件（cold plate / manifold / CDU）的 revenue slope 會比
這張 card 暗示的慢。

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

GB300 一櫃液冷 BOM 接近 **$50K**，這筆錢 2026 流去哪幾家？

我現在比較不想用「散熱概念股」這種說法，因為太粗。
真正的變化是：AI rack 從風冷切到液冷後，散熱從旁料變成一整套 plumbing。

公開拆解資料顯示，GB300 NVL72 單櫃液冷 BOM 約 $49,860，GB200 約 $41,500。
EE Times China 拆 cooling system：cold plate 40-45%、CDU 30-35%、UQD
15-20%、manifold 5-10%。Taipei Times 引 TrendForce 說，GB300 今年可能占
global AI server rack shipments 70-80%。

為什麼會變成這樣？

因為功耗就是熱。GB300 NVL72 滿配 rack 約 132-140kW，單顆 B300 GPU TDP
到 1400W。空氣冷卻要帶走這個熱量，風量、噪音、風扇耗電都會變得不合理。

所以散熱不再只是風扇 + heat sink，而是 cold plate 貼晶片、CDU 分配冷卻液、
manifold 管路分流、UQD 讓 tray 可維修不漏液。這些東西開始變成 AI rack 的
必要 BOM。

拆資金流，直接看三層：

- 奇鋐 / AVC：cold plate、液冷模組 exposure
- 雙鴻 / Auras：manifold / liquid cooling solution
- Vertiv：rack / data center 層級 cooling infrastructure

我會看的驗證訊號不是股價，而是：NVDA 下一代 rack power envelope、奇鋐 /
雙鴻 / Vertiv 法說裡的 NVDA 平台暴露、Vertiv backlog。

（bull-case kill）如果 2026-2027 主流 AI rack 仍停在 liquid-to-air 過渡設計，
direct-to-chip / liquid-to-liquid 滲透率沒有突破 50%，純液冷零件的 revenue
slope 會比這張 card 暗示的慢。

我目前還沒驗證的是 BOM 口徑：不同公開拆解對 `$49,860 / 櫃`、`$380K / 櫃`、
`42%` 的母體不一致，所以我不會寫「占整櫃 42%」。

完整 AI server 供應鏈地圖之後會放在 library：`<library-url-pending>`

本內容是研究與教育，不是投資建議。

## CTA + Footer

```text
完整 8 條支線地圖（CPU / ASIC / HBM / 散熱 / 被動 + 3 條 layer）
在 library：crayonding.io/library/ai-server-supply-chain
（library 上線前暫填 placeholder URL）

下一張會拆 MediaTek $2B 為什麼是 management expectation 不是 revenue。

本內容是研究與教育，不是投資建議。
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
- [x] Implication 有 company + signal + timeframe
- [x] Counter 有 explicit threshold + time-window
- [x] Counter direction 標明（bull-kill）
- [x] Caveat 是具體 gap
- [ ] CTA 連到 backbone library page（暫填 placeholder）
- [ ] Disclaimer footer
- [ ] 字數 350-500
- [ ] 含投資宣稱 → 過 IA1 gate

## Pre-publish TODO

- [ ] Resolve cooling BOM denominator conflict：`$49,860 / 櫃` vs `$380K / 櫃`
      vs `42%` 的母體不一致，發布前不可寫「占整櫃 42%」
- [ ] Fact-check 奇鋐冷板市占（NVDA-only vs all-platform 口徑）
- [ ] 找 1 條 primary / investor-relations source cross-check 液冷 demand
      （Vertiv backlog / NVIDIA rack power / supplier call）
- [ ] Polish hook 措辭（測試 3 個變體：問句 / 數字驚嘆 / 直接命題）
- [ ] 確認 backbone HTML library 部署 URL
- [ ] 過 IA1 gate（含投資宣稱）

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
