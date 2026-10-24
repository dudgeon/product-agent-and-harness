import sys, os
OUT=sys.argv[1]
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
S.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 620" role="img" aria-labelledby="dtitle"><title id="dtitle">Stripe’s product lifecycle by task, with the humans, agents and shared tools at each task and the handoffs between them</title>')
S.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>')
for i,t in enumerate(tasks):
    S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>'+(f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t)>1 else '')+'</text>')
    if chain[i] and (i==0 or chain[i]!=chain[i-1]): S.append(f'<text class="chain" x="{cx(i):.1f}" y="66" text-anchor="middle">{chain[i]}</text>')
    if i: S.append(f'<line class="guide" x1="{X0+W*i}" y1="50" x2="{X0+W*i}" y2="500"/>')
S.append(f'<text class="cap" x="{cx(2):.1f}" y="66" text-anchor="middle">(problem)</text>'.replace('(problem)',''))
for y,l in [(86,"HUMANS · ANY ROLE"),(226,"AGENTS"),(426,"SHARED")]:
    S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0+W*NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="412" x2="{X0+W*NCOL}" y2="412"/>')
hum={0:["leaders, PMs,","engineers"],1:["engineers, PMs,","researchers,","account execs"],2:["anyone: sales,","finance, ops,","eng, PMs"],3:["people; no","tool shown"],4:["designers, PMs,","engineers,","finance, AEs"],5:["engineers first;","team comments"],6:["started by eng.,","more and more","from Slack"],7:["a person on","every PR"],9:["ops, finance,","compliance"]}
for i,l in hum.items():
    cls="pnode acc" if i in (1,3) else "pnode"
    S.append(box(i,96,92,l,cls))
ag={2:["Kai","research,","data, docs"],4:["Harbor ·","Protodash","prototypes"],5:["Orbit","reads code +","Trailhead"],6:["Minions","~1,300 PRs","a week"],7:["Gru","review","agent"],9:["Kai triage;","compliance","agents"]}
for i,l in ag.items(): S.append(box(i,238,92,l))
S.append(box(1,238,92,["Kai: account","research","before calls"],"node lite"))
S.append(box(8,238,92,["1% canary,","auto-","rollback"],"auto"))
S.append(box(0,436,56,["Toolshed (~500 MCP tools) · Trailhead (owner-verified docs) · devboxes · Compass (projects) · Slack · Google Docs · tickets"],"sub",span=NCOL,size=13))
def arrow(d,cls="doc",mk="ah"): S.append(f'<path class="{cls}" d="{d}" marker-end="url(#{mk})"/>')
y=284
arrow(f"M{X0+W*3-6+0.1} {y}H{X0+W*4+6}")   # Kai -> Harbor (skip goal col)
S.append(f'<text class="cap" x="{X0+W*3+W/2:.1f}" y="{y-8}" text-anchor="middle">via MCP</text>')
arrow(f"M{X0+W*6-6} {y}H{X0+W*6+6}")   # Orbit -> Minions
arrow(f"M{X0+W*7-6} {y}H{X0+W*7+6}")   # Minions -> Gru
arrow(f"M{X0+W*8-6} {y}H{X0+W*8+6}")   # Gru -> canary
arrow(f"M{cx(4):.1f} 330 C{cx(4):.1f} 384 {cx(6)-40:.1f} 384 {cx(6)-18:.1f} 332")  # Harbor -> Minions
S.append(f'<text class="cap" x="{cx(5):.1f}" y="398" text-anchor="middle">prototype files → coding agents</text>')
# Kai -> Orbit gap
S.append(f'<path class="gap" d="M{cx(2)+26:.1f} 238 C{cx(2)+70:.1f} 200 {cx(5)-70:.1f} 200 {cx(5)-26:.1f} 236" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{(cx(2)+cx(5))/2:.1f}" cy="208" r="12"/><text class="gapq" x="{(cx(2)+cx(5))/2:.1f}" y="214" text-anchor="middle">?</text>')
# humans -> agents (people use the agent for the task)
for i in (2,4,5): arrow(f"M{cx(i):.1f} 188V236","inf")
# substrate up
arrow(f"M{cx(5):.1f} 436V332"); S.append(f'<text class="cap" x="{cx(5)+5:.1f}" y="426">reads docs</text>')
arrow(f"M{cx(6):.1f} 436V332"); S.append(f'<text class="cap" x="{cx(6)+5:.1f}" y="426">thread, doc, ticket</text>')
S.append(f'<path class="inf" d="M{cx(9):.1f} 332V434" marker-end="url(#ah)"/><text class="cap" x="{cx(9)-5:.1f}" y="426" text-anchor="end">logs → prompts</text>')
ly=530
S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+52}" y="{ly+5}">documented by Stripe</text>')
S.append(f'<path class="inf" d="M{X0+250} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+302}" y="{ly+5}">a person uses the agent for the task</text>')
S.append(f'<path class="gap" d="M{X0+600} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0+652}" y="{ly+5}">research → plan (Kai → Orbit): not described in any source</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly+40}">Column headers are tasks; the row below them is Stripe’s whiteboard chain. Accent: tasks still done by people with no tool shown. Our own diagram, not Stripe’s UI.</text>')
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

body='''<div class="wrap">
<header>
  <div class="eyebrow">Stripe teardown · lifecycle map by task · 24 Oct 2026</div>
  <h1>Where Stripe’s agents sit in the product lifecycle, task by task</h1>
  <p class="lede">Anchored on tasks, not job titles: at Stripe, engineers talk to users and write intent, and PMs, designers, finance staff and account executives build prototypes. Each handoff is marked documented, inferred or unknown. Every figure is Stripe’s own.</p>
</header>

<div class="answer">
  <h2>Research → plan (Kai → Orbit) isn’t in the public record</h2>
  <ol>
    <li><strong>Kai’s work stays in one person’s sessions.</strong> Stripe lists sharing across sessions as roadmap: context in Kai sessions is “currently ‘locked in’” (Kai post, July 2026).</li>
    <li><strong>Orbit plans from intent a person types.</strong> In the only demo an engineer types a question; Orbit reads the codebase and Trailhead, then drafts a plan the team comments on.</li>
    <li><strong>People bridge the two, through shared tools and documents.</strong> Every agent reaches Toolshed’s ~500 MCP tools and the same docs, Slack threads and tickets.</li>
  </ol>
  <p><strong>What the task view adds:</strong> at Stripe one person often does research, intent and planning (engineers wear the “product hat”), so the missing link costs little there: the context travels in that person’s head. It bites when those tasks sit with different people, as in most of our target orgs. That handoff, research → intent → plan across people, is the seam to fund.</p>
</div>

<div class="diagram" role="figure" aria-label="Swimlane diagram of Stripe's lifecycle by task">
''' + svg + '''
</div>

<section>
  <h2>Task by task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it at Stripe</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>
      <tr><td>Spot the opportunity</td><td>Leaders, PMs, engineers wearing the “product hat”</td><td>None named</td><td>Not described</td></tr>
      <tr><td>Talk to customers</td><td>Engineers (“close to users”), PMs, researchers, account executives</td><td>People; Kai researches accounts before calls</td><td>Not shown (the whiteboard’s “customer conversations”)</td></tr>
      <tr><td>Research the problem, read the data</td><td>Anyone: sales, finance, ops, engineers, PMs</td><td>Kai: data analysis (5,000+ sessions a day), docs, email digests</td><td>Kai dashboards, reports, docs; single-user</td></tr>
      <tr><td>Set the goal</td><td>People</td><td>No tool shown</td><td>Not described</td></tr>
      <tr><td>Shape the intent</td><td>Designers, PMs (now Protodash’s largest group), engineers, finance, account executives</td><td>Harbor (12,000 prototypes), Protodash, Google Docs PRDs, agent-drafted specs reviewed as GitHub issues</td><td>Prototype URL with comments; PRD; spec issue</td></tr>
      <tr><td>Plan the change</td><td>Engineers first; teammates comment</td><td>Orbit: reads code and Trailhead; “Workspaces share context across sessions”</td><td>A shareable, commented plan</td></tr>
      <tr><td>Write the code</td><td>Agents, started by engineers and increasingly by non-engineers from Slack</td><td>Minions (~1,300 PRs a week); Claude Code, Cursor; the payment-method factory</td><td>Branch and pull request</td></tr>
      <tr><td>Review the change</td><td>A person on every PR</td><td>Gru, the review agent; CI capped at two rounds</td><td>Approved PR</td></tr>
      <tr><td>Release</td><td>Automated</td><td>1% canary, auto-pause and rollback</td><td>Live change</td></tr>
      <tr><td>Operate and learn</td><td>Ops, finance, compliance analysts, engineers</td><td>Kai triage and digests; 100+ compliance agents; factory learning logs</td><td>Answers, digests, improved prompts and skills</td></tr>
    </tbody>
  </table></div>
</section>

<section>
  <h2>Every handoff, task to task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>From → to</th><th>How</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Research (Kai) → shape intent (Harbor)</td><td>Harbor’s tools over internal MCP; its renderer is a service Kai uses. A stripe.com analysis in Kai became a clickable prototype</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Shape intent → write code</td><td>Coding agents pull a Harbor prototype’s files into a repo; a Protodash prototype PR became an engineer’s source of truth</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Any thread, doc or ticket → write code (Minions)</td><td>Emoji reaction or tagging the app; the thread is the prompt; the docs, feature-flag and ticketing tools can launch minions</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Plan (Orbit) → write code (Minions)</td><td>One button: devbox, plan and instructions; up to 12 hours; pauses to ask</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Shared docs (Trailhead) → plan, code</td><td>Orbit and minions read owner-verified internal docs</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Research (Kai) → other agents</td><td>Kai “invoke[s] more specialized agents and skills”; mechanism not described</td><td><span class="status s-inf">mechanism unknown</span></td></tr>
      <tr class="row-gap"><td>Research (Kai) → plan (Orbit)</td><td>Not described. One person doing both carries it in their head and docs; two people pass docs, Slack posts or prototypes</td><td><span class="status s-unk">unknown</span></td></tr>
      <tr><td>Talk to customers, set goal → shape intent</td><td>People; no tool shown</td><td><span class="status s-inf">inferred</span></td></tr>
      <tr><td>Operate and learn → shared knowledge</td><td>Factory learning and decision logs update prompts; Kai skill reflection is roadmap</td><td><span class="status s-doc">documented</span> <span class="status s-inf">roadmap</span></td></tr>
    </tbody>
  </table></div>
</section>

<section>
  <h2>What it means for our options</h2>
  <ul class="impl">
    <li><strong>One agent per task, used by whoever does the task.</strong> Kai for research, Harbor for prototypes, Orbit for plans, Minions for code. That favours a job or stage agent over a persona agent built around a job title.</li>
    <li><strong>The seam to fund is research → intent → plan when different people do them.</strong> Options that carry shaped intent, with its evidence, into planning target exactly what Stripe left to people.</li>
    <li><strong>Single-user sessions are the blocker Stripe names itself.</strong> Orbit’s shared workspaces suggest it solved sharing for planning first.</li>
    <li><strong>Agents connect through a shared tool layer and documents, not an orchestrator.</strong></li>
  </ul>
</section>

<p class="foot">Sources: Stripe’s Kai post (July 2026), Harbor post (Sept 2026), Minions parts 1–2 (Feb 2026), How I AI episodes with Steve Kaliski (Mar 2026), Owen Williams (May 2026) and Sharadh Krishnamurthy (Sept 2026), the Not My Business video showing Orbit (Oct 2026), Stripe Sessions 2024 (Trailhead), the AWS/Stripe compliance post (June 2026), and The Pragmatic Engineer on Stripe’s culture (Jan 2024, independent). Orbit is documented only by one video and one tweet. Full notes: project-agent-and-harness, task competitive-teardown-stripe-knowledge-agents, 02-pdlc-agent-ecosystem-map.md.</p>
</div>'''

head_common='''<title>Stripe Agent Lifecycle Map</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">'''
# Artifact fragment (the viewer adds the document skeleton)
frag=head_common+'\n<meta name="claude:viewport-fit-sides" content="cover">\n<style>\n'+css+'\n</style>\n'+body+'\n'
open(os.path.join(OUT,'02-pdlc-agent-ecosystem-map.html'),'w').write(frag)
# Standalone vanilla document
full='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+head_common+'\n<style>\n'+css+'\n</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n'
open(os.path.join(OUT,'02-pdlc-agent-ecosystem-map.standalone.html'),'w').write(full)
print('ok')
