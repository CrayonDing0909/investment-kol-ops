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
- Reason: Worksheet 內容已由使用者確認可接受，並同步到正式 brief。POV 與 invalidation 已具體填入，足以支撐 internal research use。此 approval 不等於 public publishing approval。M2.1 已補到 AMD share target、MediaTek AI ASIC target、CPU latency paper 的 primary / original sources，但 HBM / 散熱 / 被動元件支線與 scenario / data quality gates 仍未完成。

## Edit Notes

不適用（structure 沒有問題，等內容補完）。

## Reject Notes

不適用。

## Reflection (HUMAN-WRITTEN, mandatory for IA1)

> 規則：填完 brief 的 4 區塊後，回頭在這裡寫 reflection。Defer 階段先空著。

1. **Weakest point if challenged publicly (e.g. 股癌 粉絲質疑)**:
   AMD >50% server CPU revenue market share target 已找到 AMD Financial Analyst Day primary source；MediaTek 的 AI ASIC `$2B Q4 2026` 也已對到官方 transcript。現在比較弱的是 HBM / 散熱 / 被動元件還沒有 source-backed 深挖，且 scenario / data quality gates 尚未跑。另外，CPU demand 是 structural 還是短期補貨，目前也還需要更多 architecture / financial data 才能說死。

2. **Best skill / step in this run**:
   最有幫助的是 HTML Q&A 和 source reading view，因為它讓我把 CPU 重新重要這件事
從口號變成一個可理解的系統架構問題。BusinessNext 的文章讓我用中文理解
agentic AI 為什麼會增加 CPU orchestration demand；AMD / Intel source packets
則提供財報與管理層語言來支撐這個 mental model。

3. **What I most want to improve next time / 下一週最想補哪個 theme 的 deep dive**:
   下一個我想補 ASIC，因為 CPU 和 ASIC 是這條 AI server spend 外溢敘事的兩個主軸。
MediaTek / 世芯 / 創意都需要先理解 ASIC 才能判斷。MediaTek 的 $2B Q4 AI ASIC revenue 已有 official transcript 支撐，但公開前仍需寫成 management expectation，不是已實現營收。

## Linked Files

- Source checklist: [research/notes/2026-05-10_ai-server-supply-chain_cpu-revival_sources.md](../../research/notes/2026-05-10_ai-server-supply-chain_cpu-revival_sources.md)
- Knowledge pages updated:
  - [research/knowledge/ai-server-supply-chain/index.html](../../research/knowledge/ai-server-supply-chain/index.html)
  - [research/knowledge/ai-server-supply-chain/cpu.html](../../research/knowledge/ai-server-supply-chain/cpu.html)
- Subsequent action:
  1. 若要公開發布，補 HBM / 散熱 / 被動元件 source packets。
  2. 實際呼叫 scenario-analyzer，替代目前 agent-drafted scenarios。
  3. 將 AMD / MediaTek 已 source-hardened 的 claims 改成 forward-looking / expectation wording。
  4. 進入 M2.1 public-readiness hardening。

## Status After Gate

- New artifact status: **gate-approved (internal-only)** — 可作為 M1 CPU 復興 research baseline。
- Public status: **not-public-ready** — 若要公開，需要補 HBM / 散熱 / 被動元件 source packets，並完成 scenario-analyzer。Data-quality checker 已於 M2.1 跑過且 0 findings。
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
- HBM / 散熱 / 被動元件支線 source-backed 深挖。
- scenario-analyzer real invocation。
- AMD / MediaTek forward-looking wording 的 public edit。


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
3. If public publication is planned, HBM / cooling / passive component branches
   still need source-backed research and AMD / MediaTek claims need careful
   forward-looking wording.


## M1.2 POV Completion Note

Date: 2026-05-12

The worksheet at `research/worksheets/ai-server-supply-chain/2026-05-10_cpu-revival_pov-worksheet.md` was filled as an agent-seeded draft and accepted by the user for workflow continuity. Its contents were synced into the CPU brief.

Internal decision after M1.2: **approve (internal only)**.

Not public-ready because:

1. HBM / cooling / passive component branches still need source-backed research.
2. Scenario-analyzer has not been invoked as a real skill. Data-quality checker was run in M2.1 with 0 findings.
3. AMD / MediaTek claims must be framed as forward-looking target / management expectation in any public draft.

Recommended next theme: **ASIC**.
