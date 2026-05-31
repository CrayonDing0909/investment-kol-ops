---
workflow: content-production
artifact_type: ig-carousel-template
risk: medium
status: template
created_at: 2026-05-31
---

# IG Carousel Template

> Purpose：把一個 artifact 拆成 6-8 張 IG carousel slides。重視覺、低文字密度。
> 每張 slide 一個重點，封面 hook 決定停留率。
>
> 來源結構沿用 [content/templates/thesis-card.md](thesis-card.md) 與
> [content/templates/artifact-brief.md](artifact-brief.md)。含投資宣稱 → 走
> Gate B（IA1）；純教育 → Gate A。

## Frontmatter

```yaml
workflow: content-production
artifact_type: ig-carousel
risk: <low | medium | high>
artifact_ref: <相對路徑到 artifact-brief 或 thesis-card>
slide_count: <6-8>
core_question: <一句話>
created_at: YYYY-MM-DD
public_status: <draft | ready | scheduled | published>
published_at:
post_url:
```

## Slide plan

### Slide 1 — Cover / Hook

- 一行 hook（用 lens 或 core question，不要 clickbait）。
- 一個視覺 anchor（數字 / 圖示）。
- 角落放系列標記（例：AI Server #1）。

### Slide 2 — Core question / Why care

- 把問題講清楚：讀者為什麼該在意這 30 秒。

### Slide 3-5 — 3 key points（一張一點）

- Slide 3：重點 1（圖 + 1-2 句）
- Slide 4：重點 2
- Slide 5：重點 3

### Slide 6 — Source / Caveat

- 資料來源 + 一句不確定性 label（哪裡還沒驗證）。

### Slide 7 — Insight + CTA

- 一句 human insight（不是投資建議）。
- CTA：連回 library backbone page / 邀互動 / follow。
- Disclaimer 一句。

## Visual checklist

- [ ] 每張 slide 文字 ≤ 40 字，靠視覺承載
- [ ] 字級在手機可讀（標題 ≥ 大，內文 ≥ 中）
- [ ] 配色一致，系列有共用模板
- [ ] 封面停留 hook 明確
- [ ] 最後一張有 CTA + disclaimer

## Review checklist（發布前）

- [ ] Hook 不是 clickbait
- [ ] 有 source + label
- [ ] 無買賣建議 / 無目標價（否則升 Gate B）
- [ ] 有不確定性 label
- [ ] 含投資宣稱 → 已過 IA1（Gate B）

## Disclaimer

This is research and education, not financial advice.
