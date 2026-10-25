# Generates 01-pdlc-block.html (standalone: inline styles, no scripts, system fonts).
# Usage: python3 01-pdlc-block.build.py [outdir]. Frame and styles follow the Stripe map's generator
# (../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.build.py).
import sys, os
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.abspath(__file__))
W=124; X0=20; NCOL=10
cx=lambda i: X0+W*i+W/2
tasks=[["Spot the","opportunity"],["Talk to","customers"],["Research","the problem"],["Set the","goal"],["Shape the","intent"],["Plan the","change"],["Write the","code"],["Review the","change"],["Release"],["Operate","and learn"]]
chain=["Opportunity","Problem","Problem","Goal","Intent","Plan","Code","","",""]
S=[]
def box(i,y,h,lines,cls="node",span=1,size=12.5):
    x=X0+W*i+6; w=W*span-12
    t=''.join(f'<tspan x="{x+w/2:.1f}" dy="{0 if k==0 else 15.5}">{l}</tspan>' for k,l in enumerate(lines))
    ty=y+h/2-(len(lines)-1)*7.75+4.5
    return f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="7"/><text class="nt" style="font-size:{size}px" x="{x+w/2:.1f}" y="{ty:.1f}" text-anchor="middle">{t}</text>'
S.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 620" role="img" aria-labelledby="dtitle"><title id="dtitle">Block’s product lifecycle by task, with the humans, agents and shared tools at each task and the handoffs between them</title>')
S.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>')
for i,t in enumerate(tasks):
    S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>'+(f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t)>1 else '')+'</text>')
    if chain[i] and (i==0 or chain[i]!=chain[i-1]): S.append(f'<text class="chain" x="{cx(i):.1f}" y="66" text-anchor="middle">{chain[i]}</text>')
    if i: S.append(f'<line class="guide" x1="{X0+W*i}" y1="50" x2="{X0+W*i}" y2="500"/>')
for y,l in [(86,"HUMANS · ANY ROLE"),(226,"AGENTS"),(426,"SHARED")]:
    S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0+W*NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="412" x2="{X0+W*NCOL}" y2="412"/>')
hum={0:["leaders, DRIs;","sellers via","customer agents"],1:["PMs,","designers;","no tool shown"],2:["anyone: PMs,","growth, sales,","finance, risk"],3:["the DRI;","no tool","shown"],4:["PMs, designers","(90%+ ship PRs),","engineers"],5:["engineers;","team steers","in the thread"],6:["PMs, designers,","engineers start","agents"],7:["a person makes","the final","push"],8:["not","described"],9:["engineers,","security,","support"]}
for i,l in hum.items():
    cls="pnode acc" if i in (1,3,8) else "pnode"
    S.append(box(i,96,92,l,cls))
ag={2:["goose +","Data MCP,","Query Expert"],4:["goose, Cursor,","V0, Figma","Make, App Kit"],5:["Builderbot","plans from","ticket or thread"],6:["Builderbot","~1,500 PRs","a week"],7:["Builderbot","reviews 90%+","of changes"],9:["overnight","patch agents;","CI fixes"]}
for i,l in ag.items(): S.append(box(i,238,92,l))
S.append(box(0,238,92,["Managerbot,","Moneybot","requests"],"node lite"))
S.append(box(8,238,92,["not","described"],"auto"))
S.append(box(0,436,56,["goose MCP catalogue (~150 services) · skills marketplace (100+) · AGENTS.md / ai-rules (7 harnesses) · Slack · Linear / Jira · Google Drive · App Kit · Buzz"],"sub",span=NCOL,size=13))
def arrow(d,cls="doc",mk="ah"): S.append(f'<path class="{cls}" d="{d}" marker-end="url(#{mk})"/>')
y=284
arrow(f"M{X0+W*3-6+0.1} {y}H{X0+W*4+6}","inf")   # goose research -> prototype (inferred, skips goal col)
S.append(f'<text class="cap" x="{X0+W*3+W/2:.1f}" y="{y-8}" text-anchor="middle">same person?</text>')
arrow(f"M{X0+W*6-6} {y}H{X0+W*6+6}")   # Builderbot plan -> code
arrow(f"M{X0+W*7-6} {y}H{X0+W*7+6}")   # code -> review
arrow(f"M{cx(4):.1f} 330 C{cx(4):.1f} 384 {cx(6)-40:.1f} 384 {cx(6)-18:.1f} 332")  # PM/designer prototype -> PR
S.append(f'<text class="cap" x="{cx(5)-10:.1f}" y="400" text-anchor="end">PMs and designers ship the PR</text>')
# research -> plan across people: the gap
S.append(f'<path class="gap" d="M{cx(2)+26:.1f} 238 C{cx(2)+70:.1f} 200 {cx(5)-70:.1f} 200 {cx(5)-26:.1f} 236" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{(cx(2)+cx(5))/2:.1f}" cy="208" r="12"/><text class="gapq" x="{(cx(2)+cx(5))/2:.1f}" y="214" text-anchor="middle">?</text>')
# customer agents -> opportunity (documented claim)
arrow(f"M{cx(0):.1f} 238V190")
# humans use the agent for the task
for i in (2,4): arrow(f"M{cx(i):.1f} 188V236","inf")
# substrate up
arrow(f"M{cx(5):.1f} 436V332"); S.append(f'<text class="cap" x="{cx(5)+5:.1f}" y="426">ticket, thread</text>')
arrow(f"M{cx(2):.1f} 436V332"); S.append(f'<text class="cap" x="{cx(2)+5:.1f}" y="426">MCP servers</text>')
arrow(f"M{cx(9)-30:.1f} 332 C{cx(9)-30:.1f} 372 {cx(6)+40:.1f} 372 {cx(6)+18:.1f} 332")  # operate -> code (patches)
S.append(f'<text class="cap" x="{cx(8):.1f}" y="388" text-anchor="middle">bug tickets → draft patches</text>')
ly=530
S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+52}" y="{ly+5}">documented by Block</text>')
S.append(f'<path class="inf" d="M{X0+230} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+282}" y="{ly+5}">inferred, or a person uses the agent for the task</text>')
S.append(f'<path class="gap" d="M{X0+640} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0+692}" y="{ly+5}">research → plan across people: not described in any source</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly+40}">Column headers are tasks; the row below them is the Stripe whiteboard chain used by every map. Accent: tasks done by people with no tool shown, or not described. Our own diagram, not Block’s UI.</text>')
S.append('</svg>')
svg='\n'.join(S)

css='''/* Layout: one reading column with a wide, scrollable task-by-task swimlane; tables below. Ink on cool paper; one amber accent for the undocumented handoff and the tasks only people do. */
:root{
  --paper:#f6f6f2; --surface:#ffffff; --ink:#1d2228; --muted:#5d6670; --rule:#d6d9d6; --accent:#b4580c; --accent-soft:#f5e3d2; --auto:#e9ecef; --lite:#f1f3f1;
  --serif:"Source Serif 4", Georgia, "Times New Roman", serif; --sans:"Public Sans", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif; --mono:"IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
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
.foot{font-size:13.5px; color:var(--muted); max-width:82ch}'''
NL='\n      '

H=[  # (from -> to, how, status class, status label)
 ("Research (goose + data MCPs) → shape intent","Likely the same person in the same or a later goose session; research → report or internal app is documented, report → product prototype is not","s-inf","inferred"),
 ("Shape intent (prototype) → decision","People bring a prototype they built instead of a deck or Google Doc; Friday demos","s-doc","documented"),
 ("Shape intent (PM or designer) → write code","The same person ships the PR, via a sandbox-to-production programme with engineers pairing","s-doc","documented"),
 ("Any Slack thread or Linear/Jira ticket → plan and code (Builderbot)","Tag @builderbot with a short description, or it picks up the ticket; teammates steer in the thread","s-doc","documented"),
 ("Seller-request backlog → code (Builderbot)","Features sellers had waited months for shipped “in days”; how the list was produced is not said","s-doc","documented · upstream unknown"),
 ("Plan → write code (Builderbot; RPI)","One agent researches, plans, branches and codes; engineers keep research, plan and implement in separate sessions","s-doc","documented"),
 ("Write code → review","AI reviewed 90%+ of change requests (Q1 2026); a human makes the final push","s-doc","documented"),
 ("CI failure → fix (headless goose)","Failing CI becomes a draft-PR fix","s-doc","documented"),
 ("Review → release","Deploy mechanics not described; only outcome metrics","s-unk","unknown"),
 ("Operate (bug tickets, vulnerabilities) → code","Background agents draft patches overnight for engineers to review in the morning","s-doc","documented"),
 ("Customer agents (Managerbot, Moneybot) → spot the opportunity","Customers request automations before features ship; Block says they “align with our roadmap”; the essay proposes composition failures as the roadmap","s-doc","documented claim · mechanism unknown"),
 ("Talk to customers → research or intent","No tool or artifact described","s-unk","unknown"),
 ("Set the goal → shape intent","The DRI holds both; a company markdown file of metrics and non-goals is proposed","s-inf","inferred"),
 ("Research (one person’s goose session) → plan (Builderbot or an engineer), across people","Not described. goose sessions are local; recipes and skills carry method, not findings. What crosses is a prototype, a PR, a thread or a ticket","s-unk","unknown"),
 ("Shared capability → every task","One MCP catalogue (~150 services), a skills marketplace, AGENTS.md and an ai-rules generator across seven harnesses","s-doc","documented"),
 ("Operate and learn → shared capability","Red-team findings become upstream goose fixes; skills PR-reviewed into the marketplace; ~50 AI Champions","s-doc","documented"),
 ("Company and customer “world model” → every task","Proposed in Block’s essay as the replacement for management’s information routing; not shown in use","s-unk","unknown"),
]
GAP=' class="row-gap"'
rows=''.join(f'<tr{GAP if "across people" in a else ""}><td>{a}</td><td>{b}</td><td><span class="status {c}">{d}</span></td></tr>' + NL for a,b,c,d in H)
T=[
 ("Spot the opportunity","Leaders; DRIs; sellers, through customer agents","None internal; proposed: Managerbot and Moneybot requests and the intelligence layer’s failures as roadmap signal","A backlog of seller-requested features"),
 ("Talk to customers","PMs (the role still asks for customer research), designers","No tool named; Dorsey says conversational interfaces replace inferred research","Not described"),
 ("Research the problem, read the data","Anyone: PMs, growth managers (“without waiting on an analyst”), sales, finance, risk, engineers","goose with the Block Data MCP (1,100+ governed metrics) and Query Expert (2.1K monthly users); Snowflake, Looker, Glean, Drive","Analyses, reports, internal apps (App Kit: 1,000+)"),
 ("Set the goal","DRIs (own a customer problem, e.g. 90 days); growth managers","No tool shown; a company “markdown file” of metrics and non-goals is proposed","Not described"),
 ("Shape the intent","PMs, designers, engineers; DRIs decide","goose, Claude Code, Cursor, V0, Figma Make; App Kit. No PRD agent or recipe found","A prototype or demo, often a PR; prototypes replace decks and docs"),
 ("Plan the change","Engineers; teammates steer in the thread","Builderbot plans from a ticket or thread; RPI sessions; “Ready” issues in goose’s own repo","Linear/Jira ticket, Slack thread, Ready issue"),
 ("Write the code","Agents started by engineers; PMs and designers ship PRs","Builderbot (~1,500 merged PRs a week, ~15% of changes); seven harnesses; goose recipes","Branch and pull request"),
 ("Review the change","A person makes the final push","Builderbot reviewed 90%+ of change requests; headless goose drafts CI fixes","Approved PR"),
 ("Release","Not described","Not described; claims: post-change incidents down 70%+, 130 Square features in H1 2026","Live change"),
 ("Operate and learn","Engineers, security, support","Overnight patch agents; Gosling UI tests; red-team fixes; skills marketplace; Buzz agents with memory","Patches, skills, product signal"),
]
trows=''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' + NL for a,b,c,d in T)

body='''<div class="wrap">
<header>
  <div class="eyebrow">Block research · lifecycle map by task · 24 Oct 2026</div>
  <h1>Where Block’s agents sit in the product lifecycle, task by task</h1>
  <p class="lede">Anchored on tasks, not job titles. At Block one DRI owns an idea through to scale, PMs and designers ship pull requests, and feature teams of about 14 became squads of 1–6. Each handoff is marked documented, inferred or unknown. Nearly every figure is Block’s own.</p>
</header>

<div class="answer">
  <h2>Research → plan across people isn’t in the record. Block removes the handoff instead of building it</h2>
  <ol>
    <li><strong>Research happens in a person’s own goose session.</strong> That session is local, running on MCP servers such as the governed-metrics Data MCP and Query Expert. Recipes and skills are shared, but they carry method, not findings.</li>
    <li><strong>The one documented shared handoff is a ticket or a Slack thread.</strong> Anyone tags @builderbot or it picks up a Linear or Jira ticket, then plans, codes and iterates while teammates steer. It is told what to build, not why.</li>
    <li><strong>The rest is role collapse.</strong> The DRI owns the arc. PMs and designers build the prototype and often the PR, and prototypes replace decks and docs. The company “world model” that would generate the backlog is a published plan, not a system shown in use.</li>
  </ol>
  <p><strong>What the task view adds.</strong> Block takes Stripe’s and Shopify’s approach to its furthest point: it removes the people boundary instead of carrying context across it. The cost is visible. Cuts fell mostly on development, compliance was left intact, and every change still needs a human to push it. Staff dispute the gains. For an org that keeps a PM/engineering split, the seam to build for is still research → intent → plan across people. Block offers no artifact for it.</p>
</div>

<div class="diagram" role="figure" aria-label="Swimlane diagram of Block's lifecycle by task">
''' + svg + '''
</div>

<section>
  <h2>Task by task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it at Block</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>
      ''' + trows + '''</tbody>
  </table></div>
</section>

<section>
  <h2>Every handoff, task to task</h2>
  <p>17 handoffs: 11 documented (two with an upstream link or mechanism unknown), 2 inferred, 4 unknown.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>From → to</th><th>How</th><th>Status</th></tr></thead>
    <tbody>
      ''' + rows + '''</tbody>
  </table></div>
</section>

<section>
  <h2>What it means for our options</h2>
  <ul class="impl">
    <li><strong>A general harness for everyone, with shared stage services on top.</strong> Every employee gets goose with a curated MCP bundle. The heavy jobs became services: Builderbot for code and review, Query Expert for data. This favours neither “one agent, many skills” nor “one agent per task” alone.</li>
    <li><strong>Own the harness and the data, not the model.</strong> “To us the models are interchangeable.” Yet engineering buys seven coding harnesses and generates their configs from one rule set. That is a third option between owning one harness and buying one.</li>
    <li><strong>Role collapse closes the seam only where roles can collapse.</strong> It depends on tiny squads and a human gate kept at push. Where a PM/engineering split stays, the handoff stays open.</li>
    <li><strong>The Slack thread is the shared session.</strong> Builderbot, like Shopify’s River, works in a thread several people steer. goose itself stays local and single-user.</li>
  </ul>
</section>

<p class="foot">Sources (all filed in the project’s research library): Block’s Lenny’s Podcast and Sequoia interviews with CTO Dhanji Prasanna (Sept–Oct 2025); the investor day (Nov 2025); Dorsey’s note of 26 Feb 2026 and the essay “From Hierarchy to Intelligence” (Mar 2026); Owen Jennings on a16z (Apr 2026); Cameron Worboys on Dive Club (Mar 2026); Willem Avé on The Product Podcast (Aug 2026); Block engineering posts on MCP, skills, data, App Kit, CI, Buzz and red-teaming (2025–26); the Builderbot post (Jun 2026); the Q1 and Q2 2026 shareholder letters and the Q2 call; goose docs and blog; Block job posts (Oct 2026). Independent: The New Stack (Oct 2025, May 2026), The Guardian (Mar 2026), Fortune (Jul 2024), TechCrunch, HRD, Cointelegraph, Payments Dive. No Block PM has written first-hand about using agents. Full notes: project-agent-and-harness, task research-block-product-practices, 01-pdlc-block.md.</p>
</div>'''

full='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>Block Agent Lifecycle Map</title>\n<style>\n'+css+'\n</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n'
open(os.path.join(OUT,'01-pdlc-block.html'),'w').write(full)
print('ok')
