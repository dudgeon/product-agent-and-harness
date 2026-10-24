---
title: Under the River
source_url: https://shopify.engineering/under-the-river
author: Burke Libbey, Javier Moreno, River (Shopify)
publisher: Shopify Engineering blog (announced by @ShopifyEng on X, https://x.com/ShopifyEng/status/2059985599205912957)
published: 2026-05-28
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [shared-persistent-sessions, org-learning-loop, compounding-context-repo, legible-org-for-agents, harness-portability, single-agent-many-skills, remote-agent-invocation, memory-architecture, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project

Shopify's own engineering account of River (its Slack agent) and Aquifer (the platform under it). It is the most detailed first-party description in our library of a company-wide agent whose sessions are durable, multiplayer and public by default, and whose next agents are "profiles" (config bundles) on one substrate. It bears directly on runtime location, harness layering (brain/hands split), session persistence, capability packaging, agent interface (Slack-only) and the trust and privacy model (no DMs). All numbers are Shopify's own.

## Themes

- **shared-persistent-sessions**: Aquifer's rule is that "the conversation doesn't" die; session = append-only Postgres event log, harness and sandbox disposable; idle "session cells" exit and rehydrate on any host (Part III, "The session must survive", "Session cells").
- **org-learning-loop**: River works only in public Slack channels, no DMs; Shopify mines the transcript corpus and feeds patterns back into skills, prompts and defaults; "the privacy of an agent thread is a disadvantage" (Part II "River only works in the open"; "What to take with you").
- **compounding-context-repo**: monorepo World holds code plus skills, conventions, intent documents, runbooks, AGENTS.md and "zone knowledge"; sessions leave "a pebble, a skill update, an AGENTS.md diff" behind (Part II "At scale").
- **legible-org-for-agents**: "agent-friendly ≈ human-friendly"; the 2024 monorepo + Nix bets made the codebase legible to agents (Part I).
- **harness-portability**: harness outside the sandbox lets Shopify "swap models, runtimes, even languages on the harness side" (Part III).
- **single-agent-many-skills**: one substrate, many agents as "profiles": "The cost of the next River-shaped thing is no longer a new platform, it's just a profile" (Part III).
- **remote-agent-invocation**: three modes on one stack: interactive (River), automation (PR review, woken by an external system), job (CI/batch, session log optional) (Part III).
- **vendor-claims-vs-independent-evidence**: usage counts come from "the river_sessions domain table that River writes to itself"; no outcome or quality measure (Part II "At scale").

## Key points

- **Timeline.** Spring 2024: Shopify decides to become a monorepo company (World) and to build everything with Nix, on the bet that "code is going to be increasingly written with AI". Monorepo migration forced CI to scale "by an order of magnitude", made merge queues and the build cache load-bearing (Part I). River "launched a couple of months ago" / "shipped about two months ago" as of 2026-05-28, i.e. roughly March 2026 (intro; "We are at the start"). Note: Tobi's Oct 2026 chart already shows 35,418 River threads in March 2026, so the launch was probably earlier in Q1 or an internal ramp preceded the "launch".
- **Payoffs of the substrate:** an agent at the repo root that can navigate across zones; skills as files loaded on demand; "ask the repo a question" as an interface; navigation from a production log line to the causing commit in one workspace; same Nix environments in dev, CI and production (Part I).
- **"Local agents have a ceiling":** every engineer's laptop agent is a private artifact that dies with the session; none learn from each other (Part I, quoting Tobi).
- **The surface.** River is invoked with @river in a public channel; reads code, runs tests, opens PRs, queries the data warehouse, reads production traces, "occasionally pushes back on a plan". Median session 19 minutes; median 50 tool calls (Part II).
- **Public-only rule.** No direct messages; "every conversation with River becomes a public Slack transcript, open by default to other Shopify employees" (Part II). The good thread: one person asks, River posts partial findings, a second human joins with a constraint, River continues, the thread becomes searchable and the next person starts from it.
- **Scale (30-day window before 2026-05-28):** 59,918 sessions in 5,170 channels, touching 7,000+ people (~1,200 more than in Tobi's early-May post), 3,536 River-coauthored merged PRs; "one in eight merged pull requests across Shopify is coauthored by it" (intro, Part II).
- **Demand for more agents:** PR review, research, migration, compliance scans, performance investigations: "agentic workflow against the monorepo, in Slack, durable, multiplayer" (Part II "Can I do this for X?").
- **Aquifer decomposition:** Session (durable identity, append-only, Postgres-backed event log, canonical truth); Harness (agent loop: reads history, calls model, emits tool intents; disposable); Sandbox (filesystem, shell, repo; disposable, sometimes warm). Plus gateway, credentials proxy, observability pipeline. The harness lives outside the sandbox, giving safety (loop not in the `rm -rf` blast radius), replaceability, and observability (whole decision stream on the harness side) (Part III).
- **Session cells:** an ephemeral process (Go runtime + harness in one process group) materialised per live session; exits when idle; the next interaction may land on a different host; "cattle, not pets, at the session level". Orchestrator not named (Part III).
- **Profiles:** "A profile is data: a system prompt, a set of skills, a set of extensions, a sandbox policy, model defaults", built with Nix, shipped as bundles. River, PR review and "Vanilla, the headless 'pi' agent" are peer profiles (Part III). (The post does not say whether "pi" is the open-source Pi coding agent or an internal name; unverified.)
- **Influence:** cites Anthropic's "Scaling Managed Agents" (Apr 2026) "Decouple the brain from the hands" as validating their direction (Part II end).
- **Three takeaways for others:** decouple brain from hands ("you will not be able to retrofit it"); make the agent multiplayer by construction; treat the next agent as a profile, not a platform ("What to take with you").
- **Not covered:** model vendor(s), cost, identity/permissions model (beyond a "credentials proxy"), how private/sensitive work is handled, evals. Nothing on non-engineering use beyond "7,000+ people".

## Notable quotes

- "River only works in the open. No direct messages." (Part II)
- "Cells die, sandboxes die, machines die. The conversation doesn't." (Part III)
- "A profile is data" (Part III)
- "the privacy of an agent thread is a disadvantage" (What to take with you)

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify

- The embedded example thread ("Here's what that looks like") is an image/video not captured in text.
- Launch date of River; identity of the "pi" agent; which models River uses.
