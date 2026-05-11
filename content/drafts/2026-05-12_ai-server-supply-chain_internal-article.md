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

過去一年，AI 交易幾乎等於 GPU 交易。

但最近市場開始出現一個變化：資金不再只買 GPU，而是開始找下一批 AI server spend 的外溢方向。

這些方向看起來很散：CPU、ASIC、HBM、被動元件、散熱、甚至被殺過的軟體股。

問題是：這些東西真的有關係嗎？還是只是資金在亂輪動？

## Context

我會先把這題理解成一個 supply chain 問題，而不是單一個股問題。

AI server 不只是 GPU。真正的 AI infrastructure 是一整套系統：

```text
compute → memory → server OEM → power / cooling → software
```

GPU 仍然是最核心的算力零件，但當市場開始接受 AI capex 不會只集中在 GPU，資金就會開始尋找下一個瓶頸。

這就是 CPU、ASIC、被動元件、散熱、HBM 最近會被重新討論的原因。

## Main Thesis

我的初步 thesis 是：

> AI server 的投資機會正在從「單一 GPU 敘事」擴散到「整個系統瓶頸敘事」。CPU 是第一個可以被財報與管理層語言支撐的外溢方向；ASIC 是下一個需要深入驗證的主線；被動元件與散熱則更像等待 catalyst 的台股支線。

這不是說 GPU 不重要。

而是說：當所有人都知道 GPU 重要時，超額報酬可能開始出現在那些「原本被忽略，但 AI server 沒有它們也跑不起來」的環節。

## Framework：AI server 不是只有 GPU

我原本也直覺覺得，AI server 的重點應該就是 GPU / ASIC。

但讀完 AMD、Intel 和 BusinessNext 之後，我覺得 CPU 的角色要重看。

GPU / ASIC 負責 tensor compute，這沒問題。

但 agentic AI 不再只是「問一句，模型答一句」。它會拆任務、呼叫工具、查資料庫、寫程式、執行程式、多輪修正，甚至長時間運行多個 agent。

這些事情更像 system orchestration，而不是單純 matrix multiplication。

所以 CPU 的角色不是「跟 GPU 搶主要算力」，而是讓整套 AI workflow 跑得動。

用 BusinessNext 那篇文章的比喻延伸來說，GPU / ASIC 像廚師，CPU 像廚房領班。廚師再強，如果訂單拆解、食材調度、任務安排都亂掉，整間廚房還是跑不起來。

## Evidence：目前 source-backed 的部分

### AMD：目前最乾淨的 CPU 復興 source

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

### Intel：CPU 是 AI stack 的 control plane

Intel 的價值不是證明它已經打贏 AMD，而是提供另一個角度：

> CPU 是 AI stack 的 orchestration layer / critical control plane。

Intel Q1 2026：

- Total revenue: `$13.6B`, +7% YoY
- DCAI revenue: `$5.1B`, +22% YoY
- Xeon 6 被選為 NVIDIA DGX Rubin NVL8 host CPU
- Intel 也提到 ASIC revenue QoQ +30%、YoY nearly doubled

這說明 CPU 復興不是只有 AMD 單方面在講。Intel 也在用類似語言重新定義 CPU 在 AI system 裡的位置。

但我會把 Intel 視為防守 / 修復線，而不是最強攻擊線。因為它還有 Foundry、18A ramp、成本壓力等問題。

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

我目前相信 CPU 復興這條 thesis 有成立，但我不會把它理解成 CPU 取代 GPU。

更準確地說，AI server spend 正在從 GPU 擴散到整個系統架構。AMD 的 source 最有說服力，因為它已經在 Data Center revenue、EPYC demand、server CPU TAM 上修裡看到財報證據。Intel 的說法也重要，但我會把它視為防守與修復線，而不是最強攻擊線。

如果只能先研究一檔，我會先看 AMD，因為它同時有 CPU 和 accelerator exposure，而且 thesis 比較 source-backed。Intel 我會觀察 DCAI 和 Xeon design wins 是否延續。MediaTek 我暫時不會把它當 CPU 主晶片故事，而是 ASIC / subsystem optionality；它最大的風險是市場把「未來可能性」提前 price in。

所以我的行動會是先建立觀察清單，不急著把這條當成買進理由。

我會等 AMD 下一份法說確認 server CPU growth 是否延續，也會等 MediaTek 官方 transcript 確認 AI ASIC revenue 的說法。這題對中文投資者最有價值的 insight 是：

> AI server 不是只有 GPU，真正的投資機會可能來自資金開始理解整個系統瓶頸。

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
AI server 的投資機會，不應該只看 GPU。
當工作負載從 chatbot 走向 agentic AI，整個系統瓶頸會從單一算力，擴散到 orchestration、custom silicon、memory、power、cooling。
```

這才是 CPU / ASIC / 被動元件 / 散熱重新被討論的底層原因。

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

