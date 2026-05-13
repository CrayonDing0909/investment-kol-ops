---
workflow: content-production
artifact_type: thesis-card
risk: high
lens: 啟動
platform_target: x+threads
counter_direction: bear-falsify
backbone_ref: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
backbone_section: "Manufacturing Capacity / Apple 找 Intel 不是因為 Intel 變強，是因為 TSMC 沒位子"
sources:
  - WSJ 2026/05 Apple-Intel preliminary chip-making agreement (secondary, both companies declined to comment)
  - CNBC follow-up coverage (secondary)
  - Intel Q1 2026 Foundry revenue $5.4B +16% YoY (reported-fact)
  - TSMC 3nm utilization > 100%, 2nm booked to 2028 (reported-fact, C.C. Wei public)
created_at: 2026-05-13
public_status: outline
target_word_count: 400-500
---

# Card #004 — Apple-Intel preliminary deal 是訊號，但「preliminary」這個字現在做什麼還太早

> Outline 狀態：mechanism 已 seed（TSMC 卡 → Apple 找 second source →
> 為什麼是 Intel 而非 Samsung）。Counter direction = bear-falsify
> （什麼會讓「現在做什麼還太早」這個 risk-cautious 立場被推翻）。
>
> 這張的 voice 要特別小心：preliminary deal 是真實訊號，但寫過頭就變
> 成 hype；寫太弱就漏掉真實 catalyst。Hook + caveat 雙層結構在這張最
> 重要。

## Hook

> Apple-Intel preliminary chip-making agreement 是 Intel Foundry **第一次
> 拿到 hyperscale-tier 訊號**——但 source 是 WSJ 報導、雙方 declined to
> comment、沒有 primary press release。
>
> 這張 card 拆：(1) 為什麼 Apple 必須找 second source、(2) 為什麼是 Intel
> 不是 Samsung、(3) 「preliminary」這個字目前能 / 不能用來做什麼。

## Observation

2026/05 WSJ 首發報導，CNBC 等多家跟進：

- Apple 與 Intel 簽 **preliminary chip-making agreement**
- 雙方都 declined to comment
- **沒有 primary press release / 8-K**
- Source label：**secondary, pending primary confirmation**

Intel Foundry 進度（reported-fact）：

- 18A 已在 Arizona Fab 52 進入 HVM（high-volume manufacturing）
- Foundry external customer ramp 預期 2027
- 14A 量產 2029
- Q1 2026 Foundry revenue `$5.4B`, +16% YoY（外部 vs 內部客戶比例未拆）

TSMC 結構性卡住（reported-fact，C.C. Wei 2025/11 公開）：

- 3nm utilization 已過 100%
- 2nm booked 到 2028
- AI 算力需求是 TSMC 可產能 3 倍

## Mechanism

> 拆成 3 個遞推因果：

**第一層：TSMC 為什麼卡住**

3nm / 2nm 廠房擴建 + 設備（特別是 EUV）+ 認證 cycle 至少 3-4 年。AI 算力
需求 3 倍於 TSMC 可產能，但 TSMC 不會冒險大幅擴產（2018-19 半導體 boom-
bust 教訓還在）。

**第二層：Apple 為什麼必須找 second source**

Apple 是 TSMC 第二大客戶，但 NVIDIA / AMD / AVGO 同時都在排隊。Apple
被優先供應 cap allocation cut 的 risk 上升。Apple 自家 wafer 需求很大
（iPhone + Mac + Vision + AI 端側），任何 cap cut 都直接影響產品 roadmap。
single-source 風險變商業風險。

**第三層：為什麼是 Intel 不是 Samsung**

- Samsung 在 leading-edge（5nm 以下）yield 歷史不穩定，過去 Apple 試過
  Samsung A 系列 chip 後重回 TSMC，這次不太可能再賭一次
- Intel 18A 由前 TSMC Sr. Fellow Sanjay Natarajan 帶領，2025 yield 數據
  驗證後 Apple 才願意 commit
- Intel 美國本土製造，符合 Apple 「分散到美國」的政策訴求（Tim Cook 多次
  公開 align）

**第四層：可能 ramp 節點是 18A-P（2027 refresh）而非 18A（2026）**

Apple 對 yield + power efficiency 要求極高。18A 是 Intel 首次 GAA + back-
side power 雙技術，2026 量產但 yield ramping，CFO Zinsner 公開承認毛利
unprofitable until late 2026。18A-P 是 refresh 版本（小幅修正 + better
yield），預期是 Apple 真正大量 ramp 的可能節點。

## Implication

主要受惠：

- **Intel 自己**：Foundry 從「政策業務」升級為「商業業務」，valuation
  framework 改變（不再是「政策補貼支撐」，而是「真實商業收入」）。
- **次要受惠**：政策證明效果——CHIPS Act 撥款的合理性被市場 re-price，
  Intel downside floor 上升。

不直接受惠（但常被誤掛）：TSMC 不會 idle（NVIDIA / AMD / AVGO 還在搶），
但 Apple 配額轉走 = Apple TSMC wafer 占比下降，這對台廠 Apple 供應鏈
（鴻海 / 立訊 等）**間接**有 mix shift，但這條 evidence 還很薄，不要硬寫。

觀察訊號：

1. Apple / Intel 正式 8-K 或 press release（最強 trigger）
2. Intel Q2 / Q3 2026 Foundry 法說 external customer 細節（part-name /
   revenue uplift）
3. 18A-P yield 進度（TechInsights / SemiAnalysis 是 leaks 來源）
4. Samsung Texas 廠是否成為第三家 second source（如果是，Intel
   competitive position 反而被削弱）

Timeframe：**6 個月內無正式公告 → 視為 stuck，需要重新評估**。

## Counter（bear-case falsification）

> 這張立場是 risk-cautious（「現在做什麼還太早」），所以 Counter 是
> falsify-bear——什麼會讓「太早」這個立場被推翻。

**（bear-case falsification）** 如果 Intel 在 **2026 Q3 法說（10/30 前後）
明確 disclose Foundry external customer name 或 revenue uplift（即使不是
Apple，是其他 hyperscale-tier 客戶如 Microsoft / Cisco / Broadcom），
preliminary deal 的「pending primary confirmation」風險降低**，可以從
secondary 升級到 reported-fact 等級。

如果 **Apple 2026 Q3 / Q4 同期 8-K 出現相關 commitment**（例如「我們已
diversify 到多個 advanced foundry partners」），更強訊號。

如果 **2026 年內 18A-P yield 數據 public leak 顯示 > 70%（Apple grade）**，
ramp 節點的 timing 從 2027-2028 縮短到 2027 上半年——「太早做什麼」這個
立場明確被 invalidate。

## Caveat

我目前最大的不確定是：preliminary deal 從 WSJ 報導到正式公告通常 3-12 個月
不等。MediaTek / NVIDIA 都有過類似 leak → 數月後 confirm 的 pattern，但也
有過 leak → 永不 confirm（雙方默契取消）的 pattern。**我無法判斷哪一條是
這次的劇本**——所以「太早做什麼」這個立場必須 hold 6 個月。

## CTA + Footer

```text
完整 Manufacturing layer 分析（含 CHIPS Act / Foundry second-source / 
Apple-Intel deal 三條交織）在 library：
crayonding.io/library/ai-server-supply-chain#manufacturing
（library 上線前暫填 placeholder URL）

下一張拆 3 個會破 CPU 復興 thesis 的具體數字。

本內容是研究與教育，不是投資建議。Apple-Intel deal 在公告 confirm 前
均為 media-reported preliminary，請勿視為已簽訂單。
```

## Platform Adaptation Notes

- **X long post**：4 層 mechanism 用 numbered，每層 1-2 句濃縮。「為什麼是
  Intel 不是 Samsung」是這張最 differentiated insight，獨立段落。
- **Threads carousel**（8 slides）：
  - Slide 1: Hook（強調「preliminary」這個字）
  - Slide 2: Observation（WSJ source 透明化）
  - Slide 3: Mechanism layer 1-2（TSMC 卡 + Apple 找 second）
  - Slide 4: Mechanism layer 3（為什麼 Intel 不是 Samsung）
  - Slide 5: Mechanism layer 4（18A vs 18A-P）
  - Slide 6: Implication + 4 個觀察訊號
  - Slide 7: Counter（bear-falsify）
  - Slide 8: Caveat + CTA + 「prelim 不是已簽單」disclaimer

## Review Checklist

- [ ] Hook 用 lens 命名（啟動）+ 「但...」雙層結構
- [ ] Source label 清楚（WSJ secondary，雙方 declined）
- [ ] 4 層 mechanism 都 plain Chinese
- [ ] 「為什麼 Intel 不是 Samsung」差異化論點清楚
- [ ] Implication 區分主要 / 次要受惠 + 不要硬掛間接受惠
- [ ] Counter 是 bear-falsify，有 explicit time-window（Q3 法說 / 6 個月）
- [ ] Caveat 承認劇本不確定（leak 兩種 pattern）
- [ ] CTA 連 backbone
- [ ] 「preliminary 不是已簽單」明確 disclaim
- [ ] 字數 400-500
- [ ] 過 IA1 gate（risk: high，含 Apple / Intel 雙公司宣稱）

## Pre-publish TODO

- [ ] 確認 Sanjay Natarajan 前 TSMC Sr. Fellow 身份（LinkedIn / Intel 公告
      cross-check）
- [ ] 確認 18A-P refresh schedule（Intel 公開 roadmap）
- [ ] 確認 CFO Zinsner 「unprofitable until late 2026」原始 quote
- [ ] Polish hook（hook 太長要截，但「but preliminary」必須保留）
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
