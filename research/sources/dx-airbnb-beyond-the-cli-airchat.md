---
title: "Beyond the CLI: Agentic AI for async workloads and non-developers"
source_url: https://getdx.com/podcast/beyond-the-cli-agentic-ai-for-async-workloads-and-non-developers/
author: Christopher Sanson (Product Lead, AI Developer Experience, Airbnb) and Madison Capps (Engineering Manager, Infrastructure, Airbnb)
publisher: Engineering Enablement by DX (talk recorded at DX Annual)
published: 2026-06-22
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [enablement-by-product, leadership-permission-mandate, non-engineer-builders, single-agent-many-skills, cost-control-routing, remote-agent-invocation, shared-persistent-sessions, spec-becomes-prototype-and-evals, prd-agents, agent-factory-sdlc, outcome-measurement-gap, skills-marketplace]
relevance: high
---

## Relevance to the project
The richest first-party account of Airbnb's internal agent platform. AirChat is Airbnb's internal harness ("our internal AI harness before that was a term"): it wraps Claude Code and Codex behind one gateway, handles auth and permissions, loads default MCPs, and carries a community plugin and skill marketplace. On top sit an SDK (about 40 internal apps, including Pascal, a PM and designer tool that turns an idea into a concept brief using market research, the roadmap and business objectives) and AirChat Remote for parallel and async agents on sandboxed cloud workspaces. The talk also states Airbnb's product-process shift: short concept briefs, many prototypes, smaller pods, and an "AI project coordinator" to keep docs, prototypes and Jira in sync. This is close to the project's target design and gives adoption numbers with methods.

## Themes
- enablement-by-product: AirChat was branded and run like a product (t-shirts, workshops, internal marketing, UX focus); an AI champions and train-the-trainer program; the AI dev-productivity Slack channel (started Aug 2023) is among the most active (Sanson, ~05:21).
- leadership-permission-mandate: no mandates, quotas or links to performance reviews; "It's all been organic adoption" (Sanson, ~03:22). Contrast with Chesky's "move at the speed of AI" framing (airbnb-earnings-q1-2026).
- non-engineer-builders: agentic-tool users are about double the ~2,000 active developers; a finance director wrote a 30-page VS Code onboarding guide and moved ops and finance onto AirChat in VS Code; Sanson (not an active coder for 10 years) built an internal browser in three days instead of a PRD and a three-month roadmap slot (~14:20).
- prd-agents: Pascal, built on the AirChat SDK, takes PMs and designers "from idea to concept brief", doing market research, reading the roadmap and pulling in business objectives (~15:39).
- spec-becomes-prototype-and-evals: "no more long requirement docs"; write a shorter concept brief and go straight to high-fidelity prototypes, five or ten of them; a designer vibe-coding prototype tool (~17:24).
- agent-factory-sdlc: named pain: after a prototype teaches something, the doc is not updated and reviews are out of order; idea of an AI project coordinator that creates Jira tickets and keeps artifacts in sync ("early days") (~17:24).
- cost-control-routing: AirChat CLI is a thin wrapper around coding agents that routes all API calls through one gateway for cost control and standard usage metrics (Capps, ~26:30).
- skills-marketplace: a community-managed plugin ecosystem and marketplace with many skills and instruction markdown files, plus centrally managed pieces (~05:21).
- remote-agent-invocation: AirChat Remote: sessions (parallel) and tasks (async) in one web UI; triggers from Slack, on-call channels, failing PRs; schedules being added; agent daemon per worker wraps runtimes behind ACP (~33:17).
- shared-persistent-sessions: long-running non-local environments that keep context so migrations can run while the laptop is closed; dynamic "next step" buttons (rebase, open PR) instead of chat.
- outcome-measurement-gap: metrics come from DX (vendor) instruments: TrueThroughput, survey-based AI-authored share, self-reported time saved; quality measured by change failure rate and maintainability sentiment.

## Key points
- Adoption (Sanson, June 2026): 97% of active engineers use agentic AI weekly, 90% daily; "it's Claude Code, it's Codex"; from about 0% to 97% in under a year.
- History: three years of AI work; early vendor autocomplete did not reach the latest models or all IDEs, so AirChat began as JetBrains and Xcode plugins; agentic AI launched early 2025.
- Productivity (Airbnb claims via DX metrics): PR throughput 65% above pre-agentic baseline, mostly since early 2026; developers using agents 4+ hours a day more than doubled PR output; AI-authored code about 59% vs an industry average near 27% (DX benchmark); devs report about six hours a week saved, over a third say 8+ hours.
- Survey shift: in Oct 2025, 3% said AI authors 80-100% of their code; six months later 28%.
- Quality: change failure rate down; maintainability sentiment up; change confidence flat (attributed partly to migration and tech-debt work).
- Migration framework: validate, transform, validate loop per target; "dozens" of migrations; saves a few months up to seven years each; "about a 5X speed up" (Capps).
- SDK: language-agnostic protocol, bidirectional streaming, client-configurable prompts, tools and hooks; build time for an app down from a day or two to 2-4 hours; about 40 apps. Datako (data query tool with guardrails over business data) has high hundreds of daily users.
- AirChat Remote runs on AirDev cloud workspaces: full toolchain and source control, network-isolated from production services and user data. EAP of about 50 users with PR throughput about 3x higher again (claim).
- Platform philosophy: aim to be 4-6 months ahead of what vendors ship; build modularly so pieces can be swapped for vendor tools; keep a stable paved path; let teams experiment unless security or cost is at stake.
- Predicted bottlenecks: code review volume, coordination, validation, infrastructure capacity.

## Notable quotes
- "We can build faster than we can align, I think sometimes." (Capps, ~33:17)
- "Coding now is cheap and fast and easy." (Sanson)

## Could not verify
- Numbers are self-reported and partly from a vendor's (DX) instruments; 59% "primarily AI-authored" is survey-based. Pascal is described in one sentence; how it pulls research, and whether its brief links back to evidence, is not shown.
