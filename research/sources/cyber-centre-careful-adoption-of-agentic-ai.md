---
title: "Careful adoption of agentic AI services (joint guidance: CISA, NSA, ASD ACSC, Cyber Centre, NCSC-NZ, NCSC-UK)"
source_url: https://cyber.gc.ca/en/guidance/careful-adoption-agentic-ai
author: CISA, NSA, ASD ACSC, Canadian Centre for Cyber Security, NCSC-NZ, NCSC-UK
publisher: cyber.gc.ca
published: 2026-04-30
retrieved: 2026-11-22
type: docs
evidence: first-party
filed_by: research-future-of-product
themes: [identity-delegation, agent-protocol-security, human-review-gates, agent-stewardship]
relevance: high
---

## Relevance to the project
The first joint Five Eyes guidance on agentic AI gives concrete controls the bank-side identity and authority truths presuppose: a distinct cryptographically anchored identity per agent, a trusted registry, least privilege with short-lived credentials re-checked on every request, human approval for high-impact actions decided by operators not the agent, and full logging of reasoning, tool calls and privilege changes. It also states a phased, low-risk-first adoption posture.

## Themes
- identity-delegation: each agent a distinct identity in a trusted registry; deny agents or keys not registered; avoid borrowing an employee's session (confused deputy)
- human-review-gates: when approval is needed is set by designers or operators, not delegated to the agent; log-deletion requests quarantined for human review
- agent-stewardship: define legal accountability and risk ownership in governance policy

## Key points
- Risk categories: privilege, design and configuration, behavioural, structural, accountability.
- Privilege: minimum access, narrow scope, just-in-time credentials for high-impact actions, authorisation re-verified per request rather than at startup.
- Logging: all agent operations including reasoning, tool calls, identity or privilege changes; unified logs for inter-agent interaction; automated analysis plus human review.
- Adopt incrementally, expand autonomy gradually, be ready to roll back, fail safe and escalate when uncertain.

## Could not verify
- Release date varies in sources (30 April or 1 May 2026); page shows modified 2026-09-10. Guidance is cyber-security guidance, not financial-services supervision, and says nothing on segregation of duties per se.
