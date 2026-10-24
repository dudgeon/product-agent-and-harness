---
title: "Not all AI agents are created equal"
source_url: https://www.lennysnewsletter.com/p/not-all-ai-agents-are-created-equal
author: Hamza Farooq and Jaya Rajwani (guest authors; agent-building course instructors and consultants), introduced by Lenny Rachitsky
publisher: Lenny's Newsletter
published: 2026-04-14
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [work-structure-spectrum, agent-frameworks, one-job-per-agent, single-agent-many-skills, outcome-measurement-gap, agent-project-failure-rates, cost-control-routing]
relevance: medium
---

## Relevance to the project
A consultant's taxonomy for sorting a backlog of "agent" ideas into three architectural types (deterministic automation, reasoning-and-acting agents, multi-agent networks), each with its own tools, timelines, metrics and "you've outgrown this" signals. It bears directly on the work-structure dimension (what agent shape fits which work) and on sequencing (start deterministic, add reasoning, reserve multi-agent for cross-team coordination). Its observation that real systems like Claude Code are **layered** (a reasoning loop plus deterministic hooks plus isolated sub-agents) is a useful counter to treating "single agent vs multi-agent" as an either/or. Not PM-specific: the PM assistant appears only as a typical backlog item, and its category placement sits in a table image we could not read.

## Themes
- work-structure-spectrum: three categories with explicit fit tests: Category 1 if the process maps as a flowchart with "fewer than 15 to 20 branches"; Category 2 if "the same user request can trigger different action sequences every time"; Category 3 if multiple teams own agents that must delegate to each other ("The three agent categories").
- agent-frameworks: tool mapping: n8n, Zapier, Make, OpenAI AgentKit, Lindy, Gumloop for Category 1; LangGraph, CrewAI, AutoGen, Google ADK for Category 2; ADK/AutoGen plus A2A and Temporal, Kafka or Step Functions for Category 3.
- single-agent-many-skills: "A single orchestrator agent (Category 2) is usually simpler and more effective until true cross-team coordination becomes unavoidable" (Category 3, prioritization).
- one-job-per-agent: Category 3 is justified when "Different teams want to own their specialized agents" and a single agent "is trying to handle too many domains ... and performance is degrading" (outgrown Category 2).
- outcome-measurement-gap: per-category metric sets (completion, automation rate, human review rate, cost per run; task completion, tool-call efficiency, CSAT; cross-agent success, discovery success, time to add an agent); "Define success metrics before building" (path forward). These are product-agent metrics, not PM-outcome metrics.
- agent-project-failure-rates: the common failure is mis-categorization: building Category 1 problems with Category 2 frameworks (over-engineering), or Category 2 problems with Category 1 tools, which "breaks in production" (three categories).
- cost-control-routing: operating cost varies from "$500 per month" to "a six-figure annual LLM bill"; cost per workflow/session/complex task is a first-class metric.

## Key points
- Claimed share of opportunities from the authors' client work: Category 1 is 60-70%, Category 2 is 25-30%, Category 3 used by "fewer than 5% to 10% of teams building agents", expected to grow over 12-24 months.
- Client examples (consultant-reported, unnamed companies): an email support agent went 52% → 78% → 87% workflow completion over 8 weeks, automating 3,000 emails a month and saving "$18K/month"; a voice + image shopping assistant went 71% → 86% task completion and $0.12 → $0.08 per session over four months, conversion lift +8% → +22%; a retailer's multi-agent network went 72% → 91% cross-agent success and 6-8 → 2-3 weeks to add a new agent.
- Signals you've outgrown Category 1: 30+ nodes and new branches weekly; unpredictable phrasing; the agent must choose which source or API to use. Outgrown Category 2: too many domains in one agent; agents must delegate to agents; tasks run hours or days; hundreds of parallel instances.
- "Real-world systems: where architectures converge": Claude Code is a ReAct loop with "a deterministic hooks system" at lifecycle events and sub-agents with isolated contexts; OpenClaw is ReAct that can be configured multi-agent. "Deterministic for auditability. ReAct for flexible reasoning. Multi-agent for parallelism and isolation."
- Three questions per agent idea: which category does it need; do we have the infrastructure and expertise; what is the measurable ROI. Treat categorization as "a living decision".
- Authors' client base named as Fortune 500 companies including Jack in the Box, Tripadvisor and The Home Depot; the guide took "over 50 hours".

## Notable quotes
- "comparing apples, oranges, and jet engines on the same spreadsheet" (opening).
- "you control the tools; the LLM controls the reasoning" (Category 2).
- "not which architecture to pick, but knowing when your problem has outgrown one layer and needs the next" (where architectures converge).

## Could not verify
- Several tables (example agents per category, per-category resource profiles, the 5-minute triage questions) were images not in the text; the PM assistant's category is therefore unknown.
- All metrics come from the authors' unnamed client engagements; method and baselines are unstated. The authors sell agent-building courses.
