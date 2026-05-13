---
workflow: content-production
artifact_type: thesis-card
risk: high
lens: 基本面
platform_target: x+threads
counter_direction: bear-falsify
backbone_ref: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
backbone_section: "第二條 / MediaTek 在 ASIC 故事裡的位置（4 個具體風險）"
sources:
  - MediaTek Q1 2026 earnings call transcript (reported-fact for $2B framing)
  - MediaTek Analyst Day 2025 (forward-looking-target)
  - Stock price + valuation 歷史（自行驗算）
created_at: 2026-05-13
public_status: outline
target_word_count: 400-500
---

# Card #002 — MediaTek $2B AI ASIC 是 management expectation，不是已實現營收

> Outline 狀態：題目 / lens / Counter direction 已定，4 risks 已從 backbone
> 萃。最終 wording、股價數字需要 polish + fact-check。
>
> 這張是 risk-heavy card，所以 Counter direction = bear-falsify（什麼會讓
> 「這是個 risk」這個 claim 被推翻 / 弱化）。

## Hook

> MediaTek $2B AI ASIC 不是已實現營收，是 Q4 2026 management expectation。
> 兩件事差距很大——不只 timing 差，valuation framework 也完全不同。
>
> 中文圈很多人寫 MediaTek 直接把 $2B 當成「已經拿到的訂單」。這張 card
> 拆 4 個具體風險，幫你判斷股價反應的是「敘事」還是「兌現」。

## Observation

MediaTek 公開：

- AI ASIC revenue target `~$2B in Q4 2026`（management-expectation，源自
  官方法說 transcript）
- Cloud ASIC TAM `$70B-$80B in 2027`（forward-looking-target，是市場規模
  不是 MediaTek 收入）
- Cloud ASIC share target `10%-15%`（forward-looking-target）

實際出貨組成：source 顯示目前 ramp 多是 **subsystem**（I/O / memory /
interconnect / 少量 silicon photonics CPO optionality + custom HBM 可選性），
**不是 ASIC 主晶片**。

ASIC 主晶片角色目前還是 Broadcom / Marvell / 創意 / 世芯為主。

## Mechanism

> 重點：股價 priced 的是「主晶片切入 + Q4 數字兌現」雙重劇本，但實際 ramp
> 可能只兌現其中一條。

4 個具體風險（這就是「小心」的具體形狀）：

1. **Track record 風險**
   MediaTek 過去主力是手機 SoC（HiSilicon 替代 + 中低階 5G）+ 消費電子。
   Data center silicon 是新領土，customer engagement → tape-out →
   qualification → ramp 是 18-30 個月 cycle，每一步都有 yield / 良率 /
   認證 risk。我們沒有 MediaTek 在 hyperscaler 端的歷史交付資料。

2. **Subsystem vs 主晶片混淆**
   股價反映的是「MediaTek 切入 AI ASIC」這個敘事；source 顯示目前 ramp
   多是 subsystem。Subsystem 毛利結構（~10-15%）與主晶片（30-40%）差距
   很大，估值假設不能等同。如果未來只 ramp subsystem 沒 ramp 主晶片，
   敘事與營收會脫鉤。

3. **Expectation reset 風險**
   `$2B Q4 2026` 是 Q4 單季 ASIC revenue target。如果 Q4 實際數字落在
   $1.0-1.5B（仍是大數字、但低於指引），市場會視為「敘事打折」而非「絕對
   失敗」。Historically MediaTek 法說 guidance miss 後股價 derate 約
   15-25%。

4. **Price-in 風險**
   MediaTek 從 2025 年中到 2026/05，stock price 約 +60-80%（**TODO：填實際
   數字**），本益比擴張到歷史高點 1.5 個標準差以上（**TODO：fact-check**）。
   即使敘事兌現，價格已經反映了部分；如果敘事兌現速度比市場期待慢，下檔
   空間先變大。

合起來的 mechanism：股價 priced 的雙重劇本任一條沒兌現，估值倍數就要
re-rate。

## Implication

要追蹤的是 3 件事，**不是「值得關注」這種空話**：

1. 每季 ASIC 拆分（主晶片 vs subsystem 收入比例）。如果 subsystem 占比
   > 70% 持續超過 2 季 → subsystem-confusion 風險被驗證
2. Tape-out → qualification 公告節奏。如果 2026 內無新 tape-out 公告 →
   track record 風險不降
3. MediaTek 法說管理層對 Q4 $2B 的措辭強度變化。如果從「on track」變成
   「subject to customer ramp timing」→ expectation reset 訊號

Timeframe：2026 Q2 法說（7 月底）+ Q3 法說（10 月底）是關鍵窗口。

## Counter（bear-case falsification）

> 這張是 risk card，Counter direction 是 falsify-bear——什麼會讓這個 risk
> 被弱化或推翻。

**（bear-case falsification）** 如果 MediaTek 在 **2026 Q2 法說（7/30 前後）
或 Q3 法說（10/30 前後）公布具體主晶片 design win**——hyperscaler 客戶名稱
（GOOG / META / AWS / Microsoft 之一）+ project size（單一 design 預期年
revenue contribution），track-record 與 subsystem-confusion **兩個風險會同
時降低**。

如果到 **2026 Q4（2027/01 法說）仍只揭露 subsystem revenue 而無主晶片
design win 公告，risk 維持原狀**。

如果 Q4 實際 ASIC revenue 落在 $1.8B+（>90% target），expectation reset
風險也會被推翻，價格反而可能 re-rate up。

## Caveat

我目前還沒驗證的是：MediaTek 在 hyperscaler 端的歷史交付資料。如果有人能
找到他們過去 5 年對美系 hyperscaler 的成功 design 紀錄，track record 風險
的權重需要下調。Stock price 與 valuation 數字也需要對近期 close 重新驗算。

## CTA + Footer

```text
完整 ASIC 段（包含 hyperscaler 為什麼自研 ASIC 的 mechanism）
在 library：crayonding.io/library/ai-server-supply-chain
（library 上線前暫填 placeholder URL）

下一張拆「為什麼 CPU 又被討論」——agent AI 跟 memory wall 的因果鏈。

本內容是研究與教育，不是投資建議。我不持有 MediaTek 部位（**TODO：上線前
確認 disclosure**）。
```

## Platform Adaptation Notes

- **X long post**：4 risks 用 numbered list（X 對 numbered 友善）。Counter
  獨立段落，醒目放最後。
- **Threads carousel**（8 slides，risk card 多 1 slide）：
  - Slide 1: Hook
  - Slide 2: Observation（$2B + cloud TAM + share target）
  - Slide 3: Subsystem vs 主晶片（這是核心 misconception，獨立 slide）
  - Slide 4-5: 4 risks（2 risks per slide）
  - Slide 6: Implication（3 個追蹤訊號）
  - Slide 7: Counter（bear-falsify）
  - Slide 8: Caveat + CTA + 持倉揭露

## Review Checklist

- [ ] Hook 用 lens 命名（基本面）+ 直接挑戰常見誤解
- [ ] Observation 有 source + label（reported-fact / management-expectation
      / forward-looking-target 都明確）
- [ ] 4 risks 每個都 specific（不是「市場波動」這種廢話）
- [ ] Mechanism 不是 tautology
- [ ] Implication 有具體 threshold（>70% / 兩季 / 措辭變化）
- [ ] Counter 是 bear-falsify direction，有 explicit time-window
      （Q2 / Q3 / Q4 法說）
- [ ] Caveat 是具體 gap
- [ ] 持倉揭露 included（risk: high 必填）
- [ ] CTA 連 backbone
- [ ] 字數 400-500
- [ ] 過 IA1 gate（risk: high）

## Pre-publish TODO

- [ ] Fact-check MediaTek stock price +60-80% from 2025 mid（用最新 close）
- [ ] Fact-check 本益比 1.5 std above historical（用 5-year P/E z-score）
- [ ] 確認 subsystem 毛利 10-15% / 主晶片 30-40% 數字（公開資料 / sell-side
      consensus）
- [ ] 確認個人持倉狀態 + disclosure 措辭
- [ ] Polish hook 措辭（測試 3 個變體）
- [ ] 過 IA1 gate
- [ ] 確認 backbone library URL

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
