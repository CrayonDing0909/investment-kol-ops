---
workflow: content-production
artifact_type: series-bible-template
status: template
created_at: 2026-06-01
---

# Series Bible Template

> Purpose：每個內容系列開工前先寫這份。它是「我們知道什麼（內部 artifact）」與
> 「我們要教什麼（公開產出）」之間的邊界。**Series Bible 未經 owner 核准前，不得
> 生成任何公開產出。**
>
> 系統定義：[docs/CONTENT_CONVERSION_PIPELINE.md](../../docs/CONTENT_CONVERSION_PIPELINE.md)。
> 系列弧與語氣：[.cursor/rules/series-narrative-architecture.mdc](../../.cursor/rules/series-narrative-architecture.mdc)、
> [docs/VOICE_PROFILE.zh.md](../../docs/VOICE_PROFILE.zh.md)。

## Frontmatter

```yaml
workflow: content-production
artifact_type: series-bible
series: <series-slug>            # e.g. ai-server-overview
theme_backbone: <連回 research/knowledge/<theme>/ 的內部 artifact（知識地圖 / primer）>
audience: <一句話：這個系列是寫給誰看的>
owner_approved: false            # owner 核准後改 true，並填日期
owner_approved_at:
link_phase: <early | mid | late> # 連結放置政策，見 series 規則
created_at: YYYY-MM-DD
```

## 1. 受眾（Audience）

- 這個系列是寫給誰看的？他們**現在**已經懂什麼、**還不**懂什麼？
- 他們為什麼要花時間看？（痛點 / 好奇 / 想搞懂某件事）

## 2. 承諾（Promise）

- 看完整個系列，觀眾會多理解什麼？用一句話寫。

## 3. 三階段弧（Three-Phase Arc）

對齊 series 規則：科普 → 機制 → thesis。每集屬於恰好一個階段。

| 集數 | 階段（explainer / mechanism / thesis） | 這一集的**單一**重點（one-takeaway，一句話） |
|------|------|------|
| EP1 | explainer | <一句話> |
| EP2 | | |
| EP3 | | |
| ... | | |

> 規則：每一集只能有**一句** one-takeaway。寫不出一句話 = 這集還沒準備好。

## 4. 語氣（Voice）

- 參照 [docs/VOICE_PROFILE.zh.md](../../docs/VOICE_PROFILE.zh.md)。
- 這個系列的語氣特徵（第一人稱 / 研究中 / 括號內心話 / 觀眾嘴替…）。

## 5. 術語政策（Jargon Policy）

- 哪些術語**整個系列前期禁用**，或第一次出現必須白話解釋？
- 第一階段（explainer）預設：第一屏 0 個專有名詞。

## 6. 連結政策（Link Placement）

- 依 series 規則的 early / mid / late 階段。預設 early：主貼文與第一則回覆都不放
  外部連結。

## 7. 內部 artifact 來源（Internal sources）

- 這個系列的內容來自哪些**內部 artifact**（知識地圖 / primer / brief）？
- 提醒：公開產出是這些內部素材的**重新創作**，不是渲染。

## Owner 核准

- [ ] Owner 已 review 並同意 audience / promise / arc / voice / jargon policy
- 核准後：`owner_approved: true` + 填日期；此後才可進入各集的 Episode Contract。
