#!/usr/bin/env python3
"""ops/build_dashboard.py

Generate ops/dashboard.html and ops/current.md from canonical sources:

- ops/data/milestones.toml
- ops/data/now.toml
- ops/data/blockers.toml
- content/cards/*.md (frontmatter)
- ops/sessions/*.md (frontmatter)
- gh CLI (open + recently merged PRs; optional, graceful fallback)
- git CLI (current branch; optional)

Run:
    python3 ops/build_dashboard.py

Or:
    make dashboard

Zero third-party dependencies. Uses stdlib `tomllib` (Python 3.11+).

Linking strategy (mixed):
- .md / .yaml / .toml / .py source files -> open in editor via
  ``cursor://file/<absolute path>`` (override with env CURSOR_EDITOR_SCHEME).
- .html browser-readable pages -> relative path, opens in browser.
"""

from __future__ import annotations

import datetime
import html
import json
import os
import re
import subprocess
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
OPS_DIR = REPO_ROOT / "ops"
DATA_DIR = OPS_DIR / "data"
TEMPLATE_DIR = OPS_DIR / "templates"
SESSIONS_DIR = OPS_DIR / "sessions"
CARDS_DIR = REPO_ROOT / "content" / "cards"

DASHBOARD_OUT = OPS_DIR / "dashboard.html"
CURRENT_OUT = OPS_DIR / "current.md"

EDITOR_SCHEME = os.environ.get("CURSOR_EDITOR_SCHEME", "cursor")

E = html.escape  # tiny alias used by every renderer below

# Map status strings to a CSS class. Unknown statuses get an empty class
# (default neutral pill).
STATUS_CSS = {
    "active": "active",
    "draft": "draft",
    "blocked": "blocked",
    "blocker": "blocked",
    "done": "done",
    "completed": "done",
    "merged": "done",
    "paused": "paused",
    "handed-off": "paused",
    "outline": "",
    "ready": "active",
    "scheduled": "active",
    "published": "done",
    "archived": "paused",
}


def pill_css(status: str) -> str:
    return STATUS_CSS.get(status, "")


def pill_html(status: str) -> str:
    cls = pill_css(status)
    return f'<span class="pill{(" " + cls) if cls else ""}">{E(status)}</span>'


# ---------------------------------------------------------------------------
# Minimal YAML frontmatter parser (scalar-only)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body). Only flat scalar keys are parsed.

    Anything indented under a key (list items, nested dicts) is silently
    skipped. That is fine because the dashboard only consumes scalars.
    """
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    body_start = end + 5
    if end == -1:
        end = text.find("\n---", 4)
        if end == -1:
            return {}, text
        body_start = end + 4
    fm_text = text[4:end]
    body = text[body_start:]
    data: dict = {}
    for line in fm_text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0] in (" ", "\t"):
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        val = raw.strip()
        if not val:
            continue
        if (val.startswith('"') and val.endswith('"')) or (
            val.startswith("'") and val.endswith("'")
        ):
            val = val[1:-1]
        data[key] = val
    return data, body


def extract_title(body: str, fallback: str = "Untitled") -> str:
    for line in body.splitlines():
        m = re.match(r"^#\s+(.*)$", line.strip())
        if m:
            return m.group(1).strip()
    return fallback


def clean_card_title(title: str, card_id: str) -> str:
    """Strip 'Card #ID — ' or similar prefix so we can render it next to the id."""
    patterns = [
        rf"^Card\s*#?{re.escape(card_id)}\s*[—–\-:]\s*",
        rf"^#?{re.escape(card_id)}\s*[—–\-:]\s*",
    ]
    for p in patterns:
        new = re.sub(p, "", title).strip()
        if new and new != title:
            return new
    return title


def clean_session_title(title: str, letter: str) -> str:
    """Convert 'Session Status: Session C — Card #001 Cooling BOM' -> 'Card #001 Cooling BOM'."""
    if "—" in title:
        return title.split("—", 1)[1].strip()
    if " - " in title:
        return title.split(" - ", 1)[1].strip()
    return title


# ---------------------------------------------------------------------------
# Data loaders
# ---------------------------------------------------------------------------

def load_toml(path: Path) -> dict:
    with path.open("rb") as f:
        return tomllib.load(f)


@dataclass
class Card:
    id: str
    path: str
    title: str
    status: str
    lens: str = ""
    counter_direction: str = ""
    risk: str = ""


@dataclass
class Session:
    id: str
    letter: str
    path: str
    title: str
    status: str
    branch: str = ""
    scope: str = ""
    active_card: str = ""
    last_updated: str = ""


def load_cards() -> list[Card]:
    cards: list[Card] = []
    for path in sorted(CARDS_DIR.glob("*.md")):
        if path.name == "_index.md":
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        m = re.search(r"_(\d{3})\.md$", path.name)
        cid = m.group(1) if m else path.stem
        cards.append(
            Card(
                id=cid,
                path=path.relative_to(REPO_ROOT).as_posix(),
                title=extract_title(body, fallback=path.stem),
                status=fm.get("public_status", "outline"),
                lens=fm.get("lens", ""),
                counter_direction=fm.get("counter_direction", ""),
                risk=fm.get("risk", ""),
            )
        )
    cards.sort(key=lambda c: c.id)
    return cards


def load_sessions() -> list[Session]:
    sessions: list[Session] = []
    for path in sorted(SESSIONS_DIR.glob("*.md")):
        if path.name in {"_index.md"}:
            continue
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        letter_m = re.search(r"session-([a-z])(?:-|$)", path.name)
        letter = letter_m.group(1).upper() if letter_m else ""
        id_m = re.search(r"session-([a-z0-9-]+)", path.name)
        sid = id_m.group(1) if id_m else path.stem
        sessions.append(
            Session(
                id=sid,
                letter=letter,
                path=path.relative_to(REPO_ROOT).as_posix(),
                title=extract_title(body, fallback=f"Session {letter or sid}"),
                status=fm.get("status", "active"),
                branch=fm.get("branch", ""),
                scope=fm.get("scope", ""),
                active_card=fm.get("active_card", ""),
                last_updated=fm.get("last_updated", fm.get("created_at", "")),
            )
        )
    order = {"active": 0, "paused": 1, "handed-off": 2, "completed": 3}
    sessions.sort(key=lambda s: (order.get(s.status, 9), s.id))
    return sessions


def fetch_prs(state: str, limit: int = 5) -> list[dict]:
    try:
        out = subprocess.run(
            [
                "gh", "pr", "list", "--state", state, "--limit", str(limit),
                "--json", "number,title,url,mergedAt,headRefName,baseRefName,state",
            ],
            capture_output=True, text=True, timeout=10, check=False, cwd=REPO_ROOT,
        )
        if out.returncode != 0:
            return []
        return json.loads(out.stdout or "[]")
    except (FileNotFoundError, subprocess.TimeoutExpired, json.JSONDecodeError):
        return []


def current_branch() -> str:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=5, check=False, cwd=REPO_ROOT,
        )
        return out.stdout.strip() if out.returncode == 0 else ""
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return ""


# ---------------------------------------------------------------------------
# Link helpers (mixed scheme)
# ---------------------------------------------------------------------------

def link_editor(rel_from_repo_root: str) -> str:
    abs_path = (REPO_ROOT / rel_from_repo_root).resolve()
    return f"{EDITOR_SCHEME}://file/{abs_path.as_posix()}"


def link_browser_from_ops(rel_from_repo_root: str) -> str:
    abs_path = (REPO_ROOT / rel_from_repo_root).resolve()
    return os.path.relpath(abs_path, OPS_DIR).replace(os.sep, "/")


def link(rel_from_repo_root: str, *, force_editor: bool = False) -> str:
    """Mixed linking: editor for source files, browser-relative for .html."""
    if force_editor or not rel_from_repo_root.endswith(".html"):
        return link_editor(rel_from_repo_root)
    return link_browser_from_ops(rel_from_repo_root)


# ---------------------------------------------------------------------------
# HTML renderers
# ---------------------------------------------------------------------------

def render_text_with_code(s: str) -> str:
    """Render ``...`` as <code>...</code>, escaping the rest."""
    parts = re.split(r"(`[^`]+`)", s)
    out: list[str] = []
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) >= 2:
            out.append(f"<code>{E(p[1:-1])}</code>")
        else:
            out.append(E(p))
    return "".join(out)


def render_topbar(last_updated: str) -> str:
    return (
        '<div class="topbar">\n'
        '  <div class="left">\n'
        '    <span class="brand">Now Page</span>\n'
        '    <span class="crumb">/ ops / investment-kol-ops</span>\n'
        '  </div>\n'
        f'  <div class="right">最後更新 {E(last_updated)} · 自動生成 from frontmatter + data/*.toml</div>\n'
        '</div>'
    )


def render_hero(
    next_action: str,
    do_not: list[str],
    active_milestone: dict | None,
    active_branch: str,
    active_card: Card | None,
    active_session: Session | None,
) -> str:
    chips: list[str] = []
    if active_milestone:
        chips.append(
            f'<span class="chip active"><span class="label">milestone</span> '
            f'{E(active_milestone["id"])} active</span>'
        )
    if active_branch:
        chips.append(
            f'<span class="chip"><span class="label">branch</span> '
            f'<code>{E(active_branch)}</code></span>'
        )
    if active_card:
        chip_css = pill_css(active_card.status)
        chips.append(
            f'<span class="chip{(" " + chip_css) if chip_css else ""}">'
            f'<span class="label">task</span> '
            f'Card #{E(active_card.id)} {E(active_card.status)}</span>'
        )
    if active_session:
        chips.append(
            f'<span class="chip active"><span class="label">session</span> '
            f'Session {E(active_session.letter or active_session.id)}</span>'
        )
    do_not_html = (
        '<ul>' + "".join(f"<li>{render_text_with_code(d)}</li>" for d in do_not) + '</ul>'
    )
    return (
        '<section class="hero" aria-label="現在該做什麼">\n'
        '  <div class="eyebrow">下一步 · one next action</div>\n'
        f'  <h1>{render_text_with_code(next_action.strip())}</h1>\n'
        '  <div class="chips">\n    '
        + "\n    ".join(chips)
        + '\n  </div>\n'
        '  <div class="donot">\n'
        '    <span class="key">不要做</span>\n'
        f'    {do_not_html}\n'
        '  </div>\n'
        '</section>'
    )


def render_progress(milestones: list[dict]) -> str:
    parts: list[str] = []
    for i, m in enumerate(milestones):
        status = m.get("status", "todo")
        cls = "done" if status == "done" else ("active" if status == "active" else "todo")
        parts.append(
            f'<div class="step {cls}"><span class="dot"></span>'
            f'<span class="name">{E(m.get("id", ""))}</span>'
            f'<span class="sub">{E(m.get("label", ""))}</span></div>'
        )
        if i < len(milestones) - 1:
            # Connector is "done" only if BOTH neighbors are done OR the next step is done.
            next_status = milestones[i + 1].get("status", "todo")
            connector_done = status == "done" and next_status in {"done", "active"}
            # More commonly, mark connector done only between done<->done.
            connector_done = status == "done" and next_status == "done"
            parts.append(
                f'<div class="connector{" done" if connector_done else ""}"></div>'
            )
    return (
        '<div class="section-label">Milestone 進度</div>\n'
        '<section class="progress" aria-label="Milestone 進度">\n'
        '  <div class="track">\n    '
        + "\n    ".join(parts)
        + '\n  </div>\n'
        '</section>'
    )


def render_lane_item_card(card: Card) -> str:
    short_title = clean_card_title(card.title, card.id)
    return (
        '<div class="item">\n'
        '  <div class="head">\n'
        f'    <span class="title"><a href="{E(link(card.path))}">'
        f'Card #{E(card.id)} · {E(short_title)}</a></span>\n'
        f'    {pill_html(card.status)}\n'
        '  </div>\n'
        f'  <div class="desc">lens：{E(card.lens or "—")} · counter：{E(card.counter_direction or "—")}'
        f'{" · risk：" + E(card.risk) if card.risk else ""}</div>\n'
        '</div>'
    )


def render_lane_item_session(s: Session) -> str:
    desc = E(s.scope) if s.scope else ""
    footer = f'<span>branch <code>{E(s.branch)}</code></span>' if s.branch else ""
    short_title = clean_session_title(s.title, s.letter)
    return (
        '<div class="item">\n'
        '  <div class="head">\n'
        f'    <span class="title"><a href="{E(link(s.path))}">'
        f'Session {E(s.letter or s.id)} — {E(short_title)}</a></span>\n'
        f'    {pill_html(s.status)}\n'
        '  </div>\n'
        + (f'  <div class="desc">{desc}</div>\n' if desc else "")
        + (f'  <div class="footer">{footer}</div>\n' if footer else "")
        + '</div>'
    )


def render_lane_item_blocker(b: dict) -> str:
    title = f"{b.get('title', '')} · {b.get('scope', '')}".rstrip(" ·")
    btype = b.get("type", "blocker")
    return (
        '<div class="item">\n'
        '  <div class="head">\n'
        f'    <span class="title">{render_text_with_code(title)}</span>\n'
        f'    <span class="pill blocked">{E(btype)}</span>\n'
        '  </div>\n'
        f'  <div class="desc">{render_text_with_code(b.get("detail", ""))}</div>\n'
        '</div>'
    )


def render_lane_item_pr(pr: dict) -> str:
    title = f"PR #{pr.get('number', '?')} · {pr.get('title', '')}"
    state = (pr.get("state") or "").lower()
    pill_class = "done" if state == "merged" else "active"
    label = "merged" if state == "merged" else state or "open"
    detail = ""
    if pr.get("headRefName"):
        detail = f"<code>{E(pr['headRefName'])}</code> → <code>{E(pr.get('baseRefName', 'main'))}</code>"
    return (
        '<div class="item">\n'
        '  <div class="head">\n'
        f'    <span class="title"><a href="{E(pr.get("url", "#"))}">{E(title)}</a></span>\n'
        f'    <span class="pill {pill_class}">{E(label)}</span>\n'
        '  </div>\n'
        + (f'  <div class="desc">{detail}</div>\n' if detail else "")
        + '</div>'
    )


def render_lanes(
    sessions: list[Session],
    active_card: Card | None,
    blockers: list[dict],
    merged_prs: list[dict],
    open_prs: list[dict],
) -> str:
    active_items: list[str] = []
    for s in sessions:
        if s.status == "active":
            active_items.append(render_lane_item_session(s))
    if active_card and active_card.status != "ready":
        active_items.append(render_lane_item_card(active_card))
    for pr in open_prs:
        active_items.append(render_lane_item_pr(pr))

    blocked_items = [render_lane_item_blocker(b) for b in blockers]
    done_items = [render_lane_item_pr(pr) for pr in merged_prs]

    def lane(name: str, label: str, items: list[str]) -> str:
        return (
            f'<section class="lane {name}" aria-label="{label}">\n'
            '  <header>\n'
            f'    <h3><span class="dot-mark"></span>{label}</h3>\n'
            f'    <span class="count">{len(items)} items</span>\n'
            '  </header>\n'
            + ("\n".join("  " + line for line in "\n".join(items).splitlines()) if items else "  <div class=\"desc\" style=\"color:var(--muted)\">無</div>")
            + '\n</section>'
        )

    return (
        '<div class="section-label">三欄狀態 · active / blocked / done</div>\n'
        '<div class="lanes">\n'
        + lane("active", "進行中", active_items)
        + "\n"
        + lane("blocked", "阻塞中", blocked_items)
        + "\n"
        + lane("done", "近期完成", done_items)
        + "\n</div>"
    )


def render_reference(
    sessions: list[Session],
    cards: list[Card],
) -> str:
    # Sessions list
    sess_lis = []
    for s in sessions:
        short = clean_session_title(s.title, s.letter)
        sess_lis.append(
            f'<li>{pill_html(s.status)} '
            f'<a href="{E(link(s.path))}">Session {E(s.letter or s.id)} — {E(short)}</a></li>'
        )

    # Cards list
    card_lis = []
    for c in cards:
        meta = " · ".join([x for x in [c.lens, c.counter_direction] if x])
        short = clean_card_title(c.title, c.id)
        card_lis.append(
            f'<li>{pill_html(c.status)} '
            f'<a href="{E(link(c.path))}">#{E(c.id)} {E(short)}</a> '
            f'<span class="label">{E(meta)}</span></li>'
        )

    # Pointers
    pointers = [
        ("md", "ops/current.md", "本頁的 markdown 來源"),
        ("md", "content/cards/_index.md", "Cards 規範與全表"),
        ("md", "ops/sessions/_index.md", "Sessions 規範與全表"),
        ("html", "content/drafts/2026-05-12_ai-server-supply-chain_internal-article.html", "Backbone article"),
        ("html", "research/knowledge/ai-server-supply-chain/index.html", "Knowledge map"),
        ("md", "docs/IMPLEMENTATION_PLAN.md", "Implementation plan"),
        ("md", "ops/tooling-dashboard-options.md", "Tooling options survey"),
        ("md", "ops/build_dashboard.py", "Dashboard generator 程式"),
        ("md", "ops/data/now.toml", "Hero 文案（next_action / do_not）"),
        ("md", "ops/data/milestones.toml", "Milestone 狀態"),
        ("md", "ops/data/blockers.toml", "Blockers 清單"),
    ]
    pointer_lis = []
    for kind, rel, desc in pointers:
        if not (REPO_ROOT / rel).exists():
            continue
        pointer_lis.append(
            f'<li><span class="label">{kind}</span> '
            f'<a href="{E(link(rel))}">{E(rel)}</a> · {E(desc)}</li>'
        )

    return (
        '<div class="section-label">Sessions · Cards · 守則 · 入口</div>\n'
        '<div class="reference">\n'
        '<div class="ref-block">\n'
        '  <h3>Sessions</h3>\n'
        '  <ul>\n    ' + "\n    ".join(sess_lis) + '\n  </ul>\n'
        '</div>\n'
        '<div class="ref-block">\n'
        '  <h3>Cards · AI Server Supply Chain v1</h3>\n'
        '  <ul>\n    ' + "\n    ".join(card_lis) + '\n  </ul>\n'
        '</div>\n'
        '<div class="ref-block">\n'
        '  <h3>工作守則</h3>\n'
        '<pre>1. 開 ops/dashboard.html，先讀 Hero。\n'
        '2. 在 active branch 上只做那一件下一步。\n'
        '3. 停下來前更新對應 markdown frontmatter，再跑：\n'
        '   python3 ops/build_dashboard.py  (or `make dashboard`)\n'
        '4. 想開新研究分支或 worktree 時 → STOP，\n'
        '   先回去看 Hero 區的「不要做」。</pre>\n'
        '  <p class="small">一個 active task = 一條 branch。Session 是 chat 邊界，不是 branch。</p>\n'
        '</div>\n'
        '<div class="ref-block">\n'
        '  <h3>常用入口</h3>\n'
        '  <ul>\n    ' + "\n    ".join(pointer_lis) + '\n  </ul>\n'
        '</div>\n'
        '</div>'
    )


def render_html(context: dict) -> str:
    css = (TEMPLATE_DIR / "dashboard.css").read_text(encoding="utf-8")
    body_parts = [
        render_topbar(context["last_updated"]),
        render_hero(
            context["now"]["next_action"],
            context["now"]["do_not"],
            context["active_milestone"],
            context["active_branch"],
            context["active_card"],
            context["active_session"],
        ),
        render_progress(context["milestones"]),
        render_lanes(
            context["sessions"],
            context["active_card"],
            context["blockers"],
            context["merged_prs"],
            context["open_prs"],
        ),
        render_reference(context["sessions"], context["cards"]),
        '<footer>Static HTML cockpit · 由 <code>ops/build_dashboard.py</code> 自動生成 · 編輯 markdown frontmatter 與 <code>ops/data/*.toml</code> 後重跑即可。</footer>',
    ]
    return (
        "<!doctype html>\n"
        '<html lang="zh-Hant">\n'
        "<head>\n"
        '<meta charset="utf-8" />\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1" />\n'
        "<title>Now Page — Investment KOL Ops</title>\n"
        "<style>\n"
        + css
        + "\n</style>\n"
        "</head>\n"
        "<body>\n\n"
        "<!-- DO NOT EDIT. Generated by ops/build_dashboard.py. -->\n\n"
        + "\n\n".join(body_parts)
        + "\n\n</body>\n</html>\n"
    )


# ---------------------------------------------------------------------------
# Markdown renderer (ops/current.md)
# ---------------------------------------------------------------------------

def render_markdown(context: dict) -> str:
    now = context["now"]
    milestones = context["milestones"]
    sessions: list[Session] = context["sessions"]
    cards: list[Card] = context["cards"]
    blockers: list[dict] = context["blockers"]
    merged_prs: list[dict] = context["merged_prs"]
    open_prs: list[dict] = context["open_prs"]
    active_milestone = context["active_milestone"]
    active_card: Card | None = context["active_card"]
    active_session: Session | None = context["active_session"]
    active_branch = context["active_branch"]

    def md_link(rel: str, label: str | None = None) -> str:
        return f"[{label or rel}]({rel})"

    lines: list[str] = []
    lines.append("---")
    lines.append("artifact_type: current-status")
    lines.append(f"created_at: {datetime.date.today().isoformat()}")
    lines.append(f"last_updated: {context['last_updated']}")
    lines.append("generated_by: ops/build_dashboard.py")
    lines.append("---")
    lines.append("")
    lines.append("<!-- DO NOT EDIT. Generated by ops/build_dashboard.py. -->")
    lines.append("")
    lines.append("# Now Page")
    lines.append("")
    lines.append(
        "> Single source of truth for \"what is happening right now in this repo.\""
    )
    lines.append(">")
    lines.append("> **Read this file at the start of every session.**")
    lines.append("> Visual cockpit: open `ops/dashboard.html` in browser.")
    lines.append("> Edit `ops/data/*.toml` or session/card frontmatter and re-run")
    lines.append("> `python3 ops/build_dashboard.py` to refresh.")
    lines.append("")

    # Right Now
    lines.append("## Right Now")
    lines.append("")
    lines.append(f"- **Next action**: {now['next_action'].strip()}")
    if active_milestone:
        lines.append(f"- **Milestone**: `{active_milestone['id']}` — {active_milestone.get('label', '')}")
    if active_branch:
        lines.append(f"- **Branch**: `{active_branch}`")
    if active_card:
        short = clean_card_title(active_card.title, active_card.id)
        lines.append(
            f"- **Task**: Card #{active_card.id} `{active_card.status}` — {short}"
        )
    if active_session:
        lines.append(
            f"- **Session**: Session {active_session.letter or active_session.id} "
            f"`{active_session.status}`"
        )
    lines.append("")
    lines.append("**Do not start**:")
    lines.append("")
    for d in now["do_not"]:
        lines.append(f"- {d}")
    lines.append("")

    # Milestones
    lines.append("## Milestones")
    lines.append("")
    lines.append("| Milestone | Status | Notes |")
    lines.append("|---|---|---|")
    for m in milestones:
        lines.append(
            f"| {m.get('id', '')} {m.get('label', '')} | {m.get('status', '')} | {m.get('description', '')} |"
        )
    lines.append("")

    # Sessions
    lines.append("## Sessions")
    lines.append("")
    lines.append("| Session | Status | Branch | Scope |")
    lines.append("|---|---|---|---|")
    for s in sessions:
        short = clean_session_title(s.title, s.letter)
        label = f"Session {s.letter or s.id} — {short}"
        link_md = md_link(s.path, label)
        branch_cell = f"`{s.branch}`" if s.branch else "—"
        lines.append(f"| {link_md} | {s.status} | {branch_cell} | {s.scope or ''} |")
    lines.append("")

    # Cards
    lines.append("## Cards")
    lines.append("")
    lines.append("| ID | Title | Lens | Status | Counter |")
    lines.append("|---|---|---|---|---|")
    for c in cards:
        short = clean_card_title(c.title, c.id)
        title_md = md_link(c.path, short)
        lines.append(
            f"| {c.id} | {title_md} | {c.lens or '—'} | {c.status} | {c.counter_direction or '—'} |"
        )
    lines.append("")

    # Blockers
    lines.append("## Blockers")
    lines.append("")
    for b in blockers:
        lines.append(f"- **{b.get('title', '')}** ({b.get('scope', '')}, `{b.get('type', '')}`) — {b.get('detail', '')}")
    lines.append("")

    # Recent PRs
    if merged_prs:
        lines.append("## Recently Merged PRs")
        lines.append("")
        for pr in merged_prs:
            lines.append(
                f"- PR #{pr.get('number', '?')} — {pr.get('title', '')} ({pr.get('url', '')})"
            )
        lines.append("")
    if open_prs:
        lines.append("## Open PRs")
        lines.append("")
        for pr in open_prs:
            lines.append(
                f"- PR #{pr.get('number', '?')} — {pr.get('title', '')} ({pr.get('url', '')})"
            )
        lines.append("")

    lines.append("## Working Rule")
    lines.append("")
    lines.append("```text")
    lines.append("1. Open ops/dashboard.html, read the Hero.")
    lines.append("2. Do exactly one next action on the active branch.")
    lines.append("3. Update markdown frontmatter, then run:")
    lines.append("   python3 ops/build_dashboard.py   # or: make dashboard")
    lines.append("4. If you are about to open a new research branch or worktree,")
    lines.append("   STOP and re-check the 'Do not start' list above.")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_context() -> dict:
    milestones_data = load_toml(DATA_DIR / "milestones.toml")
    now_data = load_toml(DATA_DIR / "now.toml")
    blockers_data = load_toml(DATA_DIR / "blockers.toml")

    milestones = milestones_data.get("milestones", [])
    blockers = blockers_data.get("blockers", [])
    sessions = load_sessions()
    cards = load_cards()
    merged_prs = fetch_prs("merged", limit=5)
    open_prs = fetch_prs("open", limit=5)

    active_milestone = next((m for m in milestones if m.get("status") == "active"), None)
    active_session = next((s for s in sessions if s.status == "active"), None)
    active_branch = (active_session.branch if active_session else "") or current_branch()
    active_card: Card | None = None
    if active_session and active_session.active_card:
        active_card = next(
            (c for c in cards if c.id == active_session.active_card), None
        )
    if active_card is None:
        active_card = next((c for c in cards if c.status == "draft"), None)

    last_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    return {
        "now": now_data,
        "milestones": milestones,
        "blockers": blockers,
        "sessions": sessions,
        "cards": cards,
        "merged_prs": merged_prs,
        "open_prs": open_prs,
        "active_milestone": active_milestone,
        "active_session": active_session,
        "active_card": active_card,
        "active_branch": active_branch,
        "last_updated": last_updated,
    }


def main() -> int:
    ctx = build_context()
    html_out = render_html(ctx)
    md_out = render_markdown(ctx)
    DASHBOARD_OUT.write_text(html_out, encoding="utf-8")
    CURRENT_OUT.write_text(md_out, encoding="utf-8")

    print(f"wrote {DASHBOARD_OUT.relative_to(REPO_ROOT)}")
    print(f"wrote {CURRENT_OUT.relative_to(REPO_ROOT)}")
    print(f"  active milestone: {ctx['active_milestone']['id'] if ctx['active_milestone'] else 'none'}")
    print(f"  active branch:    {ctx['active_branch'] or 'none'}")
    print(f"  active session:   {ctx['active_session'].id if ctx['active_session'] else 'none'}")
    print(f"  active card:      #{ctx['active_card'].id if ctx['active_card'] else 'none'}")
    print(f"  cards loaded:     {len(ctx['cards'])}")
    print(f"  sessions loaded:  {len(ctx['sessions'])}")
    print(f"  merged PRs:       {len(ctx['merged_prs'])}")
    print(f"  open PRs:         {len(ctx['open_prs'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
