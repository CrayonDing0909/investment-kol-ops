---
workflow: investment-analysis
artifact_type: analysis-brief
risk: high
created_at: YYYY-MM-DD
umbrella_theme: <e.g. AI Server Supply Chain>
theme: <e.g. CPU 復興>
time_horizon: <e.g. 6-18 個月>
asset_universe:
  primary: []
  secondary: []
  ecosystem: []
intake_sources: []
knowledge_pages: []
sources_checklist: <path>
status: draft | gate-pending | gate-approved | gate-edited | gate-rejected | published
gate: IA1 | IA1+IA2
gate_decision_log: <path>
---

# Analysis Brief: <theme name>

> 目的：把 structured 證據 + 你的個人 POV 合成一份可被 review 的分析 artifact。
>
> 區塊規則：
> - **AI 可填**：Theme thesis / Drivers / Winners-Losers / Key data points。Agent 從 structured findings 填，你 review。
> - **HUMAN-WRITTEN**：What I Learned / What I Don't Understand / My POV / My Invalidation。Agent 不可代寫，floor 限制見各區塊。

## Market Question

<一句話的問題，例如：AI server 資金從 GPU 外溢後，CPU 是否重新回到核心 spend？市占與供應鏈會如何洗牌？>

## Time Horizon

<6-18 個月 / 1-3 個月 / 1-2 年>

## Asset Universe

- Primary: <main tickers, e.g. AMD, INTC, 2454.TW>
- Secondary: <connected tickers, e.g. NVDA, MRVL, TSM>
- Ecosystem: <OEM / 配套, e.g. DELL, SMCI, HPE>

---

## Theme Thesis (AI-FILLED, human-reviewed)

<One sentence thesis. Must be falsifiable, must have a time frame, must avoid certainty language.>

## Drivers (AI-FILLED, human-reviewed)

> 把 fundamental / 敘事 / catalyst 三者分開列。

### Fundamental Drivers

- <driver> — <evidence ref>

### Narrative Drivers

- <driver> — <evidence ref>

### Catalysts (next 0-6 months)

- <catalyst, expected date or trigger>

## Winners / Losers (AI-FILLED, human-reviewed)

> 規則：每家公司一句理由，並標出 confidence。不可以列出沒在 source 裡出現過的公司。

| Side | Ticker / Name | One-line reason | Confidence |
|------|---------------|-----------------|------------|
| Winner | | | known / inferred / uncertain |
| Loser | | | |

## Key Data Points (AI-FILLED, human-reviewed)

| # | Data Point | Value | Date / Period | Source | Confidence |
|---|-----------|-------|---------------|--------|------------|

---

## What I Learned (HUMAN-WRITTEN, ≥ 100 字)

> 規則：你新理解到什麼？不是 summary，是「我之前不懂、現在懂了」的具體點。
> Floor: 至少 100 字。Floor 是強制，不是上限。

<your text>

## What I Still Don't Understand (HUMAN-WRITTEN, ≥ 3 條)

> 規則：誠實列出。不丟臉。下次優先補。每條最好點到 knowledge page 的 "Questions I still have"。

- <question>
- <question>
- <question>

## My POV (HUMAN-WRITTEN, ≥ 200 字)

> 規則：你的觀點。為什麼買 / 不買 / 觀察 / 避開。允許不確定，但要明確說「我不確定」而不是空話。
> Floor: 至少 200 字。

<your text>

## My Invalidation (HUMAN-WRITTEN, exactly 3)

> 規則：3 個會讓你改變想法的具體訊號。要可被觀察、可被計數、有時間框。

1. <invalidation signal 1, observable + time-framed>
2. <invalidation signal 2>
3. <invalidation signal 3>

---

## Disclaimer

This is research and education, not financial advice. I may be wrong. Do your own
research and consider your own risk tolerance.
