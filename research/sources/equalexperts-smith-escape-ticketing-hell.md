---
title: "Escape ticketing hell with a shift to self-service platforms"
source_url: https://www.equalexperts.com/blog/our-thinking/escape-ticketing-hell-with-a-shift-to-self-service-platforms/
author: Steve Smith (Equal Experts)
publisher: Equal Experts
published: 2024-08-15
retrieved: 2026-10-28
type: article
evidence: anecdote
filed_by: research-dependency-agent
themes: [platform-onboarding-friction, coordination-cost-and-waiting, process-governance-load]
relevance: high
---

## Relevance to the project
A consultancy practitioner's account of "ticketing hell" in large organisations, with two concrete cases: at a Dutch bank a new employee waited 11 weeks for access to code repositories because the request sat in the platform team's queue, and at an Australian telco every deployment to every environment needed a platform ticket, a "combinatorial explosion" that blocked deployments. It traces the pattern to ITIL-style central workflow management and proposes converting the slowest frequent ticket workflows into automated, audited self-service one at a time. That method (measure end-to-end time, pick the frequent slow task, automate with an audit trail, retire the ticket) is a template for what a dependency agent could drive.

## Themes
- platform-onboarding-friction: a task "that takes minutes to complete" can wait days or weeks in a queue; Dutch bank: 11 weeks for repository access (body). Evidence: anecdote from consulting engagements.
- coordination-cost-and-waiting: handoffs to DBAs for schema changes, change managers for approvals, operations for deployments; tickets move through triage, prioritised, blocked.
- process-governance-load: self-service workflows keep "automated guardrails and audit trails", visualised in a platform portal, so control is kept without the queue.

## Key points
- Costs: slower delivery against DORA metrics, low internal customer value, high platform cost (the platform team handles tickets alongside build and run), strained relationships, burnout.
- Root cause named: a long-standing ITIL-driven culture of central workflow management, where platform workload grows with each team and capability added.
- Rejects embedding platform engineers in product teams as unsustainable.
- Steps: measure end-to-end time of ticket workflows; prioritise a frequent and slow task; build an automated pipeline that does it consistently and logs each action; show the audit trail in a portal; migrate teams and retire the ticket; repeat.

## Could not verify
- The bank and telco are unnamed; the 11-week figure is a single case.
