---
workflow: investment-analysis
artifact_type: source-checklist
risk: low
created_at: 2026-05-10
brief_ref: research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md
status: draft
---

# Source Checklist: CPU 復興 deep dive

> 規則：每個 claim 一行；confidence ≠ known 都要在 brief 標出來。

## Claims

| # | Claim | Source | Captured At | Confidence | Verified By |
|---|-------|--------|-------------|------------|-------------|
| 1 | AMD server CPU TAM expected to exceed $120B by 2030, CAGR &gt;35% | research/sources/ai-server-supply-chain/earnings/2026-05-10_amd-q1-2026-source-packet.md | 2026-05-12 | known via earnings transcript; corrected from EP659 interpretation | Motley Fool transcript; AMD official transcript preferred |
| 2 | AMD 目標伺服器 CPU revenue market share &gt; 50% | research/sources/ai-server-supply-chain/earnings/2026-05-10_amd-q1-2026-source-packet.md | 2026-05-12 | known as forward-looking target | AMD Financial Analyst Day 2025 press release |
| 3 | AMD 2027 年 AI 營收能見度高 | research/intake/2026-05-10_gooeye-ep659_cpu.md | 2026-05-10 | known (per EP659) | self |
| 4 | Intel 法說呼應 CPU 成為市場核心 | research/intake/2026-05-10_gooeye-ep659_cpu.md | 2026-05-10 | known (per EP659; secondary) | self |
| 5 | 美股崩爛時 CPU 族群相對強勢 | research/intake/2026-05-10_gooeye-ep659_cpu.md | 2026-05-10 | known (per EP659 觀察) | self |
| 6 | 聯發科出現多根漲停、股價到 ~3000 TWD | research/intake/2026-05-10_gooeye-ep659_cpu.md | 2026-05-10 | known (per EP659) | self |
| 7 | 聯發科目前做 I/O、memory，未打入主晶片 | research/intake/2026-05-10_gooeye-ep659_cpu.md | 2026-05-10 | known (per EP659) | self |
| 8 | 「資金從 GPU 大轉向」是市場主敘事 | research/intake/2026-05-10_gooeye-ep659_cpu.md | 2026-05-10 | known narrative (per EP659) | self |
| 9 | 每台 AI server 仍配 1-2 顆 CPU | research/knowledge/ai-server-supply-chain/cpu.html (industry consensus) | 2026-05-10 | inferred | self |
| 10 | ARM / NVDA Grace / AWS Graviton 為非 x86 替代路徑 | research/knowledge/ai-server-supply-chain/cpu.html | 2026-05-10 | inferred | self |
| 11 | 「CPU 復興」 theme 目前處於哪個 lifecycle 階段 | (none) | — | uncertain | skill missing: theme-detector |
| 12 | 近 10 天 CPU 相關新聞影響排序 | (none) | — | uncertain | skill missing: market-news-analyst |
| 13 | AMD / 聯發科週圖技術結構 | (none) | — | uncertain | skill missing: technical-analyst |
| 14 | 6-18 個月 bull/base/bear scenarios | brief 中 Scenarios 段（agent draft） | 2026-05-10 | uncertain | skill missing: scenario-analyzer (currently agent-drafted only) |
| 15 | 整份 brief 的單位 / 日期 / instrument 一致性檢查 | (none) | — | uncertain | skill missing: data-quality-checker (manual sweep done by agent, not gated) |

## Numbers Used

| # | Number | Unit | Context | Source | Verified |
|---|--------|------|---------|--------|----------|
| 1 | 120 | B USD | Server CPU TAM by 2030 | AMD Q1 2026 earnings transcript | corrected from EP659 / M1.0 interpretation |
| 2 | &gt; 35 | % CAGR | Server CPU TAM expected growth | AMD Q1 2026 earnings transcript | corrected from EP659 / M1.0 interpretation |
| 3 | &gt; 50 | % | AMD server CPU revenue market share target | AMD Financial Analyst Day 2025 press release | verified as forward-looking target |
| 4 | ~ 3000 | TWD | 聯發科股價位階 | EP659 (2026-05 觀察) | needs price feed verification before public |
| 5 | 1-2 | 顆 | 每台 AI server CPU 配比 | knowledge/cpu.html (industry consensus) | needs spec source |

## External Links Cited

| # | URL or reference | Why cited | Last accessed |
|---|------------------|-----------|---------------|
| — | (none, EP659 podcast feed not linked publicly) | — | — |

## Unsourced Claims (must resolve before public)

> M1 是 internal only，這些 claim 可保留為 uncertain。發布前必須清空或補 source。

- 「CPU 復興」 theme lifecycle 標籤（uncertain → 需 theme-detector 跑一次）。
- AMD 週圖支撐 / 阻力結構（uncertain → 需 technical-analyst 跑一次）。
- 近 10 天 CPU 相關新聞 impact ranking（uncertain → 需 market-news-analyst 跑一次）。
- 18 個月 bull/base/bear scenarios（agent-drafted → 需 scenario-analyzer 跑一次驗證）。
- AMD 法說數字的 primary verification（從 EP659 二手轉述 → 已部分對到 AMD press release / official Financial Analyst Day source；earnings transcript仍以 Motley Fool 為輔）。
- AMD / Intel server CPU 市占的歷史對照數據（沒在 EP659 內，brief 沒用，但若公開時要補）。


## M1.1 Source-Backed Addendum

| # | Claim | Source | Captured At | Confidence | Verified By |
|---|-------|--------|-------------|------------|-------------|
| A1 | AMD Q1 2026 revenue was $10.253B, up 38% YoY | research/intake/2026-05-10_amd-q1-2026_cpu.md | 2026-05-10 | known | AMD press release |
| A2 | AMD Data Center revenue was $5.8B, up 57% YoY | research/intake/2026-05-10_amd-q1-2026_cpu.md | 2026-05-10 | known | AMD press release |
| A3 | AMD server CPU TAM expected CAGR >35%, reaching >$120B by 2030 | research/intake/2026-05-10_amd-q1-2026_cpu.md | 2026-05-10 | known via secondary transcript | Motley Fool transcript; official transcript preferred |
| A4 | Intel Q1 2026 DCAI revenue was $5.1B, up 22% YoY | research/intake/2026-05-10_intel-q1-2026_cpu.md | 2026-05-10 | known | Intel press release |
| A5 | Intel says CPU is the AI orchestration/control plane | research/intake/2026-05-10_intel-q1-2026_cpu.md | 2026-05-10 | known via secondary transcript | Motley Fool transcript |
| A6 | Intel ASIC revenue grew >30% QoQ and nearly doubled YoY | research/intake/2026-05-10_intel-q1-2026_cpu.md | 2026-05-10 | known via secondary transcript | Motley Fool transcript |
| A7 | MediaTek Jan-Apr 2026 YTD revenue was NT$195.887B, down 3.06% YoY | research/intake/2026-05-10_mediatek-q1-2026_cpu-asic.md | 2026-05-10 | known | MediaTek IR monthly table |
| A8 | MediaTek expects around $2B AI ASIC revenue in Q4 2026 | research/sources/ai-server-supply-chain/earnings/2026-05-10_mediatek-q1-2026-source-packet.md | 2026-05-12 | known as management expectation | MediaTek Q1 2026 official transcript |
| A9 | Agentic AI tool-dominated workloads can spend up to 88% of E2E latency in CPU-side tool processing | research/sources/ai-server-supply-chain/papers/2026-05-12_agentic-ai-cpu-centric-source-packet.md | 2026-05-12 | known with workload caveat | Georgia Tech / Intel paper |

### Corrections From M1.0

- EP659 note interpreted "120B" as if it were AMD 2026 revenue. M1.1 source packet corrects this: source-backed wording is **server CPU TAM >$120B by 2030**, not AMD 2026 revenue.
- EP659 / M1.0 implied AMD server CPU share >50%. M2.1 source hardening found AMD Financial Analyst Day 2025 primary wording: AMD "expects to achieve more than 50% server CPU revenue market share." This is source-backed as a forward-looking target, not current share.
- MediaTek AI ASIC `$2B Q4 2026` is now verified against MediaTek's official Q1 2026 transcript. Public wording should still call it management expectation / guidance-like commentary, not realized revenue.
- BusinessNext's CPU latency framing now has primary support from the Georgia Tech / Intel paper, but public wording should be workload-specific: "up to 88% in selected tool-dominated workloads," not a universal CPU latency share.
