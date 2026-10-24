# Generates 07-pdlc-agent-ecosystem-map.html: Ramp's agent ecosystem by lifecycle task. Same frame and styling as the
# Stripe map (../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.build.py). Standalone: one file,
# inline styles, no scripts, system fonts.   python3 07-pdlc-agent-ecosystem-map.build.py
import os
OUT=os.path.dirname(os.path.abspath(__file__))
W=114; X0=20; NCOL=11
cx=lambda i: X0+W*i+W/2
tasks=[["Spot the","opportunity"],["Talk to","customers"],["Research","the problem"],["Set the","goal"],["Shape the","intent"],["Plan the","change"],["Write the","code"],["Review the","change"],["Test"],["Release"],["Operate","and learn"]]
chain=["identify","","","","define","","build","review","test","coordinate","improve"]
S=[]
def box(i,y,h,lines,cls="node",span=1,size=12):
    x=X0+W*i+5; w=W*span-10
    t=''.join(f'<tspan x="{x+w/2:.1f}" dy="{0 if k==0 else 15}">{l}</tspan>' for k,l in enumerate(lines))
    ty=y+h/2-(len(lines)-1)*7.5+4.5
    return f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="7"/><text class="nt" style="font-size:{size}px" x="{x+w/2:.1f}" y="{ty:.1f}" text-anchor="middle">{t}</text>'
S.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1300 640" role="img" aria-labelledby="dtitle"><title id="dtitle">Ramp’s product lifecycle by task, with the humans, agents and shared tools at each task and the handoffs between them</title>')
S.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>')
for i,t in enumerate(tasks):
    S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>'+(f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t)>1 else '')+'</text>')
    if chain[i]: S.append(f'<text class="chain" x="{cx(i):.1f}" y="66" text-anchor="middle">{chain[i]}</text>')
    if i: S.append(f'<line class="guide" x1="{X0+W*i}" y1="50" x2="{X0+W*i}" y2="500"/>')
for y,l in [(86,"HUMANS · ANY ROLE"),(226,"AGENTS"),(426,"SHARED")]:
    S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0+W*NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="412" x2="{X0+W*NCOL}" y2="412"/>')
hum={0:["PMs,","leaders"],1:["account mgrs,","sales, PMs"],2:["anyone:","ops, sales,","PMs, eng."],3:["people; no","tool shown"],4:["PMs and","others"],6:["eng. and","non-eng.:","Slack, web,","ext., PR"],7:["a human","reviewer the","agent picks"],8:["PMs give","instructions"],9:["PMs"],10:["on-call,","support, ops"]}
for i,l in hum.items(): S.append(box(i,96,92,l,"pnode acc" if i==3 else "pnode"))
S.append(box(5,96,92,["inside Glass;","no separate","step shown"],"pnode"))
ag={0:["Insight agent","calls, tickets,","surveys"],1:["Glass prompt","calls → ~20k","requests/mo"],2:["Ramp","Research ·","Gadget"],4:["Glass","define-stage","agent"],6:["Inspect","~75% of PRs","(Ramp’s figure)"],7:["Review","Buddy"],8:["Testo","browser QA"],9:["Gadget","launch","content"],10:["OCA · small","loops"]}
for i,l in ag.items(): S.append(box(i,238,92,l))
S.append(box(5,238,92,["no planning","agent","named"],"node lite"))
S.append(box(0,436,56,["Laminar (one harness) · Ramp Router · tool catalog · Dojo skills (350+) · Glass memory (24 h) · shared and multiplayer sessions · Notion / Linear / Slack record"],"sub",span=NCOL,size=13))
def arrow(d,cls="doc",mk="ah"): S.append(f'<path class="{cls}" d="{d}" marker-end="url(#{mk})"/>')
y=284
arrow(f"M{X0+W*1-5} {y}H{X0+W*1+5}")    # insight -> talk to customers
arrow(f"M{X0+W*7-5} {y}H{X0+W*7+5}")    # Inspect -> Review Buddy
arrow(f"M{X0+W*8-5} {y}H{X0+W*8+5}")    # Review Buddy -> Testo
arrow(f"M{X0+W*3-5} {y+30} C{cx(3):.1f} {y+30} {cx(3):.1f} {y+30} {X0+W*4+5} {y+30}","inf")  # research -> Glass, inferred
S.append(f'<text class="cap" x="{cx(3):.1f}" y="{y+22}" text-anchor="middle">connected</text>')
# Testo -> back to code
S.append(f'<path class="doc" d="M{cx(8):.1f} 330 C{cx(8):.1f} 358 {cx(6)+8:.1f} 358 {cx(6)+8:.1f} 333" marker-end="url(#ah)"/>')
S.append(f'<text class="cap" x="{cx(7):.1f}" y="372" text-anchor="middle">Testo: bugs back to the loop</text>')
# OCA -> Inspect
S.append(f'<path class="doc" d="M{cx(10)-14:.1f} 330 C{cx(10)-14:.1f} 392 {cx(6)+30:.1f} 392 {cx(6)+30:.1f} 333" marker-end="url(#ah)"/>')
S.append(f'<text class="cap" x="{cx(8):.1f}" y="406" text-anchor="middle">OCA: fix PR, a human merges</text>')
# Glass (define) -> Inspect: the contract, transport unknown
S.append(f'<path class="gap" d="M{cx(4)+26:.1f} 238 C{cx(4)+70:.1f} 198 {cx(6)-70:.1f} 198 {cx(6)-26:.1f} 236" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{cx(5):.1f}" cy="206" r="12"/><text class="gapq" x="{cx(5):.1f}" y="212" text-anchor="middle">?</text>')
# Testo -> release: deploy not described
S.append(f'<path class="gap" d="M{X0+W*9-5} {y} H{X0+W*9+5}" marker-end="url(#ahg)"/>')
# humans use the agent
for i in (1,2,4,6): arrow(f"M{cx(i):.1f} 188V236","inf")
# shared session across people
S.append(f'<text class="cap" x="{cx(6)+5:.1f}" y="426">multiplayer session</text>')
arrow(f"M{cx(6):.1f} 436V332")
S.append(f'<path class="inf" d="M{cx(10)+24:.1f} 332V434" marker-end="url(#ah)"/><text class="cap" x="{cx(10)+20:.1f}" y="426" text-anchor="end">to the KB</text>')
ly=540
S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+52}" y="{ly+5}">documented by Ramp</text>')
S.append(f'<path class="inf" d="M{X0+240} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+292}" y="{ly+5}">a person uses the agent, or inferred</text>')
S.append(f'<path class="gap" d="M{X0+600} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0+652}" y="{ly+5}">mechanism not described: define → build contract; test → release</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly+40}">Column headers are tasks; the italic row below them is Geoff Charles’s “software factory” stages. “Test” is a row the Stripe map doesn’t have. Accent: the task only people do, with no tool shown. Our own diagram, not Ramp’s UI.</text>')
S.append('</svg>')
svg='\n'.join(S)

css=r"""/* Same styling as the Stripe map (02-pdlc-agent-ecosystem-map.build.py) so the maps compare side by side. One amber accent for the undocumented handoffs and the task only people do. */
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
.foot{font-size:13.5px; color:var(--muted); max-width:82ch}"""
css=css.replace('--serif:"Source Serif 4", Georgia','--serif:Charter, "Iowan Old Style", Georgia').replace('--sans:"Public Sans", system-ui','--sans:system-ui').replace('--mono:"IBM Plex Mono", ui-monospace','--mono:ui-monospace')
css+="\n.diagram svg{min-width:1100px}"

def st(s): return {'d':'<span class="status s-doc">documented</span>','i':'<span class="status s-inf">inferred</span>','u':'<span class="status s-unk">unknown</span>','du':'<span class="status s-doc">documented</span> <span class="status s-unk">link unknown</span>'}[s]
H=[("1","Spot the opportunity (insight agent) → talk to customers","Traceable insight lets a PM “identify exactly which customers to talk to”; via Slack agent, dashboard, podcast","d"),
("2","Talk to customers (calls) → feature requests (Glass)","A saved Glass prompt pulls requests from call recordings","d"),
("3","Feature requests → prioritised → customer email on ship","Two more saved prompts; how “shipped” is detected isn’t described","du"),
("4","Research (Ramp Research) → scoping features","Teams add it to “project channels to scope out new features”","d"),
("5","Research (Ramp Research, Snowflake) → shape intent (Glass)","Both are connected tools in every Glass install; carrying answers into a define session isn’t shown","i"),
("6","Set the goal → shape intent","Not described","u"),
("7","Shape intent (Glass, PM) → plan and write code (Inspect, engineer)","“The next contract” (data, requirements for coding agents, prototype) is named; how it travels between sessions or people isn’t","u"),
("8","Shape intent → plan the change","Inside Glass (“AI is your tech lead”); no separate plan artifact","i"),
("9","Slack thread, PR comment, Chrome selection, web prompt → write code (Inspect)","Slack app with a repository classifier; extension sends the element tree; state synced across clients","d"),
("10","One person’s session → another person (Glass, Inspect)","Share the Glass session; Inspect sessions are multiplayer with attributed prompts","d"),
("11","Write code (Inspect) → review (Review Buddy, human)","PR under the requester’s identity; Review Buddy reads the code and the prompts behind it and picks the human reviewer","d"),
("12","Review → test (Testo) → back to code","Feedback goes “back through the loop to fix”; routing not described","du"),
("13","Review and test → release","Deploy and rollout not described in any source","u"),
("14","Release → launch content and the record (Gadget)","Reads Notion, Linear, Slack, tickets; writes help-center, blog, customer email; updates the roadmap","d"),
("15","Incident → OCA → Inspect → human merge","OCA joins the incident channel, reports at ~5 and ~13 min, asks Inspect for a PR; nothing merges without a human","d"),
("16","Feedback → backlog → plan → code → CI → knowledge base (small loops)","Agent routes, matches to Linear, dedupes, ranks, plans, asks in Slack, codes; each link’s mechanism not described","du"),
("17","Glass issue reports → tickets","A Slack channel triaged into tickets automatically","d"),
("18","Everyday work → every Glass session (memory)","24-hour pipeline writes memory files read at session start (April design)","d"),
("19","One person’s workflow → everyone (Dojo, knowledge edits)","Publish creates a reviewed Git change; 323 people made 6,500+ edits to what Glass knows","d")]
GAPROW=' class="row-gap"'
hrows='\n'.join(f'      <tr{GAPROW if n=="7" else ""}><td>{a}</td><td>{b}</td><td>{st(s)}</td></tr>' for n,a,b,s in H)
T=[("Spot the opportunity","PMs, leaders","Customer insight agent over calls, tickets, session replays and surveys; Slack agent, dashboard, daily digest and podcast","Clustered, traceable insight"),
("Talk to customers","Account managers, sales, PMs","Glass saved prompt pulls feature requests from calls (≈300 → ≈20,000 a month); earlier, Notion agents triaged sales feedback","Feature-request records; prioritised list"),
("Research the problem","Anyone: sales, ops, finance, PMs, engineers","Ramp Research (Slack data agent; 1,476 questions in four weeks vs 66 in the human channel); Glass with Snowflake; Gadget for org questions","Threaded answers with CSV previews; Glass sessions"),
("Set the goal","People","None named","Not described"),
("Shape the intent","PMs and others","Glass as the define-stage agent: data, research, strategy, spec conventions, design system, code base","“The next contract”: data, requirements, a working prototype"),
("Plan the change","Not shown as a separate task","No named planning agent; inside Glass or the small loops","Not described separately"),
("Write the code","Agents, started by engineers and non-engineers","Inspect (≈30% of merged PRs in Jan, &gt;50% in Mar, “75%” in Sept)","Branch and PR under the requester’s identity"),
("Review the change","A human reviewer the agent picks","Review Buddy (“93% of our PRs” handled)","Reviewed PR"),
("Test <em>(Ramp split)</em>","Agents; PMs give instructions","Testo browser QA agent; 425 bugs in 30 days","Bug and design-quality feedback"),
("Release","PMs","Deploy not described; Gadget writes launch content and updates the roadmap; Glass prompt emails customers when their request ships (5,000+)","Launch content; status updates"),
("Operate and learn","On-call, support, ops; small-loop agents","OCA (575 of 1,220 incident-fix PRs assisted in four weeks); small loops; issue channel to tickets","Incident reports, fix PRs, tickets, KB updates")]
trows='\n'.join(f'      <tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in T)

body=f"""<div class="wrap">
<header>
  <div class="eyebrow">Ramp teardown · lifecycle map by task · 24 Oct 2026</div>
  <h1>Where Ramp’s agents sit in the product lifecycle, task by task</h1>
  <p class="lede">Same frame as the Stripe map: rows are tasks, not job titles. At Ramp non-engineers write code through Inspect and PMs prototype in Glass. Each handoff is marked documented, inferred or unknown. Every figure is Ramp’s own; none is independently checked.</p>
</header>

<div class="answer">
  <h2>Ramp names the define → build contract, but not how it travels</h2>
  <ol>
    <li><strong>The contract is named.</strong> Geoff Charles: engineering wants the data, “the actual requirements that they can use for their coding agents, and a prototype”: “the next contract”. No source shows how it moves from a PM’s Glass session to an engineer’s Inspect session.</li>
    <li><strong>Where context crosses people, Ramp carries the session itself.</strong> Glass sessions can be handed to a colleague, and every Inspect session is multiplayer with attributed prompts. Since October, Glass and Inspect run on one harness, Laminar.</li>
    <li><strong>For small work, the people boundary goes away.</strong> Agent-run loops take feedback to backlog, plan, code, CI and the knowledge base, with a Slack check; “60% of UX issues … fixed within 24 hours”.</li>
    <li><strong>The top of the chain is unrecorded.</strong> No tool is shown for setting the goal, and planning has no agent of its own.</li>
  </ol>
  <p><strong>Against Stripe:</strong> Stripe’s gap is between two agents (Kai → Orbit). Ramp’s tooling has fewer gaps: one workspace, shared sessions, one harness. Its public record leaves the same seam open in a different place: the hand-off from a define-stage session to a build-stage session when different people own them.</p>
</div>

<div class="diagram" role="figure" aria-label="Swimlane diagram of Ramp's lifecycle by task">
{svg}
</div>

<section>
  <h2>Task by task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it at Ramp</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>
{trows}
    </tbody>
  </table></div>
</section>

<section>
  <h2>Every handoff, task to task</h2>
  <p>19 handoffs: 11 documented, 3 documented with one link’s mechanism unknown, 2 inferred, 3 unknown.</p>
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
    <li><strong>Ramp’s answer to context across people is the shared session, not a hand-off artifact.</strong> It leaves open what happens when the next person needs a durable, reviewable artifact.</li>
    <li><strong>The define → build contract is a concrete candidate spec standard</strong>: evidence, requirements written for coding agents, and a working prototype. Its format is the open question.</li>
    <li><strong>One agent per stage, on one harness.</strong> Insight, Glass, Inspect, Review Buddy, Testo, Gadget, OCA, all on Laminar.</li>
    <li><strong>Split by size.</strong> Agent-run loops for small changes; human-shaped intent for large ones.</li>
  </ul>
</section>

<p class="foot">Sources (all Ramp first-party unless marked): Geoff Charles’s “software factory” talk (Sept 2026); Ramp Builders posts on Inspect (Jan 2026), Ramp Research (Sept 2025), OCA (Sept 2026), Laminar (Oct 2026) and agent trust (July 2025); Seb Goddijn’s and Shane Buchan’s Glass articles (Apr 2026); Eric Glyman’s launch article and Karim Atiyeh’s post (Oct 2026, vendor claims); the Pragmatic Summit talk by Ramp engineers (Mar 2026). Review Buddy, Testo, Gadget and the insight agent appear only in Charles’s talk. Full notes: project-agent-and-harness, task competitive-teardown-ramp-glass, 07-pdlc-agent-ecosystem-map.md.</p>
</div>"""

full='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>Ramp Agent Lifecycle Map</title>\n<style>\n'+css+'\n</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n'
open(os.path.join(OUT,'07-pdlc-agent-ecosystem-map.html'),'w').write(full)
print('ok')
