---
workflow: investment-analysis
artifact_type: tutor-qa
risk: low
created_at: 2026-05-10
theme: ai-server-supply-chain
topic: cooling
status: draft
---

# Q&A: 液冷、3D VC、cold plate、CDU 差在哪？

## Question

液冷、3D VC、cold plate、CDU 是什麼？AI server 為什麼會讓散熱變成投資主題？

## Short Answer

AI server 的 GPU/CPU/ASIC 功率越來越高，傳統風冷逐漸不夠，散熱從「零件」變成「系統瓶頸」。3D VC 是高效導熱板，cold plate 是直接貼晶片的水冷板，CDU 是 rack 級冷卻液分配設備。散熱的重要性在於：如果熱帶不走，GPU/ASIC 無法滿載，資料中心 capex 就被散熱限制。

## Mental Model

AI server 像一座高爐。GPU/ASIC 是火，電源是燃料，散熱是排熱系統。火越旺，排熱越關鍵；排熱不夠，高爐就不能開滿，投資再多晶片也沒用。

## Technical Explanation

3D VC（Vapor Chamber）利用相變導熱，提升熱從晶片擴散到散熱鰭片的效率；cold plate 把冷卻液直接帶到晶片上方，是 direct-to-chip liquid cooling 的核心；CDU（Cooling Distribution Unit）負責把冷卻液分配到 rack 並與外部熱交換系統連接。AI server 從空冷走到液冷，是因為 rack power density 上升太快。

## Why Investors Care

散熱供應鏈通常會跟 AI server reference design 一起放量。若 NVDA GB200 / GB300 或 hyperscaler 自研 server 大量採 liquid cooling，雙鴻、奇鋐、建準、台達電、Vertiv 等可能受惠。風險是：很多標的是台廠 component，真正毛利/規模要看客戶滲透率與 ASP，不是只看題材。

## Companies / Tickers

| Company / Ticker | Role | Why it matters |
|------------------|------|----------------|
| 3324.TW 雙鴻 | cold plate / 3D VC | 台系 AI server 散熱代表。 |
| 3017.TW 奇鋐 | heat sink / 3D VC / liquid module | AI server 散熱模組受惠。 |
| 2421.TW 建準 | fan / motor | 風冷與輔助散熱。 |
| 2308.TW 台達電 | power + thermal integration | Data center power/thermal solution。 |
| VRT | Vertiv system-level cooling | Data center cooling infrastructure benchmark。 |

## What To Watch

| Signal | Why it matters | Source to monitor |
|--------|----------------|-------------------|
| NVDA GB200 / GB300 reference design | 決定散熱 BOM | NVDA / ODM teardown |
| Liquid cooling attach rate | 決定散熱受惠強度 | ODM / component company calls |
| Cold plate / CDU ASP | 毛利與收入放大關鍵 | company IR |
| Data center rack power density | 決定風冷→液冷切換速度 | industry reports |

## What I Still Don't Know

- EP659 沒有散熱直接 source；這一頁需要新原料支撐。
- 雙鴻 / 奇鋐 / 建準誰真正進入 NVDA reference design。
- 台廠是 component supplier 還是能拿到 system-level margin。

## Sources

- `research/intake/2026-05-10_gooeye-ep659_cooling.md`

## Update Targets

- Knowledge page to update: `research/knowledge/ai-server-supply-chain/cooling.html`
- Brief section to update: future cooling deep dive
