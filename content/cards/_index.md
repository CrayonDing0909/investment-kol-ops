---
artifact_type: cards-index
created_at: 2026-05-13
last_updated: 2026-05-14T22:30+08:00
---

# Thesis Cards Index

> Purpose：追蹤所有 thesis card 的狀態、lens 分佈、平台、發布結果與 metrics。
>
> 一張 card = `content/cards/YYYY-MM-DD_<topic>_<lens>_<id>.md`。
>
> Card 規格定義見 `content/templates/thesis-card.md`。

## Cadence Target

- 2 張 card / 週（穩定節奏，不過 burnout）
- 1 個產業 backbone 4-5 週循環，每週期 6-10 張 card + 1 篇 newsletter

## Active Backbone

`content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md`
（AI Server Supply Chain v1，PR #13 在審）

## Cards Registry

| ID | Date | Topic | Lens | Platform | Status | Counter Dir | Notes |
|----|------|-------|------|----------|--------|-------------|-------|
| 001 | 2026-05-13 | ai-server / 散熱 BOM 流向 | 資金 | x+threads | ready | bull-kill | IA1 approved; ready to schedule / publish |
| 002 | 2026-05-13 | ai-server / MediaTek $2B 拆 expectation vs revenue | 基本面 | x+threads | outline | bear-falsify | 從 backbone MediaTek 4 risks 段萃出 |
| 003 | 2026-05-13 | ai-server / 為什麼 CPU 又被討論 | 為什麼 | x+threads | outline | bull-kill | 從 backbone CPU + Intel 段萃出 |
| 004 | 2026-05-13 | ai-server / Apple-Intel preliminary deal 怎麼讀 | 啟動 | x+threads | outline | bear-falsify | 從 backbone Manufacturing layer 段萃出 |
| 005 | 2026-05-13 | ai-server / 3 個會破 CPU 復興 thesis 的數字 | 破局 | x+threads | outline | bull-kill | 從 backbone "What Would Change My Mind" 段萃出 |
| 006 | 2026-05-13 | ai-server / 為什麼被動元件這條 evidence chain 偏窄 | meta | x+threads | outline | n/a | meta lens 通常不需要 Counter direction，因為談 method |

## Lens Distribution（Active Backbone）

```text
資金:    1 張 (#001)
基本面:  1 張 (#002)
為什麼:  1 張 (#003)
啟動:    1 張 (#004)
破局:    1 張 (#005)
meta:    1 張 (#006)
```

第一個產業有 6 張 card 平均覆蓋 6 個 lens——故意這樣設計，目的是測試哪個
lens 在中文投資圈互動最強，回饋下個 backbone 的 lens 配比。

## Status Definitions

- `outline`：題目 + lens + Counter direction 已決定，內容還沒寫。
- `draft`：6 個 section 都填了，還沒 self-review。
- `ready`：Review checklist 全跑完，可以排程。
- `scheduled`：已排到平台 scheduler，等發布。
- `published`：已發布，post_url 已填。
- `archived`：寫了但決定不發（記下原因）。

## Per-Card Workflow

每張 card 從 outline 推到 published 的流程：

```text
1. outline:    從 backbone 萃題目、決定 lens、決定 Counter direction
2. draft:      填 6 個 section，套 voice profile（hook 強、body 保留 raw）
3. self-review: 跑 thesis-card.md 的 Review Checklist
4. IA1 (if needed): 含投資宣稱 → 過 ops/decisions/ IA1 gate
5. ready:      改 frontmatter status: ready
6. scheduled:  排程到 X / Threads
7. published:  填 post_url，記 metrics 種子（24hr / 72hr）
8. metrics 7d: 7 天後填完整 metrics + qualitative signal
```

## Metrics Tracking

每張 published card 在發布後 7 天內，於對應 card file 末尾加：

```yaml
metrics:
  impressions_24h:
  impressions_72h:
  impressions_7d:
  likes_7d:
  reposts_7d:
  replies_7d:
  saves_7d:
  follows_attributed:
  link_clicks:
  qualitative:
    - <reply / DM 的具體 quote>
  reflection:
    repeat_pattern: <要在下張 card 重複的元素>
    drop_pattern: <要在下張 card 停掉的元素>
```

## Backbone Update Loop

當一張 card 在公開後得到新 evidence / counter-argument / source，**回頭更新
backbone**，不是只更新 card：

- card 是當時的快照，發出去就盡量不改（誠實的 paper trail）。
- backbone 是活的判斷地圖，會隨新證據更新。
- 兩個方向的 link 要保持：card frontmatter `backbone_ref` + backbone 在
  「Linked Cards」段加回來。

## Open Questions（這個 cycle）

- [ ] 6 張 card 哪一張先 ship？（建議 #001 資金 lens 或 #002 基本面 lens
      先打——有具體數字 + 對散戶常見誤解直接挑戰，theoretically 互動最高）
- [ ] X 跟 Threads 同步發 vs 錯時發？需要 1 週測試
- [ ] Backbone HTML library 部署到哪個 domain？（需要 user 決定，影響 CTA
      連結）
