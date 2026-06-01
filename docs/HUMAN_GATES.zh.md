# Human Gates（中文版）

> 中文鏡像 / 對照原文：[HUMAN_GATES.md](HUMAN_GATES.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

目的：定義「人類必須先 approve 才能往下」的節點。Gate 是要抓 agent 不知道自己錯
的時刻，不是要拖慢每一步。

對齊 [docs/AGENTIC_HARNESS.zh.md](AGENTIC_HARNESS.zh.md)、
[docs/WORKFLOW_PATTERNS.zh.md](WORKFLOW_PATTERNS.zh.md)、
[ops/RISK_AND_COMPLIANCE.md](../ops/RISK_AND_COMPLIANCE.md)。

## Gate 設計原則

- Gate 用來保護不可逆或難以挽回的動作。
- Gate 用來保護可能造成名譽、財務、合規傷害的動作。
- Gate 不是用來檢查瑣碎格式或感覺的。
- 每個 gate 都要有：trigger、給人類看的 artifact、決策選項、決策後行為。

## 風險等級

Harness 的風險分類器會給每個 output 打 tag：

| 等級 | 例子 | 預設行為 |
|------|------|----------|
| Low | 內部 swipe、draft hook、draft pain cluster、內部筆記。 | 自動存 artifact。 |
| Medium | 一般主題的公開 post、改寫內容、demo 截圖。 | 跑 pre-publish checklist。可選人工讀過。 |
| High | 投資宣稱、回測宣稱、持倉相關內容、MVP launch、公開更正、付費 offer。 | 強制 human gate。 |

Workflow 可依情境提升風險等級。例如「general」內容若包含具體買賣建議，會升為高風險。

## 兩層發布 Gate：A vs B

不是每個公開 artifact 都要走重量級投資觀點審查。依 artifact 宣稱什麼來路由，
對齊 [docs/ARTIFACT_SYSTEM.zh.md](ARTIFACT_SYSTEM.zh.md) 的分級。

- **Gate A - Artifact Publish（輕量，預設）。** 給教育型 / 視覺型 artifact：
  供應鏈地圖、公司卡、ETF X-ray、explainer、名詞視覺化。大多數 L1/L2 artifact。
- **Gate B - Investment View（重量級）。** 給方向 / 部位內容：市場方向 call、
  個股買賣判斷、bull/base/bear、winner/loser、回測 / 策略結果。既有的 **IA1**
  與 **IA2** 就是 Gate B 家族。

路由：

```text
這個 artifact 有沒有做方向 / 部位 / 買賣 / 回測宣稱？
  沒有 -> Gate A（checklist 過了就能發）
  有   -> Gate B（IA1，若涉策略 / 回測再加 IA2）
```

不確定就往上走 Gate B。一個教育型 artifact 若暗示了一筆交易，就變成 Gate B。

### Gate A - Artifact Publish

Trigger：任何不做方向、部位、買賣、目標價、回測宣稱的公開教育 / 視覺型 artifact。

給人類看：

- Artifact（圖 / 地圖 / 卡 / 腳本）與它的公開版本。
- Source note：每個關鍵宣稱對應至少一個 source。
- 不確定性 label（哪裡還沒驗證）。

Gate A 有**兩個**必過檢查。**安全不等於可發布** —— 兩個都要過。

**檢查一 — Safety Check（全部必填）：**

- [ ] 至少有一個 source 且有 label。
- [ ] 沒有買賣 call。
- [ ] 沒有目標價。
- [ ] 沒有個人化投資建議。
- [ ] 有標不確定性。

**檢查二 — Owner Comprehension Check（全部必填）：**

由 owner（或替身目標讀者）看完 artifact 後回答：

- [ ] 1. 我 5 秒內知道這篇要教我什麼嗎？
- [ ] 2. 我看完能用一句話講出學到什麼嗎？
- [ ] 3. 第一屏陌生名詞是否 ≤3 個？（explainer 目標：0）
- [ ] 4. 這是作品，還是資料堆疊？

**硬規則：** 若 owner 說「我沒學到東西」，Gate A **不能 approve**。Artifact 退回
**rebuild**（依 [docs/CONTENT_CONVERSION_PIPELINE.zh.md](CONTENT_CONVERSION_PIPELINE.zh.md)
重開 Episode Contract），不是輕量潤稿。公開 artifact 到達這個 gate 前，必須已經過
它的 Episode Contract；把知識地圖直接渲染成公開形式，從定義上就過不了 Gate A。

決策：approve（發布）、edit、reject（rebuild）。

決策後：

- Approved artifact 可不過 IA1 直接發布。
- 若 review 發現有方向 / 部位宣稱，升級走 Gate B（IA1），不要用 Gate A approve。
- 決策像其他 gate 一樣記在 artifact 旁（或 `ops/decisions/`）。

## 強制 Gate

下列 gate 不能跳過。即使 draft 看起來沒問題，agent 也必須等人類。IA1 與 IA2 是
上面提到的 Gate B 投資觀點家族。

### Gate IA1 - 投資宣稱發布（Gate B）

Trigger：任何包含市場方向 call、regime 宣稱、持倉暗示、回測結果、策略結果的公開
artifact。

給人類看：

- Draft post 或 asset。
- Source checklist：每個宣稱對應到 source。
- Invalidation 列表。
- Risk and compliance pre-publish checklist。

決策：

- Approve。
- Edit（退回，附 note）。
- Reject（封存，附原因）。

決策後：

- Approved drafts 進排程。
- Edited drafts 從 LLM 階段重跑，不從頭開始。
- Rejected drafts 保留在 `content/drafts/` 並附 rejection note。

### Gate IA2 - 策略 / 回測公開宣稱

Trigger：任何討論策略、回測、量化結果的公開 artifact，包括教學說明。

給人類看：

- 全部品質 gate 項目：lookahead bias、樣本數、fees、slippage、OOS / walk-forward、
  drawdown、turnover、exposure、failure conditions。
- Draft 中使用的 caveat 語言。

決策：approve、edit、reject。

決策後：同 IA1，加上在 `ops/METRICS.md` 記錄信任追蹤。

### Gate MVP1 - MVP Scope 與安全

Trigger：任何新 MVP spec，或任何加入帳戶整合、付款、儲存使用者資料的改動。

給人類看：

- MVP spec。
- 資料來源，含需要憑證的。
- Trust / safety 顧慮。
- Build scope 與明確 non-goals。
- Kill criterion。

決策：

- Approve to build。
- Edit scope。
- Reject（封存 idea）。

決策後：

- Approved spec 移到 `mvp/` 並加 build milestone 列表。
- Approved spec 觸發配套的 launch-post brief 進入 content production。

### Gate MVP2 - Demo Launch

Trigger：任何 demo 公開上線（含 soft launch）。

給人類看：

- Demo URL 或截圖。
- Launch post draft。
- Feedback capture 機制。
- Demo 輸出的 risk and compliance check。

決策：approve、edit、delay。

### Gate AR1 - 採用 Algorithm Research 戰術

Trigger：algorithm-research workflow 建議採用觀察到的 hook、format、framing 時。

給人類看：

- 候選 post。
- 建議的改編方式。
- 「不採用」的理由（如有）。
- 對 `RISK_AND_COMPLIANCE.md` 的衝突檢查。

決策：approve、modify、reject。

### Gate AD1 - 選下一個 MVP Pain

Trigger：audience-discovery workflow 提出下一個要建的 pain。

給人類看：

- Pain cluster 摘要。
- 排序的 MVP 候選清單。
- 敏感資料 flag。
- 使用者已經為類似問題付費的 workaround。

決策：approve、defer、reject。

### Gate PM1 - 公開 Postmortem

Trigger：任何錯誤判斷或失敗實驗的公開 postmortem。

給人類看：

- 原始 artifact 與日期。
- 重建的假設、觀察、決策。
- 學到的事與建議的 playbook 更新。

決策：approve、edit、改為內部不公開。

## 選擇性 Gate

下列 gate 可跳過，但建議使用。Agent 可自動往下，除非該 sprint 設定為 mandatory。

### Gate CP1 - 每週內容日曆

開始 draft 前選擇性的人工 review。在高產量 sprint 比較有用。

### Gate CP2 - 改寫批准

當一個來源 artifact 要被切成多種 format 時，選擇性人工 review，避免單一想法被
重複過度發布。

## 決策紀錄

每個 human gate 決策都要記下：

- 日期。
- Workflow。
- Artifact 引用。
- 決策。
- 一句話原因。

紀錄存在「該決策對應的 artifact 旁邊」，不存在另一個獨立 database。

## Agent 不確定時

不確定 gate 是否適用 → 預設啟用 gate。問人類成本很小；錯誤的公開投資宣稱成本很大。

如果使用者明確 waive 某個低風險 gate，agent 必須把這個 waiver 記在 artifact 旁邊，
不只記在 chat。
