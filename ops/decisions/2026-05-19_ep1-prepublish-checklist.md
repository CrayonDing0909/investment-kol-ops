---
artifact_type: prepublish-checklist
status: active
workflow: content-production
related_artifacts:
  - content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md
  - ops/decisions/2026-05-14_card-writing-voice-lessons.md
  - ops/decisions/2026-05-19_thesis-card-rule-drafts.md
created_at: 2026-05-19
reviewer: CrayonDing0909
promotion_gate: "ship Ep1 → review Ep1 → ship Ep2 → confirm same checklist holds → only then consider rule promotion"
---

# Ep1 Pre-Publish Checklist

> 目的：在 Ep1 公開前，跑這份手感清單。先不寫成 rule，先用 decision 紀錄。
> 等 Ep2 / Ep3 也照這份跑過、感覺穩，再決定要不要升 rule。

## Why a decision, not a rule

- Ep1 剛磨出來，Ep2 / Ep3 還沒跑。
- PR #20 已經帶 `.cursor/rules/series-narrative-architecture.mdc`，這份
  checklist 之後可能會被那條 rule 涵蓋或補強，先不重複。
- Rule 的成本是「凍結未驗證的流程」；decision 的成本是「下次自己要記得讀」。
  現階段選 decision。

## The Ep1 Pre-Publish Questions

每一條都用「我會自己讀過 1 次」的標準，不是「agent 跑 grep」。

1. **讀起來像你在整理資料嗎？**
   - 不是教學 / 解釋 / 投研報告口氣。
   - 第一句要有「我為什麼停下來看這件事」的內心理由。

2. **有沒有完整 mental model？**
   - 讀者讀完一遍後，自己能用一句話講出這條線的因果。
   - 不只是「散熱很重要」、「ASIC 在崛起」這種標籤。

3. **有沒有讓人想看下一集？**
   - Ep1 結尾要留一個下集勾子（不只是 CTA 連結）。
   - 例如：「下一集我會拆 ASIC 那條為什麼不是 GPU 外溢」、「下集講 CPU
     為什麼又被討論」。
   - 沒有勾子等於系列文不存在。

4. **有沒有不小心變成教學文？**
   - 出現大量「什麼是 X」、「X 用在哪裡」就要警覺。
   - 教學文歸 primer / source tutor，Ep 是 POV / 觀察 / 判斷。
   - 如果一定要解釋名詞，用一行帶過 + 連回 primer。

5. **有沒有公司名 / 投資暗示？**
   - 明確列出哪幾家被點名（奇鋐 / 雙鴻 / Vertiv / MediaTek / ...）。
   - 每個公司名旁邊都要有：訊號 + timeframe。
   - 不要出現「相關概念股」、「值得關注」這類 hand-wave。
   - 含投資暗示 → 過 IA1 gate（risk: high）。

6. **有沒有外部 link？**
   - 連回 backbone library page（複利資產）。
   - 連回 primer / tutor HTML（如果讀者想往下挖）。
   - X 對 link 不友善，連結放最後。
   - 沒有外部 link 等於把流量黑洞化。

## How to Use

發 Ep1 前自己讀一次 `## Draft Post`，逐條打勾。每一條沒過：

- 1 / 4 沒過 → 改 voice。
- 2 / 3 / 5 沒過 → 改結構或補內容。
- 6 沒過 → 加 link 段。

## After Ep1 Ships

24 小時內回頭看：

- 哪幾條 checklist 救了你？
- 哪幾條沒派上用場？
- 哪些新狀況是這份 checklist 沒涵蓋的？

把新觀察記到 Ep2 草稿前的一份新 decision（或補在這份檔案的「Lessons」
section）。Ep2 跑完同樣動作。Ep3 跑完，再評估是否升 rule。

## Linked

- [content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md](../../content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md)
- [ops/decisions/2026-05-14_card-writing-voice-lessons.md](2026-05-14_card-writing-voice-lessons.md)
- [ops/decisions/2026-05-19_thesis-card-rule-drafts.md](2026-05-19_thesis-card-rule-drafts.md)
- [ops/decisions/2026-05-13_workflow-rule-audit-card-001.md](2026-05-13_workflow-rule-audit-card-001.md)
