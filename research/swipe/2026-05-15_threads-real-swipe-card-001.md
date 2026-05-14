---
workflow: algorithm-research
artifact_type: real-swipe-pass
created_at: 2026-05-15
platform: threads
target_artifact: content/cards/2026-05-13_ai-server_funds-cooling-bom_001.md
risk: medium
status: draft
access_note: public Threads access partial; some metrics/full text unavailable
---

# Threads Real Swipe Pass — Card #001

> Goal: validate Card #001 against real Threads formats, especially native
> long-form text attachments and collapsed preview behavior. This supplements
> the official Threads ranking docs and the UI pattern pass.

## Access Note

Threads pages were only partially accessible without login. Some examples expose
text and visible counts, but metric labels / full reply context are not always
available. Treat visible counts as directional only.

## Five Threads Examples

| # | Creator / Source | Topic | Hook / Outer Post | Format | Visible metrics | What it teaches Card #001 |
|---|---|---|---|---|---|---|
| 1 | `@threads` official | text attachment launch | `If 500 characters aren’t enough, this one’s for you.` | outer post + gray text attachment | `7.7K / 1.1K / 1.3K / 378` | Make the outer post solve an obvious pain; attachment delivers depth |
| 2 | `@metanewsroom` | 10k character attachments | `You can now attach up to 10k characters...` | outer post + takeaways in attachment | `237 / 16 / 31 / 9` | Put takeaways early; show the format by using the format |
| 3 | `@conno_r` | TechCrunch text attachment | `You can now attach text directly...` | outer post + external article preview | `586 / 88 / 61 / 27` | Text attachment works for source-backed previews, but original synthesis is stronger than quoted article text |
| 4 | `@steadycompound` | AI chip architecture | `Hyperscalers are pouring hundreds of billions... yet most people still don’t understand...` | standard educational thread | `72 / 15 / 12 / 19` | Knowledge-gap hook + taxonomy works for complex investing topics |
| 5 | `@benedictevans` | Apple Intelligence | `Apple... proposing a different answer: LLMs are commodity infrastructure, not platforms.` | compact strategic frame + link | `125 / 11 / 20` | One-sentence contrarian frame can work if the idea is sharp |

## Threads-Native Patterns

### Pattern 1 — Short outer post + deeper attachment

Threads now supports long-form text attachments. The feed can show:

```text
outer post
gray preview card
tap to expand full text
```

For Card #001, use:

```text
Outer post:
GB300 一櫃要花接近 $50K 在液冷上。

我原本以為這只是散熱概念股，整理完覺得不是這樣。
```

### Pattern 2 — Preview begins with reader psychology

The screenshot pattern works because it starts with:

```text
你第一個反應是什麼？
```

For Card #001:

```text
你第一個反應可能是：
「散熱不就是風扇嗎？」
「又是 AI server 題材？」
「最重要的不還是 GPU？」
```

This is more native than opening with source caveats.

### Pattern 3 — Keep long-form coherent, not over-fragmented

The better Threads direction is **not** 10 separate numbered replies. It is a
single long-form attachment with clear paragraphs and section-like rhythm.

For Card #001:

```text
first reaction
→ rack context
→ heat / thermal throttle
→ liquid cooling parts
→ BOM meaning
→ company mapping
→ watchlist logic
→ counter
→ CTA
```

### Pattern 4 — Put source link after the value

Threads has limited outbound link traffic. The post must deliver the core value
inside Threads. The library link should be at the end.

### Pattern 5 — Ask for missing context, not generic engagement

Better CTA:

```text
你會先追散熱、HBM，還是 ASIC 這幾條線？
```

Potential stronger CTA for later:

```text
如果你有奇鋐 / 雙鴻 / Vertiv 法說裡更直接的 NVDA exposure 線索，丟給我，我會回頭更新供應鏈地圖。
```

## Recommended Threads Version

Use native long-form attachment:

```text
Outer post:
GB300 一櫃要花接近 $50K 在液冷上。

我原本以為這只是散熱概念股，整理完覺得不是這樣。

Text attachment:
你第一個反應可能是：
「散熱不就是風扇嗎？」
「又是 AI server 題材？」
「最重要的不還是 GPU？」

...full reasoning...
```

This is now reflected in Card #001.

## What To Validate After Publishing

- Do people open the text attachment?
- Do replies respond to the psychological opener or to the company list?
- Does the CTA produce useful replies?
- Does the library link get clicks despite being at the end?
- Do named companies attract low-quality ticker replies?
