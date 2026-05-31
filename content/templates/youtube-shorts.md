---
workflow: content-production
artifact_type: youtube-shorts-template
risk: medium
status: template
created_at: 2026-05-31
---

# YouTube Shorts Script Template

> Purpose：把一個 artifact 變成 30-60 秒直式短影音腳本。前 3 秒決定生死。
> 一個 Short = 一個 core question + 3 個 beats + 一個 caveat + 一個 CTA。
>
> 含投資宣稱 → 走 Gate B（IA1）；純教育 → Gate A。
> 系統定義：[docs/ARTIFACT_SYSTEM.md](../../docs/ARTIFACT_SYSTEM.md)。

## Frontmatter

```yaml
workflow: content-production
artifact_type: youtube-shorts
risk: <low | medium | high>
artifact_ref: <相對路徑到 artifact-brief 或 thesis-card>
duration_sec: <30-60>
core_question: <一句話>
created_at: YYYY-MM-DD
public_status: <draft | ready | scheduled | published>
published_at:
post_url:
```

## Script

| 時間 | 畫面 | 旁白 / 字卡 |
|------|------|-------------|
| 0-3s | Hook 視覺 | 一句 hook（core question 或反直覺事實） |
| 3-10s | 鋪陳 | 為什麼這件事值得 30 秒 |
| 10-40s | 3 beats | beat 1 / beat 2 / beat 3，配圖 |
| 40-50s | Caveat | 一句不確定性 / 還沒驗證的部分 |
| 50-60s | CTA | follow / 看完整地圖 / 留言問題 + disclaimer |

### Hook（0-3s，逐字）

>

### 3 beats（逐字 + 對應畫面）

1.
2.
3.

### Caveat（1 句）

>

### CTA（1 句）

>

## On-screen / production notes

- 直式 9:16，字卡大、對比強。
- 每個 beat 一個畫面切換，維持節奏。
- 結尾畫面固定放 disclaimer 字卡。

## Review checklist（發布前）

- [ ] 前 3 秒 hook 成立
- [ ] 有 source（影片描述或字卡標註）
- [ ] 無買賣建議 / 無目標價（否則升 Gate B）
- [ ] 有不確定性 caveat
- [ ] 含投資宣稱 → 已過 IA1（Gate B）

## Disclaimer

This is research and education, not financial advice.
