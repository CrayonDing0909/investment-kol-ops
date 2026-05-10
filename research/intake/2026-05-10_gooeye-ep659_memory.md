---
workflow: investment-analysis
artifact_type: intake-note
risk: low
created_at: 2026-05-10
source_type: podcast
source_id: gooeye-ep659
source_url: ""
themes: [memory]
status: needs-follow-up
---

# Intake Note: 股癌 EP659 — 資金從 GPU 大轉向 (Memory 段落)

> 注意：EP659 沒有獨立的 memory（HBM / DRAM / NAND）章節，這份 intake 屬於 `needs-follow-up`：
> 只能從聯發科段落「I/O、memory 還沒打入主晶片」這一句側面取得，正式 memory deep dive 需要後續補資料（Hynix / Micron / Samsung 法說、HBM3e/HBM4 roadmap、CoWoS 容量）。

## Source

- Type: podcast
- Title: 股癌 EP659
- Author / Host: 股癌（謝孟恭）
- Date: 2026-05-06
- Captured At: 2026-05-10

## Themes (this intake covers)

- [ ] cpu
- [ ] asic
- [x] memory
- [ ] passive-components
- [ ] cooling
- [ ] software

## Key Claims (verbatim or near-verbatim)

- 「目前做 I/O、memory，還沒看到打入主晶片，預期打太滿了。」 — 股癌 EP659（CPU 段，提到聯發科切 memory subsystem）

EP659 沒有額外的 memory / HBM 直接論述，這條是唯一明確訊號。

## Numbers (with units, dates, sources)

| Number | Unit | Subject | Date / Period | Source position |
|--------|------|---------|---------------|-----------------|
| — | — | EP659 沒有 memory 直接數字 | — | needs follow-up |

## Names Mentioned

- Companies / Tickers: 聯發科（2454.TW，談 I/O + memory subsystem）
- Implicit but not stated in EP659: Samsung、SK Hynix、Micron、Sandisk、AMD MI 系列（HBM 客戶）
- Products / Technologies: I/O subsystem、memory subsystem（聯發科切入點）

## My Initial Reaction (HUMAN-WRITTEN)

> 範例提示：「memory 在 AI server 應該是 HBM 主軸，但 EP659 沒明講。我需要去找 Hynix / Micron / Samsung 最新法說補。」

<TODO: 你親手寫 1-3 句>

## Open Questions (HUMAN-WRITTEN)

> 起始參考（這個 theme open questions 特別多，因為 EP659 沒講）：
> - HBM3e / HBM4 timeline 是什麼？哪一家進度領先？
> - HBM 跟 CoWoS 是什麼關係？bottleneck 在哪？
> - DRAM / NAND cycle 現在到哪？
> - 「I/O subsystem」跟「memory subsystem」是什麼？聯發科怎麼切進來？跟 AMD / Intel CPU 的關係？

- <你的 question>

## Quotes Worth Reusing

- （EP659 中無 memory 直接 quote，這份 intake 主要是 placeholder + open questions。）

## Follow-up Sources Needed

- AMD 2026 Q1 法說 transcript（特別是 MI 系列 HBM 容量需求）
- SK Hynix / Micron / Samsung 最新法說 + roadmap
- TSMC CoWoS capacity update
- 任何 memory-specific 報告（看是否有近期 podcast 或產業報告專講）

## Linked Outputs

- Knowledge pages updated: [research/knowledge/ai-server-supply-chain/memory.html](../knowledge/ai-server-supply-chain/memory.html)
- Briefs that cite this intake: <pending; cross-referenced from CPU brief about 聯發科>
