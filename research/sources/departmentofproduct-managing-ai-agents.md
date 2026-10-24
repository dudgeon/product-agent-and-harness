---
title: How to Manage AI Agents Effectively
source_url: https://departmentofproduct.substack.com/p/how-to-manage-ai-agents-effectively
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-08-10
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [cost-control-routing, enterprise-admin-controls, identity-delegation, evals-autonomy-trust, human-review-gates, agent-control-plane, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
A PM-audience map of "AI agent management" in five areas (spend, governance and security, identity and access, testing and safety, observability), each illustrated with roughly 20 company cases from mid-2026. It is the broadest single catalogue in the library of how companies govern agents once they run, and bears directly on the governance-control-plane, agent-identity-delegation and pm-agent-evaluation dimensions. Every company fact is second-hand, relayed from vendor blogs and press without links checked here, and several (agent-made exploits, a $1.8M wrong-model bill) are dramatic claims that need their primaries before use. Treat it as a list of leads and a framing, not as evidence.

## Themes
- cost-control-routing: three spend tactics (section 1): gateway budget limits (Databricks Unity AI Gateway, Vercel AI Gateway), model routing by task difficulty (Block's Buzz benchmark: priciest model about 5.5x the cost for about 9 points more quality), and dedicated spend products (Ramp Token Spend Management; Rippling AI Spend Console, which sets spend against PR volume and review rework).
- enterprise-admin-controls: Notion admin controls over who may create agents and what they reach; Anthropic adding OpenTelemetry export to Cowork so agent activity lands in existing observability stacks (sections 3 and 5).
- identity-delegation: Uber gave agents their own cryptographic identity inside its zero-trust setup because "who authorised what" was lost across agent hops; Block's User Identity Delegation carries the human and the agent as two identities through every downstream call (section 3).
- agent-control-plane: DoorDash's Agent Gateway, a single checkpoint every agent passes before any tool call (authentication, rate limiting, credential hand-off, plus an agent-to-tool allowlist); an AWS "Rex" runtime that blocks script operations unless a policy allows them (section 3).
- human-review-gates: Vercel runs coding agents in sandboxes and returns Git patches that a human must approve (section 3); Vanta PM Herman Errico's AARM proposal intercepts an agent's action before it runs so a person or system can check it is permitted (section 2).
- evals-autonomy-trust: DoorDash moved from about one human-submitted review a day to 2,000 LLM-judge-graded sessions daily (claimed 8-point quality gain, errors nearly halved, regression testing from 6+ hours to about 20 minutes); Airbnb's three layers (programmatic checks, LLM judge, human review) with judges calibrated to 80-90% agreement with humans; Gusto's schema-compliance scorers; Slack concluding agentic end-to-end tests complement, not replace, deterministic ones (section 4).
- vendor-claims-vs-independent-evidence: all figures above are company-reported and relayed without scrutiny; the post itself does not question any of them.

## Key points
- **What is agent management:** the operational layer for agents once they run against real users and systems, distinct from designing or prompting them. The framing shift: from "what can agents do" to "what are they actually doing". Three questions it says leaders now ask: cost per task/user/week; whether the agent gets its own identity or inherits the user's; whether legal or compliance must sign off before launch.
- **Spend:** the gateway is the one place all agent traffic must cross, so the natural point to enforce budgets. Rippling is called the most advanced because it ties spend to output rather than only reporting usage.
- **Governance:** Vanta open-sourced "Agentic Trust Controls", two groups of controls: how an agent is built (verifies the requester, limits actions, protects memory from tampering, has been attacked on purpose) and how it is run (inventory of every agent, who watches it, credential handling, review of vendor agents, staff training). The post argues ISO 27001/42001 predate agents.
- **Identity vs access:** identity is a trackable identity per agent; access is what each agent may do, where, and for how long.
- **Testing:** agent readiness as a launch checkpoint: Intercom made agent knowledge-base readiness a mandatory sign-off alongside engineering and design (primary filed: [Intercom NPI](intercom-fin-npi-agent-readiness.md)). Pinterest published a reliability testing guide.
- **Observability:** fold agents into existing stacks (OpenTelemetry); engagement analytics (Pendo Agent Analytics, citing customer Quorum at 64% "stickiness"; see [Pendo note](pendo-agent-analytics-fast-company.md)); monitoring as security (Microsoft agentic observability; Slack agents triaging billions of daily security events).
- A downloadable PDF and example list are offered to paid subscribers; not read.

## Notable quotes
- "the gateway is the one place all agent traffic has to pass through" (section 1)

## Could not verify
- None of the company claims were checked against primaries. Specifically unverified: Amazon's "$1.8 million" wrong-model spend; Uber's CTO having spent the 2026 AI budget; OpenAI agents forming a hidden message board and breaching Hugging Face; Anthropic finding Claude breached three companies in red-teaming; UK AISI logging 19 autonomous hacking attempts; product names "Herdr" (Vercel) and "Rex" (AWS); the model name "GPT-5.6 Sol".
- Block's Buzz benchmark is described both as "about 9 points" and "8.9 points"; the underlying scale is not given.
- Paywalled text summarised, not reproduced.
