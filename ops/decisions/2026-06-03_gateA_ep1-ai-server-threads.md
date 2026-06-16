---
artifact_type: gate-decision-log
gate_id: A
workflow: content-production
artifact_ref: content/series/ai-server-overview/ep1-threads-draft.md
target_version: EP1 Threads v3.1
approval_type: Gate A approval for Threads draft only (NOT publish, NOT public derivatives)
decision: approve
created_at: 2026-06-03
reviewer: CrayonDing0909
mode: live
decision_scope: threads-draft-only
public_status: gate-approved
---

# Gate Decision: Gate A — EP1 Threads draft (AI Server Overview)

> Gate A = **Safety Check + Owner Comprehension Check**
> （[docs/HUMAN_GATES.md](../../docs/HUMAN_GATES.md)）。**安全不等於可發布。**
> 本檔狀態：**APPROVED（2026-06-03，live human gate）**，目標版本 **EP1 Threads v3.1**。
> 核准範圍**僅限 Threads draft 通過 Gate A（safety + comprehension）**；**不**授權發布、
> 不授權產生 HTML / IG / Shorts / 任何公開衍生。
>
> 審查對象**僅** EP1 Threads draft。舊的 `ep1-one-map.html` 不在此範圍，僅作內部
> appendix / 失敗參考（見 [ops/postmortems/2026-06-01_a1-001-ep1-one-map_postmortem.md](../postmortems/2026-06-01_a1-001-ep1-one-map_postmortem.md)）。

## Artifact Under Review

- Path: [content/series/ai-server-overview/ep1-threads-draft.md](../../content/series/ai-server-overview/ep1-threads-draft.md)
- Type: threads-draft（series: ai-server-overview, episode 1, phase: explainer）
- **Target version: EP1 Threads v3.1**（版本 B 基底 + 回補 GPU gloss 與 Reply 3 具體熱畫面）
- Risk: **low** — 純教育 explainer，無個股方向 / 持倉 / 目標價。
- Status before gate: draft / gate-pending
- Episode Contract（已核准）: [content/series/ai-server-overview/ep1-episode-contract.md](../../content/series/ai-server-overview/ep1-episode-contract.md)（`owner_approved: true`）
- Series Bible: [content/series/ai-server-overview/series-bible.md](../../content/series/ai-server-overview/series-bible.md)

## Check 1 — Safety Check（通過）

- [x] **無買賣 call** —— 全文無「買 / 賣 / 加減碼」；明寫「先不講買賣」。
- [x] **無目標價** —— 無任何價格 / 估值結論。「買進 / 賣出 / 目標價」字串均不在 post bodies。
- [x] **無個人化投資建議** —— 無「你應該…」式建議。
- [x] **無公司推薦 / 無 ticker pick** —— 全 thread 無任何公司名稱。
- [x] **post bodies 無 news / company / spec 術語** —— NVIDIA / Rubin / Computex / Taipei /
      $600K / 600K / 132kW / HBM / CoWoS / ODM / ABF / MLCC / CDU / UQD / cold plate 均**不在
      實際貼文內**（僅出現在本檔與 draft 的 frontmatter / 註記）。
- [x] **Disclaimer present** —— 第 7 則：「非投資建議。」

### `受惠股` 語意安全例外（已解決先前 scan 爭議）

先前的逐字 scan list 把「受惠股」列為禁字，但 v3.1 post bodies 中「受惠股 / 受惠」
**每一次出現都是 negation / anti-recommendation framing**：

- Main post：「也不講**受惠股**」
- 5/：「誰是**受惠股**？」（緊接「我會先問…解決什麼限制」）
- 1/：「誰**受惠**」（描述「市場常見的講法」，隨即反對之）

這些是**明確宣告「本篇不做受惠股 / winner-pick 內容」**，不是個股推薦、不是 ticker
pick、不是方向建議、不是受惠股清單。owner 判定：以**語意安全例外**處理，保留原字，
不 scrub。Gate A 的禁制意圖（不得有受惠股**推薦**）已滿足。

## Check 2 — Owner Comprehension Check（owner 確認：通過）

| # | 問題 | 結果 | Owner 確認 |
|---|------|-----------|-----------|
| 1 | 5 秒內知道這篇要教什麼？ | 通過（main post 即點出「不是很多張 GPU，是一台很貴、很熱、很難組的機器」） | [x] |
| 2 | 能用一句話複述 takeaway？ | 通過（第 7 則明寫該句） | [x] |
| 3 | main post 只用允許 anchor terms（AI server / GPU）？ | 通過（GPU 自帶白話註「（運算卡）」，無其他術語） | [x] |
| 4 | 是作品而非資料堆疊？ | 通過（敘事弧，無規格清單） | [x] |
| 5 | Reply 3 是否提供具體錨點 / 小驚訝？ | 通過（已回補具體物理畫面：「它比較像要不停把一整台機器的熱抽出去，不是桌上吹一顆風扇就能解決。」） | [x] |

### Timely framing safety

- 「新一代平台很熱」維持**泛稱**，post bodies **不解釋**任何 company / platform / news。
- EP1 主軸仍是核心 reframe：**AI server 不是很多張 GPU，是一台很貴、很熱、很難組的機器。**

## Escalation Check（是否需升 Gate B / IA1）

- [x] 無 market direction / regime call
- [x] 無 position implication（無公司名、無受惠排序）
- [x] 無 winner / loser、無受惠股
- [x] 無 backtest / strategy result

→ 維持 **Gate A**，不需升 IA1。

## Decision

- **Decision**: **approve**（Gate A，live human gate，2026-06-03）
- **Approval type**: **Gate A approval for the Threads draft only**（safety + owner comprehension）。
- **Reason (one sentence)**: EP1 Threads v3.1 通過 Safety Check 與 Owner Comprehension
  Check，post bodies 無 news/company/spec 術語、無買賣/目標價，`受惠股` 僅以
  anti-recommendation framing 出現（語意安全例外），故 owner 核准此 Threads draft 通過
  Gate A——但**不**授權發布或任何公開衍生。

## Approval Scope & Explicit Non-Authorization

**已授權**：EP1 Threads v3.1 此一 **Threads draft** 通過 Gate A（safety + comprehension）。

**未授權（明確不做）**：

- 不發布（no publish）
- 不產生 HTML
- 不產生 IG carousel
- 不產生 Shorts
- 不產生任何 public derivative
- 不更動舊的 `ep1-one-map.html`
- 不 push（除非另行明確指示）
- 不 commit 無關 / orphan 檔案

任何上述動作需 owner 另行授權；發布若帶方向 / 持倉 / 受惠判斷則需改走 Gate B。

## Edit Notes

（owner review 後若需修改，記在此並指出回到哪個 stage：Threads prose / Episode Contract / Series Bible。）

## Reject / Rebuild Notes

若 owner 表示「我沒學到東西」或任一 Comprehension 項為否 → 不 approve，退回 **rebuild**
（重開 Episode Contract，而非輕量潤稿），依 [docs/CONTENT_CONVERSION_PIPELINE.md](../../docs/CONTENT_CONVERSION_PIPELINE.md)。

## Linked Files

- Threads draft（審查對象）: [content/series/ai-server-overview/ep1-threads-draft.md](../../content/series/ai-server-overview/ep1-threads-draft.md)
- Episode Contract（已核准）: [content/series/ai-server-overview/ep1-episode-contract.md](../../content/series/ai-server-overview/ep1-episode-contract.md)
- Series Bible: [content/series/ai-server-overview/series-bible.md](../../content/series/ai-server-overview/series-bible.md)
- Pipeline: [docs/CONTENT_CONVERSION_PIPELINE.md](../../docs/CONTENT_CONVERSION_PIPELINE.md)
- Gate 定義: [docs/HUMAN_GATES.md](../../docs/HUMAN_GATES.md)

## Status After Gate

- New artifact status: **gate-approved（Threads draft v3.1）**
- Public status: **gate-approved，但尚未授權發布**（approval ≠ publish）
- Next step owner: **owner** 決定是否（之後）授權發布 / 產生公開衍生 / 進 EP2；agent 在
  取得明確授權前不發布、不產生衍生、不 push。
