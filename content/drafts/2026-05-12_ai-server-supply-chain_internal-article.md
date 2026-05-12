---
workflow: content-production
artifact_type: internal-article-draft
risk: high
created_at: 2026-05-12
source_brief: research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md
source_decision: ops/decisions/2026-05-10_ia1_cpu-deep-dive.md
status: internal-draft
public_status: not-public-ready
target_audience: 中文投資者 / 想理解 AI supply chain 但不想只聽口號的人
content_pillar: market-understanding
---

# 最近整理 AI server 相關族群，先拆出的幾條支線

> Internal draft. Not public-ready.
>
> 這篇是 M2 internal article draft，目標是把 M1 的 research baseline 先轉成比較像我的研究口語稿。
> 它仍不適合公開，因為 HBM / 散熱 / 被動元件支線還沒有 source-backed 深挖，scenario-analyzer 也還沒有 real invocation。

## 先記一下目前的想法

最近整理 AI server 相關族群的整體敘事架構，感覺大概有幾條支線。

所以這篇比較像是先把腦中的地圖攤開來看，順一下自己到底在看哪幾條故事。

之前很容易把這些東西全部塞進一句「GPU 外溢」。但我現在覺得這樣講有點太粗，因為就我的理解 CPU、ASIC、HBM、散熱、被動元件背後的原因應該不太一樣才對。

如果真的要拆，我目前會先拆成三條：

```text
CPU：比較像 agent AI / agentic workflow 把調度需求拉起來。
ASIC：比較像 hyperscaler 想要 custom compute、成本、功耗和自主性。
HBM / 散熱 / 被動元件：比較像算力基建越蓋越大後，物理瓶頸被逼出來。
```

這三條不一定會同時成立，也不一定會用同一個速度反映到股價或財報。

所以我現在想做的不是直接「哪個要買」，而是能夠把這幾條支線拆清楚，之後再一條一條補 source。能夠讓我了解自己到底在買什麼故事或敘事，也可以讓自己抱得比較安心 XD

## 第一條：CPU 這條我目前比較能理解

CPU 這條，我目前比較能理解。

如果 agent AI 真的開始跑起來，任務拆解、工具呼叫、資料庫查詢、寫程式、執行程式、多輪修正、長時間運行，這些東西確實不像是 GPU 自己能全部解決的。

GPU / ASIC 還是負責主要算力，但 CPU 比較像讓整套系統可以被餵資料、被排程、被管理、被接到外部系統的那一層。

這也是 BusinessNext 那篇文章給我的啟發：它不是在講 CPU 要取代 GPU，而是在講 AI workload 變複雜以後，CPU 原本擅長的部分又被發現了，像是順序性的任務可以去拆解任務、安排流程、調度工具等等。

但這裡我也會小心。

CPU 需求是不是真的會這樣放大，還是需要更多財報和法說去確認（目前看起來是，這是前幾天打的，我懶得改了）。現在只能說：這條支線目前相對有 source 可以先支撐。

## CPU 目前比較 source-backed 的部分

AMD Q1 2026 的資料，是目前我覺得最乾淨的 CPU source。

- Total revenue: `$10.253B`, +38% YoY
- Data Center revenue: `$5.8B`, +57% YoY
- Data Center 成長由 EPYC processor demand 和 Instinct GPU ramp 驅動
- AMD 說 inferencing / agentic AI 會增加 server CPU compute demand
- AMD 把 server CPU TAM 上修到 `>$120B by 2030`，CAGR `>35%`

這裡有一個重要修正。

EP659 裡提到的「120B」不能寫成 AMD 2026 revenue。source-backed 的版本是：

```text
server CPU TAM > $120B by 2030
```

這個修正很重要，因為它把「公司營收」和「市場規模」分清楚。

Intel 也提供另一個角度：

> CPU 是 AI stack 的 orchestration layer / critical control plane

Intel Q1 2026：

- Total revenue: `$13.6B`, +7% YoY
- DCAI revenue: `$5.1B`, +22% YoY
- Xeon 6 被選為 NVIDIA DGX Rubin NVL8 host CPU
- Intel 也提到 ASIC revenue QoQ +30%、YoY nearly doubled

我會把 Intel 先放在修復線 / 驗證線。CPU 敘事變好，不等於 Intel 這家公司所有問題都解決。Foundry、18A ramp、成本壓力還是要分開看。

## 第二條：ASIC / MediaTek 這條還需要小心

ASIC 這條我覺得是另一個故事。

它不是 CPU，也不只是 GPU 外溢，比較像 hyperscaler 想要更便宜、更省電、更客製化，而且不要所有東西都被單一 GPU 供應鏈卡住。

聯發科這邊比較微妙。

從 source 看，MediaTek 的 data center story 更像：

```text
AI ASIC + I/O / memory subsystem + high-speed interconnect + custom HBM optionality
```

不是 server CPU main silicon story。

目前比較有吸引力的數字，是 secondary source 提到的：

- AI ASIC revenue target: `~$2B in Q4 2026`
- Cloud ASIC TAM: `$70B-$80B in 2027`
- Cloud ASIC share target: `10%-15%`

這個 `$2B Q4 2026` 數字現在已經對到 MediaTek 官方 transcript，但還是要寫成 management expectation，不是已經實現的營收。

所以我暫時不會把聯發科寫成「CPU 主晶片受惠股」。

我會先把它放在：

```text
data center ASIC / subsystem optionality
```

而不是：

```text
CPU 主晶片受惠股
```

## 第三條：HBM / 散熱 / 被動元件還沒補完

HBM、散熱、被動元件這條，我目前還沒有補完。

但我想像中，它們應該不是 agent AI 直接帶出來的需求。

它們比較像是 AI 算力基建越蓋越大之後，memory、power、thermal 這些物理瓶頸被放大。

這條跟 CPU 不太一樣。

CPU 比較像 workload 變複雜後的調度需求；HBM、散熱、被動元件比較像硬體基建擴張後，整套 server 的供電、散熱、記憶體頻寬都被逼到更高規格。

但這邊我還不能寫太滿。比較合理的做法是先放觀察清單，之後再去補：

- HBM：到底是供給限制、價格循環，還是 AI server BOM 持續上修？
- 散熱：是單一設計變動，還是整體 heat density 上升的長線需求？
- 被動元件：是原物料 / 漲價題材，還是真的有高階料缺貨和 lead time 拉長？

## 目前先做成假設地圖

這篇現在最重要的是不要把還沒驗證的東西寫成結論。

所以我先把它整理成這張表：


| 支線   | 我目前怎麼想                                             | 目前狀態                                           | 下一步要看什麼                                             |
| ---- | -------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------- |
| CPU  | 比較像 agent AI / agentic workflow 讓調度需求被重新看見         | AMD / Intel 有初步 source                         | AMD server CPU growth、Intel DCAI / Xeon design wins |
| ASIC | 比較像 hyperscaler 的 custom compute / 成本 / 功耗 / 自主性需求 | `$2B Q4 2026` 已對到官方 transcript，但仍是 expectation | customer / project ramp、後續營收驗證                      |
| HBM  | 比較像算力基建擴張後的 memory bottleneck                      | 這篇還沒補 source                                   | 報價、供需、capex、AI server BOM                           |
| 散熱   | 比較像 heat density 上升後的 thermal bottleneck           | 這篇還沒補 source                                   | 產品設計變化、客戶拉貨、營收驗證                                    |
| 被動元件 | 可能是高階料缺貨 / lead time / 原物料漲價混在一起                   | 這篇還沒補 source                                   | lead time、漲價信、稼動率、法說                                |


這樣寫比較接近我現在的狀態：不是已經有答案，而是先知道接下來要驗證什麼。

## 我現在比較確定和不確定的地方

我目前比較確定的是：

1. 不能把 AI server 外溢全部當成同一個故事。
2. CPU 這條目前最容易先找到財報和管理層語言支撐。
3. MediaTek 比較像 ASIC / subsystem optionality，不應該硬寫成 CPU 主晶片。

我還不確定的是：

1. CPU 需求能不能真的從敘事轉成持續的 revenue。
2. ASIC 的數字目前有多少是市場期待，有多少已經進入 official guidance。
3. HBM、散熱、被動元件到底是短期題材，還是 AI server BOM 真的持續把它們推上去。

## What Would Change My Mind

1. 如果 AMD 下一份季報 Data Center revenue 或 server CPU growth 明顯低於 guidance，且管理層下修 server CPU demand，我會降低 CPU 復興 thesis 的信心。
2. 如果 Intel 下一份季報 DCAI / Xeon design wins 無法延續，或 CPU control plane 敘事沒有轉成收入，我會把 Intel 從修復線降級成純敘事。
3. 如果 MediaTek 官方 transcript 無法支持 AI ASIC `$2B Q4 2026` / data center project ramp，或明確顯示目前只停在低毛利 subsystem，我會把台廠 AI server optionality 降級。

## What Still Needs Verification Before Public

這篇不能直接公開，原因還是很明確：

- AMD `>50% server CPU revenue market share` 已找到 AMD Financial Analyst Day primary source，但只能寫成 forward-looking target，不能寫成目前市占。
- MediaTek `AI ASIC $2B Q4 2026` 已找到官方 transcript，但要寫成 management expectation，不是已實現營收。
- BusinessNext 提到 CPU latency 的原始 paper 已找到；公開時要用 workload-specific 說法，例如 selected tool-dominated workloads up to 88%，不能寫成所有 agentic AI 都是 CPU latency >50%。
- data-quality-checker 已跑過，報告 0 findings；scenario-analyzer 還沒有 real invocation。
- HBM / 散熱 / 被動元件支線還沒有 source-backed 深挖，不能跟 CPU 寫成同一個確定結論。

## 先收在這裡

如果要把這篇變成公開文章，我希望它不要變成「AI server 不只 GPU，所以大家去買下一個零件」。

比較想寫的是：

```text
我最近整理 AI server 相關族群，發現它不是一條線。
CPU、ASIC、HBM、散熱、被動元件背後可能是不同支線。
現在要做的不是急著下結論，而是先把每條線的驗證點拆出來。
```

這樣比較接近我目前的狀態，也比較不會把還沒驗證完的想法講得太滿。

## Draft Review Checklist

- [x] Draft starts from my current research state, not a teaching frame.
- [x] Unverified branches are labeled as hypothesis map.
- [x] Analysis is framed as research, not advice.
- [x] Uncertainty and invalidation are included.
- [ ] Public-ready source verification is complete.
- [x] Data-quality checker has run (`reports/data_quality_2026-05-12_025848.md`, 0 findings).
- [ ] Scenario-analyzer has run.
- [ ] CTA for public version is defined.

## Disclaimer

This is research and education, not financial advice. I may be wrong. Do your own research and consider your own risk tolerance.