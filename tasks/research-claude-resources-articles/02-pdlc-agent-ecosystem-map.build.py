# Generates 02-pdlc-agent-ecosystem-map.html (one standalone document, inline styles, no scripts).
# Structure and styling reused from the Stripe map's generator so the two maps compare side by side.
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
S.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 640" role="img" aria-labelledby="dtitle"><title id="dtitle">Anthropic’s own product lifecycle by task, with the humans, agents and shared context at each task and the handoffs between them</title>')
S.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>')
for i,t in enumerate(tasks):
    S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>'+(f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t)>1 else '')+'</text>')
    if chain[i] and (i==0 or chain[i]!=chain[i-1]): S.append(f'<text class="chain" x="{cx(i):.1f}" y="66" text-anchor="middle">{chain[i]}</text>')
    if i: S.append(f'<line class="guide" x1="{X0+W*i}" y1="50" x2="{X0+W*i}" y2="510"/>')
for y,l in [(86,"HUMANS · ANY ROLE"),(226,"AGENTS"),(436,"SHARED")]:
    S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0+W*NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="422" x2="{X0+W*NCOL}" y2="422"/>')
hum={0:["tech lead, PMs;","anyone seeing","latent demand"],1:["PMs read","transcripts;","dogfooding"],2:["anyone: PMs,","analysts,","eng, sales"],3:["people set the","north star;","JIT sheet"],4:["PMs, designers,","engineers","(side quests)"],5:["the builder;","low risk self-","approves"],6:["directed by","eng, PMs,","from Slack"],7:["people by risk:","none, one","or two"],9:["weekly","on-call;","security"]}
for i,l in hum.items():
    cls="pnode acc" if i in (0,3) else "pnode"
    S.append(box(i,96,92,l,cls))
ag={2:["analytics skills,","Tag in Slack,","Cowork, loops"],4:["prototypes,","Claude Design,","PRDs, evals"],5:["plan mode","+ security","review (PSR)"],6:["Claude Code;","internal Tag","(>½ of code)"],7:["Code Review","+ security","+ risk classifier"],9:["Tag CI on-call,","superfans,","alert agent"]}
for i,l in ag.items(): S.append(box(i,238,92,l))
S.append(box(0,238,92,["Claude as","strategy","critic"],"node lite"))
S.append(box(1,238,92,["Tag merges","feature","requests"],"node lite"))
S.append(box(8,238,92,["flags to staff,","latest → stable"],"auto"))
S.append(box(0,446,56,["Open Slack channels with a resident Claude Tag (channel memory) · CLAUDE.md, REVIEW.md, skills in repos · shared eval repository · Scion + Antique"],"sub",span=NCOL,size=13))
def arrow(d,cls="doc",mk="ah"): S.append(f'<path class="{cls}" d="{d}" marker-end="url(#{mk})"/>')
y=284
arrow(f"M{X0+W*2-6} {y}H{X0+W*2+6}")   # requests -> research
arrow(f"M{X0+W*3-6+0.1} {y}H{X0+W*4+6}")   # research -> shape intent (skip goal)
S.append(f'<text class="cap" x="{X0+W*3+W/2:.1f}" y="{y-8}" text-anchor="middle">eval, PRD</text>')
arrow(f"M{X0+W*5-6} {y}H{X0+W*5+6}")   # intent -> plan
arrow(f"M{X0+W*6-6} {y}H{X0+W*6+6}")   # plan -> code
arrow(f"M{X0+W*7-6} {y}H{X0+W*7+6}")   # code -> review
arrow(f"M{X0+W*8-6} {y}H{X0+W*8+6}")   # review -> release
arrow(f"M{X0+W*9-6} {y}H{X0+W*9+6}")   # release -> operate
arrow(f"M{cx(4):.1f} 330 C{cx(4):.1f} 384 {cx(6)-40:.1f} 384 {cx(6)-18:.1f} 332")  # design -> code
S.append(f'<text class="cap" x="{cx(5):.1f}" y="398" text-anchor="middle">design → Claude Code</text>')
arrow(f"M{cx(9)-10:.1f} 332 C{cx(9)-30:.1f} 404 {cx(6)+40:.1f} 404 {cx(6)+18:.1f} 332")  # operate -> code
S.append(f'<text class="cap" x="{cx(8):.1f}" y="414" text-anchor="middle">fix PR (cannot deploy)</text>')
# research -> plan across people: unknown
S.append(f'<path class="gap" d="M{cx(2)+26:.1f} 238 C{cx(2)+70:.1f} 200 {cx(5)-70:.1f} 200 {cx(5)-26:.1f} 236" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{(cx(2)+cx(5))/2:.1f}" cy="208" r="12"/><text class="gapq" x="{(cx(2)+cx(5))/2:.1f}" y="214" text-anchor="middle">?</text>')
for i in (2,4,5,6,7): arrow(f"M{cx(i):.1f} 188V236","inf")
arrow(f"M{cx(2):.1f} 446V332"); S.append(f'<text class="cap" x="{cx(2)+5:.1f}" y="436">channels read</text>')
arrow(f"M{cx(6)-30:.1f} 446V332"); S.append(f'<text class="cap" x="{cx(6)-25:.1f}" y="436">thread → PR</text>')
S.append(f'<path class="doc" d="M{cx(9)+30:.1f} 332V444" marker-end="url(#ah)"/><text class="cap" x="{cx(9)+25:.1f}" y="436" text-anchor="end">lessons, evals</text>')
ly=540
S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+52}" y="{ly+5}">documented by Anthropic</text>')
S.append(f'<path class="inf" d="M{X0+250} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+302}" y="{ly+5}">a person uses the agent for the task</text>')
S.append(f'<path class="gap" d="M{X0+600} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0+652}" y="{ly+5}">research → plan across people: not described in any source</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly+40}">Column headers are tasks; the row below them is the opportunity-to-code chain used for every ecosystem map. Accent: tasks only people do, with no tool or artifact shown.</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly+60}">Our own diagram from Anthropic’s published accounts of its own teams. The playbook’s intent.md → spec.md → plan.md chain is a prescription for customers and is not drawn.</text>')
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
def st(s):
    c={'documented':'s-doc','inferred':'s-inf','unknown':'s-unk'}[s.split()[0]]
    return f'<span class="status {c}">{s}</span>'
rows=[
("Spot the opportunity","Tech lead with a 3–6 month view; PMs plotting the path; anyone noticing latent demand (non-coders in Claude Code led to Cowork)","Claude as strategy critic; revisiting features with each model","No artifact described; themes and prototypes"),
("Talk to customers","PMs, tenured hires included (read consented transcripts and feedback, talk to customers); engineers through dogfooding","Reading trajectories; Claude Tag consolidating feature requests from sales channels","Classified failure descriptions; consolidated request lists"),
("Research the problem, read the data","Anyone: PMs, analysts, engineers, sales","Analytics skills over a governed semantic layer (95% of business queries automated, Anthropic’s figure); Claude Tag for ad-hoc data; a PM’s adoption-analytics and sentiment agents; morning feedback summary; a loop on #project-feedback","Answers with provenance; readouts; summaries; triaged issues"),
("Set the goal","People: humans “always set the north star”; team principles; monthly JIT planning sheet","No tool shown (whether agents write the weekly readouts is not stated)","Principles; planning sheet"),
("Shape the intent","PMs, designers, engineers (“side quests”)","Claude Code prototypes; Claude Design; Cowork PRD drafts from stacked plugins; HTML specs; evals (prompt plus golden answer) as “test-driven development for PMs”; security review of design docs","Working prototype for internal users; design; eval set; PRD for big alignment; risk rating"),
("Plan the change","The builder; low-risk projects self-approve at the security check","Claude Code plan mode (Cherny starts ~80% of tasks there); interview-style unknowns pass","A plan in the session (a committed plan.md is the playbook’s prescription, not shown internally)"),
("Write the code","Agents, directed by engineers, PMs and others, often from a Slack thread","Claude Code (parallel sessions, auto mode, dynamic workflows); an internal Claude Tag that merges more than half of code; Claude writes ~80% of merged code","Branch and PR"),
("Review the change","Agents first; people by risk tier (none, one or two); whoever directed the agent counts as a reviewer","Self-verification and a fresh-context subagent; Code Review with voting agents; blocking security review; CI; risk classifiers; Antique","Approved PR with every finding resolved"),
("Release","Automated; PMM and DevRel announce the next day","Merge queue or post-merge testing (Scion); flags to staff first; latest then stable channel; research-preview branding","Live change behind a flag; announcement"),
("Operate and learn","Weekly on-call; CI team; security engineers “monitoring loops”","Claude Tag CI first responder; per-component “superfan” agents; an alert agent that writes the fix but cannot deploy; incidents become reviewer evals","Post-mortem, fix PR, lessons.md, new evals, CLAUDE.md edits"),
]
hand=[
("Channels → research (feedback consolidation)","Claude Tag reads granted channels and consolidates requests and weekly issues; automated morning feedback summary; hourly loop on #project-feedback","documented"),
("Talk to customers → research","PMs read consented transcripts and classify each failure, which routes it to a team","documented"),
("Research (failure description) → shape intent (eval)","“The failure description becomes an eval”, run on each new model","documented"),
("Research (plugins: usage data, quotes) → shape intent (PRD)","Stacked plugins in one Cowork session draft the PRD","documented"),
("Research (readouts) → set goal","Weekly metrics readouts and written principles let people decide without the PM; agent role not stated","inferred"),
("Spot the opportunity → shape intent","People notice latent demand; side-quest sprints; no artifact shown","inferred"),
("Set goal → shape intent","Six-monthly themes, monthly JIT sheet; people choose","inferred"),
("Shape intent → plan, code","“Send [the spec] to Claude Code and see if it can build it”; prototypes go to internal users, then become the build","documented"),
("Shape intent (Claude Design) → code","Handoff to Claude Code, which continues from the design","documented"),
("Shape intent (design doc) → plan (security)","Opus security review reads design docs against an org-wide knowledge index; low risk self-approves","documented"),
("Research (one person) → plan (another person)","Not described. One person carries it in their session; across people the inferred carriers are public channels, prototypes and Claude-written explainers","unknown"),
("intent.md → spec.md → plan.md chain","Prescribed by the playbook for customers; no Anthropic team shown using it","unknown"),
("Plan (plan mode) → write code","Plan mode first, then auto-accept edits once the plan is right","documented"),
("Any Slack thread → write code (internal Tag)","Changes start from a Claude session in Slack; the internal Tag merges more than half of code, humans own approval","documented"),
("Write code → review","Self-verification, fresh-context subagent, AI review against the PR’s stated intent, security review, CI, risk classifier","documented"),
("Review → shape intent (change direction)","In the thread: someone asks why or cites an earlier decision; the author closes or reshapes the PR","documented"),
("Review → release","Merge queue or post-merge testing; flags to staff; latest then stable","documented"),
("Release → operate","Weekly on-call; component superfans; CI first responder","documented"),
("Operate → write code","Alert agent root-causes and writes the fix through review; cannot deploy","documented"),
("Operate → shared knowledge","lessons.md promoted into skills; incidents become reviewer evals; repeat findings into CLAUDE.md or REVIEW.md","documented"),
]
trs=''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in rows)
GAPCLS=' class="row-gap"'
hrs=''.join(f'<tr{GAPCLS if s=="unknown" and "another" in a else ""}><td>{a}</td><td>{b}</td><td>{st(s)}</td></tr>' for a,b,s in hand)
nd=sum(1 for h in hand if h[2]=='documented'); ni=sum(1 for h in hand if h[2]=='inferred'); nu=sum(1 for h in hand if h[2]=='unknown')

body='''<div class="wrap">
<header>
  <div class="eyebrow">Anthropic (own use) · lifecycle map by task · 24 Oct 2026</div>
  <h1>Where Anthropic’s agents sit in its own product lifecycle, task by task</h1>
  <p class="lede">The same frame as the Stripe map. Anchored on tasks, not job titles: at Anthropic, PMs code, designers build, and pods are sometimes one engineer. Built from Anthropic’s own posts, guides and staff interviews, so almost everything is first-party and self-reported. Each handoff is marked documented, inferred or unknown.</p>
</header>

<div class="answer">
  <h2>Research → plan across people isn’t in the record; the open channel stands in for it</h2>
  <ol>
    <li><strong>“The channel is the context.”</strong> Work defaults to open Slack channels with a resident Claude Tag. Agents read threads, past decisions and code instead of receiving a handoff document, and course corrections happen in the thread.</li>
    <li><strong>One person usually carries research, intent and plan, and the prototype is the spec.</strong> Planning moved from design docs to prototypes in front of internal users; a spec is tested by sending it to Claude Code. Plan mode starts from what the builder types.</li>
    <li><strong>Where Anthropic names a break, it is meetings → documents and personal agents.</strong> The Cowork guide names “decisions and customer insights lost between meetings and PRDs”; another post warns that “fleets of personal AIs” fracture a team’s context. Cowork sessions and Claude Code projects have a single owner.</li>
    <li><strong>The playbook’s intent.md → spec.md → plan.md chain is a prescription for customers.</strong> No source shows Anthropic’s own teams using it.</li>
  </ol>
  <p><strong>Against Stripe:</strong> both rely on one person doing research to plan. Stripe bridges people through shared tools and docs; Anthropic bridges them through public-by-default channels with an agent in them. That substitute assumes an openness regulated orgs may refuse, so the seam to build for for split-role orgs is unchanged: research → intent → plan, across people.</p>
</div>

<div class="diagram" role="figure" aria-label="Swimlane diagram of Anthropic's own lifecycle by task">
''' + svg + '''
</div>

<section>
  <h2>Task by task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it at Anthropic</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>''' + trs + '''</tbody>
  </table></div>
  <p class="foot">No row added or split. Two Anthropic differences sit inside rows: evals as an intent artifact (shape the intent), and one monitoring agent per component (operate and learn).</p>
</section>

<section>
  <h2>Every handoff, task to task</h2>
  <p>''' + f'{nd} documented, {ni} inferred, {nu} unknown.' + '''</p>
  <div class="tablewrap"><table>
    <thead><tr><th>From → to</th><th>How</th><th>Status</th></tr></thead>
    <tbody>''' + hrs + '''</tbody>
  </table></div>
</section>

<section>
  <h2>What it means for our options</h2>
  <ul class="impl">
    <li><strong>A shared, agent-readable place to work is Anthropic’s substitute for handoff artifacts.</strong> It costs openness by default, which bears on trust and privacy defaults in a regulated org.</li>
    <li><strong>The eval as the intent artifact</strong> (examples plus golden answers, run on every model) is distinctive to Anthropic and adds an option for intent shaping.</li>
    <li><strong>Review is the most engineered task:</strong> classifiers set risk tiers, low-risk changes merge with no human approval, an agent’s approval never counts as a person’s, and incidents become the reviewer’s eval set.</li>
    <li><strong>The playbook’s committed artifact chain is untested inside Anthropic.</strong> Cite it as a vendor prescription.</li>
  </ul>
</section>

<p class="foot">Sources, all first-party unless noted: the Claude Code team’s code review post (Oct 2026); Redesigning source control at Anthropic (Oct 2026); How Anthropic secures its AI-native SDLC (Jul 2026); Claude Tag as CI first responder (Aug 2026); Running an AI-native engineering org (Jun 2026); Product management on the AI exponential (Mar 2026); Lessons on human-agent teams (Jun 2026); How Anthropic employees use Claude Tag (Aug 2026); self-service data analytics (Jun 2026); Deploying Claude across your organization (Cowork guide); the Claude Design designer’s workflow (Jul 2026); Lenny’s Podcast with Cat Wu, Boris Cherny, Dianne Penn, Fiona Fung and Mike Krieger; the AI-native SDLC playbook (Aug 2026, a prescription for customers). Full notes: project-agent-and-harness, task research-claude-resources-articles, 02-pdlc-agent-ecosystem-map.md.</p>
</div>'''

full='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>Anthropic Agent Lifecycle Map</title>\n<style>\n'+css+'\n</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n'
open(os.path.join(OUT,'02-pdlc-agent-ecosystem-map.html'),'w').write(full)
print('ok', nd, ni, nu)
