---
workflow: content-production
artifact_type: thesis-card
risk: medium
lens: 資金
platform_target: x+threads
counter_direction: bull-kill
backbone_ref: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
backbone_section: "第三條 / 散熱：GPU power 突破空氣冷卻物理上限"
sources:
  - TrendForce 2026/04 published research (secondary, aggregator)
  - NVIDIA Blackwell / Rubin power roadmap (reported-fact)
  - Vertiv 公開 ecosystem position (reported-fact)
created_at: 2026-05-13
public_status: outline
target_word_count: 350-450
---

# Card #001 — 散熱在 GB300 機櫃裡占 42% 成本，這個錢 2026 流去哪幾家

> Outline 狀態：6 個 section 都已 seed，hook / Counter direction 已決定，
> 數字需要 fact-check，最終 wording 還沒 polish。

## Hook

> 散熱在 GB300 NVL72 機櫃裡占整櫃 ~$600K 成本的 42%——一個過去
> 不到 5% 的 commodity 旁料變成 BOM 大宗。這個錢 2026 流去哪幾家，
> 為什麼是物理上回不去。

## Observation

TrendForce 整理（2026/04 published）：

- GB200 NVL72 散熱 BOM ~$41,500 / 機櫃
- GB300 NVL72 散熱 BOM ~$49,860 / 機櫃，占整櫃成本 42%
- 拆分：cold plate 40-45% / CDU 30-35% / UQD 15-20% / manifold 5-10%
- GB300 預計吃 2026 AI server 機架 70-80%；液冷在 AI chip 滲透率 2026 突破 50%

Source label：TrendForce 是 secondary aggregator；NVIDIA Blackwell roadmap
是 reported-fact；Vertiv ecosystem position 是 reported-fact 公開資料。

## Mechanism

> 寫的時候用 plain Chinese，不要 institutional jargon。

NVIDIA GPU power 每代翻倍：

```text
Hopper H100   700W
Blackwell B200 1000W
Rubin R200 估 1300W
```

空氣冷卻在單顆 chip 大約極限就是 700W（受空氣熱容、風扇噪音、rack 體積
限制）。超過 700W，空氣帶不走熱、chip 會 thermal throttle。

一旦穿透 → 必須切液冷：cold plate 直接貼 chip、coolant 流過 micro-channel
把熱帶走，傳熱效率比空氣高 1000x 以上。NVL72 一櫃 72 顆 GPU × 1.4kW =
100kW+，整櫃靠液冷。

BOM 結構性 uplift：原本散熱在 server 是 commodity 旁料（風扇 + heat sink，
總 BOM 不到 5%）；液冷一整套（cold plate 每 GPU 1 片、CDU 每櫃 1 台、
manifold 一整組、UQD 大量）變成 BOM 42%。從 commodity 變大宗，物理門檻
一旦穿透就回不去。

## Implication

具體受惠（不是「散熱概念股」這種空話）：

- **奇鋐**：冷板 30%+ 市占，最直接 levered 到 GB300 ramp
- **雙鴻**：manifold 主玩家
- **Vertiv**：CDU 拿 ecosystem 35%+ 價值份額
- 建準（fan）只在仍有 air/liquid hybrid 設計時受惠，levered 較弱

觀察訊號：

1. NVDA 下一代架構 power envelope（如果 Rubin Ultra → 1500W+ 需要更猛
   液冷，受惠彈性再放大）
2. 奇鋐 / 雙鴻 / Vertiv 接下來 2 季法說，明確 disclose NVDA 平台暴露
   百分比
3. Vertiv backlog 變化（先行指標）

時間框架：3-5 年結構性，不是 1-2 季題材。

## Counter（bull-case kill）

> 必填欄位，必須帶 threshold + time-window，必須標明 direction。

**（bull-case kill）** 如果 NVIDIA 後續架構從密集大顆走向 chiplet 切細 +
per-chip power 退回 700W 內（例如 Rubin Ultra refresh 改 chiplet），液冷
必要性會局部回退到空冷。但目前公開的 Blackwell / Rubin roadmap 都還在
per-chip power 上升方向——**這個 Counter 至少 2027 中之前不會發生**。

第二個 Counter：如果 immersion cooling（浸沒式）成為主流，cold plate +
manifold 受惠結構會被打散，受惠對象換成不同供應鏈（化學材料 + tank 供應
商而非 cold plate / manifold 廠）。**Threshold：immersion 在新建 AI data
center 滲透率 > 20%，目前 < 5%。Time-window：2027-2028 才需要重新評估。**

## Caveat

> 1 句話 acknowledge 1 個具體 gap。voice profile 那種「我目前覺得 / 還沒
> 驗證」語氣。

我目前還沒驗證的是：奇鋐 30%+ 冷板市占的口徑——是 NVDA 平台 only 還是含
ASIC（Google TPU / AWS Trainium）平台？這會直接影響受惠彈性的計算。
TrendForce 整理的數字也是 secondary aggregator，公開引用前我會找 1 條
一手 source（NVIDIA 法說提及散熱 BOM、或 Vertiv 季報 explicit mention）做
cross-check。

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

- [ ] Hook 用 lens 命名（資金）
- [ ] Observation 有具體 source + label
- [ ] Mechanism 是 plain Chinese
- [ ] Mechanism 不是 tautology
- [ ] Implication 有 company + signal + timeframe
- [ ] Counter 有 explicit threshold + time-window
- [ ] Counter direction 標明（bull-kill）
- [ ] Caveat 是具體 gap
- [ ] CTA 連到 backbone library page（暫填 placeholder）
- [ ] Disclaimer footer
- [ ] 字數 350-500
- [ ] 含投資宣稱 → 過 IA1 gate

## Pre-publish TODO

- [ ] Fact-check 奇鋐冷板市占（NVDA-only vs all-platform 口徑）
- [ ] 找 1 條非 TrendForce 來源 cross-check 散熱 BOM 數字
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
