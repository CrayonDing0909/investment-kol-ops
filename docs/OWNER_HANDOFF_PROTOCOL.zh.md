# Owner Handoff Protocol（中文版）

> 中文鏡像 / 對照原文：[OWNER_HANDOFF_PROTOCOL.md](OWNER_HANDOFF_PROTOCOL.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

目的：讓 agent 的回覆**以 owner 看得懂為先**，不要 git-status 先行。當任務走到
「需要人（repo owner）做決定」的節點，agent 必須先給一份白話的 **Owner Handoff
Packet**，技術細節放最後。

## 為什麼需要這個

Owner 應該不用讀 git diff、commit 圖、檔案樹，就能知道任何任務目前在哪。Git 是
儲存層，不是溝通層。一個用 `git status` 開頭的回覆，等於逼 owner 自己反推意義。
這份協定把順序反過來：**先講意義，機器細節放最後。**

## 什麼時候觸發

只要符合**任一**條件，就要產出 Owner Handoff Packet：

- 有 human gate 適用（Gate A、IA1、IA2、MVP1、MVP2、AR1、AD1、PM1），而且決定權
  在人手上。
- Agent 卡住，需要 owner 選一條路。
- 任務產生了檔案變更，需要 owner 先核准才能 commit / publish / push。
- Owner 問「我們在哪」「你做了什麼」「我現在該做什麼」。
- [docs/AGENT_ROLES.zh.md](AGENT_ROLES.zh.md) 裡定義的某個 role 走到「需要人類
  決定」的步驟（見該檔的 role 規則）。

如果任務瑣碎、完全可逆、沒有待決事項，一般簡短回覆即可。不確定時，就產出 packet。

## Owner Handoff Packet 格式

用以下六段、照這個順序、用白話寫。預設用 owner 的工作語言（本 repo 為中文），除非
另有要求。保持非技術：正文不要 git 動詞、不要 SHA、不要 diff 術語。

```md
## 1. Current Stage（現在在哪）
- Track（軌道）：     <哪條軌道，例如 A 系列 artifact / 研究 / MVP>
- Item（項目）：      <具體項目或 ID>
- State（狀態）：     <白話狀態，例如 草稿完成、等審>
- Gate（關卡）：      <哪個 gate + 目前決定（defer / pending / 不適用）>
- Public status：     <draft / ready / scheduled / published / 不適用>
- 你現在的角色：      <一句話：只有人能做的下一步>

## 2. 做了什麼（白話）
- <最多 5 點，不用 git 術語，描述成品與意義>

## 3. 你該 review 什麼
- <最多 3 個檔案，依優先序。每個只講「看這一件事」。>

## 4. 你現在要做的決定
- A. <選項>
- B. <選項>
- C. <選項>
- 建議：<其中一個> — <一句話原因>

## 5. 還沒在做的事
- <明列不做清單：發布 / push / gate 核准 / GitHub 物件 / 擴大範圍>

## 6. 下一個最安全動作
- <一句 owner 可以直接點頭的話>

---

### Appendix（技術，選填）
- git status / diff stat / commit SHA 放這裡，永遠不放最上面。
```

## 規則

- **意義先於機器**：六段在前。Git 輸出、SHA、diff、檔案樹只放最後的 Appendix。
- **最多 3 個檔案**（第 3 段）：如果改的更多，分組後挑出與決定最相關的三個。
- **只給一個建議**：第 4 段一定指名單一建議選項並說明原因，即使最終決定權在 owner。
- **講清楚沒在做什麼**：第 5 段必須重申與本任務相關的安全邊界（不發布 / 不 push /
  不核准 gate / 不建遠端 GitHub 物件 / 不擴大範圍）。
- **一句可點頭的話**：第 6 段是一句 owner 可以直接同意的話，agent 之後要做什麼必須
  明確無歧義。
- **handoff 內不翻 gate / 不改 status**：handoff 只報告狀態；它不會自己核准 gate，
  也不會把 `public_status` 改成 `ready`。
- **誠實說明保存狀態**：如果工作區已經乾淨 / 已存檔，就直說，不要暗示有待辦動作。

## Handoff 紀錄放哪

多數 handoff 是對話式的，不需要檔案。若是並行工作、session 交接、或 owner 可能回頭
重看的決定，用 [ops/handoffs/_template.md](../ops/handoffs/_template.md) 在
`ops/handoffs/` 下存一份。這份是補充，不取代 `ops/decisions/` 的 gate 決定紀錄，也
不取代 `ops/sessions/` 的 session 狀態檔。

## 與其他文件的關係

- Gate 與決定：[docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md)、`ops/decisions/`。
- 必須 handoff 的 role：[docs/AGENT_ROLES.zh.md](AGENT_ROLES.zh.md)。
- 每日焦點介面：[NEXT_ACTIONS.md](../NEXT_ACTIONS.md)（其頂部 Current Stage 區塊對齊
  本 packet 的第 1 段）。
- 人類閱讀面規則：[docs/HTML_READING_UI_GUIDE.zh.md](HTML_READING_UI_GUIDE.zh.md)。
