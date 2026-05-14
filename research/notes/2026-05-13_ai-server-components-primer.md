---
workflow: investment-analysis
artifact_type: domain-primer
theme: ai-server-supply-chain
risk: low
created_at: 2026-05-13
last_updated: 2026-05-13T23:00+08:00
status: draft
canonical_for: research/knowledge/ai-server-supply-chain/primers/ai-server-components.html
audience: KOL operator getting onboarded into AI server supply chain
---

# AI Server 元件 Primer

> 這份是 markdown canonical。請優先讀 HTML 閱讀頁：
> [research/knowledge/ai-server-supply-chain/primers/ai-server-components.html](../knowledge/ai-server-supply-chain/primers/ai-server-components.html)
>
> 目的：在讀 source、寫 card、過 IA1 之前，先建立 AI server 元件 mental
> model。寫完 primer 後你應該能自己回答「散熱是什麼 / BOM 是什麼 / GB300
> 整櫃是什麼 / HBM 是什麼 / 被動元件 / ASIC BOM 是什麼」，不必再去讀分析
> 師報告。

## 這份文件在解決什麼問題

AI server 供應鏈不是「GPU + 外溢概念股」這麼簡單。它分多層，每層各有自己
的物理瓶頸、玩家、和投資邏輯。如果不先弄清楚這些層次，讀任何 source
都會變成「我看到很多數字但不知道在拼哪張圖」。

這份 primer 是 AI server 的「世界地圖」。讀完你會知道：

- 一台 AI server 跟一台 web server 為什麼物理結構不同
- 為什麼 NVIDIA 賣的不是「一張 GPU」而是「一整櫃 rack」
- 為什麼散熱、HBM、被動元件、ASIC 是 4 條 **獨立** 的故事，不是「GPU 外溢」這一條

## 先建立 Mental Model — AI Server 6 層架構

AI server 不是一張 GPU，也不是一台普通電腦。它是一整套工業設備，真的就是一層一層堆起來：

```text
Chip 晶片
→ Package 封裝
→ Board / PCB 主板
→ Compute Tray 運算托盤
→ Rack 機櫃
→ Data Center 資料中心
```

可以先用這個比喻記：

| AI server 元件 | 比喻 |
|---|---|
| CPU / GPU | 引擎，真正做運算 |
| Package 封裝 | 引擎底座，把 GPU、HBM 放得很近 |
| PCB 主板 | 車架和電線，把電與訊號送到各處 |
| Tray 運算托盤 | 可抽換的引擎模組，壞了可以維修 |
| Rack 機櫃 | 一整台賽車，裡面有很多 tray |
| Data Center | 整個賽車場，供電、散熱、網路都在這層 |

以前一般 server 比較像「一台電腦」；現在 AI server 比較像「一整櫃工業設備」。所以投資分析不能只看 GPU，要看整櫃裡每個必要零件的成本和供應鏈。

AI server 從小到大有 6 層，每層各有獨立投資故事與代表廠商：

| Layer | 名稱 | 一句話 | 代表玩家 |
|---|---|---|---|
| 6 | Data Center 資料中心 | 很多 rack 放在一起的「賽車場」：供電、散熱、網路都在這層；單站功耗 30MW → 1GW+ | Hyperscaler 自建、Equinix |
| 5 | Rack 機櫃 | 一整台「賽車」：GB300 NVL72 是 72 GPU + Grace CPU + 散熱 + 電源的 rack-level system；132-140kW、~$600K/櫃 | NVIDIA、Vertiv (CDU)、Foxconn、Quanta |
| 4 | Compute Tray 運算托盤 | 可抽換的「引擎模組」；裡面有 GPU、Grace CPU、HBM、冷板、電源、連接器、快接頭。UQD 讓 tray 維修時不漏液 | 奇鋐 (cold plate)、雙鴻 (manifold)、OEM/ODM |
| 3 | Board / PCB 主板 | 車架和電線；封裝後的晶片焊到 PCB，主板靠 traces / connector 接訊號與電。MLCC 像小型穩壓水庫，AI 主板高階用量 5-10x | Yageo、村田、太陽誘電 |
| 2 | Package 封裝 | 引擎底座；GPU 要跟 HBM 很近地放在一起，靠 CoWoS 接起來。CoWoS 產能不夠，就算有 GPU + HBM 也組不出完整 AI chip | TSMC (CoWoS)、ABF 載板 (味之素)、日月光 |
| 1 | Chip 晶片 | 真正做運算的引擎；GPU / CPU / ASIC / HBM。TDP = 滿載時散熱系統要排掉多少熱；700W → 1400W 代表單顆 GPU 熱量變 2 倍 | NVIDIA、AMD、Intel、Broadcom、SK hynix (HBM) |

AI server 跟一般 server 最大差別：

- 一般 server：layer 1-3 是重點；功耗低、靠風扇散熱
- AI server：每一層都被重新設計；功耗破百 kW；rack-level 思維取代 box-level

**關鍵心法**：AI server 投資不是「GPU 受惠」這一條，是 **6 層 × 各自玩家 × 各自瓶頸** 的網狀故事。任何只看一層的分析都太粗。

## 產業上中下游（板塊圖）

把上面 6 層用「錢和物料怎麼流」重新切。上中下游不是「所有原料清單」，而是看一筆 hyperscaler capex 怎麼一路變成各家供應商的收入。

```text
上游 (製造能力 / 關鍵材料 / 關鍵產能)
→ 中游 (晶片設計 / 模組 / 系統零件)
→ 下游 (整機組裝 / hyperscaler 採購 / 算力使用)
```

### 上游 Upstream — 原料、晶圓代工、封裝、HBM、載板

不是「所有原料」，而是 AI server 能不能做出來的關鍵供應瓶頸。

| 子類別 | 廠商 |
|---|---|
| 晶圓 + 封裝 | TSMC（GPU / ASIC / HBM 都要走這）、TSMC CoWoS（先進封裝瓶頸）、日月光、Amkor |
| 記憶體 | SK hynix（HBM 龍頭）、Samsung（HBM 追趕）、Micron（HBM 受美國政策加分） |
| 載板與被動料 | 味之素 ABF substrate、欣興、南電 ABF 載板代工、Yageo / 村田 / 太陽誘電（高階 MLCC） |

### 中游 Midstream — 晶片設計、模組組裝、散熱整合

把上游能力轉成可出貨的晶片、模組、系統零件。

| 子類別 | 廠商 |
|---|---|
| GPU / CPU 設計 | NVIDIA（GPU + Grace CPU + rack reference design）、AMD（EPYC + Instinct）、Intel（Xeon + Gaudi） |
| ASIC 設計合作 | Broadcom（Google TPU、Meta MTIA）、Marvell（AWS Trainium 2）、Alchip、GUC |
| 散熱模組 | 奇鋐 AVC（cold plate）、雙鴻 Auras（manifold / liquid module）、Vertiv（rack-level CDU / 整合）、建準 Sunon（hybrid air/liquid） |

### 下游 Downstream — 整機組裝、Hyperscaler、算力銷售

把 rack 組出來、賣給 hyperscaler，最後變成可用算力。

| 子類別 | 廠商 |
|---|---|
| ODM 整機組裝 | Foxconn 鴻海、Quanta 廣達、Wistron 緯創、Supermicro |
| Hyperscaler（真正買方） | Microsoft Azure、Meta、Google Cloud、Amazon AWS、Oracle、CoreWeave |
| 最終買單 | AI 模型公司（OpenAI、Anthropic 等）、企業 SaaS 整合、政府 / 主權 AI 採購 |

**讀法**：同一家公司可能跨多層（NVIDIA 同時做 chip + reference rack design），但分析「誰受惠」時要先放到正確的位置。奇鋐是中游零件廠、Vertiv 是中游系統整合、Foxconn 是下游 ODM，不能直接比百分比。

### 錢怎麼流？從 hyperscaler capex 到供應商收入

1. **Hyperscaler capex**：Microsoft / Meta / Google / Amazon 決定多買 AI 算力。
2. **NVIDIA rack order**：買的不只是 GPU，是 GB300 / NVL72 這種整櫃 reference design。
3. **ODM 組裝**：Foxconn / Quanta / Wistron / Supermicro 把整櫃組出來。
4. **NVIDIA reference design 指定零件**：rack 裡需要 HBM、CoWoS、ABF、MLCC、cold plate、CDU、manifold、UQD。
5. **上游 / 中游供應商出貨**：SK hynix 出 HBM，TSMC 出 CoWoS，奇鋐 / 雙鴻 / Vertiv 出液冷相關零件，國巨 / 村田出高階被動元件。
6. **最後看財報驗證**：真的有沒有反映到 revenue、gross margin、backlog、客戶暴露比例。

所以一篇投資內容不應該停在「誰在供應鏈」。它要回答：

```text
這家公司卡在哪個必要環節？
那個環節的 BOM / ASP / volume 有沒有變大？
財報能不能驗證？
```

## Domain Glossary

### 散熱（Cooling）

- **是什麼**：把晶片產生的熱搬走，讓晶片不會 thermal throttle 或燒掉。
- **在哪層**：跨 layer 1（晶片表面）、layer 4（tray 內管路）、layer 5（rack CDU）、layer 6（data center 冷卻塔）。
- **thermal throttle 是什麼**：晶片太熱時，為了不燒掉會自動降頻。你花大錢買 GPU，但熱排不出去，它就自己降速保命，算力跑不滿。
- **為什麼變大事**：H100 700W → B300 1400W；一整櫃 GB300 約 132-140kW。空氣冷卻單顆極限大約 700W，超過就帶不走熱。
- **拆四段**：
  1. `Cold Plate`：水冷板，直接貼晶片。台廠 = 奇鋐 / 雙鴻 / Cooler Master。
  2. `CDU`（Coolant Distribution Unit）：rack 內冷卻液分配。Vertiv / Schneider 等系統廠。
  3. `Manifold`：水管歧管，把冷卻液送到每個 tray。雙鴻是台廠主玩家。
  4. `UQD`（Universal Quick Disconnect）：快接頭，tray 維修不漏液。安費諾等。
- **常見誤解**：「散熱概念股」太粗。每一段供應鏈玩家不同，市占口徑也不同。

**液冷怎麼把熱帶走**：

```text
GPU 發熱
→ 熱傳到 cold plate
→ 冷卻液流過 cold plate，把熱帶走
→ manifold 把冷卻液分配到不同 tray
→ CDU 控制整櫃冷卻液流量與熱交換
→ 熱最後被帶到 data center 冷卻系統
```

可以想成水冷電腦，但 scale 放大 100 倍，而且要企業級可靠：不能漏水、不能停機、tray 還要能抽換維修。

**散熱投資邏輯鏈**：

1. **需求不是從散熱開始，是從 AI 算力開始**：hyperscaler 要更多 AI 算力，所以 NVIDIA 推更強 GPU。
2. **更強 GPU 帶來更高功耗**：H100 700W → B300 1400W，單顆 GPU 熱量大幅上升。
3. **熱排不出去，GPU 就跑不滿**：散熱不夠會 thermal throttle，昂貴算力無法 full utilization。
4. **所以液冷從 optional 變成必要**：風扇不夠了，必須用 cold plate、CDU、manifold、UQD。
5. **必要零件變多，BOM 變大**：以前 server 散熱是風扇 + heat sink；現在一整櫃要一套液冷 plumbing，單櫃 cooling BOM 接近 $50K。
6. **BOM 變大，供應商收入機會變大**：如果 GB300 rack 出貨增加，每一櫃都要這套液冷，零件廠的訂單量和 ASP 可能上升。
7. **所以才看公司，但只是 watchlist**：cold plate → 奇鋐 / 雙鴻；manifold → 雙鴻；CDU / rack cooling → Vertiv；hybrid fan → 建準。接下來要看法說有沒有證實 NVDA 平台暴露、backlog、毛利。

錯誤投資邏輯：

```text
AI 很熱 → 散熱股買
```

正確投資邏輯：

```text
AI 算力需求上升
→ GPU power density 上升
→ rack cooling 從 optional 變 required
→ cooling BOM per rack 上升
→ 指定零件供應商 ASP / volume 有機會上升
→ 用公司法說驗證 revenue / margin / backlog
```

### BOM (Bill of Materials)

- **是什麼**：一台設備的零件成本表。每個零件多少錢、占整台百分比。
- **跟 revenue 的差別**：BOM 是 **零件成本**，不是 **公司營收**。
  - 例：GB300 一櫃液冷 BOM ~$50K → 是 NVIDIA 採購整套液冷的成本，不是某家供應商賺 $50K。供應商賺多少要看它自己的 ASP × 數量。
- **為什麼在投資裡常被提**：BOM 占比高的零件，零件廠 ASP 容易跟產品升級一起上漲（BOM uplift）。例如 GB200 → GB300 cooling BOM 從 $41.5K → $49.86K，整體散熱供應鏈水位往上。
- **常見誤解**：把 BOM 數字直接當 revenue。錯。

**BOM 投資邏輯鏈**：

1. 先找產品升級，例如 GB200 → GB300，不只是 GPU 更強，整櫃散熱、電源、連接器都變複雜。
2. 看哪個零件的 `content per unit` 變大。如果每櫃散熱 BOM 從 $41.5K → $49.86K，代表每賣一櫃，散熱供應鏈拿到的內容價值變大。
3. 問誰拿到這段 BOM。cold plate / CDU / manifold / UQD 各有不同供應商，不是一家公司吃全部。
4. 回財報驗證。看 ASP、shipment、gross margin、backlog 是否跟 BOM uplift 同步改善。

錯誤投資邏輯：

```text
BOM 變大 → 供應商一定賺更多
```

正確投資邏輯：

```text
BOM 變大
→ 找出哪個零件 content 變大
→ 找到供應商
→ 用 ASP / volume / margin / backlog 驗證
```

### GB300 整櫃（NVL72）

- **是什麼**：NVIDIA 把 Grace CPU + Blackwell Ultra (B300) GPU + NVLink switch + 散熱 + 電源整合成一個 rack。
- **不是**：「一張 GPU」。NVIDIA 已經 **不賣單片 GPU 給 AI**，賣的是 rack-level system。
- **規格**：72 顆 B300 GPU + 36 顆 Grace CPU + 9 個 NVSwitch tray，整櫃功耗 132-140kW，重量 ~1500kg，整櫃售價約 600,000 美元（業界拆解）。
- **跟之前的差別**：
  - 之前 hyperscaler 採購單位是「一張 H100」
  - 現在採購單位是「一個 NVL72 rack」
- **為什麼重要**：rack 一上線就要綁定整套散熱 / 電源 / 配電，所有層的供應鏈都被拉進主流。

**GB300 整櫃投資邏輯鏈**：

1. NVIDIA 從 chip seller 變 rack system seller。買方不只買 GPU，而是買一整套 reference design。
2. Reference design 指定一整串零件。散熱、電源、HBM、CoWoS、ABF、被動元件都跟著整櫃出貨。
3. 每一櫃出貨都帶動一包供應鏈。不是單一 GPU 出貨，而是一組 rack-level BOM 出貨。
4. 所以看 GB300 ramp 時，要看每層供應商。ODM 組裝、散熱零件、HBM、被動元件、電源都會被拉動，但彈性不同。

錯誤投資邏輯：

```text
GB300 很貴 → NVIDIA 以外所有供應鏈都大賺
```

正確投資邏輯：

```text
GB300 整櫃化
→ 每櫃固定需要一整套 BOM
→ 找 content per rack 提升最大的環節
→ 看實際 shipment / margin
```

### HBM (High Bandwidth Memory)

- **是什麼**：高頻寬記憶體。3D 堆疊 + TSV（穿矽通孔）放在 GPU 旁邊。
- **不是**：一般 DRAM。HBM 比 DDR 貴 5-10 倍。
- **解決什麼問題**：memory wall。GPU 算力越來越快，但 DRAM 餵料速度跟不上；HBM 把記憶體頻寬拉到 TB/s 等級。
- **三家**：SK hynix / Samsung / Micron。SK hynix 是 NVIDIA 主要供應，Micron 在追，Samsung 在認證。
- **節奏**：HBM3 → HBM3E（current）→ HBM4（2026-2027）。
- **為什麼重要**：HBM 供給不足會直接卡住 GPU 出貨，是整條 AI server 供應鏈的一個 hard bottleneck。

**HBM 投資邏輯鏈**：

1. GPU 算力提升後，資料餵不進去會浪費算力。這就是 memory wall。
2. HBM 把記憶體貼近 GPU，頻寬提升，GPU 比較不會等資料。
3. HBM 供給變成 GPU 出貨瓶頸。GPU 有了，如果 HBM 或 CoWoS 不夠，整顆 AI chip 還是出不了貨。
4. 所以看 HBM 廠，不只看 DRAM 景氣。要看 NVIDIA / AMD 配額、HBM3E / HBM4 認證、ASP、毛利。

錯誤投資邏輯：

```text
AI 帶動 HBM → DRAM 全部都漲
```

正確投資邏輯：

```text
AI 算力需要高頻寬
→ HBM 變必要瓶頸
→ 看 SK hynix / Micron / Samsung 的 HBM 配額、認證、ASP、margin
```

### 被動元件（Passive Components）

- **是什麼**：電容（capacitor）、電阻（resistor）、電感（inductor）。不是 IC，但每塊主板都需要。
- **為什麼 AI server 需要更多**：高功耗主板（CPU + GPU 同時拉電）需要 5-10x 高階 MLCC（多層陶瓷電容）來穩定供電。
- **玩家**：日本 = 村田 / 太陽誘電；台灣 = Yageo（國巨）/ 華新科 / 信昌電；韓國 = Samsung Electro-Mechanics。
- **常見誤解**：因為單價低，常被忽略。但 AI server 主板上的高階 MLCC 數量翻倍，整體拉動高階料 ASP。

**被動元件投資邏輯鏈**：

1. AI 主板功耗上升。CPU + GPU 同時拉大電流，供電瞬間波動變大。
2. 電壓不能亂跳。否則晶片不穩、訊號不穩、系統容易出錯。
3. 高階 MLCC / 電感需求變大。用量變多，規格變高，content per board 上升。
4. 投資驗證看高階產品 mix。不是看整個被動元件景氣，而是看 AI server / high-end MLCC 是否拉 ASP、毛利、交期。

錯誤投資邏輯：

```text
AI server 要更多零件 → 被動元件全部受惠
```

正確投資邏輯：

```text
高功耗主板
→ 高階 MLCC / 電感用量與規格上升
→ 看高階料 ASP / mix / 交期，不看低階 commodity
```

### ASIC BOM

- **是什麼**：ASIC = Application-Specific Integrated Circuit，客製化晶片。
- **誰做**：hyperscaler 自己設計（Google TPU、AWS Trainium、Meta MTIA、微軟 Maia），通常找 Broadcom / Marvell / Alchip / GUC 做設計合作。
- **跟 GPU 的差別**：
  - GPU = 通用，什麼 model 都能跑
  - ASIC = 為特定 workload（例如 inference）優化，perf/W 更好，但放棄通用性
- **為什麼 hyperscaler 要做**：(a) 不想把 80% gross margin 都付給 NVIDIA；(b) 對自家 workload 可以省掉 GPU 的通用功能。
- **ASIC BOM ≠ GPU BOM**：是 **平行** 的供應鏈，不是 GPU 外溢。Google TPU 用 Broadcom 設計 + TSMC 製造 + 自家 HBM 配額；跟 NVIDIA GB300 是兩條不同 BOM。

**ASIC 投資邏輯鏈**：

1. Hyperscaler 不想完全依賴 NVIDIA。GPU 好用但貴，毛利大多被 NVIDIA 拿走。
2. 自家 workload 可以用專用晶片優化。例如 inference 固定、模型架構固定，就能用 ASIC 換更好的 perf/W。
3. 但 hyperscaler 不一定自己做完。它們定義需求，Broadcom / Marvell / Alchip / GUC 幫忙設計，TSMC 幫忙製造。
4. ASIC 仍吃共用瓶頸。TSMC 先進製程、CoWoS、HBM 都可能跟 NVIDIA GPU 搶產能。
5. 投資驗證看 design win + 量產時點。不是「有 ASIC 需求」就算數，要看 customer、project size、ramp schedule。

錯誤投資邏輯：

```text
hyperscaler 做 ASIC → Broadcom / Marvell 全部受惠
```

正確投資邏輯：

```text
hyperscaler 自研需求
→ 設計合作商拿 design win
→ TSMC / HBM / CoWoS 配額能跟上
→ project ramp 進 revenue
```

## 你需要先知道的背景

- **rack-scale vs box-scale 思維轉變**：AI server 是 rack 級系統，整櫃綁定散熱 / 電源 / 互聯。任何「GPU 受惠」分析如果只看單片 GPU，就漏掉 rack 一半的故事。
- **NVIDIA 賣的是整套參考設計**：NVIDIA reference design 決定整條供應鏈分配。Hyperscaler 通常照 NVIDIA reference 採購，所以 NVIDIA 一改 spec，整條供應鏈跟著動。
- **Hyperscaler 是真正的買方**：Microsoft / Meta / Google / Amazon 是 AI server 最大採購方。他們 capex 才是這條 thesis 的真正驅動。
- **TSMC 是 single point of failure**：B300 GPU、Trainium ASIC、TPU、AMD Instinct 全部都在 TSMC 做。TSMC 產能分配 = 誰能出貨。

## 容易混淆的點

| 容易搞錯 | 正確讀法 |
|---|---|
| 「NVIDIA 一張 GPU 賣多少」 | NVIDIA 現在以 rack 為單位出貨，一櫃 $600K |
| BOM = 公司營收 | BOM = 零件成本表，跟公司營收兩件事 |
| TrendForce 預期 = 已實現 | Forecast 跟 reported-fact 是兩種等級，永遠先看時態 |
| 散熱概念股 | 拆 cold plate / CDU / manifold / UQD 四層，市占口徑不同 |
| Component supplier vs system integrator | 奇鋐做零件 vs Vertiv 整合 rack，不能直接比百分比 |
| ASIC 受惠 = GPU 外溢 | ASIC 是平行 BOM，不是 GPU 衍生 |
| HBM 漲價 = 一般 DRAM 漲價 | HBM 是高階 niche 產品，跟 DRAM 大宗價脫鉤 |
| 被動元件 = 低附加價值 | AI server 高階 MLCC 數量翻倍，ASP 拉動明顯 |

## 按章節導讀（讀完這份 primer 後該去哪）

| 你想知道的下一步 | 該去看的檔 |
|---|---|
| 散熱 source 怎麼讀 | `research/knowledge/ai-server-supply-chain/readings/cooling-bom.html` |
| GB300 整櫃對供應鏈的影響 | `research/sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md` |
| AMD / Intel CPU 復興 | `research/source-tutor/ai-server-supply-chain/2026-05-13_amd-q1-2026_reading.md`、`...intel-full-thesis-v2_reading.md` |
| HBM 供需 | `research/sources/ai-server-supply-chain/reports/2026-05-13_hbm-supply-demand-source-packet.md` |
| 被動元件 | `research/sources/ai-server-supply-chain/news/2026-05-13_passive-components-source-packet.md` |
| ASIC | `research/knowledge/ai-server-supply-chain/asic.html` |
| 整個產業地圖 | `research/knowledge/ai-server-supply-chain/index.html` |

## Debug / Review Checklist（看別人的文章 / 自己寫稿前自檢）

- [ ] 講「散熱概念股」？停一下，到底是 cold plate / CDU / manifold / UQD 哪一段？
- [ ] 引用 BOM 數字？確認它是 BOM 還是 revenue？
- [ ] 引用市占百分比？確認 component 還是 system 口徑？
- [ ] 引用未來預測？確認是 reported-fact 還是 forecast？
- [ ] 把 ASIC 寫成「GPU 外溢」？拆開，兩條供應鏈不同。
- [ ] 把 HBM 寫成「DRAM 漲」？HBM 跟 commodity DRAM 是兩條曲線。
- [ ] 把整櫃 $600K 寫成「GPU 漲價」？不對，是整套 system 售價。

## 最小可記住版本

1. AI server 不是 GPU 一張，是 rack 一台。
2. GB300 一櫃 ~$600K，包含 72 GPU + Grace + 散熱 + 電源。
3. BOM = 零件成本表，不是公司營收。
4. 散熱從旁料變大 BOM，是因為 rack 功耗破 130kW。
5. 散熱拆 4 段：cold plate / CDU / manifold / UQD。
6. HBM 解決 memory wall，SK / Samsung / Micron 三家。
7. 被動元件是電容電阻電感，AI 主板高階料用量翻倍。
8. ASIC 是 hyperscaler 自研晶片，BOM 結構跟 GPU 不同（平行不是外溢）。
9. Forecast 跟 fact 永遠分開，看時態。
10. Component supplier（奇鋐）跟 system integrator（Vertiv）不能直接比百分比。

## 建議追問

讀完這份 primer，這些是你之後可以自己拿來問 agent 的下一輪問題：

- 「NVIDIA reference design 怎麼決定供應鏈分配？」
- 「TSMC CoWoS 產能瓶頸怎麼影響 AMD Instinct / NVIDIA Rubin？」
- 「Hyperscaler capex 跟 GPU 出貨量的時間差是多久？」
- 「AI server 的單位電力成本（TCO）vs 傳統 server 差多少？」
- 「HBM4 的時程跟 GPU roadmap 如何對齊？」
- 「Liquid-to-air 過渡液冷 vs liquid-to-liquid 直液冷有什麼 BOM 差異？」

## Source / Follow-up

- 這份 primer 本身是 **常識整理 + agent inference**，不是 source-backed claim。任何具體投資結論都要回去走 source tutor 流程。
- 後續可以把 primer 內的具體數字（B300 TDP 1400W、132-140kW、$600K rack、cooling BOM $49,860）對到 source packet 中的對應 reference，讓 primer 從「常識版」升級到「source-backed」。

## Update Targets（之後如何維護）

- 當有新的元件加入故事線（例如 optical interconnect、CPO），在這份 primer 加一個 glossary entry。
- 當 NVIDIA / hyperscaler 換代（GB300 → Rubin / Vera Rubin / etc.），更新 `GB300 整櫃` 段為新一代。
- 當被動元件 / HBM / ASIC 有 generation change，回來更新節奏資訊。
