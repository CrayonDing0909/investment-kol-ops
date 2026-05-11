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

# AI server 資金從 GPU 外溢後，市場到底在買什麼？

> Internal draft. Not public-ready.
>
> 這篇是 M2 internal article draft，目標是把 M1 的 research baseline 轉成可讀文章。
> 它仍不適合公開，因為 AMD >50% server CPU share target、MediaTek AI ASIC $2B Q4 2026 等關鍵 claim 還需要 primary source hardening。

## Hook

如果只看 GPU，最近很多 AI server 供應鏈的討論其實會看起來很亂。

今天有人講 CPU，明天有人講 ASIC，接著又變成 HBM、散熱、被動元件。第一反應很容易是：這是不是只是資金在找還沒漲的東西？

我現在比較傾向先不要這樣看。

比較有用的問法應該是：

> 當 GPU 已經是共識之後，AI server 裡下一個會被重新定價的瓶頸是什麼？

## Context

我會先把這題理解成一個系統瓶頸問題，而不是單一晶片問題。

AI server 當然需要 GPU / accelerator，但一台 server 不是把 GPU 插上去就結束。比較完整的地圖大概長這樣：

```text
accelerator → host CPU → memory / networking → power / cooling → server OEM
```

GPU 仍然是最核心的算力零件。只是如果 AI capex 繼續往上，投資人遲早會問第二層問題：除了 GPU，還有哪些零件會因為整套系統變大、變複雜而重新變重要？

這就是我會把 CPU、ASIC、HBM、散熱和被動元件放進同一張圖裡看的原因。它們不是同一種投資機會，但都跟「AI server 不只是 GPU」這個框架有關。

## Main Thesis

我的初步 thesis 是：

> AI server 的研究框架，正在從「GPU 供不應求」擴成「整套系統哪裡會卡住」。在目前看過的 source 裡，CPU 是第一個比較有財報與管理層語言支撐的外溢方向；ASIC 是下一條需要深入驗證的主線；被動元件與散熱比較像還在等 catalyst 的台股支線。

這不是說 GPU 不重要。

而是說：當 GPU 重要性已經變成共識，我更想找的是那些原本被視為配角、但 AI server 沒有它也跑不順的環節。

## Framework：AI server 不是只有 GPU

我原本也直覺覺得，AI server 的重點應該就是 GPU / ASIC。CPU 聽起來比較像上一個時代的東西。

但讀完 AMD、Intel 和 BusinessNext 之後，我覺得 CPU 的角色要重看。

GPU / ASIC 負責 tensor compute，這沒問題。

但 agentic AI 不只是「問一句，模型答一句」。它會拆任務、呼叫工具、查資料庫、寫程式、執行程式、多輪修正，甚至長時間跑多個 agent。

這些事情比較像系統調度，而不是單純做 matrix multiplication。

所以 CPU 的角色不是「跟 GPU 搶主要算力」。它比較像讓整套 AI workflow 可以被餵資料、被排程、被管理、被接到外部系統的那一層。

用工程一點的說法：GPU / ASIC 是把特定運算做很快的引擎，CPU 則更像整台機器的調度器。引擎再強，如果資料餵不進去、任務排不好、外部系統接不起來，整體 throughput 還是會被卡住。

## Evidence：目前 source-backed 的部分

### AMD：目前最乾淨的 CPU revival source

AMD Q1 2026 的資料最能支撐這條 thesis。

- Total revenue: `$10.253B`, +38% YoY
- Data Center revenue: `$5.8B`, +57% YoY
- Data Center 成長由 EPYC processor demand 和 Instinct GPU ramp 驅動
- AMD 說 inferencing / agentic AI 會增加 server CPU compute demand
- AMD 把 server CPU TAM 上修到 `>$120B by 2030`，CAGR `>35%`

這裡有一個重要修正：

EP659 裡提到的「120B」不能寫成 AMD 2026 revenue。source-backed 的版本是：

```text
server CPU TAM > $120B by 2030
```

這個修正很重要，因為它把「公司營收」和「市場規模」分清楚。

### Intel：CPU 是 AI stack 的 control plane，但公司線要分開看

Intel 的價值不是證明它已經打贏 AMD，而是提供另一個角度：

> CPU 是 AI stack 的 orchestration layer / critical control plane。

Intel Q1 2026：

- Total revenue: `$13.6B`, +7% YoY
- DCAI revenue: `$5.1B`, +22% YoY
- Xeon 6 被選為 NVIDIA DGX Rubin NVL8 host CPU
- Intel 也提到 ASIC revenue QoQ +30%、YoY nearly doubled

這說明 CPU 復興不是只有 AMD 單方面在講。Intel 也在用類似語言重新定義 CPU 在 AI system 裡的位置。

但我會把 Intel 視為防守 / 修復線，而不是最強攻擊線。CPU 敘事變好，不等於 Intel 這家公司所有問題都解決。Foundry、18A ramp、成本壓力還是要分開看。

### MediaTek：不要把 ASIC / subsystem 誤讀成 CPU 主晶片

聯發科比較微妙。

從 source 看，MediaTek 的 data center story 更像：

```text
AI ASIC + I/O / memory subsystem + high-speed interconnect + custom HBM optionality
```

不是 server CPU main silicon story。

目前比較有吸引力的數字是 secondary source 提到的：

- AI ASIC revenue target: `~$2B in Q4 2026`
- Cloud ASIC TAM: `$70B-$80B in 2027`
- Cloud ASIC share target: `10%-15%`

但這些還不能公開寫死，因為目前主要來自 Alpha Spread / Futurum summary，還需要 MediaTek official transcript / presentation 驗證。

所以我暫時會把聯發科歸類成：

```text
data center ASIC / subsystem optionality
```

而不是：

```text
CPU 主晶片受惠股
```

## What I Think

我目前會把 CPU revival 當成一條可以繼續追的 thesis，但不是「CPU 取代 GPU」。

更準確地說，AI server spend 如果繼續擴張，研究重點會從單一 accelerator 擴到整個系統架構。AMD 的 source 最有說服力，因為它已經在 Data Center revenue、EPYC demand、server CPU TAM 上修裡看到比較直接的證據。

Intel 的說法也重要，但我會把它視為修復線，而不是主攻線。MediaTek 我暫時不會把它當 CPU 主晶片故事，而是 ASIC / subsystem optionality；它最大的風險是市場把「未來可能性」提前 price in。

所以我的行動不是直接把這條當成買進理由，而是先建立觀察清單：

| Company / line | 我會看什麼 | 目前定位 |
| --- | --- | --- |
| AMD | Data Center revenue、EPYC demand、server CPU TAM comment | 最乾淨的 CPU revival 主線 |
| Intel | DCAI growth、Xeon design wins、control plane 敘事能不能轉成收入 | 修復線 / 驗證線 |
| MediaTek | 官方 transcript 是否支持 AI ASIC revenue target、data center project ramp | ASIC / subsystem optionality |

這題對中文投資者最有價值的 insight 不是「去買 CPU 股」，而是：

> AI server 不是只有 GPU。當 workload 從 chatbot 往 agentic AI 走，系統瓶頸可能會從單一算力，慢慢擴散到 CPU 調度、custom silicon、memory、power、cooling。

## What Would Change My Mind

1. 如果 AMD 下一份季報 Data Center revenue 或 server CPU growth 明顯低於 guidance，且管理層下修 server CPU demand，我會降低 CPU 復興 thesis 的信心。
2. 如果 Intel 下一份季報 DCAI / Xeon design wins 無法延續，或 CPU control plane 敘事沒有轉成收入，我會把 Intel 從修復線降級成純敘事。
3. 如果 MediaTek 官方 transcript 無法支持 AI ASIC `$2B Q4 2026` / data center project ramp，或明確顯示目前只停在低毛利 subsystem，我會把台廠 AI server optionality 降級。

## What Still Needs Verification Before Public

這篇不能直接公開，原因很明確：

- AMD `>50% server CPU share target` 還需要 primary source。
- MediaTek `AI ASIC $2B Q4 2026` 仍是 secondary source，需要 official transcript / presentation。
- scenario-analyzer / data-quality-checker 還沒有 real invocation。
- BusinessNext 提到 CPU latency 可能超過 50%，需要找到 Georgia Tech + Intel 原始 paper。

## Reader Takeaway

如果要把這篇變成公開文章，我希望讀者帶走的不是「快去買 CPU 股」。

而是：

```text
AI server 的研究，不應該只停在 GPU。
下一階段更值得問的是：整套系統變大以後，哪個環節會從配角變成瓶頸？
```

這才是我會把 CPU、ASIC、被動元件、散熱重新放回研究清單的原因。

## Draft Review Checklist

- [x] Hook is specific.
- [x] Reader pain is clear: 不知道 GPU 以外市場在買什麼。
- [x] Analysis is framed as research, not advice.
- [x] Uncertainty and invalidation are included.
- [ ] Public-ready source verification is complete.
- [ ] Data-quality checker has run.
- [ ] Scenario-analyzer has run.
- [ ] CTA for public version is defined.

## Disclaimer

This is research and education, not financial advice. I may be wrong. Do your own research and consider your own risk tolerance.

