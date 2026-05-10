---
workflow: investment-analysis
artifact_type: tutor-qa
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
topic: passive-components
status: draft
---

# Q&A: 被動元件是哪些東西？AI server 為什麼需要？

## Question

被動元件到底是哪些東西？MLCC、鉭電容、鋁電容差在哪？為什麼 AI server 會讓它們供需吃緊？

## Short Answer

被動元件是電路裡不主動放大訊號的基礎零件，主要包含電容、電阻、電感。AI server 功率密度高、電流變化大，需要大量電容做穩壓與濾波，其中 MLCC 用量最大，鉭電容/鋁電容用在不同電源位置。股癌 EP659 提到信昌電交期拉長、鉭電容/鋁電容/MLCC 供需吃緊，市場在等類 2017-2018 的漲價敘事啟動。

## Mental Model

把 AI server 想成一台超高功率跑車。GPU/CPU/ASIC 是引擎，被動元件像油路、電瓶、穩壓器，平常不顯眼，但功率一上來，不穩就整台車會熄火。引擎越強，周邊穩壓需求越高。

## Technical Explanation

MLCC（Multi-Layer Ceramic Capacitor）適合高頻濾波，用量極大；鉭電容容量密度高，常用在電源穩壓；鋁電容容量大、成本低，常用在電源輸入或低頻濾波。AI server board 上 GPU/CPU/ASIC 需要乾淨穩定電源，VRM 與 power delivery network 裡會使用大量電容。供需吃緊通常先表現在交期拉長，再到漲價、庫存補貨與財報改善。

## Why Investors Care

被動元件投資不是看單一產品多酷，而是看「供需週期 + 漲價 + 庫存補貨」是否同步發生。EP659 的重點是敘事還沒真正啟動，所以投資上要等 catalyst，而不是聽到供需吃緊就追。最重要指標是交期、ASP、月營收、庫存週轉與漲價公告。

## Companies / Tickers

| Company / Ticker | Role | Why it matters |
|------------------|------|----------------|
| 6173.TW 信昌電 | 鉭電容 | EP659 直接提到交期拉長。 |
| 2327.TW 國巨 | MLCC 大哥 | 若高階產能轉向 AI server，可能帶動小弟吃訂單。 |
| 2492.TW 華新科 | MLCC 台系 | 台系「小弟」可能承接外溢。 |
| 2472.TW 立隆電 | 鋁電容 | AI power delivery 可能拉動部分需求。 |
| 2375.TW 智寶 | 鋁電容 | 同上，需資料驗證。 |

## What To Watch

| Signal | Why it matters | Source to monitor |
|--------|----------------|-------------------|
| 交期拉長公告 | 供給吃緊早期訊號 | 公司公告 / 通路報價 |
| 漲價公告 | 敘事啟動 catalyst | 國巨 / 華新科 / 信昌電新聞 |
| 月營收 YoY 轉正 | 財報可見化 | MOPS / 公司月營收 |
| 庫存週轉改善 | cycle 反轉 | 季報 |

## What I Still Don't Know

- AI server 單機 MLCC / 鉭 / 鋁電容 BOM 具體顆數與單價。
- 2017-2018 那輪的完整時序：交期 → 漲價 → 月營收 → 股價。
- 海外大哥（Murata / TDK / Samsung Electro-Mechanics）產能轉高階的實際證據。

## Sources

- `research/intake/2026-05-10_gooeye-ep659_passive-components.md`

## Update Targets

- Knowledge page to update: `research/knowledge/ai-server-supply-chain/passive-components.html`
- Brief section to update: Open Questions / future passive-components deep dive
