---
workflow: investment-analysis
artifact_type: analysis-brief
risk: high
created_at: 2026-05-10
umbrella_theme: AI Server Supply Chain
theme: CPU 復興
time_horizon: 6-18 個月
asset_universe:
  primary: ["AMD", "INTC", "2454.TW", "ARM"]
  secondary: ["NVDA", "MRVL", "TSM", "2330.TW"]
  ecosystem: ["DELL", "SMCI", "HPE"]
intake_sources:
  - research/intake/2026-05-10_gooeye-ep659_cpu.md
knowledge_pages:
  - research/knowledge/ai-server-supply-chain/index.html
  - research/knowledge/ai-server-supply-chain/cpu.html
sources_checklist: research/notes/2026-05-10_ai-server-supply-chain_cpu-revival_sources.md
status: gate-pending
gate: IA1
gate_decision_log: ops/decisions/2026-05-10_ia1_cpu-deep-dive.md
---

# Analysis Brief: CPU 復興（AI Server Supply Chain）

> 範圍：第一次 M1 anchor deep dive，搭配 AI Server Supply Chain knowledge map 一起讀。
> Internal only。Gate IA1 dry run。

## Market Question

AI server 資金從 GPU 外溢後，CPU 是否重新回到核心 spend？市占與供應鏈會如何洗牌？

## Time Horizon

6-18 個月。

## Asset Universe

- Primary: AMD、INTC、2454.TW（聯發科）、ARM（隱含 NVDA Grace / AWS Graviton）。
- Secondary: NVDA、MRVL、TSM、2330.TW（TSMC）。
- Ecosystem: DELL、SMCI、HPE。

---

## Theme Thesis (AI-FILLED, human-reviewed)

> 在 AI server 場景下，CPU 從「commodity 旁角」重新被市場推回 spend 中心；接下來 6-18 個月，AMD 透過 EPYC 在伺服器 CPU 市占有機會穩定壓過 Intel，聯發科則仍停在 I/O / memory subsystem，距離「打入主晶片」還有 1-2 年的不確定性，但個股股價已先 priced 進這條故事。

## Drivers (AI-FILLED, human-reviewed)

### Fundamental Drivers

- AI server unit 出貨 ramp，每台仍配 1-2 顆 server CPU，CPU 需求隨 GPU/ASIC 同步成長。
  — Source: knowledge/cpu.html (industry consensus, confidence: inferred).
- AMD 法說 guidance 給出 2026 年營收 120B / 年增 &gt; 35% / 伺服器 CPU 市占目標 &gt; 50%。
  — Source: gooeye-ep659 引述 AMD 法說 (confidence: known per EP659, must verify against AMD 8-K before public).
- Intel 法說呼應 CPU 重要性，市場開始把 CPU 從「被 GPU 邊緣化」的論述拉回。
  — Source: gooeye-ep659 (confidence: known per EP659, secondary cite).
- 聯發科法說切入 I/O / memory subsystem，搭 AMD/Intel 周邊。
  — Source: gooeye-ep659 (confidence: known per EP659, paths/customers not detailed).

### Narrative Drivers

- 「資金從 GPU 大轉向，CPU 成市場核心」的市場敘事 — gooeye-ep659 主軸。
- 美股大跌時 CPU 族群相對強勢，技術面已先反映。
- 聯發科第一次出現多根漲停，市場對台廠切 server CPU 周邊的想像升溫。

### Catalysts (next 0-6 months)

- AMD 下一份季法說（重點：server segment 出貨量、AI 段營收揭露）。
- Intel 下一份季法說（重點：foundry 進度、Gaudi 競爭策略、server CPU 市占防守）。
- 聯發科法說對 server CPU subsystem 進度的說明。
- Hyperscaler（AWS / GOOGL / MSFT / META）capex 更新對 CPU vs GPU 比例的揭露。
- skill missing: `theme-detector` 對「CPU 復興」當前 lifecycle 的定位（emerging / accelerating / mature / decaying）。

## Winners / Losers (AI-FILLED, human-reviewed)

| Side | Ticker / Name | One-line reason | Confidence |
|------|---------------|-----------------|------------|
| Winner | AMD | EPYC 市占擴張、guidance 強、AI server CPU 主受惠者 | known (per EP659 引述法說) |
| Watch | INTC | 落後 EPYC 但仍有 foundry / 政府 / Gaudi 反擊牌 | uncertain |
| Watch | 2454.TW 聯發科 | 從 I/O / memory subsystem 切入，但「還沒打入主晶片」、預期已打滿 | uncertain (per EP659 警語) |
| Edge case | NVDA Grace / AWS Graviton / Ampere | ARM 路徑替代品；hyperscaler 自研 | inferred (not in EP659) |
| Ecosystem | TSM (2330.TW) | AMD/Intel/聯發科都仰賴 TSMC | inferred |
| Ecosystem | DELL / SMCI / HPE | server OEM，CPU + GPU 出貨同步受惠 | inferred |
| Loser candidate | 高估值 ARM 替代股 (若 x86 防守成功) | x86 ecosystem 鎖定企業、ARM ramp 慢 | uncertain |

## Key Data Points (AI-FILLED, human-reviewed)

| # | Data Point | Value | Date / Period | Source | Confidence |
|---|-----------|-------|---------------|--------|------------|
| 1 | AMD 2026 全年營收 guidance | 120B USD | 2026 全年 | gooeye-ep659 引述 AMD 法說 | known |
| 2 | AMD 2026 營收年增 | &gt; 35% YoY | 2026 全年 | gooeye-ep659 | known |
| 3 | AMD 伺服器 CPU 市占目標 | &gt; 50% | 中期目標，未指定年 | gooeye-ep659 | known |
| 4 | AMD AI 營收能見度 | 2027 年 | 中長期 | gooeye-ep659 | known |
| 5 | 聯發科股價反應位階 | ~3000 TWD | 2026-05 EP659 錄製當週 | gooeye-ep659 | known |
| 6 | CPU 在 AI server 的配比 | 每台 1-2 顆 | 持續 | knowledge/cpu.html (產業共識) | inferred |
| 7 | 「CPU 復興」 theme lifecycle | unknown | 2026-05 | skill missing: theme-detector | uncertain |
| 8 | AMD 週圖技術結構 | unknown | 2026-05 | skill missing: technical-analyst | uncertain |
| 9 | 近 10 天 CPU 相關新聞 impact ranking | unknown | 2026-05 | skill missing: market-news-analyst | uncertain |
| 10 | 18 個月 bull/base/bear scenarios | 見下方 Scenarios（draft） | 6-18 個月 | skill missing: scenario-analyzer (draft below by agent) | uncertain |

## Scenarios (DRAFT — pending scenario-analyzer)

- **Bull case**: AMD 法說兌現，AI 營收 2026 末已可量化；聯發科 server CPU subsystem 進度公告，台廠切入路徑明朗化；hyperscaler capex 維持高檔 → CPU 族群延續多頭 6-12 個月。
- **Base case**: AMD guidance 達成度約 80-90%，但 narrative 已 priced；聯發科仍停 I/O / memory，股價橫盤消化；INTC 反擊有限；族群進入「個股表現分化」階段 → 主動選股勝過 ETF。
- **Bear case**: AMD 下次法說 server segment 出貨弱於 guidance；聯發科被客戶否認進入主晶片；hyperscaler capex 重新偏向 GPU/ASIC；CPU theme narrative 失效 → 6 個月內回吐 50% 漲幅。

需要 `scenario-analyzer` 重跑驗證，目前是 agent draft。

---

## What I Learned (HUMAN-WRITTEN, ≥ 100 字)

> 規則：你新理解到什麼？不是 summary，是「我之前不懂、現在懂了」的具體點。
> Floor: 至少 100 字。

<TODO: 你親手寫 ≥ 100 字>

提示：以下是這次資料中「應該讓你產生新理解」的候選點，從這幾條挑你真有體會的去發揮——
- AI server 即使滿載 GPU/ASIC，仍需要 1-2 顆 CPU 做 host 控制；GPU 越多、CPU 協調工作越關鍵。
- AMD 在 server CPU 的市占擴張不是因為通用運算復甦，而是 AI server unit 同步擴張帶動的。
- 聯發科「I/O / memory subsystem」是周邊，不是主晶片；股價先 priced 主晶片故事是預期錯置。
- 「資金從 GPU 外溢」這條敘事的執行週期一般 6-18 個月，不是一兩季。

## What I Still Don't Understand (HUMAN-WRITTEN, ≥ 3 條)

> 規則：誠實列出。不丟臉。下次優先補。

<TODO: 你親手列 ≥ 3 條>

起始候選（來自 cpu.html 的 open questions，可挑可加）：
- AI server 對 CPU 是 structural 需求還是 cyclical 補貨？
- 聯發科 I/O / memory subsystem 對應哪些產品（PCIe switch / CXL controller / memory expander）？
- AMD 拿伺服器 CPU 市占 &gt; 50% 後，Intel 防守牌是哪個（製程、政府、Gaudi、Foundry）？
- 「CPU 復興」這個敘事的歷史對照組（2017 EPYC 1st-gen ramp？2020 數據中心爆發？）是什麼？

## My POV (HUMAN-WRITTEN, ≥ 200 字)

> 規則：你的觀點。為什麼買 / 不買 / 觀察 / 避開。允許不確定，但要明確說「我不確定」而不是空話。
> Floor: 至少 200 字。

<TODO: 你親手寫 ≥ 200 字>

提示：你的 POV 不該重複 thesis，而是回答幾個具體問題：
- 你會買 AMD 嗎？什麼價位 / 什麼條件？
- 你會接聯發科嗎？預期打滿是不是真的，怎麼判斷？
- 「資金外溢」這條敘事你會 stand by 多久？看到什麼就退？
- 如果讓你只能選一檔 CPU 受惠股，你會選誰？為什麼？
- 你個人立場：beat（超越市場）/ in line / underperform，給原因。
- 你不確定的部分要說出來，不要假裝有把握。

## My Invalidation (HUMAN-WRITTEN, exactly 3)

> 規則：3 個會讓你改變想法的具體訊號。要可被觀察、可被計數、有時間框。

<TODO: 你親手寫 3 條 invalidation>

起始候選（你可以採用、修改或全部換掉）：

1. **AMD 下一份季法說 server segment 營收 &lt; guidance 中位數**（2026 Q2 揭露，date-stamped）→ 這條失效則 thesis 主軸動搖。
2. **聯發科法說明確說明 server CPU subsystem 仍只在 I/O 階段、未進主晶片 roadmap**（下次 IR 說明會內，60 天內）→ 反映預期 mispriced。
3. **Hyperscaler capex 公告中 GPU/ASIC 對比 CPU 配比顯著上修**（AWS / GOOGL / MSFT / META 任一）→ 反映 CPU 不是受惠主軸。

---

## Disclaimer

This is research and education, not financial advice. I may be wrong. Do your own
research and consider your own risk tolerance.
