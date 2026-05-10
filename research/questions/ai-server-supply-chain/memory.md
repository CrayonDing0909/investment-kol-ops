---
workflow: investment-analysis
artifact_type: tutor-qa
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
topic: memory
status: draft
---

# Q&A: HBM 跟一般 DRAM 差在哪？為什麼現在仍重要？

## Question

HBM 跟一般 DRAM 差在哪？AI server 不是都看 GPU/ASIC 嗎，為什麼記憶體還很重要？MediaTek 說 custom HBM / memory subsystem 跟這有關嗎？

## Short Answer

HBM 是高頻寬記憶體，專門貼在 GPU / ASIC 旁邊，讓加速器可以高速讀寫資料；一般 DRAM 是伺服器主記憶體，離晶片較遠，頻寬低但容量大。AI 模型越大、推論越複雜，memory bandwidth 越容易成為瓶頸。AMD Q1 source 提到 Samsung + AMD 的 HBM4 / DRAM collaboration；MediaTek source 也提到 custom HBM、high-speed interconnect、CPO 等 data center 技術，代表 memory subsystem 是 AI server spend 的一部分。

## Mental Model

GPU/ASIC 像工廠機器，HBM 像貼在機器旁邊的超高速零件倉庫；DRAM 像廠房外的大倉庫。機器越快，旁邊倉庫補貨速度越重要，不然機器會空轉。

## Technical Explanation

HBM 把多層 DRAM die 垂直堆疊並用 TSV 連接，再透過 CoWoS / advanced packaging 靠近 GPU/ASIC。它犧牲成本與封裝難度，換取極高 bandwidth。一般 DDR DRAM 容量大但距離運算晶片較遠，適合 CPU 主記憶體。AI server 需要兩者：GPU/ASIC 旁邊要 HBM，CPU host 仍要 DDR / LPDDR 類主記憶體，storage 還需要 NAND/SSD。

## Why Investors Care

HBM 是 AI accelerator 的 attach part，會跟 GPU/ASIC 出貨一起走；但 bottleneck 往往不只在晶片，還在 HBM 產能與 CoWoS 封裝。Memory 成本上升也會壓 PC / smartphone demand，AMD 和 Intel 都提到 memory/component cost pressure，MediaTek smartphone weakness 也跟 memory costs 有關。

## Companies / Tickers

| Company / Ticker | Role | Why it matters |
|------------------|------|----------------|
| SK Hynix | HBM leader | 需補 source，可能是 HBM3e/HBM4 主要受惠者。 |
| Samsung | HBM / DRAM | AMD source 提到 Samsung + AMD HBM4 collaboration。 |
| Micron (MU) | HBM / DRAM | HBM3e ramp 需要追。 |
| TSM / 2330.TW | CoWoS packaging | HBM + GPU/ASIC 的封裝 bottleneck。 |
| 2454.TW MediaTek | custom HBM / memory subsystem | 可能切入 data center interconnect / memory 周邊，不是記憶體製造。 |

## What To Watch

| Signal | Why it matters | Source to monitor |
|--------|----------------|-------------------|
| HBM3e / HBM4 supply allocation | 驗證 AI accelerator ramp 是否被 memory 限制 | SK Hynix / Samsung / Micron earnings |
| CoWoS capacity | HBM + compute die 封裝瓶頸 | TSMC earnings |
| Memory cost commentary | 成本壓力會影響 PC/smartphone demand | AMD / Intel / MediaTek earnings |
| MediaTek custom HBM / interconnect roadmap | 驗證是否能從 subsystem 走向更核心 data center exposure | MediaTek official transcript |

## What I Still Don't Know

- HBM3e / HBM4 timeline 和各廠份額需要 primary source。
- MediaTek 的 `custom HBM` 是 design support、controller、IP，還是封裝/客戶案的一部分？
- CoWoS capacity 何時從瓶頸變成過剩，這會決定 HBM/ASIC narrative 何時降溫。

## Sources

- `research/sources/ai-server-supply-chain/earnings/2026-05-10_amd-q1-2026-source-packet.md`
- `research/sources/ai-server-supply-chain/earnings/2026-05-10_mediatek-q1-2026-source-packet.md`
- `research/intake/2026-05-10_gooeye-ep659_memory.md`

## Update Targets

- Knowledge page to update: `research/knowledge/ai-server-supply-chain/memory.html`
- Brief section to update: Open Questions, Drivers
