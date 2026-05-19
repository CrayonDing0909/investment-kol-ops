---
workflow: content-production
artifact_type: thesis-card
risk: medium
lens: 資金-mechanism
platform_target: x+threads
counter_direction: n/a (mechanism episode, thesis lives in Ep3)
series: ai-server-thermal
series_episode: 2
series_phase: mechanism
series_arc_total: 3
series_prereq_episodes: [1]
sources:
  - LianLi Work / Morgan Stanley supply-chain estimate (cooling BOM, secondary)
  - EE Times China cooling system breakdown (component mix, secondary)
  - Taipei Times / TrendForce GB300 shipment notes (secondary)
created_at: 2026-05-15
public_status: outline
target_word_count: 450-600
position_disclosure: "n/a — mechanism episode, no buy/sell claim"
related_episodes:
  - "2026-05-15_thermal-series_ep1-electricity.md"
  - "2026-05-15_thermal-series_ep3-suppliers.md"
---

# 散熱系列：第二集 — 一櫃 GB300 為什麼要花 $50K 在液冷上

> **outline only**。第一集 ship 後再回頭寫完整 draft。
>
> 內容繼承自原 Card #001 的 Mechanism + Observation 段，依新系列結構
> 重新組織為「先解釋零件、再解釋花在哪、最後解釋為什麼是這個量級」。

## Episode Outline

| 段 | 重點 | 字數估計 |
|---|---|---|
| Recap from Ep1 | 一櫃 130kW 變熱，所以必須液冷 | 50-80 |
| 液冷四件套 | cold plate / CDU / manifold / UQD 各做什麼 | 150-200 |
| BOM 拆解 | $50K 怎麼分（~40 / 30 / 15 / 10） | 100-150 |
| 為什麼是 $50K | 比較對照：~3% rack 成本、不是 42% | 100-120 |
| Tease Ep3 | 「下一集會講錢流到哪幾家、為什麼我還不急著喊散熱概念股」 | 50 |

## Source Material (preserved from original Card #001)

### Cooling BOM 量級

- LianLi Work 引 Morgan Stanley / supply-chain data：GB300 NVL72 單櫃液冷
  BOM 約 **$49,860**，GB200 約 $41,500，約 +20%。
- 計算：$49,860 / $600,000 ≈ **8.31%**（不是「42% of rack cost」，那個
  數字源頭有分母衝突，本系列不使用）。

### Cooling 零件成本結構

來源 EE Times China teardown：

| 零件 | 佔比 | 角色 |
|---|---|---|
| Cold plate | 40-45% | 貼在 GPU/CPU 上，第一接觸點，把熱帶到冷卻液 |
| CDU (Cooling Distribution Unit) | 30-35% | 整櫃冷卻液循環的主機 |
| UQD (Universal Quick Disconnect) | 15-20% | 快接頭，讓 tray 可以拆下維修不漏液 |
| Manifold | 5-10% | 把冷卻液分流到每個 tray |

### GB300 出貨數量（給規模感）

- TrendForce / Taipei Times：GB300 今年預計占 global AI server rack
  shipments 70-80%。
- 2026 仍以 liquid-to-air 過渡方案為主，liquid-to-liquid 會在 2027 更明顯。

## What Ep2 Deliberately Skips

- 公司名稱（奇鋐 / 雙鴻 / Vertiv 留給 Ep3）
- 投資 thesis（誰受惠、買賣判斷留給 Ep3）
- Position disclosure（沒有 claim）

## IA1 Gate Status

當這集從 outline → draft → ready 時，重跑 IA1 gate：

- 主要 risk：BOM 數字 $49,860 是 secondary estimate，必須清楚標示
- 必須拒絕：「42% of rack cost」這個分母衝突的版本
- 必須保留：「~3% of rack BOM, 但相對於 GB200 +20%」這種正確 framing

## Next Step

Ep1 ship 後 → 評估 Ep1 的 metrics → 如果系列結構被讀者感知到（有人問
「下一集呢？」） → 開始寫 Ep2 full draft。
