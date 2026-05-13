---
workflow: content-production
artifact_type: thesis-card
risk: high
lens: 破局
platform_target: x+threads
counter_direction: bull-kill
backbone_ref: content/drafts/2026-05-12_ai-server-supply-chain_internal-article.md
backbone_section: "What Would Change My Mind"
sources:
  - AMD Q1 2026 earnings call + 2025 Analyst Day (reported-fact + forward-target)
  - Intel Q1 2026 earnings call (reported-fact)
  - MediaTek Q1 2026 earnings call transcript (reported-fact for $2B framing)
created_at: 2026-05-13
public_status: outline
target_word_count: 400-500
---

# Card #005 — 3 個會讓我下調 AI server CPU 復興 thesis 的具體數字

> Outline 狀態：3 個 invalidation threshold 已從 backbone "What Would
> Change My Mind" 段萃出。需要把 threshold 數字 calibrate 得更具體
> （目前是合理估計）。
>
> 這張 card 是「破局 lens」的 prototype——要證明你不是只會喊 thesis，
> 而是公開預先 commit「什麼數字會讓我改變看法」。這個透明度是中文圈
> 投資 KOL 幾乎沒人在做的。

## Hook

> 寫出 thesis 容易，公開寫出「什麼會推翻我自己 thesis」很少人做。
>
> 我把 AI server CPU 復興 thesis 拆成 3 個 quarterly 訊號——這 3 個數字
> 任一個沒打到 threshold，我會在自己的 watchlist 上降級。**這是公開的
> commitment，不是事後解釋。**

## Observation

當下我對 AI server CPU 復興 thesis 的 conviction：

- **CPU**：source-backed（AMD / Intel Q1 已 print），thesis 啟動
- **AMD vs Intel framework**：AMD 攻擊線、Intel 修復 + 政策線（兩條 valuation
  framework 不同）
- **MediaTek**：ASIC / subsystem optionality，不是 CPU 主受惠

但 thesis 啟動 ≠ thesis 兌現。市場會用接下來 1-2 個 quarterly print 重新
校準 thesis 強度。下面 3 個是我會主動聽的訊號 + threshold。

## Mechanism

> 為什麼是這 3 個訊號（不是其他）：

每一個都是 **獨立、可觀察、有 quarterly cadence、threshold 可以 pre-commit**
的訊號：

1. **AMD Data Center growth**：是 thesis 最直接的 share gain 證明
2. **Intel DCAI 內 Xeon 拆分**：是「Intel 修復線」的關鍵驗證
3. **MediaTek ASIC 主晶片 design win**：是「台廠 AI server optionality」
   能否兌現的 binary 訊號

3 個訊號都來自不同公司、不同 segment、不同 valuation 角色——避免單點失敗
誤判整體 thesis。如果 3 個都 confirm → thesis 升級為 reported-fact，
conviction 加碼；如果 2 個 confirm → 維持目前判斷；如果 < 2 個 confirm →
降級為「single-vendor share gain」而非「結構性 CPU 復興」。

## Implication（這張 card 的 Implication 直接 = 3 個 invalidation threshold）

### Threshold #1 — AMD

**如果 AMD Q2 2026 季報 Data Center revenue growth < +40% YoY**（vs Q1
+57%）**且**管理層下修 server CPU demand forward guidance：

- → CPU 復興 thesis **降級**：從「結構性需求」改寫成「single-vendor share
  gain」
- → AMD valuation framework 從「growth 加碼」回到「commodity cycle」
- 觀察日期：2026/07/29 前後（AMD Q2 法說預期日）

### Threshold #2 — Intel

**如果 Intel Q2 2026 季報 DCAI 沒有 explicit Xeon segment growth disclosure**，
**或** Xeon vs ASIC 拆分顯示 Xeon 動能 **< 季增 10%**（vs DCAI 整體 Q1
+22% YoY）：

- → Intel **從修復線降為純敘事**：CPU control plane 沒有轉成收入
- → Intel valuation framework 回到「Foundry pure-play + 政策 floor」
- 觀察日期：2026/07/24 前後（Intel Q2 法說預期日）

### Threshold #3 — MediaTek

**如果 MediaTek 在 2026 Q3 法說（10/30 前後）無法 confirm AI ASIC 主晶片
design win**（hyperscaler 客戶名稱 + project size），**且** subsystem
revenue 占 ASIC segment > 70%：

- → 台廠 AI server **optionality 降級**：MediaTek 故事從「ASIC 主晶片切
  入」改寫成「subsystem ramp 但無主晶片」
- → 估值倍數 derate 預期 15-25%（historical guidance miss pattern）
- 觀察日期：2026/10/30 前後

## Counter（bull-case kill applied to my own bull thesis）

> 這張 card 本身就是 Counter——public commitment 我自己 thesis 的
> invalidation。所以 Counter section 在這張變成 meta：threshold 本身
> 會不會錯？

**threshold 是我目前判斷的合理 calibration，不是市場 consensus。**

- AMD threshold +40% YoY 對應 Q1 +57% 約 -17pp 下修——如果你的 conviction
  更高（例如要看 -25pp 以上才降級），threshold 可以提到 +30%
- Intel threshold 季增 10% 是合理 baseline 但不是強 anchor，可以調整 ±3pp
- MediaTek threshold 主晶片 design win + subsystem < 70% 是 binary check，
  比較難調整

**重點不是 threshold 對不對，是寫下你的 threshold 並對它負責。**事後修改
threshold 是 cognitive bias 的入口，請 freeze threshold + 接受結果。

## Caveat

3 個 threshold 都假設「正常 quarterly 揭露」。如果出現 macro shock（Fed
emergency cut / 地緣事件 / 重大 hyperscaler capex 修正），threshold 需要
重新 contextualize——但這個重新 contextualize 必須在 macro event 之前先
寫下，不能事後 retrofit。

我目前還沒驗證的：MediaTek threshold 的 subsystem 70% 比例是 source-derived
合理估計，需要在 Q2 法說後 calibrate（如果 Q2 揭露 subsystem ratio，可以
更新 threshold）。

## CTA + Footer

```text
完整「What Would Change My Mind」list（含 backbone 8 條支線各自的
invalidation threshold）在 library：
crayonding.io/library/ai-server-supply-chain#invalidation
（library 上線前暫填 placeholder URL）

下一張是這個 backbone 的最後一張——meta lens：
為什麼我把被動元件這條標成「evidence chain 偏窄」。

本內容是研究與教育，不是投資建議。3 個 threshold 是個人判斷，
公開出來是為了 commit falsifiability。
```

## Platform Adaptation Notes

- **X long post**：3 個 threshold 用 numbered + 醒目格式（threshold 數字
  + 觀察日期）。Hook 強調「公開 commitment」。
- **Threads carousel**（8 slides）：
  - Slide 1: Hook（公開 commitment 的元 message）
  - Slide 2: 3 個訊號 overview（為什麼這 3 個）
  - Slide 3: Threshold #1 AMD
  - Slide 4: Threshold #2 Intel
  - Slide 5: Threshold #3 MediaTek
  - Slide 6: Threshold 本身會不會錯（meta-Counter）
  - Slide 7: Caveat（macro shock 例外）
  - Slide 8: CTA + 「freeze threshold 不事後修改」commitment

## Review Checklist

- [ ] Hook 用 lens 命名（破局）+ 強調公開 commitment 元 message
- [ ] 3 個 threshold 各自獨立、可觀察、有 quarterly cadence
- [ ] 每個 threshold 有 explicit 數字 + 觀察日期
- [ ] Counter（meta）承認 threshold 本身可能 calibrate 錯
- [ ] Caveat 承認 macro shock 例外但要求 pre-commit
- [ ] 「freeze threshold 不事後修改」明確
- [ ] CTA 連 backbone
- [ ] 字數 400-500
- [ ] 過 IA1 gate（含 thesis invalidation 公開宣稱，risk: high）

## Pre-publish TODO

- [ ] 確認 AMD Q2 2026 法說日期（07/29 是預期，公告日要 cross-check）
- [ ] 確認 Intel Q2 2026 法說日期
- [ ] 確認 MediaTek Q3 2026 法說日期
- [ ] Polish hook（這張 hook 是元 message，要寫得有重量）
- [ ] 過 IA1 gate
- [ ] 確認 backbone library URL

## Metrics（發布後填）

```yaml
metrics:
  impressions_24h:
  impressions_72h:
  impressions_7d:
  likes_7d:
  reposts_7d:
  replies_7d:
  saves_7d:
  follows_attributed:
  link_clicks:
  qualitative:
    - 
  reflection:
    repeat_pattern: 
    drop_pattern: 
```
