---
workflow: source-tutor
artifact_type: source-tutor-reading
reading_mode: cross-source-synthesis
risk: medium
created_at: 2026-05-13
last_updated: 2026-05-13T22:40+08:00
theme: ai-server-supply-chain
source_id: cooling-bom
source_quality: secondary + tertiary-aggregation
source_class: cross-source (report + news + industry-research)
reading_goal: prepare-brief
status: draft
---

# Source Tutor Reading: GB300 液冷 BOM Cross-Source Synthesis

> Purpose：把 Card #001 引用的 4 份散熱 source 一次讀懂，學會「拿到一堆
> 二手拆解、彼此數字不完全一致」這類 source 該怎麼讀。
>
> 這份 reading 的目的不是替 Card #001 背書，而是：
>
> 1. 教你怎麼讀「industry teardown / supply-chain estimate」這類二手源。
> 2. 把 4 份 source 的可信度逐條拆開來看。
> 3. 把目前最刺眼的「$49,860 vs $600K vs 42%」分母衝突，明確標成 `open`
>    並解釋為什麼公開寫作不能繞過這個衝突。
>
> 完成這份後你會知道：哪幾個數字可以寫進貼文、哪幾個只能當「方向感」、
> 哪幾個必須完全避開。

## Source Metadata

This reading synthesizes 4 source packets / articles across 3 source classes：

| # | Packet / Article | Source class | Source quality | Layer / Angle |
|---|------------------|--------------|----------------|---------------|
| 1 | [LianLi Work — 英伟达 GB300單櫃比黃金還貴](https://cn.lianliwork.com/news/nvidia-gb300-liquid-cooling-cost-breakdown-2026) | news / industry teardown，引用 Morgan Stanley supply-chain data | tertiary aggregation（聚合 Morgan Stanley 報告 + supply-chain 訊息） | BOM 金額 + 機櫃成本框架 |
| 2 | [EE Times China — GB200/GB300 散熱系統成本分析](https://www.eet-china.com/mp/a468082.html) | report （產業電子媒體） | high-quality-secondary | 散熱系統 4 大零件 cost mix |
| 3 | [TrendForce / Taipei Times — GB300 to lead AI servers](https://www.taipeitimes.com/News/biz/archives/2026/01/20/2003850873) | news 引 industry research（TrendForce） | secondary-quoted-from-primary | GB300 share + 液冷滲透 forecast |
| 4 | [Vocus — 液冷散熱供應鏈深入剖析](https://vocus.cc/article/6760e08dfd897800011ad609) | industry research blog（台廠導向） | secondary | 台廠（奇鋐 / 雙鴻 / 建準）角色定位 |

- 對應 source packet：[research/sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md](../../sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md)
- Captured at: 2026-05-13
- Related companies / tickers: NVDA / VRT / 3017.TW（奇鋐 AVC）/ 3324.TW（雙鴻 Auras）/ 2384.TW（建準 Sunon，注意 packet 寫 2384，topic page 寫 2421，**ticker 本身有衝突，需驗證**）

## Reading Goal

幫你內化「Card #001 引用的散熱 BOM 故事」到可以被路人質疑時自己反駁。
具體在解兩個問題：

1. 為什麼 `$49,860 / 櫃` 可以寫，但 `占整櫃 42%` 不能寫？
2. 我們有 4 份 source 在說同一件事，但「同一個說法被 4 個人轉述 = 4 倍可信
   嗎？」答案是不一定。

## 這份 Set 在解決什麼問題

Card #001 想說「散熱在 GB300 機櫃裡是大宗 BOM，這個錢 2026 流去哪幾家」。
要 ship 之前，必須先確認：

- 散熱 BOM 數字到底有多硬？
- 受惠公司歸屬有多硬？
- 哪些東西是 NVIDIA 公開 spec 一致、哪些只是產業分析師「拼出來」？

這 4 份 source 不是「primary 證據」。它們是 industry teardown / supply
chain analyst commentary。讀法跟讀 AMD 法說完全不同——AMD 法說是公司自己
講，這 4 份是別人**幫我們拼出來**的。

### User prior beliefs 與 source 對照

| User 心裡的話 | 哪個 source 對應 | 結論 |
|---|---|---|
| 「GB300 一櫃液冷 BOM 大概 $50K」 | Source 1 (LianLi) + Source 2 (EE Times) | ✅ 兩個獨立 secondary 數字一致（$49,860），可作為「方向感」用，但仍是 secondary，因為 Morgan Stanley 原始報告我們沒看到 |
| 「散熱占整個機櫃 42%」 | Source 1 + Source 2（但內部矛盾） | ⚠️ **不是我們自己算的，是二手 source 出現的說法**。但它算術不通：$49,860 / $600,000 = 8.31%。要嘛是 $600K 機櫃裡有別的東西算進 cooling，要嘛 42% 的母體不是 $600K。**這條目前是 `open conflict`，不能直接寫進公開內容。** |
| 「GB300 今年占 AI rack 70-80%」 | Source 3 (TrendForce) | ✅ 引 TrendForce 行業 forecast，是 secondary-quoted-from-primary，可寫但要標「TrendForce 預期」 |
| 「奇鋐 / 雙鴻 / Vertiv 受惠」 | Source 4 (Vocus) + Source 2 (EE Times) | ⚠️ 角色定位是產業共識，但**市占百分比**（奇鋐 30%+、Vertiv 35%+）來自單一 source，未被多源獨立驗證 |

## Reading Lens — Cross-Source Synthesis 怎麼讀

### 跨 source 閱讀的 4 個原則（直接套用）

1. **獨立 evidence chain 才算多源**：LianLi 引 Morgan Stanley、EE Times 自家拆解、Vocus 引自己整理——這 3 條看起來「都說 $49,860」，但 LianLi 跟 Vocus 都可能在引 Morgan Stanley 原始報告。**真正獨立 secondary 大概只有 2 條**（Morgan Stanley + EE Times China），不是 4 條。
2. **Source class 階層不變**：primary > high-quality-secondary > secondary > tertiary。這份 set **完全沒有 primary**（NVIDIA / Vertiv / 奇鋐 / 雙鴻 法說都不在這 4 份裡）。所以**所有結論都帶 secondary 上限**。
3. **管理層 framing 不能跨 source 累加**：沒有管理層 framing 問題，但有「分析師重複 framing 問題」——「散熱占 42%」這句話被 LianLi 與 EE Times 都講過，看起來 2 票，實際是同一個分析師原始說法。
4. **Forward-looking 不能因為跨 source 就升等**：TrendForce 的「GB300 占 70-80%」與「液冷滲透率 >50%」都是 2026 全年 forecast，不是已 reported。即使 LianLi 也轉述，仍是 forward-looking。

### 對「Industry Teardown / Supply-Chain Estimate」這類 source 特有的讀法

- **這類 source 的優勢**：把「散落在多家公司供應鏈的數字」拼成 BOM 總圖，是 primary（每家公司只講自己片段）做不到的。
- **這類 source 的弱點**：分析師為了「拼出整圖」會 inferred / estimated 一些數字。Source packet 已經把所有 claim 都標 `(inferred)`，這是好事。
- **常見 fail mode**：分析師把不同口徑的數字放在同一段。例如「$49,860 cooling BOM」與「occupies 42% of $600K rack」可能來自兩個不同分析（不同機櫃配置 / 不同口徑）但被同一篇文章拼在一起。讀者沒注意就會以為這兩個數字是同一個拆解出來的。

## Cross-Source Map（依 Thesis 線整合）

每條 thesis 列出：所有支持 source、最強 claim 類型、是否多源一致、能不能公開引用。

這裡的「多硬」意思是：**這句話有多可信，能不能拿去公開寫？** 不是股價強弱，也不是投資機會大小。

強度判斷規則：

| 強度 | 意思 | 通常長怎樣 | 公開寫法 |
|---|---|---|---|
| strong | 可以比較安心公開寫 | primary source / reported fact / 多 source 一致 / 無內部矛盾 | 可直接寫，但保留時間與來源 |
| medium | 可以寫，但要加來源標籤或 caveat | 二手 source、industry estimate、forecast、多 source 但可能同源 | 寫「公開拆解 / TrendForce 預期 / secondary」 |
| weak | 不建議寫成精確事實 | 單一二手來源、市占百分比、口徑不清楚、無公司 IR / 法說 | 避開百分比，改寫角色定位或方向 |
| open conflict | 不能寫，不是「弱」而是目前矛盾 | 同組數字彼此算不通，或來源自相矛盾 | 不寫；若必要，寫成「口徑衝突」 |

| # | Thesis 線 | 支持 sources | 最強 claim 類型 | 多源一致？ | 可公開引用？ |
|---|---|---|---|---|---|
| 1 | GB300 NVL72 一櫃液冷 BOM 約 $49,860（GB200 約 $41,500） | Source 1 + Source 2（兩者一致；原始可能都來自 Morgan Stanley supply-chain note） | reported-fact (secondary aggregation) | ⚠️ 表面一致，可能是同源轉述 | ✅ 可寫，但**必須標「secondary / 業界拆解」** |
| 2 | 液冷系統成本結構：cold plate 40-45% / CDU 30-35% / UQD 15-20% / manifold 5-10% | Source 2 only | reported-fact (secondary, single source) | ❌ 單一 source | ⚠️ 可寫，但要明確標來源（EE Times China），且承認沒對到 NVIDIA / Vertiv 原始 BOM |
| 3 | UQD 單顆 $80 → $45（NVUQD03 標準化），但數量翻倍 | Source 2 (EE Times) | reported-fact (secondary) | ❌ 單一 source | ⚠️ 可寫；這條最像 NVIDIA spec 公開的事，但目前只看到 EE Times 講 |
| 4 | GB300 NVL72 滿配 rack 功耗 132-140kW、單顆 B300 GPU TDP 1400W | Source 1 (LianLi) | reported-fact (secondary，但 NVIDIA 公開 spec 一致) | ✅（與 NVIDIA 官方 spec 文件方向一致） | ✅ 可直接寫，數字屬於公開 spec |
| 5 | GB300 占 2026 AI server rack shipments 70-80% | Source 3 (Taipei Times 引 TrendForce) | forward-looking-target (industry forecast) | n/a（單一 forecast） | ⚠️ 可寫，但必須寫成「TrendForce 預期」 |
| 6 | 液冷在 AI 晶片 2026 滲透率突破 50% | Source 3 (TrendForce) | forward-looking-target | n/a | ⚠️ 可寫，要標「TrendForce 預期」；也要承認 2026 仍以 liquid-to-air 過渡為主 |
| 7 | Vertiv 拿液冷 ecosystem 35%+ 價值份額 | Source 2 (EE Times) | secondary-interpretation（單一分析師估計） | ❌ | ⚠️ 可寫，但要寫成「EE Times China 估」，不能寫成事實 |
| 8 | 奇鋐冷板市占 ~30%+ | Source 4 (Vocus) + Source 1 引述 | secondary（口徑未驗證：NVDA-only？全平台？） | ⚠️ 表面 2 source，但 Vocus 可能就是 LianLi 引用源 | ⚠️ 可寫，但**必須加 caveat**：「口徑（NVDA-only vs all-platform）未驗證」 |
| 9 | 雙鴻是 manifold 主玩家 | Source 4 + Source 2 | secondary（角色定位） | ✅ 角色定位多源一致 | ✅ 可寫「manifold / 液冷模組」這類角色描述 |
| 10 | 散熱占整個 GB300 機櫃成本 ~42% | Source 1 + Source 2（皆引述） | **`open conflict`** — $49,860 / $600,000 = 8.31%，跟「占 42%」算術不一致 | ❌ 內部矛盾 | ❌ **不可公開引用為事實**。可寫成「不同分析有不同口徑，安全做法是不引用百分比」 |
| 11 | 建準 / Sunon 在液冷供應鏈相對 peripheral | Source 4 | secondary | n/a | ⚠️ 可寫，但 ticker 衝突（packet 寫 2384，topic page 寫 2421）要先解決 |

## 哪些數字不能直接拿去公開寫

| # | Number | Unit | Period | Source | Why risky | Safer wording |
|---|--------|------|--------|--------|-----------|---------------|
| 1 | 42 | % cooling of GB300 rack | 2026 | Source 1 + Source 2 | $49,860 / $600,000 = 8.31%，算術不通；分母可能是不同口徑（不是整櫃 $600K） | 不要用百分比；改用絕對金額「~$50K / 櫃」 |
| 2 | 600,000 | USD per GB300 rack | 2026 | Source 1 | 整櫃成本 $600K 是 LianLi 一處說法，但同篇文章又說 "$380K 散熱系統" 形成多重內部數字（packet 有提到 $380K 出處）。母體不一致。 | 不引整櫃成本，只引「cooling BOM 約 $49,860」 |
| 3 | 30+ | % AVC 奇鋐 cold plate share | 2026 | Source 4 + Source 1 | 口徑（NVDA-only vs 全平台 / 含 ASIC）未驗證 | 改寫「奇鋐 / AVC 是 cold plate 主要供應商之一」，避免具體百分比 |
| 4 | 35+ | % Vertiv ecosystem 價值份額 | 2026 | Source 2 only | 單一 secondary 估計，無第二源獨立驗證 | 改寫「Vertiv 是 rack / data center 層級 cooling infrastructure 主力之一」 |
| 5 | 70-80 | % GB300 share of 2026 AI rack shipments | 2026 | Source 3 | TrendForce forecast；2026 還沒過完 | 改寫「TrendForce 預期 GB300 將是 2026 主流」，不寫具體 70-80% |
| 6 | 50+ | % liquid cooling 滲透率 in AI chip | 2026 | Source 3 + Source 4 | TrendForce forecast；2026 仍以 liquid-to-air 過渡為主 | 改寫「液冷滲透率往 50% 走，但 2026 主要還是 liquid-to-air 過渡」 |

## What This Set Proves

- AI server 機櫃從風冷切到液冷後，散熱從風扇 + heat sink 變成 cold plate
  + CDU + manifold + UQD 一整套 plumbing 是公開事實（NVIDIA spec 文件、
  EE Times、LianLi 三方一致）。
- GB300 一櫃液冷 BOM 在 $40K-$50K 量級是兩個獨立 secondary 拆解一致的數字
  （即使可能原始都來自 Morgan Stanley），可作為「方向感」公開引用。
- GB300 滿配 rack 功耗 132-140kW、單顆 B300 GPU TDP 1400W 是 NVIDIA 公開
  spec 範圍內，這部分二手轉述跟 primary spec 方向一致。
- 奇鋐 / 雙鴻 / Vertiv 是液冷供應鏈裡有明確角色定位的玩家（cold plate /
  manifold / rack-level integration）。

## What This Set Does Not Prove

- 散熱占整櫃 42% — 內部算術矛盾，**不是事實**。
- 奇鋐冷板市占的精確口徑（NVDA-only？全平台？含 ASIC？）— 沒任一 source
  講清楚。
- Vertiv 35%+ 是真的或只是分析師估計 — 沒對到 Vertiv IR / 投資人簡報。
- GB300 mass-deployment 真正 ramp 月份 — TrendForce 預期是 2026 全年，但
  時間分布沒被任何 source 拆出來。
- 純液冷 (direct-to-chip + liquid-to-liquid) vs 過渡液冷 (liquid-to-air)
  2026 的真正比重 — Source 3 / TrendForce 自己也說「2026 主要還是 liquid-to-
  air 過渡」。

## Sub-Thesis Breakdown

### Sub-Thesis A — 「散熱從旁料變必要 BOM」（Mechanism story）

- Source backing: NVIDIA 公開 spec（B200/B300 TDP）+ Source 1 (132-140kW
  rack power) + EE Times 4 大零件拆解
- Reported: B300 GPU TDP 1400W、GB300 NVL72 rack 132-140kW
- Forward-looking: 後續架構（Rubin）功耗仍上升
- 角色 / role：這是 Card #001 最硬的一條 — 物理機制清楚、有 primary spec
- 風險 / what could break：如果 NVIDIA 改 chiplet 切細 + per-chip power
  退回 700W 內（Counter A），但 Blackwell / Rubin roadmap 都不是這方向

### Sub-Thesis B — 「液冷 BOM 大概 $50K / 櫃」（Number story）

- Source backing: Source 1 + Source 2，可能同源（Morgan Stanley）
- Reported: GB300 ~$49,860 / GB200 ~$41,500
- Forward-looking: n/a（這是現況拆解）
- 角色：給散熱供應鏈一個量級概念
- 風險：分母衝突（看 Sub-Thesis E）；數字本身可能只是分析師估算

### Sub-Thesis C — 「奇鋐 / 雙鴻 / Vertiv 受惠」（Investment implication）

- Source backing: Source 4 (Vocus, 台廠角度) + Source 2 (EE Times, 系統角度)
- Reported: 角色定位（cold plate / manifold / CDU）
- Forward-looking: 市占百分比都是分析師估計
- 角色：把資金流落地到 ticker
- 風險：市占百分比 / NVDA 平台暴露未被公司 IR 揭露；屬於 inferred

### Sub-Thesis D — 「GB300 + 液冷 2026 主流化」（Adoption forecast）

- Source backing: Source 3 (TrendForce)
- Reported: 無
- Forward-looking: GB300 70-80% rack share、液冷 >50% AI chip 滲透
- 角色：給時間框架；放在 Implication 段
- 風險：forecast 本身可能下修；2026 上半年實際 ramp 可能慢

### Sub-Thesis E — 「散熱占整櫃 42%」（Open conflict）

- Source backing: Source 1 + Source 2（皆引述但算術不通）
- Reported: n/a
- Forward-looking: n/a
- 角色：**這是要刻意避開的數字**
- 風險：如果公開引用，被任何人算一下 $49,860 / $600,000 就會發現算術不通

## What Each Source Adds That Others Don't

| Source | 它獨家貢獻什麼？ | 沒有它就會缺什麼？ |
|---|---|---|
| 1 LianLi | Morgan Stanley supply-chain framework + 整櫃 $600K + 132-140kW rack power 等數字 | 沒有量化金額，只剩 mechanism |
| 2 EE Times China | 散熱系統 4 大零件 cost mix（cold plate / CDU / UQD / manifold 百分比）+ UQD 單顆價格變化 | 沒有零件級拆解 |
| 3 TrendForce / Taipei Times | GB300 share + 液冷滲透率 forecast（時間框架） | 沒有 2026 全年 adoption 預期 |
| 4 Vocus | 台廠定位（奇鋐 / 雙鴻 / 建準）+ 中文圈視角 | 沒有 ticker 對照、Card #001 寫不出受惠公司 |

## Sources 互相強化 / 互相牴觸

### 強化（多 source 一致）

- 「GB300 一櫃液冷 BOM 約 $50K」：Source 1 + Source 2 一致（雖然可能同源）
- 「散熱供應鏈核心玩家是 cold plate / manifold / CDU 三層」：Source 2 + Source 4 一致
- 「GB300 是 2026 主流 + 液冷成為必要」：Source 1 + Source 3 一致

### 牴觸 / 張力（要刻意處理）

- 「散熱占整櫃 42%」 vs 「$49,860 / $600K = 8.31%」：**Source 1 自己內部矛盾**。
  $380K 散熱系統的數字也出現在 Source 1，可能是「另一種拆解」。
  Card #001 已經選擇不引用 42%。
- 「奇鋐冷板 30%+ 市占」（Source 4）vs 法說透明度（無）：產業共識 vs 公司
  IR 沒揭露。

## Common Misreads

| Misread | Why it is wrong | Better wording |
|---|---|---|
| 「散熱占 GB300 整櫃 42%」 | 算術不通；$49,860 / $600,000 = 8.31% | 「GB300 一櫃液冷 BOM 接近 $50K」（絕對金額，避開百分比） |
| 「Morgan Stanley / TrendForce / EE Times China 都這樣說，所以非常可信」 | 可能是同一條原始 Morgan Stanley note 被多家轉述，仍只算 1 條 evidence chain | 「兩個獨立 secondary 一致」（標明仍是 secondary） |
| 「奇鋐 cold plate 30%+ 市占」 | 口徑（NVDA-only / 全平台）未驗證 | 「奇鋐是 cold plate 主要供應商之一」 |
| 「2026 液冷滲透率突破 50%」直接寫成事實 | TrendForce forecast，且 2026 還沒過完；2026 主要還是 liquid-to-air 過渡 | 「TrendForce 預期 2026 液冷滲透往 50% 走，但主要仍是 liquid-to-air 過渡」 |
| 「Vertiv 拿 35% 液冷生態份額」直接寫成事實 | EE Times China 單一 secondary 估計 | 「Vertiv 是 rack / data center 層級 cooling infrastructure 主力」（避開百分比） |

## 如果我是投資人，該看哪 5 條 Thesis

| # | Thesis 線 | 為什麼重要 | 最強支持 |
|---|---|---|---|
| 1 | rack power 從 ~50kW 走到 132-140kW，逼出純液冷 | 物理因果鏈最硬，被 NVIDIA primary spec 支持 | NVIDIA 公開 spec + Source 1 |
| 2 | GB300 一櫃液冷 BOM 量級到 $50K | 給供應鏈一個資金規模 | Source 1 + Source 2（同源風險） |
| 3 | 散熱供應鏈分 cold plate / CDU / manifold / UQD 四段，各家公司位置不同 | 受惠不能只說「散熱概念股」，要拆零件 | Source 2 + Source 4 |
| 4 | GB300 + 液冷在 2026 主流化（70-80% rack / >50% chip） | 時間框架支持「3-5 年結構性」 | Source 3 (TrendForce) |
| 5 | 散熱 BOM 內部數字有衝突（42% 跟 $600K 算術不通） | 提醒自己：industry teardown 要逐條校對，不能整套引用 | Source 1 內部矛盾 |

## Internalization Artifacts

### Claim Ledger

| # | Claim | Claim type | Strength | Source(s) | Safe public wording |
|---|-------|-----------|---------|----------|---------------------|
| 1 | GB300 NVL72 滿配 rack 功耗 132-140kW、B300 GPU TDP 1400W | reported-fact (secondary, NVIDIA spec 一致) | strong | Source 1 + NVIDIA public spec | 「GB300 NVL72 一櫃功耗約 132-140kW，B300 GPU 單顆 TDP 1400W」 |
| 2 | GB300 一櫃液冷 BOM 約 $49,860（GB200 約 $41,500） | reported-fact (secondary aggregation) | medium（同源風險） | Source 1 + Source 2 | 「公開拆解資料顯示 GB300 NVL72 單櫃液冷 BOM 約 $49,860」 |
| 3 | 散熱系統 cold plate 40-45% / CDU 30-35% / UQD 15-20% / manifold 5-10% | reported-fact (secondary, single source) | medium | Source 2 only | 「EE Times China 拆 cooling system：cold plate 40-45%、CDU 30-35%、UQD 15-20%、manifold 5-10%」 |
| 4 | GB300 占 2026 AI server rack shipments 70-80% | forward-looking-target (industry forecast) | medium | Source 3 (TrendForce) | 「TrendForce 預期 GB300 將是 2026 AI server 主流（占 rack shipments 70-80%）」 |
| 5 | 液冷在 AI 晶片 2026 滲透率突破 50% | forward-looking-target | medium | Source 3 + Source 4 | 「液冷滲透率往 50% 走，但 2026 主要仍是 liquid-to-air 過渡」 |
| 6 | Vertiv 在液冷 ecosystem 拿 35%+ 價值份額 | secondary-interpretation | weak | Source 2 only | 「Vertiv 是 rack 層級 cooling infrastructure 主力之一」（不寫百分比） |
| 7 | 奇鋐 cold plate 30%+ 市占 | secondary-interpretation (口徑未驗證) | weak | Source 4 + Source 1 引用 | 「奇鋐 / AVC 是 cold plate 主要供應商之一」（避開百分比） |
| 8 | 雙鴻是 manifold / 液冷模組主玩家 | secondary (role positioning) | medium | Source 4 + Source 2 | 「雙鴻 / Auras 是 manifold / 液冷模組玩家」 |
| 9 | 散熱占 GB300 整櫃 42% | open (內部算術衝突) | n/a | Source 1 + Source 2 引用，但算術不通 | **不要寫**；如要提到比例，改用「散熱從原本 5% 不到的旁料變成系統級 BOM」這種定性說法 |
| 10 | 建準 / Sunon 在液冷供應鏈 peripheral | secondary | weak | Source 4 | 「建準在 hybrid air/liquid 設計仍有角色，但純液冷主鏈條較弱」 |

### Mental Model Update

- **AI server 散熱 = 物理瓶頸 + 系統級 BOM**：rack 功耗從 ~50kW 跳到 132-
  140kW，風冷物理上不夠，散熱從旁料變必要系統零件。這條 mental model 被
  NVIDIA primary spec 支持，可長期套用到任何 AI server 公司分析。
- **Industry teardown 要逐條校對，不能整套引用**：Source 1 自己內部就有
  $49,860 / $600K 跟 42% 算術不通的問題。教訓：拿到任何 BOM 拆解報告，先
  自己算一下百分比對不對。
- **「多源一致」要看是不是獨立 evidence chain**：4 份散熱 source 表面上
  互相引用，但 LianLi 跟 Vocus 可能引同一份 Morgan Stanley note。真正獨立
  的 secondary 大概只有 2 條。
- **供應鏈受惠要拆零件，不能講「散熱概念股」**：cold plate / CDU /
  manifold / UQD 四段各自市占不同，奇鋐、雙鴻、Vertiv、建準位置不同；
  公開寫作要對應到具體角色。

### Verification Watchlist

| # | Signal / metric | Why it matters | Where to look | Cadence |
|---|---|---|---|---|
| 1 | NVIDIA 下一代 rack power envelope | 如果 Rubin 往 160kW+ 走，液冷必要性更高；如果回退到 chiplet + 700W per chip，Counter 觸發 | NVIDIA GTC keynote + roadmap | event-driven |
| 2 | 奇鋐 / 雙鴻 / Vertiv 季報 NVDA 平台暴露百分比 | 把「角色定位」升級成「實際營收暴露」 | 公司 IR 法說 | quarterly |
| 3 | Vertiv 法說 liquid cooling backlog | 先行指標：backlog 增長 vs 持平 | Vertiv 季報 | quarterly |
| 4 | NVIDIA GTC 或 OCP 公開 BOM 拆解 | 把 $50K / 櫃從 secondary 升級到 primary | NVIDIA GTC / OCP | event-driven |
| 5 | Morgan Stanley AI infrastructure note 原文 | 如果能拿到，可解開 $50K vs 42% 內部衝突 | 機構研究訂閱 | event-driven |
| 6 | 2026 AI rack shipment mix（liquid-to-air vs direct-to-chip vs immersion） | 驗證 Sub-Thesis D 與 Counter B | TrendForce / IDC quarterly | quarterly |

### Reusable Output Block

> AI server 機櫃從風冷切到液冷的關鍵是 rack power：NVIDIA GB300 NVL72 一櫃
> 滿配功耗約 132-140kW、B300 GPU 單顆 TDP 1400W（NVIDIA 公開 spec 一致）。
> 風冷在這個功耗等級已不可行，散熱從風扇 + heat sink 變成 cold plate +
> CDU + manifold + UQD 整套 plumbing。公開拆解資料顯示 GB300 一櫃液冷 BOM
> 約 $49,860（GB200 約 $41,500，secondary aggregation，可能源自 Morgan
> Stanley supply-chain note）。EE Times China 拆 cooling system：cold plate
> 40-45%、CDU 30-35%、UQD 15-20%、manifold 5-10%（secondary, single
> source）。TrendForce 預期 GB300 將是 2026 AI server rack 主流，液冷滲透
> 率往 50% 走，但 2026 仍以 liquid-to-air 過渡為主（forward-looking
> forecast）。受惠對象拆零件來看：奇鋐 / AVC 是 cold plate 主要供應商之
> 一、雙鴻 / Auras 是 manifold / 液冷模組玩家、Vertiv 是 rack 層級 cooling
> infrastructure 主力（角色定位 secondary）。**注意：「散熱占整櫃 42%」
> 這個說法雖然在公開拆解出現，但 $49,860 / $600,000 = 8.31%，算術不通，
> 不應引用為事實。**

## Downstream Routing

| Artifact | Action | Path |
|---|---|---|
| Source packet | 在 packet 內補上「42% conflict 已在 tutor 處理」備註 | [research/sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md](../../sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md) |
| Knowledge HTML page | 把 cooling.html 從 `needs follow-up` 升級，引用本 reading | [research/knowledge/ai-server-supply-chain/cooling.html](../../knowledge/ai-server-supply-chain/cooling.html) |
| Readings HTML index | 新增本 reading 卡片 | [research/knowledge/ai-server-supply-chain/readings/index.html](../../knowledge/ai-server-supply-chain/readings/index.html) |
| HTML reading view (paired) | 創建配對 HTML 學習頁 | [research/knowledge/ai-server-supply-chain/readings/cooling-bom.html](../../knowledge/ai-server-supply-chain/readings/cooling-bom.html) |
| Card #001 | 確認 caveat 已寫成「不引用 42%」（已 done）；確認 ticker conflict 已記錄 | [content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md](../../../content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md) |
| Follow-up sources | 在 questions/cooling.md（不存在則新建）登記要找 Morgan Stanley 原文、Vertiv 法說、NVIDIA OCP 拆解 | [research/questions/ai-server-supply-chain/cooling.md](../../questions/ai-server-supply-chain/cooling.md) |

## 還不能回答什麼

- $49,860 vs $600K vs 42% 的內部衝突，到底是 LianLi 抄錯、是 EE Times 講
  另一個口徑、還是 Morgan Stanley 原報告就是這樣寫——沒看到原文之前無法判
  斷。
- 奇鋐 cold plate 30%+ 的具體口徑（NVDA-only / 全 AI 平台 / 含 ASIC）。
- Vertiv 35%+ 在液冷 ecosystem 的母體（總值多大？）。
- 建準 ticker：2384 vs 2421 哪個對（兩個檔案不一致，要查證）。
- 2026 上半年 vs 下半年的 GB300 ramp 分布。
- 純液冷 vs 過渡液冷 2026 真正比重。

## Tutor Explanation（白話版）

如果你現在被人問「散熱這條故事有多硬」，你要分三層回答：

1. **物理機制這層最硬**：rack 功耗變高、風冷不夠、必須上液冷。這條有
   NVIDIA primary spec 背書，是公開事實。
2. **金額量級這層中等**：$50K / 櫃這個數字兩個獨立 secondary 都這樣說，
   方向感對，但精確度不是 primary 等級。可以用，但要標 secondary。
3. **占整櫃幾%這層最脆**：42% 跟 $600K 算術不通，公開寫了會被打臉。所以
   Card #001 才特地不講百分比，只講絕對金額。

讀「industry teardown」這類 source 的核心動作只有兩個：

- **逐條校對**：把所有數字寫在一起，自己算一遍百分比。
- **逐源 trace**：問「這個說法獨立 source 有幾個？還是只是同一份原始報告
  被多家轉述？」

這個 reading 教你的「跨二手源整合 lens」可以直接套到 HBM 拆解、被動元件
拆解、ASIC BOM 拆解等任何「industry analyst 拼出來的數字」上。

## Checkpoint Questions

- **哪條 thesis 最 source-backed？哪條最弱？**
  最強：rack power 132-140kW（NVIDIA primary spec 一致）。
  最弱：散熱占整櫃 42%（內部算術衝突，不可引用）。

- **如果要把這份 set 壓成一句話**：
  「GB300 機櫃從風冷切到液冷後，每櫃 cooling BOM 約 $50K，主要錢分到
  cold plate / CDU / manifold 三段；台廠角色定位明確（奇鋐 / 雙鴻 /
  Vertiv），但具體市占百分比是 secondary 估計。」

- **拿掉哪份 source 哪條 thesis 會垮？**
  - 拿掉 Source 1：金額量級沒了，只能講機制不能講錢。
  - 拿掉 Source 2：散熱系統 4 大零件 cost mix 沒了。
  - 拿掉 Source 3：時間框架（2026 主流）沒了。
  - 拿掉 Source 4：台廠角色定位沒了（中文圈視角）。

- **哪條 mental model 我想留下來，即使散熱不再有趣**？
  「Industry teardown 要逐條校對 + 逐源 trace。」這條可以套到任何二手
  數字拼出來的供應鏈分析。

## Follow-Up Needed

- 找 Morgan Stanley AI infrastructure / supply-chain note 原文（解 42% vs
  $600K 衝突）
- 找 Vertiv 最新 IR 投資人簡報（驗證 35% liquid cooling ecosystem 份額）
- 找 NVIDIA GTC 2026 / OCP 對 GB300 cooling 公開拆解
- 拉 奇鋐（3017.TW）/ 雙鴻（3324.TW）Q1 2026 法說 transcript（NVDA 平台
  暴露百分比）
- 解 ticker 衝突：建準 = 2384 還是 2421？

## Update Targets

- Source packet：[research/sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md](../../sources/ai-server-supply-chain/reports/2026-05-13_cooling-source-packet.md)
- HTML knowledge page：[research/knowledge/ai-server-supply-chain/cooling.html](../../knowledge/ai-server-supply-chain/cooling.html)
- HTML readings index：[research/knowledge/ai-server-supply-chain/readings/index.html](../../knowledge/ai-server-supply-chain/readings/index.html)
- HTML reading view (paired)：[research/knowledge/ai-server-supply-chain/readings/cooling-bom.html](../../knowledge/ai-server-supply-chain/readings/cooling-bom.html)
- Questions backlog：[research/questions/ai-server-supply-chain/cooling.md](../../questions/ai-server-supply-chain/cooling.md)

## Template Validation (Meta Reflection)

- Sections that held up as-is：cross-source thesis-line map、claim ledger
  with strength、common misreads、4 跨源原則、sub-thesis breakdown。
- Sections that needed extension：「哪些數字不能直接寫」這張表本來在
  single-source 比較重要，但對 industry teardown 也很重要（因為分析師會
  拼數字）。
- New sections introduced：無，模板涵蓋完整。
- Proposed template upgrade：可考慮加一個 `[cross]` 限定的「同源風險檢測」
  小段，提醒讀者「多家 secondary 引述同一個原始報告」的問題。本次以
  Reading Lens 第一原則涵蓋。
