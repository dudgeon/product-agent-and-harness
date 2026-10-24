# Stripe's agent ecosystem, mapped to the product and software lifecycle

Date: 2026-10-24. Worker draft for Geoff's review (task competitive-teardown-stripe-knowledge-agents). Built only from the filed source notes in `../../research/sources/`; each handoff is marked **documented** (a Stripe source says it happens), **inferred** (consistent with sources but not stated), or **unknown**.

## The short answer on Kai → Orbit

**No public source describes a direct handoff from Kai to Orbit.** What the sources show instead:

1. **Kai's context is locked in single-user sessions.** Stripe lists "better collaboration primitives" as roadmap because "Users generate a lot of context in their Kai sessions that is currently 'locked in'" ([Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md), first-party, Jul 2026). So in mid-2026 there was no shared Kai session or artifact an engineering agent could pick up.
2. **Orbit starts from an engineer's stated intent, not from a PM artifact.** In the only demo, an engineer types a research question, Orbit reads the **codebase and Trailhead** (internal docs), then drafts a plan ([Not My Business video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md), first-party, Oct 2026). Orbit is "targeting individual engineers first"; PM use isn't stated.
3. **The shared substrate is the bridge.** Kai, Orbit, Minions and Harbor all reach the same Toolshed MCP tools (~500, "a shared capability layer" for "hundreds of different agents") and the same documents (Trailhead, Google Docs, Slack threads, tickets) ([Minions part 2](../../research/sources/stripe-minions-part-2.md); [part 1](../../research/sources/stripe-minions-one-shot-coding-agents.md)). So a PM's output reaches engineering agents **through documents, Slack, tickets and prototypes that people carry across**, not through an agent-to-agent call.

So the PM → engineering boundary at Stripe is, as far as the public record goes, **a human handoff over shared documents and tools**. The agent-to-agent handoffs that *are* documented sit elsewhere: Kai → Harbor, Harbor → coding agents, docs, tickets and Slack → Minions, Orbit → Minions.

That matters for us: the gap Geoff's intent-shaping work targets (goal → intent → agent-ready plan) is exactly the seam Stripe has *not* automated. Orbit picks up at intent, written by an engineer.

## The lifecycle, stage by stage

The rows follow Stripe's own whiteboard chain (Opportunity → Problem → Goal → Intent → Plan, then Code; [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) ~12:24), extended with review, release and operate.

| Stage | Who does it at Stripe | Agents and tools | Artifact produced | Evidence |
|---|---|---|---|---|
| **Opportunity** | People (leaders, PMs, engineers wearing a "product hat") | none named; Kai for research and data | Not described | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md); [Pragmatic Engineer](../../research/sources/pragmaticengineer-inside-stripe-engineering-culture-part-2.md) |
| **Problem, Goal** | People, through **customer conversations** (the board's brace) and UXR | **Kai**: account research, data analysis (5,000+ sessions a day), reading team email lists; **Hubble/"ask data"** for metrics | Kai artifacts (dashboards, reports, docs) that "live alongside the conversation", single-user | [Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md); [How I AI, Krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md) |
| **Intent (define, prototype)** | PM, designer or engineer | **Harbor** (browser prototypes, 12,000 made); **Protodash** (Dashboard prototypes; "more PMs than designers"; a PM pastes a PRD from Google Docs); Google Docs; agent-drafted specs reviewed as GitHub issues (SDK team) | Published prototype URL with anchored comments; PRD in Google Docs; spec issue | [Harbor](../../research/sources/stripe-harbor-ai-prototyping.md); [Protodash](../../research/sources/howiai-stripe-protodash-owen-williams.md); [SDK post](../../research/sources/stripe-ai-didnt-write-our-sdk.md) |
| **Plan** | Engineer, with teammates commenting | **Orbit**: reads codebase and Trailhead, drafts a step plan; teammates annotate; Orbit's UI says "Workspaces share context across sessions, all visible to each other" | A shareable, commented plan | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) (13:30-15:30; UI tip read from a frame) |
| **Code** | Agents, steered by an engineer | **Minions** (Goose fork, devboxes, Toolshed); also Claude Code and Cursor reading the same rule files; **payment-method factory** for repeated integrations | Branch and PR (~1,300 minion PRs a week) | [Minions part 1](../../research/sources/stripe-minions-one-shot-coding-agents.md), [part 2](../../research/sources/stripe-minions-part-2.md); [factory](../../research/sources/stripe-payment-method-factory.md) |
| **Review** | Human reviewer on every PR, plus an agent | **Gru** (code-review agent); CI capped at two rounds | Approved PR | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md); [part 2](../../research/sources/stripe-minions-part-2.md) |
| **Release** | Automated | Deploy to 1% of boxes, auto-pause and roll back on errors | Live change | [video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) |
| **Operate, learn** | Ops, finance, compliance, engineers | **Kai** (incident triage, logs, recurring digests); **compliance review agents** (100+ agents on the agent service); factory **learning and decision logs** feed prompt updates; Kai's planned skill-reflection loop | Digests, review answers, improved prompts and skills | [Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md); [AWS](../../research/sources/aws-stripe-compliance-agents.md); [factory](../../research/sources/stripe-payment-method-factory.md) |

## Every handoff, and how sure we are

| From → to | Mechanism | Artifact carried | Status |
|---|---|---|---|
| Kai → Harbor | Harbor's toolset over Stripe's internal MCP; Harbor's renderer (Drydock) is a service Kai uses. Example: a producer ran a stripe.com viewport analysis in Kai, then made it a clickable Harbor prototype | Research → prototype | **documented** ([Harbor](../../research/sources/stripe-harbor-ai-prototyping.md)) |
| Harbor → coding agents | Coding agents on devboxes pull a prototype's file tree into a repo, or push an idea into Harbor | Prototype source | **documented** ([Harbor](../../research/sources/stripe-harbor-ai-prototyping.md)) |
| Protodash → engineering | A designers' prototype PR became the source of truth an engineer built from | Prototype PR | **documented**, one example ([Protodash](../../research/sources/howiai-stripe-protodash-owen-williams.md)) |
| Slack thread / Google Doc / ticket → Minion | Emoji reaction or tagging the app; the thread or message is the prompt; links are hydrated over MCP before the run; the docs platform, feature-flag platform and ticketing UI can launch minions; flaky tests auto-file tickets that prompt a minion | Thread, doc, ticket | **documented** ([part 1](../../research/sources/stripe-minions-one-shot-coding-agents.md); [Kaliski](../../research/sources/howiai-stripe-minions-kaliski.md)) |
| Orbit → Minion | One button; the minion gets a devbox, the plan and extra instructions; may run 12 hours and pause to ask | Reviewed plan | **documented** ([video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md)) |
| Trailhead → Orbit, Minions, Kai | Agents read internal docs (Orbit "reading Trailhead"; minions fetch internal documentation over MCP) | Owner-verified docs | **documented** for Orbit and Minions; **inferred** for Kai |
| Kai → specialised agents | Kai "invoke[s] more specialized agents and skills" for engineers | Not described | **documented**, mechanism unknown ([Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md)) |
| **Kai → Orbit** | Not described. Likely a person shares Kai's output (doc, dashboard, Slack post) and an engineer starts Orbit with intent and links; Orbit's research then re-reads code and docs | Doc or link, via a person | **unknown / inferred** |
| PM → engineer (intent) | Prototypes, Google Docs PRDs, Slack threads, Compass project pages; teams of 6-10 engineers own a product area | Prototype, PRD, project page | **inferred** from [Pragmatic Engineer](../../research/sources/pragmaticengineer-inside-stripe-engineering-culture-part-2.md) (Compass), Protodash, and the video |
| Shipped work → knowledge | Factory learning/decision logs and review comments update prompts; Kai skill reflection (roadmap); Trailhead owner verification | Prompt, skill and doc updates | **documented** for the factory; **roadmap** for Kai |

## A diagram in words

```
            PEOPLE (customer conversations)                    AGENTS
Opportunity ──► Problem ──► Goal ──► Intent ──────────────► Plan ──► Code ──► Review ──► Release
                 │  Kai research, data      │ Harbor / Protodash       Orbit      Minions   Gru + human  1% canary
                 │  (single-user sessions)  │ prototypes, PRDs, specs   (eng.)
                 └──── artifacts carried by people via Slack, Docs, tickets, prototypes ────┘
   Shared substrate under every stage: Toolshed (~500 MCP tools) · Trailhead (verified docs) · devboxes · Compass (projects)
   Documented agent-to-agent links: Kai→Harbor · Harbor→coding agents · Slack/Docs/tickets→Minions · Orbit→Minions
   Not documented: Kai→Orbit
```

## What this implies for our options

- **The seam to fund is intent → plan across roles.** Stripe automated plan → code (Orbit, Minions) for engineers and research → prototype for everyone, but the PM's goal and intent reach engineering through people and documents. Options that carry shaped intent (with its evidence) into a planning agent, a shared session or an agent-ready spec, address the part Stripe left manual. See [intent-shaping-and-spec](../../options/DIMENSIONS.md#intent-shaping-and-spec-intent-shaping-mode-and-spec-standard) and the S05 story.
- **Single-user sessions are the blocker Stripe names itself.** Kai's roadmap item (share context across sessions, many people and agents on one artifact) is the same choice as our [session-persistence-sharing](../../options/DIMENSIONS.md#session-persistence-sharing-session-persistence-sharing-and-handoff) dimension; Orbit's workspaces "share context across sessions", which suggests Stripe solved it first on the engineering side.
- **Stripe connects agents through a shared tool layer and documents, not orchestration.** Toolshed plus MCP-exposed specialist tools (Harbor) is the pattern; there's no evidence of a central orchestrator routing work from Kai to Orbit.

Key questions this raises (for the contributions file, not answered here):
1. Does Kai share anything with Orbit today (e.g. Kai artifacts as Orbit context), or is the human handoff deliberate? — *answered by:* asking Stripe's Agent Foundation team; watching for the promised Kai collaboration features.
2. Who writes the intent Orbit starts from on PM-led work: the PM or the engineer? — *answered by:* Stripe; a second Orbit demo.
3. Would our users accept a shared session that spans PM shaping and engineering planning, or do they want a handoff artifact (spec, plan) at the boundary? — *answered by:* user interviews; prototype both.

## Could not verify
- Orbit is documented only by one vendor-produced video and one tweet; the UI tip was read from a 360p frame.
- Compass's role in agent handoffs is inferred; no source says agents read or write Compass.
- Kai → specialised agents: the mechanism (MCP, skill, Orbit itself?) is not described.
