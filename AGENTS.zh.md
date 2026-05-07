# Agent 指令

> 中文鏡像 / 對照原文：[AGENTS.md](AGENTS.md)
> 英文是 LLM 主要讀取版本；中文版供人類 review 對照用，AI agent 仍以英文版為準。

## 任務目標

替 `CrayonDing0909` 建立投資 KOL 操作系統：受眾研究、投資分析、內容生產、AI
agent MVP demo、發布營運。

## 操作模型

本 repo 以 [docs/AGENTIC_HARNESS.zh.md](docs/AGENTIC_HARNESS.zh.md) 定義的 agentic
harness 運作。每個有意義的任務都要照這個 harness 跑。

預設行為：

1. 先確認意圖，從 [docs/WORKFLOW_PATTERNS.zh.md](docs/WORKFLOW_PATTERNS.zh.md) 選一個
   workflow。
2. 先收集 structured data，不要把 raw notes 直接丟給 LLM。
3. 從 [docs/CONTEXT_STRATEGY.zh.md](docs/CONTEXT_STRATEGY.zh.md) 只載入對應的 context
   pack。
4. LLM 用來做 synthesis、draft、分類、按 checklist review。不用來做計數、排序、
   過濾、儲存狀態，也不要假裝跑過工具。
5. 套用風險分類器，遵守 [docs/HUMAN_GATES.zh.md](docs/HUMAN_GATES.zh.md) 中所有
   mandatory gate。
6. 產出實體 artifact，存到 runbook 指定的位置。
7. 更新 metrics，讓下一次 routing 決策更準。

如果任務對不到任何 workflow，不要硬做。問人，或先定義新 workflow。

## 預設優先順序

- 個人策略與投資分析：品質與學習 > 速度。
- MVP demo：速度 > 完美，但學習 loop 不能省。
- 所有產出必須實用：每個 research 都要轉成 content idea、product idea、checklist、
  腳本、或實驗。
- 不要把這個 repo 和工作專案的規則混用。

## 程式優先規則

只要能用程式、腳本、確定性檢查解決的事，就不要交給 LLM。

- 驗證 ticker、單位、日期、星期一致性。
- 統計 metrics、排序貼文、計算重複次數、過濾 cluster 都先做完，再交給 LLM
  summarize。
- 把 raw notes 轉成 structured data，欄位至少要有：source、timestamp、confidence、
  workflow tag。

## Context 注入規則

- 先選 workflow，再載入「一個」context pack。
- 不要貼整份檔案，能貼一段就好。
- 不要同時載入多個 workflow pack。要 compose 就用順序串接。
- 注入前先把雜訊資料整理過，傳結構化摘要。
- 如果 agent 開始拉 active pack 沒列出的文件，立刻停下來重新 routing。

## Human Gate 規則

- 高風險 artifact 沒過 human gate 不准發布或 launch。
- 高風險包含：投資宣稱、持倉相關內容、回測宣稱、MVP launch、公開更正、付費 offer。
- 不確定 gate 是否適用時，預設要走 gate。
- 每次 gate 決策都要記錄在 artifact 旁邊，不要只記在 chat。

## 投資分析規則

- 使用可重複的流程：macro regime、breadth、market leadership、sector/theme
  rotation、news catalysts、technical structure、risk zones、scenario planning。
- 觀察、解讀、行動三者要分開。
- 標出不確定性與 invalidation 條件。
- 投資內容絕對不能呈現為「保證的建議」。
- 討論策略或回測時，必須含 fees、liquidity、drawdown、overfitting、資料品質的
  caveat。

## 內容規則

- 把每篇 post 當實驗，要有 hypothesis。
- 一律要定義：目標受眾、hook、平台、format、CTA、成功指標。
- 寧可清楚實用，不要含糊的市場 commentary。
- 發布後要寫學習紀錄。

## MVP 規則

- 對非 AI agent 使用者，從痛點出發，不是從技術出發。
- 在 5 分鐘內解決一個具體 workflow 的 demo。
- 在做大型產品前，先做簡單 web demo、checklist、calculator、引導式表單。
- 把每個 demo 當作 structured workflow：data input、programmatic checks、LLM
  judgment、human review。

## 動態流程規則

- Workflow 是模板，不是腳本。Agent 可以根據當前證據和風險，跳過、分岔、或
  escalate 步驟。
- 任務中途若需要改流程，要明確宣告新的 workflow chain，並更新 artifact。

## Ship Workflow 規則

- 任何有檔案變更的任務結束時，執行
  [docs/WORKFLOW_PATTERNS.zh.md](docs/WORKFLOW_PATTERNS.zh.md) 定義的 ship-workflow。
- 在使用者明確 approve 之前，永遠不執行 `git commit`、`git push`、或
  `git checkout -b`。這條規則是絕對的，即使是低風險的文件改動也不例外。
- 推到 `main` 需要額外多一次確認。
- Branch 與 commit 決策遵守
  [docs/IMPLEMENTATION_PLAN.zh.md](docs/IMPLEMENTATION_PLAN.zh.md) 的策略。
- 成功 commit 後，在 `IMPLEMENTATION_PLAN.zh.md` 的 Progress Log append 一行。

## 驗證

- 完成有意義的改動前，跑一次 ship check：哪些檔案變了、有哪些 open risk、跑了什麼
  test 或人工驗證、下一步是什麼。
- 沒實際跑就不要宣稱跑過 commands、tests、research、發布。

## Anti-Patterns

- 把整份 repo 都貼給 LLM。
- 期待 LLM 跨 turn 自己記住狀態。
- 用 prompt 強迫執行那些其實該寫成程式或 checklist 的規則。
- 每一步都人工確認（決策疲勞）或都不確認（不安全產出）。
- 把 workflow 當成固定腳本，而不是動態模板。
