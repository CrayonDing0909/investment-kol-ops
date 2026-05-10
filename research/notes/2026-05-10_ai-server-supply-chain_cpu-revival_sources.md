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
| 1 | AMD 法說估 2026 營收 120B、年增 &gt; 35% | research/intake/2026-05-10_gooeye-ep659_cpu.md (EP659 CPU 段) | 2026-05-10 | known (per EP659; needs primary verification before public) | self |
| 2 | AMD 目標伺服器 CPU 市占 &gt; 50% | research/intake/2026-05-10_gooeye-ep659_cpu.md | 2026-05-10 | known (per EP659; needs primary verification) | self |
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
| 1 | 120 | B USD | AMD 2026 全年營收 guidance | EP659 引述 AMD 法說 | needs primary AMD 8-K before public |
| 2 | &gt; 35 | % YoY | AMD 2026 營收年增 | EP659 | needs primary verification |
| 3 | &gt; 50 | % | AMD 伺服器 CPU 市占目標 | EP659 | needs primary verification |
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
- AMD 法說數字的 primary verification（從 EP659 二手轉述 → 必須對到 AMD 8-K 或法說官方 transcript）。
- AMD / Intel server CPU 市占的歷史對照數據（沒在 EP659 內，brief 沒用，但若公開時要補）。
