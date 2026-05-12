---
workflow: investment-analysis
artifact_type: source-packet
risk: low
created_at: 2026-05-12
theme: ai-server-supply-chain
company: Georgia Tech / Intel
ticker: n/a
source_class: research-paper
source_quality: primary
status: draft
---

# Source Packet: Agentic AI Execution — CPU-Centric Perspective

## Source Metadata

- Title: Towards Understanding, Analyzing, and Optimizing Agentic AI Execution: A CPU-Centric Perspective
- Authors: Ritik Raj, Souvik Kundu, Ishita Vohra, Hong Wang, Tushar Krishna
- Institutions: Georgia Institute of Technology, Intel
- Source class: research paper
- Source quality: primary research paper
- URL:
  - https://arxiv.org/pdf/2511.00739
  - https://repository.gatech.edu/server/api/core/bitstreams/913bb86c-6bf1-4381-8ada-61de83960949/content
- Captured at: 2026-05-12

## Why This Source Matters

BusinessNext cited Georgia Tech + Intel research to explain why CPU can become a
latency bottleneck in agentic AI workloads. This packet verifies that claim
against the original paper instead of relying only on the BusinessNext article.

## Raw Facts

- The paper studies agentic AI execution from a CPU-centric perspective.
- Representative workloads include Toolformer, SWE-Agent, RAG, ChemCrow, and a Web-Augmented Agent.
- The experiments compare CPU/GPU systems to isolate CPU, GPU, and I/O bottlenecks.
- Tool-dominated agentic workloads can be bottlenecked by CPU-side tool processing.
- The paper says tool-dominated workloads consume up to 88% of end-to-end latency on the CPU.
- For RAG, exact nearest neighbor search consumes 83%-82% of total latency on one system and up to 89% on another.
- For Web-Augmented Agent, LexRank summarization accounts for 55% / 48% of latency on one system and 40%-45% on another.
- For SWE-Agent, Bash/Python execution accounts for 38% / 25% of latency on one system and up to 65% on another.
- The paper notes that a higher-performance GPU system can shift the bottleneck toward CPU tool execution.
- Proposed optimizations include CPU-Aware Overlapped Micro-Batching (COMB) and Mixed Agentic Scheduling (MAS).

## Key Numbers

| Number | Unit | Metric | Context | Source wording |
|--------|------|--------|---------|----------------|
| up to 88 | % E2E latency | CPU-side tool processing latency share | tool-dominated agentic workloads | "tool dominated agentic AI workloads are ... bottle-necked by tool processing on the CPU consuming up to 88% of the end-to-end latency" |
| 83-89 | % E2E latency | ENNS retrieval latency share | RAG / Haystack | "ENNS retrieval consumes up to 89% of total latency" |
| 40-55 | % E2E latency | LexRank summarization latency share | Web-Augmented Agent | "LexRank summarization tool execution accounts for 55% and 48%... 40-45%" |
| 38-65 | % E2E latency | Bash/Python execution latency share | SWE-Agent | "Bash/Python execution accounts for 38%... up to 65%" |
| 3.9 | x lower | Service latency improvement | COMB under homogeneous open-loop load | "up to 3.9x lower service latency" |
| 2.37 / 2.49 | x lower | P50 / P90 latency improvement | MAS under heterogeneous open-loop load | "up to 2.37x / 2.49x at P50/P90" |

## Direct Quotes

- "Agentic AI serving converts monolithic LLM-based inference to autonomous problem-solvers that can plan, call tools, perform reasoning, and adapt on the fly." — paper abstract.
- "The majority of the external tools responsible for agentic capability, either run on or are orchestrated by the CPU." — paper abstract.
- "Tool dominated agentic AI workloads are significantly bottle-necked by tool processing on the CPU consuming up to 88% of the end-to-end latency." — paper, contributions section.
- "HP GPU system can shift the bottleneck from GPU to CPU when tool execution latency is comparable to LLM inference latency." — paper, Key Takeaway 2.

## Source Reliability Notes

- This is a primary research source for the CPU latency / bottleneck claim.
- The headline number should be written carefully as "up to 88% in selected tool-dominated workloads," not as a universal CPU latency share for all agentic AI.
- BusinessNext's "over half" framing is directionally supported by several workloads in the paper, but the exact public wording should cite the original paper and specify workload context.

## Follow-up Needed

- Decide whether public content should cite the arXiv URL or Georgia Tech repository URL.
- If using this in a public article, avoid implying that every agentic AI workload is CPU-bound.

## Linked Artifacts

- BusinessNext source packet: `research/sources/ai-server-supply-chain/news/2026-05-10_bnext-ai-cpu-source-packet.md`
- Intake note: `research/intake/2026-05-10_bnext-ai-cpu_cpu.md`
- Knowledge page: `research/knowledge/ai-server-supply-chain/cpu.html`
