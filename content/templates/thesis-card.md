---
workflow: content-production
artifact_type: thesis-card-template
risk: medium
status: template
created_at: 2026-05-13
target_word_count: 350-500
---

# Thesis Card Template

> Purpose：把 backbone document（如 internal article）裡的單一支線 / 單一
> mechanism 萃成一張 ready-to-publish 的公開短內容。300-600 字、X long post
> 或 Threads carousel 規格、保留完整因果鏈與 Counter。
>
> 設計原則：
>
> 1. 一張 card = 一個 mechanism + 一個 implication + 一個 Counter。
>    不是「把 backbone 整段貼出來」。如果你發現一張 card 想塞 2 個 mechanism，
>    拆成 2 張。
> 2. **Hook 用 lens 命名**，不是 click-bait。Lens 包括：資金、為什麼、基本面、
>    啟動、破局、meta（關於研究方法本身）。
> 3. **Counter 是必填，不是 nice-to-have**。每張 card 都要 publicly commit
>    到 falsifiability。Counter 必須有 threshold + time-window，還要標明
>    direction（bull-kill 或 bear-falsify）。
> 4. **Voice：hook + caveat 雙層結構**。Hook 強、body 保留你的「我目前覺得」、
>    Counter 用 falsifiable 語氣、Caveat 1 句承認還沒驗證的部分。
> 5. **每張 card 結尾連回 backbone HTML page**，把社群流量導到 library。
>    Backbone 是複利資產，card 是 channel。
>
> 與 analysis-reasoning rule 的關係：thesis card 套用 analysis-reasoning
> 4 步法（Observation → Mechanism → Implication → Counter）的 compressed
> 形式——每張 card 1 個完整 chain，而不是 backbone 那種 stacked multi-chain。
>
> （PR #13 merge 後，這個 template 應該明確 link `.cursor/rules/analysis-reasoning.mdc`，
> 並依 `ops/decisions/2026-05-13_analysis-reasoning-v2-suggestions.md` 套用 v2
> Counter 規則。本 template 已預先套用 v2 精神。）

## Frontmatter Fields

```yaml
workflow: content-production
artifact_type: thesis-card
risk: medium  # 含投資宣稱的 card 升級為 high，過 IA1
lens: <資金 | 為什麼 | 基本面 | 啟動 | 破局 | meta>
platform_target: <x | threads | x+threads>
counter_direction: <bull-kill | bear-falsify>
backbone_ref: <相對路徑到 backbone document，例：content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md>
backbone_section: <backbone 裡的章節 anchor，例：「第三條 / HBM」>
sources:
  - <primary source 1 與 source label，例：AMD Q1 2026 earnings call transcript / reported-fact>
  - <primary source 2>
created_at: YYYY-MM-DD
public_status: <draft | ready | scheduled | published>
published_at: <填發布後>
post_url: <填發布後>
target_word_count: 350-500
```

## Card Structure

### 1. Hook（1 句）

用 lens 直接命名 + 1 個具體 anchor（數字 / 公司 / 事件）。不要用「驚人地」、
「很多人不知道」這類空話。

範例：

- 資金 lens: `散熱在 GB300 機櫃裡占整櫃成本 42%——這個錢 2026 流去哪幾家。`
- 基本面 lens: `MediaTek $2B AI ASIC 是 management expectation，不是已實現營收。`
- 為什麼 lens: `為什麼 CPU 又被討論？memory wall 物理逼出 agent AI 的調度成本。`
- 啟動 lens: `Apple-Intel preliminary deal 是 Intel Foundry 第一個 hyperscale-tier 訊號。`
- 破局 lens: `3 個會讓我下調 AI server CPU 復興 thesis 的具體數字。`
- meta lens: `為什麼我把被動元件這條標成「evidence chain 偏窄」。`

### 2. Observation（1-2 句 with primary source label）

1 個具體事實 + source。Source label 用 `source-tutor-reading` 規則的分類：
`reported-fact` / `management-expectation` / `forward-looking-target` /
`secondary` / `my-interpretation`。

範例：

```text
TrendForce 整理：GB300 NVL72 散熱 BOM 約 $49,860 / 機櫃，占整櫃 ~$600K
成本 42%（reported-fact，2026/04 published）。
```

### 3. Mechanism（1 段，60-150 字）

A 為什麼會導致 B。用 plain Chinese、不用 institutional jargon。

不要：

- `底層原因是 power density 結構性轉變。`（institutional + tautology）
- `AI 帶動所以散熱受惠。`（tautology）

要：

- `Hopper H100 700W → Blackwell B200 1000W → Rubin R200 估 1300W。空氣
   冷卻在單顆 chip 大致極限就是 700W（受空氣熱容限制），超過就無法把熱
   及時帶走。一旦穿透，cold plate + CDU + manifold + UQD 整套液冷變必要
   BOM，散熱從原本 server 5% 不到的 commodity 旁料，變成 42% 大宗。`

### 4. Implication（1-2 句，要有 company + signal + timeframe）

不要：「值得關注」、「相關概念股」這種 hand-wave。

要：明確 company 名 + 觀察訊號 + timeframe。

範例：

```text
直接受惠：奇鋐（冷板 30%+ 市占）、雙鴻（manifold）、Vertiv（CDU 35%+ 價值
份額）。觀察訊號：奇鋐 / 雙鴻 / Vertiv 下兩季法說的 NVDA 平台暴露百分比。
時間框架：3-5 年結構性，不是 1-2 季題材。
```

### 5. Counter（1-2 句，必填，必須帶 threshold + time-window）

Counter 是這張 card 最重要的欄位。不是 nice-to-have。

格式：`如果 [具體可觀察事件 + threshold + time-window]，[mechanism / thesis]
[會發生什麼程度的 invalidation]。`

開頭明確標 direction：

- 對 bullish thesis card 用 `（bull-case kill）`：「如果 X，這條 thesis 會被
  挑戰」。
- 對 risk / bearish card 用 `（bear-case falsification）`：「如果 X，這個
  風險會降低」。

範例（bull-case kill，散熱）：

```text
（bull-case kill）如果 NVIDIA 後續架構從密集大顆走向 chiplet 切細 + per-chip
power 退回 700W 內，液冷必要性會局部回退到空冷。但 Blackwell / Rubin
roadmap 都還在 per-chip power 上升方向——這個 Counter 至少 2027 之前不會
發生。
```

範例（bear-case falsification，MediaTek 風險）：

```text
（bear-case falsification）如果 MediaTek 在 2026 Q2 或 Q3 法說公布具體主晶片
design win（hyperscaler 客戶名稱 + project size），track-record 與 subsystem-
confusion 兩個風險會同時降低；如果到 2026 Q4 仍只揭露 subsystem revenue 而
無主晶片 design win，risk 維持。
```

### 6. Caveat（1 句）

用 voice profile 的「我目前覺得 / 還沒驗證」語氣 acknowledge 1 個具體 gap。
不要寫制式 disclaimer 在這裡（disclaimer 走 footer）。

範例：

- `這篇用的散熱 BOM 數字主要來自 TrendForce 整理，公開引用前我會找 1 條
   非 TrendForce 來源（NVIDIA 法說 / Vertiv 季報 mention）做 cross-check。`
- `我目前還沒驗證的是：奇鋐冷板 30%+ 市占的口徑（是 NVDA 平台 only，還是含
   ASIC 平台），這個會影響受惠彈性的計算。`

### 7. CTA + Footer（2-3 行）

3 件事：

1. 連回 backbone HTML page（library 引流）。
2. 1 個下個動作（newsletter 訂閱、留言問題、follow）。
3. Disclaimer（1 句）。

範例：

```text
完整 8 條支線地圖在 library：crayonding.io/library/ai-server-supply-chain
下一張會拆 ASIC 那條為什麼是獨立故事，不是 GPU 外溢。
本內容是研究與教育，不是投資建議。
```

## Platform Adaptations

### X (Twitter) Long Post 形式

- 整張 card 一個 post block。
- Hook 變成第一行（粗體不行，但放最開頭）。
- Mechanism / Implication / Counter 用空行分段。
- Source label 用括號顯示。
- 結尾 CTA 連結（X 對 link 不友善，連結放最後一行）。

### Threads Carousel 形式

- Hook → slide 1（封面）。
- Observation → slide 2。
- Mechanism → slide 3-4（如果 mechanism 較長分 2 slides）。
- Implication → slide 5。
- Counter → slide 6。
- Caveat + CTA → slide 7。

### Both 平台同步發

- X 版先 ship，1 小時後 Threads carousel ship。
- 兩邊保留同樣 Hook，但 Threads carousel 可以用更多視覺。
- 互動數據分開記錄到 metrics（lens / platform / topic 三維度交叉）。

## Review Checklist（發布前必跑）

- [ ] Hook 用 lens 命名，不是 clickbait
- [ ] Observation 有具體 source + source label（reported-fact /
      management-expectation / etc.）
- [ ] Mechanism 是 plain Chinese，不是 institutional jargon
- [ ] Mechanism 不是 tautology（「需求增加 → 受惠」這類）
- [ ] Implication 有 company + signal + timeframe，不是「值得關注」
- [ ] Counter 有 explicit threshold + time-window
- [ ] Counter direction 標明（bull-kill 或 bear-falsify）
- [ ] Caveat 是具體 gap，不是制式 disclaimer
- [ ] CTA 連到 backbone library page
- [ ] Disclaimer footer 存在
- [ ] 整張 card 字數 350-500（X long post 限制 ~4000 字元；Threads carousel
      每 slide ~500 字元）
- [ ] 含投資宣稱 → 已過 IA1 gate（risk: high 的 card）

## File Convention

```text
content/cards/
  YYYY-MM-DD_<topic-slug>_<lens>_<short-id>.md
```

範例：

```text
content/cards/2026-05-13_ai-server_funds-cooling-bom.md
content/cards/2026-05-13_ai-server_fundamentals-mediatek-2b.md
```

`_index.md` 維護一張總表（card id / lens / platform / status / metrics）。

## Disclaimer

This is research and education, not financial advice.
