#!/usr/bin/env python3
"""Builds 02-interactions.html: the nine interactions shared, persistent agents make possible, as a before-and-after
page and an interaction map. Standalone: inline CSS, no scripts, system fonts. Content is data below; run
`python3 02-interactions.build.py` from this folder. Source: 01-synthesis.md (2026-10-26)."""
from html import escape as E

SRC = "../../research/sources/"

# ---------------------------------------------------------------- content
PROPS = [
  ("Where it runs", "The laptop. Nothing happens while the lid is closed.", "Disposable cloud workers, session cells, sandboxes per session, vendor VMs.", "Platform team"),
  ("What survives", "The transcript, deleted after 30 days by default.", "A session log outside harness and sandbox; memory files rewritten offline; skills in a repo; lessons files.", "Platform team, retention owner"),
  ("Whose authority", "The person's.", "The requester's, the creator's, the agent's own per compartment, or none (a QA devbox).", "Security and policy owner"),
  ("Who can see and join", "Nobody.", "Private and shared on demand; workspace visibility; channel-scoped; public by default with no DMs.", "Leadership (a culture decision)"),
  ("Who starts work", "The person, at the keyboard.", "A person from Slack or a phone; an emoji reaction; a ticket; a schedule or an external system.", "Product and platform teams"),
]

# Each interaction: id, title, one-line, new, speed/quality tags, mechanism, examples [(text, label)], conditions, fails, diagram kind
INTER = [
 dict(id="C1", title="One person's correction becomes everyone's baseline",
   new="The correction is written where every later session reads it: a skill in a repo, a channel's standing instructions, a lessons file, or a memory store curated by an offline job.",
   tags=["quality","speed"], mech="M3 Corrections compound",
   ex=[("Ramp Glass: 323 employees, 6,500+ edits to what Glass knows; Finance's \"UK customers\" fix", "company's own figure"),
       ("Shopify River: merge rate 36% to 77% in two months, credited to people writing down what River should have known", "CEO's figure, undefined"),
       ("Anthropic's legal channel: a counsel's correction becomes a standing instruction; a Friday routine proposes updates for approval", "first-party"),
       ("Cursor Bugbot: review comments become learned rules, 44,000+ across 110,000+ repos", "vendor claim")],
   cond="A shared, writable knowledge store read at session start; a curate step with an owner; attribution; corrections shared by default with a private exception.",
   fails="A wrong correction reaches everyone too; whole-file rewrites collapse context; mined examples were 87.5% noise at Spotify; \"6x\" with no baseline.",
   kind="correction"),
 dict(id="C2", title="A teammate joins a running session",
   new="The session is a shared object on a per-session control plane: anyone invited opens it, sees the reasoning and evidence, and adds an attributed prompt. Vendors share a snapshot; live joining is still an in-house build.",
   tags=["speed","quality"], mech="M1 No human relay",
   ex=[("Ramp Inspect: \"every session is multiplayer\"; a support agent hands a ticket session to an engineer", "first-party"),
       ("Shopify's good thread: a second human drops in with a constraint; the thread is searchable for the next person", "first-party"),
       ("Claude Code on the web: \"their view doesn't update in real time\"", "first-party"),
       ("A 2026 benchmark: one agent serving several people loses instruction accuracy under conflict", "independent, simulated")],
   cond="Per-session control plane with attributed prompts; an identity answer for the joiner's prompt; a visibility default and a way to share on demand; repo-access checks before showing a session.",
   fails="Cursor runs teammates' follow-ups on the creator's tokens by design; Open-Inspect's visibility enforcement defaults to \"shadow\"; 100 watchers are 100 interruptions.",
   kind="join"),
 dict(id="C3", title="An agent hands off to another agent with the plan attached",
   new="The plan is an artifact people and agents can read; the downstream agent is provisioned by the platform (a devbox, a sandbox, a warm Mac) and runs in parallel by default.",
   tags=["speed","quality"], mech="M2 Idle time works · M4 Verification separated",
   ex=[("Stripe Orbit: a reviewed seven-step plan, one button to a Minion that may run 12 hours and pauses to ask; 3 to 7 projects per engineer", "first-party marketing"),
       ("Claude Code projects: a coordinator delegates to parallel cloud threads on their own branches", "first-party, beta"),
       ("Block Buzz: orchestrator, two executors, a reviewer from another model family", "first-party"),
       ("Sentry Seer: root cause and solution as a structured prompt to Cursor, Claude Code or Copilot; \"never merges on its own\"", "first-party")],
   cond="A plan artifact with a stable home; an identity for the downstream agent; environment provisioning; an iteration cap and a hand-back point in code; a way to ask.",
   fails="32% of multi-agent failure labels are inter-agent misalignment, 24% verification (1,642 traces); task status lags; silent deadlocks; permission inheritance (Kiro, contested).",
   kind="handoff"),
 dict(id="C4", title="An agent runs overnight and reports in the morning",
   new="Work starts from a trigger (a ledger, a ticket, a failing PR, a cron) on a runtime that is not a laptop, and the report is waiting with evidence and a decision left to a person.",
   tags=["speed","quality"], mech="M2 Idle time works",
   ex=[("Shopify: overnight mobile bug fixes on warm remote Macs; River opened four threads for 35 findings within a minute", "first-party"),
       ("Anthropic: a daily ci-weather report; median 14 minutes to first evidence-grounded incident analysis", "first-party, unverified"),
       ("Ramp: more Inspect sessions started by automations than by humans", "CTO, no numbers"),
       ("Across millions of PRs, agent-authored merged PRs rose 0.86% to 27.6%; reverts lower than human for Codex and Claude, higher for Cursor background agents and Devin", "vendor claim")],
   cond="A cloud runtime; a service identity for unattended runs (personal connectors don't run unattended); a place to report; a human gate on the side effect; detection of silent failure.",
   fails="\"Green does not mean the work succeeded\"; slop grenades for reviewers; motion mistaken for remediation; a $1.5M token week; Replit ignored a freeze.",
   kind="overnight"),
 dict(id="C5", title="A reviewer agent waits on a shared artifact",
   new="A second agent in its own context is woken by an event on the artifact and checks it against intent, without authoring or approving it; identity stops self-approval.",
   tags=["quality","speed"], mech="M4 Verification separated from authoring",
   ex=[("Anthropic Code Review: substantive comments on 16% to 54% of PRs; under 1% marked incorrect; never approves; $15-25 per review", "first-party"),
       ("Spotify Honk's judge vetoes about a quarter of runs, mostly scope creep; half correct course", "first-party"),
       ("Intercom: about 19% of PRs auto-approved by risk; the shipping engineer stays accountable", "first-party"),
       ("Industrial study: 73.8% of reviewer comments resolved, but PR closure rose from 5h52m to 8h20m", "independent")],
   cond="The artifact in an event-bearing shared place; a fresh context for the judge; the original intent or a rubric; separation of duties by identity; risk tiers.",
   fails="Review is \"now becoming a big bottleneck\"; \"marked incorrect\" is disagreement, not recall; judges favour their own generations; no evals for the judge.",
   kind="reviewer"),
 dict(id="C6", title="People watch a thread and steer it",
   new="The conversation that already holds the context is where the work happens; channel memory is injected at session start, and any member can redirect.",
   tags=["speed","quality"], mech="M5 Decisions reach the owner · M1 No relay",
   ex=[("Shopify: #tobi_river with 100+ watchers; 171,853 same-thread links in September 2026 (volume, not outcome)", "first-party"),
       ("Stripe: Minions in a public \"robots\" channel 76 people follow; \"we pair prompt\"", "first-party"),
       ("Block Builderbot: steered mid-task in the thread; \"the conversation is the development environment\"", "vendor claim"),
       ("River itself: \"Some questions that would have been asked in a DM just don't get asked\"", "first-party, written by the agent")],
   cond="A visibility default and a deliberate path to private; channel memory and pre-loaded skills; an identity for the agent in the channel and a rule for who may direct it.",
   fails="Chilling effect; Bernstein's curtains raised output 10-15% (a 2009 factory); channel membership becomes the access boundary; noise is unmeasured anywhere.",
   kind="watch"),
 dict(id="C7", title="Traces reveal where to standardise",
   new="Sessions retained in one place let a platform team read across them and fix the harness, skills or tooling, instead of each person fixing their prompt.",
   tags=["quality","speed"], mech="M3 Corrections compound",
   ex=[("Shopify: River's unit-test failures became an ML test-selection model, saving about 30 minutes per task; the Jev classifier tags every mobile conversation", "first-party"),
       ("Stripe: telemetry sorts 2,000 skills into about 50 daily, 100-150 by sub-org, a long tail; promotes by evidence", "first-party"),
       ("Intercom: a SessionEnd hook classifies each transcript's gaps and opens a pre-filled issue", "first-party"),
       ("Research: workflows mined from traces help on web benchmarks; mined SKILL.md files read well but did not transfer", "independent")],
   cond="Traces retained and readable under a retention and works-council policy; a classifier; a team empowered to change defaults; a path from finding to skill.",
   fails="Activity is not outcome; chat-mined expertise was off by 21 points; monitoring rules; the classifier's error rate is never reported.",
   kind="traces"),
 dict(id="C8", title="An agent asks the right person a question",
   new="A persistent agent can wait, reach someone else, and address the owner rather than the requester, because it has ownership data and a channel. Routing to the right person is mostly not built yet.",
   tags=["quality","speed"], mech="M5 Decisions reach the owner with evidence",
   ex=[("Shopify: \"hand off the decision, not the investigation\"; the smallest question an owner has to answer; River dropped its own patch after a developer's question", "first-party"),
       ("A Stripe Minion pauses to ask mid-run; Cowork asks \"a call only you can make\" on the phone", "first-party"),
       ("Cursor's agentic codeowners pick reviewers by contribution history; AWS: separate escalation from routing", "vendor claim"),
       ("MAST: failure to ask for clarification was 6.8% of failure labels", "independent")],
   cond="Ownership data the agent can read; a channel to reach the person; a resumable session; a policy on when to ask; the question and answer recorded in the artifact.",
   fails="Asking nobody (Devin pursued infeasible tasks); prompt fatigue when every tool asks; the model's self-rating decides when to ask.",
   kind="ask"),
 dict(id="C9", title="A session outlives its creator",
   new="The session is separated from the device, the authority from the person, and the knowledge from both: a durable log, a service identity with an owner, memory that stays.",
   tags=["quality","speed"], mech="Precondition for M2, M3, M5",
   ex=[("Shopify Aquifer: \"Cells die, sandboxes die, machines die. The conversation doesn't.\"", "first-party"),
       ("Claude Tag: its own service account per channel; revoking it ends access everywhere; tasks \"run after the requester logs off\"", "first-party"),
       ("Block Buzz: a keypair per agent, revoked without touching the human identity", "first-party"),
       ("Microsoft Entra: a business sponsor per agent with succession required; Ramp: standalone agents need an accountable owner", "first-party")],
   cond="A durable session store outside harness and sandbox; a service identity with an admin owner; a named human steward; retention and residency policy; ownership transfer.",
   fails="Orphaned agents; credentials cached in snapshots; tokens outliving a revoked grant; vendor-side retention; a creator-token agent still acting as someone who left.",
   kind="outlive"),
]

MECH = [("M1","No human relay","The session, thread or plan is the handoff object; nobody copies between tools.","speed"),
        ("M2","Idle time works","Triggers start work, parallel by default; the morning report is waiting.","speed"),
        ("M3","Corrections compound","A fix is written where every session reads it, with a curate step.","quality"),
        ("M4","Verification separated","A second context judges against intent; identity stops self-approval.","quality"),
        ("M5","Decisions reach the owner","The accountable person answers one small question with evidence; watchers redirect early.","quality")]
MECH_MAP = {"C1":["M3"],"C2":["M1","M5"],"C3":["M1","M2","M4"],"C4":["M2"],"C5":["M4"],"C6":["M1","M5"],"C7":["M3"],"C8":["M5"],"C9":["M2","M3","M5"]}
CONDS = [("runtime","Cloud runtime"),("durable","Durable session"),("identity","Identity model"),("visibility","Visibility default"),("place","Place to report and ask"),("gate","Gate in code"),("curate","Curate step")]
COND_MAP = {"C1":["durable","curate","visibility"],"C2":["durable","identity","visibility"],"C3":["runtime","durable","identity","gate"],"C4":["runtime","identity","place","gate"],"C5":["durable","identity","gate"],"C6":["visibility","identity","place"],"C7":["durable","curate"],"C8":["durable","place","identity"],"C9":["runtime","durable","identity"]}
CLASSES = [("P5a","per-employee workspace"),("P5b","company agent service"),("P7","background and cloud"),("P8a","public, chat-native"),("P8b","channel-scoped, own identity"),("P8c","private, shared on demand"),("P8d","multiplayer control plane"),("P8e","watch-only run log"),("P8f","shared plan workspace")]
CLASS_MAP = {
 "C1":{"P5a":"Glass edits","P5b":"Kai areas; River skills","P7":"Dreaming","P8a":"River AGENTS.md","P8b":"Claude Tag instructions","P8d":"Inspect review bot"},
 "C2":{"P5a":"Glass share","P7":"Cloud (snapshot)","P8a":"Good thread","P8b":"Claude Tag; Buzz","P8c":"Glass handoff","P8d":"Inspect; Honk v2"},
 "C3":{"P5a":"Glass to Inspect","P5b":"Kai projects (partial)","P7":"Projects; Honk; Minions","P8b":"Buzz roles","P8d":"OCA to Inspect","P8f":"Orbit to Minion"},
 "C4":{"P5a":"Glass automations","P5b":"River automation; AirChat","P7":"Scheduled tasks; ci-weather","P8a":"Security threads","P8b":"Claude Tag routines","P8d":"Inspect automations"},
 "C5":{"P5b":"PR-review profile; Gru","P7":"Code Review; Shrek; Honk judge","P8b":"Buzz reviewer","P8d":"Inspect review bot","P8f":"Harbor comments"},
 "C6":{"P8a":"River; robots channel","P8b":"On-call; Builderbot","P8d":"Inspect in threads","P8e":"Minions channel"},
 "C7":{"P5a":"Laminar debug UI","P5b":"Kai telemetry; Jev","P7":"Intercom SessionEnd","P8a":"Public corpus"},
 "C8":{"P5a":"Cowork asks","P5b":"Kai confirmations","P7":"Minion pauses","P8a":"Smallest question","P8b":"Asks for access","P8d":"Inspect asks"},
 "C9":{"P5a":"Laminar sessions","P5b":"Aquifer; Managed Agents","P8b":"Service identity; keypairs"},
}
AGAINST = [
 ("Noise","Unmeasured for agent sessions. The bot literature: dozens of comments in a row, overload; the fix was digests and a quieter lane.","independent (2021), gap"),
 ("Privacy","\"Some questions just don't get asked\" (River). Privacy zones raised output 10-15% (Bernstein, 2009 factory). Monitoring is stressful in every form (meta-analysis).","first-party, independent"),
 ("Identity","Channel membership is the access boundary (Tenable). Creator tokens by design (Cursor). A planted issue made an agent leak private repos with its user's authority (Invariant).","independent, anecdote"),
 ("Cost","A $1.5M token week preceded metering (Ramp). $15-25 per agent review. Mean $108, median $23, P95 $291 per user per month on one harness (gateway data).","first-party, vendor claim"),
 ("Review burden","98% more PRs, 91% longer review time, no company-level gain (10,000 developers). 45% of merged agent PRs needed revision. \"Slop grenades.\"","vendor telemetry, independent, first-party"),
 ("What fails","Green does not mean success. One-way handoffs. Silent deadlocks. 3 of 20 tasks (Devin). A third of multi-agent failures are misalignment between agents.","first-party, independent"),
]

# ---------------------------------------------------------------- drawing
def person(x,y,c="var(--ink)",s=1.0):
    return f'<circle cx="{x}" cy="{y-9*s}" r="{5*s}" fill="none" stroke="{c}" stroke-width="1.6"/><path d="M{x-8*s} {y+9*s} q{8*s} -14 {16*s} 0" fill="none" stroke="{c}" stroke-width="1.6"/>'
def laptop(x,y,c="var(--ink)"):
    return f'<rect x="{x-14}" y="{y-10}" width="28" height="18" rx="2" fill="none" stroke="{c}" stroke-width="1.6"/><path d="M{x-18} {y+10}h36" stroke="{c}" stroke-width="1.6"/>'
def agent(x,y,c="var(--ink)",fill="var(--paper)"):
    return f'<rect x="{x-9}" y="{y-9}" width="18" height="18" rx="4" fill="{fill}" stroke="{c}" stroke-width="1.6"/><circle cx="{x-3}" cy="{y-1}" r="1.4" fill="{c}"/><circle cx="{x+3}" cy="{y-1}" r="1.4" fill="{c}"/><path d="M{x-4} {y+4}h8" stroke="{c}" stroke-width="1.4"/>'
def card(x,y,w,h,c="var(--ink)",dash=False,fill="var(--paper)"):
    d=' stroke-dasharray="4 3"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{c}" stroke-width="1.6"{d}/>'
def arrow(x1,y1,x2,y2,c="var(--ink)",dash=False):
    d=' stroke-dasharray="4 3"' if dash else ''
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{c}" stroke-width="1.5" fill="none"{d} marker-end="url(#ah)"/>'
def label(x,y,t,c="var(--muted)",anchor="middle",size=10):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{c}" font-family="ui-monospace,SFMono-Regular,Menlo,monospace">{E(t)}</text>'
def clock(x,y,c="var(--ink)"):
    return f'<circle cx="{x}" cy="{y}" r="8" fill="none" stroke="{c}" stroke-width="1.6"/><path d="M{x} {y-5}v5h4" stroke="{c}" stroke-width="1.5" fill="none"/>'
def badge(x,y,c="var(--accent)"):
    return f'<path d="M{x} {y-9} l8 3 v6 q0 7 -8 10 q-8 -3 -8 -10 v-6z" fill="none" stroke="{c}" stroke-width="1.6"/>'
def glass(x,y,c="var(--ink)"):
    return f'<circle cx="{x-2}" cy="{y-2}" r="6" fill="none" stroke="{c}" stroke-width="1.6"/><path d="M{x+2} {y+2}l6 6" stroke="{c}" stroke-width="2"/>'
def lines(x,y,n=3,w=18,c="var(--faint)"):
    return ''.join(f'<path d="M{x} {y+i*5}h{w - (i%2)*6}" stroke="{c}" stroke-width="1.4"/>' for i in range(n))
def bubble(x,y,w,h,c="var(--ink)"):
    return f'<path d="M{x} {y} h{w} v{h} h{-w+10} l-6 6 v-6 h-4z" fill="var(--paper)" stroke="{c}" stroke-width="1.5"/>'

def diagram(kind):
    W,H=480,156
    out=[f'<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="Before and after: desktop versus shared, persistent">',
         '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="var(--ink)"/></marker></defs>',
         f'<path d="M{W//2} 14v{H-28}" stroke="var(--hair)" stroke-width="1" stroke-dasharray="2 4"/>',
         label(16,14,"desktop",anchor="start"), label(W//2+16,14,"shared, persistent",anchor="start")]
    L=112; R=W//2+112
    # left: person at laptop, private session card dashed
    base = person(L-50,78)+laptop(L-50,104)+card(L-14,52,70,46,dash=True)+lines(L-4,66)+label(L+21,116,"private, 30 days")
    out.append(base)
    # right by kind
    if kind=="correction":
        out.append(card(R-60,44,70,46)+lines(R-50,58)+label(R-25,106,"a session"))
        out.append(person(R+50,60,"var(--accent)")+arrow(R+40,70,R+14,70,"var(--accent)")+label(R+50,84,"correction","var(--accent)"))
        out.append(card(R-66,110,164,26,fill="var(--wash)")+label(R+15,127,"shared skills · memory · instructions",size=9.5))
        out.append(arrow(R-25,92,R-25,108)+arrow(R+40,108,R+60,92,dash=True)+label(R+92,70,"next session",size=9.5))
    elif kind=="join":
        out.append(card(R-60,40,130,60)+lines(R-50,54,4)+label(R+5,112,"one session, live"))
        out.append(person(R+95,60)+arrow(R+84,66,R+72,66)+label(R+95,80,"joins"))
        out.append(person(R-80,60,"var(--accent)")+arrow(R-68,66,R-62,66,"var(--accent)")+label(R-80,80,"redirect","var(--accent)"))
        out.append(agent(R+40,84))
    elif kind=="handoff":
        out.append(card(R-70,40,60,40)+label(R-40,55,"plan",size=11)+lines(R-62,62,2,40))
        out.append(arrow(R-8,60,R+10,60)+agent(R+22,60)+arrow(R+34,60,R+52,60)+agent(R+64,46,fill="var(--wash)")+agent(R+64,74,fill="var(--wash)"))
        out.append(label(R+64,96,"parallel runs")+person(R-40,110,"var(--accent)")+label(R-40,128,"reviews the plan","var(--accent)"))
        out.append(arrow(R-40,88,R-40,84,"var(--accent)"))
    elif kind=="overnight":
        out.append(clock(R-60,56)+label(R-60,78,"trigger"))
        out.append(arrow(R-48,56,R-30,56)+agent(R-18,56)+arrow(R-6,56,R+20,56))
        out.append(card(R+22,40,90,34)+lines(R+32,54,2,70)+label(R+67,88,"morning report"))
        out.append(person(R+67,118,"var(--accent)")+label(R+67,140,"a person decides","var(--accent)")+arrow(R+67,78,R+67,100,"var(--accent)"))
    elif kind=="reviewer":
        out.append(card(R-70,44,70,46)+lines(R-60,58)+label(R-35,106,"shared artifact",size=9.5))
        out.append(agent(R-90,44,fill="var(--wash)")+arrow(R-78,52,R-72,56)+label(R-90,30,"author"))
        out.append(glass(R+40,58)+agent(R+40,86,fill="var(--wash)")+label(R+40,110,"fresh context",size=9.5)+arrow(R+22,66,R+2,66,dash=True))
        out.append(person(R+100,66,"var(--accent)")+label(R+100,88,"approves","var(--accent)",size=9.5)+arrow(R+74,74,R+88,72,"var(--accent)",dash=True))
    elif kind=="watch":
        out.append(bubble(R-70,36,150,50)+lines(R-60,50,4,120)+agent(R+62,76))
        for i,x in enumerate([R-70,R-40,R-10,R+20,R+50,R+80]):
            out.append(person(x,120,"var(--accent)" if i==2 else "var(--ink)",0.85))
        out.append(arrow(R-10,104,R-10,92,"var(--accent)")+label(R+5,138,"watch · redirect · learn"))
    elif kind=="traces":
        for i in range(4):
            out.append(card(R-70+i*8,40+i*6,80,34,fill="var(--paper)"))
        out.append(lines(R-50,60,3,50)+label(R-14,100,"sessions, retained"))
        out.append(arrow(R+34,60,R+56,60)+person(R+70,60)+label(R+70,78,"platform team"))
        out.append(card(R+40,96,70,30,fill="var(--wash)")+label(R+75,114,"fix the harness")+arrow(R+70,72,R+70,94))
    elif kind=="ask":
        out.append(card(R-70,44,70,46)+agent(R-35,60)+label(R-35,106,"session waits"))
        out.append(bubble(R+10,44,80,26)+label(R+50,61,"one question",size=10)+arrow(R-5,60,R+8,60))
        out.append(person(R+104,66,"var(--accent)")+label(R+104,86,"owner","var(--accent)"))
        out.append(arrow(R+94,90,R-10,104,"var(--accent)",dash=True)+label(R+40,128,"answer with evidence","var(--accent)"))
    elif kind=="outlive":
        out.append(card(R-70,44,120,46)+lines(R-60,58,3,90)+label(R-10,106,"durable session log"))
        out.append(badge(R+70,62)+label(R+70,86,"own identity","var(--accent)"))
        out.append(person(R-92,60)+arrow(R-84,66,R-74,66)+label(R-92,80,"creator"))
        out.append(f'<path d="M{R-104} 90 l24 -42" stroke="var(--accent)" stroke-width="1.4"/>'+label(R-92,96,"leaves","var(--accent)",size=9.5))
        out.append(person(R+100,122,"var(--accent)")+label(R+100,142,"steward","var(--accent)")+arrow(R+90,112,R+76,82,"var(--accent)",dash=True))
    out.append('</svg>')
    return ''.join(out)

# ---------------------------------------------------------------- page
CSS = """
:root{--paper:#f6f4ee;--ink:#1d2229;--muted:#596069;--faint:#9aa1a9;--hair:#d9d5cc;--wash:#ebe7dd;--accent:#b4570f;--accentwash:#f3e3d2;--good:#2d6a4f}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--paper:#15181c;--ink:#e6e3dc;--muted:#a9adb3;--faint:#6b7077;--hair:#2c3138;--wash:#1f2429;--accent:#e58a3c;--accentwash:#3a2718;--good:#7fc8a9}}
:root[data-theme=dark]{--paper:#15181c;--ink:#e6e3dc;--muted:#a9adb3;--faint:#6b7077;--hair:#2c3138;--wash:#1f2429;--accent:#e58a3c;--accentwash:#3a2718;--good:#7fc8a9}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 Georgia,'Iowan Old Style','Times New Roman',serif;padding:0 16px 64px}
main{max-width:1180px;margin:0 auto}
h1,h2,h3{font-weight:600;letter-spacing:-.01em;line-height:1.2}
h1{font-size:30px;margin:40px 0 6px}h2{font-size:22px;margin:48px 0 10px;padding-top:16px;border-top:1px solid var(--hair)}h3{font-size:17px;margin:0 0 6px}
.lede{color:var(--muted);max-width:72ch;margin:0 0 8px}
.mono{font:12px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted)}
.tag{display:inline-block;font:11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;padding:4px 7px;border:1px solid var(--hair);border-radius:4px;color:var(--muted);margin-right:4px;white-space:nowrap}
.tag.speed{border-color:var(--ink);color:var(--ink)}.tag.quality{border-color:var(--accent);color:var(--accent)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(340px,1fr));gap:18px}
.card{border:1px solid var(--hair);border-radius:10px;padding:16px 18px;background:var(--paper)}
.card .id{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--accent);margin-bottom:4px}
.card p{margin:8px 0;font-size:14.5px}
.card ul{margin:6px 0 0;padding-left:18px;font-size:13.5px}.card li{margin:4px 0}
.card .lbl{font:11px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted)}
.kv{font-size:13.5px;margin:8px 0 0}.kv b{font-weight:600}
.props{width:100%;min-width:640px;border-collapse:collapse;font-size:14px;margin-top:12px}
.props th,.props td{text-align:left;vertical-align:top;padding:10px 10px;border-top:1px solid var(--hair)}
.props th{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted);font-weight:500}
.props td:nth-child(2){color:var(--muted)}.props td:nth-child(3){background:var(--wash)}
.wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
.map{border-collapse:collapse;font-size:13px;min-width:720px}
.map th,.map td{border:1px solid var(--hair);padding:7px 8px;vertical-align:top;text-align:left}
.map th{font:12px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted);font-weight:500;background:var(--paper);position:sticky;top:0}
.map td.on{background:var(--accentwash);color:var(--ink)}.map td.c{text-align:center}
.map td.dot::before{content:"●";color:var(--accent)}
.map tr td:first-child{white-space:nowrap;font-weight:600}
.against{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.against .card{border-left:3px solid var(--accent)}
.mech{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}
.mech .card{padding:12px 14px}.mech .card h3{font-size:15px}
.note{font-size:13.5px;color:var(--muted);max-width:80ch}
a{color:inherit}
.legend{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:8px 0 0}
svg text{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
@media (max-width:600px){h1{font-size:24px}.grid{grid-template-columns:1fr}}
"""

def page():
    h=[]
    h.append('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Shared agent interactions</title>')
    h.append(f'<style>{CSS}</style></head><body><main>')
    h.append('<h1>What shared, persistent agents make possible</h1>')
    h.append('<p class="lede">Nine agent-to-human and agent-to-agent interactions that appear once an agent no longer lives on one person\'s desktop, each drawn as a before and after, with the mechanism that drives speed or quality, the evidence and its type, the conditions it needs, and what fails. From the task <a href="01-synthesis.md">synthesis</a> (2026-10-26); every company figure is the company\'s own unless marked independent.</p>')
    h.append('<p class="mono">Labels: first-party (the company about its own system) · vendor claim · independent · anecdote. The accent colour marks where a person decides or is reached.</p>')

    # before/after properties
    h.append('<h2>Before and after: four properties and who decides them</h2>')
    h.append('<p class="lede">"Shared and persistent" is a bundle. The teardowns show every combination shipping: Stripe Kai is persistent but private and single-user; Ramp Glass is private by default and shared on demand; Shopify River is public by default and multiplayer; Claude Tag is channel-scoped with its own identity.</p>')
    h.append('<div class="wrap"><table class="props"><thead><tr><th>Property</th><th>Desktop default</th><th>Shared, persistent designs</th><th>Who decides</th></tr></thead><tbody>')
    for p in PROPS: h.append('<tr>'+''.join(f'<td>{E(x)}</td>' for x in p)+'</tr>')
    h.append('</tbody></table></div>')

    # interactions
    h.append('<h2>The nine interactions</h2>')
    h.append('<div class="grid">')
    for it in INTER:
        h.append('<article class="card">')
        h.append(f'<div class="id">{it["id"]} · {E(it["mech"])}</div><h3>{E(it["title"])}</h3>')
        h.append(diagram(it["kind"]))
        h.append('<div class="legend">'+''.join(f'<span class="tag {t}">{t}</span>' for t in it["tags"])+'</div>')
        h.append(f'<p><b>What is new.</b> {E(it["new"])}</p>')
        h.append('<p class="lbl">Evidence</p><ul>'+''.join(f'<li>{E(t)} <span class="lbl">({E(l)})</span></li>' for t,l in it["ex"])+'</ul>')
        h.append(f'<p class="kv"><b>Needs:</b> {E(it["cond"])}</p>')
        h.append(f'<p class="kv"><b>What fails:</b> {E(it["fails"])}</p>')
        h.append('</article>')
    h.append('</div>')

    # mechanisms
    h.append('<h2>Five mechanisms behind the nine</h2>')
    h.append('<div class="mech">')
    for m,name,desc,kind in MECH:
        h.append(f'<div class="card"><div class="id">{m} · <span class="tag {kind}">{kind}</span></div><h3>{E(name)}</h3><p>{E(desc)}</p></div>')
    h.append('</div>')
    h.append('<p class="note">Judgment: the speed mechanisms (M1, M2) have the most first-party volume evidence and no independent confirmation; the quality mechanisms (M3, M4, M5) have the one independent experiment (a verification step gave +15.6% task success across 1,642 multi-agent traces) and the most contested first-party number (the merge rate).</p>')

    # interaction map
    h.append('<h2>Interaction map: mechanisms and conditions</h2>')
    h.append('<div class="wrap"><table class="map"><thead><tr><th>Interaction</th>'+''.join(f'<th>{m}<br>{E(n)}</th>' for m,n,_,_ in MECH)+''.join(f'<th>{E(n)}</th>' for _,n in CONDS)+'</tr></thead><tbody>')
    for it in INTER:
        h.append(f'<tr><td>{it["id"]} {E(it["title"])}</td>')
        for m,_,_,_ in MECH: h.append('<td class="c dot"></td>' if m in MECH_MAP[it["id"]] else '<td class="c"></td>')
        for k,_ in CONDS: h.append('<td class="c on">needs</td>' if k in COND_MAP[it["id"]] else '<td class="c"></td>')
        h.append('</tr>')
    h.append('</tbody></table></div>')
    h.append('<p class="note">Conditions: a cloud runtime (not a laptop); a durable session outside harness and sandbox; an identity model decided before launch; a visibility default with a deliberate path to private; a place where the agent reports and asks; a human gate on the side effect enforced in code; a curate step on anything that compounds.</p>')

    # pattern classes
    h.append('<h2>Where each interaction has been seen, by pattern class</h2>')
    h.append('<p class="lede">Classes from the taxonomy\'s B.2 as revised by the teardown mapping. A cell names the example; blank means none found. P8a and P8b carry the most, because a chat channel supplies visibility, memory, identity and a place to ask at once.</p>')
    h.append('<div class="wrap"><table class="map"><thead><tr><th>Interaction</th>'+''.join(f'<th>{c}<br>{E(n)}</th>' for c,n in CLASSES)+'</tr></thead><tbody>')
    for it in INTER:
        h.append(f'<tr><td>{it["id"]}</td>')
        for c,_ in CLASSES:
            v=CLASS_MAP[it["id"]].get(c)
            h.append(f'<td class="on">{E(v)}</td>' if v else '<td></td>')
        h.append('</tr>')
    h.append('</tbody></table></div>')

    # against
    h.append('<h2>The evidence against</h2>')
    h.append('<div class="against">')
    for t,d,l in AGAINST: h.append(f'<div class="card"><h3>{E(t)}</h3><p>{E(d)}</p><p class="lbl">{E(l)}</p></div>')
    h.append('</div>')
    h.append('<p class="note">Nobody has published a like-for-like comparison of shared versus private agents on time to resolve, defect rate, cost or retention. The only multiplayer metric is Shopify\'s same-thread links (61,680 in March 2026 to 171,853 in September), which is volume, not outcome.</p>')

    h.append('<h2>Sources and method</h2>')
    h.append('<p class="note">Built from the teardown sources already in the project library (Ramp, Shopify, Stripe, Anthropic, Spotify, Block, Intercom, Airbnb) plus 19 source notes from targeted gap research. Every claim on this page links, through the synthesis, to a source note in <code>research/sources/</code> with its evidence label. Options and key questions are in <code>options/contributions/research-shared-persistent-agents.md</code>. Generated by <code>02-interactions.build.py</code>; no scripts, no web fonts.</p>')
    h.append('</main></body></html>')
    return ''.join(h)

open("02-interactions.html","w").write(page())
print("wrote 02-interactions.html")
