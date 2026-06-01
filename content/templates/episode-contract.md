---
workflow: content-production
artifact_type: episode-contract-template
status: template
created_at: 2026-06-01
---

# Episode Contract Template

> Purpose：每一集公開內容開工前先寫這份「敘事合約」。它把「這集只教一句話」釘死，
> 並設好術語預算與理解目標。**Episode Contract 未經 owner 核准前，不得生成 HTML /
> IG / Shorts / 公開貼文。**
>
> 系統定義：[docs/CONTENT_CONVERSION_PIPELINE.md](../../docs/CONTENT_CONVERSION_PIPELINE.md)。
> Gate A 的理解檢查：[docs/HUMAN_GATES.md](../../docs/HUMAN_GATES.md)。

## Frontmatter

```yaml
workflow: content-production
artifact_type: episode-contract
series: <series-slug>
episode: <integer>
phase: <explainer | mechanism | thesis>
series_bible_ref: <相對路徑到該系列已核准的 series-bible>
owner_approved: false            # owner 核准後改 true，並填日期
owner_approved_at:
created_at: YYYY-MM-DD
```

## 1. 這集只要觀眾記住哪一句話？（One-takeaway）

> 一句話。寫不出來 = 這集還沒準備好。必須與 series-bible 該集的 one-takeaway 一致。

## 2. 這集不要講什麼？（What NOT to say）

- 例：不列公司名 / 不講受惠股 / 不放 BOM 數字 / 不下買賣判斷 / 不像供應鏈清單。

## 3. 這集用的比喻是什麼？（Metaphor）

- 一個降低理解成本的比喻。只有真的能幫助理解時才用；不要硬套、不要講太滿。

## 4. 第一屏術語預算（First-screen jargon budget）

- 第一屏最多幾個陌生名詞？（explainer 預設 0）
- 任何術語第一次出現必須立刻白話解釋，否則不准用。
- 明確列出**本集禁用詞**（例：hyperscaler / CoWoS / ABF / MLCC / CDU…）。

## 5. 理解目標（Comprehension target）

> 觀眾看完，應該能用「自己的話」講出哪一句？（寫出預期的讀者複述句）

## 6. 語氣（Voice）

- 參照 series-bible + [docs/VOICE_PROFILE.zh.md](../../docs/VOICE_PROFILE.zh.md)。
- 本集語氣要點（第一人稱 / 不確定 / 括號內心話 / 觀眾嘴替）。

## 7. 結尾（Ending）

- 只 tease 下一集，不做投資判斷（explainer / mechanism 階段）。

## Owner Comprehension 預檢（對齊 Gate A）

owner 核准合約前，先用這四問檢查「合約本身」是否能導向可理解的成品：

1. [ ] 5 秒內知道這集要教什麼？
2. [ ] 看完能用一句話講出學到什麼？（= §5）
3. [ ] 第一屏陌生名詞是否 ≤ 預算（explainer = 0）？
4. [ ] 這會是一個作品，還是資料堆疊？

## Owner 核准

- [ ] Owner 已 review 並同意這份 Episode Contract
- 核准後：`owner_approved: true` + 填日期；**此後才可生成公開產出**。

## Disclaimer

This is research and education, not financial advice.
