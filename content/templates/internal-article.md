---
workflow: content-production
artifact_type: internal-article-template
risk: medium
created_at: YYYY-MM-DD
source_brief: <research/notes/...>
status: template
---

# Internal Article Template

> Purpose: convert a source-backed research brief into a readable internal article
> draft. This is not public-ready by default.

## Frontmatter Fields

```yaml
workflow: content-production
artifact_type: internal-article-draft
risk: high
created_at: YYYY-MM-DD
source_brief: <path>
source_decision: <path>
status: internal-draft
public_status: not-public-ready
target_audience: <who this is for>
content_pillar: market-understanding
```

## Draft Structure

### Title

<one clear title>

### Hook

<concrete pain / surprising observation / useful question>

### Context

<why this topic is relevant now>

### Main Thesis

<one thesis paragraph; no certainty language>

### Framework

<how to think about the topic>

### Evidence + Reasoning

Each evidence point must walk the 3-step causal chain defined in
[`.cursor/rules/analysis-reasoning.mdc`](../../.cursor/rules/analysis-reasoning.mdc):

```text
Observation (what the source actually says, with source label)
→ Mechanism (why A causes B, in plain Chinese, not institutional phrasing)
→ Implication (which company / signal / timeframe to watch)
→ Counter (optional per point; required at least once per section): what
  would break this mechanism?
```

Example:

```text
Observation: GB200 NVL72 散熱 BOM 約 $41,500/櫃，GB300 上修到 ~$49,860，占整
             櫃成本 42%（TrendForce / EE Times China 整理）。
Mechanism:   Hopper H100 700W → Blackwell 1000W → Rubin 約 1300W，單顆 power
             已穿透空氣冷卻物理上限 (~700W)。一旦穿透，cold plate + CDU +
             manifold + UQD 整套液冷成為必要 BOM，不是選配。
Implication: 結構性受惠台廠是奇鋐（冷板 30%+ 市占）、雙鴻（manifold），加上
             美系 Vertiv（CDU 35%+ 價值份額）。觀察訊號是 NVDA 下一代
             reference design power envelope + 這三家季報 NVDA 平台暴露。
Counter:     如果 NVIDIA 後續架構從密集大顆轉成更多顆但每顆 power 下修
             （例如 chiplet 切更細 + per-chip 700W 內），液冷必要性會局部
             回退到空冷。
```

Fact aggregation without mechanism (e.g. "GB300 散熱 BOM $49,860 → 所以 X 受惠")
is rejected by this template.

### What I Think

<personal POV; must be clearly framed as research, not advice>

### What Would Change My Mind

<3 observable invalidation signals>

### What I Still Need To Verify

<primary-source gaps before public publishing>

### Reader Takeaway

<what the reader should understand / watch next>

### Disclaimer

This is research and education, not financial advice.

