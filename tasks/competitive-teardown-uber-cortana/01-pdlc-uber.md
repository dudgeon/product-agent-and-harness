# Uber's agent ecosystem, mapped to the tasks of the product lifecycle

Date: 2026-11-02. Task competitive-teardown-uber-cortana. Built only from the filed source notes in `../../research/sources/`, in the frame of the [Stripe map](../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md). Each handoff is marked **documented** (an Uber source says it happens), **inferred** (consistent with the sources but not stated) or **unknown**. Visual version: [01-pdlc-uber.html](01-pdlc-uber.html), built by [01-pdlc-uber.build.py](01-pdlc-uber.build.py).

## Why this map is anchored on tasks

Uber's sources describe tasks, not job families:
- **Anyone can run the shaping tasks.** Cortana is for "anyone in the company", including "someone in Ops in some country" ([podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 42:11). In the demo the same assistant does business research, requirements, mock-ups and code-change analysis ([talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 11:46-13:14).
- **PMs, designers and engineers each have their own tools as well.** "Dozens of PMs" use a PRD Evaluator ([PRD reviewer](../../research/sources/uber-first-pass-prd-reviewer.md)). A designer built uSpec, a set of Cursor skills over a Figma MCP that writes design specs ([uSpec](../../research/sources/uber-automate-design-specs.md)). Engineers start Minion from Slack or the web ([podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 50:20).
- **Engineers are told their job is now building context.** Medisetty: "how do you build the right context for the agents to produce reliable output", and "give the right specs right constraints" (podcast 1:25:42).

So each row below is a **task**. "Who does it" lists the roles the sources show doing it.

## The short answer on Cortana → Minion

**Uber documents the shaping-to-code handoff that Stripe's record lacks, but not how it works.**

1. **One assistant covers research → requirements → mock-ups → plan.** In the demo a Slack thread tags Cortana, which judges whether the idea is "a good business opportunity" from the context graph, drafts requirements, makes Figma mock-ups for an A/B test, and lists the code that can be reused. Then "we hand off from that Cortana agent" to Minion ([talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 11:46-13:25). Stripe has no published Kai → Orbit link.
2. **The handoff mechanism is not shown.** No source says what crosses from Cortana to Minion: a link, a spec file, the Slack thread or a session. The nearest documented mechanism is "@minion, follow this thread ... create a PR", which turns a Slack thread into a PR (podcast 51:30-51:49). Minion also takes a plan or "really good spec" (podcast 50:02).
3. **Specs have a tracked home that agents read, but Cortana's link to it is not documented.** A PRD/ERD tool (uPlan) holds product and engineering design docs, launch, experiment and production-readiness reviews, with status, owners and Jira/Linear links. It all feeds the context graph: "a source of truth system for both humans and agents to know the specs for every project" (podcast 46:48-48:28). Whether Cortana's drafted requirements are saved there, or pass the PRD Evaluator, is **unknown**.

**What the task view changes.** At Uber the seam is not missing; it is *undocumented*. The shaping tasks sit inside one shared assistant, often in a team Slack channel, so the context may travel inside Cortana's session and thread rather than in a person's head. What Uber leaves open is the artifact: whether shaped intent becomes a reviewed, tracked spec (uPlan, PRD Evaluator) before Minion builds it, or goes straight from a chat to a PR. That choice is ours to make too.

## The lifecycle, task by task

The rows follow the stages in Huda's walkthrough (idea → business research → requirements → designs → code changes → Minion → inner loop → outer loop → maintenance), extended with experiment and operate.

| Task | Who does it at Uber (roles seen) | Agents and tools | Artifact produced | Evidence |
|---|---|---|---|---|
| **Spot the opportunity** | Whoever is "jamming on it in Slack"; leaders say "should we build it" is now the bottleneck | Slack thread; Cortana tagged in | Slack thread | [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 11:46-12:08, 17:44 |
| **Research the opportunity** | Anyone, including ops staff | **Cortana** grounded on the **context graph** (past large-venue events, candidate stadiums); data agents such as QueryGPT and Finch for SQL | Cortana answer in Slack, then in the web interface | [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md); [podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 42:11; [QueryGPT](../../research/sources/uber-querygpt.md); [Finch](../../research/sources/uber-finch-data-agent.md) |
| **Write the requirements (PRD)** | PMs (PRD Evaluator users); in the demo, the presenter with Cortana | **Cortana** drafts requirements (e.g. North America only); **PRD Evaluator** scores readiness (Ready, Caveats, Not Ready) without approving; **uPlan** holds the PRD and its reviews | Requirements in Cortana; PRD and review status in uPlan | [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 12:31; [PRD reviewer](../../research/sources/uber-first-pass-prd-reviewer.md); [podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 46:48 |
| **Design: mock-ups, prototype, design spec** | Designers, PMs, the demo presenter | **Cortana** makes Figma mock-ups (two A/B variants); **uSpec** (Cursor + Figma MCP) writes design specs; AI prototyping sharpens the PRD | Figma mock-ups; design spec | [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 12:38; [uSpec](../../research/sources/uber-automate-design-specs.md); [prototyping](../../research/sources/uber-ai-prototyping.md) |
| **Plan the change (ERD)** | Engineers; Cortana in the demo | **Cortana** lists reusable screens and back-end code; ERD in **uPlan**; Minion plan mode | Code-change analysis; ERD; Minion plan | [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 12:54; [podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 47:07-49:38 |
| **Write the code** | Agents, started by engineers from Slack, web, CLI or a PR | **Minion** on a mega DevPod (~15% of production PRs, Oct 2026); Claude Code, Codex, OpenCode through **AIFX** | Draft PR, possibly across repos | [podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 49:38; [Summit](../../research/sources/pragmatic-summit-uber-leading-engineering-agentic-shift.md) |
| **Validate (inner loop)** | Agents | `aifx validate` (lint, coverage, build rules); simulator screenshot compared with Figma; **Slate** per-branch staging | Validated draft PR with a table of checks and screenshots | [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 14:14-15:49; [podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 55:08-1:02:33 |
| **Review the change** | A person on every PR; a small model inside the agent's own validation loop, a large one in CI | **uReview**; **Code Inbox** (routing, risk score, blast radius); self-healing CI | Approved PR | [uReview](../../research/sources/uber-ureview-code-review.md); [podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 56:35-59:22 |
| **Release and experiment** | Not described for agents | A/B variants planned in the demo; experiment capacity named as a bottleneck | Not shown | [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 12:44, 17:40 |
| **Operate, maintain and learn** | On-call engineers; service owners who enrol services | Managed **maintenance loops** (flag cleanup, bounded and scheduled); **DebugAssist** → Minion; incident reviews mined monthly for new skills; Cortana health reports; **ADR** on endpoints | Diffs, RCAs on Jira, new skills | [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 15:53-17:10; [podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 43:07, 1:18:29; [ADR](../../research/sources/github-uber-adr.md) |

## Every handoff, task to task

| From task (agent) → to task (agent) | Mechanism | Status |
|---|---|---|
| Slack thread → research (Cortana) | Tag Cortana in the thread | **documented** |
| Cortana in Slack → Cortana on the web | "open Cortana into a web interface" from Slack | **documented** |
| Research → requirements → mock-ups → code-change analysis (all Cortana) | One assistant, shown step by step in one demo | **documented** |
| Context graph → every Cortana answer | Graph is the "default grounding"; Cortana navigates it, then reads deeper | **documented** |
| Team persona → channel members | Custom skills and prompt bound to a team Slack channel; several people collaborate there | **documented** |
| **Shaped intent (Cortana) → write code (Minion)** | "we hand off from that Cortana agent" to Minion; what crosses is not shown | **documented, mechanism unknown** |
| Requirements (Cortana) → PRD/ERD tool (uPlan) | Not described | **unknown** |
| PRD → PRD Evaluator → revised PRD | PM runs the evaluator on a PRD with its linked docs; it scores and suggests text, never approves | **documented** |
| Requirements (Cortana) → PRD Evaluator | Not described | **unknown** |
| uPlan docs and reviews → context graph | "all of this data also goes into the graph" | **documented** |
| PRD → ERD → Jira or Linear task | Links held in uPlan; AI now clusters and back-fills missing links to measure feature time | **documented** |
| Slack thread, plan or spec → write code (Minion) | "@minion, follow this thread ... create a PR"; plan mode; templates | **documented** |
| Figma mock-ups → validate | Simulator screenshot compared with the Figma spec | **documented** |
| Draft PR → validate → review | Minion stops at a draft PR; inner-loop checks; PR carries a table of checks | **documented** |
| PR → uReview, Code Inbox → human reviewer | Risk score and routing; a person reviews every PR; "green lane" only later | **documented** |
| CI failure → fix | Self-healing CI | **documented** |
| Release → experiment → decision | A/B variants planned; launch and readout not shown | **inferred** |
| Service enrolled → maintenance loop → diffs | Managed, scheduled, rate-limited loops | **documented** |
| Landed or rejected diffs → better skills | Diffs and comments used as labels | **documented** |
| Incident reviews → new maintenance skills | Monthly | **documented** |
| Bug report → DebugAssist RCA → Minion PR on the Jira task | Hand off the RCA; PR attached to the Jira task | **documented** |
| Customer or user research → research (Cortana) | Not described | **unknown** |
| Production data and health → next opportunity | Cortana can produce health reports and run queries; not shown as a loop | **inferred** |
| Agent Builder agents ↔ Cortana personas | Both bind a prompt and tools to a team; no source links them | **unknown** |
| ChatGPT Work ↔ Cortana | ChatGPT Work went to 30,000+ staff on 2026-10-22; the split with Cortana is not stated | **unknown** |

**Counts: 25 handoffs: 18 documented (one of them with its mechanism unknown), 2 inferred, 5 unknown.**

## Diagram (text)

```
TASK:     Spot        Research     Write       Design       Plan       Write   Validate  Review   Release &   Operate,
          opportunity opportunity  PRD         mock-ups     change     code    (inner)   change   experiment  maintain
HUMANS    ● anyone    ● anyone     ● PMs       ● designers  ● eng      ·       ·         ● every PR  ?        ● on-call, owners
AGENTS    Slack ────► Cortana ───► Cortana ──► Cortana ───► Cortana ══?══► Minion ─► aifx validate ─► uReview ─ ? ─ maintenance loops
                                   PRD Evaluator  uSpec      uPlan ERD                Slate, Figma check  Code Inbox     DebugAssist → Minion
                                   uPlan  ◄ - - - ? - - - (Cortana drafts → uPlan not described)
SHARED    context graph (default grounding) · skills marketplace · MCP gateway · model gateway · DevPods · Slack · Jira/Linear
```

## What it means for our options

- **One shared assistant across the shaping tasks is a real, running option.** Uber shows a single company assistant doing research, requirements, mock-ups and plan, with team personas in Slack channels. Stripe splits the same tasks across Kai, Harbor and Orbit. That is a live choice on [work-structure](../../options/DIMENSIONS.md#work-structure-how-structured-the-work-is-what-agent-shape-fits-and-the-unit-of-an-agent): one assistant across stages, or one agent per stage.
- **Uber is the clearest public case for "specs as a graph that agents read".** uPlan holds the PRD, ERD, reviews and their links to tickets, and feeds them to the graph. That supports options in [intent-shaping-and-spec](../../options/DIMENSIONS.md#intent-shaping-and-spec-intent-shaping-mode-and-spec-standard) and [artifact-and-project-structure](../../options/DIMENSIONS.md#artifact-and-project-structure-how-pm-artifacts-and-projects-are-structured-stored-and-found) where the spec is a tracked record, not a file in one repo.
- **The spec gate before code is still the open seam.** Uber has three pieces (Cortana's drafts, the PRD Evaluator, uPlan) and Minion, but no source joins them. A shaping agent that writes into the tracked spec, runs the readiness check and passes the result to the coding agent is the part nobody has shown.
- **Measurement moved to feature velocity, and Uber found broken spec-to-task links.** Uber had to use AI to rebuild PRD → ERD → task links before it could measure P50 feature time (podcast 1:24:05). That is evidence for the dependency agent's write-back job.

Key questions (in the contributions file):
1. What crosses from Cortana to Minion: the Slack thread, a saved spec, or the Cortana session? — *answered by:* Uber's AI Developer Tools team (Huda); a second demo.
2. Does shaped intent pass the PRD Evaluator and land in uPlan before Minion builds, or can a chat go straight to a PR? — *answered by:* Uber; a pilot of our own with both paths.

## Could not verify
- The talk's demo is a walkthrough; its screens were not read frame by frame, and the requirements and mock-ups shown may be staged.
- uPlan is named once in an auto-generated transcript ("U-Plan") and in job-post snippets whose originals return 404.
- DebugAssist appears only in the podcast.
- Whether Genie still runs beside Cortana, and how ChatGPT Work divides the work with it, is not stated anywhere.
