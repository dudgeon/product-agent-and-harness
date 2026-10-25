"""Builds 01-pdlc-agent-ecosystem-map.html (standalone) for the Atlassian map.

Structure and styling reused from the Stripe map's generator
(../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.build.py)
so the two maps compare side by side. Usage: python3 01-pdlc-agent-ecosystem-map.build.py <outdir>
"""
import sys, os
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
W=124; X0=20; NCOL=10
cx=lambda i: X0+W*i+W/2
tasks=[["Spot the","opportunity"],["Talk to","customers"],["Research","the problem"],["Set the","goal"],["Shape the","intent"],["Plan the","change"],["Write the","code"],["Review the","change"],["Release"],["Operate","and learn"]]
chain=["Idea","Insight","Research","Goal","Intent","Spec, plan","Draft PR","AC check","",""]
S=[]
def box(i,y,h,lines,cls="node",span=1,size=12.5):
    x=X0+W*i+6; w=W*span-12
    t=''.join(f'<tspan x="{x+w/2:.1f}" dy="{0 if k==0 else 15.5}">{l}</tspan>' for k,l in enumerate(lines))
    ty=y+h/2-(len(lines)-1)*7.75+4.5
    return f'<rect class="{cls}" x="{x:.1f}" y="{y}" width="{w:.1f}" height="{h}" rx="7"/><text class="nt" style="font-size:{size}px" x="{x+w/2:.1f}" y="{ty:.1f}" text-anchor="middle">{t}</text>'
S.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 620" role="img" aria-labelledby="dtitle"><title id="dtitle">Atlassian’s product lifecycle by task, with the humans, agents and shared objects at each task and the handoffs between them</title>')
S.append('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mk"/></marker><marker id="ahg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1L9 5L0 9" fill="none" class="mkg"/></marker></defs>')
for i,t in enumerate(tasks):
    S.append(f'<text class="stage" x="{cx(i):.1f}" y="24" text-anchor="middle"><tspan x="{cx(i):.1f}">{t[0]}</tspan>'+(f'<tspan x="{cx(i):.1f}" dy="18">{t[1]}</tspan>' if len(t)>1 else '')+'</text>')
    if chain[i]: S.append(f'<text class="chain" x="{cx(i):.1f}" y="66" text-anchor="middle">{chain[i]}</text>')
    if i: S.append(f'<line class="guide" x1="{X0+W*i}" y1="50" x2="{X0+W*i}" y2="500"/>')
for y,l in [(86,"HUMANS · ANY ROLE"),(226,"AGENTS AND TOOLS"),(426,"SHARED")]:
    S.append(f'<text class="lane" x="{X0}" y="{y}">{l}</text>')
S.append(f'<line class="lanerule" x1="{X0}" y1="212" x2="{X0+W*NCOL}" y2="212"/><line class="lanerule" x1="{X0}" y1="412" x2="{X0+W*NCOL}" y2="412"/>')
hum={0:["no internal","account"],1:["Jira team’s","user studies;","PMs steer"],2:["anyone, up to","the CEO, asks","Rovo"],3:["“people decide","what and why”"],4:["PMs, designers","prototype; a","Loom talk track"],5:["tech leads, EMs,","PMs (claimed)"],6:["engineers; a PM","on Confluence,","none on Jira"],7:["a person on","the draft PR"],8:["not shown"],9:["incident","responders; a","PM’s update bot"]}
for i,l in hum.items():
    cls="pnode acc" if i in (3,) else "pnode"
    S.append(box(i,96,92,l,cls))
ag={2:["Rovo Chat ·","Deep","Research"],4:["Loom","Record for","agent"],5:["Jira Planner","(Early Access)","spec → items"],6:["Coding agents","Rovo Dev, Claude,","Cursor, Copilot"],7:["Rovo Dev","reviewer:","AC check"],9:["Ops Expert;","Delivery","Agent"]}
for i,l in ag.items(): S.append(box(i,238,92,l))
S.append(box(0,238,92,["JPD ideas ·","Loom bug","reports"],"node lite"))
S.append(box(1,238,92,["Loom meeting:","Rovo suggests","updates"],"node lite"))
S.append(box(3,238,92,["Goals","(Atlassian","Home)"],"node lite"))
S.append(box(8,238,92,["Rovo Dev in","Pipelines","(beta)"],"auto"))
S.append(box(0,436,56,["Jira work items (the handoff medium) · Confluence pages · JPD ideas · Goals · Loom · Teamwork Graph (pairwise links) · Bitbucket / GitHub · Slack · Rovo MCP + A2A (inbound)"],"sub",span=NCOL,size=12.5))
def arrow(d,cls="doc",mk="ah"): S.append(f'<path class="{cls}" d="{d}" marker-end="url(#{mk})"/>')
y=284
arrow(f"M{X0+W*6-6} {y}H{X0+W*6+6}")   # Planner -> coding agents
S.append(f'<text class="cap" x="{X0+W*6:.1f}" y="{y-50}" text-anchor="middle">assign</text>')
arrow(f"M{X0+W*7-6} {y}H{X0+W*7+6}")   # code -> review
arrow(f"M{X0+W*8-6} {y}H{X0+W*8+6}")   # review -> pipelines
arrow(f"M{cx(4):.1f} 330 C{cx(4):.1f} 384 {cx(6)-40:.1f} 384 {cx(6)-18:.1f} 332")  # Loom -> coding agent via In Progress
S.append(f'<text class="cap" x="{cx(5):.1f}" y="398" text-anchor="middle">work item → In Progress → agent</text>')
# research -> intent/plan gap
S.append(f'<path class="gap" d="M{cx(2)+26:.1f} 238 C{cx(2)+70:.1f} 200 {cx(5)-70:.1f} 200 {cx(5)-26:.1f} 236" marker-end="url(#ahg)"/>')
S.append(f'<circle class="gapdot" cx="{(cx(2)+cx(5))/2:.1f}" cy="208" r="12"/><text class="gapq" x="{(cx(2)+cx(5))/2:.1f}" y="214" text-anchor="middle">?</text>')
# humans -> agents
for i in (2,4,5,6): arrow(f"M{cx(i):.1f} 188V236","inf")
# down into the shared objects
arrow(f"M{cx(0):.1f} 332V434"); S.append(f'<text class="cap" x="{cx(0)+5:.1f}" y="352">idea → item</text>')
arrow(f"M{cx(1):.1f} 332V434"); S.append(f'<text class="cap" x="{cx(1)+5:.1f}" y="352">item updates</text>')
arrow(f"M{cx(3):.1f} 332V434"); S.append(f'<text class="cap" x="{cx(3)+5:.1f}" y="352">Goals field</text>')
arrow(f"M{cx(9):.1f} 332V434"); S.append(f'<text class="cap" x="{cx(9)-5:.1f}" y="352" text-anchor="end">PIR actions → items</text>')
# up from the shared objects
arrow(f"M{cx(7):.1f} 436V332"); S.append(f'<text class="cap" x="{cx(7)+5:.1f}" y="426">reads item’s AC</text>')
ly=530
S.append(f'<path class="doc" d="M{X0} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+52}" y="{ly+5}">documented by Atlassian</text>')
S.append(f'<path class="inf" d="M{X0+250} {ly}h40" marker-end="url(#ah)"/><text class="leg" x="{X0+302}" y="{ly+5}">a person uses the agent for the task</text>')
S.append(f'<path class="gap" d="M{X0+600} {ly}h40" marker-end="url(#ahg)"/><text class="leg" x="{X0+652}" y="{ly+5}">research → intent / plan: not described in any source</text>')
S.append(f'<text class="cap" x="{X0}" y="{ly+40}">Column headers are tasks; the italic row is the object each task leaves behind. Shaded boxes are tools or objects rather than agents. Accent: decided by people, no agent. Our own diagram, not Atlassian’s UI.</text>')
S.append('</svg>')
svg='\n'.join(S)

# CSS: identical to the Stripe map so the two read as a set.
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
.foot{font-size:13.5px; color:var(--muted); max-width:82ch}
.tag{font-family:var(--mono); font-size:11.5px; color:var(--muted)}'''

D='<span class="status s-doc">documented</span>'
I='<span class="status s-inf">inferred</span>'
U='<span class="status s-unk">unknown</span>'
V='<span class="status s-inf">vendor claim</span>'
SP='<span class="status s-inf">speaker report</span>'
handoffs=[
 ("Talk to customers (Loom meeting) → existing work items","Meeting connected to a Jira space; Rovo reads the transcript and suggests reassignments, priority, status or comments; the owner accepts or discards each",D,False),
 ("Any recording → bug work item","Loom AI drafts a bug report with steps and a video link; “Create in Jira”",D,False),
 ("Talk to customers (insight videos) → triage","<span class=\"tag\">internal</span> JSM to review videos; a Rovo agent categorised 900+ items",D+" "+SP,False),
 ("Triaged insight → engineering","“Then we knew what to send to engineering”; how it was sent is not said",U,False),
 ("Research (Rovo Chat, Deep Research) → shape intent or plan","The report stays in Rovo Chat; no source has Planner, a JPD idea or a PRD consuming it",U,True),
 ("Research → Confluence page","“Can be effortlessly exported to your Confluence page” (2025 engineering blog; not in the support doc)",D+" "+V,False),
 ("Set the goal → work items","Goals field on a work item; a Teamwork Graph edge from work item to goal; the Delivery Agent reads goal context",D,False),
 ("Set the goal → JPD idea","A “Goals” field on ideas is reported; whether it is the Goals object is unverified",U,False),
 ("Spot the opportunity (JPD idea) → delivery work item","Delivery link from the idea; optional “Embed the idea description and fields into the work item”",D,False),
 ("JPD idea (embedded) → coding agent","The agent reads the work item description, so an embedded copy reaches it; no source shows an agent following the idea link",I,False),
 ("Shape intent (Loom talk track) → work items","Record for agent → action plan → “Create in Jira”: work items “for agents to act on”",D,False),
 ("Work item → prototype by a coding agent","<span class=\"tag\">internal</span> Moving the item to In Progress “automatically kicks off a coding agent” in the real front-end repo on a managed cloud agent; the guide lists a workflow-transition trigger",D,False),
 ("Prototype → developers","<span class=\"tag\">internal</span> Code already in the repo and design language, so “the handoff to developers was much faster”; how developers took it over is not described",D+" "+SP,False),
 ("Shape intent → plan (Jira Planner)","Idea → clarifying questions → readiness check → Confluence Live Doc spec → sequenced work items with acceptance criteria (Early Access)",D+" "+V,False),
 ("JPD idea, goal or research page → Planner","Planner “pulls in context from Teamwork Graph”, which includes JPD customer insights; no source says Planner reads them",I,False),
 ("Plan (work item) → write code (any assigned agent)","Assign, @mention or automation rule; Claude, Cursor, Copilot, Codex or the Jira Coding Agent",D,False),
 ("Confluence spec → coding agent","Interactive: reads Confluence as the user. Automation: “restricted mode … won’t read Confluence content”. Default reading of linked pages: not stated",D+" "+U,False),
 ("Work item → local coding tool","Deep link passes “summary and description” (the blog adds “linked docs”)",D,False),
 ("Teamwork Graph → third-party coding agents","Claimed that agents draw context from the graph; for third-party agents outside the Rovo MCP server, no mechanism",U,False),
 ("Write code → review","Work item key in the branch name links PR to item; Rovo Dev checks the PR against the item’s acceptance criteria; no check if the description is empty",D,False),
 ("Review comments and CI failures → coding agent","<span class=\"tag\">internal</span> Not automatic yet; the engineer goes back to the Jira session",D+" (a gap)",False),
 ("Review → release","Pipelines summarises “from commits, Jira work items, and other deployment data” (beta)",D,False),
 ("Operate (incident) → learn (backlog)","Ops Expert can “Create Jira tickets for action items in this PIR”; summarises past PIRs for new incidents",D,False),
 ("Operate (alert + bug) → write code","Automation starts a coding agent that gets telemetry “through the Teamwork Graph MCP”",D+" "+V,False),
 ("Internal feedback in Slack → write code","<span class=\"tag\">internal</span> The Jira agent in Slack triaged feedback and bugs and sent them to the coding agent",D+" "+SP,False),
 ("Operate → stakeholders","Delivery Agent status reports; <span class=\"tag\">internal</span> a PM’s agent writes his weekly updates; the CEO asked Rovo instead of the PM",D,False),
 ("Learn → the next spec","“Results feed back into the next spec”; no mechanism",U,False),
]
GAPCLS=' class="row-gap"'
hrows='\n'.join(f'      <tr{GAPCLS if g else ""}><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c,g in handoffs)

body='''<div class="wrap">
<header>
  <div class="eyebrow">Atlassian ecosystem · lifecycle map by task · 24 Oct 2026</div>
  <h1>Where Atlassian’s agents sit in the product lifecycle, task by task</h1>
  <p class="lede">Same frame as the Stripe map. Rows are tasks, not job titles. Most evidence describes what Atlassian sells (support docs, launch posts); a few sources describe how Atlassian’s own teams work, marked <span class="tag">internal</span>. Each handoff is marked documented, inferred or unknown. Every figure is Atlassian’s own.</p>
</header>

<div class="answer">
  <h2>The work item carries the what, not the why</h2>
  <p>Atlassian has an object at every step (idea, goal, spec, work item, pull request) and links between most of them. Context breaks between research and the first shaped artifact, and in what a work item copy leaves out.</p>
  <ol>
    <li><strong>Research output stays in chat.</strong> Rovo Deep Research writes a cited report in Rovo Chat; export to Confluence is claimed only in a 2025 blog. Customer insight is triaged by agents, but the documented outputs are bugs and updates to existing work items, not new ideas or specs.</li>
    <li><strong>What crosses from intent to plan is a copy.</strong> A product discovery idea links to delivery work, and its owner may embed the idea’s description in the work item. That is the only documented way idea content reaches the item an agent reads; the insights stay behind the link.</li>
    <li><strong>The coding agent reads the work item; linked documents are conditional.</strong> Started by automation it “won’t read Confluence content”. Whether it follows links by default is not stated.</li>
    <li><strong>The bridge being built is a spec, and it’s early.</strong> Jira Planner (Early Access) turns a rough idea into a Confluence spec, then into work items with acceptance criteria. Whether it reads ideas, goals or research is not stated.</li>
    <li><strong>The graph links pairs; nothing ties the chain.</strong> Teamwork Graph returns a work item’s pull requests, pages and parents, but no record joins research → idea → spec → work item → PR.</li>
  </ol>
  <p><strong>Across people:</strong> on small teams (Confluence, Rovoclaw) one person researched, shaped and prototyped, so context travelled with them. On Jira, where PMs did not commit to production, Atlassian made the PM’s intent executable instead: a Loom talk track became work items, moving one to In Progress started a cloud coding agent, and the prototype landed in the real repo, so “the handoff to developers was much faster”. That carries the prototype across people, not the evidence behind it.</p>
  <p><strong>Against Stripe:</strong> Stripe’s research agent is locked in single-user sessions and its planner starts from typed intent. Atlassian has the shared, linked objects Stripe lacks, so its gap is narrower, but it sits in the same place.</p>
</div>

<div class="diagram" role="figure" aria-label="Swimlane diagram of Atlassian's lifecycle by task">
''' + svg + '''
</div>

<section>
  <h2>Task by task</h2>
  <p>The Stripe map’s ten tasks, unchanged. One difference: Jira Planner spans “shape the intent” and “plan the change”, so it appears in both rows rather than as a new one.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Task</th><th>Who does it</th><th>Agents and tools</th><th>Artifact</th></tr></thead>
    <tbody>
      <tr><td>Spot the opportunity</td><td>No internal account; Jira Product Discovery is the product for it</td><td>Product discovery ideas with custom types (user problem, bet, opportunity, solution) and attached insights; Loom turns any recording into a bug report</td><td>Idea; bug work item</td></tr>
      <tr><td>Talk to customers</td><td><span class="tag">internal</span> The Jira team ran user studies; PMs steered</td><td>Loom meetings connected to a Jira space, with Rovo suggesting updates to existing work items; <span class="tag">internal</span> a Rovo agent triaged 900+ customer-insight items</td><td>Suggested work-item updates; triaged insight list</td></tr>
      <tr><td>Research the problem, read the data</td><td><span class="tag">internal</span> Anyone: the CEO asked Rovo for a launch date instead of the PM; PMs “not compiling research by hand”</td><td>Rovo Chat; Rovo Deep Research (plans, retrieves from Teamwork Graph, writes a cited report)</td><td>Cited report in chat; Confluence export claimed only</td></tr>
      <tr><td>Set the goal</td><td>People: “people decide what and why”</td><td>Atlassian Goals: owner, date, status, monthly update, OKR score; the Delivery Agent reads goal context</td><td>Goal linked to projects, epics and work items</td></tr>
      <tr><td>Shape the intent</td><td><span class="tag">internal</span> PMs and designers prototype; a Confluence PM fixed UX in code; Rovoclaw’s PM and designer built the alpha</td><td>Loom Record for agent (open beta); coding agents for prototypes; Figma MCP; Confluence PRD and project-poster templates; Jira Planner (Early Access)</td><td>Loom action plan; work items; prototype code in the real repo; PRD or spec page</td></tr>
      <tr><td>Plan the change</td><td>Claimed audience: tech leads, senior engineers, EMs, PMs. <span class="tag">internal</span> An engineer had Rovo Dev write plans onto subtasks</td><td>Jira Planner (claimed): sequenced work items with dependencies, milestones and acceptance criteria</td><td>Work items with acceptance criteria; spec page</td></tr>
      <tr><td>Write the code</td><td>Agents, started by engineers (<span class="tag">internal</span> “probably 95% or more of my dev work”); PMs on Confluence, not on Jira</td><td>Jira Coding Agent (Rovo Dev); Claude Agent for Jira, Cursor, GitHub Copilot and Codex, all assignable from the same work item; Rovo Dev CLI; deep link to local tools</td><td>Branch and draft PR, with the user as author</td></tr>
      <tr><td>Review the change</td><td>A person reviews the draft PR, plus an agent</td><td>Rovo Dev reviewer in Bitbucket and GitHub, checking the PR against the work item’s acceptance criteria. PR cycle time −30.8% (paper) or −45% (blog), unreconciled</td><td>Review comments; acceptance-criteria check</td></tr>
      <tr><td>Release</td><td>Not shown</td><td>Rovo Dev in Bitbucket Pipelines (beta): change summaries from commits and work items, failed-build explanations; release-notes drafter</td><td>Deployment summary; release notes</td></tr>
      <tr><td>Operate and learn</td><td>Incident responders; <span class="tag">internal</span> a PM’s own weekly-update agent</td><td>Ops Expert (alerts, similar incidents, post-incident reviews); Delivery Agent (space health, stakeholder status); Jira agent in Slack triaging feedback to a coding agent</td><td>Post-incident review; its action items as work items; status reports</td></tr>
    </tbody>
  </table></div>
</section>

<section>
  <h2>Every handoff, task to task</h2>
  <p>27 handoffs: 20 documented (6 rest on a vendor claim or a speaker report only; 2 have a partly unknown mechanism), 2 inferred, 5 unknown.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>From → to</th><th>How</th><th>Status</th></tr></thead>
    <tbody>
''' + hrows + '''
    </tbody>
  </table></div>
</section>

<section>
  <h2>What a work item carries, and what it doesn’t</h2>
  <ul class="impl">
    <li><strong>Carries:</strong> summary, description and acceptance-criteria fields (which the reviewer reads); links to an idea, a goal, pages and pull requests; an embedded copy of the idea’s description if its owner chose to embed; the agent sessions and the draft PR.</li>
    <li><strong>Doesn’t carry:</strong> the research behind the idea; the shaper’s reasoning (Loom keeps the video, but only action items become work items); review feedback back to the agent (manual today); Confluence content for agents started by automation. And a link is not a read.</li>
  </ul>
</section>

<section>
  <h2>What it means for our options</h2>
  <ul class="impl">
    <li><strong>The work item is the handoff contract, and it is harness-agnostic at the code step.</strong> Five coding agents take the same item and the reviewer checks the same acceptance criteria. That favours a product agent that writes into the system of record over one that holds intent in its own sessions.</li>
    <li><strong>Copy intent into the artifact the next agent reads; don’t rely on links.</strong> The idea “embed” option and the reviewer’s empty-description rule say the same thing.</li>
    <li><strong>The seam to build for is still research → first shaped artifact.</strong> Atlassian has the objects; it has no documented path from research output into them.</li>
    <li><strong>Who may write code is a per-codebase choice.</strong> PMs committed on Confluence (isolated repo, explicit contribution model) and not on Jira.</li>
  </ul>
</section>

<p class="foot">Sources: Atlassian support docs on the Jira Coding Agent, agents in a space, the acceptance-criteria code review, Loom Record for agent, linking ideas to work items, Goals, Rovo Deep Research, the Delivery Agent, Ops Expert and Rovo Dev in Bitbucket Pipelines (first-party); Atlassian launch posts and guides on the AI-native SDLC (July 2026), Jira Planner (Aug 2026), Rovo Dev in Jira (Apr 2026) and the agentic-engineering guide (Aug 2026) (vendor claims); the Rovo Dev code-review paper (ICSE 2026, all authors Atlassian-affiliated) and blogs; the Atlassian CPO’s Lenny &amp; Friends Summit talk (Sept 2026; auto-captions, speaker-reported, no baselines). Internal-use evidence rests on that talk and one engineer’s post. Jira Planner is Early Access and known only from a launch post. Full notes: project-agent-and-harness, task user-story-mapping, 01-pdlc-agent-ecosystem-map.md.</p>
</div>'''

head_common='''<title>Atlassian Agent Lifecycle Map</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">'''
full='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+head_common+'\n<style>\n'+css+'\n</style>\n</head>\n<body>\n'+body+'\n</body>\n</html>\n'
open(os.path.join(OUT,'01-pdlc-agent-ecosystem-map.html'),'w').write(full)
print('ok', len(handoffs), 'handoffs')
