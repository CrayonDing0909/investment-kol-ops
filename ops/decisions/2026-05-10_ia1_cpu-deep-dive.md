---
artifact_type: gate-decision-log
gate_id: IA1
workflow: investment-analysis
artifact_ref: research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md
decision: approve
created_at: 2026-05-10
reviewer: CrayonDing0909
mode: dry-run
decision_scope: internal-only
public_status: not-public-ready
---

# Gate Decision: IA1 — CPU 復興 deep dive (dry run)

> M1 internal-only。Gate IA1 走 dry run 練流程。

## Artifact Under Review

- Path: [research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md](../../research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md)
- Type: analysis-brief
- Risk: high (含 AMD 市占 / Intel 相對地位 / 聯發科 priced 警告 → 屬於 market direction + position implication 等級)
- Status before gate: gate-pending

## Materials Shown to Reviewer

- Brief: [research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md](../../research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md)
- Source checklist: [research/notes/2026-05-10_ai-server-supply-chain_cpu-revival_sources.md](../../research/notes/2026-05-10_ai-server-supply-chain_cpu-revival_sources.md)
- Invalidation list: 已內建在 brief 的 "My Invalidation" 段（目前是 candidate 草稿，未由人類最終確認）
- Knowledge map: [research/knowledge/ai-server-supply-chain/index.html](../../research/knowledge/ai-server-supply-chain/index.html)
- Risk and Compliance pre-publish checklist: [ops/RISK_AND_COMPLIANCE.md](../RISK_AND_COMPLIANCE.md)

## Pre-Publish Checklist Sweep (agent side)

從 [ops/RISK_AND_COMPLIANCE.md](../RISK_AND_COMPLIANCE.md) 的 Pre-Publish Checklist 對 brief 作初檢：

- [x] Educational vs personalized advice：POV 已填入，明確標為 research / internal-only，不作個人化建議。
- [x] Time horizon：clearly stated as 6-18 months.
- [x] Risks and invalidation：3 條 invalidation 已填入，具體且可觀察。
- [x] Data sources identified：source checklist 完整列出，含 known / inferred / uncertain。
- [x] Positions disclosed：M1 不掛持倉，brief 已標 `position_conflicts: none`。
- [x] Defensible if market moves against tomorrow：scenarios bull / base / bear 已 draft（pending scenario-analyzer 驗證）。

整體：brief 結構完備、source 紀律到位，POV / invalidation 已填入，可通過 internal-only IA1。仍不代表 public publish approval。

## Decision

- Decision: **approve (internal only)**
- Reason: Worksheet 內容已由使用者確認可接受，並同步到正式 brief。POV 與 invalidation 已具體填入，足以支撐 internal research use。此 approval 不等於 public publishing approval，因為 AMD >50% server CPU share target 與 MediaTek AI ASIC $2B target 仍需要 primary-source verification。

## Edit Notes

不適用（structure 沒有問題，等內容補完）。

## Reject Notes

不適用。

## Reflection (HUMAN-WRITTEN, mandatory for IA1)

> 規則：填完 brief 的 4 區塊後，回頭在這裡寫 reflection。Defer 階段先空著。

1. **Weakest point if challenged publicly (e.g. 股癌 粉絲質疑)**:
   最弱的點是我目前對 AMD >50% server CPU share target 還沒有 primary source，
而且 MediaTek 的 AI ASIC 數字還是 secondary source。若公開發文，
這兩點會被懂產業的人挑戰。另外，CPU demand 是 structural 還是短期補貨，
目前也還需要更多 architecture / financial data 才能說死。

2. **Best skill / step in this run**:
   最有幫助的是 HTML Q&A 和 source reading view，因為它讓我把 CPU 重新重要這件事
從口號變成一個可理解的系統架構問題。BusinessNext 的文章讓我用中文理解
agentic AI 為什麼會增加 CPU orchestration demand；AMD / Intel source packets
則提供財報與管理層語言來支撐這個 mental model。

3. **What I most want to improve next time / 下一週最想補哪個 theme 的 deep dive**:
   下一個我想補 ASIC，因為 CPU 和 ASIC 是這條 AI server spend 外溢敘事的兩個主軸。
MediaTek / 世芯 / 創意都需要先理解 ASIC 才能判斷，而且現在 ASIC 的 source quality
還不夠好，尤其 MediaTek 的 $2B Q4 AI ASIC revenue 仍是 secondary source，
需要 official transcript 或更強的 primary source 來驗證。

## Linked Files

- Source checklist: [research/notes/2026-05-10_ai-server-supply-chain_cpu-revival_sources.md](../../research/notes/2026-05-10_ai-server-supply-chain_cpu-revival_sources.md)
- Knowledge pages updated:
  - [research/knowledge/ai-server-supply-chain/index.html](../../research/knowledge/ai-server-supply-chain/index.html)
  - [research/knowledge/ai-server-supply-chain/cpu.html](../../research/knowledge/ai-server-supply-chain/cpu.html)
- Subsequent action:
  1. 若要公開發布，補 AMD >50% server CPU share target 的 primary source。
  2. 若要公開發布，補 MediaTek official transcript / presentation，驗證 AI ASIC $2B Q4 2026 target。
  3. 實際呼叫 scenario-analyzer / data-quality-checker，替代目前 agent-drafted scenarios。
  4. 進入 M2 internal article draft 或 M1.3 primary-source hardening。

## Status After Gate

- New artifact status: **gate-approved (internal-only)** — 可作為 M1 CPU 復興 research baseline。
- Public status: **not-public-ready** — 若要公開，需要補 AMD share target primary source、MediaTek official transcript、scenario-analyzer / data-quality-checker。
- Next step owner: self + agent（進 M2 文章草稿 / 或 M1.3 補 primary sources）

## M1 Acceptance Note

本 M1 milestone 在「跑通流程」這層的 DoD 已達成：
- 6 stub 資料夾建好。
- 7 份 template / mapping doc 進 main。
- 6 份 intake notes 從 EP659 產出。
- 7 份 HTML knowledge pages 產出。
- 1 份 CPU anchor deep dive brief 結構完備，且 M1.2 已補入 agent-seeded / user-accepted POV。
- IA1 dry run 已從 `defer` 轉成 `approve (internal only)`。
- Source checklist 完成、Unsourced claims 明確列出。

仍未完成、且會影響 public publishing 的條目：
- AMD >50% server CPU share target primary source。
- MediaTek AI ASIC $2B Q4 2026 target primary source。
- scenario-analyzer / data-quality-checker real invocation。


## M1.1 Re-run Note (source-backed refresh)

Date: 2026-05-10

After M1.1 source collection, the brief is now backed by AMD, Intel, and
MediaTek source packets instead of relying mostly on 股癌 EP659. The decision
remains **defer** because the human-written sections are still incomplete, but
the source checklist quality improved:

- AMD source packet corrects the 120B ambiguity: it is server CPU TAM by 2030,
  not AMD 2026 revenue.
- Intel source packet supports the "CPU as AI orchestration/control plane"
  framing.
- MediaTek source packet clarifies that its current source-backed story is AI
  ASIC + I/O / memory subsystem optionality, not server CPU main silicon.

Decision after M1.1 refresh: **defer**.

Remaining blockers before IA1 can approve:

1. User fills What I Learned / What I Still Don't Understand / My POV / My
   Invalidation in the CPU brief.
2. User fills the three reflection answers in this decision log.
3. If public publication is planned, primary verification is still needed for
   AMD >50% server CPU share target and MediaTek $2B Q4 AI ASIC revenue target.


## M1.2 POV Completion Note

Date: 2026-05-12

The worksheet at `research/worksheets/ai-server-supply-chain/2026-05-10_cpu-revival_pov-worksheet.md` was filled as an agent-seeded draft and accepted by the user for workflow continuity. Its contents were synced into the CPU brief.

Internal decision after M1.2: **approve (internal only)**.

Not public-ready because:

1. AMD >50% server CPU share target still needs a primary source.
2. MediaTek AI ASIC $2B Q4 2026 target still relies on secondary summaries.
3. Scenario-analyzer / data-quality-checker have not been invoked as real skills.

Recommended next theme: **ASIC**.
