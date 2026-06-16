---
workflow: content-production
artifact_type: series-bible
series: ai-server-overview
theme_backbone: research/knowledge/ai-server-supply-chain/ (internal artifact — knowledge map + primer)
internal_raw_source: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
failed_public_reference: research/knowledge/ai-server-supply-chain/series/overview/ep1-one-map.html (failed public artifact — see ops/postmortems/2026-06-01_a1-001-ep1-one-map_postmortem.md; reference only, do NOT render)
audience: 工程 / 科技背景、想理解 AI 供應鏈但不想只聽口號的中文讀者與理性散戶
owner_approved: false
owner_approved_at:
link_phase: early
created_at: 2026-06-01
---

# Series Bible — AI Server Overview

> 依 [docs/CONTENT_CONVERSION_PIPELINE.zh.md](../../../docs/CONTENT_CONVERSION_PIPELINE.zh.md)。
> 這是「我們知道什麼（內部 artifact）」與「我們要教什麼（公開產出）」之間的邊界。
> **未經 owner 核准前，不得生成任何公開產出。**
>
> 內部素材來源是知識地圖 / primer / 內部 raw article；**公開產出是重新創作，不是
> 渲染**。舊的 `ep1-one-map.html` 是「失敗的公開 artifact」，只當失敗範例參考。

## 1. 受眾（Audience）

- 誰：工程師 / PM / 設計 / 科技背景的人，加上想把市場「看懂」而不是「聽明牌」的
  理性散戶。
- 現在已懂：聽過 AI、聽過 NVIDIA、知道 GPU 很紅。
- **現在還不懂（起點誤解）**：以為「AI server = 一張（或很多張）很猛的 GPU」，
  以為買 AI 就是買 GPU。
- 為什麼看：想搞懂「AI 供應鏈到底在講什麼」，但被一堆英文術語勸退過。

## 2. 承諾（Promise）

看完整個系列，你能把「AI server 供應鏈」從一句口號，變成一張**你自己講得出來的
地圖**：知道這台機器大致由哪幾塊組成、錢從哪流到哪、每一層在卡什麼、以及「受惠的
是誰」這個問題該怎麼問。

## 3. 系列定位（Positioning）

- 對齊 North Star：**不是報明牌，是做地圖。**
- 這個系列是整個帳號的「第一張地圖」，也是 explainer → mechanism → thesis 三階段
  弧的示範。
- 早期階段：主貼文與第一則回覆不放外部連結（`link_phase: early`）。

## 4. EP0–EP7 地圖（每集一句 one-takeaway）

> 規則：每一集只能有**一句** one-takeaway。EP0–EP2 是科普（無公司名、無術語）；
> EP3–EP5 是機制（必要時才點名，且每集最多引入 1 個新詞並立刻白話解釋）；
> EP6–EP7 是 thesis（可含觀察線與持倉揭露，counter 先於結論）。

| 集 | 階段 | 標題方向 | One-takeaway（一句話） |
|----|------|----------|------------------------|
| EP0 | explainer | 為什麼要做這張地圖（系列開場 + 我從搞錯到搞懂） | 看 AI 供應鏈，先看懂「整台機器」，再看零件，才不會在背名詞。 |
| EP1 | explainer | AI server 到底是什麼 | **AI server 不是很多張 GPU，是一台很貴、很熱、很難組的機器。** |
| EP2 | explainer | 這台機器大概分成哪幾塊 | 這台機器大致分成「負責算、負責記、負責散熱、負責供電、負責組裝」幾塊，每塊都缺不得。 |
| EP3 | mechanism | 錢怎麼流 | 你付的一筆 AI 錢，會沿著這台機器被切成很多塊，流給不只一家公司。 |
| EP4 | mechanism | 為什麼「記」這塊會卡（記憶體） | 晶片算得再快，資料餵不進去也是空轉；這就是為什麼「記憶體」變成關鍵瓶頸。 |
| EP5 | mechanism | 為什麼「散熱」從小配件變大錢 | 太熱晶片會自己降速，所以散熱從小配件變成一筆非花不可的大錢。 |
| EP6 | thesis | 「受惠的是誰」該怎麼問 | 與其問「哪支受惠股」，先問「它卡在哪個非它不可的環節、財報有沒有驗證」。 |
| EP7 | thesis | 我目前在追的觀察線 + 什麼會推翻它 | 我把這條供應鏈當成一張會更新的地圖：這些訊號驗證它、這些訊號會推翻它。 |

> EP5 與既有的散熱子系列（`research/knowledge/.../series/thermal/`）可互相連結，但
> EP5 是「整台機器視角」的科普版，不是直接渲染散熱系列。

## 5. 語氣規則（Voice）

對齊 [docs/VOICE_PROFILE.zh.md](../../../docs/VOICE_PROFILE.zh.md) 與
[.cursor/rules/content-voice-raw-research.mdc](../../../.cursor/rules/content-voice-raw-research.mdc)。

- 第一人稱、研究中：「最近在整理…」「我以前也把它想得太簡單」。
- 保留不確定語氣：感覺 / 我想像中 / 應該比較像 / 還沒補完。
- 括號內心話與觀眾嘴替：用 `（…）` 補一句自己的 OS。
- 不用媒體解說腔（不要「這很重要，因為…」「核心 thesis」「重新定價」）。
- 不喊單（不要「這就是買點」「下一個贏家」）。
- 比喻只在能降低理解成本時用；不硬套、不講太滿。

## 6. 術語政策（Jargon Policy）

- **EP0–EP2（explainer）**：第一屏 **0** 個專有名詞。整集禁止裸用英文術語
  （NVIDIA 也先不出現在第一屏）。要講零件，用白話：算、記、散熱、供電、組裝。
- **EP3–EP5（mechanism）**：每集最多引入 **1** 個新詞，且第一次出現必須立刻白話
  解釋（例：HBM = 貼在晶片旁邊的高速記憶體）。公司名只在「結構上避不開」時出現。
- **EP6–EP7（thesis）**：可正常使用必要術語與公司名；thesis 集需含持倉揭露，
  counter / invalidation 先於任何看多結論。
- 全系列禁用清單（除非立刻白話解釋）：hyperscaler、capex、ODM、CoWoS、ABF、
  MLCC、cold plate、CDU、manifold、UQD、BOM。

## 7. 未驗證 / 偏弱的支線（Under-verified branches）

> 來源：內部 raw article 的「What Still Needs Verification」與各段 caveat。這些
> **不得在科普集當定論講**；進到 mechanism / thesis 集要標等級。

- 被動元件那條的 5 個訊號全部來自單一 publisher（DigiTimes）→ 公開前需補 1 條
  非 DigiTimes 來源。
- 信昌電「交貨期拉長」的原始公告 / 第三方追蹤仍 missing。
- AMD「>50% server CPU share」是 forward-looking target，不是目前市占。
- MediaTek「AI ASIC $2B Q4 2026」是 management expectation，不是已實現營收。
- Apple-Intel 是 preliminary、媒體報導、雙方 declined to comment，不是已簽訂單。
- 整櫃「~$600K」是業界拆解估計（LianLi），非官方報價。
- scenario-analyzer 尚未實跑；內部 article 仍待 final human edit。

## Owner 核准

- [ ] Owner 已 review 並同意 audience / promise / positioning / EP0–EP7 / voice /
      jargon policy / under-verified branches
- 核准後：`owner_approved: true` + 填日期；此後各集才可進入 Episode Contract。

## Disclaimer

This is research and education, not financial advice.
