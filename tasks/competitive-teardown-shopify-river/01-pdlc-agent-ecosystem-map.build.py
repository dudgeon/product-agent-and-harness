import sys, os
# Generator for the Shopify lifecycle map; structure and styling reused from the Stripe map's generator
# (../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.build.py) so the maps compare side by side.
# Usage: python3 01-pdlc-agent-ecosystem-map.build.py <output-dir>
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.abspath(__file__))
W=124; X0=20; NCOL=10
cx=lambda i: X0+W*i+W/2
tasks=[["Spot the","opportunity"],["Talk to","customers"],["Research","the problem"],["Set the","goal"],["Shape the","intent"],["Plan the","change"],["Write the","code"],["Review the","change"],["Release"],["Operate","and learn"]]
chain=["","","","Proposal","Prototype","Build","Build","Build","Release","Results"]
S=[]
def box(i,y,h,lines,cls="node",span=1,size=12.5):
    x=X0+W*i+6; w=W*span-12
    t=''.join(f'<tspan x="{x+w/2:.1f}" dy="{0 if k==0 else 15.5}">{l}</tspan>' for k,l in enumerate(lines))
    ty=y+h/2-(len(lines)-1)*7.75+4.5
    return f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="7"/><text class="nt" style="font-size:{size}px" x="{x+w/2:.1f}" y="{ty:.1f}" text-anchor="middle">{t}</text>'
S.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" role="img" aria-labelledby="dtitle"><title id="dtitle">Shopify’s product lifecycle by task, with the humans, agents and shared tools at each task and the handoffs between them</title>')
S.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>')
for i,t in enumerate(tasks):
    S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>'+(f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t)>1 else '')+'</text>')
    if chain[i] and (i==0 or chain[i]!=chain[i-1]):
        span=sum(1 for k in range(i,NCOL) if chain[k]==chain[i] and all(chain[m]==chain[i] for m in range(i,k+1)))
        S.append(f'<text class="chain" x="{X0+W*i+W*span/2:.1f}" y="66" text-anchor="middle">GSD: {chain[i]}</text>')
    if i: S.append(f'<line class="guide" x1="{X0+W*i}" y1="50" x2="{X0+W*i}" y2="510"/>')
for y,l in [(86,"HUMANS · ANY ROLE"),(226,"AGENTS"),(426,"SHARED")]:
    S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0+W*NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="412" x2="{X0+W*NCOL}" y2="412"/>')
hum={0:["Tobi: ~6 yearly","themes;","leaders"],1:["not described","in any","source"],2:["anyone (7,000+),","in public","channels"],3:["teams, leaders;","GSD review","OK1 / OK2"],4:["PMs, designers,","engineers,","anyone"],5:["engineers and","others in","the thread"],6:["anyone, from","Slack; overnight","workflows"],7:["a human on","every PR","(“bottleneck”)"],8:["automated"],9:["engineers, security,","SRE, code","owners"]}
for i,l in hum.items():
    cls="pnode acc" if i in (1,3) else "pnode"
    S.append(box(i,96,92,l,cls))
# River spans research -> code
S.append(box(2,238,92,["River · one agent, in one public Slack thread","research · summary, ticket, diagram, prototype · plan push-back · PR","durable session on Aquifer; anyone can join the thread"],"node",span=5,size=13))
S.append(box(0,238,92,["Roast:","competitive-","intel workflow"],"node lite"))
S.append(box(7,238,92,["PR-review","profile","(Aquifer)"]))
S.append(box(8,238,92,["merge queue;","freshness-","gated (security)"],"auto"))
S.append(box(9,238,92,["River: traces,","security fixes,","crash triage"]))
S.append(box(0,436,56,["World (code, skills, AGENTS.md, intent docs) · Aquifer sessions · Slack search · GSD · Quick sites · Remote Dev · warehouse · traces"],"sub",span=NCOL,size=13))
def arrow(d,cls="doc",mk="ah"): S.append(f'<path class="{cls}" d="{d}" marker-end="url(#{mk})"/>')
y=284
arrow(f"M{X0+W*7-6} {y}H{X0+W*7+6}")   # River PR -> review profile
arrow(f"M{X0+W*8-6} {y}H{X0+W*8+6}")   # review -> merge queue
# operate (finding) -> thread -> draft PR
arrow(f"M{cx(9):.1f} 330 C{cx(9):.1f} 392 {cx(6)+10:.1f} 392 {cx(6)+10:.1f} 332")
S.append(f'<text class="cap" x="{cx(8)-20:.1f}" y="404" text-anchor="middle">finding → thread → draft PR</text>')
# humans -> River (people pull River into the thread)
for i in (2,4,5,6): arrow(f"M{cx(i):.1f} 188V236","inf")
# gaps: customers and goal/GSD not connected to River
S.append(f'<path class="gap" d="M{cx(1):.1f} 188 C{cx(1):.1f} 214 {cx(2)-30:.1f} 214 {cx(2)-30:.1f} 236" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{cx(1)+18:.1f}" cy="212" r="12"/><text class="gapq" x="{cx(1)+18:.1f}" y="218" text-anchor="middle">?</text>')
S.append(f'<path class="gap" d="M{cx(3):.1f} 188V236" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{cx(3):.1f}" cy="212" r="12"/><text class="gapq" x="{cx(3):.1f}" y="218" text-anchor="middle">?</text>')
# substrate up into River; learn loop down
arrow(f"M{cx(4):.1f} 436V332"); S.append(f'<text class="cap" x="{cx(4)+5:.1f}" y="426">skills, memory, repo</text>')
S.append(f'<path class="doc" d="M{cx(9)+30:.1f} 332V434" marker-end="url(#ah)"/><text class="cap" x="{cx(9)+24:.1f}" y="426" text-anchor="end">dreaming · mining → skills</text>')
# private work note
S.append(f'<text class="cap" x="{X0}" y="514" style="fill:var(--accent)">Private channels and DMs: River refuses them, so work there never enters the shared context (handoff unknown).</text>')
ly=548
S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+52}" y="{ly+5}">documented by Shopify</text>')
S.append(f'<path class="inf" d="M{X0+250} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+302}" y="{ly+5}">people pull River into the thread</text>')
S.append(f'<path class="gap" d="M{X0+600} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0+652}" y="{ly+5}">customers, goals, GSD → River: not described in any source</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly+40}">Column headers are tasks; the row below them is Shopify’s GSD phase. Accent: tasks with no agent or tool shown. Our own diagram, not Shopify’s UI.</text>')
S.append('</svg>')
svg='\n'.join(S)

css='''/* Reused from the Stripe map. Layout: one reading column with a wide, scrollable task-by-task swimlane; tables below. Ink on cool paper; one amber accent for the undocumented handoff and the tasks only people do. */
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
  <div class="eyebrow">Shopify teardown · lifecycle map by task · 24 Oct 2026</div>
  <h1>Where Shopify’s agents sit in the product lifecycle, task by task</h1>
  <p class="lede">Same frame as the Stripe map: rows are tasks, not job titles. At Shopify one agent, River, does research, intent, planning and code in a public Slack thread that nearly the whole company uses. Each handoff is marked documented, inferred or unknown. Every figure is Shopify’s own.</p>
</header>

<div class="answer">
  <h2>Inside the thread, context mostly doesn’t break. At its edges, it does</h2>
  <ol>
    <li><strong>The public thread is the handoff.</strong> People discuss, then ask River to “summarize this, create a ticket… make a diagram… create a prototype”, and River “usually offers to go fix it”. Research, intent, plan and code happen in one place.</li>
    <li><strong>People hand off by joining.</strong> “A second human… drops in with a constraint or a redirect”; same-thread co-writing links grew from 61,680 (March) to 171,853 (September 2026). Later people start “from this thread, not from a blank prompt” (claimed, not measured).</li>
    <li><strong>It breaks at the edges.</strong> No source links customer conversations, yearly themes or GSD proposals to River threads. There is no intent or plan artifact beyond the thread, ticket, Quick site or PR. How a Quick prototype becomes production code is not described. River refuses DMs and private channels, so sensitive research never enters the shared context.</li>
  </ol>
  <p><strong>Against Stripe:</strong> Stripe’s break is between agents (Kai’s single-user sessions don’t reach Orbit). Shopify avoided it with one agent in one shared place, at the price of privacy and of structure. The remaining seam is between the conversation and the formal process (GSD) and the durable artifact.</p>
</div>

<div class="diagram" role="figure" aria-label="Swimlane diagram of Shopify's lifecycle by task">
''' + svg + '''
</div>

<section>
  <h2>Task by task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it at Shopify</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>
      <tr><td>Spot the opportunity</td><td>Tobi sets ~6 yearly themes from the merchant’s view; leaders</td><td>None for River; a Roast workflow aggregates competitive intel from the web and CRM conversations (2025)</td><td>Yearly themes; intel (form not described)</td></tr>
      <tr><td>Talk to customers</td><td>Not described in any source</td><td>None named</td><td>Not described</td></tr>
      <tr><td>Research the problem, read the data</td><td>Anyone (7,000+ people), in public channels</td><td>River: code, data warehouse, production traces, the PM system, papers</td><td>Public, searchable thread with findings</td></tr>
      <tr><td>Set the goal</td><td>Teams turn themes into objectives; GSD Proposal reviewed OK1/OK2 (2023)</td><td>No tool shown</td><td>Team objectives; GSD proposal, often a short PM video</td></tr>
      <tr><td>Shape the intent</td><td>PMs, designers, engineers, anyone; GSD Prototype phase “dominated by AI exploration” (2025)</td><td>River in the thread; Quick sites (50,000+); Live Preview; intent documents in World</td><td>Ticket, diagram, Quick URL, GSD prototype, intent docs</td></tr>
      <tr><td>Plan the change</td><td>Engineers and others in the thread</td><td>River “pushes back on a plan”; Helix checkpoints (migration); Dispatch partitions (security)</td><td>The thread; no standalone plan artifact for River work</td></tr>
      <tr><td>Write the code</td><td>Anyone, from Slack; overnight workflows</td><td>River (~1 in 8 merged PRs coauthored, May 2026; 6%→61% of merged mobile PRs); Remote Dev; Dispatch; local Claude Code, Cursor</td><td>PR in World, coauthored by River</td></tr>
      <tr><td>Review the change</td><td>A human on every PR, “a big bottleneck”; “slop grenades”</td><td>PR-review profile on Aquifer; before/after recordings; Helix gates</td><td>Approved PR; recordings</td></tr>
      <tr><td>Release</td><td>Automated; GSD Release</td><td>Merge queue; freshness-gated queue for security; deploy not described</td><td>Merged change on World’s head</td></tr>
      <tr><td>Operate and learn</td><td>Engineers, security, SRE, code owners; GSD Results</td><td>River: traces, security remediation, crash triage. Learning loop: dreaming, corpus mining, Jev classifier</td><td>Verified fixes; updated skills, memory, AGENTS.md</td></tr>
    </tbody>
  </table></div>
</section>

<section>
  <h2>Every handoff, task to task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>From → to</th><th>How</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Any human thread → River</td><td>@-mention in a public channel; River joins a conversation in progress</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Research → shape intent (same thread)</td><td>Ask River to summarise, ticket, diagram or prototype; “an hour or so later, that is there”</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Research or intent → write code (same thread)</td><td>River investigates and “usually offers to go fix it”; proposes a PR</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Person → person, mid-task</td><td>A second human joins the thread; the durable session continues</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Past thread → next person’s research</td><td>Slack search; per-channel and per-person memory at session start; reuse unmeasured</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Write code → review</td><td>River-coauthored PR “reviewed by us”; PR-review profile woken by an external system</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Write code (mobile) → review by non-engineers</td><td>Live Preview link; before/after recordings; explainer videos</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Review → release</td><td>Merge queue; freshness-gated for security</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Operate (finding) → code → owner → verify</td><td>Ledger; one thread per finding; draft PR; “the smallest question”; verify at head</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Operate (production signal) → research</td><td>Traces; “from a log line in production back to the commit”; crash-fix workflows being added</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Learn → every task’s context</td><td>Nightly dreaming; corpus mining; Jev classifier; skill and AGENTS.md diffs</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Spot opportunity → set goal</td><td>Yearly themes → objectives → six-month roadmap (2023, no agent)</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Set goal → shape intent</td><td>GSD Proposal → Prototype, reviewed OK1/OK2; Prototype “dominated by AI exploration”</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Meeting → thread</td><td>River joins Google Meet if invited, “not really utilized”</td><td><span class="status s-doc">documented</span></td></tr>
      <tr><td>Intent documents in World → plan, code</td><td>River works from World, which holds intent docs; authorship not stated</td><td><span class="status s-inf">inferred</span></td></tr>
      <tr><td>Roast competitive intel → research or goal</td><td>Aggregates web and CRM conversations; destination not stated</td><td><span class="status s-inf">inferred</span></td></tr>
      <tr class="row-gap"><td>Talk to customers → research</td><td>Not described</td><td><span class="status s-unk">unknown</span></td></tr>
      <tr class="row-gap"><td>GSD project ↔ River thread</td><td>River can read the PM system; linking or updating GSD not described</td><td><span class="status s-unk">unknown</span></td></tr>
      <tr class="row-gap"><td>Quick prototype → PR in World</td><td>Not described; a human engineer must own anything reaching merchants</td><td><span class="status s-unk">unknown</span></td></tr>
      <tr class="row-gap"><td>Private or sensitive work → River</td><td>River refuses DMs and private channels; route not described</td><td><span class="status s-unk">unknown</span></td></tr>
    </tbody>
  </table></div>
  <p class="foot">20 handoffs: 14 documented, 2 inferred, 4 unknown. Most documented ones rest on one first-party source.</p>
</section>

<section>
  <h2>What it means for our options</h2>
  <ul class="impl">
    <li><strong>One shared place can remove the research → intent → plan seam that Stripe left to people,</strong> if the org accepts working in public. The same default that drives learning drives handoff.</li>
    <li><strong>The thread is not an intent standard.</strong> Shopify keeps its formal gates (GSD) apart from the agent conversation, with no documented link between them. Orgs that need reviewable specs still need an explicit intent artifact.</li>
    <li><strong>One general agent with profiles, not one agent per task.</strong> This is the opposite unit to Stripe’s; narrow, structured jobs (security, migration, scanning) still get their own pipelines.</li>
    <li><strong>Learning is a loop across all tasks,</strong> and it depends on transcripts being available, which is a consequence of public-by-default.</li>
  </ul>
</section>

<p class="foot">Sources: Shopify Engineering’s Under the River (May 2026), security remediation (Sept 2026), Remote Dev (Oct 2026), Quick (June 2026), Dispatch (July 2026) and Roast (June 2025); Tobi Lütke’s Learning on the Shop floor (May 2026), his replies, the September usage chart (Oct 2026) and his April 2025 memo; The Knowledge Project with Tobi (Sept 2026); Farhan Thawar on Beyond the Pilot (2026) and to BVP (Apr 2026); Glen Coates on Lenny’s Newsletter (July 2023, for GSD and goals). All first-party; no independent source observes these handoffs. Full notes: project-agent-and-harness, task competitive-teardown-shopify-river, 01-pdlc-agent-ecosystem-map.md.</p>
</div>'''

full='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>Shopify Agent Lifecycle Map</title>\n<style>\n'+css+'\n</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n'
open(os.path.join(OUT,'01-pdlc-agent-ecosystem-map.html'),'w').write(full)
print('ok')
