---
workflow: investment-analysis
artifact_type: source-packet
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
company: BusinessNext
ticker: n/a
source_class: news
source_quality: secondary
status: draft
---

# Source Packet: BusinessNext — 人人搶 GPU，為何 CPU 需求突然爆了？

## Source Metadata

- Company: BusinessNext / 數位時代
- Ticker: n/a
- Source class: news
- Source quality: secondary
- Title: 人人搶GPU，為何CPU需求突然爆了？一篇看懂AI代理時代真正的算力瓶頸
- Publisher: 數位時代 BusinessNext
- Date published: 2026-05
- URL: https://www.bnext.com.tw/article/90464/ai-cpu
- Captured at: 2026-05-10

## Why This Source Matters

This is a strong Chinese-language explainer for why CPU demand matters in the
agentic AI era. It is especially useful for the Tutor/Q&A layer because it
explains the CPU story in language close to the target audience.

## Raw Facts

- The article argues CPU was overshadowed by GPU during the first AI wave, but is becoming key as AI agents move toward real-world task execution.
- Arm CEO Rene Haas is quoted saying people think CPU is outdated, but AI development needs more CPUs, a lot more CPUs.
- The article says chatbot-era AI was simpler: user input, CPU preprocessing, GPU inference, response. Compute gravity was centered on GPU.
- Agentic AI splits work into multiple subtasks, multiple agents, tool calls, database queries, code writing/execution, and self-reflection loops; these scheduling and system-interaction tasks mostly fall on CPUs.
- The article cites Georgia Tech + Intel research saying CPU can account for more than half of total latency in agentic AI workloads.
- The article frames the shift as going from bursty sprint-style compute to long-running marathon-style compute.
- Examples cited: Karpathy's AutoResearch running overnight or longer; Boris Cherny using multiple Claude Code agents simultaneously.
- AMD CEO Lisa Su is cited saying CPU business growth exceeded expectations and 2026 server CPU market could grow double digits.
- Intel CFO David Zinsner is cited saying CPU is hot again this year.
- The article says CPU becomes the system hub: deciding when to call models, how to allocate tasks, and how to interact with the outside world.
- NVIDIA is also strengthening its own CPU products, including Vera CPU for AI agent workloads.

## Key Numbers

| Number | Unit | Metric | Period | Source wording |
|--------|------|--------|--------|----------------|
| >50 | % latency | CPU share of total latency in agentic AI workloads | cited research | CPU 甚至可能占據整體延遲的過半比例 |
| 10+ | agents | simultaneous long-running agents example | article example | 可能同時運行超過10個 AI 代理 |
| 2026 | year | server CPU market growth cited by AMD | article summary | 2026 年伺服器 CPU 市場有兩位數成長 |

## Direct Quotes

- 「人們認為CPU已經過時了。」— Arm CEO Rene Haas, quoted by BusinessNext.
- 「隨著AI技術快速發展，我們需要愈來愈多CPU，大量的CPU。」— Rene Haas, quoted by BusinessNext.
- 「這些涉及任務安排、資源調度與系統互動的工作，幾乎全落在CPU身上。」— BusinessNext.
- 「CPU甚至可能占據整體延遲的過半比例，成為真正影響效率的關鍵環節。」— BusinessNext citing Georgia Tech + Intel research.
- 「算力需求比拼爆發力的短跑，轉變為重視長時間運轉效能的馬拉松。」— BusinessNext.

## Source Reliability Notes

- This is a secondary explanatory article, not a company primary source.
- Strong for Chinese-language framing and mental model.
- Weak for primary financial claims; company growth numbers should still come from AMD / Intel IR materials.
- The Georgia Tech + Intel research is cited but not directly linked to the paper in this packet; a future source packet should collect the original paper if this claim is used publicly.

## Follow-up Needed

- Find the original Georgia Tech + Intel paper on CPU latency in agentic AI workloads.
- Verify AMD / Intel quoted comments from primary earnings or public talk sources.
- If using the Vera CPU point publicly, link the NVIDIA source directly.

## Linked Artifacts

- Intake note: `research/intake/2026-05-10_bnext-ai-cpu_cpu.md`
- Q&A HTML page: `research/knowledge/ai-server-supply-chain/cpu-qa.html`
- Knowledge page updated: `research/knowledge/ai-server-supply-chain/cpu.html`
