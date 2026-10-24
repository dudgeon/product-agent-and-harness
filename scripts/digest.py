#!/usr/bin/env python3
"""Build digest.html: open tasks, what needs Geoff, and recent director actions.

Reads tasks/*.md frontmatter, DIRECTOR.md ("## Needs Geoff", "## Queue") and the
tail of log.md. Run after each block of work: python3 scripts/digest.py
"""
import html
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORDER = ["waiting", "active", "in-progress", "suggested", "done", "dropped"]


def fm(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""


def md_inline(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
    return s


def bullets(block):
    items = [re.sub(r"^(\d+\.|-)\s+", "", l.strip()) for l in block.splitlines() if re.match(r"\s*(\d+\.|-)\s", l)]
    return "".join(f"<li>{md_inline(i)}</li>" for i in items) or "<li>Nothing.</li>"


tasks = []
for p in sorted((ROOT / "tasks").glob("*.md")):
    f = fm(p.read_text())
    last = [l for l in p.read_text().splitlines() if l.startswith("- 20")]
    tasks.append((f.get("status", "?"), f.get("title", p.stem), f"tasks/{p.name}", last[-1][2:] if last else ""))
tasks.sort(key=lambda t: (ORDER.index(t[0]) if t[0] in ORDER else 9, t[1]))
director = (ROOT / "DIRECTOR.md").read_text()
log = [l[2:] for l in (ROOT / "log.md").read_text().splitlines() if l.startswith("- ")][-8:]

rows = "".join(
    f'<div class="task {html.escape(s)}"><span class="st">{html.escape(s)}</span>'
    f'<a href="{href}">{html.escape(t)}</a><p>{md_inline(l[:240])}</p></div>'
    for s, t, href, l in tasks if s not in ("dropped",))
page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Project digest</title>
<style>
:root{{--bg:#faf8f4;--fg:#1d1b18;--muted:#6b665e;--line:#e4dfd6;--accent:#b4532a;--card:#fff}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#16150f;--fg:#ece7de;--muted:#a39d92;--line:#2e2b25;--accent:#e08a5c;--card:#1f1d18}}}}
:root[data-theme="dark"]{{--bg:#16150f;--fg:#ece7de;--muted:#a39d92;--line:#2e2b25;--accent:#e08a5c;--card:#1f1d18}}
body{{background:var(--bg);color:var(--fg);font:16px/1.5 -apple-system,system-ui,sans-serif;margin:0;padding:16px;max-width:760px;margin-inline:auto}}
h1{{font-size:1.4rem;margin:.2rem 0}} h2{{font-size:1rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:1.6rem 0 .5rem}}
.meta{{color:var(--muted);font-size:.85rem}} a{{color:var(--accent)}} code{{font-size:.85em}}
ul{{padding-left:1.2rem}} li{{margin:.3rem 0}}
.task{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin:8px 0}}
.task a{{font-weight:600;text-decoration:none}} .task p{{margin:.3rem 0 0;color:var(--muted);font-size:.85rem}}
.st{{display:inline-block;font-size:.7rem;text-transform:uppercase;letter-spacing:.05em;border:1px solid var(--line);border-radius:99px;padding:0 8px;margin-right:8px;color:var(--muted)}}
.waiting .st{{border-color:var(--accent);color:var(--accent)}}
</style></head><body>
<h1>Product agent and harness</h1><div class="meta">Digest built {datetime.now():%Y-%m-%d %H:%M}</div>
<h2>Needs you</h2><ul>{bullets(section(director, "Needs Geoff"))}</ul>
<h2>Queue</h2><ul>{bullets(section(director, "Queue (what starts when)"))}</ul>
<h2>Tasks</h2>{rows}
<h2>Recent</h2><ul>{"".join(f"<li>{md_inline(l)}</li>" for l in log)}</ul>
</body></html>"""
(ROOT / "digest.html").write_text(page)
print("wrote digest.html:", len(tasks), "tasks")
