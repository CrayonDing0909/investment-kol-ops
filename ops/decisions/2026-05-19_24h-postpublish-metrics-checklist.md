---
artifact_type: postpublish-checklist
status: active
workflow: content-production
related_artifacts:
  - ops/decisions/2026-05-19_ep1-prepublish-checklist.md
  - ops/decisions/2026-05-13_workflow-rule-audit-card-001.md
  - content/cards/2026-05-15_thermal-series_ep1-electricity.md
created_at: 2026-05-19
reviewer: CrayonDing0909
applies_to: "content/cards/**/*.md (any card flipped to public_status: published)"
promotion_gate: "use as decision template for Ep1 → Ep2 → Ep3; only consider promoting to a Cursor rule after 3+ cards have completed the cycle"
---

# 24h Post-Publish Metrics Checklist

> Purpose：每張 card 發出去後，固定時點抓 metrics + 質性訊號，避免事後憑
> 印象 review。先寫成 decision template，等 Ep1 → Ep2 → Ep3 都跑過、欄位
> 確認穩定，再考慮升 rule。
>
> 這份是 reusable template — 用法是每張新 card 發出後，建立一份新檔案：
> `ops/decisions/<YYYY-MM-DD>_<card-id>_postpublish-log.md`，從本檔複製
> 對應 sections，填入實際數字。

## Why a Decision, Not a Rule

- 24h 結構雖然合理，但 hook archetype / Tesla 比喻 / 8-post threads 拆法
  都還沒 cross-card 驗證。同樣的 metrics 指標未來可能需要調整。
- Rule = 凍結；decision = 紀錄 + 學習。Phase 1 系列文（Ep1-Ep3）跑完後再
  決定哪些欄位夠穩到升 rule。

## Recording Cadence

每張 published card 都建一份 log，按以下時間點 capture：

| 時點 | 主要目的 |
|---|---|
| T+1h | 確認貼文沒有立即出問題（typo、404、被 shadow） |
| T+6h | 早期 reach / engagement signal；演算法決定要不要繼續推的窗口 |
| T+24h | 第一次正式 metrics snapshot；決定要不要 pin / 補回覆 |
| T+72h | 中段擴散；通常此時 reply 質量比量重要 |
| T+7d | 收斂 metrics 與 reflection 三題 |

## Per-Snapshot Fields

### T+1h — health check（5 分鐘）

- [ ] 貼文是否還在（沒被自己誤刪 / 平台下架）
- [ ] 第一行 hook 顯示正常（沒有 emoji / 換行錯位）
- [ ] X long post / Threads thread 順序顯示正確
- [ ] Bio / pinned 沒有意外顯示連結（早期帳號 phase）
- [ ] 早期 reply / DM 是否需要立即回覆

```yaml
t_plus_1h:
  status: ok | needs-fix
  notes: ""
```

### T+6h — early traction snapshot

```yaml
t_plus_6h:
  x:
    impressions:
    likes:
    replies:
    reposts:
    quotes:
    bookmarks:
    profile_clicks:
    new_followers:
  threads:
    views:
    likes:
    replies:
    reposts:
    quotes:
    bookmarks:
    profile_clicks:
    new_followers:
  notes: |
    - 哪一則 (n/8) 互動最高？
    - 有沒有 reply 直接挑戰假設？
```

T+6h 行動 checklist：

- [ ] 6 小時內回覆所有認真留言（演算法看 author engagement）
- [ ] 不要 pin（24h 才決定是否 pin）
- [ ] 不要在第一則回覆放外部 link（早期 phase 維持 link-free）
- [ ] 如果某 (n/8) 互動異常高，記下來下集 hook 沿用該結構

### T+24h — first formal metrics snapshot

```yaml
t_plus_24h:
  x:
    impressions:
    likes:
    replies:
    reposts:
    quotes:
    bookmarks:
    profile_clicks:
    new_followers:
    link_clicks: 0   # early phase 應該為 0
  threads:
    views_per_post:
      "(1/8)":
      "(2/8)":
      "(3/8)":
      "(4/8)":
      "(5/8)":
      "(6/8)":
      "(7/8)":
      "(8/8)":
    total_likes:
    total_replies:
    total_reposts:
    total_bookmarks:
    profile_clicks:
    new_followers:
  attribution:
    follows_attributed_to_this_post:
    notable_reply_handles: []
```

T+24h 質性問題（每題 1-2 句回答，沒答案就寫「沒觀察到」）：

1. 留言是來自目標 niche 嗎？（工程師 / Tesla 車主 / AI infra 人 vs 純路人）
2. 有沒有人問「下一集什麼時候出」或同義表達？
3. Hook（記憶比喻）是否被 reply 主動引用？
4. 有沒有 reply 提供新 source / 角度，可加入 Ep2 / backbone？
5. 哪一段被 quote / repost 最多？（X：哪一句被 quote tweet；Threads：哪一則 (n/8) 被引用）
6. 有沒有 reply 暴露我預設讀者懂、其實不懂的概念？
7. 有沒有 reply 是 toxic 或 derail？是否需要靜音 / 刪除？

T+24h 行動 checklist：

- [ ] 是否 pin？標準：T+24h impressions ≥ 帳號平均 × 3 或留言質量明顯高於平均，才 pin
- [ ] 是否要在第一則回覆補一個自我延伸（例如 quoted source）— 仍不放外部 link
- [ ] 是否需要更新 Ep2 hook / 結構（依 Q3 / Q4 / Q6 答案）
- [ ] 有沒有 reply 值得抓回 backbone document 或 source 清單

### T+72h — mid-cycle check（optional, 5 分鐘）

```yaml
t_plus_72h:
  x:
    impressions:
    new_followers_since_24h:
  threads:
    views:
    new_followers_since_24h:
  notes: |
    - 是否還在被推（有 24h-72h 之間明顯成長 → 演算法 second wave）？
    - 有沒有新 reply 改變 24h 的判斷？
```

### T+7d — recap + reflection

```yaml
t_plus_7d:
  x:
    impressions_final:
    likes_final:
    reposts_final:
    bookmarks_final:
    new_followers_final:
  threads:
    views_final:
    likes_final:
    reposts_final:
    bookmarks_final:
    new_followers_final:
  qualitative:
    best_reply_quote: ""
    best_repost_handle: ""
    surprise_signal: ""
  reflection:
    repeat_pattern: ""    # 下張 card 要重複的元素
    drop_pattern: ""      # 下張 card 要停掉的元素
    new_question_for_ep_next: ""
```

## Pin Decision Rule

T+24h pin / not pin 標準：

```text
PIN if:
- impressions ≥ 帳號平均 × 3, OR
- replies / impressions ratio ≥ 帳號平均 × 2, OR
- 出現 ≥ 3 條來自目標 niche 的高品質 reply

DON'T PIN if:
- impressions < 帳號平均
- replies 大多來自不相關 audience
- 任何 PASS 失誤被讀者抓到（typo / 數字錯）
```

Pin 後等 Ep2 / Ep3 ship 再 unpin（或 re-pin 新 episode）。

## Decision File Naming

每張 published card 對應一份 log：

```text
ops/decisions/<YYYY-MM-DD-of-publish>_<card-id>_postpublish-log.md
```

範例：

```text
ops/decisions/2026-05-21_thermal-ep1-electricity_postpublish-log.md
ops/decisions/2026-05-28_thermal-ep2-bom_postpublish-log.md
```

Frontmatter 範例：

```yaml
---
artifact_type: postpublish-log
related_artifact: content/cards/2026-05-15_thermal-series_ep1-electricity.md
related_template: ops/decisions/2026-05-19_24h-postpublish-metrics-checklist.md
publish_date: 2026-05-21T20:00+08:00
platforms: [x, threads]
phase: explainer
---
```

## After Ep1 → Ep2 → Ep3

跑完 3 集後 review：

- 哪些 metrics 欄位每次都有用？→ 候選升 rule
- 哪些 metrics 欄位從沒填過 / 沒幫到判斷？→ 從 template 拿掉
- Pin Decision Rule 的閾值有沒有需要調？
- 24h vs 72h vs 7d 哪個時點最常觸發決策？

把 review 結果寫成新 decision；穩定後才考慮：

- `.cursor/rules/postpublish-metrics.mdc`（rule 形式）
- 或者把欄位寫進 `content/templates/thesis-card.md` 的 metrics block

## Linked

- [ops/decisions/2026-05-19_ep1-prepublish-checklist.md](2026-05-19_ep1-prepublish-checklist.md)
- [ops/decisions/2026-05-19_thesis-card-rule-drafts.md](2026-05-19_thesis-card-rule-drafts.md)
- [.cursor/rules/series-narrative-architecture.mdc](../../.cursor/rules/series-narrative-architecture.mdc)
- Ep1 card：[content/cards/2026-05-15_thermal-series_ep1-electricity.md](../../content/cards/2026-05-15_thermal-series_ep1-electricity.md)
