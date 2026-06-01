# Artifact System（中文版）

> 中文鏡像 / 對照原文：[ARTIFACT_SYSTEM.md](ARTIFACT_SYSTEM.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

這個專案的核心單位是 **artifact（作品）**，不是 research brief。這份文件定義
artifact 是什麼、用哪些級別決定每個 artifact 需要多少人工投入，以及從 idea 到
已發布、已量測的完整生命週期。

方向錨點：[docs/NORTH_STAR.zh.md](NORTH_STAR.zh.md)。

## 定義

Artifact 是一個可被觀眾看見、理解、保存、分享的金融圖解作品：一張圖、一個供應鏈
節點地圖、一個 ETF X-ray、一張公司卡、一個 AI 工具 demo，或一張市場地圖。

Research packet 與 brief 仍然存在，但它們現在是 artifact 底下的「研究品質層」，
不是交付物本身。

## 內部 artifact vs 公開 artifact

不是每個 artifact 都給觀眾看。分成兩類，兩者標準不同、放的地方也不同。

| 類別 | 為什麼最佳化 | 放在 | 標準 | 例子 |
|------|------|------|------|------|
| 內部 artifact | 完整 / 正確 | `research/**` | 正確 + 完整 | 知識地圖、primer、source-tutor reading、brief |
| 公開 artifact | 理解 / 值得看 | `content/**`、系列閱讀面 | 一個人有學到一件事 | Threads、IG carousel、Shorts、公開 HTML explainer |

規則：

- **公開 artifact 永遠不是知識地圖的渲染。** 它必須經過 Content Conversion
  Pipeline（[docs/CONTENT_CONVERSION_PIPELINE.zh.md](CONTENT_CONVERSION_PIPELINE.zh.md)）
  重新創作：內部 artifact 餵 Series Bible 與一份 owner 核准的 Episode Contract，
  之後才生成任何公開產出。
- **Artifact-led 是理解優先，不是完整優先。** 內部 artifact 可以很密；公開
  artifact 必須好懂。
- 公開 artifact 只有在它的 Episode Contract 核准後才到 Gate A；Gate A 同時需要
  Safety Check 與 Owner Comprehension Check（[docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md)）。
  安全不等於可發布。

## Artifact 類型

1. 供應鏈地圖（Supply Chain Map）
2. 公司卡（Company Card）
3. ETF X-ray
4. AI 工具 Demo
5. 市場地圖（Market Map）
6. 名詞視覺化（Glossary Visual）

對應 [docs/NORTH_STAR.zh.md](NORTH_STAR.zh.md) 的內容支柱。

## 分級：不是每個東西都要完整 brief

最大的疲憊來源，是把每個想法都當成完整投資 brief。用分級決定需要多少 human POV。

| 級別 | 用途 | 需要 human POV？ | 預設 gate |
|------|------|------------------|-----------|
| L1 Signal Note | 一個線索、一則新聞、一個圖表想法 | 不需要 | 無 |
| L2 Artifact Note | 一張圖、一個供應鏈節點、一個 ETF X-ray | 3-5 句 human note | Gate A |
| L3 Research Brief | 可能公開成長文或產品頁 | 完整 POV / invalidation | Gate A；含方向判斷則 Gate B |
| L4 Investment View | 明確個股方向、買賣判斷 | 完整 POV + invalidation | Gate B（必須） |

大多數公開 artifact 應該停在 L2。只有當 artifact 做出方向或部位宣稱時，才升到
L3/L4。

Gate 定義在 [docs/HUMAN_GATES.zh.md](HUMAN_GATES.zh.md)：Gate A 是輕量的
artifact/教育發布 gate；Gate B（IA1/IA2）是重量級的投資觀點 gate。

## Artifact 生命週期

```text
Idea
-> Research
-> Sketch
-> Visual Draft
-> Source Check
-> Content Package
-> Publish
-> Measure
-> Iterate
```

## Definition of Done

一個 artifact 完成的條件：

- [ ] 有一個明確 core question
- [ ] 有一個視覺輸出
- [ ] 有至少一個資料來源
- [ ] 有一句 human insight（不是投資建議）
- [ ] 有至少 2 個公域內容版本（例如 Threads + IG carousel，或 X + Shorts）
- [ ] 有 metrics tracking hook

用 [content/templates/artifact-brief.md](../content/templates/artifact-brief.md)
這份輕量 spec 起一個 L1/L2 artifact。當 artifact 帶 thesis 或方向宣稱（L3/L4）
時，改用 [content/templates/thesis-card.md](../content/templates/thesis-card.md)。

## 既有 repo 工作如何對應到這個模型

這是 reframe，不是重建。既有工作已經能對上：

- `content/cards/**` thesis cards 是 L3/L4 artifact（帶 Counter，常含投資宣稱）。
- `research/knowledge/ai-server-supply-chain/series/thermal/` 的散熱教育系列是
  L2 artifact 系列（教育性、無直接買賣建議）。
- `research/knowledge/<theme>/**` HTML 頁是 artifact 連回的 backbone library。
- `research/sources/**`、`research/intake/**`、`research/notes/**` 是餵養
  L2-L4 artifact 的研究品質層。

## 第一個公開 artifact 系列：AI Server Supply Chain

既有的 AI Server Supply Chain knowledge map，從單一 research packet 改成第一個
公開 artifact 系列：

```text
EP1  AI Server 不是只有 GPU：一張圖看完整供應鏈
EP2  CPU 在 AI Server 裡到底還重不重要？
EP3  ASIC 為什麼會變成 GPU 之外的第二條主線？
EP4  HBM / Memory 到底卡在哪裡？
EP5  散熱為什麼是 AI Server 必經環節？
EP6  被動元件為什麼會被資金注意？
```

每集只需要：一張圖、一個核心問題、三個重點、一個 source note，不做買賣建議。
散熱系列已經實作了 EP5；其餘照同樣 L2 pattern 走。不要每集都硬做完整 brief。

## Anti-patterns

- 把每個想法都做到 L3/L4。
- 在市場還沒對 artifact 有反應前，就先寫完整 POV。
- 讓研究 gate（Gate B）擋住只需要 Gate A 的教育型 artifact。
