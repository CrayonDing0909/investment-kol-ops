---
workflow: content-production
artifact_type: episode-contract
series: ai-server-overview
episode: 1
phase: explainer
series_bible_ref: content/series/ai-server-overview/series-bible.md
owner_approved: true
owner_approved_at: 2026-06-01
created_at: 2026-06-01
---

# EP1 Episode Contract — AI server 到底是什麼

> 依 [docs/CONTENT_CONVERSION_PIPELINE.zh.md](../../../docs/CONTENT_CONVERSION_PIPELINE.zh.md)。
> **未經 owner 核准前，不得生成 HTML / IG / Shorts / 公開貼文。**
> EP1 不能直接用知識地圖、不能是供應鏈清單、第一屏不能有公司名、hook 不能放 $600K。

## 1. 觀眾的起點認知（Audience starting belief）

「AI server 就是一張（或很多張）很猛的 NVIDIA GPU / 顯卡；買 AI ≈ 買 GPU。」
讀者聽過 GPU 很紅，但沒想過它其實是「一整台機器」，也被一堆英文術語勸退過。

## 2. 一句話 takeaway（One-sentence takeaway）

> **AI server 不是很多張 GPU，是一台很貴、很熱、很難組的機器。**

（這集只教這一句。與 series-bible 的 EP1 one-takeaway 一致。）

## 3. 這集不要講什麼（What NOT to say）

- 不列任何公司名（含 NVIDIA 在第一屏）。
- 不講「受惠股」、不給名單、不下買賣判斷。
- 不放 BOM 數字、不把 $600K 放進 hook（整集盡量不出現）。
- 不把它寫成供應鏈零件清單。
- 不堆術語、不一次丟一排英文。
- 比喻不要展開太滿（賽車比喻最多輕點一下）。

## 4. 禁用詞（Forbidden terms）

NVIDIA（第一屏）、hyperscaler、capex、ODM、HBM、CoWoS、ABF、MLCC、cold plate、
CDU、manifold、UQD、ASIC、BOM、rack（用「機櫃 / 一整台」代替）、$600K、132kW。

## 5. 允許用詞（Allowed vocabulary）

機器 / 一整台 / 一整套、晶片、運算卡（「一張很猛的運算卡」優於直接寫 GPU）、
記憶體、散熱、電源、組裝、發熱、全速運轉、缺一塊就跑不起來。
（GPU 一詞可出現，但描述成「一張很猛的運算卡」對新手更友善。）

## 6. 比喻（Metaphor）

「一台很貴、很熱、很難組的機器」：
- 貴 = 裡面不是只有一個核心零件，是一整套東西。
- 熱 = 一直全速運轉，熱到不能用一般電腦的方式處理。
- 難組 = 每一塊都要剛剛好接在一起，少一塊、卡一塊，整台就跑不起來。
（不展開賽車 / F1；點到為止。）

## 7. 第一屏術語預算（First-screen jargon budget）

第一屏不出現**新的、未解釋的**術語。允許 anchor terms：**AI server、GPU**。
除此之外，explainer 第一屏的陌生術語預算 = 0。

## 8. 理解目標（Comprehension target）

讀者看完，應該能用「自己的話」說出類似：

> 「喔，原來 AI server 不是一張卡，是一整台機器，所以背後牽涉的東西比我想的多很多。」

## 9. 下一集 tease（Next episode tease）

只 tease：「下一集我再拆——這台機器大概可以分成哪幾塊。」
不做任何投資判斷、不點名公司。

## 10. 語氣（Voice）

- 第一人稱、研究中、不確定語氣、括號內心話、觀眾嘴替。
- 開場用「最近在整理…我以前也把它想得太簡單」這種自承誤解的進入點。
- 結尾只 tease 下一集 + 一句「純研究 / 科普，沒有投資建議」。
- 對齊 series-bible §5 與已 owner-locked 的 EP1 Threads voice base（語氣方向）。

## Owner Comprehension 預檢（對齊 Gate A）

owner 核准合約前，先確認這份合約能導向「可理解的成品」：

1. [ ] 5 秒內知道這集要教什麼？
2. [ ] 看完能用一句話講出學到什麼？（= §8）
3. [ ] 第一屏陌生名詞 ≤ 預算（= 0）？
4. [ ] 這會是一個作品，還是資料堆疊？

## Owner 核准

- [x] Owner 已 review 並同意這份 EP1 Episode Contract（2026-06-01）
- 核准後：`owner_approved: true` + 填日期；**此後才可生成 EP1 公開產出**。

> 註：`owner_approved: true` **只代表 Episode Contract（方向合約）已核准，可以開始
> 產出 public draft**。它**不代表** Threads draft 已通過 Gate A，也**不代表**可以
> 發布。正式 Gate A 仍需在成品完成後執行 **Safety Check + Owner Comprehension
> Check**（見 [docs/HUMAN_GATES.zh.md](../../../docs/HUMAN_GATES.zh.md)）。

## Disclaimer

This is research and education, not financial advice.
