---
artifact_type: rule-revision-proposal
related_pr: "#13 (feat/m21-public-readiness-complete)"
target_files:
  - .cursor/rules/analysis-reasoning.mdc
  - content/templates/internal-article.md
status: proposal
created_at: 2026-05-13
reviewer: CrayonDing0909
---

# Analysis-Reasoning Rule v2 — Suggested Sharpenings

> 這份是 PR #13 review 過程中產出的 3 個進階建議，捕捉在這裡是為了：
>
> 1. PR #13 還沒 merge，避免在那條 branch 上動工干擾另一個 session。
> 2. 這 3 個建議的精神已經先套用到 `content/templates/thesis-card.md`，
>    讓 thesis card 從 day 1 就遵守 v2 規則。
> 3. PR #13 merge 後，下個 session（或 user）可以直接拿這份當 patch list
>    去更新 `analysis-reasoning.mdc` 與 `internal-article.md` template。
>
> Background：PR #13 在 `analysis-reasoning.mdc` 把 article 寫作從 fact
> aggregation 升級成 4 步因果鏈（Observation → Mechanism → Implication →
> Counter）。Counter 是這次升級裡最有價值的單一欄位。下面 3 個建議是把
> Counter 從「好設計」推到「殺手級設計」的具體 sharpening。

## Suggestion 1：Counter 升級為 per-observation required

### 現行 v1（PR #13）

```text
The Counter is optional per observation but should appear at least once per
section.
```

### 建議 v2

```text
Counter is required for every important observation, not just once per
section. An "important observation" is any one whose Mechanism / Implication
the article actually relies on for its conclusion.

Section-level Counter (only one per section) is acceptable only when:
- The section contains a single chained mechanism (one main + supporting),
  in which case the Counter applies to the chain as a whole.
```

### 理由

- 「每節 1 條」實務上會讓 author 把最弱的 observation 放在 Counter 後面、
  不再 stress-test，因為 Counter 配額已經用掉。
- Per-observation required 強制 author 對每個 important claim 都 publicly
  commit falsifiability，這是這條規則的核心價值。
- PR #13 的 article 實際上每段都寫了 Counter（HBM / 散熱 / 被動 / Apple-Intel
  / CHIPS Act），實證證明 per-observation 是可行的工作量。

### 套用範圍

更新位置：`.cursor/rules/analysis-reasoning.mdc` 的 `## Preferred Shape per Branch`
段落（行 78-86）。

## Suggestion 2：Counter 必須帶 threshold / time-window

### 現行 v1（PR #13）

```text
Counter (what would break this mechanism)
```

### 建議 v2

```text
Counter (what would break this mechanism, with explicit threshold and/or
time-window — name a specific number/event AND a calendar window so the
reader knows when to start or stop watching)
```

加到 `## Avoid` 區塊（行 49-62）：

```text
- **Vague Counter**: "如果 demand 變弱..." / "如果競爭加劇...".
  Counter must name a specific threshold (number, ratio, event) and a
  time-window so the reader knows when to start / stop watching.
```

加到 `## Required Behavior` 後面，作為新的 Worked Counter Example：

```text
Good Counter (具體 threshold + time-window):
  "如果 18A-P yield 在 2027 年中前仍 < 70%，Apple 合作會推遲；
   PR #13 article 已有的版本：'再過 6 個月仍無正式公告 → 視為 stuck'。"

Good Counter (結構性 threshold):
  "如果 NVIDIA 後續架構 per-chip power 退回 700W 內，液冷必要性
   會局部回退到空冷。但目前 Blackwell / Rubin roadmap 都還在
   per-chip power 上升方向，這個 counter 至少 2027 之前不會發生。"

Bad Counter (vague):
  "如果 yield 不好，Apple 會走人。"

Bad Counter (no time-window):
  "如果 demand 變弱，散熱受惠會打折。"
```

### 理由

- 沒有 threshold 的 Counter 等於沒有 falsifiability——「demand 變弱」永遠可以
  解釋成「還沒夠弱」。
- Time-window 把 Counter 從「概念上會破」變成「具體哪一季財報、哪個事件可以
  驗證」，這直接對應你 4 個 lens 中的「啟動 / 破局」lens。
- PR #13 的散熱 Counter（「2027 之前不會發生」）已經是 v2 標準的範本，只是
  其他 Counter 還沒一致 enforce。

### 套用範圍

- 更新 `.cursor/rules/analysis-reasoning.mdc` 的 `## Preferred Shape per Branch`
  與 `## Avoid` 區塊。
- 更新 `content/templates/internal-article.md` 的 `### Evidence + Reasoning`
  範例（行 67-79），把現有 cooling Counter 加上明確 time-window。

## Suggestion 3：Counter 是雙向的（kill bull AND falsify bear）

### 現行 v1（PR #13）

規則裡沒有明確說 Counter 是雙向。實際 article 已經有雙向 Counter（MediaTek
那段是 falsify bear case），但規則沒明說 → 未來 author 會默認 Counter = kill
bull case。

### 建議 v2

在 `## Preferred Shape per Branch` 後面新增 `## Counter Direction` 章節：

```text
## Counter Direction

Counter does not only mean "what would kill the bull case". It includes
two directions, and both count toward falsifiability:

1. **Bull-case kill**: what observable event would invalidate the main
   bullish mechanism.
   - Example (ASIC): "如果 NVIDIA 把 inference 卡價格殺到接近 ASIC 總擁有
     成本，hyperscaler 自研 ASIC 動機降低。"

2. **Bear-case falsification**: what observable event would weaken the
   stated risk / bear thesis.
   - Example (MediaTek): "如果 MediaTek 在 2026 Q2 / Q3 法說公布具體主晶片
     design win（hyperscaler 客戶 + project size），track-record 與
     subsystem-confusion 兩個風險會降低。"

The point is to publicly commit to falsifiability, not to win an argument.
A section that has only bull-case Counters is asymmetric — it tests only
upside risk, not the durability of the stated downside.

當你寫的是 risk-heavy section（例如 MediaTek 4 個風險），優先寫
bear-case falsification Counter；當你寫的是 thesis-heavy section
（例如 HBM / 散熱），優先寫 bull-case kill Counter。
```

### 理由

- PR #13 article 實際上已經兩種都用了，但規則沒 explicit 化會導致：
  (a) 風險段落（MediaTek 4 個 risks）的 Counter 變成「再加一個 bull-case
      kill」，跟段落主題錯位。
  (b) 讀者分不清作者的 Counter 是在 stress-test bullish thesis 還是
      bearish risk。
- 雙向 Counter 強迫 author 對自己的 bear case 也保持 humility，避免「risk
  寫得很驚人但其實不可被 falsify」的常見錯誤。

### 套用範圍

新增章節到 `.cursor/rules/analysis-reasoning.mdc`，建議放在 `## Preferred
Shape per Branch`（行 76-86）之後、`## Review Checklist`（行 88-102）之前。

更新 Review Checklist 加 1 條：

```text
- [ ] 對於 risk-heavy section，Counter 是 bear-case falsification（不是
      多一個 bull-case kill）？
```

## 套用順序與 Owner

PR #13 merge 後，建議的 follow-up order：

1. **小 commit 1**（5-10 min）：套用 Suggestion 1 + 2 到
   `analysis-reasoning.mdc`。
2. **小 commit 2**（10 min）：套用 Suggestion 3 新增 `## Counter Direction`
   章節 + Review Checklist 新增 1 條。
3. **小 commit 3**（10 min）：更新 `content/templates/internal-article.md`
   範例 Counter 加 time-window。
4. **小 commit 4**（5 min）：在 `content/templates/thesis-card.md` 加
   `analysis-reasoning.mdc` 連結（thesis card template 已經套用 v2 精神，
   只差連結）。

可以三個 commit 一個 PR，或合成一個 chore PR。

## Decision

- Decision: defer（等 PR #13 merge 後再 apply）
- Owner: CrayonDing0909 / 下個 session
- Estimated effort: 30-40 min total

## Linked Files

- PR #13: feat/m21-public-readiness-complete
- Current rule: `.cursor/rules/analysis-reasoning.mdc`（在 PR #13 branch 上）
- Current template: `content/templates/internal-article.md`（在 PR #13 branch 上）
- Pre-applied template: `content/templates/thesis-card.md`（本 branch）
