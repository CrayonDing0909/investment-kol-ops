# Context Strategy（中文版）

> 中文鏡像 / 對照原文：[CONTEXT_STRATEGY.md](CONTEXT_STRATEGY.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

目的：控制 LLM 在每一步看到什麼。目標是「能完成任務的最小 context」，不是「最多
context」。本文件定義具名 context pack 與使用規則。

對齊 [docs/AGENTIC_HARNESS.zh.md](AGENTIC_HARNESS.zh.md) 和
[docs/WORKFLOW_PATTERNS.zh.md](WORKFLOW_PATTERNS.zh.md)。

## 為什麼重要

- Context 越大，最強的訊號被稀釋越多。
- Repo-wide context 會讓 agent 在分析、內容、MVP 之間漂移，失去精確度。
- 載入無關 playbook 容易導致過度自信、偏離主題。
- Token 成本和 input 量成正比。多數「聰明」答案來自 routing 變好，不是 prompt 變大。

## 規則

- 先選 workflow，再選 context pack。順序不能反。
- 每個 pack 列必要與選用文件。先載入必要，agent 真的需要才加 optional。
- 一段內容夠的時候不要貼整份檔案。引用路徑，讓 agent 需要時自己讀。
- 不要同時載多個 workflow pack。要 compose 就用 sequencing。
- 注入前先把 raw、龐大、雜訊資料整理過，傳結構化摘要。
- 任何 pack 都不能含 secret、brokerage 資料、PII。

## Context Packs

### algorithm-research-pack

用於 algorithm-research workflow。

必要：

- [research/ALGORITHM_RESEARCH.md](../research/ALGORITHM_RESEARCH.md)。
- [docs/CONTENT_STRATEGY.md](CONTENT_STRATEGY.md)，只用定位與 pillar 段。
- 此次任務收集到的 structured swipe 條目。

選用：

- [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md)，候選 post 觸及高風險
  主題時。

不要載入：

- 投資分析 playbook。
- MVP lab。
- 受眾 raw notes。

### audience-discovery-pack

用於 audience-discovery workflow。

必要：

- [research/AUDIENCE_DISCOVERY.md](../research/AUDIENCE_DISCOVERY.md)。
- 此次任務的訪談 / 觀察 structured 條目。
- 既有的 pain cluster（如果有）。

選用：

- [mvp/MVP_LAB.zh.md](../mvp/MVP_LAB.zh.md)，只在提出 MVP 候選時。
- [docs/CONTENT_STRATEGY.md](CONTENT_STRATEGY.md)，只在提出內容角度時。

不要載入：

- Algorithm swipe file。
- 投資分析 playbook。

### investment-analysis-pack

用於 investment-analysis workflow。

必要：

- [research/INVESTMENT_ANALYSIS_PLAYBOOK.md](../research/INVESTMENT_ANALYSIS_PLAYBOOK.md)。
- [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md)。
- Structured 資料輸入（macro、breadth、leadership、news、technicals、sentiment）
  與 source。

選用：

- 各 trading skill 的輸出（market-environment、macro-regime-detector、
  market-breadth-analyzer 等）做成 structured findings。
- 上週分析 brief，只在比較時用。

不要載入：

- Content drafts。
- MVP specs。
- Algorithm swipe file。

### content-sprint-pack

用於 content-production workflow。

必要：

- [content/CONTENT_OPERATING_SYSTEM.md](../content/CONTENT_OPERATING_SYSTEM.md)。
- [docs/CONTENT_STRATEGY.md](CONTENT_STRATEGY.md)。
- 要被改寫 / 重用的來源 artifact（分析 brief、MVP spec、postmortem、pain cluster）。
- 已知的平台 format 限制。

選用：

- [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md)，draft 觸及高風險主題
  時必載。
- [ops/METRICS.md](../ops/METRICS.md) 最近 metrics 摘要。

不要載入：

- Raw 訪談 notes（用 cluster output 代替）。
- 投資分析 playbook 全文（分析 brief 已足夠）。

### mvp-discovery-pack

用於 mvp-demo workflow。

必要：

- [mvp/MVP_LAB.zh.md](../mvp/MVP_LAB.zh.md)。
- 從 audience-discovery 選出的 pain cluster。
- One-line user、one-line promise、提議的 input/output。

選用：

- [research/AUDIENCE_DISCOVERY.md](../research/AUDIENCE_DISCOVERY.md)，只在重新檢查
  MVP selection filter 時。
- [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md)，demo 觸及金融建議、
  回測、持倉相關輸出時必載。

不要載入：

- Algorithm swipe file。
- Content operating system 全文。

### postmortem-pack

用於 postmortem workflow。

必要：

- 原始 artifact（post、analysis、MVP spec）。
- 原始 hypothesis 與成功指標。
- 觀察到的 metrics 與結果。

選用：

- [docs/WORKFLOW_PATTERNS.zh.md](WORKFLOW_PATTERNS.zh.md) 中相關的 workflow pattern。
- 原始 artifact 來自的 playbook。

不要載入：

- 無關 playbook。
- 其他進行中的實驗。

### git-pack

用於 ship workflow。刻意保持很小。

必要：

- [docs/IMPLEMENTATION_PLAN.zh.md](IMPLEMENTATION_PLAN.zh.md) 的「Branch 與 Commit
  策略」段。
- [AGENTS.zh.md](../AGENTS.zh.md) 的 Human Gate 規則與驗證段。
- 即時 git 狀態：`git status --short`、`git diff --stat`、目前 branch、remote
  tracking 狀態。

選用：

- `IMPLEMENTATION_PLAN.zh.md` 的 Progress Log 段，只在要 append 新 log 時。

不要載入：

- 任何 workflow 專屬 playbook。
- 任何 artifact 內容（只要檔案路徑與 diff stat 即可）。
- Secret、credential、或任何 `.env*` 內容。

## Structured Data 慣例

只要可能，傳 LLM 一個 structured 物件，不要 raw 筆記。

- 用 markdown table、YAML、或有 label 的 bullet list。
- 每個項目標：source、timestamp、confidence、workflow。
- 數字欄位保留為數字，不要塞在敘述裡。
- 注入前剝掉非必要 commentary。

## Context Drift 檢查

只要遇到下面任一情況，agent 必須停下來重新 routing：

- 開始拉 active pack 沒列的文件。
- 投資分析的語氣和 MVP 行銷語氣混在一起。
- 引用了沒載入的 metrics。
- 產出和 workflow 預期 artifact 不符。

## 不確定時的預設

- 一次一個 workflow。
- 一次一個 context pack。
- 結尾一個 artifact。
- 必須 compose 時，先完成 artifact A，再載入 pack B。
