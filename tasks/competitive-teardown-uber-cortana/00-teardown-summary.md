# Teardown: Uber's Cortana

Date: 2026-11-02. Task competitive-teardown-uber-cortana. Same frame as the [Stripe](../competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md), [Ramp](../competitive-teardown-ramp-glass/) and [Shopify](../competitive-teardown-shopify-river/00-teardown-summary.md) teardowns. Every claim links to a source note in `../../research/sources/`. Lifecycle map: [01-pdlc-uber.md](01-pdlc-uber.md) and [01-pdlc-uber.html](01-pdlc-uber.html). Options: contributions.

## Which Cortana

- **Uber's Cortana is its internal company-wide AI assistant.** It is the sixth of six "building blocks" of what Uber calls its software factory, described by Distinguished Engineer Uday Kiran Medisetty and Adam Huda (who leads AI developer tools) at AI Engineer ([talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md), first-party, uploaded 2026-08-21).
- **It is not Microsoft's Cortana.** The only Uber link to Microsoft's assistant is a 2015 Windows 10 integration that booked rides. No other Uber "Cortana" turned up. There was no ambiguity to ask Geoff about.
- **Not a rename of Genie, as far as the record shows.** Genie was Uber's 2023 Slack on-call copilot ([Genie](../../research/sources/uber-genie-on-call-copilot.md)). It became a "Michelangelo Genie framework" in 2025 ([agentic RAG](../../research/sources/uber-enhanced-agentic-rag.md)). Business Insider still called Uber's Slack Q&A bot "Genie" in September 2026 ([anecdote](../../research/sources/digitaltoday-business-insider-uber-ai-genie.md)). Medisetty gives Cortana its own origin: "back in December" (taken to be 2025), "one of the engineers built an AI assistant ... we call it Cortana" on web and Slack that answered questions from any codebase ([podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 37:45). Genie is a predecessor in shape (Slack, grounded answers), not a documented ancestor.
- **The name is absent from public sources before August 2026.** It does not appear in the March Pragmatic Summit talk, the April MCP keynote, the May Minion session, the job posts, or any uber.com blog post to 2 Nov 2026. The talk and the podcast are the only primary sources that describe it.

## Sources read in full

39 notes, filed under `filed_by: competitive-teardown-uber-cortana`. The ones that carry the teardown:

- **Cortana itself:** [AI Engineer talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) (auto-captions, read in full); [Pragmatic Engineer podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) (publisher transcript, read from 18:00 to the end).
- **The platform under it, Uber Engineering blog:**
  - cost and governance: [efficient software factory](../../research/sources/uber-efficient-software-factory.md) (Aug 2026);
  - tools: [MCP gateway](../../research/sources/uber-designing-mcp-gateway.md) (Oct 2026);
  - identity: [agent identity](../../research/sources/uber-solving-agent-identity-crisis.md) (May 2026);
  - model gateway: [GenAI Gateway](../../research/sources/uber-genai-gateway.md) (2024);
  - security: [ADR repo](../../research/sources/github-uber-adr.md).
- **Other talks:**
  - [Pragmatic Summit](../../research/sources/pragmatic-summit-uber-leading-engineering-agentic-shift.md), Chada and Smith, Mar 2026;
  - [MCP Dev Summit keynote](../../research/sources/aaif-uber-operating-mcps-enterprise-scale.md), Apr 2026;
  - [Minion session](../../research/sources/background-agents-summit-uber-minion-ramakrishnan.md), May 2026, page only;
  - [uReview talk](../../research/sources/ai-engineer-uber-ureview-code-review.md).
- **Shaping tools:** [PRD Evaluator](../../research/sources/uber-first-pass-prd-reviewer.md); [AI prototyping](../../research/sources/uber-ai-prototyping.md); [uSpec](../../research/sources/uber-automate-design-specs.md); [responsible AI](../../research/sources/uber-scaling-responsible-ai.md).
- **Earlier Slack and data agents:** [Genie](../../research/sources/uber-genie-on-call-copilot.md), [agentic RAG](../../research/sources/uber-enhanced-agentic-rag.md), [QueryGPT](../../research/sources/uber-querygpt.md), [Finch](../../research/sources/uber-finch-data-agent.md).
- **Context and competition:** [ChatGPT Work rollout](../../research/sources/uber-chatgpt-work-rollout.md) (22 Oct 2026); [The Pragmatic Engineer deepdive](../../research/sources/pragmatic-engineer-how-uber-uses-ai-for-development.md) (free part only); [Port fact sheet](../../research/sources/port-inside-uber-software-factory.md); [The AI Thinker](../../research/sources/theaithinker-ai-native-software-factory.md); [Fortune on cost](../../research/sources/fortune-uber-cto-tokenmaxxing-over.md); [Fortune on the COO](../../research/sources/fortune-uber-coo-ai-spending-claude-code.md); [job posts](../../research/sources/uber-careers-staff-engineer-aifx.md), and [a second post](../../research/sources/uber-careers-sr-staff-agentic-systems-engineer.md).
- **Derivative re-summaries of the talk:** [ZenML](../../research/sources/zenml-uber-managed-software-factory.md), [Port newsletter](../../research/sources/port-newsletter-how-uber-built-software-factory.md), [Sean Weldon](../../research/sources/seanweldon-agentic-sdlc-at-uber.md), [BigGo](../../research/sources/biggo-uber-agents-write-70-percent.md), [StartupHub](../../research/sources/startuphub-uber-agentic-sdlc.md), [ShiftMag](../../research/sources/shiftmag-how-uber-engineers-use-ai-agents.md). They add nothing new about Cortana; they only show the talk was widely relayed.

## What Cortana is and who uses it

- **One assistant, for anyone, on every surface.** Skills, MCP tools and the context graph are "plugged into that in every surface possible whether it's on Slack, CLI, web". Anyone can ask a question; Cortana "can look up the context graph, invoke any skill, check any code in any codebase" ([talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 10:19-10:47). Users include "someone in Ops in some country" asking how something is built and who owns it ([podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 42:11).
- **Team personas.** Employees "personalize" Cortana with custom skills and a custom prompt, "hook it up into your team Slack channel so that ... it knows all of the things about that team and works like ... that teammate". One or more people can collaborate in the same channel ([talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 10:49-11:17).
- **Shaping and planning, not coding.** In the demo Cortana runs from idea to code-change analysis, then hands off to Minion, the cloud coding agent ([talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 11:46-13:25).
- **How it grew.** One engineer built a code Q&A assistant in December (2025). Usage spread to research, query, data-source, ownership and RCA questions. Traces showed models spending turns getting grounded, so Uber built the context graph and made it Cortana's default grounding ([podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 37:45-39:43).

## Which jobs it does

From the talk and podcast. Each is first-party; none has a published outcome.
- **Answer questions about code and the org.** How is this built, where is it, who works on it, what is its history ([podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md) 42:35).
- **Data questions.** The worked example is "how many mobility trips in India are cash", grounded through the graph to "blessed queries" ([talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md) 09:53; podcast 40:43).
- **Service health.** A "360 degree health report" for an asset from logs, monitoring, dependencies and storage (podcast 43:07).
- **Run any skill** "anyone has built" (podcast 42:58).
- **Business research, requirements, Figma mock-ups and code-change analysis** for a new feature (talk 12:08-13:14).
- **Act as a team teammate through a persona** in a team channel (talk 10:49).

## Harness architecture

- **Loop source: not disclosed.** No source names Cortana's agent loop, framework or model.
  - Uber has its own options: LangFx, a LangChain/LangGraph-based SDK used for Genie, Autocover and other agents ([agentic RAG](../../research/sources/uber-enhanced-agentic-rag.md); [Summit](../../research/sources/pragmatic-summit-uber-leading-engineering-agentic-shift.md)).
  - It also has an agent platform from early 2025: a framework-agnostic Python SDK plus a no-code UI, deployed to Kubernetes, with "thousands of internal agents" ([identity](../../research/sources/uber-solving-agent-identity-crisis.md)).
  - That Cortana runs on either is inference.
- **Layering: Cortana is the top of a stack of shared, harness-neutral building blocks.** Medisetty calls them "vendor-neutral harness-neutral building blocks" (podcast 33:08). Uber's six:
  1. **Model gateway:** every model request at Uber goes through it; 800+ projects; 100M+ requests a day.
  2. **MCP gateway:** 1,000+ tools in the talk; 800+ servers and 5,000+ tools in the Oct 2026 post.
  3. **Agentic DevPods.**
  4. **Skills marketplace:** 2,500 skills in the talk; 3,600+ in the Aug post.
  5. **Context graph.**
  6. **Cortana.**

  Sources: [talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md); [efficient factory](../../research/sources/uber-efficient-software-factory.md); [MCP gateway](../../research/sources/uber-designing-mcp-gateway.md).
- **Beside Cortana, a wrapper over the vendor harnesses.** AIFX (AI Foundations) wraps Claude Code, Codex and OpenCode. Settings, skills, tools and plugins follow the engineer across harnesses, settings are centrally managed, and a status line shows tips and spend (podcast 24:00-25:28). The Aug 2026 post calls it a "unified harness wrapper" ([efficient factory](../../research/sources/uber-efficient-software-factory.md)).
- **Runtime location: inside Uber, mechanism not stated.**
  - Cortana is reached on Slack, web and CLI, and carries the user's permissions, so it runs as an Uber-hosted service.
  - Where it executes is not stated: a service, a DevPod or a Kubernetes agent deployment.
  - Minion, by contrast, runs on the "mega DevPod": pre-warmed Kubernetes "balloon pods" with every repo cloned and search indexes built (talk 05:41-07:06; podcast 52:17).

## Capability packaging and distribution

- **Skills marketplace.**
  - Contents: one skills monorepo of central and team skills, behind one quality gate of lint checks and automated reviews.
  - Install: "one single command to discover and install any plug-in". Default skills are auto-installed by engineer persona.
  - Scale: 20,000+ executions a day at the talk; "around probably 30,000" in the podcast; 3,600+ skills and 30K+ executions a day in the Aug 2026 post.
  - Improvement: traces, comments and continuous evals are fed back to skill authors. Generating improvement patches from harness traces is in flight.
  - Sources: talk 07:09-08:31; podcast 33:43-35:24; [efficient factory](../../research/sources/uber-efficient-software-factory.md).
- **The same skills reach Cortana and the coding harnesses.** Cortana can "invoke any skill"; AIFX installs a plugin "across all of the harnesses". The ChatGPT Work rollout is supported by "an internal AI skills library" ([ChatGPT Work](../../research/sources/uber-chatgpt-work-rollout.md)).
- **Tools come through one MCP gateway.**
  - Generation: AutoCrawler generates MCP tools from the Thrift/Protobuf IDL registry. Each tool stays disabled until its owning team reviews and enables it, and description changes are diffs the owner approves.
  - SaaS tools: Google, Slack and Jira are hosted with token exchange.
  - Token savings: Omni MCP, CLI projection and code mode keep token use down ("more than 40% fleetwide" savings in the talk; 55-71% from code mode on simple calls in the blog).
  - Sources: [MCP gateway](../../research/sources/uber-designing-mcp-gateway.md); [MCP keynote](../../research/sources/aaif-uber-operating-mcps-enterprise-scale.md); talk 03:46-05:36.
- **A separate no-code route: Uber Agent Builder.** No-code agents over MCP servers and Uber datasets, with Agent Studio for tracing, versioning and evals, and a registry where agents are found and copied. "Thousands" were active monthly by April 2026 ([MCP keynote](../../research/sources/aaif-uber-operating-mcps-enterprise-scale.md); [PE deepdive](../../research/sources/pragmatic-engineer-how-uber-uses-ai-for-development.md)). How Cortana personas relate to Agent Builder agents is not stated.

## Remote invocation

- **Cortana is reached from Slack (by tagging), web and CLI.** A Slack conversation can be opened into the web interface (talk 12:15).
- **Cortana hands off to Minion; the mechanism is not shown.** The handoff itself is documented (talk 13:17).
- **Minion has its own routes:**
  - from web or Slack, in plan mode or one-shot (podcast 50:20);
  - "@minion ... follow this thread ... create a PR", with the thread as context (podcast 51:30-51:49);
  - from CLI, API and an existing PR, with prompt templates and a prompt improver ([Summit](../../research/sources/pragmatic-summit-uber-leading-engineering-agentic-shift.md));
  - from DebugAssist, which passes it a root-cause analysis (podcast 1:18:29).
- **Cortana calling other agents:** only through skills. No source says Cortana calls Agent Builder agents or Minion programmatically.

## Sessions, persistence and sharing

- **Shared in team channels; sessions otherwise undescribed.** A persona lives in a team Slack channel, where "one or more people can even collaborate on the same Slack channel" (talk 11:15). This makes Cortana's work visible to the channel by design.
- Nothing is published on whether web or CLI sessions persist, can be resumed, handed on or shared, or what a "session" counts in the 20,000-a-day figure.
- Coding harnesses have session traces in the model gateway and a dashboard that flags 16 anti-patterns ([efficient factory](../../research/sources/uber-efficient-software-factory.md)). Whether that covers Cortana is unknown.

## Identity and delegation

- **Cortana acts as the user.** "We carry forward all of the existing user permissions, so then if I'm only able to access the stuff that I had access to" (podcast 43:20).
- **Uber's agent identity stack (May 2026) is the most detailed published in our library** ([identity](../../research/sources/uber-solving-agent-identity-crisis.md)):
  - SPIRE workload identity, plus an Agent Registry populated by Michelangelo;
  - a token service mints single-hop JWTs, valid for minutes, carrying the actor chain [user, agent, agent…];
  - the MCP gateway enforces charter policies for humans, services and agents, and relays the user's token to SaaS servers;
  - P99 for token exchange is under 40 ms.
  - Roadmap: human-in-the-loop approval, workflow authorisation, session and intent claims in tokens.
- **Not stated:** whether personas are registered agents with their own identity, or how channel membership interacts with each asker's permissions in a shared channel.

## Governance, cost, review and autonomy

- **One perimeter for every model call.**
  - Model gateway: Spire identity; a PII anonymiser for 20+ types; AI Guard (five specialised models from the security team on every request and response, under 100 ms); audit logs and session traces (talk 01:46-03:19; podcast 22:10-23:42).
  - Endpoints: the open-source ADR watches third-party coding agents, with 10k+ sessions a day ([ADR](../../research/sources/github-uber-adr.md); [CISO](../../research/sources/claude-uber-ciso-insider-threat-ai.md)).
- **Cost is shown to people rather than hard-capped** ([efficient factory](../../research/sources/uber-efficient-software-factory.md); podcast 25:34-28:20):
  - spend tiers per user, with manager approval to step up, and a separate tier for background agents;
  - Slack nudges at 50/80/100% of expected spend;
  - a CostCheck plugin and a live cost status line.
  - The history: AI costs up at least 6x since 2024 by March ([Summit](../../research/sources/pragmatic-summit-uber-leading-engineering-agentic-shift.md)); the year's budget reported gone in four months ([Fortune](../../research/sources/fortune-uber-cto-tokenmaxxing-over.md)); a per-tool cap later replaced by visibility.
  - Cortana's own cost model is not published. One commentator frames it as cost per query ([AI Thinker](../../research/sources/theaithinker-ai-native-software-factory.md)).
- **Review.**
  - A person reviews every PR. Minion stops at a draft PR, validates in the inner loop, and attaches a table of checks and screenshots.
  - Code Inbox adds a risk score and blast radius.
  - A "green lane" for auto-landing low-risk PRs waits on backtesting (talk 13:47-15:49; podcast 56:35-59:22).
- **Bounded autonomy for loops.** Maintenance loops run from "a managed surface", on a schedule, with a cap on diffs per engineer: "We don't want thousands of loops being set up across the company without any bounds" (talk 16:26-16:50).
- **On the shaping side, no approval step for Cortana's output is described.** The PRD Evaluator "doesn't approve anything"; it scores readiness for the human checkpoint ([PRD Evaluator](../../research/sources/uber-first-pass-prd-reviewer.md)). Governance of AI features "starts in PRD/ERD review" ([responsible AI](../../research/sources/uber-scaling-responsible-ai.md)).

## Context and memory, and artifacts

- **The context graph is Cortana's memory of the organisation.**
  - What it holds: people, PRs, services, mobile apps, the data lake, design docs, Jira, incidents, on-call events and config changes, all linked.
  - Sizes, which don't reconcile:
    - 150 node and edge types, 40M entries (talk);
    - 100+ node types and 130+ edge types (podcast);
    - 24M nodes, 80M edges, 86 node types and 117 edge types from 30+ systems (Aug 2026 post).
  - The grounding claim: grounded, an agent found the right table in 38 s; ungrounded, it ran 20 minutes and was wrong. "An ungrounded agent fails slowly rather than cheaply."
  - Who built it: the production graph platform team.
  - Sources: talk 08:37-09:41; podcast 38:46-41:53; [efficient factory](../../research/sources/uber-efficient-software-factory.md).
- **Specs are tracked artifacts that the graph ingests.**
  - The PRD/ERD tool (named "U-Plan" in the transcript; job-post snippets say uPlan) puts product and engineering design docs, launch reviews, experiment reviews and production-readiness reviews "in one place". Each has its status, owners and Jira or Linear links, and "all of this data also goes into the graph".
  - Medisetty: "a source of truth system for both humans and agents to know the specs for every project" (podcast 46:48-48:28).
- **Artifacts Cortana produces** in the demo: research answers, requirements, Figma mock-ups and a code-change analysis. Where they are stored is not shown.
- **Persona memory** is the persona's custom skills and prompt plus the channel. No per-user memory is described.

## Agent interface

- **Chat-native first, with a web view for longer work and a CLI.** Tag Cortana in Slack; "open Cortana into a web interface" for the research and design steps (talk 12:15). Personas are configured per team channel.
- Engineers' own coding stays in vendor harnesses through AIFX. Background coding goes to Minion's web, Slack and CLI.

## Trust and privacy defaults

- **Permissions:** the user's existing permissions are carried forward, so there is no new privileged view.
- **Model calls:** no PII leaves for a vendor by default, through the gateway's anonymiser.
- **Visibility:** persona channels make answers visible to the team.
- **Not described:** session visibility outside Slack; retention; whether others can see a user's web sessions.

## Adoption

- **Spread was organic, from a single engineer.** Usage followed the demand the traces showed (podcast 37:45). In "the last one month" before the talk there were "300 unique personas created and more than 20,000 sessions per day" (talk 11:19).
- **The platform's adoption was pushed through defaults:**
  - auto-installed skills and default plugins by persona;
  - AIFX preinstalled on DevPods;
  - no setup for Cortana itself.
- **Enablement by embedding.** Uber's Agentic Pods put about 30 engineers with business functions for two weeks each ([CTO post](../../research/sources/x-praveen-uber-agentic-pods.md)). Chada said top-down mandates work less well than peers sharing wins ([Summit](../../research/sources/pragmatic-summit-uber-leading-engineering-agentic-shift.md)).
- **A complication: ChatGPT Work.** On 22 Oct 2026 Uber rolled out OpenAI's ChatGPT Work to more than 30,000 employees, up from a 1,000-person pilot. It connects to Drive, Gmail, Calendar and Slack and is backed by the internal skills library; developers stay on Codex ([Uber](../../research/sources/uber-chatgpt-work-rollout.md); [The Next Web](../../research/sources/thenextweb-uber-chatgpt-work-30000.md)). So Uber buys the general employee assistant and builds the engineering and org-knowledge layer. How Cortana and ChatGPT Work divide non-engineers' questions is not stated.

## Outcomes, with evidence labels

| Claim | Number | Date | Who said it | Evidence |
|---|---|---|---|---|
| Cortana personas created | 300 in "the last one month" | Aug 2026 talk | Medisetty | first-party ([talk](../../research/sources/ai-engineer-uber-software-factory-building-blocks.md)) |
| Cortana sessions | 20,000+ a day | Aug 2026 talk | Medisetty | first-party; "session" not defined |
| Cortana's quality, cost or time saved | none published | — | — | — |
| Context-graph grounding | right table in 38 s vs 20 min and wrong | Aug 2026 | Uber blog | first-party, single example ([efficient factory](../../research/sources/uber-efficient-software-factory.md)) |
| "Massive improvement in tokens, turns and latency" with the graph | not quantified | Aug 2026 talk | Medisetty | first-party |
| PRs by local or cloud agents | 70%+ | Aug 2026 | talk, blog, CTO on X | first-party ([efficient factory](../../research/sources/uber-efficient-software-factory.md)) |
| PRs opened by agents | 11% | Mar 2026 | Summit talk via The Pragmatic Engineer | first-party relayed by an independent source ([PE](../../research/sources/pragmatic-engineer-how-uber-uses-ai-for-development.md)) |
| Minion's share of PRs | 11% of merged (May); ~15% of production (Oct) | 2026 | Uber speakers | first-party ([Minion session](../../research/sources/background-agents-summit-uber-minion-ramakrishnan.md); [podcast](../../research/sources/pragmatic-engineer-ubers-ai-infra-from-the-inside.md)) |
| Lines of code per engineer | 2x year on year | Aug 2026 talk | Medisetty | first-party |
| Weekly active users of agentic tools | 7x, Feb–Aug 2026 | Aug 2026 | Uber blog | first-party |
| Skill executions | 20,000+/day (talk); ~30,000/day (podcast, blog) | Aug–Oct 2026 | Uber | first-party |
| AI cost | up at least 6x since 2024 | Mar 2026 | Chada | first-party |
| Cost per session | down 52% from June peak | Aug 2026 | Uber blog | first-party |
| Feature vs maintenance PRs | feature share up, maintenance share down; no figures | Oct 2026 | Medisetty | first-party |
| Link from AI to more useful features | "not there yet" | May 2026 | Uber's COO, via Fortune | independent ([Fortune](../../research/sources/fortune-uber-coo-ai-spending-claude-code.md)) |
| Genie (predecessor shape) | 70k+ questions, 48.9% helpful, ~13k hours saved | Oct 2024 | Uber blog | first-party ([Genie](../../research/sources/uber-genie-on-call-copilot.md)) |

**Reading.** Every Cortana number is an activity count from one talk; none measures quality, time saved or business effect. The 70% and 15% figures measure different things (any agent involvement vs Minion-authored), and the context-graph sizes differ across three first-party sources.

## What bears on intent shaping, dependency management and spec-driven development

The overarching goal for the shaping and dependency agents is faster, lower-effort, higher-quality intent, compatible with spec-driven development. Uber bears on it as follows.

1. **The chain is shown end to end, in one assistant.** Idea, research, requirements, mock-ups and code-change analysis happen in Cortana, then go to a coding agent. That is the opportunity-to-code chain run by one agent, with the claim that alignment that "could take weeks" is compressed (talk 13:05). No measure backs the claim.
2. **The spec has a tracked, graph-indexed home.** uPlan plus the context graph is the closest public case to "specs as records with owners, status and links to execution, readable by agents". It is a strong precedent for SDD inputs that live outside one repo.
3. **A readiness check exists, separate from authoring.** The PRD Evaluator classifies a PRD, sets review depth, scores readiness and names the first fix, but never approves. That is a gate-judge split for intent ([PRD Evaluator](../../research/sources/uber-first-pass-prd-reviewer.md)).
4. **The joins are missing in the record.** No source says Cortana's drafts go into uPlan, or through the Evaluator, before Minion builds. Shaping (Cortana), gating (Evaluator), recording (uPlan) and building (Minion) are separately documented, but the seam between them is not.
5. **Dependency knowledge is graph-native.** Ownership, service dependencies, patterns and incidents come from one graph rather than 20-30 systems with their own skills. "Who owns it, what are the dependencies" was the first problem the graph solved (talk 08:37). That matches the dependency agent's discovery-and-mapping core.
6. **Broken traceability had to be rebuilt by AI.** Uber had to cluster and back-fill missing PRD → ERD → task links before it could measure P50 feature time and find whether the bottleneck is in the PRD, launch or rollout phase (podcast 1:24:05). That is evidence for the write-back half of the map-ask-record loop.
7. **The bottleneck has moved to "should we build it".** Huda names decision-making and experiment capacity as the new limits (talk 17:40). That is the shaping workstream's ground.

## Compared with Stripe Kai and Shopify River

| | Uber Cortana | Stripe Kai | Shopify River |
|---|---|---|---|
| Unit | one company assistant plus team personas | one company agent service plus projects | one company agent through Slack |
| Grounding | company context graph (default) | Hubble data, docs, Toolshed | Aquifer, World |
| Sharing | team Slack channels | single-user sessions (sharing on the roadmap) | public by default |
| Identity | the user's permissions; actor-chain tokens platform-wide | the user's | not detailed |
| Shaping to code | Cortana → Minion, documented, mechanism unknown | Kai → Orbit not documented | not detailed |
| Spec home | uPlan, indexed in the graph | Google Docs PRDs, GitHub spec issues | not detailed |

Sources: this teardown; [Stripe](../competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md); [Shopify](../competitive-teardown-shopify-river/00-teardown-summary.md).

## Pattern classes

Placed in the revised classes P1–P11 of the [taxonomy synthesis, B.2](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#b2-pattern-classes). Fit is marked clear, partial or contested; evidence is first-party unless noted.

| System | Class | Fit | Why |
|---|---|---|---|
| **Cortana** | **P5b** company agent service | **clear** | One hosted assistant for anyone, reached through Slack, web and CLI, with team-level personas and no personal workspace. Same class as Stripe Kai and Shopify River. |
| Cortana personas in team channels | P8b channel-scoped | **partial** | A persona is bound to a team Slack channel where several people work with it. But P8b names "the agent's own identity", and Cortana acts with each user's permissions; how a shared channel's access works is not described. |
| Cortana's loop | P3 own harness | **contested** | No source names the loop. Uber has its own SDKs (LangFx; the early-2025 agent platform), so P3 is likely, but a vendor SDK (P2) can't be ruled out. |
| Cortana → Minion; Slack/DebugAssist → Minion | P6 calling a deployed agent | **partial** | Minion is reached from Slack, web, CLI, API and other agents. Cortana's handoff is documented, but its route is not. |
| Minion on DevPods | P7 background and cloud agents | **clear** | Unattended runs on pre-warmed Kubernetes DevPods with all repos, returning draft PRs (11% of merged PRs in May; ~15% in Oct 2026). |
| AIFX over Claude Code, Codex, OpenCode | P4 meta-harness (in-house governed wrapper) | **clear** on the definition | Centrally managed settings, skills, plugins and spend across three vendor harnesses. The same strain as Airbnb's AirChat: no named P4 sub-shape fits. |
| Engineers in Claude Code, Codex, OpenCode | P1 vendor harness plus skills | **clear** | 84% agentic users in March 2026; Claude Code use 32% → 63% from December to February. |
| Skills marketplace plus AIFX install; MCP gateway | P10 portable skills and plugins | **clear** | A governed registry (lint, automated review, owner-enabled tools) and cross-harness distribution (into AIFX's harnesses, Cortana and the ChatGPT Work skills library). |
| Managed maintenance loops; Shepherd campaigns | P9 workflow engine under agents | **partial** | Scheduled, bounded, rate-limited loops from a managed surface; Shepherd's YAML campaigns. The engine underneath is not named. |
| Uber Agent Builder agents | P3 (no-code on Uber's own agent platform) | **partial** | No-code agents with a registry and Agent Studio; SDK and UI both deploy to Kubernetes. A builder, not a single agent. |
| ChatGPT Work for 30,000+ staff | P11 or a bought P5b | **contested** | A vendor's general assistant connected to Workspace and Slack. It is not built into a system of record, so it fits P11 poorly; nor is it Uber's own service, so it fits P5b poorly either. |

**Counts: 11 placements: 6 clear, 3 partial, 2 contested.**

**Class strains Uber adds.**
1. **P5b with persona-per-channel.** Team personas give P5b a team-level configuration unit that sits between Kai's projects and River's public channels. It may justify a note under P5b, or a P8 sub-type: "channel-scoped persona acting as each user".
2. **P8b's identity clause.** Uber's channel agent acts as each user rather than with its own identity, unlike Claude Tag and Block Buzz. P8b may need to allow either.
3. **Buy-the-general, build-the-specific.** ChatGPT Work beside Cortana is the first case in the library of a company buying a general employee agent while building its own assistant over org knowledge. Neither P5b nor P11 fits the bought half cleanly.

## Options by dimension

Proposals are in options/contributions/competitive-teardown-uber-cortana.md, by slug:
- `intent-shaping-and-spec`
- `artifact-and-project-structure`
- `context-and-memory`
- `dependency-knowledge-and-intake`
- `work-structure`
- `session-persistence-sharing`
- `agent-identity-delegation`
- `governance-control-plane`
- `harness-layering`
- `capability-distribution-trust`
- `review-and-autonomy`
- `target-outcome`
- `adoption-model`
- `build-vs-buy` (as a key question under `target-user` and `harness-layering`; no new dimension proposed)

## Could not verify

- **Cortana's internals:** loop, framework, model, runtime location, session model, memory and cost per query. Nothing is published.
- **The Cortana → Minion handoff mechanism:** what crosses and in what form.
- **uPlan's link to Cortana and the PRD Evaluator.** uPlan is named once in an auto-generated transcript and in job-post snippets whose originals return 404. DebugAssist appears only in the podcast.
- **"Back in December".** The year is inferred as 2025. One derivative source (BigGo) says 2024, which looks like its own error.
- **Persona mechanics:** storage, versioning, and whether personas are Agent Builder agents or registered agents with their own identity.
- **Genie's status** beside Cortana, and the split between Cortana and ChatGPT Work.
- **Figures that conflict:**
  - context-graph size: three different counts;
  - MCP tools and servers: 1,000+ tools vs 800+ servers and 5,000+ tools;
  - skills: 2,500 vs 3,600+;
  - Minion's PR share: 11% vs 15%.
- **Not reached:**
  - LinkedIn and X posts by Uber staff about Cortana (LinkedIn needs sign-in; no post IDs were found);
  - The Pragmatic Engineer deepdive past its paywall;
  - OpenAI's Uber page (HTTP 403);
  - YouTube captions for the uReview talk (rate-limited).
- **Transcripts:** the talk (YouTube auto-captions) and podcast (publisher auto-transcript) contain garbled names.
