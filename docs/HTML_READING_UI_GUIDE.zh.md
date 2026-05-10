# HTML Reading UI Guide（中文版）

> 中文鏡像 / 對照原文：[HTML_READING_UI_GUIDE.md](HTML_READING_UI_GUIDE.md)
> 英文是 LLM 主用版本；中文供人類 review 用。

目的：定義本 repo 的人類閱讀用 HTML 頁面應該怎麼做。

這不是視覺設計系統。目標是閱讀品質：好掃讀、confidence 清楚、source 可追、降低認知負擔。

## 核心原則

```text
人類閱讀路徑：HTML first
Canonical source / metadata：Markdown
```

只要使用者會閱讀、學習、review、反覆回來看，就需要 HTML reading page。Markdown 保留為
機器可讀 source 與 git-friendly metadata layer。

## 哪些東西需要 HTML Reading Page

必須要：

- Knowledge map：`research/knowledge/<theme>/index.html`
- Topic page：`research/knowledge/<theme>/<topic>.html`
- Source reading view：`research/knowledge/<theme>/sources.html`
- 使用者可能點進去看的 individual source packet：`sources/<source>.html`
- Tutor Q&A reading view：`qa.html` 與較長的 Q&A 頁（例如 `cpu-qa.html`）
- 使用者會從 source card 點進去看的 intake page：`intakes/<source>.html`

可選：

- Internal brief，如果 markdown 變得不好讀。
- Decision log，如果 gate review 變得視覺上複雜。

不需要：

- `.gitkeep`
- raw source packet markdown
- canonical intake markdown
- 很短的 metadata-only docs

## Page Types

### Knowledge Map Page

範例：`research/knowledge/ai-server-supply-chain/index.html`

必須包含：

- Breadcrumb。
- Title。
- 一段 umbrella thesis。
- Status metadata。
- Topic cards。
- Relationship map。
- 已知事實 / 市場敘事 / 未驗證假設。
- Open questions backlog。
- Reading entry points。
- Sources / Q&A links。

### Topic Page

範例：`cpu.html`、`asic.html`。

必須包含：

- Breadcrumb。
- One-line thesis。
- What is it?
- Where is it used?
- Why it matters now?
- Industry trend。
- Companies / tickers。
- Market pricing。
- Open questions。
- Sources。

### Sources Reading View

範例：`sources.html`。

必須包含：

- 怎麼讀這頁。
- 每個 source packet 一張 card。
- Why this source matters。
- Key numbers。
- 必要時放 direct quote。
- Reliability label。
- Follow-up tasks。
- HTML source / HTML intake links 優先。
- Markdown source links 只能作 fallback，並明確標成 `md source`。

### Individual Source Page

範例：`sources/amd-q1-2026.html`。

必須包含：

- Source quality：primary / secondary / unverified。
- Why this source matters。
- Key numbers table。
- Direct quotes。
- Reliability notes。
- Follow-up tasks。
- HTML intake link 優先。
- Markdown source packet link 次之。

### Tutor Q&A Page

範例：`qa.html`、`cpu-qa.html`。

必須包含：

- 用使用者語言寫的問題。
- Short answer。
- Mental model。
- Technical explanation。
- Why investors care。
- Companies / tickers。
- What to watch。
- What is still unknown。
- Sources。

## Link Rules

人類閱讀用 HTML 頁面必須優先連到 HTML。

Good:

```html
<a href="./sources/amd-q1-2026.html">HTML source</a> ·
<a href="./intakes/amd-q1-2026.html">HTML intake</a> ·
<a href="../../sources/.../amd-q1-2026-source-packet.md">md source</a>
```

Bad:

```html
<a href="../../intake/2026-05-10_gooeye-ep659_cpu.md">intake</a>
```

規則：

- 不要把 Markdown 連結標成 `source`、`intake`、`Q&A`。
- 如果連到 Markdown，要標成 `md source`、`markdown intake`、或 `markdown canonical`。
- 如果還沒有 HTML 版，先連到上一層 HTML reading view，再附 Markdown fallback。

## Status Labels

使用簡單文字標籤，不要只靠顏色。

可用 labels：

- `draft`
- `reviewed`
- `needs follow-up`
- `primary`
- `secondary`
- `unverified`
- `do not publish as fact yet`
- `gate-pending`
- `gate-approved`
- `gate-deferred`

高風險 claim 要用白話寫 warning，不要只用 badge。

## Layout Rules

- M1-M2 只用 static HTML。
- 只用 inline CSS。
- 不用 framework。
- 不用外部 assets。
- 不用 JS，除非後續 milestone 明確需要 collapsible sections。
- 內容寬度大約 `760px-920px`。
- 手機 375px 可讀。
- 可比較 metrics 用 table。
- source packet、topic summary、warning 用 cards。
- 段落短一點：2-4 句。
- 用 list 幫助掃讀。

## Visual Style

保持樸素、好讀。

要做：

- 適合長時間閱讀的舒適對比。避免純黑 / 純白直接互打。
- 清楚 headings。
- 輕量 borders。
- 一致 spacing。
- Breadcrumbs。
- Section 底部有 source links。
- 靠近 claim 的 reliability warning。

建議閱讀配色：

```css
:root {
  --bg: #f6f7f9;
  --surface: #ffffff;
  --surface-muted: #edf1f5;
  --text: #24272d;
  --muted: #68707d;
  --line: #d8dee6;
  --link: #315f9f;
  --warn-bg: #fff4dc;
  --warn-text: #6b4b00;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #17191d;
    --surface: #20242a;
    --surface-muted: #2a3038;
    --text: #e2e8f0;
    --muted: #a8b1bd;
    --line: #3a424e;
    --link: #91b7ff;
    --warn-bg: #332813;
    --warn-text: #f1d18a;
  }
}
```

原因：

- Light mode 用中性 off-white，降低純白刺眼但不偏黃。
- Dark mode 用 soft dark，避免純黑背景 + 純白字造成疲勞。
- `muted` 只用在 metadata 與次要說明，不用在主要 claim。
- Warning 色在 light / dark mode 都要可讀。

避免：

- Gradients。
- Decorative animations。
- Heavy shadows。
- Emoji 當 icons。
- 太多顏色。
- 巨大的 hero section。
- Marketing-style copy。
- 隱藏不確定性。

## Accessibility Checklist

交付前檢查：

- [ ] Page 有清楚 `<title>`。
- [ ] Header 有 breadcrumb 和 H1。
- [ ] Links 清楚可辨。
- [ ] Source confidence 用文字標出。
- [ ] Tables 有 headers。
- [ ] 關鍵資訊不只靠顏色表示。
- [ ] 手機寬度可讀。

## Review Checklist

Commit 新 HTML reading page 前檢查：

- [ ] 它有回答使用者需要理解的東西嗎？
- [ ] 第一屏能讓讀者知道自己在哪裡嗎？
- [ ] Primary vs secondary sources 有清楚分開嗎？
- [ ] Follow-up questions 明顯嗎？
- [ ] Markdown links 是否明確標成 fallback？
- [ ] 不開 markdown 也能讀懂這頁嗎？

