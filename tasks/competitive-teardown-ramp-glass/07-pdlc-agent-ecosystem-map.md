# Ramp's agent ecosystem, mapped to the tasks of the product lifecycle

Date: 2026-10-24. Built in the same frame as the [Stripe map](../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md) so the two compare side by side. Built only from filed source notes in `../../research/sources/`. Each handoff is marked **documented** (a Ramp source says it happens), **inferred** (consistent with the sources but not stated) or **unknown**. Every figure is Ramp's own (first-party); none has been checked outside Ramp. Visual version: [07-pdlc-agent-ecosystem-map.html](07-pdlc-agent-ecosystem-map.html).

## Why tasks, not job titles (the Ramp version)

At Ramp, too, tasks cross job families:
- **Non-engineers write code.** About 1,000 Inspect PRs in a month came from non-engineers ([Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md)). Non-engineers are 12% of human-initiated PRs ([Charles, April](../../research/sources/x-geoffintech-ai-pilled-article.md)). Inspect has a Chrome extension so they can point at UI ([Inspect post](../../research/sources/ramp-builders-why-we-built-background-agent.md)).
- **PMs prototype in the product.** Glass "understands our design system ... code base", so a PM can "build a prototype that actually works within your product" ([Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md)).
- **Account managers run research and customer follow-up through saved prompts** ([Glyman](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md)).

So each row is a task, and "who" lists the roles the sources show doing it.

## The short answer: where context breaks between research, intent and plan

1. **Ramp names the hand-off but not its mechanism.** Charles describes what the define stage hands to engineering: qualitative and quantitative data, "the actual requirements that they can use for their coding agents, and a prototype". He calls it "the next contract". No source shows how that bundle gets from a PM's Glass session into an engineer's Inspect session, or what format it takes. Research → intent → plan → code across people is therefore **documented as a goal, unknown as a mechanism**.
2. **Where Ramp does carry context across people, it carries the session itself.** Glass sessions can be shared ("She shares her Glass session. The engineer jumps in, sees everything") and every Inspect session is multiplayer, with prompts attributed per person ([Glyman](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md); [Inspect post](../../research/sources/ramp-builders-why-we-built-background-agent.md)). Glass, Inspect and Ramp Research are connected tools in one workspace ([Goddijn](../../research/sources/x-sebgoddijn-glass-article.md)), and since October all run on one harness, Laminar ([Laminar post](../../research/sources/ramp-builders-building-laminar.md)). That is the opposite of Stripe, whose research agent (Kai) is single-user by its own account.
3. **For small work, Ramp removes the people boundary.** For "most small things", an agent runs the whole loop: routing, matching to the Linear backlog, dedupe, ranking, planning, a Slack check ("is this ready to go?"), code, CI and the knowledge base. "60% of UX issues ... are fixed within 24 hours" ([Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md)).
4. **The unrecorded steps are at the top of the chain.** No source names a tool for *setting the goal*, or for planning a large change as a separate step. Charles places planning inside Glass ("AI is your tech lead") and inside the small loops. There is no Orbit-like planning agent in the record.

**Compared with Stripe.** Stripe's gap is between research and planning agents (Kai → Orbit), which one person often bridges. Ramp's tooling has fewer gaps: one workspace, shared sessions, one harness. But its public record leaves open the same seam in a different place: the *contract* from a define-stage session to a build-stage session when different people own them.

## The lifecycle, task by task

Rows follow the Stripe map. One row is split where Ramp truly differs: **Test** is its own row, because Ramp has a dedicated QA agent (Testo) between review and release. Charles's factory stages (identify, define, build, review, test, coordinate, improve) map onto these rows as noted.

| Task | Who does it at Ramp (roles seen) | Agents and tools | Artifact produced | Evidence |
|---|---|---|---|---|
| **Spot the opportunity** (Charles: *identify*) | PMs, leaders; anyone reading the insight feeds | **Customer insight agent**: ETL, vector search and clustering over Gong, Zendesk, LogRocket and surveys; Slack agent, HTML dashboard, a daily "hate" channel and podcast | Clustered, traceable insight; daily digest | [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party) |
| **Talk to customers** | Account managers, sales, PMs (told "which customers to talk to") | **Glass** saved prompt pulls feature requests from calls (≈300 → ≈20,000 a month); earlier, Notion custom agents triaged sales feedback to the roadmap | Feature-request records (formerly typed into Salesforce); prioritised list | [Glyman](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md), [Atiyeh](../../research/sources/x-karimatiyeh-glass-feature-requests.md) (vendor claim); [Notion video](../../research/sources/notion-inside-ramps-custom-agent-os.md) (vendor claim) |
| **Research the problem, read the data** | Anyone: sales, ops, finance, PMs, engineers | **Ramp Research** (Slack data agent: 1,476 questions in four weeks vs 66 in the human help channel); **Glass** with Snowflake and research connected; **Gadget** answers "ask the org" questions | Threaded Slack answers with CSV previews; Glass sessions | [Ramp Research](../../research/sources/ramp-builders-meet-ramp-research.md); [Goddijn](../../research/sources/x-sebgoddijn-glass-article.md); [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party) |
| **Set the goal** | People (not shown) | None named; Glass "understands our product strategy" | Not described | [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) |
| **Shape the intent: spec, prototype** (Charles: *define*) | PMs; others with Glass | **Glass** as the define-stage agent: connected to Snowflake, user research, strategy, spec conventions, design system and code base; "AI is your tech lead" | "The next contract": data, requirements for coding agents, a working prototype | [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party) |
| **Plan the change** | Not shown as a separate task; inside Glass (PM) or the small loops (agent, with Slack sign-off) | No named planning agent; Inspect can spawn sub-sessions for research across repos | Not described as a separate artifact | [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md); [Inspect post](../../research/sources/ramp-builders-why-we-built-background-agent.md) |
| **Write the code** (Charles: *build*) | Agents, started by engineers and non-engineers from Slack, web, Chrome extension, PR comments | **Inspect** (≈30% of merged PRs in Jan, >50% in Mar, "75%" in Sept; 1M sessions); Glass builds Glass's own code | Branch and PR opened under the requester's identity | [Inspect post](../../research/sources/ramp-builders-why-we-built-background-agent.md); [Pragmatic Summit](../../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md); [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md); [Buchan](../../research/sources/x-shanebuchan-how-we-built-glass.md) |
| **Review the change** | A human reviewer the agent picks; senior engineers on the hard 7% | **Review Buddy**: knows the codebase, quality and security checks, and "all the prompts that led you to build that code"; "93% of our PRs" handled | Reviewed PR | [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party) |
| **Test** *(Ramp split)* | Agents; PMs give instructions ("pay an invoice, but amortize it") | **Testo**: browser QA agent; runs the product in "100 different combinations" from production data; 425 bugs in 30 days | Bug and design-quality feedback "back through the loop" | [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party) |
| **Release** (Charles: *coordinate*) | PMs; Gadget | Deploy mechanism not described. **Gadget** writes help-center articles, blog posts and customer emails, updates the roadmap, pings late owners; Glass prompt emails customers when their request ships (5,000+) | Launch content; roadmap and status updates | [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md); [Glyman](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md) |
| **Operate and learn** (Charles: *improve*) | On-call engineers, support, ops; agents for small loops | **OCA** (incidents: 575 of 1,220 fix PRs assisted in four weeks); small-loop agents (feedback → backlog → code → knowledge base); Glass issue channel triaged to tickets automatically; Ramp Research in alert channels | Incident reports, fix PRs, tickets, knowledge-base updates | [OCA post](../../research/sources/ramp-builders-how-we-built-oca.md); [Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md); [Goddijn](../../research/sources/x-sebgoddijn-glass-article.md); [Ramp Research](../../research/sources/ramp-builders-meet-ramp-research.md) |

**Across all tasks:** one harness since October (Laminar) under Glass, Inspect, Stack and customer-facing agents ([Laminar post](../../research/sources/ramp-builders-building-laminar.md)). A shared tool catalog of "many hundreds" of tools ([Pragmatic Summit](../../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md)). Ramp Router as the LLM gateway. Dojo skills (350+) and Glass memory refreshed every 24 hours from Slack, Notion and Calendar ([Goddijn](../../research/sources/x-sebgoddijn-glass-article.md)). Notion, Linear and Slack as the "formal record" that Gadget reads ([Charles](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md)).

**Outside the lifecycle:** Policy Agent and the other customer-facing agents are products the factory ships, not steps in it. They supply Ramp's trust pattern: suggestions first, an autonomy slider, an "unsure" outcome, and cited reasoning ([trust post](../../research/sources/ramp-builders-agents-users-can-trust.md)).

## Every handoff, task to task

| # | From task (agent) → to task (agent) | Mechanism | Status |
|---|---|---|---|
| 1 | Spot the opportunity (insight agent) → talk to customers | Insight is "traceable", so a PM can "identify exactly which customers to talk to"; delivered via Slack agent, dashboard, podcast | **documented** |
| 2 | Talk to customers (calls) → feature-request records (Glass) | A saved Glass prompt pulls requests from call recordings | **documented** |
| 3 | Feature requests → prioritised list → customer email on ship | Two more saved prompts; how "shipped" is detected is not described | **documented** (sequence); mechanism of the ship trigger **unknown** |
| 4 | Research (Ramp Research) → scoping new features | Teams add Ramp Research to "project channels to scope out new features" | **documented** |
| 5 | Research (Ramp Research, Snowflake) → shape intent (Glass) | Ramp Research and Snowflake are connected tools in every Glass install; whether a research thread's answers are carried into a define session is not shown | **inferred** |
| 6 | Set the goal → shape intent | Not described | **unknown** |
| 7 | **Shape intent (Glass, PM) → plan and write code (Inspect, engineer)** | "The next contract" (data, requirements, prototype) is named; how it travels from one session or person to the other is not | **unknown** (mechanism); the contract's contents **documented** |
| 8 | Shape intent → plan the change | Inside Glass ("AI is your tech lead"); no separate planning artifact | **inferred** |
| 9 | Any Slack thread, PR comment, Chrome selection or web prompt → write code (Inspect) | Slack app with a repository classifier; extension sends the React element tree; PR discussion; state synced across clients | **documented** |
| 10 | One person's session → another person (Glass, Inspect) | Share the Glass session; Inspect sessions are multiplayer with attributed prompts | **documented** |
| 11 | Write code (Inspect) → review (Review Buddy, human) | PR opened under the requester's identity; Review Buddy reads the code and the prompts behind it, and picks the human reviewer | **documented** |
| 12 | Write code / review → test (Testo) → back to code | Testo runs on production-shaped data; feedback "back through the loop to fix" (how it is routed not described) | **documented** (sequence); routing **unknown** |
| 13 | Review / test → release | Deploy and rollout mechanism not described in any source | **unknown** |
| 14 | Release → launch content and the record (Gadget) | Gadget reads Notion, Linear, Slack and tickets; writes help-center, blog, customer email; updates the roadmap | **documented** |
| 15 | Operate: incident (incident.io Slack channel) → OCA → write code (Inspect) → human merge | OCA joins the channel, reports at ~5 and ~13 minutes, asks Inspect for a PR; nothing merges without a human | **documented** |
| 16 | Operate: user feedback → backlog → plan → code → CI → knowledge base (small loops) | Agent routes, matches to Linear, dedupes, ranks, plans, asks in Slack, codes, runs CI, updates the KB | **documented** (sequence); each link's mechanism **unknown** |
| 17 | Operate: Glass issue reports → tickets | A Slack channel where "our team triages them into tickets automatically" | **documented** |
| 18 | Everyday work (Slack, Notion, Calendar, past sessions) → every Glass session | 24-hour memory pipeline writes files read at session start | **documented** (April design; not re-described in October) |
| 19 | One person's workflow → everyone (Dojo skills, knowledge edits) | Publish creates a reviewed Git change; 323 people made 6,500+ edits to what Glass knows | **documented** |

**Counts:** 19 handoffs.
- **Documented, mechanism included:** 11 (1, 2, 4, 9, 10, 11, 14, 15, 17, 18, 19).
- **Documented sequence, one link's mechanism unknown:** 3 (3, 12, 16).
- **Inferred:** 2 (5, 8).
- **Unknown:** 3 (6, 7, 13).

## Diagram (text)

```
TASK:     Spot        Talk to      Research    Set    Shape intent   Plan      Write     Review      Test     Release    Operate
          opportunity customers    problem     goal   (define)       change    code                                    & learn
HUMANS    PMs,leaders AMs, sales   anyone      ●?     PMs            (in Glass) eng+non-eng picked rev. PM instr.  PMs   on-call
AGENTS    insight ──► Glass prompts Ramp Research ·    Glass ═ ═ ? ═ ═ ═ ═ ═ ═ ► Inspect ─► Review Buddy ─► Testo  Gadget   OCA ─► Inspect
           agent      (300→20k)    Gadget                                        ▲ Slack/web/ext/PR                         small loops
SHARED    Laminar harness · Ramp Router · tool catalog · Dojo skills · Glass memory (24 h) · shared/multiplayer sessions · Notion/Linear/Slack record
          ═ ? ═  define → build "contract" (data, requirements, prototype): contents named, transport not described
```

## What it means for our options

- **Ramp's answer to "context across people" is the shared session, not a handoff artifact.** That is evidence for the shared and multiplayer option in [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff). It also leaves open what happens when the next person needs a durable, reviewable artifact rather than a live session.
- **The define → build contract is named but unspecified.** Ramp's three-part contract (evidence, requirements for coding agents, working prototype) is a concrete candidate for [intent-shaping-and-spec](../../options/DIMENSIONS.md#intent-shaping-and-spec-intent-shaping-mode-and-spec-standard). Its format is the open question.
- **Stage agents, one harness.** Ramp maps one agent to each stage (insight, Glass, Inspect, Review Buddy, Testo, Gadget, OCA), all on Laminar. That favours the stage-agent unit with a common substrate (see [work-structure / agent-unit](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent)).
- **Small work skips the people boundary entirely.** Autonomous small loops (60% of UX issues fixed in 24 hours, self-reported) suggest a split policy: agent-run loops for small changes, human-shaped intent for large ones. Compare [review-and-autonomy](../../options/DIMENSIONS.md#review-and-autonomy-review-and-autonomy).

Key questions:
1. When a PM finishes a Glass define session and an engineer starts an Inspect session, what exactly moves between them: a shared session link, a Linear ticket, a document, a prototype PR? — *answered by:* Ramp's Glass or Inspect team; a demo of one feature from define to merge.
2. How large is the work that small loops take end to end, and where does Ramp draw the line to human-shaped intent? — *answered by:* Ramp; our own classification of changes by size.

## Could not verify

- Every figure is Ramp's own. Charles's factory numbers (75% of PRs, 93% reviewed, 425 bugs, 85% of questions, 60% in 24 hours) come from one talk, with no method given.
- Inspect's share of PRs rose over the year: ≈30% (Jan), >50% (Mar), 75% (Sept). The figures are from different speakers and may not use the same denominator.
- Review Buddy, Testo, Gadget and the customer-insight agent are described only in Charles's talk; there are no engineering posts on them.
- No source describes Ramp's deploy and rollout step.
- The Glass memory design is from April 2026. Whether it changed when Glass moved to Laminar is not stated.
