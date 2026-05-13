#!/usr/bin/env bash
# ops/build_library.sh
#
# Build the public "library" subset of this repo for Vercel deployment.
# Copies only the HTML reading artifacts that are safe to publish; never
# touches research/sources, research/source-tutor, ops/sessions, decisions,
# .cursor/, docs/, or any markdown canonical files.
#
# Usage:
#   bash ops/build_library.sh
#
# Output:
#   ./dist/
#     index.html                                          (landing)
#     library/ai-server-supply-chain/...                  (HTML knowledge map + topic pages)
#     content/drafts/2026-05-12_ai-server-supply-chain_internal-article.html
#
# Run by Vercel (see vercel.json buildCommand) and locally for previews.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST="$ROOT/dist"

echo "[build_library] cleaning $DIST"
rm -rf "$DIST"
mkdir -p "$DIST"

# --- Library: AI Server Supply Chain (HTML reading subset) ------------------

KNOWLEDGE_SRC="$ROOT/research/knowledge/ai-server-supply-chain"
LIBRARY_DST="$DIST/library/ai-server-supply-chain"

if [[ -d "$KNOWLEDGE_SRC" ]]; then
  echo "[build_library] copy knowledge map -> library/ai-server-supply-chain/"
  mkdir -p "$LIBRARY_DST"
  # Only copy *.html and image assets; never markdown sidecars or other files.
  # Use find + cp for portability (Vercel build image has no rsync).
  (
    cd "$KNOWLEDGE_SRC"
    find . -type f \( \
        -name '*.html' -o \
        -name '*.png'  -o \
        -name '*.jpg'  -o \
        -name '*.jpeg' -o \
        -name '*.svg'  -o \
        -name '*.webp' \
      \) -print0 | while IFS= read -r -d '' rel; do
        rel="${rel#./}"
        target_dir="$LIBRARY_DST/$(dirname "$rel")"
        mkdir -p "$target_dir"
        cp "$rel" "$target_dir/$(basename "$rel")"
    done
  )
else
  echo "[build_library] WARNING: $KNOWLEDGE_SRC not found, skipping"
fi

# --- Public article drafts (HTML only) --------------------------------------

ARTICLES_SRC="$ROOT/content/drafts"
ARTICLES_DST="$DIST/content/drafts"

if [[ -d "$ARTICLES_SRC" ]]; then
  echo "[build_library] copy public article HTML -> content/drafts/"
  mkdir -p "$ARTICLES_DST"
  shopt -s nullglob
  for f in "$ARTICLES_SRC"/*.html; do
    name="$(basename "$f")"
    cp "$f" "$ARTICLES_DST/$name"
    echo "  + $name"
  done
  shopt -u nullglob
fi

# --- Landing index.html -----------------------------------------------------

echo "[build_library] write dist/index.html"
cat > "$DIST/index.html" <<'HTML'
<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>CrayonDing Library</title>
<style>
  :root {
    --bg: #fafafa; --surface: #ffffff; --line: #e4e4e7; --text: #18181b;
    --muted: #71717a; --accent: #4f46e5; --accent-soft: #eef2ff;
    color-scheme: light;
  }
  @media (prefers-color-scheme: dark) {
    :root { --bg: #1a1a1d; --surface: #232327; --line: #353539; --text: #fafafa;
            --muted: #a1a1aa; --accent: #a5b4fc; --accent-soft: #2a2570; }
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    font-family: "Inter var", "Inter", ui-sans-serif, system-ui, -apple-system,
      "PingFang TC", "Noto Sans CJK TC", sans-serif;
    font-size: 14px; line-height: 1.6; color: var(--text); background: var(--bg);
    padding: 56px 28px; max-width: 720px; margin: 0 auto;
    -webkit-font-smoothing: antialiased;
  }
  h1 { font-size: 28px; font-weight: 600; letter-spacing: -0.015em; margin: 0 0 8px; }
  .lede { color: var(--muted); margin: 0 0 32px; }
  .section { margin-bottom: 32px; }
  .section h2 {
    font-size: 11px; font-weight: 600; letter-spacing: 0.08em;
    text-transform: uppercase; color: var(--muted); margin: 0 0 12px;
  }
  .card {
    display: block;
    background: var(--surface);
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 10px;
    text-decoration: none;
    color: var(--text);
    transition: border-color 120ms ease, transform 120ms ease;
  }
  .card:hover { border-color: var(--accent); transform: translateY(-1px); }
  .card .title { font-weight: 600; font-size: 15px; margin: 0 0 4px; }
  .card .desc { font-size: 13px; color: var(--muted); margin: 0; }
  footer { color: var(--muted); font-size: 12px; margin-top: 48px; }
</style>
</head>
<body>
  <h1>CrayonDing Library</h1>
  <p class="lede">投資研究的公開閱讀區。完整的因果鏈、source 標註、Counter scenario 都放在這裡。</p>

  <section class="section">
    <h2>產業地圖</h2>
    <a class="card" href="library/ai-server-supply-chain/">
      <p class="title">AI Server Supply Chain</p>
      <p class="desc">CPU / ASIC / HBM / 散熱 / 被動元件 + Manufacturing / Procurement / Geopolitics 三條結構性 layer。</p>
    </a>
  </section>

  <section class="section">
    <h2>完整文章</h2>
    <a class="card" href="content/drafts/2026-05-12_ai-server-supply-chain_internal-article.html">
      <p class="title">AI Server Supply Chain — Internal Article v1</p>
      <p class="desc">三條主敘事 + 三條結構性 layer 的完整研究地圖。</p>
    </a>
  </section>

  <footer>本內容是研究與教育，不是投資建議。</footer>
</body>
</html>
HTML

echo "[build_library] done. files:"
find "$DIST" -type f | sed "s|$ROOT/||"
