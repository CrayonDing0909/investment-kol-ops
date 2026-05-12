---
workflow: investment-analysis
artifact_type: tutor-qa
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
topic: cpu
status: draft
---

# Q&A: CPU 在 AI server 裡還有什麼用？不是都 GPU 嗎？

## Question

CPU 在 AI server 裡還有什麼用？AI 工作負載不是都靠 GPU / ASIC 嗎？為什麼 AMD / Intel 都說 agentic AI 讓 CPU 重新重要？

## Short Answer

GPU / ASIC 負責大規模矩陣運算，但 CPU 負責「協調整台機器」：跑作業系統、處理資料搬運、I/O、前後處理、排程、以及把任務餵給加速器。當 AI 工作負載從單次訓練變成大量 inference、agentic workflow、多步驟任務，CPU 要處理的 orchestration 反而變多。AMD 和 Intel 的說法都指向同一件事：AI server 不是只有 accelerators，CPU 是 control plane。

## Mental Model

把 AI server 想成一間廚房。GPU / ASIC 是一排很猛的廚師，專門快速做菜；CPU 是廚房領班，負責接單、分工、把食材送到對的人、決定先做哪道、處理客訴。如果訂單變多、菜色變複雜，領班的重要性會上升，不會因為廚師很強就消失。

## Technical Explanation

AI 訓練和推論會用 GPU / ASIC 做主要 tensor compute，但真實系統還需要 CPU 處理 host code、資料前處理/後處理、I/O interrupt、network stack、storage access、RPC、container orchestration、scheduler、logging、model server control loop 等。Agentic AI 更像很多小任務串成 workflow，會產生更多 CPU-side coordination。這也是為什麼 AMD 說 inferencing and agentic AI 會增加 server CPU compute，Intel 說 CPU 是 orchestration layer / control plane。

## Why Investors Care

如果 CPU 只是「搭配零件」，估值敘事不強；但如果 agentic AI 真的讓每個 accelerator cluster 需要更多 CPU orchestration，那 server CPU TAM 會跟 AI capex 一起上修。這支持 AMD EPYC 的成長，也讓 Intel Xeon 有防守/修復機會。投資上要看的是：AI server 出貨是否真的帶動 EPYC / Xeon revenue，而不是只看 NVDA GPU。

## Companies / Tickers

| Company / Ticker | Role | Why it matters |
|------------------|------|----------------|
| AMD | EPYC server CPU | Q1 2026 Data Center revenue $5.8B, EPYC demand strong，server CPU TAM 上修到 >$120B by 2030。 |
| INTC | Xeon server CPU | DCAI revenue $5.1B，Xeon 6 被選為 NVIDIA DGX Rubin NVL8 host CPU。 |
| 2454.TW | I/O / memory subsystem candidate | EP659 提到目前還不是主晶片，需驗證是否能打入更核心位置。 |
| NVDA | Accelerator / system reference | DGX Rubin 使用 Intel Xeon 6 作 host CPU，說明 accelerator 還是需要 CPU。 |

## What To Watch

| Signal | Why it matters | Source to monitor |
|--------|----------------|-------------------|
| AMD server CPU revenue growth | 驗證 CPU 復興是不是財報可見 | AMD earnings / transcript |
| Intel DCAI revenue and Xeon design wins | 驗證 Intel 是否真的守住 AI control plane | Intel earnings / press release |
| Hyperscaler instance announcements | 看 AWS / GCP / Azure 是否持續擴 EPYC / Xeon instances | AMD / Intel press releases |
| NVIDIA DGX host CPU design | 看 GPU system 裡 CPU 配置是否穩定 | NVIDIA / Intel announcements |

## What I Still Don't Know

- AMD 的 >50% server CPU revenue market share target 已找到 AMD Financial Analyst Day primary source；公開時要寫成 forward-looking target，不能寫成目前市占。
- Agentic AI 到底會提高 CPU attach rate，還是只提高 server CPU utilization？這需要更細的 architecture source。
- MediaTek 的 I/O / memory subsystem 具體是什麼產品線，和 CPU control plane 的距離仍不清楚。

## Sources

- `research/sources/ai-server-supply-chain/earnings/2026-05-10_amd-q1-2026-source-packet.md`
- `research/sources/ai-server-supply-chain/earnings/2026-05-10_intel-q1-2026-source-packet.md`
- `research/sources/ai-server-supply-chain/news/2026-05-10_bnext-ai-cpu-source-packet.md`

## Update Targets

- Knowledge page to update: `research/knowledge/ai-server-supply-chain/cpu.html`
- HTML reading view: `research/knowledge/ai-server-supply-chain/cpu-qa.html`
- Brief section to update: Drivers, Key Data Points, What I Still Don't Understand
