"""Shared renderer for the task-anchored lifecycle maps in this folder.

Same frame and visual language as the Stripe map's build script
(tasks/competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.build.py):
ten task columns, lanes for humans, agents and shared tools, handoffs drawn as
documented (solid), inferred (dashed) or unknown (amber, with a "?").
Output is one standalone HTML file: inline styles, system fonts, no scripts.
"""
from html import escape

W = 124; X0 = 20; NCOL = 10
TASKS = [["Spot the", "opportunity"], ["Talk to", "customers"], ["Research", "the problem"], ["Set the", "goal"],
         ["Shape the", "intent"], ["Plan the", "change"], ["Write the", "code"], ["Review the", "change"],
         ["Release"], ["Operate", "and learn"]]
CHAIN = ["Opportunity", "Problem", "Problem", "Goal", "Intent", "Plan", "Code", "", "", ""]


def cx(i):
    return X0 + W * i + W / 2


def _box(i, y, h, lines, cls="node", span=1, size=12.5):
    x = X0 + W * i + 6; w = W * span - 12
    t = ''.join(f'<tspan x="{x + w / 2:.1f}" dy="{0 if k == 0 else 15.5}">{escape(l)}</tspan>' for k, l in enumerate(lines))
    ty = y + h / 2 - (len(lines) - 1) * 7.75 + 4.5
    return (f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="7"/>'
            f'<text class="nt" style="font-size:{size}px" x="{x + w / 2:.1f}" y="{ty:.1f}" text-anchor="middle">{t}</text>')


def svg(d):
    """d: humans {col: lines}, human_accent [cols], agents {col: lines}, lite {col: lines}, auto {col: lines},
    shared str, links [(from_col, to_col, kind, label)] kind in doc|inf|gap, people_use [cols], up [(col, label)],
    down [(col, label)], legend_doc, legend_gap, caption, title."""
    S = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 620" role="img" aria-labelledby="dtitle"><title id="dtitle">{escape(d["title"])}</title>',
         '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker>'
         '<marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>']
    for i, t in enumerate(TASKS):
        S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>'
                 + (f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t) > 1 else '') + '</text>')
        if CHAIN[i] and (i == 0 or CHAIN[i] != CHAIN[i - 1]):
            S.append(f'<text class="chain" x="{cx(i):.1f}" y="66" text-anchor="middle">{CHAIN[i]}</text>')
        if i:
            S.append(f'<line class="guide" x1="{X0 + W * i}" y1="50" x2="{X0 + W * i}" y2="500"/>')
    for y, l in [(86, "HUMANS · ANY ROLE"), (226, "AGENTS"), (426, "SHARED")]:
        S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
    S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0 + W * NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="412" x2="{X0 + W * NCOL}" y2="412"/>')
    for i, l in d["humans"].items():
        S.append(_box(i, 96, 92, l, "pnode acc" if i in d.get("human_accent", []) else "pnode"))
    for i, l in d.get("agents", {}).items():
        S.append(_box(i, 238, 92, l))
    for i, l in d.get("lite", {}).items():
        S.append(_box(i, 238, 92, l, "node lite"))
    for i, l in d.get("auto", {}).items():
        S.append(_box(i, 238, 92, l, "auto"))
    S.append(_box(0, 436, 56, [d["shared"]], "sub", span=NCOL, size=13))

    def arrow(p, cls="doc", mk="ah"):
        S.append(f'<path class="{cls}" d="{p}" marker-end="url(#{mk})"/>')

    below = 0
    for a, b, kind, label in d.get("links", []):
        cls = {"doc": "doc", "inf": "inf", "gap": "gap"}[kind]
        mk = "ahg" if kind == "gap" else "ah"
        if kind == "gap":
            off = 26 if b - a > 1 else 30
            S.append(f'<path class="gap" d="M{cx(a) + off:.1f} 238 C{cx(a) + off + 14:.1f} 198 {cx(b) - off - 14:.1f} 198 {cx(b) - off:.1f} 236" marker-end="url(#ahg)"/>')
            mx = (cx(a) + cx(b)) / 2
            S.append(f'<circle class="gapdot" cx="{mx:.1f}" cy="206" r="12"/><text class="gapq" x="{mx:.1f}" y="212" text-anchor="middle">?</text>')
            if label:
                S.append(f'<text class="cap gapl" x="{mx + 18:.1f}" y="210" text-anchor="start">{escape(label)}</text>')
        elif b == a + 1:
            y = 284
            arrow(f"M{X0 + W * b - 6} {y}H{X0 + W * b + 6}", cls, mk)
        else:
            y0 = 330; dip = 372 + 14 * below; below += 1
            arrow(f"M{cx(a):.1f} {y0} C{cx(a):.1f} {dip} {cx(b) - 40:.1f} {dip} {cx(b) - 18:.1f} {y0 + 2}", cls, mk)
            if label:
                S.append(f'<text class="cap" x="{(cx(a) + cx(b)) / 2:.1f}" y="{dip + 8}" text-anchor="middle">{escape(label)}</text>')
    for i in d.get("people_use", []):
        arrow(f"M{cx(i):.1f} 188V236", "inf")
    for i, label in d.get("up", []):
        arrow(f"M{cx(i):.1f} 436V332")
        S.append(f'<text class="cap" x="{cx(i) + 5:.1f}" y="426">{escape(label)}</text>')
    for i, label in d.get("down", []):
        S.append(f'<path class="inf" d="M{cx(i):.1f} 332V434" marker-end="url(#ah)"/><text class="cap" x="{cx(i) - 5:.1f}" y="426" text-anchor="end">{escape(label)}</text>')
    ly = 530
    S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0 + 52}" y="{ly + 5}">{escape(d["legend_doc"])}</text>')
    S.append(f'<path class="inf" d="M{X0 + 250} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0 + 302}" y="{ly + 5}">inferred, or a person uses the agent for the task</text>')
    S.append(f'<path class="gap" d="M{X0 + 640} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0 + 692}" y="{ly + 5}">{escape(d["legend_gap"])}</text>')
    S.append(f'<text class="cap" x="{X0}" y="{ly + 40}">{escape(d["caption"])}</text>')
    S.append('</svg>')
    return '\n'.join(S)


CSS = '''/* Same language as the Stripe map: ink on cool paper, one amber accent for the undocumented handoff and the tasks only people do. System fonts, no scripts. */
:root{
  --paper:#f6f6f2; --surface:#ffffff; --ink:#1d2228; --muted:#5d6670; --rule:#d6d9d6; --accent:#b4580c; --accent-soft:#f5e3d2; --auto:#e9ecef; --lite:#f1f3f1;
  --serif:"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif; --sans:system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif; --mono:ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--paper:#15181b; --surface:#1d2125; --ink:#e7e9e6; --muted:#a3abb2; --rule:#343a40; --accent:#f0a35e; --accent-soft:#3a2a1c; --auto:#262b30; --lite:#22272b; color-scheme:dark}}
:root[data-theme="dark"]{--paper:#15181b; --surface:#1d2125; --ink:#e7e9e6; --muted:#a3abb2; --rule:#343a40; --accent:#f0a35e; --accent-soft:#3a2a1c; --auto:#262b30; --lite:#22272b; color-scheme:dark}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0; background:var(--paper); color:var(--ink); font-family:var(--sans); font-size:16px; line-height:1.55}
.wrap{max-width:1120px; margin:0 auto; padding-left:max(16px, env(safe-area-inset-left, 0px)); padding-right:max(16px, env(safe-area-inset-right, 0px)); padding-block:40px 64px; display:grid; grid-template-columns:minmax(0,1fr); gap:36px}
.wrap > *{min-width:0}
header{display:grid; gap:10px; max-width:70ch}
.eyebrow{font-family:var(--mono); font-size:12.5px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted)}
h1{font-family:var(--serif); font-weight:600; font-size:clamp(30px,4.4vw,44px); line-height:1.1; margin:0; text-wrap:balance}
h2{font-family:var(--serif); font-weight:600; font-size:24px; margin:0 0 10px; text-wrap:balance}
p{margin:0; max-width:70ch}
.lede{font-size:18px}
.answer{background:var(--surface); border:1px solid var(--rule); border-left:4px solid var(--accent); border-radius:6px; padding:20px 22px; display:grid; gap:12px}
.answer ol,.answer ul{margin:0; padding-left:22px; display:grid; gap:8px; max-width:72ch}
.diagram{overflow-x:auto; background:var(--surface); border:1px solid var(--rule); border-radius:6px; padding:12px}
.diagram svg{display:block; min-width:1040px; width:100%; height:auto}
.diagram .stage{font-family:var(--serif); font-weight:600; font-size:14.5px; fill:var(--ink)}
.diagram .chain{font-family:var(--serif); font-style:italic; font-size:13.5px; fill:var(--muted)}
.diagram .lane{font-family:var(--mono); font-size:11px; letter-spacing:.1em; fill:var(--muted)}
.diagram .cap,.diagram .leg{font-family:var(--sans); font-size:12.5px; fill:var(--muted)}
.diagram .gapl{fill:var(--accent); font-size:11.5px}
.diagram .leg{font-size:13.5px; fill:var(--ink)}
.diagram .guide{stroke:var(--rule); stroke-width:1; stroke-dasharray:2 5}
.diagram .lanerule{stroke:var(--rule); stroke-width:1.2}
.diagram .node{fill:var(--surface); stroke:var(--ink); stroke-width:1.6}
.diagram .node.lite{fill:var(--lite); stroke:var(--muted); stroke-width:1.2}
.diagram .pnode{fill:var(--paper); stroke:var(--muted); stroke-width:1.2}
.diagram .pnode.acc{fill:var(--accent-soft); stroke:var(--accent); stroke-width:1.6}
.diagram .auto{fill:var(--auto); stroke:var(--muted); stroke-width:1.2}
.diagram .sub{fill:var(--auto); stroke:none}
.diagram .nt{font-family:var(--sans); fill:var(--ink)}
.diagram .doc{fill:none; stroke:var(--ink); stroke-width:1.8}
.diagram .inf{fill:none; stroke:var(--muted); stroke-width:1.5; stroke-dasharray:5 5}
.diagram .gap{fill:none; stroke:var(--accent); stroke-width:2; stroke-dasharray:3 5}
.diagram .gapdot{fill:var(--paper); stroke:var(--accent); stroke-width:2}
.diagram .gapq{font-family:var(--serif); font-weight:600; font-size:16px; fill:var(--accent)}
.diagram .mk{stroke:var(--ink); stroke-width:1.5}
.diagram .mkg{stroke:var(--accent); stroke-width:1.5}
.tablewrap{overflow-x:auto; border:1px solid var(--rule); border-radius:6px; background:var(--surface)}
table{border-collapse:collapse; width:100%; min-width:760px; font-size:14.5px}
th,td{text-align:left; vertical-align:top; padding:10px 14px; border-bottom:1px solid var(--rule)}
th{font-family:var(--mono); font-size:12px; font-weight:500; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); background:var(--paper)}
tr:last-child td{border-bottom:none}
td:first-child{font-weight:600}
.status{font-family:var(--mono); font-size:12px; padding:2px 8px; border-radius:999px; border:1px solid var(--rule); white-space:nowrap; display:inline-block}
.s-doc{border-color:var(--ink)} .s-inf{color:var(--muted); border-style:dashed} .s-unk{color:var(--accent); border-color:var(--accent)}
.row-gap td{background:var(--accent-soft)}
section{display:grid; gap:12px}
ul.impl{margin:0; padding-left:20px; display:grid; gap:10px; max-width:74ch}
.counts{font-family:var(--mono); font-size:13px; color:var(--muted)}
.foot{font-size:13.5px; color:var(--muted); max-width:82ch}'''

STATUS = {"documented": "s-doc", "inferred": "s-inf", "unknown": "s-unk"}


def page(d, out):
    """d: page_title, eyebrow, h1, lede, answer_h2, answer_items [html], answer_note html, diagram (svg dict),
    tasks [(task, who, agents, artifact)], handoffs [(from_to, how, status, gap_bool)], counts str,
    implications [html], foot html. Text cells are HTML (already escaped where needed)."""
    rows = '\n'.join(f'      <tr><td>{t}</td><td>{w}</td><td>{a}</td><td>{r}</td></tr>' for t, w, a, r in d["tasks"])

    def st(s):
        return ' '.join(f'<span class="status {STATUS.get(p.split()[0], "s-inf")}">{p}</span>' for p in s.split(' / '))
    gapcls = ' class="row-gap"'
    hrows = '\n'.join(f'      <tr{gapcls if g else ""}><td>{ft}</td><td>{how}</td><td>{st(s)}</td></tr>' for ft, how, s, g in d["handoffs"])
    items = '\n'.join(f'    <li>{x}</li>' for x in d["answer_items"])
    impl = '\n'.join(f'    <li>{x}</li>' for x in d["implications"])
    body = f'''<div class="wrap">
<header>
  <div class="eyebrow">{d["eyebrow"]}</div>
  <h1>{d["h1"]}</h1>
  <p class="lede">{d["lede"]}</p>
</header>

<div class="answer">
  <h2>{d["answer_h2"]}</h2>
  <ol>
{items}
  </ol>
  <p>{d["answer_note"]}</p>
</div>

<div class="diagram" role="figure" aria-label="{escape(d["diagram"]["title"])}">
{svg(d["diagram"])}
</div>

<section>
  <h2>Task by task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>
{rows}
    </tbody>
  </table></div>
</section>

<section>
  <h2>Every handoff, task to task</h2>
  <p class="counts">{d["counts"]}</p>
  <div class="tablewrap"><table>
    <thead><tr><th>From → to</th><th>How</th><th>Status</th></tr></thead>
    <tbody>
{hrows}
    </tbody>
  </table></div>
</section>

<section>
  <h2>What it means for our options</h2>
  <ul class="impl">
{impl}
  </ul>
</section>

<p class="foot">{d["foot"]}</p>
</div>'''
    html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>{escape(d["page_title"])}</title>\n<style>\n{CSS}\n</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n')
    with open(out, 'w') as f:
        f.write(html)
    print('wrote', out)
