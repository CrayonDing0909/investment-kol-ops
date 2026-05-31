# Roadmap（中文版）

> 中文鏡像 / 對照原文：[ROADMAP.md](ROADMAP.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

目標：建立一台可重複的投資 KOL 機器，能做研究、發布、學習，並把觀眾痛點轉成有用
的 AI 輔助 MVP 產品。

本檔聚焦產品/業務 milestone。工程實作 milestone（templates、scripts、commands、
branch 策略）放在 [docs/IMPLEMENTATION_PLAN.zh.md](IMPLEMENTATION_PLAN.zh.md)。

## 操作模型（artifact-first overlay）

方向錨點：[docs/NORTH_STAR.zh.md](NORTH_STAR.zh.md)。核心單位：
[docs/ARTIFACT_SYSTEM.zh.md](ARTIFACT_SYSTEM.zh.md)。

這個 repo 現在以 artifact 為先來讀。我們優化的迴圈是：

```text
Artifact -> 公開內容 -> 受眾訊號 -> 研究深化 -> 產品
```

下面原本的 milestone（M0-M6）仍然有效，作為研究品質層與基礎設施層。它們本身不再
是「立刻要做的下一步」，而是服務 artifact 迴圈。深度 source-backed 研究
milestone（IMPLEMENTATION_PLAN 的 M1.1/M1.2 型工作）是研究品質層，不應擋住公開
artifact 測試。

往後的 artifact-first milestone 順序：

```text
M0.5 Repo Refinement          (這個 overlay + operating layer)
M1   Artifact Engine MVP       (5 個可發布 artifact)
M2   Research Packet Lite       (只深化表現好的 artifact)
M3   Public Distribution Loop   (穩定的每週發布節奏)
M4   Landing Page + Private Traffic
M5   First Interactive Prototype
```

這些是「重用」而非「取代」下面的系統：內容生產走
[content/CONTENT_OPERATING_SYSTEM.md](../content/CONTENT_OPERATING_SYSTEM.md) 與
[content/templates/](../content/templates/)；發布用
[docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md) 的兩層 gate（教育型 artifact 走
Gate A，投資觀點走 Gate B）；metrics 用 [ops/METRICS.md](../ops/METRICS.md) 與
`ops/decisions/` 的 post-publish checklist。工作 backlog 與 milestone spec 放在
[ops/backlog.md](../ops/backlog.md)。

## Milestone 0.5 - Repo Refinement

成果：repo 讀起來像 artifact-led KOL operating system，不是只有研究流程。純
additive，不移除任何既有系統。

- 加方向層：[docs/NORTH_STAR.zh.md](NORTH_STAR.zh.md)。
- 加 artifact 模型：[docs/ARTIFACT_SYSTEM.zh.md](ARTIFACT_SYSTEM.zh.md)，含
  L1-L4 分級。
- 加每日 / 每週 operating layer：[NEXT_ACTIONS.md](../NEXT_ACTIONS.md) 與
  `ops/weekly/`。
- 加公域分發 templates：IG carousel、YouTube Shorts、輕量 artifact brief。
- 在 [docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md) 加兩層發布 gate（Gate A vs B）。
- 把 AI Server Supply Chain reframe 成第一個公開 artifact 系列。

Exit criteria：

- 新人打開 repo 就知道這專案在做什麼。
- `NEXT_ACTIONS.md` 告訴使用者今天該做什麼。
- 每個 artifact 有清楚的生命週期與 Definition of Done。
- 有每週 review 儀式。
- 研究流程仍可用，但不再擋住公開測試。

## Milestone 0 - Foundation 與 Agentic Harness

成果：repo 成為 single source of truth，並有定義好的 harness。

- 定義帳號定位：要幫誰、不做什麼。
- 建立內容操作系統與發布節奏。
- 建立投資分析品質 gate。
- 建立基本 metrics 追蹤。
- 決定前 30 天的主要平台。
- 把 agentic harness 立起來：
  [docs/AGENTIC_HARNESS.zh.md](AGENTIC_HARNESS.zh.md)、
  [docs/WORKFLOW_PATTERNS.zh.md](WORKFLOW_PATTERNS.zh.md)、
  [docs/CONTEXT_STRATEGY.zh.md](CONTEXT_STRATEGY.zh.md)、
  [docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md)、
  [ops/AGENTIC_RUNBOOK.zh.md](../ops/AGENTIC_RUNBOOK.zh.md)。
- 確認 `AGENTS.md` 強制 workflow-first 行為。

Exit criteria：

- 一句清楚的帳號定位。
- 一套每週發布流程。
- 一份 metrics sheet 或 markdown 追蹤器。
- 一個可重複的分析模板。
- 每個領域都有 canonical workflow（algorithm-research、audience-discovery、
  investment-analysis、content-production、mvp-demo、postmortem），且可以從 runbook
  routing。

## Milestone 1 - 受眾與平台研究

成果：停止猜，所有研究都走 harness。

- 用 algorithm-research workflow 跑 X、Threads、YouTube Shorts、Instagram Reels、
  長篇 blog/newsletter，記錄 structured swipe。
- 透過同一個 workflow 收集 30 個強投資/AI 創作者範例。
- LLM 只在 structured data 上做 hook、format、互動 pattern、內容角度的判斷，不直接
  讀 raw 截圖。
- 對 10-20 個不會用 AI agent 的人跑 audience-discovery workflow。
- 萃取重複出現的 pain：投資、研究、新聞過載、組合 review、自動化焦慮、工具設定門檻。
- 採用任何戰術前過 Gate AR1，選下個 MVP 前過 Gate AD1。

Exit criteria：

- 20 個帶 workflow tag 的內容 hypothesis。
- 5 個結構化形式的觀眾 pain cluster。
- 3 個準備好給 mvp-demo workflow 的候選 demo。

## Milestone 2 - Content Sprint 1

成果：用 content-production workflow 發布到一定量，從市場拿到回饋。

- 選一個觀眾：想要更好研究但不會用 agent 的散戶。
- 選兩個 format：市場分析 thread、AI workflow demo。
- 分析文跑 investment-analysis → content-production。
- AI workflow demo 直接跑 content-production。
- 連續 4 週、每週 3-5 篇。
- 任何含市場宣稱的 post 都過 Gate IA1。
- 用 [ops/METRICS.md](../ops/METRICS.md) 追蹤 hook、format、topic、CTA、impressions、
  engagement、saves、comments、follows、clicks。
- 每週 review，加碼最有效的 format。

Exit criteria：

- 12-20 篇已發布貼文。
- 3 個被驗證的內容 pattern，記錄到 algorithm-research hypothesis。
- 1 個值得服務的清楚受眾段，寫進 CONTENT_STRATEGY。

## Milestone 3 - MVP Demo Lab

成果：用 mvp-demo workflow 把注意力轉成可用的產品 loop。

- 對選定的 pain 跑 mvp-demo workflow。
- 每個 demo 必須明確定義 data input、programmatic checks、LLM judgment、human
  review。
- 為最強的 pain 做一個快 demo 網站。
- 範圍要窄：一個使用者、一個 workflow、一個結果。
- 範例：
  - Market regime explainer（簡單輸入 → 解釋）。
  - AI 輔助 earnings/news digest。
  - 組合風險 checklist。
  - 新手友善的「ask an investing agent」引導表單。
  - 給非量化族用的 backtest sanity checker。
- 加 waitlist 或 feedback 收集。
- 開發前過 Gate MVP1，launch 前過 Gate MVP2，含任何投資宣稱再加 IA1。
- MVP1 一過就立刻啟動 content-production 寫 launch post。

Exit criteria：

- 一個能用的 demo。
- 一個 feedback form。
- 20+ 使用者或對話。
- 決策：improve、pivot、archive，並對應 kill criterion 檢查。

## Milestone 4 - 分析可信度系統

成果：透過強化 investment-analysis 與 postmortem workflow，讓帳號變得可被信任。

- 收緊 investment-analysis workflow：每個公開宣稱都對應到 source。
- 對 chart、資料、宣稱加 source tracking。
- 建立持倉、watchlist、不確定性的揭露規則。
- 把「what would change my mind」當 workflow 必交 artifact。
- 對錯誤判斷與漏掉的 scenario 跑 postmortem workflow；公開前過 Gate PM1。

Exit criteria：

- Market weekly 模板。
- Theme deep dive 模板。
- Trade/idea postmortem 模板。
- 公開 disclaimer 與 source policy。
- 策略/回測內容發布前一律過 Gate IA2。

## Milestone 5 - Content Production Pipeline

成果：把 idea 到發布的摩擦縮到最小，並穩固 content-production workflow。

- 建立每週 planning workflow，使用 content-sprint-pack 與
  `CONTENT_OPERATING_SYSTEM.md` 的 weekly rhythm。
- 為文章、thread、carousel、短影片、縮圖、demo launch post 建立 template。
- 為 chart、screenshot、視覺、caption 建立 asset checklist。
- 把 review checklist（accuracy、clarity、compliance、CTA、formatting）寫進
  workflow 的 LLM step。
- 依主題批次生產內容。
- 決定本 sprint 哪些 gate 是 mandatory、哪些是 optional，並記錄設定。

Exit criteria：

- 2 週的內容日曆。
- 可重複的 publish checklist 內建在 workflow 中。
- Asset 資料夾命名慣例。
- 每週 review 儀式並更新 `ops/METRICS.md`。

## Milestone 6 - 產品與社群飛輪

成果：把內容、demo、社群連起來，同時讓每個公開 artifact 都過正確 gate。

- 建立 email/waitlist 收集（由 audience-discovery 與 mvp-demo workflow 管轄）。
- 做一個免費 lead magnet：市場 checklist、prompt pack、或迷你工具。
- 把使用者納入結構化 feedback loop，由 audience-discovery 紀錄。
- 用 postmortem 與 content-production workflow 把重複出現的問題轉成內容與產品改進。
- 重複需求出現後再考慮付費產品，且必須先在本 repo 加上專屬 workflow + gate。

Exit criteria：

- 100 個 email/waitlist 訂閱者，或一個清楚的 niche 訊號。
- 3 個重複出現的產品需求。
- 1 個依使用者回饋改良過的 demo。
- 在進入任何商業化動作前，先有 paid-product workflow。

## 第一個 7 天

1. 完成 repo 文件與規則，含 agentic harness。
2. 選主要平台與目標受眾。
3. 透過 algorithm-research workflow 產出 10 個內容 hypothesis。
4. 透過 content-production workflow 發出前 3 篇 post。
5. 開 algorithm swipe file，使用 structured 條目。
6. 透過 audience-discovery workflow 訪談 3 個不會用 AI agent 的人。
7. 透過 Gate AD1 選一個 MVP demo 候選。
