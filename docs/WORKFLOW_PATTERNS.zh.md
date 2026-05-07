# Workflow Patterns（中文版）

> 中文鏡像 / 對照原文：[WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

目的：定義本 repo 內使用的 canonical workflow。每個 workflow 都遵守
[docs/AGENTIC_HARNESS.zh.md](AGENTIC_HARNESS.zh.md) 中的 agentic harness。

每個 workflow 都同樣分成：

- Trigger（觸發）。
- Structured input（結構化輸入）。
- Programmatic checks（程式檢查）。
- LLM role（LLM 角色）。
- Human gate（人類確認）。
- Output artifact（輸出 artifact）。

如果一個實際任務對不到任何 workflow，agent 必須 (a) 串接兩個 workflow，或
(b) 先請人類定義新 workflow，再開始做。

## Index

- [Algorithm Research Workflow](#algorithm-research-workflow)
- [Audience Discovery Workflow](#audience-discovery-workflow)
- [Investment Analysis Workflow](#investment-analysis-workflow)
- [Content Production Workflow](#content-production-workflow)
- [MVP Demo Workflow](#mvp-demo-workflow)
- [Postmortem Workflow](#postmortem-workflow)
- [Ship Workflow](#ship-workflow)

## Algorithm Research Workflow

目標：學習什麼樣的內容能拿到流量、為什麼，但不亂抄戰術。
對齊 [research/ALGORITHM_RESEARCH.md](../research/ALGORITHM_RESEARCH.md)。

### Trigger

- 「研究這幾篇競品 post。」
- 「這週 X / Threads / Shorts 上有什麼是 work 的？」
- 「為什麼這篇貼文爆了？」

### Structured Input

每個候選 post 必須記下：

- 平台。
- 創作者帳號。
- URL 或截圖路徑。
- 主題。
- Hook（前 1-2 行）。
- Format（thread、chart、carousel、短影片等）。
- 可見 metrics：impressions、likes、replies、reposts、saves、follows。
- 發布日期與時間。
- 觀察到的留言模式。

### Programmatic Checks

- 沒有 platform、hook、metrics 的條目直接拒收。
- 依內容支柱打 tag。
- 比較前先依平台和時間窗分組。
- 「深度訊號」（saves、comments、DMs）和「reach 訊號」（impressions、reposts）分開
  排序。

### LLM Role

- 分類 hook 類型（pain、反共識、framework、故事、demo、列表）。
- 推測表現好的合理原因。
- 提出 3-5 個符合帳號定位的「改編方式」，不是盲抄。
- 標出和 [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md) 衝突的戰術。

### Human Gate

- 必要：核准哪些 pattern 是 on-brand 且符合倫理可以採用的。
- 必要：拒絕「保證收益」、「藏風險」、或「直接抄競品具體宣稱」這種戰術。

### Output Artifact

- 更新或新增 swipe file 條目。
- 用 `research/ALGORITHM_RESEARCH.md` 的格式產出 3-5 個內容 hypothesis。
- 明確記下一個「不採用」的理由。

## Audience Discovery Workflow

目標：理解非 AI agent 使用者，把 pain 變成 MVP 候選與內容角度。
對齊 [research/AUDIENCE_DISCOVERY.md](../research/AUDIENCE_DISCOVERY.md)。

### Trigger

- 「我剛做完一場訪談，幫我記錄。」
- 「把目前的 pain 做 cluster。」
- 「依目前證據選下一個 MVP。」

### Structured Input

每筆訪談或觀察要有：

- Source：訪談、DM、留言、客服、公開貼文。
- 使用者 segment（依 `CONTENT_STRATEGY`）。
- 逐字 quote。
- 目前的 workaround。
- 現在付費的工具。
- 什麼會讓他們把工具分享出去。
- 敏感性 flag（金融資料、受監管資訊）。

### Programmatic Checks

- 沒有 verbatim quote 的條目拒收。
- 標記 pain 短語。
- 在 cluster 之前先計算跨來源的重複次數。
- 過濾掉不符合 MVP selection filter 的 cluster（沒有清楚使用者、沒有 5 分鐘可
  完成結果、需要敏感憑證等）。

### LLM Role

- 把 pain statement 分群成 themes。
- 把每個 theme 轉成 1-2 個 MVP 候選與 1-2 個內容角度。
- 為每個 MVP 候選寫一句「promise」。
- 標出有趣但不可建造的 cluster。

### Human Gate

- 必要：選下一個要建的 pain。
- 必要：確認敏感資料邊界（不碰 brokerage、不碰 PII）。

### Output Artifact

- 更新後的 pain cluster doc。
- 排序過的 MVP 候選清單，附 one-line promise。
- 同一個 pain 對應的 3-5 個內容角度。

## Investment Analysis Workflow

目標：產出可重複、可審查、可公開的市場分析。
對齊 [research/INVESTMENT_ANALYSIS_PLAYBOOK.md](../research/INVESTMENT_ANALYSIS_PLAYBOOK.md)
和 [ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md)。

### Trigger

- 「做這週的市場分析。」
- 「分析這個新聞事件。」
- 「Review 這個策略 / 回測。」

### Structured Input

- 要回答的問題。
- 時間區間。
- 標的範圍。
- 資料輸入：macro、breadth、leadership、news、technicals、sentiment。
- 每個資料點的 source。
- 任何持倉或 watchlist 衝突。

### Programmatic Checks

- 驗證 ticker notation、單位、日期、星期一致性。
- 先跑可用的 trading skills（見 playbook 中的 Skill Mapping）：
  market-environment、macro-regime-detector、market-breadth-analyzer、
  uptrend-analyzer、market-top-detector、theme-detector、market-news-analyst、
  technical-analyst、scenario-analyzer、backtest-expert、data-quality-checker。
- 資料品質有問題就 block 後續分析。

### LLM Role

- 綜合 regime、breadth、leadership、news、technicals、sentiment。
- 產出帶有 invalidation 條件的 scenarios。
- 用 playbook 的公開模板起草公開貼文。
- 對自己的 draft 做「過度確定語言」與「弱 sourcing」的檢查。

### Human Gate

- 任何包含市場宣稱的公開內容前必走。
- 任何持倉相關的公開內容前必走。
- 任何回測 / 策略宣稱前必走。

### Output Artifact

- 內部分析 brief。
- 套用 playbook 公開模板的公開貼文 draft。
- Source checklist：每個宣稱對應到 source。
- Invalidation 列表：什麼會改變我的看法。

## Content Production Workflow

目標：把一個 content hypothesis 推到完成的 post 或素材。
對齊 [content/CONTENT_OPERATING_SYSTEM.md](../content/CONTENT_OPERATING_SYSTEM.md)
和 [docs/CONTENT_STRATEGY.md](CONTENT_STRATEGY.md)。

### Trigger

- 「規劃這週的內容。」
- 「寫一篇關於 X 的 post。」
- 「把這篇分析改成 thread / short / carousel。」

### Structured Input

- Content brief 欄位（date、platform、audience、pain point、pillar、hypothesis、
  hook、main idea、evidence、visual asset、CTA、risk note、success metric）。
- 來源 artifact：分析 brief、MVP demo、postmortem、訪談 cluster。
- 平台 format 限制。

### Programmatic Checks

- 缺 audience、hook、success metric 的 brief 拒收。
- 檢查發布日曆有沒有重複或節奏漂移。
- 若主題屬高風險，要求先跑 investment-analysis workflow。

### LLM Role

- 起草 2-3 個 hook 變體。
- 依平台調整 body text。
- 建議一個 visual asset 與 one-line caption。
- 用 `CONTENT_OPERATING_SYSTEM.md` 的 review checklist 自我檢查。

### Human Gate

- 高風險內容必走（依 [docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md)）。
- 低風險教育文可選，但建議仍快速人工讀過。

### Output Artifact

- 最終 draft 存進 `content/drafts/`，使用 date-first naming。
- Asset brief。
- Schedule entry。
- 完成的 pre-publish checklist。

## MVP Demo Workflow

目標：把選定的 pain 變成可上架的小 demo，不要先做完整產品。
對齊 [mvp/MVP_LAB.zh.md](../mvp/MVP_LAB.zh.md)。

### Trigger

- 「Spec 下一個 demo。」
- 「做一個小版的這個 pain。」
- 「決定 demo X 是 keep / improve / kill。」

### Structured Input

- Pain statement 與 quote。
- Target user。
- 現有 workaround。
- Promise：一句話說明 5 分鐘內的成果。
- Input 與 output 欄位。
- 資料來源，特別是需要憑證的。
- Trust / safety 顧慮。
- Build scope 與明確 non-goals。

### Programmatic Checks

- 需要 brokerage 憑證或 PII 的直接 reject。
- 無法用一篇 post 或一支短片展示的 reject。
- 沒有清楚 feedback question 的 reject。

### LLM Role

- 用 `MVP_LAB.md` 模板起草 MVP spec。
- 起草 demo flow。
- 起草配 demo 的 launch post。
- 根據可觀察的 feedback 提出 kill criterion。

### Human Gate

- 必要：寫任何 code 之前先核准 scope 與安全邊界。
- 必要：任何加入帳戶整合、付款、或儲存使用者資料的改動前都要走 gate。

### Output Artifact

- MVP spec 存到 `mvp/`。
- Build milestone 列表。
- 配套 launch-post brief 放到 `content/drafts/`。
- 明確的 kill criterion 與 review date。

## Postmortem Workflow

目標：把錯誤判斷、漏掉的 scenario、表現不佳的實驗，轉成 structured 學習。投資分析
和內容/MVP 都會用到。

### Trigger

- 「這個 call 沒過時間考驗。」
- 「這個實驗表現差。」
- 「這個 demo 沒人用。」

### Structured Input

- 原始 artifact（post、analysis、MVP spec）。
- 原始 hypothesis 與成功指標。
- 觀察到的結果，含資料和時間。
- 過程中的決策點。

### Programmatic Checks

- 從 metrics tracker 拉 metrics。
- 確認原始 artifact 還在，且發布後沒被改過。

### LLM Role

- 重建：當時假設是什麼、觀察到什麼、決定了什麼。
- 找出假設在哪裡破掉。
- 提議對對應 playbook 或 workflow 加上的 guardrail。

### Human Gate

- 公開 postmortem 前必走（屬高風險內容）。
- 要更新 playbook 必走，因為改 default 會影響未來所有 workflow。

### Output Artifact

- Postmortem note 存在原 artifact 旁邊。
- 可選的公開 postmortem draft。
- 對 playbook 或 workflow pattern 的修改建議。

## Ship Workflow

目標：把完成的工作變成乾淨的 git 歷史。在其他 workflow 完成、artifact 就緒時觸發。
對齊 [docs/IMPLEMENTATION_PLAN.zh.md](IMPLEMENTATION_PLAN.zh.md) 的 branch 與
commit 策略。

存在這個 workflow 的原因：agent 自己不知道該直接 commit 到 `main` 還是開 branch、
是否該 push、要不要先暫停。它也負責草擬本 repo 慣用的 conventional commit 訊息。

### Trigger

- 其他 workflow 已產出 artifact，使用者表示這個任務告一段落。
- 使用者說「ship」、「commit」、「收尾」，或之後加入 `/ship` 時觸發。
- 一段工作 session 要結束，但還有 uncommitted 變更。

### Structured Input

- `git status --short` 輸出。
- `git diff --stat` 輸出。
- 依區域分組的檔案：`docs/`、`scripts/`、`mvp/`、`content/`、`research/`、
  `ops/`、`.cursor/`、root。
- 變更類型分類：docs、content、script、mvp、chore、fix。
- 目前 branch 名稱與 remote tracking 狀態。

### Programmatic Checks

- 沒有可 commit 的東西就 reject。
- detached HEAD 上不操作，除非使用者明確指示。
- 看起來像 secret 的檔案（`.env*`、credential JSON、私鑰）拒絕 commit。
- 驗證 artifact 引用到的檔案是否真的存在。

### LLM Role

- 依 `IMPLEMENTATION_PLAN.zh.md` 的規則判斷：直接 commit 到 `main` 還是開 branch。
- 若 diff 混了多種主題，建議切成多個 logical commit。
- 起草 conventional commit 訊息（`feat:`、`docs:`、`script:`、`mvp:`、`fix:`、
  `refactor:`、`chore:`）。
- 需要 branch 時建議 branch 名稱。
- 建議是否 push、push 到哪個 branch。

### Human Gate

- 強制：在使用者明確 approve 之前，永遠不 commit、不 push、不 create branch，
  即使規則說安全也一樣。
- 把 git 計畫整段顯示給使用者：branch 決策、staged 檔案、commit 訊息、push 目標。
- 決策：approve、edit、reject。
- 推到 `main` 必須額外多一次確認。

### Output Artifact

- 實際 `git commit` 與選擇性 `git push`。
- 在 [docs/IMPLEMENTATION_PLAN.zh.md](IMPLEMENTATION_PLAN.zh.md) 的 Progress
  Log append 一行。
- 開新 branch 時，使用者要求才在 GitHub 開 self-PR。

## Workflow 串接

大部分真實任務都是串好幾個 workflow。範例：

- 每週發布：investment-analysis → content-production → ship。
- Demo launch：audience-discovery → mvp-demo → content-production → ship。
- 競品掃描：algorithm-research → content-production → ship。
- 錯誤判斷恢復：postmortem → content-production（透明 post）→ playbook 更新 → ship。

Agent 必須在任務開頭明確宣告 chain，過程中如果現實逼著順序改變，要更新 chain。
有檔案變更時，ship workflow 永遠是最後一環。
