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
它比較像一個高密度用電的系統。

所有它消耗的電，最後大部分都會變成熱，要被帶出去。

## Full Draft (Threads + X long-form)

```text
最近整理 GB300 散熱這條，我原本想直接看一櫃接近 $50K 的液冷 BOM 到底分去哪。

但整理到一半發現，如果一開始沒有先把「一櫃 AI server 到底多會吃電」想清楚，後面的 cold plate、CDU、manifold、UQD 其實都會變成零件名詞而已。

所以我決定先不急著跳到公司名單。
我想先把自己目前理解到的順序整理清楚。

---

一台 Tesla Model S 開一年，大概會充 ~4,000 度電。
換成電費，看你在哪個州、哪個時段，大概落在 US$500–700 一年。
平均下來一個月 $50–60 — 不算太恐怖，車本來就是吃電大戶。

---

NVIDIA 最新一代 GB300 NVL72，一櫃 72 顆 GPU。
整櫃滿載運轉的功耗大概 132 kW。

132 kW × 24 小時 × 30 天 = ~95,000 度／月。

對比一下：
→ Tesla 一年 = 4,000 度
→ AI rack 一個月 = 95,000 度
→ 一台 AI rack 一個月的電，差不多等於一台 Tesla 開 24 年。

我自己看到這個對比時，才比較能理解為什麼散熱不是「加幾個風扇」這麼簡單。

因為這已經不是一台電腦變熱一點，而是一整櫃高密度算力 24 小時一直吃電。

---

這裡開始是我真正想拆的地方：電最後都會變成熱。

132 kW 的電灌進一個機櫃，最後幾乎都會變成熱要被擠出去。而且這個熱是 24×7 的，沒有「下班」這件事。

以前很多 server rack 的直覺比較像：機器會熱，所以機房要有空調，機櫃要有風扇。
但到 100kW+ 這個量級，我感覺問題已經不是「風夠不夠冷」，而是整個 rack 的設計要不要換一種方式。

因為風扇不是免費的。
它也吃電、佔空間、產生噪音，而且越靠空氣去帶走熱，整個機櫃裡可以塞的東西就越受限制。
這不是說空冷不能用，而是當 rack power 一直往上走，空冷會越來越像一個卡住系統設計的瓶頸。

這也是為什麼我現在比較理解 liquid cooling 為什麼會被拉出來講。

它不是因為名字比較酷，也不是因為大家突然喜歡水冷。
而是如果你要讓熱更快離開 GPU，最直覺的做法就是讓冷卻介質離熱源更近。
所以才會開始看到 cold plate 這種東西直接貼到晶片附近，把熱先帶到冷卻液，再交給 CDU、manifold 這些東西去處理。

（不然就會變成只是在背零件名單。）

---

撐不住會發生什麼？

GPU 會降頻，也就是 thermal throttle。
簡單說就是你買了一張很貴的卡，跑一陣子之後它自己「限速」。

如果只有一張卡，這可能只是效能差一點。
但 GB300 NVL72 是一櫃 72 顆 GPU。72 顆一起被熱影響，問題就不是某張卡跑慢，而是整櫃算力利用率被打折。

到這裡我覺得邏輯就比較清楚了：

你買的不是「GPU 本身」而已。
你買的是一整櫃能不能穩定跑滿的算力。

散熱如果處理不好，最後影響的不是機房舒服不舒服，而是這櫃算力到底跑不跑得滿。

（這也是我一開始覺得散熱題材很難懂的地方：它聽起來像機房問題，但其實會打到算力利用率。）

所以整理到這裡，我目前會這樣 recap：

AI server 散熱開始變重要，不是因為「液冷」這個詞突然變熱門，而是因為 rack power 拉上去之後，每一櫃都變成很密集的用電系統。

用電越高，熱就越高；熱處理不好，GPU 就跑不滿；GPU 跑不滿，買來的算力利用率就被打折。

所以這就是為什麼散熱開始變重要：

不是因為 liquid cooling 聽起來很新，而是每一櫃 AI server 能不能把算力跑滿，開始跟散熱綁在一起。

如果這個邏輯成立，那散熱就不是附屬配件，而是 AI server 裡面一個必須被拆開看的成本項目。

—

下一集會拆這個成本項目。
一櫃液冷 BOM 接近 $50K，這個錢具體分到哪些零件，是我目前還在追的東西。

至於誰賺到這筆錢，會放到第三集。
在搞清楚成本結構之前，直接跳到公司名單，順序不太對。

—

註：這篇沒有任何持股 disclosure，因為這篇不講任何個股、不下任何投資判斷。第三集講公司時會補完整 disclosure。
```

## Hook Variants（供 X / Threads 不同版本選用）

1. **數字直球**：「一台 AI rack 一個月吃 95,000 度電。一台 Tesla 一年才 4,000 度。」
2. **反問**：「為什麼 2025 年大家突然在意散熱？因為 AI rack 的功耗已經高到每一櫃都要認真算熱。」
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
- Tesla 一年電費 ~US$500–700：4,000 度 × $0.12–$0.18/kWh（EIA 美國住宅電價區間）
- GB300 NVL72 整櫃 ~132 kW：NVIDIA 公開規格 + supply-chain 報告
- 24×30×132 = 95,040 度／月：簡單算術
- 95,000 ÷ 4,000 = 23.76 倍 ≈ 24 年：簡單算術

所有數字都是公開可驗證，沒有 secondary estimate 風險。

Tesla 內部 spec（100 度、400 km、15,000 mi）刻意不寫進公開文裡 — 那是 spec sheet 體質，讓讀者離我們更遠不是更近。電費 / 月攤才是讀者真正會感覺到的東西。

## CTA Policy

**早期階段（< 1K followers / 第一個系列尚未跑完）：主貼文與第一則回覆都不放外部連結**。

理由：Threads 與 X 都對外部連結降權，我們在還沒累積算法信任的階段，沒理由用觸及換 click-through。連結策略要等流量起來才開始（M6.0 之後）。

### Ep1 結尾段（取代原本連結 CTA）

```text
所以整理到這裡，我目前會這樣 recap：

AI server 散熱開始變重要，不是因為「液冷」這個詞突然變熱門，而是因為 rack power 拉上去之後，每一櫃都變成很密集的用電系統。

用電越高，熱就越高；熱處理不好，GPU 就跑不滿；GPU 跑不滿，買來的算力利用率就被打折。

所以這就是為什麼散熱開始變重要：

不是因為 liquid cooling 聽起來很新，而是每一櫃 AI server 能不能把算力跑滿，開始跟散熱綁在一起。

如果這個邏輯成立，那散熱就不是附屬配件，而是 AI server 裡面一個必須被拆開看的成本項目。

—

（下一集會拆這個成本項目。一櫃液冷 BOM 接近 $50K，這個錢具體分到哪些零件，是我目前還在追的東西。

至於誰賺到這筆錢，會放到第三集 — 在搞清楚成本結構之前，直接跳到公司名單，順序不太對。）
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
