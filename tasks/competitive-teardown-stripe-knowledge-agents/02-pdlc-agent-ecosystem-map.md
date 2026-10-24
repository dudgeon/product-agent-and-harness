# Stripe's agent ecosystem, mapped to the tasks of the product lifecycle

Date: 2026-10-24 (v2, re-anchored on tasks at Geoff's request). Worker draft (task competitive-teardown-stripe-knowledge-agents). Built only from the filed source notes in `../../research/sources/`. Each handoff is marked **documented** (a Stripe source says it happens), **inferred** (consistent with the sources but not stated) or **unknown**. Visual version: [Stripe Agent Lifecycle Map](https://claude.ai/artifact/CqRTGU5Dy5Wqz3kAwdbw2n).

## Why this map is anchored on tasks, not job families

At Stripe, tasks that are historically a PM's are routinely done by engineers, and the reverse:
- **Engineers do product tasks.** Stripe "didn't have the PM role for a long time". Engineers take part in "figuring out business scope, talking to users, collaborating with designers"; Stripe "still expects engineers to be close to users" ([Pragmatic Engineer](../../research/sources/pragmaticengineer-inside-stripe-engineering-culture-part-2.md), independent, Jan 2024).
- **An engineer explains the chain.** In the Orbit video, an engineer draws the whole chain, opportunity to plan, and an engineer states the intent Orbit plans from ([video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md)).
- **PMs and others do design and engineering tasks.**
  - A PM who is a former engineer built a prototype CLI and revised it between UXR sessions ([video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md)).
  - PMs are now the largest group of Protodash users ([Protodash](../../research/sources/howiai-stripe-protodash-owen-williams.md)).
  - Finance staff and account executives build Harbor prototypes ([Harbor](../../research/sources/stripe-harbor-ai-prototyping.md)).
  - A PM brief or design feedback "is in effect just writing a prompt" for a minion ([Kaliski](../../research/sources/howiai-stripe-minions-kaliski.md)).

So each row below is a **task**, and "who does it" lists the roles the sources show doing it.

## The short answer on Kai → Orbit

**No public source describes a direct handoff from Kai to Orbit.** In task terms, that is the handoff from *researching the problem* to *planning the change*.

1. **Kai's context is locked in single-user sessions.** Stripe lists sharing across sessions as roadmap: "Users generate a lot of context in their Kai sessions that is currently 'locked in'" ([Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md), first-party, Jul 2026).
2. **Orbit starts from intent that a person types.** In the demo, an engineer types a research question; Orbit reads the codebase and Trailhead, then drafts a plan ([video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md)). Orbit targets engineers first.
3. **What bridges the two is people, plus shared tools and documents.** Kai, Orbit, Minions and Harbor all reach Toolshed (~500 MCP tools, used by "hundreds of different agents") and the same documents, Slack threads and tickets ([Minions part 2](../../research/sources/stripe-minions-part-2.md); [part 1](../../research/sources/stripe-minions-one-shot-coding-agents.md)).

**What the task view changes.** Because one person at Stripe often does both tasks, the missing agent link may cost little there: the context travels in that person's head and in the docs they share. The gap bites when the tasks are split across people (a PM researches, an engineer plans), which is the norm in most of our target orgs. That makes "research → intent → plan, carried across people" the seam to fund, whatever the job titles.

## The lifecycle, task by task

The rows follow Stripe's whiteboard chain (Opportunity → Problem → Goal → Intent → Plan, then Code; [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) at about 12:24), broken into tasks and extended with review, release and operate.

| Task | Who does it at Stripe (roles seen) | Agents and tools | Artifact produced | Evidence |
|---|---|---|---|---|
| **Spot the opportunity** | Leaders, PMs, engineers wearing the "product hat" | None named | Not described | [Pragmatic Engineer](../../research/sources/pragmaticengineer-inside-stripe-engineering-culture-part-2.md) |
| **Talk to customers** | Engineers ("close to users"), PMs, researchers; account executives with accounts | People. Kai does account research before calls | Not shown (the board's brace: "customer conversations") | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md); [Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md) |
| **Research the problem, read the data** | Anyone: sales, finance, ops, engineers, PMs | **Kai**: data analysis (5,000+ sessions a day), docs and email digests; "ask data" over Hubble | Kai dashboards, reports, docs (single-user) | [Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md); [Krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md) |
| **Set the goal** | People (not shown in any tool) | None named | Not described | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) |
| **Shape the intent: prototype, spec** | Designers, PMs (now more than designers in Protodash), engineers, finance, account executives | **Harbor** (12,000 prototypes); **Protodash**; Google Docs PRDs; agent-drafted specs reviewed as GitHub issues | Prototype URL with anchored comments; PRD; spec issue | [Harbor](../../research/sources/stripe-harbor-ai-prototyping.md); [Protodash](../../research/sources/howiai-stripe-protodash-owen-williams.md); [SDK post](../../research/sources/stripe-ai-didnt-write-our-sdk.md) |
| **Plan the change** | Engineers first; teammates comment | **Orbit**: reads code and Trailhead; "Workspaces share context across sessions" | Shareable, commented plan | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) |
| **Write the code** | Agents, started by engineers and increasingly by non-engineers from Slack | **Minions** (~1,300 PRs a week); Claude Code, Cursor; the payment-method factory | Branch and pull request | [part 1](../../research/sources/stripe-minions-one-shot-coding-agents.md), [part 2](../../research/sources/stripe-minions-part-2.md); [Kaliski](../../research/sources/howiai-stripe-minions-kaliski.md); [factory](../../research/sources/stripe-payment-method-factory.md) |
| **Review the change** | A person on every PR, plus an agent | **Gru**; CI capped at two rounds | Approved PR | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md); [part 2](../../research/sources/stripe-minions-part-2.md) |
| **Release** | Automated | 1% canary, auto-pause and rollback | Live change | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) |
| **Operate and learn** | Ops, finance, compliance analysts, engineers | **Kai** (incident triage, digests); **compliance agents** (100+ on the agent service); factory learning logs; Kai skill reflection (roadmap) | Answers, digests, improved prompts and skills | [Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md); [AWS](../../research/sources/aws-stripe-compliance-agents.md); [factory](../../research/sources/stripe-payment-method-factory.md) |

## Every handoff, task to task

| From task (agent) → to task (agent) | Mechanism | Status |
|---|---|---|
| Research (Kai) → shape intent (Harbor) | Harbor's tools over internal MCP; its renderer is a service Kai uses. Example: a stripe.com analysis in Kai became a clickable prototype | **documented** ([Harbor](../../research/sources/stripe-harbor-ai-prototyping.md)) |
| Shape intent (Harbor, Protodash) → write code (coding agents) | Coding agents pull a prototype's file tree into a repo; a Protodash prototype PR became an engineer's source of truth | **documented** |
| Any task's thread, doc or ticket → write code (Minions) | Emoji reaction or tagging the app; the thread is the prompt; links hydrated over MCP; the docs, feature-flag and ticketing tools can launch minions | **documented** |
| Plan (Orbit) → write code (Minions) | One button: devbox, plan and instructions; up to 12 hours; pauses to ask | **documented** |
| Shared docs (Trailhead) → plan, code | Orbit and minions read internal docs | **documented** |
| Research (Kai) → other agents | Kai "invoke[s] more specialized agents and skills" | **documented**, mechanism unknown |
| **Research (Kai) → plan (Orbit)** | Not described. If one person does both, the context is in their head and their docs. If two people, it goes via shared docs, Slack or prototypes | **unknown** |
| Talk to customers / set goal → shape intent | People; not in any tool shown | **inferred** |
| Operate and learn → shared knowledge | Factory learning and decision logs update prompts; Kai skill reflection is roadmap | **documented** / roadmap |

## Diagram (text)

```
TASK:        Spot      Talk to     Research   Set     Shape intent   Plan     Write   Review   Release  Operate
             opportunity customers  problem    goal    (prototype)    change   code    change            & learn
HUMANS       ●(any role) ●(any role)  ●          ●       ●               ●(eng-first) ·    ●(every PR)        ●
AGENTS                               Kai ──────────────► Harbor ──────► Orbit ──► Minions ─► Gru ─► 1% canary  Kai, compliance
                                      └ - - - - - ? - - - - - - - - - - ┘ (Kai → Orbit not documented)
SHARED       Toolshed (~500 MCP tools) · Trailhead (owner-verified docs) · devboxes · Compass · Slack · Google Docs · tickets
```

## What it means for our options

- **Map agents to tasks, then let roles vary.** Stripe's own record shows a single agent per task (Kai for research, Harbor for prototypes, Orbit for plans, Minions for code), used by whoever does the task. That is evidence for the "job agent" or "stage agent" unit over a "persona agent" (see [work-structure / agent-unit](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent)).
- **The seam to fund is research → intent → plan when those tasks sit with different people.** At Stripe one person often does all three. In orgs with a firmer PM/engineering split, the missing Kai → Orbit link becomes a real handoff cost. Options that carry shaped intent, with its evidence, into planning address it ([intent-shaping-and-spec](../../options/DIMENSIONS.md#intent-shaping-and-spec-intent-shaping-mode-and-spec-standard); story S05).
- **Single-user sessions are the blocker Stripe names itself.** Kai's roadmap item matches our [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff) choice. Orbit's shared workspaces suggest Stripe solved it first for planning.
- **Agents connect through a shared tool layer and documents, not an orchestrator.**

Key questions (in the contributions file):
1. On work where research and planning are done by different people, who writes the intent Orbit starts from, and does Kai output feed it? — *answered by:* Stripe's Agent Foundation team; a second Orbit demo.
2. How split are research, intent and planning across people in our target orgs, compared with Stripe's "product hat" engineers? — *answered by:* a task-level time study with 5–8 teams.

## Could not verify
- Orbit is documented only by one vendor-produced video and one tweet; the UI tip was read from a 360p frame.
- How often one person does both research and planning at Stripe today is not measured; "product hat" is a cultural description from 2024.
- Compass's role in agent handoffs is inferred.
