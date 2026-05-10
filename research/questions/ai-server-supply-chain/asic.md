---
workflow: investment-analysis
artifact_type: tutor-qa
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
topic: asic
status: draft
---

# Q&A: ASIC 是什麼？用在哪裡？為何重要？

## Question

ASIC 是什麼？跟 GPU 差在哪？為什麼市場會從 GPU 轉到 ASIC？MediaTek / Intel / 創意 / 世芯在這裡各自是什麼角色？

## Short Answer

ASIC 是 Application-Specific Integrated Circuit，也就是為特定工作負載客製的晶片。GPU 是通用並行運算工具，彈性高；ASIC 是為固定任務最佳化，彈性低但效能/功耗/成本可能更好。Hyperscaler（AWS、Google、Meta）有足夠規模與固定 workload，所以會自研 ASIC 降低對 NVDA 的依賴。投資上，ASIC 不是 GPU 死掉，而是 AI capex 外溢到另一條供應鏈。

## Mental Model

GPU 像萬用瑞士刀，什麼都能做；ASIC 像工廠裡專門做一個動作的機台，只做一件事但做到最便宜最快。當客戶量夠大、需求夠固定，專用機台就比萬用工具划算。

## Technical Explanation

ASIC 的關鍵是客製化。雲端巨頭可以根據自家模型、資料中心架構、軟體棧設計 tensor cores、memory hierarchy、interconnect 和 I/O。缺點是研發週期長、NRE 高、設計錯就很難改；優點是大規模部署後成本和功耗可能優於 GPU。MediaTek 的資料顯示其第一個美國 hyperscaler AI accelerator ASIC project 進入 production schedule，Q4 2026 目標收入約 $2B（仍需官方 transcript 進一步驗證）。

## Why Investors Care

如果 ASIC 成為 AI server spend 的第二腿，受惠的不只是 NVDA，而是 AVGO、MRVL、MediaTek、創意、世芯、TSMC、封測和 HBM 供應鏈。估值比較上，市場會把「可持續客製晶片 revenue」當成長股 story，尤其當大型 ASIC 廠估值低於已炒高的光通股時。

## Companies / Tickers

| Company / Ticker | Role | Why it matters |
|------------------|------|----------------|
| 2454.TW MediaTek | AI accelerator ASIC / data center tech | Q4 2026 AI ASIC revenue target around $2B (secondary source). |
| INTC | custom ASIC IPU + foundry/packaging | Google collaboration includes custom ASIC IPUs; ASIC revenue up >30% QoQ / nearly 2x YoY (secondary transcript). |
| AVGO | large-scale custom silicon | Likely comparison point for “large-cap ASIC” valuation. |
| MRVL | custom silicon / interconnect | ASIC + networking/optical exposure. |
| 3443.TW 創意 | ASIC design service | Google TPU narrative exposure. |
| 3661.TW 世芯-KY | ASIC design service | AWS Trainium narrative exposure. |

## What To Watch

| Signal | Why it matters | Source to monitor |
|--------|----------------|-------------------|
| MediaTek AI ASIC Q4 2026 revenue | 驗證從 narrative 變成財報收入 | MediaTek transcript / quarterly results |
| Hyperscaler customer disclosure | 確認客戶集中與 ramp quality | MediaTek / industry reports |
| AVGO / MRVL custom silicon commentary | 定義大市值 ASIC benchmark | AVGO / MRVL earnings |
| TSMC CoWoS / advanced packaging capacity | ASIC ramp 是否受限於封裝 | TSMC earnings / reports |

## What I Still Don't Know

- MediaTek 第一個美國 hyperscaler 客戶是否為 Google？目前不能公開寫死。
- Q4 2026 $2B 是單季 revenue 還是 annualized run-rate，需要官方 transcript 驗證。
- Intel 的 ASIC growth 到底是 IPU、DCAI custom silicon，還是 broader ASIC 分類。

## Sources

- `research/sources/ai-server-supply-chain/earnings/2026-05-10_mediatek-q1-2026-source-packet.md`
- `research/sources/ai-server-supply-chain/earnings/2026-05-10_intel-q1-2026-source-packet.md`
- `research/intake/2026-05-10_gooeye-ep659_asic.md`

## Update Targets

- Knowledge page to update: `research/knowledge/ai-server-supply-chain/asic.html`
- Brief section to update: Drivers, Winners/Losers, Open Questions
