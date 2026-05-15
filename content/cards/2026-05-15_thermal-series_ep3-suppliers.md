---
workflow: content-production
artifact_type: thesis-card
risk: high
lens: 資金-thesis
platform_target: x+threads
counter_direction: bull-kill (counter-first framing required)
series: ai-server-thermal
series_episode: 3
series_phase: thesis
series_arc_total: 3
series_prereq_episodes: [1, 2]
sources:
  - LianLi Work / Morgan Stanley supplier exposure estimate (secondary)
  - 奇鋐 / 雙鴻 / Vertiv public filings + 法說 quotes (primary where available)
  - SemiAnalysis cooling supply chain teardown (secondary)
created_at: 2026-05-15
public_status: outline
target_word_count: 550-750
position_disclosure: "required when finalized — author may hold mentioned names; generic disclosure"
related_episodes:
  - "2026-05-15_thermal-series_ep1-electricity.md"
  - "2026-05-15_thermal-series_ep2-bom.md"
---

# 散熱系列：第三集 — 這筆錢流到哪幾家公司，為什麼我還不急著喊散熱概念股

> **outline only**。Ep1 + Ep2 ship 後才寫 full draft。
>
> 這集是 thesis phase，必須有完整 position disclosure + counter-first
> 結構。內容繼承自原 Card #001 的 Companies + Counter + Raw Voice 結論。

## Episode Outline

| 段 | 重點 | 字數估計 |
|---|---|---|
| Recap Ep1 + Ep2 | 「電變熱、熱要液冷、液冷一櫃 $50K」 | 80-100 |
| Counter first | 「但我不會急著喊散熱概念股」+ 反向檢查點 | 120-150 |
| 零件 → 公司 mapping | cold plate→奇鋐/AVC、CDU→Vertiv、manifold→雙鴻 等 | 150-200 |
| 我目前在追什麼 | 法說 backlog、margin、單櫃 ASP 三條觀察線 | 100-150 |
| Position disclosure + CTA | 持股聲明 + 系列地圖回鏈 + 完整供應鏈地圖 | 50-100 |

## Counter-First Framing (mandatory per series-narrative-architecture rule)

依規則要求，thesis 集必須先 counter 再 bull。預設 counter：

```text
這條線我會先放一個反向檢查點（算一種利多出盡吧）：

如果未來兩年 AI rack 還是以過渡型液冷為主，
沒有更快走向 direct-to-chip / 全液冷，
那 cold plate、manifold、CDU 這些零件的成長速度
可能就沒有想像中快。

（但至少目前看到的產業資料跟資訊是 OK 的。）
```

## Supplier Mapping (preserved from original Card #001)

| 零件 | 主要供應商 / 受惠 | 證據強度 |
|---|---|---|
| Cold plate | 奇鋐、AVC、雙鴻 / Auras | LianLi Work supply-chain map + 法說交叉確認 |
| CDU | Vertiv、Boyd | 公開新聞 + Vertiv 法說 |
| Manifold | 雙鴻 / Auras（部分） | secondary estimate |
| UQD | CPC / Stäubli / Parker | 國際零件商，台廠 exposure 較低 |

## Raw Voice Conclusion (preserved)

```text
所以統整完上面這些資料，我目前得到的結論是：
散熱本身會開始受到關注，是因為 AI server 變成一組一組的去賣，
所以它上面的散熱組件就被綁定一起出貨，
那就導致相關零件廠商有連帶關係。

如果未來一切都很美好，AI rack 繼續往更高功耗走，
這條線會繼續值得追；
但如果液冷 adoption 卡在過渡方案，
或供應商法說沒有轉成 backlog / margin，
那就要小心一點。

但我覺得本質不變，
算力不斷短缺的情況下，
液冷應該是個很好的基本面支撐。
```

## Position Disclosure (template)

```text
作者可能持有上述公司之一或多家股票。
這篇不是投資建議。
若你考慮交易，請自行研究或諮詢專業人士。
```

## IA1 Gate Requirements

當這集從 outline → draft → ready，**必須**重跑 IA1：

- High risk：包含公司名 + thesis + 持股聲明
- 必須通過：counter-first 結構、position disclosure 完整、零件→公司
  mapping 至少 1 條 primary source（法說／公告）
- 必須拒絕：明確 buy / sell 用語、特定價位推薦、forward-looking 收益保證

## CTA Strategy

```text
散熱系列首頁：vercel.app/library/ai-server-supply-chain/series/thermal/
完整 AI Server 供應鏈地圖：vercel.app/library/ai-server-supply-chain/
```

第三集結尾把讀者引導到更大的供應鏈地圖（HBM、ASIC、CPO 等其他條線），
為未來其他系列（記憶體系列、ASIC 系列等）鋪路。

## Next Step

只在 Ep1 + Ep2 都已 ship 且 metrics 健康後才寫 Ep3 full draft。
