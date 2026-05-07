# Agentic Runbook（中文版）

> 中文鏡像 / 對照原文：[AGENTIC_RUNBOOK.md](AGENTIC_RUNBOOK.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

目的：日常操作手冊。當你想做某件事時，這份文件告訴你該啟動哪個 workflow、載哪個
context pack、套哪些 gate。

對齊 [docs/AGENTIC_HARNESS.zh.md](../docs/AGENTIC_HARNESS.zh.md)、
[docs/WORKFLOW_PATTERNS.zh.md](../docs/WORKFLOW_PATTERNS.zh.md)、
[docs/CONTEXT_STRATEGY.zh.md](../docs/CONTEXT_STRATEGY.zh.md)、
[docs/HUMAN_GATES.zh.md](../docs/HUMAN_GATES.zh.md)。

## 怎麼用

1. 從表格找到你的任務。
2. 跑列出來的 workflow。
3. 只載入列出來的 context pack。
4. 遵守列出來的 gate。
5. Artifact 存到列出來的位置。

## 快速對照表

| 意圖 | Workflow | Context Pack | 強制 Gate | Artifact 位置 |
|------|----------|--------------|-----------|---------------|
| 「做這週的市場分析」 | investment-analysis | investment-analysis-pack | IA1（如含策略/回測再加 IA2） | 分析 brief + draft 在 `content/drafts/` |
| 「分析這個新聞事件」 | investment-analysis | investment-analysis-pack | IA1 | 分析 brief 存研究筆記 |
| 「Review 這個策略 / 回測」 | investment-analysis | investment-analysis-pack | IA2 | review note 放在回測旁邊 |
| 「規劃這週內容」 | content-production | content-sprint-pack | CP1（選用） | calendar 條目存 `content/` |
| 「寫一篇關於 X 的 post」 | content-production | content-sprint-pack | 含投資宣稱→IA1，否則無 | draft 存 `content/drafts/` |
| 「把分析改成 thread / short / carousel」 | content-production | content-sprint-pack | 含投資宣稱→IA1 | drafts 存 `content/drafts/` |
| 「研究競品 / 平台 post」 | algorithm-research | algorithm-research-pack | 採用前→AR1 | swipe 條目 + hypothesis |
| 「為什麼這篇 post 爆了」 | algorithm-research | algorithm-research-pack | 採用戰術前→AR1 | swipe 條目 |
| 「記錄一場新訪談」 | audience-discovery | audience-discovery-pack | raw 紀錄不需要 | 結構化訪談條目 |
| 「Cluster 目前的 pain」 | audience-discovery | audience-discovery-pack | 選下個 MVP→AD1 | pain cluster 文件 |
| 「Spec 一個新 MVP」 | mvp-demo | mvp-discovery-pack | MVP1 | MVP spec 存 `mvp/` |
| 「Launch 一個 demo」 | mvp-demo + content-production | 先 mvp-discovery-pack，再 content-sprint-pack | MVP2 | demo + launch post |
| 「決定 demo 是 keep / improve / kill」 | mvp-demo | mvp-discovery-pack | scope 變動→MVP1 | decision note |
| 「Postmortem 錯誤判斷或失敗實驗」 | postmortem | postmortem-pack | 公開→PM1 | postmortem note 放原 artifact 旁 |
| 「ship / commit / 收尾這個任務」 | ship-workflow | git-pack | 永遠 user approve，push 到 `main` 額外加一次確認 | git history + 在 `IMPLEMENTATION_PLAN.zh.md` Progress Log 加一行 |

## 常見 Sequences

### 每週發布

1. investment-analysis：產出分析 brief。
2. content-production：把 brief 改成 thread、blog、short variant。
3. 發布前過 Gate IA1。
4. 發布後到 `ops/METRICS.md` 記 metrics。

### Demo Launch

1. audience-discovery：確認選定的 pain。
2. mvp-demo：spec、做一個輕量版。
3. Gate MVP1。
4. content-production：寫 launch post。
5. 走 Gate MVP2，post 含投資結果暗示再加 IA1。

### 競品掃描

1. algorithm-research：收集 5-10 篇強 post。
2. Gate AR1，挑要採用哪些 pattern。
3. content-production：排 2-3 個實驗。

### 錯誤判斷恢復

1. 對該 call 跑 postmortem。
2. 若是結構性教訓，更新對應 playbook。
3. content-production：選擇性公開 postmortem。
4. 公開前走 Gate PM1。
5. ship-workflow commit 並記錄進度。

### 任何任務結束

1. 觸發 ship-workflow。
2. Agent 把變更分類並提出 branch / commit / push 計畫。
3. 使用者 approve、edit、或 reject。
4. Agent 只執行被 approve 的 git 指令。
5. 在 [docs/IMPLEMENTATION_PLAN.zh.md](../docs/IMPLEMENTATION_PLAN.zh.md) 的
   Progress Log append 一行。

## 每日節奏

- 早：掃 inbox / replies，把 audience-discovery 命中內容存成結構化條目。
- 午：跑當日主任務的 workflow（分析、內容、MVP）。
- 晚：對當天有發布的 artifact 做 post-publish review。

## 每週節奏

- 週一：investment-analysis + content-production（規劃）。
- 週二到週四：content-production（發布）、audience-discovery（記錄）。
- 週五：較深的分析或 demo launch，再加 algorithm-research 回顧。
- 週末：批次任務、MVP 迭代、必要時做 postmortem。

## 任務不對應現有 workflow 時

- 不要硬做。請人類，或在
  [docs/WORKFLOW_PATTERNS.zh.md](../docs/WORKFLOW_PATTERNS.zh.md) 先定義新 workflow 再跑。
- 若 workflow 需要新 context pack，先在
  [docs/CONTEXT_STRATEGY.zh.md](../docs/CONTEXT_STRATEGY.zh.md) 定義。
- 若 workflow 需要新 human gate，先在
  [docs/HUMAN_GATES.zh.md](../docs/HUMAN_GATES.zh.md) 定義。

## Anti-Patterns

- 為求保險載多個 context pack。
- 因為 draft 「看起來沒問題」就跳過 mandatory gate。
- 把 runbook 當腳本。它是 routing 地圖，不是 recipe。
- 加新 gate 但不退舊 gate；gate 疲勞是真的。
