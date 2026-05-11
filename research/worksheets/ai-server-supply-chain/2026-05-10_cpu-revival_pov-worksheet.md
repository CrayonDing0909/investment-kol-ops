---
workflow: investment-analysis
artifact_type: pov-worksheet
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
topic: cpu-revival
status: synced-to-brief
target_brief: research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md
target_gate: ops/decisions/2026-05-10_ia1_cpu-deep-dive.md
---

# POV Worksheet: CPU 復興

> 目的：這不是正式文章，也不是要寫漂亮。這是你讀完 HTML 後，把自己的理解和觀點寫出來的草稿。
>
> 使用方式：
> 1. 先照閱讀順序讀 HTML。
> 2. 每題用短句回答即可。
> 3. 不確定就寫「我不確定」。
> 4. 寫完後，agent 才會幫你 sharpen，整理進正式 brief。

## Reading Order

1. `research/knowledge/ai-server-supply-chain/index.html`
2. `research/knowledge/ai-server-supply-chain/sources.html`
3. `research/knowledge/ai-server-supply-chain/qa.html`
4. `research/knowledge/ai-server-supply-chain/cpu-qa.html`
5. `research/knowledge/ai-server-supply-chain/cpu.html`
6. `research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md`

## 1. What I Learned

> 至少 100 字。寫「我原本不知道 / 現在知道」的東西，不要摘要全文。

Prompt:

- 我以前怎麼理解 CPU 在 AI server 裡的角色？
- 讀完後哪個 mental model 改變了？
- AMD / Intel / BusinessNext 哪個 source 最改變我的理解？
- 哪個數字最重要？

Draft:

```text
我原本以為 CPU 在 AI server 裡只是配角，真正重要的是 GPU / ASIC。
但讀完 AMD、Intel 和 BusinessNext 後，我比較理解 CPU 的角色不是負責主要算力，
而是負責 orchestration / control plane。尤其 agentic AI 從單次問答變成多步驟任務，
會需要更多資料搬運、工具呼叫、排程、程式執行和長時間運行，這些不是 GPU 擅長的部分。

所以 CPU 復興不是「CPU 取代 GPU」，而是 AI server spend 從單一 GPU 敘事擴散到整個系統架構。
AMD 的 Data Center revenue、EPYC demand、server CPU TAM 上修，是目前最直接的財報證據。
Intel 的說法則讓我理解，CPU 也可以被重新定義為 AI stack 的 control plane，
不是過去那種單純通用運算的老故事。
```

## 2. What I Still Don't Understand

> 至少 3 條。這些不是缺點，是下次研究方向。

Prompt:

- 哪些技術名詞我還沒真的懂？
- 哪些 claim 我覺得 source 還不夠？
- 哪些公司 / 供應鏈關係我還無法說清楚？

Draft:

```text
1. 我還不確定 AMD 的 server CPU TAM >120B by 2030，市場目前到底 price in 多少。
2. 我還不懂 CPU demand 是因為 attach rate 上升、server units 上升，還是 utilization 上升。
3. 我還不確定 Intel 的 CPU control plane 說法，是實際競爭力回來，還是公司在重塑敘事。
4. 我不確定 MediaTek 到底是 ASIC story、I/O / memory subsystem story，還是市場把兩者混在一起炒。
5. 我還需要找 AMD Analyst Day 的 primary source 來驗證 >50% server CPU share target。
```

## 3. My POV

> 至少 200 字。這是最重要的部分。不是 summary，是你的立場。

你可以從下面 6 題挑 3-4 題回答：

1. 我相信「CPU 復興」這條 thesis 嗎？為什麼？
2. 我覺得市場已經 price in 了什麼？還沒 price in 什麼？
3. 如果只能選 AMD / Intel / MediaTek 其中一個，我會先研究誰？為什麼？
4. MediaTek 這條線我覺得是 CPU、ASIC、還是 subsystem story？
5. 我會現在買、等 catalyst、還是避開？為什麼？
6. 我覺得這題對中文投資者最有價值的 insight 是什麼？

Draft:

```text
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
```

## 4. My Invalidation

> exactly 3 條。必須可觀察、可驗證、有時間框。

候選可改：

1. AMD 下一份季報若 Data Center / server CPU growth 明顯低於 guidance，CPU thesis 降級。
2. Intel 下一份季報若 DCAI / Xeon design wins 無法延續，CPU 作為 control plane 的修復線降級。
3. MediaTek 官方 transcript 若無法支持 AI ASIC $2B / Q4 2026 或 data center project ramp，台廠 AI server optionality 降級。

Draft:

```text
1. 如果 AMD 下一份季報 Data Center revenue 或 server CPU growth 明顯低於 guidance，且管理層下修 server CPU demand，我會降低 CPU 復興 thesis 的信心。
2. 如果 Intel 下一份季報 DCAI / Xeon design wins 無法延續，或 CPU control plane 敘事沒有轉成收入，我會把 Intel 從修復線降級成純敘事。
3. 如果 MediaTek 官方 transcript 無法支持 AI ASIC $2B Q4 2026 / data center project ramp，或明確顯示目前只停在低毛利 subsystem，我會把台廠 AI server optionality 降級。
```

## 5. IA1 Reflection

> 這三題會寫回 `ops/decisions/2026-05-10_ia1_cpu-deep-dive.md`。

### Weakest point if challenged publicly

如果這份 thesis 被股癌粉絲或懂產業的人質疑，最弱的點在哪？

```text
最弱的點是我目前對 AMD >50% server CPU share target 還沒有 primary source，
而且 MediaTek 的 AI ASIC 數字還是 secondary source。若公開發文，
這兩點會被懂產業的人挑戰。另外，CPU demand 是 structural 還是短期補貨，
目前也還需要更多 architecture / financial data 才能說死。
```

### Best skill / step in this run

這次 source / Q&A / HTML knowledge / brief 裡，哪一步最幫助你理解？

```text
最有幫助的是 HTML Q&A 和 source reading view，因為它讓我把 CPU 重新重要這件事
從口號變成一個可理解的系統架構問題。BusinessNext 的文章讓我用中文理解
agentic AI 為什麼會增加 CPU orchestration demand；AMD / Intel source packets
則提供財報與管理層語言來支撐這個 mental model。
```

### What to improve next time

下一個你最想補的 theme 是什麼？ASIC / memory / passive / cooling / software？為什麼？

```text
下一個我想補 ASIC，因為 CPU 和 ASIC 是這條 AI server spend 外溢敘事的兩個主軸。
MediaTek / 世芯 / 創意都需要先理解 ASIC 才能判斷，而且現在 ASIC 的 source quality
還不夠好，尤其 MediaTek 的 $2B Q4 AI ASIC revenue 仍是 secondary source，
需要 official transcript 或更強的 primary source 來驗證。
```

## 6. Agent Review Checklist

> 你填完後，agent 用這段檢查，不會替你重寫成 AI 口吻。

- [ ] My POV 是否至少 200 字？
- [ ] 是否有明確立場，而不是 summary？
- [ ] 是否有引用 source-backed 事實？
- [ ] 是否有承認不確定性？
- [ ] Invalidation 是否 exactly 3 條？
- [ ] Invalidation 是否具體可觀察？
- [ ] 有沒有像 AI 代寫的句子？如果有，改回你的口吻。


## Synced To Brief

2026-05-12: Agent-seeded draft accepted by user for workflow continuity and synced to `research/notes/2026-05-10_ai-server-supply-chain_cpu-revival.md`. IA1 updated to internal-only approve.
