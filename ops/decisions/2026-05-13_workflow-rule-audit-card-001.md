---
artifact_type: workflow-audit
related_gate: ops/decisions/2026-05-13_ia1_card-001-cooling-bom.md
related_artifact: content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md
created_at: 2026-05-13
last_updated: 2026-05-13T22:55+08:00
reviewer: CrayonDing0909
trigger: "User 質疑「我什麼跟 Card #001 有關的 source 都還沒看，那我根本沒學到東西」"
---

# Workflow Rule / Skill Audit — Card #001 Cooling BOM

## Why this audit exists

在推 Card #001 走到 IA1 gate 的過程中，user 提出兩個關鍵質疑：

1. 既然要審稿，應該是 HTML，不是 markdown。
2. 我沒讀過任何跟 #001 有關的 source，怎麼能審？我學到什麼？

兩個質疑都對。問題不在 user，是 agent 在 ship Card #001 時跳過了 repo
自己定義的學習層。這份 audit 把規則 / skill / workflow 跑完一次盤點，
明確記錄這次「用到什麼、漏掉什麼、之後該怎麼改」。

## Rules audit

| Rule path | Status | 用到了嗎 | 該不該用到 | 備註 |
|---|---|---|---|---|
| [.cursor/rules/session-isolation.mdc](../../.cursor/rules/session-isolation.mdc) | ✅ used | yes | yes | branch boundary、session log 都建好 |
| [.cursor/rules/git-workflow.mdc](../../.cursor/rules/git-workflow.mdc) | ✅ used | yes | yes | 每次 commit 前先要 user 同意 |
| [.cursor/rules/source-tutor-reading.mdc](../../.cursor/rules/source-tutor-reading.mdc) | ❌ **missed** | no | **必須用** | Card #001 引 4 份 source，應走 cross-source-synthesis；漏到這份 audit 才補回去 |
| [.cursor/rules/html-reading-ui.mdc](../../.cursor/rules/html-reading-ui.mdc) | ⚠️ partially | yes（知識頁）/ no（審稿頁） | yes | 寫了 IA1 markdown decision file 給 user 審，但沒做配對 HTML 審稿頁 |
| [.cursor/rules/analysis-reasoning.mdc](../../.cursor/rules/analysis-reasoning.mdc) | ✅ used | yes | yes | Card #001 結構符合 Observation → Mechanism → Implication → Counter |
| [.cursor/rules/content-voice-raw-research.mdc](../../.cursor/rules/content-voice-raw-research.mdc) | ✅ used | yes | yes | Card #001 用「我目前覺得 / 還沒驗證」raw voice |

## Workflow audit

| Workflow（per `docs/WORKFLOW_PATTERNS.md`） | Status | 用到了嗎 | 該不該用到 | 備註 |
|---|---|---|---|---|
| Investment Analysis | ✅ used (earlier M1/M2) | yes | yes | M1 / M2 已跑完，產出 backbone article |
| **Source Tutor** | ❌ **missed for cooling** | no | **必須用** | Card #001 引 4 份 source 卻沒跑 source tutor；本次 audit 補上 cooling-bom reading |
| Content Production | ⚠️ partially | yes | yes | Card 結構建好，但「先學會再輸出」原則被跳過 |
| Ship Workflow | ✅ used | yes | yes | 每次 commit 都按 ship workflow |

## Skills / agent role audit

依 [docs/AGENT_ROLES.md](../../docs/AGENT_ROLES.md) 列的 M1 roles：

| Role | Status | 用到了嗎 | 該不該用到 | 備註 |
|---|---|---|---|---|
| Source Collector | ✅ used | yes | yes | cooling-source-packet.md 已建立 |
| Intake Curator | ⚠️ skipped | no | optional | cooling 沒走 intake step，直接從 packet 寫 card |
| **Source Tutor** | ❌ **missed** | no | **必須用** | 4 份 source 應該整合 → cross-source tutor note + HTML reading |
| Tutor / Q&A | ⚠️ partial | yes (cooling.html topic) | yes | cooling 主題 Q&A 還停在 needs follow-up |
| Knowledge Architect | ⚠️ partial | yes (主題地圖建好) | yes | cooling.html 還是 needs follow-up，本次 audit 後可升級 |
| Brief Builder | n/a | n/a | n/a | M2 已完成，cooling 段在 backbone article |
| POV Coach | n/a | n/a | n/a | Card 本身就是 POV 載體 |
| Gate Reviewer | ✅ used | yes | yes | IA1 decision file 建好；本次 audit 後改成兩段流程 |

## Skills（external）audit

| Skill / Tool | 用到了嗎 | 備註 |
|---|---|---|
| `data-quality-checker` | ✅ used | 跑過 card，0 findings — 但 0 findings ≠ 內容對；它檢格式，不檢 source quality |
| `domain-doc-tutor` | ❌ missed | Source tutor reading 該借用這個 tutoring stance |
| `shadcn` / Vercel / cursor IDE | ✅ used | dashboard、Vercel library deploy 都用上 |
| `figma-*` | n/a | 本次無視覺資產需求 |

## 跑歪在哪？

按 `AGENTS.md` 預設行為：

1. **Identify intent and pick a workflow** — ✅ 已選 content-production。
2. **Collect structured data first** — ⚠️ 有 packet，但沒整合過。
3. **Load only the matching context pack** — ✅ 載 cooling packet。
4. **Use LLM for synthesis, drafting, classification, review against checklists** — ⚠️ 跳過了 Source Tutor 的「synthesis + classification against
   claim taxonomy」這層；直接進 IA1 review against checklists。
5. **Apply risk classifier and respect mandatory human gate** — ✅ 已標 high risk + IA1 gate。
6. **Produce a tangible artifact** — ✅ card + decision file 都有。
7. **Update metrics** — n/a（card 還沒 ship）。

**核心錯誤**：第 4 步把「synthesis + classification」與「review against
checklists」當作同一步驟。實際上：

- synthesis + classification 屬於 **Source Tutor 階段**（學習層）
- review against checklists 屬於 **Gate Reviewer 階段**（gate 層）

兩個階段都需要 user 出席，但**順序不能顛倒**：先學會（HTML reading），才
能審（HTML review + IA1 decision）。

## 修正辦法（已在本次套用）

| 修正項 | 已 done | path |
|---|---|---|
| 補 cooling cross-source tutor note | ✅ | [research/source-tutor/ai-server-supply-chain/2026-05-13_cooling-bom-reading.md](../../research/source-tutor/ai-server-supply-chain/2026-05-13_cooling-bom-reading.md) |
| 補配對 HTML 學習頁 | ✅ | [research/knowledge/ai-server-supply-chain/readings/cooling-bom.html](../../research/knowledge/ai-server-supply-chain/readings/cooling-bom.html) |
| 把 reading 連進 readings index | ✅ | [research/knowledge/ai-server-supply-chain/readings/index.html](../../research/knowledge/ai-server-supply-chain/readings/index.html) |
| 為 Card #001 建 HTML 審稿頁 | ✅ | [content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html](../../content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html) |
| Update IA1 decision file 為兩段流程 | ✅ | [ops/decisions/2026-05-13_ia1_card-001-cooling-bom.md](./2026-05-13_ia1_card-001-cooling-bom.md) |
| 改 dashboard next action 指向 cooling-bom HTML | ✅ | [ops/data/now.toml](../data/now.toml) |
| 把 cooling source 內化加成 blocker（learning 類） | ✅ | [ops/data/blockers.toml](../data/blockers.toml) |
| 把 cooling-bom HTML + 審稿 HTML 加進 dashboard pointers | ✅ | [ops/build_dashboard.py](../build_dashboard.py) |

## Workflow correction going forward（之後每張 card 都要遵守）

### 第二次修正：Domain Primer is the missing first layer

**2026-05-13 第二輪 audit**：user 讀完 cooling-bom HTML 後仍困惑，因為
他還不知道「散熱 / BOM / GB300 整櫃 / HBM / 被動元件 / ASIC BOM 是什麼」。

問題：**source tutor 預設 user 已經知道 domain 詞彙**。當這個預設不成立
時，source tutor 變成「解釋 source」而不是「教 domain」，使 user 無法
從 source 中學東西。

我們其實有對應的 skill：[`domain-doc-tutor`](/Users/dylanting/.cursor/skills/domain-doc-tutor/SKILL.md)，
專門做「domain knowledge / mental model / glossary」。但這個 skill 沒有
被 chain 進 content-production workflow，所以從來沒有 trigger。

修正：新增 **Domain Primer** 階段，放在 source tutor 之前。

### 完整 ship sequence（2026-05-13 v2）

```text
1. source packet（Source Collector role）

2. domain primer（NEW; Domain Primer role; uses domain-doc-tutor skill）
   - markdown canonical: research/notes/<theme>/<primer>.md
   - HTML reading view:  research/knowledge/<theme>/primers/<primer>.html
   - 涵蓋：mental model、glossary、common confusion、最小可記住版本
   - 成功標準：user 能用自己的話講出每個基本名詞

3. cross-source tutor note + paired HTML reading（Source Tutor role）
   - 預設 user 已讀完 primer
   - 重點：claim 強度 / 公開可引用度，不再解釋名詞

4. card draft（Content Production workflow）

5. paired HTML review page（HTML reading UI rule extended to reviews）

6. user 讀 HTML primer → HTML source tutor → HTML review
   依序看完才能進 IA1

7. agent 套用變更 → IA1 second pass

8. user 填 reflection 三題 → final approve

9. card frontmatter public_status: ready
```

### Decision: when does each user need Domain Primer?

| 訊號 | 是否需要 primer |
|---|---|
| User 主動問「X 是什麼」「X 用在哪裡」 | 必須 |
| User 看完 source 仍說「我沒學到東西」 | 必須 |
| User 看 card draft 困惑「為什麼是這幾家公司」 | 必須 |
| User 對 domain 已熟悉，要 verify claim | 可跳，直接 source tutor |
| 跨 domain 跳第一張 card（例如從 AI server 跳到 fintech） | 必須 |

### Rule promotion 暫不做

目前是第 1 張 card，2 次修正都有效。等 Card #001 完整 ship 後再考慮：

- 新增 `.cursor/rules/domain-primer.mdc`：「unfamiliar domain → primer first」
- 或在 `.cursor/rules/source-tutor-reading.mdc` 加 pre-condition：「assumes user has read theme primer; if not, route to Domain Primer」
- 或在 `content/templates/thesis-card.md` 內加「Pre-requisite primer」欄位

3 張 card 都跑完且順序穩定後再凍結。

---

如果一張 card 引用的 source 不到 3 份，可以用 single-source mode（仍要
paired HTML），但**不可跳過 source tutor**，也**不可跳過 domain primer**
（除非 user 已對該 domain 熟悉）。

## Candidate framework: Business / Investment Logic Chain

本次 user 指出另一個更抽象的缺口：知道名詞是什麼還不夠，還要知道**它怎麼
變成投資線索**。這其實可以抽象成一套通用 skill / rule，暫名：

```text
business-logic-chain
```

### Core logic

任何 component / company / theme 都要走同一條鏈：

```text
需求變化
→ 技術 / 物理 / 供應瓶頸
→ 必要零件 / 能力 / 產能
→ BOM / ASP / content per unit / volume 變化
→ 公司 revenue / margin / backlog 驗證
→ Counter：哪個環節不成立，投資線索就斷掉
```

### Required questions

1. **需求從哪裡來？**（hyperscaler capex、AI workload、政策、替代需求）
2. **哪個瓶頸被放大？**（power、memory bandwidth、CoWoS、供電穩定、散熱）
3. **哪個零件 / 能力從 optional 變 required？**
4. **BOM / ASP / volume 有沒有變大？還只是 narrative？**
5. **哪家公司卡在必要環節？是 component supplier、system integrator，還是 ODM？**
6. **財報怎麼驗證？**（revenue、gross margin、backlog、customer exposure、design win）
7. **Counter 是什麼？**（需求放緩、替代技術、供應鏈切換、價格下滑）

### Examples from this primer

| Component | Demand change | Bottleneck | Required capability | Company lens | Verification |
|---|---|---|---|---|---|
| 散熱 | AI 算力需求上升 | rack power 130kW+，風冷不夠 | cold plate / CDU / manifold / UQD | 奇鋐 / 雙鴻 / Vertiv | NVDA exposure、backlog、margin |
| HBM | GPU 算力提升 | memory wall | high-bandwidth memory near GPU | SK hynix / Micron / Samsung | HBM 配額、認證、ASP、gross margin |
| 被動元件 | AI 主板功耗上升 | 電壓穩定、供電波動 | 高階 MLCC / 電感 | Yageo / 村田 / 太陽誘電 | high-end mix、ASP、交期 |
| ASIC | hyperscaler 不想完全依賴 NVIDIA | 成本 / perf-per-watt / 自主性 | custom silicon design | Broadcom / Marvell / Alchip | design win、project size、ramp timing |

### Skill / rule promotion decision

先不要立刻建新 skill / rule。原因同上：Card #001 還沒完整 ship，流程仍在調整。
但若接下來 #002 / #003 也反覆需要這條鏈，就應該新增：

- `.cursor/rules/business-logic-chain.mdc`（讓每個 component analysis 都必須回答上述 7 問）
- 或 skill：`business-logic-tutor` / `investment-logic-chain`（把 domain concept 轉成 investable watchlist，不直接給買賣建議）

### Minimal future rule wording

```text
When explaining a domain component for investment use, do not stop at definition.
Always connect:
Demand change → bottleneck → required capability → BOM/ASP/volume change →
company exposure → financial verification → counter.
```

## 之後是否要把這條 sequencing 寫進 rule？

建議「再 ship 過 1-2 張 card」後再決定。理由：

- M1 階段 [docs/AGENT_ROLES.md](../../docs/AGENT_ROLES.md) 明示「roles
  before skills」「先 3 次重複再升 skill」。
- 這次是第 1 次正式從 backbone 萃 card；流程還在發掘。
- 直接寫 rule 容易凍結錯的順序。

如果未來 2-3 張 card ship 後仍維持上述順序，再考慮：

- 升級 `.cursor/rules/content-production-card.mdc`（新 rule，目前不存在）
- 或在 `content/templates/thesis-card.md` 補一段 ship sequence
- 或在 `.cursor/rules/source-tutor-reading.mdc` 加「card 引 source 前
  必須先有 paired reading」這條

本次先用 audit 記錄，rule promotion 之後再說。

## Reflection（process）

- **本次最大的學習**：rules 都在，但 agent 沒 chain 起來；rules 不會自動
  互相 trigger，agent 要主動把 Source Tutor 接在 Card draft 前。
- **未來的早期警示**：當 user 出現「我看不懂」「我感覺沒學到東西」「為什麼
  要我審這個」這類訊號，幾乎一定是 learning layer 被跳過了。
- **HTML-first 不只研究頁**：審稿頁也屬於人會反覆讀的 artifact，理應 HTML-
  first。本次 IA1 decision file 是個例外（為了 git diff 友善 + reviewer
  template 一致），但搭配 HTML review page 是更完整的 pattern。
- **第二輪反思（domain primer）**：補上 source tutor 後，user 仍困惑於
  「散熱 / BOM / GB300 / HBM / 被動元件 / ASIC BOM 是什麼」。所以
  source tutor 不是第一層學習；**domain primer 才是**。我們有 domain-doc-
  tutor skill 卻沒用上，這是工具齊全 + 流程未 chain 的典型例子。修正後
  9 步 ship sequence 把 primer 明確放在第二步。
- **Skill 庫存 vs workflow chain**：repo 提到「先做 roles，再升 skill」。
  本次 audit 顯示另一個 axis：「skill 存在 ≠ workflow chain 起來」。
  之後新加 skill 時，要同步問「這 skill 該被哪個 trigger 接起來」，否則
  skill 永遠不會 fire。
- **第三輪反思（voice lessons）**：Card #001 結構和 source confidence 都
  調順後，user 又指出公開稿仍像 AI：`不再只是...而是...`、`這不是 primary
  source...`、`為什麼 X...？` 這類句型不符合他的整理資料語氣。本次把已接受
  的寫作模式另存為 [2026-05-14_card-writing-voice-lessons.md](./2026-05-14_card-writing-voice-lessons.md)，
  暫不升 rule，先拿 #002 / #003 測試。

## Linked

- 對應 IA1 gate：[ops/decisions/2026-05-13_ia1_card-001-cooling-bom.md](./2026-05-13_ia1_card-001-cooling-bom.md)
- Card：[content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md](../../content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md)
- **Domain Primer HTML（NEW，Step 1 必讀）**：[research/knowledge/ai-server-supply-chain/primers/ai-server-components.html](../../research/knowledge/ai-server-supply-chain/primers/ai-server-components.html)
- Domain Primer markdown canonical：[research/notes/2026-05-13_ai-server-components-primer.md](../../research/notes/2026-05-13_ai-server-components-primer.md)
- HTML source tutor learning（Step 2）：[research/knowledge/ai-server-supply-chain/readings/cooling-bom.html](../../research/knowledge/ai-server-supply-chain/readings/cooling-bom.html)
- HTML review（Step 3）：[content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html](../../content/cards/reviews/2026-05-13_card-001-cooling-bom_review.html)
- Source tutor markdown：[research/source-tutor/ai-server-supply-chain/2026-05-13_cooling-bom-reading.md](../../research/source-tutor/ai-server-supply-chain/2026-05-13_cooling-bom-reading.md)
- 對應 skill：[`domain-doc-tutor`](/Users/dylanting/.cursor/skills/domain-doc-tutor/SKILL.md)（本次首度被 chain 進 content-production）
- Card voice lesson：[ops/decisions/2026-05-14_card-writing-voice-lessons.md](./2026-05-14_card-writing-voice-lessons.md)
