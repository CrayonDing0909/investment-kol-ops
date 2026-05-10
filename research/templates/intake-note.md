---
workflow: investment-analysis
artifact_type: intake-note
risk: low
created_at: YYYY-MM-DD
source_type: podcast | earnings | research-report | news | filing | newsletter | thread
source_id: <e.g. gooeye-ep659, AMD-2026Q1-call, MS-AI-supply-chain-2026-04>
source_url: <optional, if public>
themes: [<theme-slug>, ...]      # e.g. cpu, asic, memory, passive-components, cooling, software
status: draft | reviewed
---

# Intake Note: <source title>

> 目的：把一份外部素材消化成可重用、可引用的 structured notes。一份原料一份 intake。一份 intake 可掛多個 theme。
>
> 規則：Key claims、Numbers、Names mentioned 由 agent 抽取；My initial reaction、Open questions 必須由人類親手寫。

## Source

- Type: <podcast / earnings / report / news / filing / newsletter / thread>
- Title: <full title or episode title>
- Author / Host: <e.g. 股癌 謝孟恭 / AMD CFO Jean Hu>
- Date: YYYY-MM-DD
- Location: <URL, podcast app link, or local file path>
- Captured At: YYYY-MM-DD HH:MM (when this intake was taken)

## Themes (this intake covers)

- [ ] cpu
- [ ] asic
- [ ] memory
- [ ] passive-components
- [ ] cooling
- [ ] software
- [ ] other: <slug>

## Key Claims (verbatim or near-verbatim)

> 規則：盡量保留原話，避免改寫成自己的話。每條附 attribution（誰講的）。

- "<claim>" — <attribution>
- "<claim>" — <attribution>

## Numbers (with units, dates, sources)

| Number | Unit | Subject | Date / Period | Source position |
|--------|------|---------|---------------|-----------------|
| 120 | B USD | AMD 2026 estimated revenue | 2026 full year guide | call transcript |
| +35 | % YoY | AMD revenue growth | 2026 full year | call transcript |

## Names Mentioned

- Companies / Tickers: AMD, INTC, 2454.TW, ...
- People: ...
- Products / Technologies: Trainium, TPU, MI300X, ...

## My Initial Reaction (HUMAN-WRITTEN)

> 規則：1-3 句你看到當下的真實反應。不要美化、不要 LLM 風格。
>
> 範例：「CPU 我之前覺得早就被 GPU 邊緣化了，這集才知道 AI server 對 CPU 的需求其實在 reaccelerate。聯發科漲停我有跟到一段，但不知道接下來的故事是什麼。」

<your reaction here>

## Open Questions (HUMAN-WRITTEN)

> 規則：列出你聽完還不懂的東西。這些會被 Knowledge Architecture Agent 接走，產出 tutor-style 解釋。
>
> 範例：
> - ASIC 跟 GPU 的 use case 差在哪？
> - 為什麼資金會從 GPU 轉到 ASIC？是估值還是供應鏈？
> - 「I/O、memory 還沒打入主晶片」這句什麼意思？

- <question>
- <question>
- <question>

## Quotes Worth Reusing

> 規則：當這份 intake 之後被引用到 brief 或 article 時，這裡是直接可拿來貼的句子。

- "<quote>" — <source position>

## Linked Outputs

- Knowledge pages updated: [research/knowledge/<theme>/<topic>.html](../knowledge/...)
- Briefs that cite this intake: [research/notes/<...>.md](../notes/...)
