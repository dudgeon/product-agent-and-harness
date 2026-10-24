---
title: Meet Stripe's Knowledge AI Platform
source_url: https://stripe.dev/blog/meet-stripes-knowledge-ai-platform
author: Anna Mason, Sharadh Krishnamurthy (EM, Agent Foundation), Anupam Upadhyay (SWE, AI Platform)
publisher: Stripe Dot Dev Blog
published: 2026-07-30
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [agent-as-service-many-surfaces, single-agent-many-skills, skills-marketplace, org-learning-loop, task-context-isolation, build-vs-buy, harness-over-model, shared-persistent-sessions, outcome-measurement-gap, vendor-claims-vs-independent-evidence, work-structure-spectrum]
relevance: high
---

## Relevance to the project
Stripe's own account of Kai, its company-wide agent for non-engineers (sales, finance, TAMs, legal, ops). It is the closest peer to Ramp Glass and the cleanest statement of an alternative answer to several of our dimensions: a cloud-hosted agent **service** with many surfaces (web app, Slack, Chrome extension, embedded in internal apps) rather than one app; a federated control plane (Agent Studio) where domain owners build and govern their own agents and skills; and a shared execution substrate with Stripe's customer-facing agents. Bears on loop-source, harness-layering, runtime-location, agent interface, trust/privacy, capability distribution, and adoption.

## Themes
- agent-as-service-many-surfaces: "The agent is a service, not an application, and surfaces are simply customized views into it." Web app (most users), Slack integration, Chrome extensions inside third-party web tools, and internal apps embedding Kai via API (e.g. Finance's budget-modelling app) (section "Surface-agnostic APIs"). A standalone product "would force users out of their natural workflows"; a per-surface product "would be hard to maintain".
- task-context-isolation: invariant "you shouldn't combine data from two unrelated customer contexts in a single analysis"; isolation is "what should this task be allowed to view given this context?", not what the user's token can access (section "Building guardrails from scratch").
- single-agent-many-skills: one harness connected to 1,000+ skills and tools; skill choice is the hard part because knowledge work lacks the folder structure coding agents use; follow-up post promised on a "hybrid RAG/LLM approach".
- skills-marketplace / org-learning-loop: Agent Studio = control plane for domain owners to "build, test, and monitor their skills, custom Kai agents, and tool selections", with usage data and quality signals per asset; assets organised into "areas" managed by domain experts.
- build-vs-buy: prior options failed: a NoCode Agent Builder (4,000+ agents built; "conceptually similar prompts but with varying levels of quality", "proliferation of these micro-agents increasingly hard to monitor and maintain") and coding agents for non-engineers (security concerns; new support burden for code-quality teams).
- harness-over-model: core primitives (harness, sandbox, workflow orchestration, access control) "deliberately shared with Stripe's product-facing agents"; same security bar internal and external; "flywheel".
- shared-persistent-sessions: sessions are single-user today; context "currently 'locked in'"; roadmap: share across sessions, multiple people and agents collaborating on the same artifacts (section "We haven't won yet").
- outcome-measurement-gap / vendor-claims-vs-independent-evidence: sales uplift figures compare the same sellers in weeks with vs without Kai, not a controlled test (section "Impact").
- work-structure-spectrum: coding work is "rather uniform", so one agent architecture fits; knowledge work needs "different tools, different data, different outputs, and different definitions of 'done'".

## Key points
- Launch April 2026; "within two weeks ... most of Stripe was using" Kai. 83% weekly active users (as of 2026-07-30), "nearly all of GTM".
- Most sessions are many-turn (deep research, artifact creation, refinement before sharing). One session reached 932 turns.
- Three layers: (1) surface-agnostic APIs; (2) Agent Studio; (3) execution environments. Harness built on LangChain deepagents, on Kubernetes, per-session secure sandbox, multi-tenant virtual filesystem; agent iterates on artifacts in the VFS; code sandbox for analytics/data processing. Extended context lives in S3/VFS.
- A GTM team owns a Kai agent tuned to its workflows: loads its skills by default, connects to its data sources, formats output its users expect.
- Impact (all Stripe-reported): GTM new hires use Kai 2.7x more; power users close 80% more value than low users in the same cohort; AEs in Kai weeks: 2x sales activity, +17% opportunities, +26% revenue opportunities, +39% deals closed; "25,000 hours per year" shifted from admin to revenue work; 5,000+ sessions a day centre on data analysis.
- Engineering uses Kai too: system questions, research for run requests, logs, plans, invoking more specialised agents.
- Roadmap: state management (active vs extended context), reflection loop that proposes skill improvements "for the skill owner to review", collaboration primitives.

## Notable quotes
- "The agent is a service, not an application, and surfaces are simply customized views into it."
- "Coding agents operate in an environment with decades of fast, verifiable guardrails ... Knowledge work has very little support for these constructs."
- "A single monolithic agent simply cannot encode all of these constraints effectively."

## Could not verify
- All numbers are Stripe's own; no independent audit. "Most of Stripe within two weeks" vs LangChain's "296 to 5,000 in about four weeks" are different framings of the ramp.
- The promised follow-up on skill routing was not found as of 2026-10-24.
- How the context-isolation invariant is enforced technically is not described.
