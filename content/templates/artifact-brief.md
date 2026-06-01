---
workflow: content-production
artifact_type: artifact-brief-template
risk: low
status: template
tier: L1-L2
created_at: 2026-05-31
---

# Artifact Brief Template (lightweight, L1/L2)

> Purpose：起一個 educational / visual artifact（一張圖、一個供應鏈節點、
> 一個 ETF X-ray）時用的最小 spec。**刻意保持輕量**：不需要 thesis、不需要
> Counter、不需要完整投資 POV。
>
> 什麼時候用這份：L1 Signal / L2 Artifact（教育、解釋、圖解，無買賣判斷）。
> 什麼時候改用 thesis-card：當 artifact 帶 thesis 或方向判斷（L3/L4）時，改用
> [content/templates/thesis-card.md](thesis-card.md)。
>
> 系統定義：[docs/ARTIFACT_SYSTEM.md](../../docs/ARTIFACT_SYSTEM.md)。
> 發布走 Gate A（[docs/HUMAN_GATES.md](../../docs/HUMAN_GATES.md)）。

## 前置條件（生成任何公開產出前必過）

本 brief 屬於
[docs/CONTENT_CONVERSION_PIPELINE.md](../../docs/CONTENT_CONVERSION_PIPELINE.md)
的一環。**在生成 HTML / IG / Shorts / 公開貼文之前**，必須先具備：

- [ ] 該系列已核准的 **Series Bible**（[series-bible.md](series-bible.md)）
- [ ] 該集 owner 核准的 **Episode Contract**（[episode-contract.md](episode-contract.md)）

沒有這兩份，這份 brief 只能停在規格層，**不得產出公開內容**。公開 artifact 不是
知識地圖的渲染，必須 comprehension-first 重新創作。

## Frontmatter

```yaml
workflow: content-production
artifact_type: artifact
tier: <L1 | L2>
risk: low            # 無買賣判斷才是 low；一旦帶方向判斷 → 升 L3/L4 + Gate B
artifact_kind: <supply-chain-map | company-card | etf-xray | ai-tool-demo | market-map | glossary-visual>
core_question: <一句話：這個 artifact 要回答什麼？>
backbone_ref: <連回 research/knowledge/<theme>/ 的 HTML page（若有）>
series_bible_ref: <相對路徑到該系列已核准的 series-bible（公開產出前必填）>
episode_contract_ref: <相對路徑到該集 owner 核准的 episode-contract（公開產出前必填）>
sources:
  - <source 1 + label（reported-fact / management-expectation / secondary / ...）>
created_at: YYYY-MM-DD
public_status: <draft | ready | scheduled | published>
```

## Body

### Core question（1 句）

這個 artifact 要回答的一個具體問題。

### Visual output（1 個）

要做出的視覺：一張圖 / 一個地圖 / 一張卡 / 一個 UI screenshot。寫清楚形式即可。

### 3 key points（最多 3 點）

1.
2.
3.

### Source note

- 至少 1 個資料來源 + label。沒有 source 的內容不進公開 artifact。

### Human insight（1 句）

我看完這個 artifact 後，多理解了什麼？**不是投資建議**，是一句理解。

### Public versions（至少 2）

- [ ] Threads（用 thesis-card / 一般貼文格式）
- [ ] IG carousel（[content/templates/ig-carousel.md](ig-carousel.md)）
- [ ] YouTube Shorts（[content/templates/youtube-shorts.md](youtube-shorts.md)）
- [ ] X long post

### Metrics hook

- 發布後建立 post-publish log（參考
  [ops/decisions/2026-05-19_24h-postpublish-metrics-checklist.md](../../ops/decisions/2026-05-19_24h-postpublish-metrics-checklist.md)）。

## Definition of Done（對齊 ARTIFACT_SYSTEM）

- [ ] 有一個明確 core question
- [ ] 有一個視覺輸出
- [ ] 有至少一個資料來源
- [ ] 有一句 human insight（不是投資建議）
- [ ] 有至少 2 個公域內容版本
- [ ] 有 metrics tracking hook
- [ ] 公開產出前：Series Bible + Episode Contract 皆已 owner 核准
- [ ] Gate A 同時通過 Safety Check 與 Owner Comprehension Check（owner 看完有學到一件事）

## Disclaimer

This is research and education, not financial advice.
