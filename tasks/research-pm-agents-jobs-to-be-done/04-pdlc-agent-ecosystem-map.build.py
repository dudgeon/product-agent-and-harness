import sys, os
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.dirname(os.path.abspath(__file__))
# Same grid, lanes, classes and styling as the Stripe map (competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.build.py),
# so the per-ecosystem maps compare side by side.
W=124; X0=20; NCOL=10
cx=lambda i: X0+W*i+W/2
tasks=[["Spot the","opportunity"],["Talk to","customers"],["Research","the problem"],["Set the","goal"],["Shape the","intent"],["Plan the","change"],["Write the","code"],["Review the","change"],["Release"],["Operate","and learn"]]
S=[]
def box(i,y,h,lines,cls="node",span=1,size=12.5):
    x=X0+W*i+6; w=W*span-12
    t=''.join(f'<tspan x="{x+w/2:.1f}" dy="{0 if k==0 else 15.5}">{l}</tspan>' for k,l in enumerate(lines))
    ty=y+h/2-(len(lines)-1)*7.75+4.5
    return f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="7"/><text class="nt" style="font-size:{size}px" x="{x+w/2:.1f}" y="{ty:.1f}" text-anchor="middle">{t}</text>'
S.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 620" role="img" aria-labelledby="dtitle"><title id="dtitle">Intercom’s product lifecycle by task, with the humans, agents and shared tools at each task and the handoffs between them</title>')
S.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>')
for i,t in enumerate(tasks):
    S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>'+(f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t)>1 else '')+'</text>')
    if i: S.append(f'<line class="guide" x1="{X0+W*i}" y1="50" x2="{X0+W*i}" y2="500"/>')
for y,l in [(86,"HUMANS · ANY ROLE"),(226,"AGENTS"),(426,"SHARED")]:
    S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0+W*NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="412" x2="{X0+W*NCOL}" y2="412"/>')
hum={0:["leaders,","top-down"],1:["research &","data science","team"],2:["researchers,","data sci.,","PMs, sales"],3:["not described"],4:["designers","(in code),","PMs"],5:["engineers"],6:["engineers;","also designers,","PMs, TPMs"],7:["a person on","~80% of PRs"],8:["shipping eng.","owns rollback;","NPI manager"],9:["engineers,","support eng.,","PM leaders"]}
for i,l in hum.items():
    S.append(box(i,96,92,l,"pnode acc" if i in (0,3) else "pnode"))
ag={2:["Claude Code +","Claude4Data;","Cockpit"],4:["Claude Code","prototypes ·","Surge"],5:["plan mode,","held in the","session"],6:["Claude Code","267 skills;","~94% of PRs"],7:["Shrek","reviewers;","~19% auto"],9:["prod console","(MCP); incident","skill"]}
for i,l in ag.items(): S.append(box(i,238,92,l))
S.append(box(1,238,92,["AI-moderated","interviews","(churn, pilots)"],"node lite"))
S.append(box(8,238,92,["auto-deploy","~12 min;","Operator → Fin"],"auto"))
S.append(box(0,436,56,["Claude Code plugins and skills (267, installed by MDM) · Surge design system · Snowflake semantic layer · GitHub · Slack · release tracker · Honeycomb, Datadog"],"sub",span=NCOL,size=13))
def arrow(d,cls="doc",mk="ah"): S.append(f'<path class="{cls}" d="{d}" marker-end="url(#{mk})"/>')
y=284
arrow(f"M{X0+W*2-6} {y}H{X0+W*2+6}")   # interviews -> research (documented)
arrow(f"M{X0+W*6-6} {y}H{X0+W*6+6}")   # plan -> code (same session)
S.append(f'<text class="cap" x="{X0+W*6:.1f}" y="{y-50}" text-anchor="middle">same session</text>')
arrow(f"M{X0+W*7-6} {y}H{X0+W*7+6}")   # code -> review
S.append(f'<text class="cap" x="{X0+W*7:.1f}" y="{y+62}" text-anchor="middle">PR states why</text>')
arrow(f"M{X0+W*8-6} {y}H{X0+W*8+6}")   # review -> release
arrow(f"M{X0+W*9-6} {y}H{X0+W*9+6}")   # release -> operate
S.append(f'<text class="cap" x="{X0+W*9:.1f}" y="{y-50}" text-anchor="middle">“what we built” doc</text>')
arrow(f"M{cx(4):.1f} 330 C{cx(4):.1f} 384 {cx(6)-40:.1f} 384 {cx(6)-18:.1f} 332")  # prototype -> code
S.append(f'<text class="cap" x="{cx(4)+4:.1f}" y="350" text-anchor="start">prototype + tighter brief</text>')
# research -> shape intent gap
S.append(f'<path class="gap" d="M{cx(2)+26:.1f} 238 C{cx(2)+60:.1f} 200 {cx(4)-60:.1f} 200 {cx(4)-26:.1f} 236" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{(cx(2)+cx(4))/2:.1f}" cy="208" r="12"/><text class="gapq" x="{(cx(2)+cx(4))/2:.1f}" y="214" text-anchor="middle">?</text>')
# operate (Fin data) -> own research gap, drawn under the agents lane
P0=(cx(9)-10,332); P1=(cx(9)-40,400); P2=(cx(2)+60,400); P3=(cx(2)+16,334)
S.append(f'<path class="gap" d="M{P0[0]:.1f} {P0[1]} C{P1[0]:.1f} {P1[1]} {P2[0]:.1f} {P2[1]} {P3[0]:.1f} {P3[1]}" marker-end="url(#ahg)"/>')
bz=lambda t,k: (1-t)**3*P0[k]+3*(1-t)**2*t*P1[k]+3*(1-t)*t*t*P2[k]+t**3*P3[k]
gx,gy=bz(0.22,0),bz(0.22,1)
S.append(f'<circle class="gapdot" cx="{gx:.1f}" cy="{gy:.1f}" r="12"/><text class="gapq" x="{gx:.1f}" y="{gy+6:.1f}" text-anchor="middle">?</text>')
S.append(f'<text class="cap" x="{gx-18:.1f}" y="{gy-10:.1f}" text-anchor="end">Fin data → own roadmap</text>')
# humans use agents
for i in (2,4,5,6): arrow(f"M{cx(i):.1f} 188V236","inf")
# substrate
arrow(f"M{cx(6):.1f} 436V332"); S.append(f'<text class="cap" x="{cx(6)+5:.1f}" y="426">skills, hooks</text>')
S.append(f'<path class="doc" d="M{cx(9)+20:.1f} 332V434" marker-end="url(#ah)"/><text class="cap" x="{cx(9)+16:.1f}" y="426" text-anchor="end">gaps → skills</text>')
ly=530
S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+52}" y="{ly+5}">documented by Intercom</text>')
S.append(f'<path class="inf" d="M{X0+250} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+302}" y="{ly+5}">a person uses the agent for the task</text>')
S.append(f'<path class="gap" d="M{X0+600} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0+652}" y="{ly+5}">not described in any source</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly+40}">Column headers are tasks (same rows as the Stripe map). Accent: tasks with no tool or process shown. Our own diagram, not Intercom’s UI.</text>')
S.append('</svg>')
svg='\n'.join(S)

def st(s): return {'d':'<span class="status s-doc">documented</span>','i':'<span class="status s-inf">inferred</span>','u':'<span class="status s-unk">unknown</span>','a':'<span class="status s-doc">documented</span> <span class="status s-inf">anecdote</span>'}[s]
rows=[("Spot the opportunity","Leadership, top-down: the CEO narrowed the company to customer service and bet on AI","None named","Not described"),
("Talk to customers","Research and data science researchers","AI-moderated interviews for churn studies, pilots and well-defined topics; early discovery and current customers stay human","Transcripts; a 60+ interview study turned into a queryable skill"),
("Research the problem, read the data","Researchers, data scientists, PMs, sales reps","Claude Code with Claude4Data (30+ analytics skills) and company-metric guidance skills; Cockpit clusters customer feedback","HTML and Snowflake/Streamlit reports; daily win/loss feed; leadership deal briefing"),
("Set the goal","Not described (the CTO names company measures: release throughput, idea-to-release time)","None named","Not described"),
("Shape the intent","Designers, primarily in code; PMs, closer to customers","Claude Code prototypes on production components and live data; Surge design system; Figma as a whiteboard","Prototypes (“the new wireframe”), tighter briefs; no PRD template found"),
("Plan the change","Engineers, who own “the shape of the solution”","Claude Code plan mode, 5–20 turns before building","A plan held in the session, not persisted"),
("Write the code","Engineers; also designers, PMs and TPMs","Claude Code: 13 plugins, 267 skills from 153 contributors; ~93–94% of PRs agent-driven; cloud agents a small share","PR whose description states why (create-pr skill, hook-enforced)"),
("Review the change","A person on ~80% of PRs; repo owners set requirements","Shrek: review sub-agents (Claude, Codex) on GitHub webhooks, with evals; ~19% auto-approved by size and risk; CI-watching agent; QA sessions → GitHub issues","Approved, labelled, logged PR"),
("Release","Automated; the shipping engineer owns rollback; an NPI manager owns support readiness","Auto-deploy (313 in a day, ~12 min merge to production); Fin: replay tests with AI judges, A/B, staged rollout; Operator drafts support content and FAQ tests","Live change; tested support content and sign-off"),
("Operate and learn","Engineers; support engineers, design managers and PM leaders use the production console","Read-only production console over MCP; incident skill; launch monitors on resolution rate and CX score; SessionEnd hook mines sessions for missing skills","Answers; issues for new skills; updated CLAUDE.md")]
hand=[("Talk to customers → research","Interview studies become a queryable skill; existing calls and win/loss are synthesised first",'d',False),
("Research → shape intent","Not described: reports, the interview skill and Cockpit clusters exist, but no source says how findings reach designers, PMs or engineers",'u',True),
("Research, spot the opportunity → set the goal","Not described",'u',False),
("Set the goal → shape intent","People; no tool shown",'i',False),
("Shape intent (prototype) → plan and build","Prototypes convey intent and tone, implementation left to engineers; tighter briefs, fast reviews, clear criteria",'d',False),
("Shape intent → code, when a designer or PM codes it","The same person uses Claude Code directly; no ticket or spec hop described",'i',False),
("Design system → write code","Auto-installed skills encode Surge and React standards; agent use of existing components 7% → 96%",'d',False),
("Plan → write code","Same session; the plan stays in session memory",'a',False),
("Write code → review","Hook-enforced create-pr skill writes why into the PR; GitHub webhook triggers Shrek, which checks the diff against that intent",'d',False),
("QA session → tracked work","Recording → video-transcript skill → QA follow-up skill → GitHub issues",'d',False),
("Review → release","Approved merge triggers automatic deploy; non-approved PRs go to a person with a Slack notice",'d',False),
("Release → support knowledge (Fin)","“What we built” doc in the release tracker plus walkthrough notes → Operator drafts and FAQ tests → NPI manager signs off",'d',False),
("Operate → harness learning","SessionEnd hook → gap classified → Slack post and GitHub issue → new skill; promotion at 50 weekly users; weekly CLAUDE.md fact-check",'d',False),
("Operate (Fin data) → Intercom’s own roadmap","Not described; Fin Insights is documented only as a customer product",'u',True)]
trows='\n'.join(f'      <tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in rows)
GAP=' class="row-gap"'
hrows='\n'.join(f'      <tr{GAP if g else ""}><td>{a}</td><td>{b}</td><td>{st(s)}</td></tr>' for a,b,s,g in hand)
nd=sum(1 for h in hand if h[2] in 'da'); ni=sum(1 for h in hand if h[2]=='i'); nu=sum(1 for h in hand if h[2]=='u')

body=f'''<div class="wrap">
<header>
  <div class="eyebrow">PM agents research · Intercom lifecycle map by task · 24 Oct 2026</div>
  <h1>Where Intercom’s agents sit in the product lifecycle, task by task</h1>
  <p class="lede">Same frame as the Stripe map: rows are tasks, not job titles. At Intercom engineers take on PM work, designers work in code, and nearly every employee has Claude Code. Each handoff is marked documented, inferred or unknown ({nd} documented, {ni} inferred, {nu} unknown). Almost every source is Intercom’s own, and every figure is self-reported.</p>
</header>

<div class="answer">
  <h2>Intent is captured downstream, at the pull request; upstream, research → intent → plan is left to people</h2>
  <ol>
    <li><strong>Downstream, the “why” is written down and checked.</strong> A hook forces a PR skill that asks why the change exists; review agents check the diff against that intent; a “what we built” doc feeds the support agent’s readiness gate at launch.</li>
    <li><strong>No source describes research reaching intent or plan.</strong> The research team’s syntheses live in sessions, reports and a queryable interview skill; how they reach designers, PMs or engineers isn’t described.</li>
    <li><strong>The plan isn’t an artifact.</strong> Engineers plan in 5–20 Claude Code turns with no formal spec; the plan stays in the session (one engineer’s account).</li>
    <li><strong>Fin’s customer data isn’t shown feeding Intercom’s own roadmap.</strong></li>
  </ol>
  <p><strong>Across people:</strong> like Stripe, Intercom shrinks the seam by collapsing roles. Where research, shaping and planning still sit with different people, the first durable statement of intent is the PR description, written after the plan.</p>
</div>

<div class="diagram" role="figure" aria-label="Swimlane diagram of Intercom's lifecycle by task">
{svg}
</div>

<section>
  <h2>Task by task</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it at Intercom</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>
{trows}
    </tbody>
  </table></div>
  <p class="foot">No rows were added. QA sessions sit under review; support-agent readiness (Fin new-product introduction) sits under release, because Intercom treats it as a release gate.</p>
</section>

<section>
  <h2>Every handoff, task to task</h2>
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
    <li><strong>Re-capture intent at the PR, then verify it in review.</strong> Cheap and enforceable, but it comes after planning, so it can’t stop a well-built wrong thing.</li>
    <li><strong>One general harness plus a governed skills marketplace, not a set of named agents.</strong> The only named custom agents are the reviewer (Shrek) and Operator; Stripe, by contrast, names an agent per task.</li>
    <li><strong>Write-back after release is a first-class step.</strong> Support knowledge is a launch gate; harness gaps come back as skills.</li>
    <li><strong>The seam to build for is research → shaped intent, with the evidence attached.</strong> Intercom’s research team is heavily AI-assisted, but its handoff to the people who shape work isn’t on record.</li>
  </ul>
</section>

<p class="foot">Sources (first-party unless noted): Intercom’s ideas.fin.ai posts by Brian Scanlan (Mar and Jul 2026), Darragh Curran, CTO (Apr and May 2026), John Moriarty (Mar 2026), Molly Mahar (Jan 2026), Clíona de Róiste (Jul 2026), Karen Church (Jul 2026), Maia Bridi (Feb 2026), Pedro Tabacof (Aug 2026), Andrii Yakovenko (Mar 2026), Andrew Walker (Mar 2026, anecdotal); the Intercom blog on AI-approved PRs (Apr 2026) and Fin new-product introduction (Jun 2026); Eoghan McCabe on Lenny’s Podcast (Aug 2025); How I AI with Brian Scanlan (Apr 2026). No independent account of Intercom’s process was found. Full notes: project-agent-and-harness, task research-pm-agents-jobs-to-be-done, 04-pdlc-agent-ecosystem-map.md.</p>
</div>'''

css=r'''/* Layout: one reading column with a wide, scrollable task-by-task swimlane; tables below. Ink on cool paper; one amber accent for the undocumented handoff and the tasks only people do. */
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
full='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<title>Intercom Agent Lifecycle Map</title>\n<style>\n'+css+'\n</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n'
open(os.path.join(OUT,'04-pdlc-agent-ecosystem-map.html'),'w').write(full)
print('ok', nd, ni, nu)
