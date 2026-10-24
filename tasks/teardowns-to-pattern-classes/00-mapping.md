# Teardowns mapped to the runtime pattern classes P1-P10

Date: 2026-10-24. Task: [teardowns-to-pattern-classes](../teardowns-to-pattern-classes.md). Worker draft for review. The classes are those of [B.2 in the taxonomy synthesis](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#b2-pattern-classes); B.1 (axes) and B.3 (how classes combine) were read with them. This file maps; it does not change the classes. Where a teardown strains a class definition, the strain is reported in [section 6](#6-class-definitions-the-teardowns-strain).

**Sources read.**
- Ramp: [00-teardown-summary.md](../competitive-teardown-ramp-glass/00-teardown-summary.md), [07-pdlc-agent-ecosystem-map.md](../competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md), [audit-2026-10-24.md](../competitive-teardown-ramp-glass/audit-2026-10-24.md).
- Shopify: [00-teardown-summary.md](../competitive-teardown-shopify-river/00-teardown-summary.md), [01-pdlc-agent-ecosystem-map.md](../competitive-teardown-shopify-river/01-pdlc-agent-ecosystem-map.md).
- Stripe: [00-teardown-summary.md](../competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md), [02-pdlc-agent-ecosystem-map.md](../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md).
- Anthropic: [00-summary.md](../research-claude-resources-articles/00-summary.md), [02-pdlc-agent-ecosystem-map.md](../research-claude-resources-articles/02-pdlc-agent-ecosystem-map.md).
- Atlassian: [01-pdlc-agent-ecosystem-map.md](../user-story-mapping/01-pdlc-agent-ecosystem-map.md), [research-atlassian-sdlc-agents.md](../user-story-mapping/research-atlassian-sdlc-agents.md), [research-artifacts-platforms.md](../user-story-mapping/research-artifacts-platforms.md), [research-artifacts-standardization.md](../user-story-mapping/research-artifacts-standardization.md).
- Intercom: [04-pdlc-agent-ecosystem-map.md](../research-pm-agents-jobs-to-be-done/04-pdlc-agent-ecosystem-map.md).
- Cross-ecosystem: [README.md](../pdlc-cross-ecosystem-map/README.md) and [index.html](../pdlc-cross-ecosystem-map/index.html) (read as text). It adds no agent beyond the six maps, so it is used only for evidence counts.
- Block: [follow-up 3 (open harnesses)](../research-agent-runtime-patterns-taxonomy/followup-3-open-harnesses.md) and the Goose notes it cites.
- The source notes in `research/sources/` that these files cite: 95 are linked below, and each was opened to confirm its placement. The architecture claims were checked against the notes, not only the teardown text.
- Airbnb, Spotify, Block: their task folders hold no finished summary yet (`research-airbnb-spotify-product-practices/` has only `mapkit.py`; `research-block-product-practices/` is empty). See [section 7](#7-gaps-and-caveats).

**How to read this.**
- **One agent can sit in several classes.** Each placement is one row: one agent, one class. Most systems take two to four rows, as B.3 expects (Glass is in five).
- **Fit**:
  - **clear**: the agent meets the class definition as B.2 writes it;
  - **partial**: it meets part of the definition, or the evidence covers only part of it (the reason is given);
  - **contested**: the sources, or B.2/B.3 and a newer source, point to different classes.
- **Evidence** is the `evidence` field in the note's frontmatter: first-party, vendor-claim, independent or anecdote. Fit and evidence are separate. An agent can fit clearly on vendor-claim evidence only.
- **Dates matter.** Ramp changed Glass's class within six months. Rows carry a date where the source does.
- **Links.** Source notes are `../../research/sources/<slug>.md`. "Teardown" links go to the teardown or map file the placement comes from.

---

## 1. Ecosystem × class matrix

Cells name the agents in the class, marked **(c)** clear, **(p)** partial, **(x)** contested. A blank cell means no placement.

| Ecosystem | P1 vendor harness + skills | P2 vendor SDK embedded | P3 own harness | P4 meta-harness | P5 org-deployed workspace | P6 harness calls deployed agent | P7 background / cloud | P8 shared sessions | P9 workflow engine | P10 skill ecosystem |
|---|---|---|---|---|---|---|---|---|---|---|
| **Ramp** | | Glass, Apr 2026 (c) | Glass on Laminar (c); Laminar (c); Inspect (p) | OCA (p) | Glass (x) | OCA → Inspect (p) | Glass (c); Inspect (c) | Glass (c); Inspect (c); Ramp Research (p) | Laminar (p); OCA (p) | Dojo (p); tool catalog (p) |
| **Shopify** | engineers' local tools (c) | Roast (p) | River on Aquifer (c); "Vanilla" pi profile (x) | | Aquifer (p) | PR-review profile (p) | River (c) | River (c) | Dispatch (c); Roast (c); Helix (p) | profiles and World skills (p) |
| **Stripe** | Claude Code, Cursor and others (c); Protodash (p) | | Kai (c); Minions (c) | Kai projects (p) | Kai (p) | Orbit → Minions (p); Harbor over MCP (p) | Minions (c) | Minions (p); Orbit (p) | Minions (c); compliance agents (c); payment-method factory (c) | Kai skills and Agent Studio (p); Toolshed (p); shared rule files (p) |
| **Anthropic** | Claude Code (c); Cowork and plugins (c); SDLC playbook (p) | | | Managed Agents (x) | | Code Review (c); Sentry Seer (p) | Cowork and Code cloud sessions (c); Managed Agents (c); ABC Legal fleet (c); Claude Tag on-call (p) | Claude Tag (c) | Claude Code team review stack (p) | org plugin marketplace and skill sync (c) |
| **Atlassian** | | | | work-item dispatch to several agents (x) | | Rovo A2A gateway (c); Rovo MCP server (p); Rovo Dev reviewer (p); Rovo Dev in Pipelines (p) | Jira Coding Agent (c); third-party agents from a work item (c) | | Jira automation triggers (p) | |
| **Intercom** | Claude Code + plugins + hooks (c) | | | | | Shrek reviewers (c) | CI-watching agent (p); Buzz (p) | | | plugin marketplace (p) |
| **Block** *(placeholder; filed notes only)* | Goose company-wide (p) | | Goose (c) | | | | background agents (p) | | | Goose skills (p) |
| **Spotify** *(placeholder; provisional)* | | Honk (p) | | | | Vedder (p) | Honk (p) | | | |
| **Airbnb** *(placeholder)* | | | | | | | | | | |

**What the matrix shows.**
- **Densest:** P7, P8 and P9 are where the teardowns put most weight. Every ecosystem with a full teardown has a P7 placement.
- **Clear cases by class:** P2 has one clear case, and it is historical (Glass in April 2026). P4 and P5 have none; every placement there is partial or contested.
- **Own harness:** the three companies with the strongest first-party architecture posts (Ramp, Shopify, Stripe) all own their loop (P3). Each also has P9-style deterministic orchestration around narrow jobs.

**Counts: 78 placements: 34 clear, 40 partial, 4 contested.**

| Ecosystem | clear | partial | contested | total |
|---|---|---|---|---|
| Ramp | 7 | 8 | 1 | 16 |
| Shopify | 6 | 5 | 1 | 12 |
| Stripe | 7 | 10 | 0 | 17 |
| Anthropic | 8 | 4 | 1 | 13 |
| Atlassian | 3 | 4 | 1 | 8 |
| Intercom | 2 | 3 | 0 | 5 |
| Block (placeholder) | 1 | 3 | 0 | 4 |
| Spotify (placeholder) | 0 | 3 | 0 | 3 |
| Airbnb (placeholder) | 0 | 0 | 0 | 0 |

---

## 2. Detail per ecosystem

### 2.1 Ramp

Teardown: [summary](../competitive-teardown-ramp-glass/00-teardown-summary.md), [lifecycle map](../competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md), [audit](../competitive-teardown-ramp-glass/audit-2026-10-24.md). Every outcome figure is Ramp's own. The architecture posts (Buchan in April, Kronick in October) are the high-signal sources.

**The Glass question, answered from the sources.**
- **April 2026: P2.** Charles calls Glass "our own version of Claude Code's Cowork" built on Anthropic's Claude Agent SDK.
- **October 2026: P3.** Kronick's Laminar post says Glass now runs on Laminar, Ramp's own provider-agnostic harness. Ramp tried vendor SDKs and managed-agent APIs, then built its own.
- **The New Stack** is independent but rests on the Ramp post.
- **So "P2 and/or P3" resolves to P2 then P3, in sequence.** The October form also matches the P5 definition, which B.3 does not consider (row R3).

| # | Agent or product | Class | Why it fits | Sources | Evidence | Fit |
|---|---|---|---|---|---|---|
| R1 | Glass (April 2026 form) | P2 | Anthropic's Agent SDK ran inside a desktop app Ramp owned. Ramp supplied Okta SSO, an MCP proxy, memory, Dojo skills and cost metering. | [x-geoffintech-ai-pilled-article](../../research/sources/x-geoffintech-ai-pilled-article.md); [x-sebgoddijn-glass-article](../../research/sources/x-sebgoddijn-glass-article.md); [x-shanebuchan-how-we-built-glass](../../research/sources/x-shanebuchan-how-we-built-glass.md); [teardown](../competitive-teardown-ramp-glass/00-teardown-summary.md) | first-party | clear (historical: superseded by Laminar by October 2026) |
| R2 | Glass on Laminar (October 2026) | P3 | Ramp owns the loop: a provider-agnostic harness built in house from about May 2026 after vendor SDKs and managed-agent APIs were tried. Glass is one of its products. | [ramp-builders-building-laminar](../../research/sources/ramp-builders-building-laminar.md); [thenewstack-ramp-laminar-agent-harness](../../research/sources/thenewstack-ramp-laminar-agent-harness.md); [teardown](../competitive-teardown-ramp-glass/00-teardown-summary.md) | first-party; independent (relies on Ramp's post) | clear |
| R3 | Glass (October form) | P5 | An org-deployed, always-on workspace for every employee, with a platform-native agent, central connectors, SSO and a per-project cost meter. That is the P5 definition. B.3 instead reads Glass as P2+P8+P10+P7. | [ramp-builders-building-laminar](../../research/sources/ramp-builders-building-laminar.md); [x-eglyman-introducing-glass-learn-things-once](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md); [teardown](../competitive-teardown-ramp-glass/00-teardown-summary.md) | first-party; vendor-claim | contested: B.3 places Glass elsewhere. P5's only example (Cloudflare OS) adds per-user apps and zero ambient access, which Glass sources do not describe. |
| R4 | Glass | P8 | Sessions can be shared: a support agent hands a session to an engineer who "jumps in, sees everything". Laminar lists multiplayer sessions and Slack integration as core features. | [x-eglyman-introducing-glass-learn-things-once](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md); [ramp-introducing-glass](../../research/sources/ramp-introducing-glass.md); [ramp-builders-building-laminar](../../research/sources/ramp-builders-building-laminar.md); [map](../competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md) | vendor-claim; first-party | clear (private by default, shared on demand) |
| R5 | Glass | P7 | Async agents run on "a fleet of generic disposable workers" and take "minutes or hours". Sessions survive the laptop sleeping. The April form ran headless with phone approvals on the user's laptop. | [ramp-builders-building-laminar](../../research/sources/ramp-builders-building-laminar.md); [x-sebgoddijn-glass-article](../../research/sources/x-sebgoddijn-glass-article.md); [teardown](../competitive-teardown-ramp-glass/00-teardown-summary.md) | first-party | clear for October; the April laptop-as-server form was only a partial fit |
| R6 | Dojo (Glass skills marketplace) | P10 | A Git-backed, versioned, reviewed marketplace of markdown skills (350+), with a recommender. It is a registry, but no source says it serves any harness other than Glass. | [x-sebgoddijn-glass-article](../../research/sources/x-sebgoddijn-glass-article.md); [x-shanebuchan-how-we-built-glass](../../research/sources/x-shanebuchan-how-we-built-glass.md); [teardown](../competitive-teardown-ramp-glass/00-teardown-summary.md) | first-party | partial: registry and review yes; harness-neutral distribution not shown (B.2 lists Dojo under P10 regardless) |
| R7 | Laminar (platform under Glass, Inspect, Stack, support and OCR agents) | P3 | An own harness with 15 named responsibilities, on FastAPI, Temporal, Postgres and S3. Session state is decoupled from sandboxes, and models are reached through Ramp Router. | [ramp-builders-building-laminar](../../research/sources/ramp-builders-building-laminar.md); [thenewstack-ramp-laminar-agent-harness](../../research/sources/thenewstack-ramp-laminar-agent-harness.md); [map](../competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md) | first-party; independent | clear |
| R8 | Laminar | P9 | Temporal provides durable orchestration under the agents. No deterministic step graph around agent steps is described. | [ramp-builders-building-laminar](../../research/sources/ramp-builders-building-laminar.md) | first-party | partial: durable execution yes; the "deterministic steps and agent steps in one graph" half is not described |
| R9 | Inspect (background coding agent) | P7 | A whole coding task runs in a Modal sandbox per session and returns a PR under the requester's identity. Sessions are started from Slack, web, a Chrome extension, PR comments, and increasingly by automations. | [ramp-builders-why-we-built-background-agent](../../research/sources/ramp-builders-why-we-built-background-agent.md); [modal-ramp-inspect-background-agent](../../research/sources/modal-ramp-inspect-background-agent.md); [claude-customers-ramp-office-hours](../../research/sources/claude-customers-ramp-office-hours.md); [map](../competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md) | first-party; vendor-claim | clear |
| R10 | Inspect | P8 | "Every session is multiplayer": prompts are attributed per person, state syncs across clients, and each session has its own Durable Object and SQLite store. B.2 already lists it. | [ramp-builders-why-we-built-background-agent](../../research/sources/ramp-builders-why-we-built-background-agent.md); [modal-ramp-inspect-background-agent](../../research/sources/modal-ramp-inspect-background-agent.md); [wavect-ramp-inspect-architecture](../../research/sources/wavect-ramp-inspect-architecture.md) | first-party; vendor-claim; independent (critique, not evidence of deployment) | clear |
| R11 | Inspect | P3 | Ramp "built our own background agent" with OpenCode as the agent loop inside its own sandbox, clients and control plane. Since October it runs on Laminar. | [ramp-builders-why-we-built-background-agent](../../research/sources/ramp-builders-why-we-built-background-agent.md); [modal-ramp-inspect-background-agent](../../research/sources/modal-ramp-inspect-background-agent.md); [ramp-builders-building-laminar](../../research/sources/ramp-builders-building-laminar.md) | first-party; vendor-claim | partial: OpenCode is used, not stated as forked, so this sits on the P2/P3 line (see section 6) |
| R12 | OCA (on-call assistant) | P4 | A Temporal-orchestrated agent that runs inside Claude Code for Anthropic models and Codex for OpenAI models, switching with the model. That is a light layer delegating the loop to whichever vendor harness fits (B.2's "DIY coordinator" sub-shape). | [ramp-builders-how-we-built-oca](../../research/sources/ramp-builders-how-we-built-oca.md); [claude-customers-ramp-office-hours](../../research/sources/claude-customers-ramp-office-hours.md) | first-party; vendor-claim | partial: one agent, not a layer serving many; no sharing or policy plane |
| R13 | OCA | P9 | Temporal orchestration around an incident investigation, with fixed reporting points (about 5 and 13 minutes) and hook "detours" that force self-checks. | [ramp-builders-how-we-built-oca](../../research/sources/ramp-builders-how-we-built-oca.md) | first-party | partial: the engine and checkpoints are there; the graph of steps is not described |
| R14 | OCA → Inspect | P6 | OCA "asks Inspect to prepare a PR for human review": one agent reaches a deployed task agent. | [ramp-builders-how-we-built-oca](../../research/sources/ramp-builders-how-we-built-oca.md); [map](../competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md) | first-party | partial: the caller is an agent, not a general harness; the route (API or other) is not described |
| R15 | Ramp Research (Slack data agent) | P8 | Stateful Slack threads in which users clarify and collaborate, with CSV previews, added to alert and project channels. It is a chat-native shared agent, and it is also a connected tool inside Glass. | [ramp-builders-meet-ramp-research](../../research/sources/ramp-builders-meet-ramp-research.md); [x-sebgoddijn-glass-article](../../research/sources/x-sebgoddijn-glass-article.md) | first-party | partial: runtime, loop and persistence model not described; figures date from Aug-Sep 2025 |
| R16 | Shared tool catalog ("many hundreds" of tools) | P10 | One catalog shared across all of Ramp's agents and built with product teams: a central capability layer. | [pragmatic-engineer-ramp-lessons-new-ai-product](../../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md); [map](../competitive-teardown-ramp-glass/07-pdlc-agent-ecosystem-map.md) | first-party (ASR captions) | partial: tools, not skills; the format and registry checks are not described |

**Fits no class (Ramp).**
- **Ramp Router and the per-project meter** are governance and cost controls (axis 7). They are not a runtime pattern.
- **The Glass memory pipeline** (24-hour, files read-only in session) is a context-and-memory choice (D.13). It is not a class.
- **Review Buddy, Testo, Gadget, the customer-insight agent and the "small loops"** appear only in one Charles talk ([lenny-podcast-geoff-charles-product-when-coding-solved](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md), first-party, ASR captions). No runtime is described, so placing them would be invention. One later vendor-claim source says a code-review bot is built on Inspect ([claude-customers-ramp-office-hours](../../research/sources/claude-customers-ramp-office-hours.md)). That would make it P7, but the bot is not named there, so it is not placed.
- **The Policy Agent** is a customer-facing product, not an internal runtime ([ramp-builders-agents-users-can-trust](../../research/sources/ramp-builders-agents-users-can-trust.md)).
- **The Notion custom agents** (Feb 2026, [notion-inside-ramps-custom-agent-os](../../research/sources/notion-inside-ramps-custom-agent-os.md), vendor-claim) are agents hosted inside a SaaS tool. No class covers that (section 6, strain 8).
- **Open-Inspect** is a community reimplementation, not Ramp's code. B.2 already lists it under P8.

### 2.2 Shopify

Teardown: [summary](../competitive-teardown-shopify-river/00-teardown-summary.md), [lifecycle map](../competitive-teardown-shopify-river/01-pdlc-agent-ecosystem-map.md). The architecture is first-party and specific. The independent notes (ZenML, adaptordie, Port, Internal Agents Map) restate Shopify's claims.

| # | Agent or product | Class | Why it fits | Sources | Evidence | Fit |
|---|---|---|---|---|---|---|
| S1 | River on Aquifer | P3 | Shopify runs "its own harness", a disposable loop outside the sandbox, on its own substrate (session, harness, sandbox, gateway, credentials proxy). The design goal is to "swap models, runtimes, even languages". | [shopify-engineering-under-the-river](../../research/sources/shopify-engineering-under-the-river.md); [zenml-llmops-shopify-river-durable-infrastructure](../../research/sources/zenml-llmops-shopify-river-durable-infrastructure.md); [teardown](../competitive-teardown-shopify-river/00-teardown-summary.md) | first-party; independent (restates) | clear |
| S2 | River | P8 | Slack-only, public by default and multiplayer: anyone can join a thread and redirect the work. Sessions are append-only Postgres event logs that rehydrate on any host. Same-thread co-writing grew from 61,680 to 171,853 links (Mar-Sep 2026). | [shopify-engineering-under-the-river](../../research/sources/shopify-engineering-under-the-river.md); [x-tobi-river-floods-shopify-chart](../../research/sources/x-tobi-river-floods-shopify-chart.md); [map](../competitive-teardown-shopify-river/01-pdlc-agent-ecosystem-map.md) | first-party | clear (chat-native, no private mode) |
| S3 | River (automation and job modes; Remote Dev) | P7 | Server-side session cells with no laptop dependency. Automation mode opens its own threads from a security ledger, and overnight mobile bug-fix runs open PRs. Remote Dev claims a warm Mac per session. | [shopify-engineering-river-vulnerability-remediation](../../research/sources/shopify-engineering-river-vulnerability-remediation.md); [shopify-engineering-remote-dev](../../research/sources/shopify-engineering-remote-dev.md); [shopify-engineering-under-the-river](../../research/sources/shopify-engineering-under-the-river.md) | first-party | clear |
| S4 | Aquifer (platform) | P5 | An org-deployed platform with a platform-native agent used by "7,000+ people", governed by a gateway and credentials proxy, with one substrate under many profiles. | [shopify-engineering-under-the-river](../../research/sources/shopify-engineering-under-the-river.md); [port-software-factories-shopify](../../research/sources/port-software-factories-shopify.md); [teardown](../competitive-teardown-shopify-river/00-teardown-summary.md) | first-party; independent (restates) | partial: no per-employee workspace (the surface is Slack); the identity model is not disclosed ([internal-agents-shopify-river](../../research/sources/internal-agents-shopify-river.md): credentials "Not reported") |
| S5 | Profiles (Nix bundles) and skills in the World monorepo | P10 | Capability is packaged as data (prompt, skills, extensions, sandbox policy, model defaults). Skills are files in the monorepo, reused across teams, and distributed through code review and CI. | [shopify-engineering-under-the-river](../../research/sources/shopify-engineering-under-the-river.md); [x-tobi-learning-on-the-shop-floor](../../research/sources/x-tobi-learning-on-the-shop-floor.md); [teardown](../competitive-teardown-shopify-river/00-teardown-summary.md) | first-party | partial: one substrate, not harness-neutral distribution; the skill format is not disclosed |
| S6 | PR-review profile | P6 | Automation mode, "woken by an external system, often no human in the loop": an event-triggered deployed agent. | [shopify-engineering-under-the-river](../../research/sources/shopify-engineering-under-the-river.md); [map](../competitive-teardown-shopify-river/01-pdlc-agent-ecosystem-map.md) | first-party | partial: no general harness is the caller; the trigger is not described beyond "external system" |
| S7 | Dispatch (AppSec scanning) | P9 | A thin Ruby orchestrator with fixed stages (bootstrap, partition, hunt, verify, post-process, report, remediate). Agents fill steps, verification uses a different model, and state lives in a Rails backend. | [shopify-engineering-agentic-harness-outlasts-model](../../research/sources/shopify-engineering-agentic-harness-outlasts-model.md) | first-party | clear |
| S8 | Roast (2025) | P9 | YAML workflows interleave deterministic steps with agent steps, with replay to resume from any step: "Non-determinism is the enemy of reliability". | [shopify-engineering-introducing-roast](../../research/sources/shopify-engineering-introducing-roast.md) | first-party | clear |
| S9 | Roast's CodingAgent step | P2 | Roast embeds Claude Code as a step inside Shopify's own workflow tool. | [shopify-engineering-introducing-roast](../../research/sources/shopify-engineering-introducing-roast.md); [teardown](../competitive-teardown-shopify-river/00-teardown-summary.md) | first-party | partial: a vendor harness embedded as a subprocess, but in a workflow tool, not a product supplying UX, memory and policy |
| S10 | Helix (native-app migration) | P9 | A structured multi-stage harness with checkpoints, where "the reference is the spec". | [shopify-engineering-under-the-river](../../research/sources/shopify-engineering-under-the-river.md); [map](../competitive-teardown-shopify-river/01-pdlc-agent-ecosystem-map.md) | first-party | partial: named in passing; no architecture given |
| S11 | Engineers' local Claude Code, Cursor, Codex, Copilot, Gemini | P1 | "One tool for one job, except for with AI": several general harnesses coexist on one LLM proxy. | [bvp-inside-shopifys-ai-first-engineering-playbook](../../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md); [venturebeat-shopify-ai-stack-model-agnostic](../../research/sources/venturebeat-shopify-ai-stack-model-agnostic.md) | first-party; independent | clear |
| S12 | "Vanilla, the headless 'pi' agent" (Aquifer profile) | P3 | A peer profile on Aquifer. If "pi" is the open-source Pi agent, this is an open harness on Shopify's substrate. | [shopify-engineering-under-the-river](../../research/sources/shopify-engineering-under-the-river.md); [adaptordie-shopify-river-agent-stack](../../research/sources/adaptordie-shopify-river-agent-stack.md) | first-party; independent | contested: Shopify does not say what "pi" is; adaptordie calls it "likely" Pi, by inference |

**Fits no class (Shopify).**
- **Quick** hosts agent-made artifacts; it is not an agent runtime.
- **The internal LLM proxy** is governance and routing.
- **The nightly "dreaming", corpus mining and the Jev classifier** are a learning loop (D.13).
- **GSD** is a human project process.

### 2.3 Stripe

Teardown: [summary](../competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md), [lifecycle map](../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md). The architecture comes from Stripe staff and is specific. The build-speed headline is LangChain's (vendor-claim). The only independent critique is about outcome numbers, not architecture.

| # | Agent or product | Class | Why it fits | Sources | Evidence | Fit |
|---|---|---|---|---|---|---|
| T1 | Kai (Knowledge AI Platform) | P3 | Kai is built on LangChain's open-source Deep Agents harness over LangGraph, plus a Stripe harness layer and a configuration layer. B.2 names LangGraph among P3's frameworks. | [stripe-meet-knowledge-ai-platform](../../research/sources/stripe-meet-knowledge-ai-platform.md); [langchain-how-stripe-built-kai-deep-agents](../../research/sources/langchain-how-stripe-built-kai-deep-agents.md); [teardown](../competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md) | first-party; vendor-claim | clear (the teardown calls it the first production non-coding, multi-user agent on a general framework in the library) |
| T2 | Kai | P5 | A company-wide, always-on agent service on Kubernetes inside Stripe's security boundary. Governance sits in owner-run projects, and many surfaces are views into one service. | [stripe-meet-knowledge-ai-platform](../../research/sources/stripe-meet-knowledge-ai-platform.md); [howiai-stripe-kai-krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md) | first-party (podcast: ASR captions) | partial: sessions are single-user and there is no persistent personal workspace or memory; it is closer to "agent as a service" than to a workspace |
| T3 | Kai skills and Agent Studio | P10 | Skills follow the open spec ("you can use on any of your harnesses"), owned by 100+ teams. Agent Studio is a control plane with usage and quality signals, and telemetry promotes or demotes skills. | [howiai-stripe-kai-krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md); [langchain-how-stripe-built-kai-deep-agents](../../research/sources/langchain-how-stripe-built-kai-deep-agents.md); [stripe-meet-knowledge-ai-platform](../../research/sources/stripe-meet-knowledge-ai-platform.md) | first-party; vendor-claim | partial: portable format claimed, but distribution only into Kai is shown |
| T4 | Kai projects backed by another harness | P4 | A project can be "backed by a different API in the back end and a different harness" while keeping Kai's features. Kai then becomes a front door and governance layer above other loops. | [howiai-stripe-kai-krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md) (31:00); [teardown](../competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md) | first-party (ASR captions) | partial: described, not demoed; no harness named |
| T5 | Minions | P3 | The core loop runs on a fork of Block's Goose, inside Stripe devboxes, with a curated Toolshed subset. B.2's lead P3 example. | [stripe-minions-one-shot-coding-agents](../../research/sources/stripe-minions-one-shot-coding-agents.md); [howiai-stripe-minions-kaliski](../../research/sources/howiai-stripe-minions-kaliski.md) | first-party | clear |
| T6 | Minions | P7 | Unattended one-shot runs on pre-warmed devboxes with no human credentials, started from a Slack emoji. They return a PR and can work "for the next 12 hours". | [stripe-minions-part-2](../../research/sources/stripe-minions-part-2.md); [howiai-stripe-minions-kaliski](../../research/sources/howiai-stripe-minions-kaliski.md); [youtube-notmybusiness-inside-stripe-ships-fast](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) | first-party | clear |
| T7 | Minions | P9 | The orchestration "interleaves agent loops with deterministic code": git, lint and tests are fixed nodes, MCP hydration runs beforehand, and CI is capped at two rounds. | [stripe-minions-one-shot-coding-agents](../../research/sources/stripe-minions-one-shot-coding-agents.md); [stripe-minions-part-2](../../research/sources/stripe-minions-part-2.md) | first-party | clear ("blueprint" is a third-party word, not Stripe's) |
| T8 | Minions (public "robots" channel) | P8 | Runs post to a public Slack channel that 76 people follow to watch and "pair prompt". The engineer can drop into the devbox. | [howiai-stripe-minions-kaliski](../../research/sources/howiai-stripe-minions-kaliski.md) | first-party (ASR captions) | partial: others can watch; joint steering of one session is not documented |
| T9 | Orbit (planning layer) | P8 | "Workspaces share context across sessions, all visible to each other"; teammates comment on a shareable plan. | [youtube-notmybusiness-inside-stripe-ships-fast](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md); [x-stevekaliski-orbit](../../research/sources/x-stevekaliski-orbit.md); [map](../competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md) | first-party (ASR captions; UI tip read from a 360p frame) | partial: one vendor-filmed video and one post; runtime unknown |
| T10 | Orbit → Minions | P6 | A one-button handoff from the planning agent to a deployed coding agent that gets a devbox, the plan and instructions. | [youtube-notmybusiness-inside-stripe-ships-fast](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) | first-party (ASR captions) | partial: the caller is Stripe's own planning tool, not a general harness; the route is not described |
| T11 | Harbor (prototyping agent) | P6 | Harbor's toolset and its Drydock renderer are exposed over Stripe's internal MCP, so Kai and devbox coding agents can create and publish prototypes. | [stripe-harbor-ai-prototyping](../../research/sources/stripe-harbor-ai-prototyping.md) | first-party | partial: other agents reach Harbor's tools and renderer, not the Harbor agent as a whole |
| T12 | Compliance review agents | P9 | The review tooling is the orchestrator: a DAG of quality-tested sub-questions. Agents pre-fetch research, a human answers each question, and every run is logged. | [aws-stripe-compliance-agents](../../research/sources/aws-stripe-compliance-agents.md) | first-party (on an AWS blog) | clear |
| T13 | Payment-method factory | P9 | "Predictable coordination is better implemented in code": ordered generators, one PR per step, and learning and decision logs that harden prompts. | [stripe-payment-method-factory](../../research/sources/stripe-payment-method-factory.md) | first-party | clear |
| T14 | Toolshed (central MCP server) | P10 | About 500 MCP tools, extended by owning teams and used by "hundreds of different agents" (Kai, Minions, Orbit). MCP servers are one of P10's harness-neutral assets. | [stripe-minions-part-2](../../research/sources/stripe-minions-part-2.md); [latentspace-emily-sands-stripe](../../research/sources/latentspace-emily-sands-stripe.md) | first-party | partial: a centrally hosted tool server, not a registry that validates and distributes packages |
| T15 | Agent rule files shared by Minions, Cursor and Claude Code | P10 | Minions "read the same agent rule files as Cursor and Claude Code", applied by subdirectory: one capability asset read by three harnesses. | [stripe-minions-one-shot-coding-agents](../../research/sources/stripe-minions-one-shot-coding-agents.md) | first-party | partial: cross-harness assets yes; no registry or distribution layer |
| T16 | Claude Code, Cursor and four other assistants | P1 | General harnesses on every laptop and devbox, pre-configured, with "no singular tool to rule them all". | [howiai-stripe-minions-kaliski](../../research/sources/howiai-stripe-minions-kaliski.md); [claude-customers-stripe-claude-code-rollout](../../research/sources/claude-customers-stripe-claude-code-rollout.md) | first-party; vendor-claim | clear |
| T17 | Protodash (prototyping kit) | P1 | Version 1 was "a bundle of cursor rules" plus the Sail MCP server: capability added to a general harness. A later in-browser studio runs on devboxes. | [howiai-stripe-protodash-owen-williams](../../research/sources/howiai-stripe-protodash-owen-williams.md) | first-party (ASR captions) | partial: the studio's own agent runtime is not described |

**Fits no class (Stripe).**
- **Gru** (code review) is known only from captions in one video. Its mechanism is unknown.
- **Trailhead** (owner-verified docs) and **Compass** (project tracking) are context and records, not runtimes.
- **The LLM Proxy** is governance.
- **GoLLM, LibreChat, Hubert and the NoCode Agent Builder** are historical, pre-Kai.
- **Kai is explicitly not P8.** Sessions are single-user, and Stripe calls sharing roadmap ([stripe-meet-knowledge-ai-platform](../../research/sources/stripe-meet-knowledge-ai-platform.md)).

### 2.4 Anthropic

Teardown: [summary](../research-claude-resources-articles/00-summary.md), [lifecycle map](../research-claude-resources-articles/02-pdlc-agent-ecosystem-map.md).
- **First-party throughout.** Anthropic describes its own products and teams. Customer stories on claude.com are labelled vendor-claim.
- **One AI lab, unusually resourced.** The lab's users are its own builders.
- **Prescription is kept apart from practice.** The map keeps the AI-native SDLC playbook (a prescription for customers) separate from evidence of internal practice, and so does this table.

| # | Agent or product | Class | Why it fits | Sources | Evidence | Fit |
|---|---|---|---|---|---|---|
| A1 | Claude Code (internal use) | P1 | Parallel sessions, plan mode, skills, hooks, CLAUDE.md and REVIEW.md: users work directly in the vendor harness and add structure on demand. | [lenny-podcast-boris-cherny-after-coding](../../research/sources/lenny-podcast-boris-cherny-after-coding.md); [claude-dev-claude-code-team-code-review](../../research/sources/claude-dev-claude-code-team-code-review.md); [map](../research-claude-resources-articles/02-pdlc-agent-ecosystem-map.md) | first-party | clear |
| A2 | Cowork with department plugins | P1 | Non-engineers use the vendor harness with stacked plugins (skills, subagents, MCP connectors), on a five-level maturity ladder. | [claude-guide-deploying-cowork-across-org](../../research/sources/claude-guide-deploying-cowork-across-org.md); [claude-customers-cyera-cowork-front-door](../../research/sources/claude-customers-cyera-cowork-front-door.md) | first-party; vendor-claim | clear |
| A3 | Org plugin marketplace and skill sync to every surface | P10 | Admin-provisioned department plugin marketplaces. The data team's skills sync on merge to a plugin marketplace, cloud-storage blobs and MCP resources, reaching IDEs, hosted apps and Slack. | [claude-guide-deploying-cowork-across-org](../../research/sources/claude-guide-deploying-cowork-across-org.md); [claude-anthropic-self-service-analytics](../../research/sources/claude-anthropic-self-service-analytics.md); [summary](../research-claude-resources-articles/00-summary.md) | first-party | clear (all surfaces are Anthropic's, but MCP resources make one route harness-neutral) |
| A4 | Claude Tag (channel agent) | P8 | A shared agent resident in Slack channels, with channel memory and its own identity per channel. Several engineers steer one investigation "in multi-player mode". Personal connectors add on-behalf-of reads. | [claude-agent-identity-access-model](../../research/sources/claude-agent-identity-access-model.md); [claude-tag-ci-cd-first-responder](../../research/sources/claude-tag-ci-cd-first-responder.md); [claude-tag-personal-connectors](../../research/sources/claude-tag-personal-connectors.md); [tenable-claude-tag-slack-access-model](../../research/sources/tenable-claude-tag-slack-access-model.md) | first-party; independent (Tenable, on the access model) | clear |
| A5 | Claude Tag as CI first responder, per-component "superfans", alert agent | P7 | Agents watch alerts and CI unattended, root-cause, write the post-mortem and the fix as a PR. They cannot deploy, and one Tag session ran for months. | [claude-tag-ci-cd-first-responder](../../research/sources/claude-tag-ci-cd-first-responder.md); [claude-securing-ai-native-sdlc-at-anthropic](../../research/sources/claude-securing-ai-native-sdlc-at-anthropic.md); [anthropic-redesigning-source-control-scion](../../research/sources/anthropic-redesigning-source-control-scion.md) | first-party | partial: event-started and channel-resident, not a task a person hands off; it sits between P7 and P8 |
| A6 | Cowork on web and mobile; Claude Code cloud project threads | P7 | Sessions and scheduled tasks run "with no device online". Project threads are full cloud Claude Code sessions on their own branches, steerable from a phone. | [claude-cowork-web-mobile-handoff](../../research/sources/claude-cowork-web-mobile-handoff.md); [claude-code-projects-redesigned](../../research/sources/claude-code-projects-redesigned.md) | first-party | clear (single owner, so not P8; beta) |
| A7 | Code Review (managed multi-agent PR review) | P6 | On PR open, a GitHub App starts parallel agents that find, verify and rank bugs. It is a deployed agent reached by the CI route, and it never approves. | [claude-code-review-ga](../../research/sources/claude-code-review-ga.md); [claude-dev-claude-code-team-code-review](../../research/sources/claude-dev-claude-code-team-code-review.md) | first-party | clear (B.2 lists the GitHub Action form under P6) |
| A8 | Claude Code team's review and release stack | P9 | Seven fixed layers (self-verification, AI review, blocking security review, CI, risk-tiered approval set by classifiers, merge queue and flags, rollback), with agents filling steps. | [claude-dev-claude-code-team-code-review](../../research/sources/claude-dev-claude-code-team-code-review.md); [claude-securing-ai-native-sdlc-at-anthropic](../../research/sources/claude-securing-ai-native-sdlc-at-anthropic.md) | first-party | partial: a CI pipeline with fixed gates, not a workflow engine with checkpoints |
| A9 | Claude Managed Agents | P4 | B.2 lists it as P4's "model vendor's hosted service" sub-shape, on Anthropic's own "meta-harness" label: a durable session log, a stateless harness and a credential vault. | [claude-managed-agents-dreaming-outcomes](../../research/sources/claude-managed-agents-dreaming-outcomes.md); [summary](../research-claude-resources-articles/00-summary.md) | first-party | contested: P4's definition is a layer above several vendors' harnesses, and Managed Agents hosts one vendor's loop. It fits P7 better (A10). |
| A10 | Claude Managed Agents (dreaming, outcomes, multiagent orchestration) | P7 | A hosted runtime for long-running agents. A lead agent splits work to specialists on a shared filesystem, with scheduled memory "dreaming" and rubric grading. | [claude-managed-agents-dreaming-outcomes](../../research/sources/claude-managed-agents-dreaming-outcomes.md) | first-party (customer results within it are customers' claims) | clear |
| A11 | ABC Legal agent fleet on Managed Agents | P7 | 50+ employee-built single-job agents moved off desktops to a hosted runtime, run by cron through Bitbucket Pipelines. Every agent is config in git, changed by an approved PR. | [claude-abc-legal-managed-agents-builders](../../research/sources/claude-abc-legal-managed-agents-builders.md) | vendor-claim | clear (fit); evidence is the customer's claims, published by Anthropic |
| A12 | Sentry Seer handing root cause to a coding agent on Managed Agents | P6 | A product reaches a deployed coding agent that plans, implements and opens a PR. | [claude-customers-sentry-bug-fixing-agents](../../research/sources/claude-customers-sentry-bug-fixing-agents.md) | vendor-claim | partial: the caller is a product, not a general harness (B.2 already lists Sentry's MCP route under P6) |
| A13 | AI-native SDLC playbook (intent.md → spec.md → plan.md chain) | P1 | Structure added to the general harness: skills as advisory policy, hooks as gates, `claude -p` jobs triggered by merges, evals on the agent's configuration. | [claude-ai-native-sdlc-playbook](../../research/sources/claude-ai-native-sdlc-playbook.md); [map](../research-claude-resources-articles/02-pdlc-agent-ecosystem-map.md) | first-party | partial: a prescription for customers; no Anthropic team is shown using the chain |

**Fits no class (Anthropic).**
- **The apps gateway** ([claude-apps-gateway](../../research/sources/claude-apps-gateway.md)) is a self-hosted control plane for one harness: governance (axis 7), not a layer above several harnesses.
- **Claude Design** ([claude-design-designer-workflow](../../research/sources/claude-design-designer-workflow.md)) is a design tool that hands off to Claude Code. It is a product surface, not a runtime pattern.
- **Scion and Antique** are source-control and review infrastructure.
- **The Opus project security review app** classifies risk; its runtime is not described.

### 2.5 Atlassian

Teardown: [lifecycle map](../user-story-mapping/01-pdlc-agent-ecosystem-map.md), [task research](../user-story-mapping/research-atlassian-sdlc-agents.md), [artifacts research](../user-story-mapping/research-artifacts-platforms.md).
- **Product capability, not internal use.** Most evidence is support docs (first-party) and launch blogs (vendor-claim).
- **Internal use rests on two sources:** one CPO talk (ASR captions) and one engineer's post.

| # | Agent or product | Class | Why it fits | Sources | Evidence | Fit |
|---|---|---|---|---|---|---|
| L1 | Jira Coding Agent (Rovo Dev) | P7 | Assigned, @-mentioned or started by an automation rule. It produces a branch and a draft PR with the user as author; started by automation, it runs in a restricted mode. | [atlassian-jira-coding-agent-generate-code](../../research/sources/atlassian-jira-coding-agent-generate-code.md); [lenny-podcast-tamar-yehoshua-roles-expanding](../../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md); [map](../user-story-mapping/01-pdlc-agent-ecosystem-map.md) | first-party (talk: speaker-reported, ASR captions) | clear |
| L2 | Third-party agents started from a work item (Claude Agent for Jira on Managed Agents, Cursor, Copilot, Codex) | P7 | Each runs in its vendor's cloud from the same work item and returns a draft PR. Claude Agent for Jira clones the repo in Anthropic's sandbox and streams status back. | [atlassian-jira-manage-agents-in-space](../../research/sources/atlassian-jira-manage-agents-in-space.md); [atlassian-blog-jira-ai-native-software-development](../../research/sources/atlassian-blog-jira-ai-native-software-development.md) | first-party; vendor-claim | clear |
| L3 | Jira work items as a dispatcher across several vendors' agents | P4 | One object launches any of five coding agents, lists their sessions on a space Agents page, and gives the reviewer one shared acceptance-criteria check. It is a layer that leaves the loop to the vendors. | [atlassian-jira-manage-agents-in-space](../../research/sources/atlassian-jira-manage-agents-in-space.md); [atlassian-rovo-dev-acceptance-criteria-code-review](../../research/sources/atlassian-rovo-dev-acceptance-criteria-code-review.md); [map](../user-story-mapping/01-pdlc-agent-ecosystem-map.md) | first-party | contested: no B.2 sub-shape is a system of record that dispatches work; it has no shared policy or sharing plane; it could equally be read as P7 routing |
| L4 | Rovo A2A gateway | P6 | Atlassian hosts an A2A server in front of Rovo, so external agents (Gemini featured) hand off requests. OAuth only; it acts with the user's permissions; responses are capped at about 30 seconds unless streamed. | [atlassian-rovo-a2a-gateway-docs](../../research/sources/atlassian-rovo-a2a-gateway-docs.md) | first-party | clear as a capability (inbound only; A2A 0.3.0; no usage figures) |
| L5 | Rovo MCP server | P6 | General harnesses reach Jira, Confluence, Goals and Teamwork Graph over remote MCP with user OAuth. Destructive tools are off by default. | [atlassian-rovo-mcp-server-supported-tools](../../research/sources/atlassian-rovo-mcp-server-supported-tools.md); [atlassian-rovo-mcp-server-getting-started](../../research/sources/atlassian-rovo-mcp-server-getting-started.md); [artifacts research](../user-story-mapping/research-artifacts-platforms.md) | first-party | partial: it serves tools, not a deployed agent |
| L6 | Rovo Dev code reviewer (Bitbucket, GitHub) | P6 | A deployed review agent on the PR route that checks the PR against the work item's acceptance criteria. | [atlassian-rovo-dev-acceptance-criteria-code-review](../../research/sources/atlassian-rovo-dev-acceptance-criteria-code-review.md); [arxiv-rovodev-code-reviewer-icse26](../../research/sources/arxiv-rovodev-code-reviewer-icse26.md) | first-party; vendor-claim (figures unreconciled: −30.8% vs −45%) | partial: triggers are documented (on PR creation, on every commit, or manually), but the caller is the repository, not a general harness |
| L7 | Rovo Dev in Bitbucket Pipelines | P6 | A CI-route agent that summarises deployments and explains failed builds. | [atlassian-rovo-dev-bitbucket-pipelines](../../research/sources/atlassian-rovo-dev-bitbucket-pipelines.md) | first-party | partial: beta; where its output goes is not stated |
| L8 | Jira workflow transitions and automation rules that start agents | P9 | Deterministic control flow in the work tracker: moving an item to In Progress, or an alert plus a bug, starts an agent step. | [atlassian-jira-agentic-engineering-guide](../../research/sources/atlassian-jira-agentic-engineering-guide.md); [lenny-podcast-tamar-yehoshua-roles-expanding](../../research/sources/lenny-podcast-tamar-yehoshua-roles-expanding.md); [atlassian-rovo-ops-expert-agent](../../research/sources/atlassian-rovo-ops-expert-agent.md) | vendor-claim; first-party (speaker) | partial: triggers yes; no engine-owned retries or checkpoints described |

**Fits no class (Atlassian).**
- **SaaS-native agents in the system of record:** Rovo Chat, Rovo Deep Research, the Delivery Agent, Ops Expert, Loom Record for agent and Jira Planner (Early Access).
- **Why not:** the vendor ships them inside its SaaS. The customer org does not choose or run their runtime, and no B.2 class describes that (section 6, strain 8).
- **Rovo Dev CLI** is named in the map, but no filed note describes it, so it is not placed.
- **Teamwork Graph, Goals and JPD** are records an agent reads.

### 2.6 Intercom

Teardown: [lifecycle map](../research-pm-agents-jobs-to-be-done/04-pdlc-agent-ecosystem-map.md). Almost all sources are Intercom's own, and Intercom sells Fin and an AI-native engineering story.

| # | Agent or product | Class | Why it fits | Sources | Evidence | Fit |
|---|---|---|---|---|---|---|
| I1 | Claude Code for everyone, with 13 plugins, 267 skills and enforcing hooks | P1 | One general harness, MDM-installed for about 1,100 of 1,305 staff. Hooks force a create-pr skill, and a SessionEnd hook mines transcripts for missing skills. B.2 already cites it. | [intercom-we-gave-claude-code-to-everyone](../../research/sources/intercom-we-gave-claude-code-to-everyone.md); [ideas-fin-how-we-use-claude-code-today](../../research/sources/ideas-fin-how-we-use-claude-code-today.md); [ideas-fin-2x-nine-months-later](../../research/sources/ideas-fin-2x-nine-months-later.md); [map](../research-pm-agents-jobs-to-be-done/04-pdlc-agent-ecosystem-map.md) | first-party | clear |
| I2 | Private auto-updating plugin marketplace (team-2x), plus the public 2x-skills subset | P10 | A governed registry: skills are reviewed against a rubric, pushed by MDM, promoted to the base plugin at 50 weekly users, and removed when unused. | [ideas-fin-claude-code-good-skills-bad-skills](../../research/sources/ideas-fin-claude-code-good-skills-bad-skills.md); [ideas-fin-webinar-qa-3x-rd-output](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md) | first-party | partial: serves one harness; harness-neutral distribution not claimed |
| I3 | "Shrek" review agents | P6 | GitHub webhooks start specialised review sub-agents (Claude and Codex) in short-lived AWS containers. About 19% of PRs are auto-approved by risk and size. | [ideas-fin-webinar-qa-3x-rd-output](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md); [intercom-ai-approving-pull-requests](../../research/sources/intercom-ai-approving-pull-requests.md) | first-party | clear (CI route; uses two vendors' models) |
| I4 | Background agent that watches CI after a PR is created | P7 | Work continues after the person moves on. | [ideas-fin-how-we-use-claude-code-today](../../research/sources/ideas-fin-how-we-use-claude-code-today.md) | first-party | partial: one sentence; runtime not described |
| I5 | "Buzz" cloud agents | P7 | Internal cloud agents, "a small contribution right now"; attribution to the starter had to be fixed to drive use. | [ideas-fin-webinar-qa-3x-rd-output](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md) | first-party | partial: named only; no architecture |

**Fits no class (Intercom).**
- **Fin, Fin Insights and Operator** are products Intercom sells. Operator's part in the support-readiness gate ([intercom-fin-npi-agent-readiness](../../research/sources/intercom-fin-npi-agent-readiness.md)) is a process step; its runtime is not described.
- **The read-only production console over MCP** is a tool, not an agent.
- **Cockpit and the AI interview moderator** have no runtime described.

### 2.7 Block (placeholder, built from filed notes only)

No Block summary exists yet. [research-block-product-practices/](../research-block-product-practices/) is empty and the task is active.
- **Used here:** the Lenny's Podcast note and follow-up 3, as instructed, plus the two Goose notes follow-up 3 cites.
- **Not used:** a dozen further `block-*` notes are being filed by the active Block worker. They are left out until its brief lands.

| # | Agent or product | Class | Why it fits | Sources | Evidence | Fit |
|---|---|---|---|---|---|---|
| B1 | Goose at Block | P3 | Block built and runs its own open-source general agent (Rust, Apache-2.0; desktop app, CLI and API) with a pluggable provider system. The org owns the loop. Now stewarded by AAIF. | [lenny-podcast-block-dhanji-goose](../../research/sources/lenny-podcast-block-dhanji-goose.md); [github-block-goose-repo](../../research/sources/github-block-goose-repo.md); [follow-up 3](../research-agent-runtime-patterns-taxonomy/followup-3-open-harnesses.md) | first-party | clear |
| B2 | Goose as the company-wide general agent, extended by MCP | P1 | Staff work directly in one general harness, and capability comes from MCP wrappers around internal systems ("Goose can write its own MCPs"). | [lenny-podcast-block-dhanji-goose](../../research/sources/lenny-podcast-block-dhanji-goose.md) | first-party | partial: P1 assumes a vendor's harness, and this one is Block's own (section 6, strain 9) |
| B3 | Background Goose agents (24/7 and in CI) | P7 | Overnight vulnerability analysis and patch drafts from bug tickets, and overnight feature attempts. | [lenny-podcast-block-dhanji-goose](../../research/sources/lenny-podcast-block-dhanji-goose.md) | first-party | partial: one podcast; runtime not described |
| B4 | Goose skills and custom distributions | P10 | Goose reads SKILL.md from `.agents/skills/` and Claude Code's `.claude/skills/`, so the asset format is portable. Custom distributions bundle internal MCP servers and recipes. | [goose-docs-using-skills](../../research/sources/goose-docs-using-skills.md); [github-block-goose-repo](../../research/sources/github-block-goose-repo.md); [follow-up 3](../research-agent-runtime-patterns-taxonomy/followup-3-open-harnesses.md) | first-party | partial: format portability yes; Block's own registry or distribution is not described |

Cross-link: Stripe Minions run on a Goose fork (T5). Goose is therefore also the upstream of another company's P3.

### 2.8 Spotify (placeholder, provisional)

No Spotify summary exists yet. [research-airbnb-spotify-product-practices/](../research-airbnb-spotify-product-practices/) holds only `mapkit.py`, and the task is active. Three notes filed by other tasks name Spotify agents. They are placed provisionally and should be rechecked when the brief lands.

| # | Agent or product | Class | Why it fits | Sources | Evidence | Fit |
|---|---|---|---|---|---|---|
| SP1 | Honk | P2 | "The Claude Agent SDK in a Kubernetes pod", with internal tools users can add and CI on Linux and macOS. | [claude-customers-spotify-office-hours](../../research/sources/claude-customers-spotify-office-hours.md) (filed by research-claude-resources-articles, not cited in its summary) | vendor-claim | partial: one vendor-hosted conversation; the architecture is one line |
| SP2 | Honk | P7 | Automated PRs across thousands of repos, auto-merged with owning teams told they may no longer see them; also invoked from Slack. Verification moved to a separate service that opens PRs only after full validation. | [claude-customers-spotify-office-hours](../../research/sources/claude-customers-spotify-office-hours.md); [infoq-spotify-honk](../../research/sources/infoq-spotify-honk.md) | vendor-claim; independent | partial: provisional |
| SP3 | Vedder (data assistant) | P6 | One agent served through a Slack bot, an MCP server for IDEs and AI tools, and a web UI, grounded on expert-owned context clusters. | [spotify-engineering-vedder-context-layer](../../research/sources/spotify-engineering-vedder-context-layer.md) (cited in the [Stripe teardown](../competitive-teardown-stripe-knowledge-agents/00-teardown-summary.md)) | first-party | partial: the MCP route is named; latency, identity and runtime are not described |

### 2.9 Airbnb (placeholder)

No Airbnb summary and no Airbnb source note are filed. No placement is made. Add rows when the [research-airbnb-spotify-product-practices](../research-airbnb-spotify-product-practices.md) brief lands.

---

## 3. By class (paste-ready for a later edit of B.2)

Each line is one teardown example: agent, fit, one-line reason, source and evidence. Teardown links go to the summary or map. Lines marked *placeholder* depend on briefs not yet filed.

### P1. Vendor harness plus skills and subagents
- **Intercom, Claude Code for everyone** (clear): about 1,100 of 1,305 staff on one MDM-installed harness with 13 plugins and 267 skills; hooks force a create-pr skill and a SessionEnd hook mines gaps into new skills. [Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md), [CTO](../../research/sources/ideas-fin-2x-nine-months-later.md) (first-party); [map](../research-pm-agents-jobs-to-be-done/04-pdlc-agent-ecosystem-map.md).
- **Anthropic, Claude Code and Cowork internally** (clear): plan mode, parallel sessions, CLAUDE.md and REVIEW.md for engineers; stacked department plugins for non-engineers. [Cherny](../../research/sources/lenny-podcast-boris-cherny-after-coding.md), [Cowork guide](../../research/sources/claude-guide-deploying-cowork-across-org.md) (first-party); [map](../research-claude-resources-articles/02-pdlc-agent-ecosystem-map.md).
- **Stripe and Shopify engineers** (clear): several general harnesses side by side, pre-configured, with no consolidation. [Kaliski](../../research/sources/howiai-stripe-minions-kaliski.md), [BVP](../../research/sources/bvp-inside-shopifys-ai-first-engineering-playbook.md) (first-party); [Stripe rollout](../../research/sources/claude-customers-stripe-claude-code-rollout.md) (vendor-claim).
- **Anthropic's AI-native SDLC playbook** (partial, prescription only): a committed intent.md → spec.md → plan.md chain run with skills, hooks and `claude -p`. No Anthropic team is shown using it. [playbook](../../research/sources/claude-ai-native-sdlc-playbook.md) (first-party).
- **Block, Goose company-wide** (partial; *placeholder*): one general agent extended by MCP for all staff, but the harness is Block's own. [Lenny](../../research/sources/lenny-podcast-block-dhanji-goose.md) (first-party).

### P2. Vendor SDK embedded in an own product
- **Ramp Glass, April 2026** (clear, historical): Claude Agent SDK inside a desktop app with Okta SSO, an MCP proxy, Dojo skills and a 24-hour memory pipeline. By October 2026 it had been replaced by Ramp's own harness, Laminar (see P3). [Charles](../../research/sources/x-geoffintech-ai-pilled-article.md), [Goddijn](../../research/sources/x-sebgoddijn-glass-article.md) (first-party); [teardown](../competitive-teardown-ramp-glass/00-teardown-summary.md).
- **Shopify Roast** (partial): Claude Code embedded as the CodingAgent step of an own workflow tool (2025). It is a precursor of Shopify's later own harness. [Roast](../../research/sources/shopify-engineering-introducing-roast.md) (first-party).
- **Spotify Honk** (partial; *placeholder*): Claude Agent SDK in a Kubernetes pod with user-added internal tools. [office hours](../../research/sources/claude-customers-spotify-office-hours.md) (vendor-claim).
- *Suggested edit:* B.2's P2 example "Ramp Glass on the Claude Agent SDK" needs an April 2026 date and a note that Glass moved to P3.

### P3. Own harness: framework-built, forked, or minimal loop
- **Ramp Laminar, under Glass, Inspect, Stack and customer agents** (clear): an in-house, provider-agnostic harness. Version 1 took six weeks from about May 2026, after Ramp tried vendor SDKs and managed-agent APIs. [Building Laminar](../../research/sources/ramp-builders-building-laminar.md) (first-party); [New Stack](../../research/sources/thenewstack-ramp-laminar-agent-harness.md) (independent, relies on Ramp's post); [teardown](../competitive-teardown-ramp-glass/00-teardown-summary.md).
- **Shopify River on Aquifer** (clear): an own disposable loop outside the sandbox, over a durable session log, with new agents added as profiles. [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (first-party); [teardown](../competitive-teardown-shopify-river/00-teardown-summary.md).
- **Stripe Kai** (clear): framework-built on LangChain Deep Agents over LangGraph plus a Stripe harness layer. It is the library's first production non-coding, multi-user agent on a general framework. [Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [LangChain](../../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor-claim).
- **Stripe Minions** (clear): a fork of Goose. B.2 already lists it. [Minions](../../research/sources/stripe-minions-one-shot-coding-agents.md) (first-party).
- **Block Goose** (clear; *placeholder*): Block wrote and runs its own open harness, now foundation-governed. [Lenny](../../research/sources/lenny-podcast-block-dhanji-goose.md), [repo](../../research/sources/github-block-goose-repo.md) (first-party).
- **Ramp Inspect** (partial): Ramp's own background agent with OpenCode as the loop; whether it is forked is not stated. [Inspect post](../../research/sources/ramp-builders-why-we-built-background-agent.md) (first-party).
- **Shopify "Vanilla" pi profile** (contested): it may be the open-source Pi agent on Aquifer, but that is unverified. [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (first-party); [adaptordie](../../research/sources/adaptordie-shopify-river-agent-stack.md) (independent, inference).

### P4. Meta-harness: a layer above vendor harnesses
- **Ramp OCA** (partial, DIY-coordinator shape): one Temporal-orchestrated agent that runs inside Claude Code or Codex depending on the model. [OCA post](../../research/sources/ramp-builders-how-we-built-oca.md) (first-party).
- **Stripe Kai projects** (partial): a project can be backed by "a different harness" behind Kai's UI and governance. Described, not demoed. [Krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party, ASR captions).
- **Atlassian Jira work items** (contested): one work item can launch Rovo Dev, Claude Agent for Jira, Cursor, Copilot or Codex, with sessions listed per space. A system-of-record dispatcher is not a B.2 sub-shape. [agents in a space](../../research/sources/atlassian-jira-manage-agents-in-space.md) (first-party); [map](../user-story-mapping/01-pdlc-agent-ecosystem-map.md).
- **Anthropic Managed Agents** (contested): B.2 lists it on Anthropic's own label, but it hosts one vendor's loop, so it fits P7 better. [launch](../../research/sources/claude-managed-agents-dreaming-outcomes.md) (first-party).
- No teardown supplies a clear P4 case.

### P5. Org-deployed agent workspace with its own agent
- **Ramp Glass, October 2026** (contested): an org-deployed, employee-wide, governed workspace with a platform-native agent on Laminar. It matches P5's definition, but B.3 classes Glass as P2+P8+P10+P7. [Building Laminar](../../research/sources/ramp-builders-building-laminar.md) (first-party); [Glyman](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md) (vendor-claim).
- **Shopify Aquifer** (partial): an org platform with a platform-native agent for 7,000+ people, but the surface is Slack and there is no per-employee workspace. [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (first-party).
- **Stripe Kai** (partial): a company-wide hosted agent service with project-level governance and many surfaces. Sessions are single-user and there is no personal memory. [Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md), [Krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party).
- No teardown supplies a clear P5 case. Cloudflare OS stays the only example that meets every part of the definition.

### P6. General harness calling deployed task agents
- **Anthropic Code Review** (clear): a GitHub App starts parallel find, verify and rank agents on every PR, and never approves. [GA post](../../research/sources/claude-code-review-ga.md) (first-party).
- **Intercom "Shrek"** (clear): webhook-triggered review sub-agents (Claude and Codex) in short-lived containers. About 19% of PRs are auto-approved by risk and size. [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md), [AI approving PRs](../../research/sources/intercom-ai-approving-pull-requests.md) (first-party).
- **Atlassian Rovo A2A gateway** (clear, as capability): an inbound A2A endpoint to Rovo with user-delegated OAuth and a 30-second sync cap. It adds a named A2A host to B.2's evidence; there is still no usage data. [A2A docs](../../research/sources/atlassian-rovo-a2a-gateway-docs.md) (first-party).
- **Atlassian Rovo MCP server; Rovo Dev reviewer; Rovo Dev in Pipelines** (partial): the MCP server is a tool route, not an agent. The reviewer runs on PR creation, on each commit, or manually, and Pipelines is beta; in both the repository is the caller, not a general harness. [MCP tools](../../research/sources/atlassian-rovo-mcp-server-supported-tools.md), [AC review](../../research/sources/atlassian-rovo-dev-acceptance-criteria-code-review.md), [Pipelines](../../research/sources/atlassian-rovo-dev-bitbucket-pipelines.md) (first-party).
- **Agent-to-agent calls in the teardowns** (partial): Ramp OCA asks Inspect for a PR; Stripe Orbit hands a plan to Minions; Kai and devbox agents use Harbor's tools over internal MCP; Shopify's PR-review profile is woken by an external system; Sentry Seer hands off to a coding agent on Managed Agents. [OCA](../../research/sources/ramp-builders-how-we-built-oca.md), [Orbit video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md), [Harbor](../../research/sources/stripe-harbor-ai-prototyping.md), [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (first-party); [Sentry](../../research/sources/claude-customers-sentry-bug-fixing-agents.md) (vendor-claim).
- **Spotify Vedder** (partial; *placeholder*): one data agent served over Slack, an MCP server for IDEs and a web UI. [Vedder](../../research/sources/spotify-engineering-vedder-context-layer.md) (first-party).

### P7. Background and cloud agents
- **Stripe Minions** (clear): unattended one-shot runs on pre-warmed devboxes, started from a Slack emoji, up to 12 hours, returning a PR. [Part 2](../../research/sources/stripe-minions-part-2.md), [Kaliski](../../research/sources/howiai-stripe-minions-kaliski.md) (first-party).
- **Ramp Inspect** (clear): a Modal sandbox per session returns a PR under the requester's identity. Automations now start more sessions than humans do (vendor-claim). [Inspect post](../../research/sources/ramp-builders-why-we-built-background-agent.md) (first-party); [Modal](../../research/sources/modal-ramp-inspect-background-agent.md), [office hours](../../research/sources/claude-customers-ramp-office-hours.md) (vendor-claim).
- **Ramp Glass on Laminar** (clear): async agents on disposable cloud workers, with tasks of "minutes or hours" that survive the laptop sleeping. [Building Laminar](../../research/sources/ramp-builders-building-laminar.md) (first-party).
- **Shopify River automation and job modes, and Remote Dev** (clear): River opens its own threads from a security ledger, runs overnight mobile bug fixes, and claims a warm remote Mac per session. [vuln remediation](../../research/sources/shopify-engineering-river-vulnerability-remediation.md), [Remote Dev](../../research/sources/shopify-engineering-remote-dev.md) (first-party).
- **Atlassian Jira Coding Agent and third-party agents from a work item** (clear): assign or automate, then get a draft PR as the user. [coding agent](../../research/sources/atlassian-jira-coding-agent-generate-code.md), [agents in a space](../../research/sources/atlassian-jira-manage-agents-in-space.md) (first-party).
- **Anthropic Cowork and Claude Code cloud sessions; Managed Agents; the ABC Legal fleet** (clear): scheduled tasks and project threads run with no device online; a hosted runtime with lead-agent orchestration; 50+ single-job agents moved off desktops. [Cowork web](../../research/sources/claude-cowork-web-mobile-handoff.md), [projects](../../research/sources/claude-code-projects-redesigned.md), [Managed Agents](../../research/sources/claude-managed-agents-dreaming-outcomes.md) (first-party); [ABC Legal](../../research/sources/claude-abc-legal-managed-agents-builders.md) (vendor-claim).
- **Anthropic Claude Tag on-call** (partial): an event-started, channel-resident agent that writes post-mortems and fix PRs but cannot deploy. [CI on-call](../../research/sources/claude-tag-ci-cd-first-responder.md) (first-party).
- **Intercom CI-watcher and "Buzz"; Block background Goose; Spotify Honk** (partial; Block and Spotify are *placeholders*): each is named, with no runtime described. [Scanlan](../../research/sources/ideas-fin-how-we-use-claude-code-today.md), [webinar Q&A](../../research/sources/ideas-fin-webinar-qa-3x-rd-output.md), [Lenny/Block](../../research/sources/lenny-podcast-block-dhanji-goose.md) (first-party); [office hours](../../research/sources/claude-customers-spotify-office-hours.md) (vendor-claim).

### P8. Shared, persistent, multi-user sessions
- **Shopify River** (clear; public by default): Slack-only with no DMs; durable event-log sessions; anyone can join a thread. It has the only published multiplayer metric (171,853 same-thread links in September 2026). [Under the River](../../research/sources/shopify-engineering-under-the-river.md), [chart](../../research/sources/x-tobi-river-floods-shopify-chart.md) (first-party); [teardown](../competitive-teardown-shopify-river/00-teardown-summary.md).
- **Anthropic Claude Tag** (clear; channel-scoped): a resident agent with channel memory, its own identity per channel, personal connectors for on-behalf-of reads, and multiple engineers steering one investigation. [identity model](../../research/sources/claude-agent-identity-access-model.md), [CI on-call](../../research/sources/claude-tag-ci-cd-first-responder.md) (first-party); [Tenable](../../research/sources/tenable-claude-tag-slack-access-model.md) (independent).
- **Ramp Inspect** (clear; multiplayer control plane) and **Ramp Glass** (clear; private by default, share on demand): already in B.2; Laminar now lists multiplayer as a harness feature. [Inspect post](../../research/sources/ramp-builders-why-we-built-background-agent.md), [Building Laminar](../../research/sources/ramp-builders-building-laminar.md) (first-party); [Glyman](../../research/sources/x-eglyman-introducing-glass-learn-things-once.md) (vendor-claim).
- **Ramp Research** (partial): stateful, collaborative Slack threads; runtime not described. [Ramp Research](../../research/sources/ramp-builders-meet-ramp-research.md) (first-party).
- **Stripe Minions' public channel and Orbit's shared workspaces** (partial): others watch and "pair prompt"; plans are shared and commented. Both rest on thin, ASR-caption sources. [Kaliski](../../research/sources/howiai-stripe-minions-kaliski.md), [Orbit video](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) (first-party).
- **Counter-example:** Stripe Kai is single-user by Stripe's own account, so it is not P8. [Kai post](../../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party).

### P9. Workflow engine and durable execution under agents
- **Stripe compliance agents** (clear): the review tooling orchestrates a DAG of tested sub-questions, and a human answers each one. [AWS/Stripe](../../research/sources/aws-stripe-compliance-agents.md) (first-party).
- **Stripe payment-method factory** (clear): "predictable coordination is better implemented in code"; an orchestrator LLM was dropped. [factory](../../research/sources/stripe-payment-method-factory.md) (first-party).
- **Stripe Minions** (clear): deterministic git, lint and test nodes around the agent loop. Already in B.2. [Minions](../../research/sources/stripe-minions-one-shot-coding-agents.md) (first-party).
- **Shopify Dispatch** (clear): a staged Ruby orchestrator for security scanning, with a verifier on a different model and published per-run costs ($50-300 per full scan). [Dispatch](../../research/sources/shopify-engineering-agentic-harness-outlasts-model.md) (first-party).
- **Shopify Roast** (clear): YAML workflows interleave shell, Ruby and agent steps, with replay from any step. [Roast](../../research/sources/shopify-engineering-introducing-roast.md) (first-party).
- **Ramp Laminar and OCA** (partial): Temporal provides durable orchestration under the agent loop, but no step graph is described. [Building Laminar](../../research/sources/ramp-builders-building-laminar.md), [OCA](../../research/sources/ramp-builders-how-we-built-oca.md) (first-party).
- **Anthropic's Claude Code review stack; Atlassian Jira automation; Shopify Helix** (partial): fixed CI gates with agent steps; work-tracker triggers that start agents; a migration harness with checkpoints, named only. [code review post](../../research/sources/claude-dev-claude-code-team-code-review.md), [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (first-party); [agentic guide](../../research/sources/atlassian-jira-agentic-engineering-guide.md) (vendor-claim).

### P10. Portable skill and plugin ecosystems as the distribution layer
- **Anthropic data team's skill sync** (clear): on merge, skills go to a plugin marketplace, cloud-storage blobs and MCP resources, so one skill reaches IDEs, hosted apps and Slack. [self-service analytics](../../research/sources/claude-anthropic-self-service-analytics.md) (first-party). It sits alongside the org marketplace already in B.2.
- **Stripe shared rule files** (partial): Minions read the same agent rule files as Cursor and Claude Code. It is the clearest cross-harness asset in the teardowns, but there is no registry. [Minions](../../research/sources/stripe-minions-one-shot-coding-agents.md) (first-party).
- **Stripe Kai skills and Agent Studio** (partial): open-spec skills from 100+ teams, telemetry-driven promotion, and a quality-signal control plane. Distribution only into Kai is shown. [Krishnamurthy](../../research/sources/howiai-stripe-kai-krishnamurthy.md) (first-party); [LangChain](../../research/sources/langchain-how-stripe-built-kai-deep-agents.md) (vendor-claim).
- **Stripe Toolshed; Ramp tool catalog** (partial): central MCP tool layers used by hundreds of agents. They are hosted services, not distributed packages. [Minions part 2](../../research/sources/stripe-minions-part-2.md), [Pragmatic Summit](../../research/sources/pragmatic-engineer-ramp-lessons-new-ai-product.md) (first-party).
- **Ramp Dojo; Intercom's team-2x marketplace; Shopify profiles and World skills** (partial): governed, reviewed internal registries, each serving one harness or substrate. [Goddijn](../../research/sources/x-sebgoddijn-glass-article.md), [good skills, bad skills](../../research/sources/ideas-fin-claude-code-good-skills-bad-skills.md), [Under the River](../../research/sources/shopify-engineering-under-the-river.md) (first-party).
- **Block Goose skills** (partial; *placeholder*): reads SKILL.md from both the cross-harness and Claude Code paths. [goose skills](../../research/sources/goose-docs-using-skills.md) (first-party).

---

## 4. Agents and systems that fit no class

| Ecosystem | Agent or system | Why no class | Source |
|---|---|---|---|
| Ramp | Ramp Router, per-project meter | Governance and cost control (axis 7), not a runtime pattern | [x-ramp-router-launch-posts](../../research/sources/x-ramp-router-launch-posts.md) (vendor-claim) |
| Ramp | Glass memory pipeline | Context and memory (D.13) | [x-shanebuchan-how-we-built-glass](../../research/sources/x-shanebuchan-how-we-built-glass.md) (first-party) |
| Ramp | Review Buddy, Testo, Gadget, customer-insight agent, small loops | No runtime described; one talk only | [lenny-podcast-geoff-charles-product-when-coding-solved](../../research/sources/lenny-podcast-geoff-charles-product-when-coding-solved.md) (first-party, ASR) |
| Ramp | Policy Agent | Customer-facing product, not an internal runtime | [ramp-builders-agents-users-can-trust](../../research/sources/ramp-builders-agents-users-can-trust.md) (first-party) |
| Ramp | Notion custom agents | Agents hosted inside a SaaS tool (strain 8) | [notion-inside-ramps-custom-agent-os](../../research/sources/notion-inside-ramps-custom-agent-os.md) (vendor-claim) |
| Shopify | Quick | Artifact hosting, not an agent runtime | [shopify-engineering-quick](../../research/sources/shopify-engineering-quick.md) (first-party) |
| Shopify | LLM proxy; "dreaming"; Jev classifier | Governance; learning loop | [venturebeat-shopify-ai-stack-model-agnostic](../../research/sources/venturebeat-shopify-ai-stack-model-agnostic.md) (independent); [shopify-engineering-remote-dev](../../research/sources/shopify-engineering-remote-dev.md) (first-party) |
| Stripe | Gru | Mechanism unknown; captions only | [youtube-notmybusiness-inside-stripe-ships-fast](../../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) (first-party) |
| Stripe | Trailhead, Compass, LLM Proxy | Context, records, governance | [stripe-sessions-2024-10x-engineer-panel](../../research/sources/stripe-sessions-2024-10x-engineer-panel.md) (first-party); [aws-stripe-compliance-agents](../../research/sources/aws-stripe-compliance-agents.md) (first-party) |
| Stripe | GoLLM, LibreChat, Hubert, NoCode Agent Builder | Pre-Kai and historical; the no-code builder was retired for micro-agent sprawl | [latentspace-emily-sands-stripe](../../research/sources/latentspace-emily-sands-stripe.md) (first-party) |
| Anthropic | Apps gateway | Control plane for one harness (axis 7) | [claude-apps-gateway](../../research/sources/claude-apps-gateway.md) (first-party) |
| Anthropic | Claude Design; Scion and Antique | Product surface; source-control infrastructure | [claude-design-designer-workflow](../../research/sources/claude-design-designer-workflow.md), [anthropic-redesigning-source-control-scion](../../research/sources/anthropic-redesigning-source-control-scion.md) (first-party) |
| Atlassian | Rovo Chat, Deep Research, Delivery Agent, Ops Expert, Loom Record for agent, Jira Planner | SaaS-native agents in the vendor's system of record (strain 8) | [atlassian-rovo-deep-research](../../research/sources/atlassian-rovo-deep-research.md), [atlassian-rovo-ops-expert-agent](../../research/sources/atlassian-rovo-ops-expert-agent.md), [atlassian-loom-record-for-agent](../../research/sources/atlassian-loom-record-for-agent.md) (first-party); [atlassian-blog-introducing-jira-planner](../../research/sources/atlassian-blog-introducing-jira-planner.md) (vendor-claim) |
| Atlassian | Rovo Dev CLI | Named in the map; no filed note describes it | [map](../user-story-mapping/01-pdlc-agent-ecosystem-map.md) |
| Intercom | Fin, Fin Insights, Operator | Products Intercom sells; Operator's runtime is not described | [intercom-fin-npi-agent-readiness](../../research/sources/intercom-fin-npi-agent-readiness.md) (first-party) |
| Intercom | Read-only production console over MCP; Cockpit; AI interview moderator | A tool; runtimes not described | [ideas-fin-how-we-use-claude-code-today](../../research/sources/ideas-fin-how-we-use-claude-code-today.md) (first-party) |

---

## 5. Notes on specific placements

- **Glass moves classes over time.** It was P2 in April 2026 and P3 in October 2026. The April form's P7 ("turns your laptop into a server") was a laptop-as-server variant, which B.3 already names. The October form is cloud-first.
- **Laminar is not "P4 in house".** Ramp calls it a "Managed Agents Platform" and names Anthropic's Managed Agents API among the options it rejected (single-provider lock-in). It owns the loop, so it is P3, not a layer above vendor loops.
- **Shopify's own lineage runs P2 to P3.** Roast embedded Claude Code in 2025; Aquifer runs Shopify's own harness in 2026. Shopify made the move a few months before Ramp did.
- **Ramp and Intercom use several harnesses in their review and on-call agents.** OCA runs in Claude Code or Codex, and Shrek uses Claude and Codex. These are small, per-agent forms of the P4 idea, without a governance layer.

---

## 6. Class definitions the teardowns strain

These are reported for a later B.2 edit. No class was changed here.

1. **P2/P3 line: embedding an open-source harness unmodified.**
   - *What doesn't fit:* P2 says "the vendor's harness ... as a library or subprocess"; P3 says "framework-built, forked, or written as a thin loop". Ramp Inspect runs OpenCode as its agent, not stated as forked. Open-Inspect lets the harness be swapped (OpenCode or Claude Agent). Kai runs on an open framework-harness (Deep Agents).
   - *Possible fix:* define P2 as "someone else's harness embedded, vendor or open-source" and P3 as "the org owns the loop's code", or add an "open harness embedded" note.
2. **P3 is written as a loop choice, but the strongest P3 cases are whole internal platforms.**
   - *What doesn't fit:* Laminar (15 harness responsibilities, durable sessions, a connectors service, multiplayer) and Aquifer (session, harness and sandbox split; gateway; credentials proxy; profiles) are in-house versions of what B.2 lists under P4 as "model vendor's hosted service".
   - *Possible fix:* a P3 sub-shape: "in-house agent platform under many agent products or profiles".
3. **P4's "model vendor's hosted service" sub-shape does not meet P4's own definition.**
   - *What doesn't fit:* Managed Agents hosts one vendor's loop, not a layer above several. The teardowns use it as a runtime (P7) and as an option Ramp rejected.
   - *Possible fix:* move it to P7, or say explicitly that it is listed under P4 only because of the vendor's own vocabulary.
4. **P4 has no sub-shape for a system of record that dispatches work to several vendors' agents.**
   - *What doesn't fit:* the Jira work item launches Rovo Dev, Claude, Cursor, Copilot or Codex and lists the sessions. Stripe's Kai project backed by another harness is a related front-door shape.
   - *Possible fix:* add "work-tracker or front-door dispatcher" as a sub-shape, or state that dispatch without shared policy is not P4.
5. **P5 rests on one example, and three teardown systems half-meet it.**
   - *What doesn't fit:* Glass on Laminar, Kai and Aquifer/River are org-deployed, company-wide, governed, with platform-native agents. They differ from Cloudflare OS on per-employee workspaces, apps, and zero ambient access.
   - *Possible fix:* say whether P5 means "org-deployed company agent service" (then all three are in) or keeps the workspace and security-model criteria (then none are). B.3's reading of Glass needs updating either way.
6. **P6 is written from a general harness's point of view.**
   - *What doesn't fit:* the teardowns' deployed-agent calls come from other agents (OCA → Inspect, Orbit → Minions, Kai → Harbor tools), from products (Sentry Seer), and from CI events (Shrek, Code Review, Shopify's PR-review profile, Rovo Dev reviewer). B.2 already lists CI triggers under P6, so the caller in the definition is narrower than the examples.
   - *Possible fix:* widen the definition to "any caller", or split off "agent-to-agent" and "event-triggered" routes.
7. **P8 bundles different sharing models.** The teardowns show six: public-by-default chat-native (River); channel-scoped with its own identity (Claude Tag); private with share on demand (Glass); a multiplayer session control plane (Inspect); watch-only public run logs (the Minions channel); and shared plan workspaces (Orbit). The privacy default is the sharpest difference, and the teardowns opened a trust-privacy-defaults dimension for it. *Possible fix:* name the sub-shapes in P8.
8. **No class for agents native to a SaaS system of record.**
   - *What doesn't fit:* Atlassian's Rovo agents, Notion custom agents at Ramp, and Intercom's Operator. The org adopts these rather than choosing a runtime, so P1-P10 do not cover them.
   - *Why it matters:* they are part of every lifecycle map, and P6 reaches them over MCP and A2A.
   - *Possible fix:* add an explicit out-of-scope note, or a class for "SaaS-native agents".
9. **P1 assumes the general harness is a vendor's.**
   - *What doesn't fit:* Block's staff work in Goose, a general harness Block owns. In that case P1 and P3 coincide.
   - *Possible fix:* P1 could read "a general harness (vendor or own) plus skills", with loop ownership left to P2/P3.
10. **P9's definition is narrower than its title.**
    - *What doesn't fit:* the title says "durable execution under agents", but the definition requires "deterministic steps and agent steps in one graph". Laminar and OCA use Temporal to make the agent loop durable without a step graph.
    - *Possible fix:* split "workflow graph with agent steps" from "durable substrate under an agent loop", or move the second to dimension D.10.
11. **P10 conflates two things:** harness-neutral portability and an internal governed registry.
    - *What doesn't fit:* most teardown registries (Dojo, Intercom's marketplace, Agent Studio, Shopify's World skills) are governed but single-harness. The cross-harness cases (Stripe's shared rule files, Anthropic's MCP-resource sync, Goose reading `.claude/skills/`) have no registry.
    - *Possible fix:* name the two halves.
12. **Classes need dates.**
    - *What doesn't fit:* Ramp moved Glass from P2 to P3 within six months; Shopify moved from embedding Claude Code (Roast) to an own harness (Aquifer). A placement without a date will go stale.
    - *Possible fix:* B.2 examples should carry the date of the source.

---

## 7. Gaps and caveats

**Thin evidence.**
- Several placements rest on a single source, or a single sentence:
  - Orbit: one vendor-filmed video and one post;
  - Gru: captions only, not placed;
  - Helix: named only;
  - Intercom's Buzz and CI-watcher: one sentence each;
  - Block's background agents: one podcast;
  - Kai's other-harness projects: described, not demoed.
- Review Buddy, Testo, Gadget and Ramp's small loops are not placed at all for lack of any runtime description.
- No teardown supplies a clear P4 or P5 case.

**ASR-caption sources.** The following rest on YouTube auto-captions, where names and product terms are unreliable:
- **Ramp:** all four videos (the Lenny's channel talk, the Pragmatic Summit talk, the launch video, the Notion video).
- **Stripe:** the How I AI episodes with Krishnamurthy, Kaliski and Williams; the Not My Business video (Orbit, Gru), whose whiteboard was read from a 360p frame.
- **Atlassian:** the Yehoshua talk, the sole basis for internal-use claims.
- **Other podcasts:** the Shopify Knowledge Project note and the Anthropic Lenny's Podcast notes rest on podcast transcripts. Check each note's "Could not verify" section before quoting.

**Self-reported claims and vendor claims, kept apart.**
- **Mostly self-reported.** The cross-ecosystem page counts 105 source notes across the six maps, with one independent. This mapping uses some independent notes the maps did not cite: The New Stack on Laminar, Wavect on Inspect, Tenable on Claude Tag, VentureBeat, ZenML, adaptordie and Port on Shopify, InfoQ on Honk, and AI Founders on Kai.
- **What the independent notes cover.** They either restate the company's account (ZenML, adaptordie, Port, The New Stack) or critique a design or a number (Wavect, Tenable, AI Founders). None measures an outcome.
- **Where vendor-claim sources were used:**
  - Ramp's launch material (Glyman, the launch video);
  - customer stories on claude.com (Ramp office hours, Stripe rollout, ABC Legal, Sentry, Spotify office hours, Cyera);
  - LangChain on Kai, Modal on Inspect;
  - Atlassian launch blogs and the Rovo Dev ICSE paper (all authors Atlassian-affiliated).
- **What vendor claims support here.** Architecture placements supported only by vendor claims are marked in the evidence column. No outcome figure is used to support a placement.

**Placeholders.**
- **Airbnb:** no summary and no filed notes. No row is made.
- **Spotify:** no summary. Three rows are provisional, from notes filed by other tasks: the Honk office-hours note (vendor-claim), InfoQ on Honk (independent), and the Vedder post (first-party).
- **Block:** no summary. Four rows from the Lenny's Podcast note, the Goose repo and skills notes, and follow-up 3. About a dozen further `block-*` notes are being filed by the active Block worker and were deliberately not used; rerun this mapping when [research-block-product-practices](../research-block-product-practices.md) lands.

**Other caveats.**
- **Stale B.2 text.** B.2 and B.3 cite Glass "on the Claude Agent SDK". That is now dated April 2026 (see the P2 suggested edit).
- **Reading notes, not originals.** Where a note says its body was read through a summarising fetch (the Ramp Builders Inspect post as filed by user-story-mapping; some Atlassian pages before the audit), placements lean on the verbatim-read notes where one exists.
- **Duplicate notes.** Two notes describe the same Ramp Inspect post (`ramp-builders-why-we-built-background-agent` and `ramp-builders-why-we-built-our-own-background-agent`). This mapping cites the first, filed by the Ramp teardown.

---

## 8. Revised classes (2026-10-24)

Geoff chose to revise the classes (task revise-pattern-classes). The old-to-new table is in the [synthesis change log](../research-agent-runtime-patterns-taxonomy/01-synthesis.md#change-log). Sections 1 to 7 above keep the original numbering. These placements change under the revised classes:

| Ecosystem | Agent or system | Old | New | Fit now | Why |
|---|---|---|---|---|---|
| Ramp | Glass (October 2026) | P5 (contested) | **P5a**, on a P3 harness | clear (first-party only) | P5 now means an org-deployed, company-wide platform with a platform-native agent; Glass is a per-employee workspace on Laminar. |
| Ramp | Glass sessions | P8 | **P8c** | clear | Private, shared on demand (a support agent hands a session to an engineer). |
| Ramp | Inspect | P8 | **P8d** | clear | Multiplayer session control plane. |
| Ramp | Ramp Research | P8 (partial) | **P8b** (related form) | partial | Chat-native shared agent in Slack channels. |
| Ramp | Notion custom agents | fit no class | **P11** | clear | Agents built into a SaaS tool. |
| Shopify | River on Aquifer | P5 (partial, as Aquifer) | **P5b** | clear | Company agent service through Slack. |
| Shopify | River | P8 | **P8a** | clear | Public by default, chat-native. |
| Stripe | Kai | P5 (partial) | **P5b** | clear | Company-wide hosted agent service with project-level governance. Not P8, since sessions are single-user. |
| Stripe | Kai projects | P4 (partial) | **P4, front-door dispatcher** | partial | Described, not demoed. |
| Stripe | Minions' public channel | P8 (partial) | **P8e** | clear | Watch-only public run log. |
| Stripe | Orbit | P8 (partial) | **P8f** | partial | Shared plan workspace; ASR captions only. |
| Anthropic | Managed Agents | P4 (contested) | **P7**, hosted harness service | clear | Hosts one vendor's loop. |
| Anthropic | Claude Tag | P8 | **P8b** | clear | Channel-scoped, with the agent's own identity. |
| Atlassian | Jira work items dispatching to several agents | P4 (contested) | **P4, front-door dispatcher** | partial | Per-space session visibility; no shared policy documented. |
| Atlassian | Rovo Chat, Deep Research, Delivery Agent, Ops Expert, Loom Record for agent, Jira Planner | fit no class | **P11** | clear | SaaS-native agents in the vendor's system of record. |
| Intercom | Fin, Operator | fit no class | out of scope | n/a | Products Intercom sells, not internal runtimes. |

**Counts after the revision:** Glass, Kai, River on Aquifer and Managed Agents gain clear placements. Jira moves from contested to partial. There are 2 new P11 rows (Ramp's Notion agents; Atlassian's Rovo agents as one row). One contested placement remains: Shopify's "Vanilla" pi profile (P3).

