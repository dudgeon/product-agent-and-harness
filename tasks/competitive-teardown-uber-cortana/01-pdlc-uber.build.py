"""Build 01-pdlc-uber.html: a standalone lifecycle map of Uber's agent ecosystem by task.

Usage: python3 01-pdlc-uber.build.py [OUT_DIR]   (defaults to this file's folder)
Same frame as the Stripe map's build script; inline styles only, no external scripts or fonts.
"""
import sys, os, html
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
W = 124; X0 = 20; NCOL = 10
cx = lambda i: X0 + W * i + W / 2
tasks = [["Spot the", "opportunity"], ["Research the", "opportunity"], ["Write the", "PRD"], ["Design:", "mock-ups"],
         ["Plan the", "change"], ["Write the", "code"], ["Validate", "(inner loop)"], ["Review the", "change"],
         ["Release and", "experiment"], ["Operate,", "maintain"]]
chain = ["Idea", "Business research", "Requirements", "Figma designs", "Code changes", "Minion", "Inner loop", "Outer loop", "", "Maintenance"]

# Handoffs: (from -> to, mechanism, status) where status is doc, docmech, inf or unk
HANDOFFS = [
    ("Slack thread → research (Cortana)", "Tag Cortana in the thread", "doc"),
    ("Cortana in Slack → Cortana on the web", "Open Cortana into a web interface from Slack", "doc"),
    ("Research → requirements → mock-ups → code-change analysis (all Cortana)", "One assistant, shown step by step in one demo", "doc"),
    ("Context graph → every Cortana answer", "The graph is the “default grounding”; Cortana navigates it, then reads deeper", "doc"),
    ("Team persona → channel members", "Custom skills and prompt bound to a team Slack channel; several people collaborate there", "doc"),
    ("Shaped intent (Cortana) → write code (Minion)", "“we hand off from that Cortana agent” to Minion; what crosses is not shown", "docmech"),
    ("Requirements (Cortana) → PRD/ERD tool (uPlan)", "Not described", "unk"),
    ("PRD → PRD Evaluator → revised PRD", "A PM runs the evaluator on a PRD and its linked docs; it scores and suggests text, never approves", "doc"),
    ("Requirements (Cortana) → PRD Evaluator", "Not described", "unk"),
    ("uPlan docs and reviews → context graph", "“all of this data also goes into the graph”", "doc"),
    ("PRD → ERD → Jira or Linear task", "Links held in uPlan; AI clusters and back-fills missing links to measure feature time", "doc"),
    ("Slack thread, plan or spec → write code (Minion)", "“@minion, follow this thread … create a PR”; plan mode; templates", "doc"),
    ("Figma mock-ups → validate", "Simulator screenshot compared with the Figma spec", "doc"),
    ("Draft PR → validate → review", "Minion stops at a draft PR; inner-loop checks; the PR carries a table of checks", "doc"),
    ("PR → uReview, Code Inbox → human reviewer", "Risk score and routing; a person reviews every PR; a “green lane” only later", "doc"),
    ("CI failure → fix", "Self-healing CI", "doc"),
    ("Release → experiment → decision", "A/B variants planned in the demo; launch and readout not shown", "inf"),
    ("Service enrolled → maintenance loop → diffs", "Managed, scheduled, rate-limited loops", "doc"),
    ("Landed or rejected diffs → better skills", "Diffs and comments used as labels", "doc"),
    ("Incident reviews → new maintenance skills", "Monthly", "doc"),
    ("Bug report → DebugAssist RCA → Minion PR on the Jira task", "Hand off the RCA; the PR is attached to the Jira task", "doc"),
    ("Customer or user research → research (Cortana)", "Not described", "unk"),
    ("Production data and health → next opportunity", "Cortana produces health reports and runs queries; not shown as a loop", "inf"),
    ("Agent Builder agents ↔ Cortana personas", "Both bind a prompt and tools to a team; no source links them", "unk"),
    ("ChatGPT Work ↔ Cortana", "ChatGPT Work reached 30,000+ staff on 22 Oct 2026; the split with Cortana is not stated", "unk"),
]
LABEL = {"doc": ("documented", "s-doc"), "docmech": ("documented, mechanism unknown", "s-mech"), "inf": ("inferred", "s-inf"), "unk": ("unknown", "s-unk")}
n_doc = sum(s in ("doc", "docmech") for _, _, s in HANDOFFS)
n_mech = sum(s == "docmech" for _, _, s in HANDOFFS)
n_inf = sum(s == "inf" for _, _, s in HANDOFFS)
n_unk = sum(s == "unk" for _, _, s in HANDOFFS)
COUNTS = f"{len(HANDOFFS)} handoffs: {n_doc} documented ({n_mech} with its mechanism unknown), {n_inf} inferred, {n_unk} unknown"

S = []
def box(i, y, h, lines, cls="node", span=1, size=12.5):
    x = X0 + W * i + 6; w = W * span - 12
    t = ''.join(f'<tspan x="{x + w / 2:.1f}" dy="{0 if k == 0 else 15.5}">{l}</tspan>' for k, l in enumerate(lines))
    ty = y + h / 2 - (len(lines) - 1) * 7.75 + 4.5
    return f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="7"/><text class="nt" style="font-size:{size}px" x="{x + w / 2:.1f}" y="{ty:.1f}" text-anchor="middle">{t}</text>'

S.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 630" role="img" aria-labelledby="dtitle"><title id="dtitle">Uber’s product lifecycle by task, with the humans, agents and shared platform at each task and the handoffs between them</title>')
S.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>')
for i, t in enumerate(tasks):
    S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>' + (f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t) > 1 else '') + '</text>')
    if chain[i]: S.append(f'<text class="chain" x="{cx(i):.1f}" y="66" text-anchor="middle">{chain[i]}</text>')
    if i: S.append(f'<line class="guide" x1="{X0 + W * i}" y1="50" x2="{X0 + W * i}" y2="530"/>')
for y, l in [(86, "HUMANS · ANY ROLE"), (226, "AGENTS"), (456, "SHARED PLATFORM")]:
    S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0 + W * NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="442" x2="{X0 + W * NCOL}" y2="442"/>')
hum = {0: ["anyone in a", "Slack thread"], 1: ["anyone, incl.", "ops staff"], 2: ["PMs (PRD", "Evaluator); demo", "presenter"],
       3: ["designers,", "PMs"], 4: ["engineers"], 5: ["engineers start", "it from Slack,", "web, CLI"], 7: ["a person on", "every PR"],
       8: ["not described", "for agents"], 9: ["on-call,", "service owners"]}
for i, l in hum.items():
    cls = "pnode acc" if i == 8 else "pnode"
    S.append(box(i, 96, 92, l, cls))
# Cortana spans research -> plan (cols 1-4)
S.append(box(1, 238, 70, ["Cortana: research → requirements → Figma mock-ups → code-change analysis"], "node cortana", span=4, size=13))
S.append(f'<text class="cap" x="{cx(2) + W / 2:.1f}" y="322" text-anchor="middle">one shared assistant on Slack, web and CLI; team personas per Slack channel</text>')
S.append(box(0, 238, 70, ["Slack", "thread"], "node lite"))
S.append(box(5, 238, 70, ["Minion", "~15% of prod", "PRs (Oct 2026)"]))
S.append(box(6, 238, 70, ["aifx validate,", "Slate, Figma", "screenshot check"]))
S.append(box(7, 238, 70, ["uReview,", "Code Inbox,", "self-healing CI"]))
S.append(box(9, 238, 70, ["maintenance", "loops; Debug-", "Assist → Minion"]))
S.append(box(8, 238, 70, ["A/B planned;", "not shown"], "auto"))
# second agent row: PRD Evaluator, uSpec, uPlan
S.append(box(2, 360, 58, ["PRD Evaluator", "(scores, never", "approves)"], "node lite", size=12))
S.append(box(3, 360, 58, ["uSpec", "(Cursor +", "Figma MCP)"], "node lite", size=12))
S.append(box(4, 360, 58, ["uPlan: PRD,", "ERD, reviews,", "Jira links"], "node lite", size=12))
S.append(box(0, 466, 56, ["context graph (Cortana’s default grounding) · skills marketplace · MCP gateway · model gateway · DevPods · Slack · Jira / Linear · AIFX over Claude Code, Codex, OpenCode"], "sub", span=NCOL, size=13))

def arrow(d, cls="doc", mk="ah"): S.append(f'<path class="{cls}" d="{d}" marker-end="url(#{mk})"/>')
y = 273
arrow(f"M{X0 + W - 6} {y}H{X0 + W + 6}")          # Slack -> Cortana
# Cortana -> Minion: documented, mechanism unknown
S.append(f'<path class="mech" d="M{X0 + W * 5 - 6} {y}H{X0 + W * 5 + 6}" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{X0 + W * 5:.1f}" cy="226" r="10"/><text class="gapq" x="{X0 + W * 5:.1f}" y="231.5" text-anchor="middle">?</text>')
arrow(f"M{X0 + W * 6 - 6} {y}H{X0 + W * 6 + 6}")  # Minion -> validate
arrow(f"M{X0 + W * 7 - 6} {y}H{X0 + W * 7 + 6}")  # validate -> review
arrow(f"M{X0 + W * 8 - 6} {y}H{X0 + W * 8 + 6}", "inf")  # review -> release (inferred)
# Cortana requirements -> uPlan / PRD Evaluator: unknown
S.append(f'<path class="gap" d="M{cx(2) - 30:.1f} 308 V358" marker-end="url(#ahg)"/>')
S.append(f'<path class="gap" d="M{cx(4) - 30:.1f} 308 V358" marker-end="url(#ahg)"/>')
# uPlan -> context graph (documented)
arrow(f"M{cx(4) + 30:.1f} 418 V464")
S.append(f'<text class="cap" x="{cx(4) + 36:.1f}" y="436">into the graph</text>')
# graph -> Cortana grounding
arrow(f"M{cx(1):.1f} 464 V310")
S.append(f'<text class="cap" x="{cx(1) + 6:.1f}" y="436">grounding</text>')
# Slack thread -> Minion directly
arrow(f"M{cx(0):.1f} 308 V342 H{cx(5) - 10:.1f} V310", "doc")
S.append(f'<text class="cap" x="{cx(5) + 2:.1f}" y="358" text-anchor="middle">“@minion, follow this thread”</text>')
# humans use agents
for i in (1, 2, 3, 4, 5): arrow(f"M{cx(i):.1f} 188V236", "inf")
# operate -> skills loop
S.append(f'<path class="doc" d="M{cx(9):.1f} 308V464" marker-end="url(#ah)"/><text class="cap" x="{cx(9) - 5:.1f}" y="436" text-anchor="end">diffs, incidents → skills</text>')
ly = 566
S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0 + 52}" y="{ly + 5}">documented by Uber</text>')
S.append(f'<path class="inf" d="M{X0 + 220} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0 + 272}" y="{ly + 5}">inferred, or a person uses the agent</text>')
S.append(f'<path class="mech" d="M{X0 + 540} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0 + 592}" y="{ly + 5}">documented, mechanism unknown (Cortana → Minion)</text>')
S.append(f'<path class="gap" d="M{X0 + 950} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0 + 1002}" y="{ly + 5}">unknown</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly + 40}">Column headers are tasks; the italic row is the stage order of Uber’s own walkthrough (AI Engineer, Aug 2026). Accent: a task with no agent shown. Our own diagram, not Uber’s UI.</text>')
S.append('</svg>')
svg = '\n'.join(S)

css = '''/* One reading column with a wide, scrollable task-by-task swimlane; tables below. System fonts only. Ink on cool paper; one amber accent for the undocumented links. */
:root{
  --paper:#f6f6f2; --surface:#ffffff; --ink:#1d2228; --muted:#5d6670; --rule:#d6d9d6; --accent:#b4580c; --accent-soft:#f5e3d2; --auto:#e9ecef; --lite:#f1f3f1; --hl:#e6eef6;
  --serif:Georgia, "Times New Roman", serif; --sans:system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif; --mono:ui-monospace, Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--paper:#15181b; --surface:#1d2125; --ink:#e7e9e6; --muted:#a3abb2; --rule:#343a40; --accent:#f0a35e; --accent-soft:#3a2a1c; --auto:#262b30; --lite:#22272b; --hl:#1f2a35; color-scheme:dark}}
:root[data-theme="dark"]{--paper:#15181b; --surface:#1d2125; --ink:#e7e9e6; --muted:#a3abb2; --rule:#343a40; --accent:#f0a35e; --accent-soft:#3a2a1c; --auto:#262b30; --lite:#22272b; --hl:#1f2a35; color-scheme:dark}
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
.counts{font-family:var(--mono); font-size:13.5px; color:var(--muted)}
.diagram{overflow-x:auto; background:var(--surface); border:1px solid var(--rule); border-radius:6px; padding:12px}
.diagram svg{display:block; min-width:1040px; width:100%; height:auto}
.diagram .stage{font-family:var(--serif); font-weight:600; font-size:14.5px; fill:var(--ink)}
.diagram .chain{font-family:var(--serif); font-style:italic; font-size:13px; fill:var(--muted)}
.diagram .lane{font-family:var(--mono); font-size:11px; letter-spacing:.1em; fill:var(--muted)}
.diagram .cap,.diagram .leg{font-family:var(--sans); font-size:12.5px; fill:var(--muted)}
.diagram .leg{font-size:13.5px; fill:var(--ink)}
.diagram .guide{stroke:var(--rule); stroke-width:1; stroke-dasharray:2 5}
.diagram .lanerule{stroke:var(--rule); stroke-width:1.2}
.diagram .node{fill:var(--surface); stroke:var(--ink); stroke-width:1.6}
.diagram .node.cortana{fill:var(--hl)}
.diagram .node.lite{fill:var(--lite); stroke:var(--muted); stroke-width:1.2}
.diagram .pnode{fill:var(--paper); stroke:var(--muted); stroke-width:1.2}
.diagram .pnode.acc{fill:var(--accent-soft); stroke:var(--accent); stroke-width:1.6}
.diagram .auto{fill:var(--auto); stroke:var(--muted); stroke-width:1.2}
.diagram .sub{fill:var(--auto); stroke:none}
.diagram .nt{font-family:var(--sans); fill:var(--ink)}
.diagram .doc{fill:none; stroke:var(--ink); stroke-width:1.8}
.diagram .inf{fill:none; stroke:var(--muted); stroke-width:1.5; stroke-dasharray:5 5}
.diagram .mech{fill:none; stroke:var(--accent); stroke-width:2.4}
.diagram .gap{fill:none; stroke:var(--accent); stroke-width:2; stroke-dasharray:3 5}
.diagram .gapdot{fill:var(--paper); stroke:var(--accent); stroke-width:2}
.diagram .gapq{font-family:var(--serif); font-weight:600; font-size:15px; fill:var(--accent)}
.diagram .mk{stroke:var(--ink); stroke-width:1.5}
.diagram .mkg{stroke:var(--accent); stroke-width:1.5}
.tablewrap{overflow-x:auto; border:1px solid var(--rule); border-radius:6px; background:var(--surface)}
table{border-collapse:collapse; width:100%; min-width:760px; font-size:14.5px}
th,td{text-align:left; vertical-align:top; padding:10px 14px; border-bottom:1px solid var(--rule)}
th{font-family:var(--mono); font-size:12px; font-weight:500; letter-spacing:.06em; text-transform:uppercase; color:var(--muted); background:var(--paper)}
tr:last-child td{border-bottom:none}
td:first-child{font-weight:600}
.status{font-family:var(--mono); font-size:12px; padding:2px 8px; border-radius:999px; border:1px solid var(--rule); white-space:nowrap; display:inline-block}
.s-doc{border-color:var(--ink)} .s-inf{color:var(--muted); border-style:dashed} .s-unk{color:var(--accent); border-color:var(--accent)} .s-mech{color:var(--accent); border-color:var(--accent); background:var(--accent-soft)}
.row-key td{background:var(--accent-soft)}
section{display:grid; gap:12px}
ul.impl{margin:0; padding-left:20px; display:grid; gap:10px; max-width:74ch}
.foot{font-size:13.5px; color:var(--muted); max-width:82ch}'''

TASKROWS = [
    ("Spot the opportunity", "Whoever is “jamming on it in Slack”", "Slack thread; Cortana tagged in", "Slack thread"),
    ("Research the opportunity", "Anyone, including ops staff", "Cortana on the context graph (past large-venue events, stadiums); QueryGPT and Finch for data", "Cortana answer in Slack, then on the web"),
    ("Write the requirements (PRD)", "PMs (“dozens” use the PRD Evaluator); the demo presenter with Cortana", "Cortana drafts requirements; PRD Evaluator scores readiness (Ready, Caveats, Not Ready) and never approves; uPlan holds the PRD and its reviews", "Requirements in Cortana; PRD and review status in uPlan"),
    ("Design: mock-ups, prototype, spec", "Designers, PMs, the demo presenter", "Cortana makes two Figma mock-ups for an A/B test; uSpec (Cursor + Figma MCP) writes design specs; AI prototypes sharpen the PRD", "Figma mock-ups; design spec"),
    ("Plan the change (ERD)", "Engineers; Cortana in the demo", "Cortana lists reusable screens and back-end code; the ERD lives in uPlan; Minion has a plan mode", "Code-change analysis; ERD; Minion plan"),
    ("Write the code", "Agents, started by engineers from Slack, web, CLI or a PR", "Minion on a mega DevPod (~15% of production PRs, Oct 2026); Claude Code, Codex and OpenCode through AIFX", "Draft PR, possibly across repos"),
    ("Validate (inner loop)", "Agents", "aifx validate (lint, coverage, build rules); simulator screenshot vs Figma; Slate per-branch staging", "Validated draft PR with a table of checks and screenshots"),
    ("Review the change", "A person on every PR", "uReview; Code Inbox (routing, risk score, blast radius); self-healing CI", "Approved PR"),
    ("Release and experiment", "Not described for agents", "A/B variants planned in the demo; experiment capacity named as a bottleneck", "Not shown"),
    ("Operate, maintain and learn", "On-call engineers; owners who enrol services", "Managed maintenance loops; DebugAssist → Minion; incident reviews mined monthly for skills; Cortana health reports; ADR on endpoints", "Diffs, RCAs on Jira tasks, new skills"),
]
e = html.escape
rows_t = '\n'.join(f'      <tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td><td>{e(d)}</td></tr>' for a, b, c, d in TASKROWS)
KEY = ' class="row-key"'
rows_h = '\n'.join(f'      <tr{KEY if s == "docmech" else ""}><td>{e(a)}</td><td>{e(b)}</td><td><span class="status {LABEL[s][1]}">{LABEL[s][0]}</span></td></tr>' for a, b, s in HANDOFFS)

body = f'''<div class="wrap">
<header>
  <div class="eyebrow">Uber teardown · lifecycle map by task · 2 Nov 2026</div>
  <h1>Where Uber’s agents sit in the product lifecycle, task by task</h1>
  <p class="lede">Anchored on tasks, not job titles: Uber’s assistant Cortana is for “anyone in the company”, and PMs, designers and engineers each also have their own tools. Each handoff is marked documented, inferred or unknown. Every figure is Uber’s own.</p>
</header>

<div class="answer">
  <h2>Uber documents the shaping-to-code handoff, but not how it works</h2>
  <ol>
    <li><strong>One assistant covers research → requirements → mock-ups → plan.</strong> In the August 2026 demo, a Slack thread tags Cortana. Cortana judges the business opportunity from the context graph, drafts requirements, makes Figma mock-ups for an A/B test and lists the code to reuse. Then “we hand off from that Cortana agent” to Minion, the cloud coding agent. Stripe’s record has no such link.</li>
    <li><strong>What crosses is not shown.</strong> The nearest documented mechanism is “@minion, follow this thread … create a PR”. Minion also takes a plan or a “really good spec”.</li>
    <li><strong>Specs have a tracked home that agents read, but Cortana’s link to it is unknown.</strong> uPlan holds PRDs, ERDs, launch, experiment and readiness reviews with Jira or Linear links, all fed into the context graph: “a source of truth system for both humans and agents to know the specs for every project”. Whether Cortana’s drafts land there, or pass the PRD Evaluator, is not stated.</li>
  </ol>
  <p><strong>What the task view adds:</strong> at Uber the shaping tasks sit in one shared assistant, often in a team’s Slack channel, so context can travel in Cortana’s thread rather than in someone’s head. The open seam is the artifact. Does shaped intent become a reviewed, tracked spec before code, or go straight from a chat to a PR?</p>
  <p class="counts">{COUNTS}.</p>
</div>

<div class="diagram" role="figure" aria-label="Swimlane diagram of Uber's lifecycle by task">
{svg}
</div>

<section>
  <h2>Task by task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it at Uber</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>
{rows_t}
    </tbody>
  </table></div>
</section>

<section>
  <h2>Every handoff, task to task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>From → to</th><th>How</th><th>Status</th></tr></thead>
    <tbody>
{rows_h}
    </tbody>
  </table></div>
</section>

<section>
  <h2>What it means for our options</h2>
  <ul class="impl">
    <li><strong>One shared assistant across the shaping tasks is a running option.</strong> Uber uses one company assistant with team personas; Stripe splits the same tasks across Kai, Harbor and Orbit.</li>
    <li><strong>Specs as a graph that agents read.</strong> uPlan’s PRDs, ERDs, reviews and ticket links feed the context graph, so the spec is a tracked record, not a file in one repo.</li>
    <li><strong>The spec gate before code is still the open seam.</strong> Cortana’s drafts, the PRD Evaluator, uPlan and Minion all exist, but no source joins them.</li>
    <li><strong>Feature velocity needed rebuilt links.</strong> Uber used AI to back-fill PRD → ERD → task links before it could measure P50 feature time: evidence for a dependency agent that writes links back.</li>
  </ul>
</section>

<p class="foot">Sources: Medisetty and Huda at AI Engineer (Aug 2026); Medisetty on The Pragmatic Engineer podcast (14 Oct 2026); Uber Engineering posts on the efficient software factory (Aug 2026), the PRD Evaluator (May 2026), uSpec (Mar 2026), AI prototyping (Apr 2026), uReview (Aug 2025), QueryGPT and Finch; Chada and Smith at The Pragmatic Summit (Mar 2026); Uber’s ChatGPT Work post (22 Oct 2026). uPlan and DebugAssist are named only in the podcast (auto-generated transcript). Full notes: project-agent-and-harness, task competitive-teardown-uber-cortana, 01-pdlc-uber.md.</p>
</div>'''

full = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>Uber Agent Lifecycle Map</title>\n<style>\n' + css + '\n</style>\n</head>\n<body>\n' + body + '\n</body>\n</html>\n'
open(os.path.join(OUT, '01-pdlc-uber.html'), 'w').write(full)
print('ok:', COUNTS)
