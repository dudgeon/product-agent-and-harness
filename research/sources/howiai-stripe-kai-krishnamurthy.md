---
title: "Build your own company brain: the enterprise AI playbook from Stripe's engineering team | Sharadh Krishnamurthy (How I AI)"
source_url: https://www.youtube.com/watch?v=AbZODZ_4VaM
author: Claire Vo (host), Sharadh Krishnamurthy (EM, Stripe Agent Foundation)
publisher: How I AI (Lenny's network); also https://lennysnewsletter.com/p/build-your-own-company-brain-the
published: 2026-09-07
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [scoped-governance-containers, identity-delegation, org-context-grounding, legible-org-for-agents, skills-marketplace, org-learning-loop, single-agent-many-skills, cost-control-routing, human-review-gates, agent-failure-modes, metrics-review-agents, build-vs-buy, enablement-by-product, harness-portability]
relevance: high
---

## Relevance to the project
The richest first-party source on how Kai is governed and used, with a live demo. Three ideas are new to our register: **projects as the unit of governance** (a project owner sets default model, tool policies and human-in-the-loop rules for everyone working in it, including a separately backed "super secure" HR project and the option of a different harness behind the same UI); **user-controlled personal context** (org chart on by default, Drive/Slack/DMs opt-in, toggleable per session); and **platform-driven skill quality** (skill-creator from a session, IDE-like draft editor, automatic improvement suggestions, telemetry to promote or demote skills). Also: agent identity for load-shedding, "rogue" agents that nearly took down core systems, and a data-agent triage path. Bears on governance-control-plane, agent-identity-delegation, capability-distribution-trust, context-and-memory and trust/privacy defaults.

## Themes
- scoped-governance-containers: "projects are primarily a governance mechanism" (07:50); a project owner chooses the default model and can block expensive models (08:40); tool policies per project, e.g. HR's project prevents writing sensitive data to a Stripe-wide Google Doc without banning tools (31:50); human-in-the-loop confirmation configured per project for sensitive tools (calendar-invite demo, 32:30); "I also don't want this to be happening for every person at Stripe ... projects are again drawing a boundary" (33:30). Projects range from 5 to 500 people; created per team or short-lived effort; "it's all open" (08:10).
- harness-portability: a project can be powered by "a custom agent ... backed by a different API in the back end and a different harness" while keeping Kai's features (31:00).
- org-context-grounding / legible-org-for-agents: out of the box Kai knows who you are, your place in the org chart, date/time; project-management system (OKRs, shipped emails, projects); opt-in Drive, Slack, private messages (05:30-07:00). Krishnamurthy toggles his own access per session or day.
- identity-delegation: "agentic identity ... we haven't solved this yet" but used to tag what use case an agent is serving, for priorities and load shedding (19:40).
- agent-failure-modes: "There were agents that went rogue ... may have almost taken down core systems but we caught it in time" (20:20); "when in doubt an agent will just brute force it" against the warehouse (18:30).
- metrics-review-agents: "ask data" skill encodes a data-scientist-designed fallback: existing reports/artifacts first, then blessed analytics layer, then data catalog (16:00); Trino warehouse hardened for agent load; Hubble = data querying layer; "I now generate a dashboard every meeting I go to" (21:40).
- skills-marketplace / org-learning-loop: skill-creator skill packages a session into a reusable "load-bearing repeatable workflow" (29:30); skills follow "a standard open spec ... you can use on any of your harnesses" (36:20); publish privately or to an "area"; IDE-like draft editor (38:00); automatic suggestions to skill authors (09:50, 40:00).
- single-agent-many-skills: ~2,000 skills; telemetry: ~50 "hammered every day", a long tail of 100-150 by sub-orgs, many used by two or three people; an ETL pipeline tells harness owners which skills to promote into the general workflow and which to move out "because it's just taking up context" (42:00).
- human-review-gates: HITL confirmation for sensitive tool calls; warns against prompting on every tool call: "eventually you're going to press the wrong button" (35:30).
- build-vs-buy: built because "it's not about providing AI, it's about providing the correct governance structures" (04:00); hosted in the cloud, always on, behind standard security boundaries; infrastructure reused for Stripe's customer agents.
- enablement-by-product / adoption: v0 by "one and a half people over two weeks"; pilot with GTM (200-300 users, 2.5-3 people); a company-wide demo triggered the steep ramp; core team "less than 10 people"; "10,000 plus people use it every week"; "86 plus % of the company" (21:00).

## Key points
- Sessions run in the cloud with a per-session secure sandbox; harness tools move data into and out of the sandbox and search it (12:40).
- Artifacts are iterated in place over many turns ("hundreds of turns over multiple weeks"), which is also token-efficient (22:30). Users build "light apps" on last-mile data (23:40).
- Kai schedules exist (personal assistant use, 46:20); not demoed.
- Skill retrieval: in enterprise work "there is no hierarchy" like a repo, so packaging and retrieval of skills is the core investment (38:40).

## Notable quotes
- "Kai looks like a single product. It really isn't. It's like the icing on top of a multi-layer cake and each of those layers can be like customized" (35:00).
- "If you put too much friction in front of people, they're just going to do unsafe things" (35:20).
- "Agents are very creative at bringing your infra down" (19:30).

## Could not verify
- Transcript is YouTube auto-captions (e.g. "Sherrod" = Sharadh, "Hubble" spelled variously). Timestamps are 2-minute buckets.
- 86%+ / 10,000+ weekly are spoken claims from a live dashboard; not independently verified. Stripe headcount ~10,000 (Sands, 2025) makes 10,000+ weekly and 86% hard to reconcile exactly.
- The "different harness behind a project" capability was described, not demoed.
