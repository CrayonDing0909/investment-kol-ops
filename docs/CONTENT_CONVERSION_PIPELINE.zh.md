# Content Conversion Pipeline（中文版）

> 中文鏡像 / 對照原文：[CONTENT_CONVERSION_PIPELINE.md](CONTENT_CONVERSION_PIPELINE.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

**raw research** 和 **public artifact** 之間缺的那一層。這份文件定義必經階段、
階段之間的 gate，以及防止「把知識地圖直接丟給觀眾」的規則。

方向錨點：[docs/NORTH_STAR.zh.md](NORTH_STAR.zh.md)。Artifact 模型：
[docs/ARTIFACT_SYSTEM.zh.md](ARTIFACT_SYSTEM.zh.md)。Gate：
[docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md)。語氣：
[docs/VOICE_PROFILE.zh.md](VOICE_PROFILE.zh.md)。

## 為什麼需要這個

A1-001 之所以失敗，是因為它**直接從知識地圖生出來**：它把整張供應鏈圖渲染出來、
第一屏丟了 10 幾個沒解釋的術語、沒有一句記得住的重點、語氣像 AI 解說而不像 owner
本人。見
[ops/postmortems/2026-06-01_a1-001-ep1-one-map_postmortem.md](../ops/postmortems/2026-06-01_a1-001-ep1-one-map_postmortem.md)。

根因不是文筆爛，是**缺一層轉換**。repo 原本是「研究 → ??? → public artifact」，中間
是空的。這個 pipeline 用兩份 owner 核准的合約把缺口補起來：**Series Bible** 與
**Episode Contract**。

## 核心原則

**Artifact-led 是 comprehension-first（理解優先），不是 completeness-first（完整優先）。**

- 內部 artifact 可以又完整又密（它服務研究）。
- 公開 artifact 必須好懂、值得看（它服務觀眾）。公開 artifact 是內部素材的
  **重新創作**，永遠不是「渲染」。

## Pipeline

```text
原始研究 / sources
  → 內部 artifact            （知識地圖、primer、source-tutor、brief）        [完整優先]
  → Series Bible             （受眾、敘事弧、每集一句話、語氣、術語政策）       [owner 核准]
  → Episode Contract         （一句話、不講什麼、比喻、術語預算）              [owner 核准，逐集]
  → 公開產出                  （HTML / IG / Shorts / 公開貼文）               [理解優先]
  → Gate A                   （Safety Check + Owner Comprehension Check）
  → 發布
```

每一個箭頭都是真的步驟，不能跳。

## 階段定義

### 1. 內部 artifact（完整優先）
知識地圖、primer、source-tutor reading、brief。放在 `research/**`。為正確與覆蓋率
最佳化。**不**面向觀眾。它是 pipeline 的輸入，不是公開產出。

### 2. Series Bible（owner 核准）
每個內容系列一份，用
[content/templates/series-bible.md](../content/templates/series-bible.md)。
定義：受眾、承諾、三階段弧（科普 / 機制 / thesis）、每一集規劃的單一重點、語氣
參照、術語政策、連結放置階段。Series Bible 是「我們知道什麼」與「我們要教什麼」的
邊界。

### 3. Episode Contract（owner 核准，逐集）
每集一份，用
[content/templates/episode-contract.md](../content/templates/episode-contract.md)。
把敘事合約寫死：這集讀者必須記住的一句話、這集**不**講什麼、用什麼比喻、第一屏
術語預算、理解目標（讀者看完能複述什麼）。**在生成任何公開產出前，必須先經 owner
核准。**

### 4. 公開產出（理解優先）
HTML 閱讀面、IG carousel、Shorts、公開貼文。**只有在 Episode Contract 核准後**才能
生成，而且只能在合約限制內生成。

### 5. Gate A（Safety + Comprehension）
見 [docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md)。Gate A 現在同時需要 Safety Check 與
Owner Comprehension Check。**安全不等於可發布。**

## 硬規則（pipeline 不變量）

1. **公開 artifact 不能直接從知識地圖生成。** 必須先過 Series Bible 與 Episode
   Contract。
2. **Episode Contract 必須在生成 HTML / IG / Shorts / 公開貼文前經 owner 核准。**
   合約沒簽，不准產出。
3. **Gate A = Safety Check + Owner Comprehension Check。** 兩個都要。
4. **安全不等於可發布。** 過安全 checklist 是必要、不是充分條件。
5. **Artifact-led 是理解優先，不是完整優先。**
6. **如果 owner 說「我沒學到東西」，Gate A 不能 approve。** Artifact 退回 rebuild
   （重開 Episode Contract），不是輕量潤稿。

## 改了什麼

| 之前 | 之後 |
|------|------|
| 研究 → 公開 artifact（中間空的） | 研究 → 內部 artifact → Series Bible → Episode Contract → 公開產出 |
| Gate A = 只看安全 | Gate A = 安全 + 理解 |
| 「完整且正確」是標準 | 「好懂且值得看」是公開標準 |
| 知識地圖可被渲染成公開 HTML | 公開 artifact 必須重新創作，不能渲染 |

## 與其他文件的關係

- Artifact 類別（內部 vs 公開）：[docs/ARTIFACT_SYSTEM.zh.md](ARTIFACT_SYSTEM.zh.md)。
- Gate A 理解檢查：[docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md)。
- 系列弧 + 語氣：[.cursor/rules/series-narrative-architecture.mdc](../.cursor/rules/series-narrative-architecture.mdc)、
  [docs/VOICE_PROFILE.zh.md](VOICE_PROFILE.zh.md)。
- Brief 前置條件：[content/templates/artifact-brief.md](../content/templates/artifact-brief.md)。
