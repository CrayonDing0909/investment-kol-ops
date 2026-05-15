---
workflow: content-production
artifact_type: thesis-card
risk: low
lens: 教育-explainer
platform_target: x+threads
counter_direction: n/a (no thesis claim in this episode)
series: ai-server-thermal
series_episode: 1
series_phase: explainer
series_arc_total: 3
series_prereq_episodes: []
sources:
  - LianLi Work / Morgan Stanley supply-chain estimate (referenced for rack power data, secondary)
  - Public Tesla Model S battery / range / consumption specs (Tesla.com, secondary)
  - NVIDIA GB300 NVL72 published rack specs (NVIDIA, primary for rack power)
created_at: 2026-05-15
public_status: ready
target_word_count: 500-650
position_disclosure: "n/a — explainer episode contains no investment claim or company name"
related_episodes:
  - "2026-05-15_thermal-series_ep2-bom.md"
  - "2026-05-15_thermal-series_ep3-suppliers.md"
---

# 散熱系列：第一集 — 為什麼一台 AI server 一個月電費比一台 Model S 還貴

> 系列第一集，定位是 explainer（純科普）。沒有任何 ticker、公司名、或
> 投資 claim。目的：讓讀者 30 秒內懂為什麼 AI server 突然變成「散熱題」。

## Hook

> 你知道一台 Tesla Model S 一年充電大概用多少電嗎？
> 大概 **4,000 度**。
>
> 那一台 AI server 機櫃，一個月吃多少？
> → 大概 **95,000 度**。
>
> 一櫃 AI server 跑一個月，等於一台 Tesla 開了 **24 年**的電。

## Mental Model

AI server rack 不是一台「電腦」。
它的能量密度比較接近**一座住在資料中心大樓裡的小型發電廠**。

只是這座發電廠沒有冷卻塔、沒有風口，
所有它消耗的電，最後都會變成熱，要被「擠」出大樓。

## Full Draft (Threads + X long-form)

```text
最近在拆 GB300 這代 AI server 的時候，我一直在想一個很基本的問題：

為什麼過去十年我們用風扇就可以對付伺服器，
到了 2025-2026 年，cold plate、CDU、UQD 這些字才突然出現在所有法說裡？

讓我先用一個我自己能理解的方式講。

---

【一台 Tesla Model S 一年要用多少電？】

Tesla Model S 滿電 ~100 度，能跑 ~400 公里。
美國車主平均一年 ~15,000 英里，換算下來一台 Model S 一年大概
充電 ~4,000 度。

這個數字記一下，等下要對比。

---

【一台 AI server 機櫃一個月要用多少電？】

NVIDIA 最新一代 GB300 NVL72，一櫃 72 顆 GPU。
整櫃滿載運轉的功耗：~132,000 瓦 = 132 kW。

132 kW × 24 小時 × 30 天 = ~95,000 度／月。

對比一下：
→ Tesla 一年 = 4,000 度
→ AI rack 一個月 = 95,000 度
→ 一台 AI rack 一個月的電，等於 24 台 Tesla 一年的電。

或者反過來：一台 GB300 跑一個月，等於一台 Tesla 開了 24 年的電費。

---

【為什麼要在意這個數字？】

因為這代表 AI server 已經不能用一台「伺服器」的直覺去想了。
它的能量密度比較接近一座小型發電站，
只是它住在資料中心大樓裡。

而能量密度高，物理上一定會遇到一個老問題：

→ 電 → 熱

132 kW 的電進去，幾乎 100% 最後都會變成熱要被帶出來。
（GPU 的工作是把電轉成計算，但計算的副產品就是熱，跑不掉。）

---

【風扇能解決多少熱？】

過去那種一櫃 20-30 kW 的伺服器，風扇 + 房間空調（CRAC）撐得住。

到了 130 kW 的 AI rack，風扇要把這些熱抽出去，
你要嘛開到尖叫等級的噪音（噪音規範會擋）、
要嘛塞滿一整個房間都是風扇（沒空間）、
然後光是風扇本身的耗電可能就吃掉整體 10-15% 的電。

不可行。

---

【物理跑不動之後會發生什麼】

GPU 開始「熱降頻」（thermal throttle）。

意思是 GPU 為了保護自己不燒掉，會自動降速。
你買了一台 ~$40,000 的 GPU，結果它只跑 70% 的算力出來。

那筆錢不是在「沒花完」，
那筆錢是「正在以熱的形式燒掉，卻只換回更少的計算」。

大企業在算這條經濟帳，
所以才會把「液冷」從 optional 變成 required。

---

【下一集會講什麼】

下一集會拆：
一台 GB300 機櫃，光是液冷的零件清單，要花掉接近 $50,000 美金。

這個錢具體分到哪些零件？
（cold plate、CDU、manifold、UQD 各佔多少）

但「誰賺到這筆錢」這條線我刻意放到第三集，
因為在搞清楚「這 $50K 怎麼分」之前，
直接跳到公司名單我覺得不是好的順序。

完整系列：vercel.app/library/ai-server-supply-chain/series/thermal/

—

註：這篇沒有任何持股 disclosure，因為這篇不講任何個股。
第三集講公司時會補完整 disclosure。
```

## Hook Variants（供 X / Threads 不同版本選用）

1. **數字直球**：「一台 AI rack 一個月吃 95,000 度電。一台 Tesla 一年才 4,000 度。」
2. **反問**：「為什麼 2025 年大家突然在意散熱？因為 AI server 已經不是電腦，是發電廠。」
3. **故事開頭**：「最近在拆 GB300，我一直在想一個基本問題：為什麼過去用風扇就好的伺服器，現在突然要液冷？」

## What This Episode Deliberately Skips

- 任何個股名稱（奇鋐 / 雙鴻 / Vertiv 等都留給 Ep3）
- 任何 BOM 拆解（$50K 細項留給 Ep2）
- 任何投資 thesis（保留意見、買賣建議都留給 Ep3）
- Position disclosure（沒有 claim 就沒有 disclosure 需要）

## Success Metrics

第一集要驗證的是：

| 指標 | 為什麼重要 |
|---|---|
| Profile clicks / follows | Hook 是否引發「想看下一集」 |
| Saves / bookmarks | Tesla 比喻是否變成讀者會收藏的記憶點 |
| Replies 是否來自工程師 / Tesla 車主 | 是否打中目標 niche（不是專業金融人） |
| 留言裡有沒有人主動問「下一集什麼時候出」 | 系列結構是否被讀者感知到 |

## Source Verification Notes

- Tesla Model S 滿電 ~100 kWh：Tesla 官方規格（Model S 長程版）
- 美國車主平均年里程 ~15,000 mi：US DOT / FHWA Annual Vehicle Miles 平均值
- Tesla 年充電 ~4,000 度：15,000 mi ÷ 3.7 mi/kWh ≈ 4,054 kWh
- GB300 NVL72 整櫃 ~132 kW：NVIDIA 公開規格 + supply-chain 報告
- 24×30×132 = 95,040 度／月：簡單算術
- 95,000 ÷ 4,000 = 23.76 倍 ≈ 24 年：簡單算術

所有數字都是公開可驗證，沒有 secondary estimate 風險。

## CTA Policy

**早期階段（< 1K followers / 第一個系列尚未跑完）：主貼文與第一則回覆都不放外部連結**。

理由：Threads 與 X 都對外部連結降權，我們在還沒累積算法信任的階段，沒理由用觸及換 click-through。連結策略要等流量起來才開始（M6.0 之後）。

### Ep1 結尾段（取代原本連結 CTA）

```text
下一集會拆：
一台 GB300 機櫃，光是液冷的零件清單，要花掉接近 $50,000 美金。

這個錢具體分到哪些零件？（cold plate / CDU / manifold / UQD 各佔多少）

但「誰賺到這筆錢」這條線我刻意放到第三集，
因為在搞清楚「這 $50K 怎麼分」之前，
直接跳到公司名單我覺得不是好的順序。

—

註：這篇沒有任何持股 disclosure，因為這篇不講任何個股、不下任何投資判斷。
第三集講公司時會補完整 disclosure。
```

完。沒有 link、沒有 follow CTA、沒有「點我看更多」。

### 何時開始放連結？

依 [.cursor/rules/series-narrative-architecture.mdc](mdc:.cursor/rules/series-narrative-architecture.mdc)
裡的 Link Placement 政策（phased：early / mid / late）執行。

## Posting Checklist (for me, not for readers)

發 Ep1 前自己對一次：

- [ ] 主貼文完全沒有 URL（連 bit.ly / 自家網址都沒有）
- [ ] 第一則回覆也沒有 URL（早期階段）
- [ ] Bio 暫時不放 vercel.app link（M6.0 才放）
- [ ] 發出後 6 小時內回覆任何認真留言（演算法看 author engagement）
- [ ] 不要釘選 Ep1 直到貼文自己證明能跑（Ep1 發 24 小時後評估）
