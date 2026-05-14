---
artifact_type: gate-decision-log
gate_id: IA1
workflow: content-production
artifact_ref: content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md
decision: approve
created_at: 2026-05-13
last_updated: 2026-05-14T22:30+08:00
reviewer: CrayonDing0909
mode: live
decision_scope: public-publish
public_status: gate-approved
---

# Gate Decision: IA1 — Card #001 Cooling BOM (public publish)

> 第一張要對外 ship 的 thesis card；含「奇鋐 / 雙鴻 / Vertiv 受惠」這類
> position implication，per `docs/HUMAN_GATES.md` Gate IA1 必走 live human
> review，不能 dry-run。

## Process Note (2026-05-13 update)

> 原本 IA1 draft 直接要求 user 回答兩個 reviewer 問題；發現 user 還沒讀過
> 對應 source。為了符合 `AGENTS.md` 的「Quality and learning over speed」
> 與 `.cursor/rules/source-tutor-reading.mdc`「HTML reading view is mandatory」
> 規則，這個 IA1 改成兩段流程：
>
> 1. User 先讀 [cooling-bom HTML reading](../../research/knowledge/ai-server-supply-chain/readings/cooling-bom.html)
>    內化 source confidence 與 BOM denominator 衝突。
> 2. User 用 [Card #001 HTML 審稿頁](../../content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html)
>    審草稿並回答兩個 reviewer 問題。
> 3. Agent 應用變更 → 在本檔加 second-pass 區段、把 decision 改成
>    `approve` / `edit`。
> 4. User 回填 Reflection 三題。
>
> 在 user 完成 step 1 + 2 之前，這份 IA1 仍維持 `defer`，且不算錯誤或
> 阻塞——這是正常的人工 gate 排隊。

## Artifact Under Review

- Path: [content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md](../../content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md)
- Type: content-draft (thesis-card)
- Risk: **high** — 含具體公司 position implication（奇鋐 cold plate、雙鴻
  manifold、Vertiv CDU），且配 forward-looking BOM 數字。
- Status before gate: gate-pending
- Public URL on ship: X long post + Threads carousel；CTA →
  <https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/>

## Materials Shown to Reviewer

按 HTML-first 順序（**user 應先讀前兩項 HTML**）：

1. [Cooling BOM Cross-Source Reading（HTML 學習頁，前置必讀）](../../research/knowledge/ai-server-supply-chain/readings/cooling-bom.html)
2. [Card #001 HTML 審稿頁（reviewer 主要操作介面）](../../content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html)
3. [Card markdown — 完整 frontmatter / draft post / checklist（fallback canonical）](../../content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md)
4. [Source tutor reading markdown（fallback canonical）](../../research/source-tutor/ai-server-supply-chain/2026-05-13_cooling-bom-reading.md)
5. [Source packet — cooling source packet markdown](../../research/sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md)
6. [Backbone article 散熱段（HTML）](https://investment-kol-ops.vercel.app/content/drafts/2026-05-12_ai-server-supply-chain_internal-article/) · [markdown canonical](../../content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md)
7. [Public library landing](https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/)
8. [Pre-publish checklist — ops/RISK_AND_COMPLIANCE.md](../RISK_AND_COMPLIANCE.md)

## Pre-Publish Checklist Sweep (agent side)

按 [ops/RISK_AND_COMPLIANCE.md](../RISK_AND_COMPLIANCE.md) 的 Pre-Publish
Checklist 對 card 作初檢：

- [x] **Educational vs personalized advice**：card 結尾「本內容是研究與
      教育，不是投資建議」disclaimer 已具備；Implication 段使用「受惠 /
      observation signals」用語，非「買 / 賣」。
- [x] **Time horizon**：「3-5 年結構性，不是 1-2 季題材」明確標明（位於
      Implication 段尾）。
- [x] **Risks and invalidation**：Counter 段保留一條 plain-language
      反向檢查：若 2026-2027 仍以過渡型液冷為主，cold plate / manifold /
      CDU 等純液冷零件增速可能比市場想像慢。這是 agent-inference，不是
      source quote。
- [x] **Data sources identified**：3 條 secondary 來源（LianLi / EE Times
      China / Taipei Times-TrendForce）均在 frontmatter `sources:` 列出，
      正文 Observation 段同樣標明來源與「secondary / industry estimate」。
- [x] **Positions disclosed**：Card 提及奇鋐 / 雙鴻 / Vertiv，已加泛用
      disclosure：`持倉揭露：作者可能持有文中提及個股，內容僅作研究紀錄，
      不構成投資建議。`
- [x] **Defensible if market moves against tomorrow**：Counter 段提前
      宣告 invalidation 條件；公開正文不寫「占整櫃 42%」，分母衝突保留在
      source tutor / review 表，而不是塞進貼文。

### Additional findings (high-risk content review)

按 [ops/RISK_AND_COMPLIANCE.md](../RISK_AND_COMPLIANCE.md) High-Risk
Content list 比對：

- 無 buy/sell 字眼
- 無 leveraged products / options / crypto
- 3 家公司均為中型以上 large-cap，非 small-cap 流動性問題
- 無 backtest 結果
- 無 screenshot 私密資料
- 無 AI tool 表現宣稱

### Source quality classification

| Claim | Source class | Class label |
|---|---|---|
| GB300 NVL72 散熱 BOM ~$49,860 | LianLi quoting Morgan Stanley + EE Times China | secondary（aggregated, not primary） |
| cold plate 40-45% / CDU 30-35% / UQD 15-20% / manifold 5-10% | EE Times China | secondary |
| GB300 占 2026 AI server rack shipments 70-80% | Taipei Times 引 TrendForce | secondary-quoted-from-primary |
| 132-140kW rack power、1400W per GPU | LianLi Work | secondary（但 NVIDIA 公開 spec 一致） |
| 奇鋐冷板 30%+ 市占 | Vocus 產業研究 + LianLi 引述 | secondary（口徑未驗證） |
| Vertiv 液冷 ecosystem 35%+ 價值份額 | EE Times China | secondary |

全部 claim 均為 secondary。對 X long post 與 Threads 用，acceptable。
BOM 分母衝突不再塞入正文，改留在 source tutor / review surface；公開稿只用
`~$50K / rack` 保守量級。

## Decision

- **Decision**: **approve**
- **Reason (one sentence)**: User completed source learning, HTML review,
  position-disclosure decision, safe BOM framing, voice edits, and mandatory
  IA1 reflection; the card is approved for public scheduling with its current
  caveats and disclosure.

### First reviewer response (2026-05-14)

- **Q1 持倉揭露**：User selected **D** — 有持倉但不想揭露具體細節。
- **Q2 BOM 分母**：User selected **A** — 維持保守版，只寫 `~$49,860 / rack`，不講百分比。
- **Voice feedback**：User said draft does not sound like them; asked to revise
  tone / logic / key points.

Agent response:

1. Public draft was revised toward raw research voice (`最近整理...`, `我目前會看的不是股價...`) and away from media-explainer voice.
2. Initial response to Q1 = D removed named companies, but user corrected that named companies are useful and acceptable even with position exposure. Public draft now restores named companies (`奇鋐 / 雙鴻 / Vertiv`) and adds generic position disclosure: `作者可能持有文中提及個股，內容僅作研究紀錄，不構成投資建議。`
3. Because Q2 = A, draft keeps `~$49,860 / rack` safe wording and removes the
   `42%` discussion from the public body; that conflict stays in learning /
   review surfaces.

Status remains **defer**, not approve, until user reviews the revised HTML review page and confirms the voice is acceptable.

### Second-pass review (2026-05-14)

User reviewed the revised public draft and confirmed the voice is acceptable enough to proceed to IA1 second pass.

Agent second-pass finding:

- **Content structure**: pass. The draft has a clear memory point (`GB300 一櫃要花接近 $50K 在液冷上`), context for non-technical readers, supply-chain mapping, verification signals, and a closing synthesis.
- **Voice**: pass after edits. Removed AI-like phrasing (`不再只是...而是...`, `這不是 primary source...`, `為什麼 X...？`) and restored parenthetical inner voice (`算一種利多出盡吧`).
- **Source confidence**: pass with caveat. Public draft uses `~$50K / rack` only; `42%` stays out of the public body and remains documented in source tutor / review surfaces.
- **Position disclosure**: pass for current wording. Named companies are included with generic disclosure: `作者可能持有文中提及個股，內容僅作研究紀錄，不構成投資建議。`
- **Risk / invalidation**: pass. Draft includes a plain-language counter: if adoption stays in transitional liquid cooling and direct-to-chip / full-liquid adoption does not accelerate, component growth may be slower than expected.

**Second-pass recommendation**: content can move to `gate-approved (public)`.

**Reviewer completion (2026-05-14)**: User supplied the mandatory IA1 reflection
answers. Decision frontmatter updated from `defer` to `approve`; card may move
to `ready`.

### What this `defer` unblocks

1. User 讀 [cooling-bom HTML reading](../../research/knowledge/ai-server-supply-chain/readings/cooling-bom.html) 內化 source confidence。
2. User 進 [Card #001 HTML 審稿頁](../../content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html) 回答兩個 reviewer 問題。
3. Agent 應用變更 → 在本檔加 second-pass 區段、把 decision 改成
   `approve` 或 `edit`。
4. 通過後 status → `gate-approved (public)`，card frontmatter
   `public_status: ready`，可進入 scheduled / published 流程。

### Reviewer Questions（user 在 [HTML 審稿頁](../../content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html) 上回答；本檔同步保留問題）

1. **持倉揭露**：你目前是否持有 奇鋐（3017.TW）、雙鴻（3324.TW）、
   Vertiv（VRT）任一張？或近 30 天內有交易？
   - 如全部「無」→ card 加一行 `position disclosure: 作者目前未持有
     奇鋐、雙鴻、Vertiv，且 30 天內無交易。`
   - 如有任一張持倉 / 近期交易 → 明確揭露持倉方向（多 / 空）與大致時點。

2. **BOM 分母**：要 ship 時走哪一版？
   - (a) 維持 `~$49,860 / rack` 不講百分比（最安全，已是目前 draft 寫法）
   - (b) 補上 caveat：「公開拆解對分母不一致，LianLi 一處寫 / $600K、
     EE Times China 另一處出現 $380K / 42%；我用較低 / 較保守口徑」
   - (c) Ship 前再花一次 primary 升級（Morgan Stanley note / Vertiv
     investor day），可能仍找不到，但延後 3-7 天

Agent 建議：在你讀完 cooling-bom HTML 後選 (a)。理由：這份 set 不會升到
primary，延後也不會有更硬的數字；BOM 衝突留在 source tutor / review 表，
公開稿只保留安全量級。

**Current applied answer**: Q1 = D revised（具名公司保留 + 泛用持倉揭露）；Q2 = A（保守版）。

## Edit Notes

- Added generic position disclosure while keeping named companies in the public
  draft.
- Kept Q2=A safe BOM wording (`~$50K / rack`), removed `42%` from the public
  body, and kept the conflict in the source tutor / review surfaces.
- Rewrote the draft toward the user's raw research voice and removed AI-like
  phrasing.

## Reject Notes

不適用。

## Reflection (HUMAN-WRITTEN, mandatory for IA1)

> 規則：第一次 review 完後回頭填這 3 題。Defer 階段可先空著，但 second
> pass approve 前必須填完。

1. **Weakest point if challenged publicly (e.g. 散戶 / 同行質疑)**：
   最弱的是散熱 BOM 還是二手資料，沒有 Morgan Stanley 原文。

2. **Best skill / step in this run**:
   最有幫助的是先補 domain primer，終於知道 GB300 rack / BOM / 液冷在講什麼。

3. **What I most want to improve next time / 下一張 card 想做得更好的點**:
   下一張我希望一開始就先有學習頁，不要直接進稿子。

## Linked Files

- HTML learning page (reviewer 必讀)：[research/knowledge/ai-server-supply-chain/readings/cooling-bom.html](../../research/knowledge/ai-server-supply-chain/readings/cooling-bom.html)
- HTML review page (reviewer 主介面)：[content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html](../../content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html)
- Source tutor markdown：[research/source-tutor/ai-server-supply-chain/2026-05-13_cooling-bom-reading.md](../../research/source-tutor/ai-server-supply-chain/2026-05-13_cooling-bom-reading.md)
- Source packet：[research/sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md](../../research/sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md)
- Card markdown：[content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md](../../content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md)
- Backbone article (md)：[content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md](../../content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md)
- Backbone article (HTML, public)：<https://investment-kol-ops.vercel.app/content/drafts/2026-05-12_ai-server-supply-chain_internal-article/>
- Library landing：<https://investment-kol-ops.vercel.app/library/ai-server-supply-chain/>
- Subsequent action:
  1. User 讀完 cooling-bom HTML reading。
  2. User 在 Card #001 HTML 審稿頁回答兩題。
  3. Agent edit card 加 disclosure / voice edits。
  4. Re-run IA1，update this decision file with second-pass note。
  5. User 回填 Reflection 三題。
  6. 通過後 card frontmatter `public_status: ready`，準備 scheduled。

## Status After Gate

- New artifact status: **gate-approved (public)**.
- Public status: **ready to schedule / publish**.
- Next step owner: **user**（schedule / publish manually; agent can prepare
  platform copy if requested）.
