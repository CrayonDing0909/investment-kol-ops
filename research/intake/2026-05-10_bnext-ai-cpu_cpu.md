---
workflow: investment-analysis
artifact_type: intake-note
risk: low
created_at: 2026-05-10
source_type: news
source_id: bnext-ai-cpu-2026
source_url: https://www.bnext.com.tw/article/90464/ai-cpu
themes: [cpu]
status: draft
---

# Intake Note: 數位時代 — 人人搶 GPU，為何 CPU 需求突然爆了？

## Source

- Type: news / explainer
- Title: 人人搶GPU，為何CPU需求突然爆了？一篇看懂AI代理時代真正的算力瓶頸
- Author / Host: 數位時代 BusinessNext
- Date: 2026-05
- Location: https://www.bnext.com.tw/article/90464/ai-cpu
- Captured At: 2026-05-10

## Themes (this intake covers)

- [x] cpu
- [ ] asic
- [ ] memory
- [ ] passive-components
- [ ] cooling
- [ ] software

## Key Claims (verbatim or near-verbatim)

- 「CPU 的光芒曾一度被 GPU 掩蓋，不過現在 CPU 成為了 AI 代理落地的關鍵。」— BusinessNext
- 「AI 代理時代，任務往往更為複雜，會被拆解為多個子任務，由多個代理同時執行。」— BusinessNext
- 「過程中可能會不斷呼叫工具、查詢資料庫、撰寫與執行程式，甚至進行多輪自我反思與修正。」— BusinessNext
- 「這些涉及任務安排、資源調度與系統互動的工作，幾乎全落在 CPU 身上。」— BusinessNext
- 「CPU 甚至可能占據整體延遲的過半比例。」— BusinessNext citing Georgia Tech + Intel research
- Original paper check: selected tool-dominated agentic workloads can spend up to 88% of E2E latency in CPU-side tool processing; public wording should stay workload-specific.
- 「算力需求比拼爆發力的短跑，轉變為重視長時間運轉效能的馬拉松。」— BusinessNext
- AMD 與 Intel 管理層都承認先前低估 CPU 需求速度與規模。— BusinessNext summary

## Numbers (with units, dates, sources)

| Number | Unit | Subject | Date / Period | Source position |
|--------|------|---------|---------------|-----------------|
| >50 | % latency | CPU share of total latency in selected agentic AI workloads | cited research | BusinessNext citing Georgia Tech + Intel |
| up to 88 | % latency | CPU-side tool processing share in selected tool-dominated workloads | original paper | Georgia Tech / Intel |
| 10+ | agents | simultaneous long-running agents example | article example | BusinessNext |
| 2026 | year | server CPU market double-digit growth cited by AMD | 2026 | BusinessNext summary |

## Names Mentioned

- Companies / Tickers: Arm, Intel, AMD, NVIDIA, OpenAI, Anthropic
- People: Rene Haas, Andrej Karpathy, Boris Cherny, Lisa Su, David Zinsner
- Products / Technologies: agentic AI, AutoResearch, Claude Code agents, Vera CPU, GPU, CPU

## My Initial Reaction (HUMAN-WRITTEN)

<TODO: 你親手寫 1-3 句。提示：這篇文章的好處是把「CPU 為什麼不是過氣」講成一般人能懂的任務調度問題。>

## Open Questions (HUMAN-WRITTEN)

- <TODO: 你親手寫>
- <TODO: 你親手寫>
- <TODO: 你親手寫>

## Quotes Worth Reusing

- 「AI 代理需要長時間作業，甚至同時啟動多個任務流程。」— BusinessNext
- 「真正影響 AI 能否落地的，則是一度遭到忽視，如今再次變得不可或缺的 CPU。」— BusinessNext
- 「算力需求比拼爆發力的短跑，轉變為重視長時間運轉效能的馬拉松。」— BusinessNext

## Linked Outputs

- Source packet: [research/sources/ai-server-supply-chain/news/2026-05-10_bnext-ai-cpu-source-packet.md](../sources/ai-server-supply-chain/news/2026-05-10_bnext-ai-cpu-source-packet.md)
- Q&A HTML page: [research/knowledge/ai-server-supply-chain/cpu-qa.html](../knowledge/ai-server-supply-chain/cpu-qa.html)
- Knowledge page updated: [research/knowledge/ai-server-supply-chain/cpu.html](../knowledge/ai-server-supply-chain/cpu.html)
