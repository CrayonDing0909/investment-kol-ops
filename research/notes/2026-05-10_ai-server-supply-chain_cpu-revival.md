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
  - research/intake/2026-05-10_amd-q1-2026_cpu.md
  - research/intake/2026-05-10_intel-q1-2026_cpu.md
  - research/intake/2026-05-10_mediatek-q1-2026_cpu-asic.md
knowledge_pages:
  - research/knowledge/ai-server-supply-chain/index.html
  - research/knowledge/ai-server-supply-chain/cpu.html
  - research/questions/ai-server-supply-chain/cpu.md
  - research/questions/ai-server-supply-chain/asic.md
  - research/questions/ai-server-supply-chain/memory.md
sources_checklist: research/notes/2026-05-10_ai-server-supply-chain_cpu-revival_sources.md
status: gate-approved
gate: IA1
gate_scope: internal-only
public_status: not-public-ready
gate_decision_log: ops/decisions/2026-05-10_ia1_cpu-deep-dive.md
---

# Analysis Brief: CPU 復興（AI Server Supply Chain）

> 範圍：第一次 M1 anchor deep dive，搭配 AI Server Supply Chain knowledge map 一起讀。
> Internal only。Gate IA1 dry run。
> Note: HUMAN-WRITTEN sections below are agent-seeded drafts accepted by the user for M1.2 workflow continuity; user may revise voice later before public use.

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

> 在 AI server 場景下，CPU 從「commodity 旁角」重新被市場推回 spend 中心；接下來 6-18 個月，AMD 的 EPYC / Data Center 數字是最清楚的 source-backed 受惠線，Intel 的 Xeon 則被重新定位為 AI stack 的 orchestration / control plane。聯發科更像 AI ASIC + I/O / memory subsystem 的 data center optionality，不能和 server CPU 主晶片混為一談。

## Drivers (AI-FILLED, human-reviewed)

### Fundamental Drivers

- AMD Q1 2026 Data Center revenue was $5.8B, up 57% YoY, driven by EPYC and Instinct demand.
  — Source: `research/intake/2026-05-10_amd-q1-2026_cpu.md` (confidence: known).
- AMD management said inferencing and Agentic AI increase server CPU compute needs for orchestration, data movement, parallel execution, and head-node roles.
  — Source: AMD Q1 2026 transcript intake (confidence: known via secondary transcript; primary transcript still preferred before public).
- AMD now expects server CPU TAM to grow at &gt;35% CAGR, reaching &gt;$120B by 2030. This corrects the earlier EP659 ambiguity: 120B refers to server CPU TAM, not AMD 2026 revenue.
  — Source: AMD Q1 2026 transcript intake (confidence: known via secondary transcript).
- Intel Q1 2026 DCAI revenue was $5.1B, up 22% YoY, and management framed CPU as the AI stack orchestration/control plane.
  — Source: `research/intake/2026-05-10_intel-q1-2026_cpu.md` (confidence: known).
- MediaTek has data center ASIC visibility and I/O / memory subsystem relevance, but its exposure is not the same as owning server CPU main silicon.
  — Source: `research/intake/2026-05-10_mediatek-q1-2026_cpu-asic.md` and official Q1 2026 transcript (confidence: known for `$2B Q4 2026` as management expectation; still not realized revenue).

### Narrative Drivers

- 「資金從 GPU 外溢到 CPU / ASIC / server chain」仍是 EP659 的 narrative seed。
- AMD / Intel 的 official language 都支持「agentic AI / inference 讓 CPU 重新重要」這個方向。
- MediaTek 的故事應改寫成「data center ASIC + subsystem optionality」，不應簡化成 CPU 主晶片。

### Catalysts (next 0-6 months)

- AMD 下一份季法說（重點：server segment 出貨量、AI 段營收揭露）。
- Intel 下一份季法說（重點：foundry 進度、Gaudi 競爭策略、server CPU 市占防守）。
- 聯發科法說對 server CPU subsystem 進度的說明。
- Hyperscaler（AWS / GOOGL / MSFT / META）capex 更新對 CPU vs GPU 比例的揭露。
- skill missing: `theme-detector` 對「CPU 復興」當前 lifecycle 的定位（emerging / accelerating / mature / decaying）。

## Winners / Losers (AI-FILLED, human-reviewed)

| Side | Ticker / Name | One-line reason | Confidence |
|------|---------------|-----------------|------------|
| Winner | AMD | EPYC + Data Center 數字最直接；Data Center revenue $5.8B, +57% YoY；server CPU TAM 上修 | known |
| Watch | INTC | Xeon 作為 AI orchestration/control plane；DCAI +22% YoY，但仍有 foundry/18A/cost pressure | known + uncertain |
| Watch | 2454.TW 聯發科 | AI ASIC revenue target / data center tech exposure明確，但不是 server CPU 主晶片 | mixed (primary revenue + secondary ASIC claims) |
| Edge case | NVDA Grace / AWS Graviton / Ampere | ARM 路徑替代品；hyperscaler 自研 | inferred (not in EP659) |
| Ecosystem | TSM (2330.TW) | AMD/Intel/聯發科都仰賴 TSMC | inferred |
| Ecosystem | DELL / SMCI / HPE | server OEM，CPU + GPU 出貨同步受惠 | inferred |
| Loser candidate | 高估值 ARM 替代股 (若 x86 防守成功) | x86 ecosystem 鎖定企業、ARM ramp 慢 | uncertain |

## Key Data Points (AI-FILLED, human-reviewed)

| # | Data Point | Value | Date / Period | Source | Confidence |
|---|-----------|-------|---------------|--------|------------|
| 1 | AMD total revenue | $10.253B | Q1 2026 | AMD Q1 2026 source packet | known |
| 2 | AMD Data Center revenue | $5.8B, +57% YoY | Q1 2026 | AMD Q1 2026 source packet | known |
| 3 | AMD server CPU TAM | &gt;$120B by 2030, &gt;35% CAGR | long-term | AMD Q1 2026 transcript intake | known via secondary transcript |
| 4 | AMD expected server CPU revenue growth | &gt;70% YoY | Q2 2026 | AMD Q1 2026 transcript intake | known via secondary transcript |
| 5 | Intel DCAI revenue | $5.1B, +22% YoY | Q1 2026 | Intel Q1 2026 source packet | known |
| 6 | Intel ASIC revenue growth | &gt;30% QoQ, nearly 2x YoY | Q1 2026 | Intel transcript intake | known via secondary transcript |
| 7 | MediaTek AI ASIC revenue target | ~$2B | Q4 2026 | MediaTek official Q1 2026 transcript | known as management expectation |
| 8 | MediaTek Jan-Apr YTD revenue | NT$195.887B, -3.06% YoY | Jan-Apr 2026 | MediaTek IR monthly table | known |
| 9 | CPU 在 AI server 的配比 | 每台 1-2 顆 | 持續 | knowledge/cpu.html (industry consensus) | inferred |
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

我原本以為 CPU 在 AI server 裡只是配角，真正重要的是 GPU / ASIC。
但讀完 AMD、Intel 和 BusinessNext 後，我比較理解 CPU 的角色不是負責主要算力，
而是負責 orchestration / control plane。尤其 agentic AI 從單次問答變成多步驟任務，
會需要更多資料搬運、工具呼叫、排程、程式執行和長時間運行，這些不是 GPU 擅長的部分。

所以 CPU 復興不是「CPU 取代 GPU」，而是 AI server spend 從單一 GPU 敘事擴散到整個系統架構。
AMD 的 Data Center revenue、EPYC demand、server CPU TAM 上修，是目前最直接的財報證據。
Intel 的說法則讓我理解，CPU 也可以被重新定義為 AI stack 的 control plane，
不是過去那種單純通用運算的老故事。

提示：以下是這次資料中「應該讓你產生新理解」的候選點，從這幾條挑你真有體會的去發揮——
- AI server 即使滿載 GPU/ASIC，仍需要 1-2 顆 CPU 做 host 控制；GPU 越多、CPU 協調工作越關鍵。
- AMD 在 server CPU 的市占擴張不是因為通用運算復甦，而是 AI server unit 同步擴張帶動的。
- 聯發科「I/O / memory subsystem」是周邊，不是主晶片；股價先 priced 主晶片故事是預期錯置。
- 「資金從 GPU 外溢」這條敘事的執行週期一般 6-18 個月，不是一兩季。

## What I Still Don't Understand (HUMAN-WRITTEN, ≥ 3 條)

> 規則：誠實列出。不丟臉。下次優先補。

1. 我還不確定 AMD 的 server CPU TAM >120B by 2030，市場目前到底 price in 多少。
2. 我還不懂 CPU demand 是因為 attach rate 上升、server units 上升，還是 utilization 上升。
3. 我還不確定 Intel 的 CPU control plane 說法，是實際競爭力回來，還是公司在重塑敘事。
4. 我不確定 MediaTek 到底是 ASIC story、I/O / memory subsystem story，還是市場把兩者混在一起炒。
5. AMD Analyst Day primary source 已驗證 `>50% server CPU revenue market share` 是 forward-looking target，不是目前市占。

起始候選（來自 cpu.html 的 open questions，可挑可加）：
- AI server 對 CPU 是 structural 需求還是 cyclical 補貨？
- 聯發科 I/O / memory subsystem 對應哪些產品（PCIe switch / CXL controller / memory expander）？
- AMD 拿伺服器 CPU 市占 &gt; 50% 後，Intel 防守牌是哪個（製程、政府、Gaudi、Foundry）？
- 「CPU 復興」這個敘事的歷史對照組（2017 EPYC 1st-gen ramp？2020 數據中心爆發？）是什麼？

## My POV (HUMAN-WRITTEN, ≥ 200 字)

> 規則：你的觀點。為什麼買 / 不買 / 觀察 / 避開。允許不確定，但要明確說「我不確定」而不是空話。
> Floor: 至少 200 字。

我目前相信 CPU 復興這條 thesis 有成立，但我不會把它理解成 CPU 取代 GPU，
而是 AI server spend 從 GPU 擴散到整個系統架構。AMD 的 source 最有說服力，
因為它已經在 Data Center revenue、EPYC demand、server CPU TAM 上修裡看到財報證據。
Intel 的說法也重要，但我會把它視為防守與修復線，而不是最強攻擊線。

如果只能先研究一檔，我會先看 AMD，因為它同時有 CPU 和 accelerator exposure，
而且 thesis 比較 source-backed。Intel 我會觀察 DCAI 和 Xeon design wins 是否延續。
MediaTek 我暫時不會把它當 CPU 主晶片故事，而是 ASIC / subsystem optionality；
它最大的風險是市場把「未來可能性」提前 price in。

所以我的行動會是先建立觀察清單，不急著把這條當成買進理由。
我會等 AMD 下一份法說確認 server CPU growth 是否延續，也會等 MediaTek 官方 transcript
確認 AI ASIC revenue 的說法。這題對中文投資者最有價值的 insight 是：
AI server 不是只有 GPU，真正的投資機會可能來自資金開始理解整個系統瓶頸。

提示：你的 POV 不該重複 thesis，而是回答幾個具體問題：
- 你會買 AMD 嗎？什麼價位 / 什麼條件？
- 你會接聯發科嗎？預期打滿是不是真的，怎麼判斷？
- 「資金外溢」這條敘事你會 stand by 多久？看到什麼就退？
- 如果讓你只能選一檔 CPU 受惠股，你會選誰？為什麼？
- 你個人立場：beat（超越市場）/ in line / underperform，給原因。
- 你不確定的部分要說出來，不要假裝有把握。

## My Invalidation (HUMAN-WRITTEN, exactly 3)

> 規則：3 個會讓你改變想法的具體訊號。要可被觀察、可被計數、有時間框。

1. 如果 AMD 下一份季報 Data Center revenue 或 server CPU growth 明顯低於 guidance，且管理層下修 server CPU demand，我會降低 CPU 復興 thesis 的信心。
2. 如果 Intel 下一份季報 DCAI / Xeon design wins 無法延續，或 CPU control plane 敘事沒有轉成收入，我會把 Intel 從修復線降級成純敘事。
3. 如果 MediaTek 後續法說或營收無法延續 AI ASIC $2B Q4 2026 / data center project ramp 的說法，或明確顯示目前只停在低毛利 subsystem，我會把台廠 AI server optionality 降級。

起始候選（你可以採用、修改或全部換掉）：

1. **AMD 下一份季法說 server segment 營收 &lt; guidance 中位數**（2026 Q2 揭露，date-stamped）→ 這條失效則 thesis 主軸動搖。
2. **聯發科法說明確說明 server CPU subsystem 仍只在 I/O 階段、未進主晶片 roadmap**（下次 IR 說明會內，60 天內）→ 反映預期 mispriced。
3. **Hyperscaler capex 公告中 GPU/ASIC 對比 CPU 配比顯著上修**（AWS / GOOGL / MSFT / META 任一）→ 反映 CPU 不是受惠主軸。

---

## Disclaimer

This is research and education, not financial advice. I may be wrong. Do your own
research and consider your own risk tolerance.
