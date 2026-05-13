---
workflow: content-production
artifact_type: thesis-card
risk: medium
lens: meta
platform_target: x+threads
counter_direction: n/a-meta-method
backbone_ref: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
backbone_section: "第三條 / 被動元件 + caveat"
sources:
  - DigiTimes 2026 5 篇被動元件報導（passive components source packet）
  - 個人 historical reading 對 DigiTimes 報導風格的觀察（subjective）
created_at: 2026-05-13
public_status: outline
target_word_count: 350-450
---

# Card #006 — 5 篇 DigiTimes 報導 = 1 個 publisher = 不算 source-backed

> Outline 狀態：題目 / 4 層風險已 seed。這張是 meta lens——談 method 而
> 不是 thesis，所以 Counter direction = n/a（meta lens 通常不需要 Counter
> direction，因為談的是研究方法本身）。
>
> 這張的 unique value：示範「translator + judgment guide」wedge——別人寫
> 結論，我寫「我為什麼還沒下結論」。對信任建立比 thesis card 更重要。

## Hook

> 我手上有 5 條被動元件漲價訊號，方向都一樣，全部來自 DigiTimes。
> 為什麼我還是把這條標成「evidence chain 偏窄」、不能算 source-backed？
>
> 這張不是談被動元件——是談「讀 source 時應該怎麼算 weight」。

## Observation

我手上被動元件這條的 5 個訊號（全部源自 DigiTimes 2026 報導）：

1. Yageo 子公司 Kemet 在 2026 第 3 次調漲鉭電容
2. Samsung Electro-Mechanics 評估 MLCC 漲 5-10%
3. AI server MLCC 訂單把產能需求拉到 2x baseline
4. Nichicon (NDB) 表示漲價是 demand-driven，不是原料 shock
5. Yageo 法說提到 AI 訂單強勁

**5 條方向全部一致：高階被動元件供需吃緊、漲價動能啟動**。

但 source label 必須誠實寫成 **secondary, single-publisher evidence chain**——
不是 source-backed。

## Mechanism

> 為什麼 5 條方向一致還不算 source-backed？單一 publisher 的 evidence
> chain 有 4 個結構性風險：

**Risk 1 — Publisher bias**

每個 publisher 都有 editorial 風格 / 客戶關係 / 文化偏向。DigiTimes 過去對
台灣 component 整體偏 bullish（這是個人 historical observation，沒有正式
統計）。同樣 5 條訊號從 Nikkei / Bloomberg / Reuters 寫，措辭強度可能完全
不同。Publisher bias 不是「他們寫錯」，是「他們選擇報哪些 + 怎麼 frame」。

**Risk 2 — Source compounding（訊號不獨立）**

如果 DigiTimes 5 條報導背後是同 1 個產業 contact 提供 5 條 leak，5 條訊號
彼此不獨立 → 你不能用 5 條訊號的方向一致來放大 conviction。實際上你只有
1 條訊號（被 5 個 article 包裝）。

**Risk 3 — Repackaging**

部分 DigiTimes 文章本質是 repackage 公司新聞稿或法說 highlight，不是獨立
reporting。如果原始 source 是公司自家 PR，5 條 repackage 仍然只有 1 個
原始來源。

**Risk 4 — 沒有 dissenting view**

單一 publisher 看不到反方論點。如果 Bloomberg 同期有篇「PC consumer demand
weakness 拖累 MLCC integrated demand」的反向報導，conviction 校準完全不
一樣。

**結論：同一個 publisher 5 條訊號，conviction 不能升 5 倍，只能升 ~1.5 倍**
（同一 publisher 的多條報導當作 1.5 條 weight，不是 5 條）。

## Implication

這條 backbone 的內部判斷已啟動（evidence chain 站得住、訊號方向強），
**但公開引用前必須補 1 條非 DigiTimes 來源**：

- 一手：Yageo / 華新科 / Samsung Electro-Mechanics 法說 transcript
- 二手非 DigiTimes：Nikkei / Bloomberg / Reuters
- 三方追蹤：Murata / TDK guidance（高階 MLCC 龍頭，guidance 是最先
  reflect 供需的地方）

觀察訊號：Yageo / 華新科 / Samsung Electro-Mechanics 接下來 2 季法說正式
disclose AI server 比例變化。Timeframe：1-2 季內。

## Counter（meta lens — 對 method 本身的 falsifiability）

> Meta lens 不需要對 thesis 寫 Counter（因為這張不是 thesis card），但
> 對「method 本身」應該保持 falsifiability。

對這個 method 的 Counter：

如果你能舉例 1 個 publisher 的 evidence chain 在 5 個獨立訊號下足夠
publish 結論，請告訴我為什麼。我目前的 baseline 是「同一 publisher 5 條
不獨立訊號 ≈ 1.5 條獨立訊號 weight」，但這個 ratio 是經驗值，不是統計
推導。

對 DigiTimes bias 的 Counter：如果有人 systematically track DigiTimes 過去
5 年預測 vs 實際 outcome 的 hit rate，發現 hit rate > 70%，「DigiTimes bias
bullish」這個 prior 就要 revise。我目前沒看到這個 systematic track。

## Caveat

「DigiTimes bias bullish」是我從歷史閱讀得到的個人觀察，不是有正式統計
支撐的 finding。如果有讀者有實證資料 disagree，歡迎留言/DM——這也是公開
寫 source 紀律的目的之一：把自己的 prior 攤開來接受挑戰。

## CTA + Footer（這張 card 的 CTA 比較特別）

```text
為什麼我寫 thesis card 而不是直接 publish backbone？因為 backbone 是判斷
地圖（會錯、會更新），card 是被驗證後的單一 commit。

完整 backbone 在 library：crayonding.io/library/ai-server-supply-chain
（library 上線前暫填 placeholder URL）

這個 backbone（AI Server Supply Chain）的 6 張 card 已全部公開，下個
backbone 主題還在挑——歡迎留言告訴我你想看哪個產業 deep dive：
- 機器人（VLA / humanoid / ROS）
- 量子（IBM / Google / Atom Computing 路線之爭）
- 電力 / 核能 small modular reactor
- 還是其他？

本內容是研究與教育，不是投資建議。
```

## Platform Adaptation Notes

- **X long post**：4 risks 用 numbered，「結論：1.5 倍 weight」獨立段落
  醒目。這張 hook 是元 message，可以用問句吸引。
- **Threads carousel**（7 slides）：
  - Slide 1: Hook（5 條方向一致為什麼還不算 source-backed）
  - Slide 2: Observation（5 條訊號 list）
  - Slide 3-4: Risks 1-2 / 3-4（兩 slides 拆 4 個 structural risk）
  - Slide 5: 「1.5 倍 weight」結論
  - Slide 6: Implication（公開引用前要補什麼）
  - Slide 7: Counter（method falsifiability）+ CTA（下個 backbone 主題投票）

## 為什麼這張 card 對 wedge 特別重要

這張示範你的 differentiator——別人寫「被動元件漲價，受惠 X / Y / Z」，
你寫「為什麼我還沒下結論」。在中文投資 KOL 圈，「先別下結論，先談 source
紀律」這個角度幾乎沒人在做。

預期效果：

- 互動數可能不如 #001 / #002（這張不夠「投資 actionable」）
- 但 follower quality 高 + 留言質量高 + 信任建立快
- **Backbone 主題投票** CTA 把社群變成研究選題的合作夥伴，提高下個 backbone
  的 product-market-fit
- 對 newsletter 訂閱轉換率潛在最高（meta lens 內容最能 hook 認真讀者）

## Review Checklist

- [ ] Hook 用 lens 命名（meta）+ 反直覺命題
- [ ] Observation 5 條訊號 list 清楚 + 全部 DigiTimes label
- [ ] 4 risks 每個都有具體 mechanism（不是「來源不夠」這種空話）
- [ ] 「1.5 倍 weight」結論明確
- [ ] Implication 列出 acceptable cross-check sources
- [ ] Counter 是對 method 的 falsifiability（不是對 thesis）
- [ ] Caveat 邀請 disagreement
- [ ] CTA 連 backbone + backbone 主題投票
- [ ] 字數 350-450
- [ ] medium risk（不含直接投資宣稱）→ 不需 IA1，但走 content review

## Pre-publish TODO

- [ ] Fact-check：DigiTimes 5 篇報導日期 + 是否確實全部出自 DigiTimes
- [ ] 思考是否要 generalize「1.5 倍 weight」這個 heuristic 為 reusable rule
      （可能變成 source-tutor 規則的補充）
- [ ] Polish hook（這張 hook 是元 message + 問句，要寫得有挑戰性）
- [ ] 確認 backbone library URL
- [ ] 決定 backbone 投票選項列表（目前列了 4 個候選，可以調整）

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
