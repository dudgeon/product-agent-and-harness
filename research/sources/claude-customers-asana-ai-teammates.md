---
title: How Asana built AI Teammates on Claude Opus 4.6
source_url: https://claude.com/customers/asana-qa
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [human-review-gates, identity-delegation, enterprise-admin-controls, cost-control-routing, build-vs-buy]
relevance: medium
---

## Relevance to the project
Q&A with Asana's CPO on AI Teammates, built on Claude Managed Agents: each teammate has its own Asana account, works inside existing project permissions, records every action in task history, and follows the rule "autonomous on execution, but humans own the decisions". It adds stack and governance detail (multi-agent architecture, different Claude models per subagent, admin on/off plus user-level scoping) to the companion article on coaching agents. All claims are the customer's, about its own product, on Anthropic's customer page; the one time figure (days to a fifteen-minute review) is unaudited.

## Themes
- human-review-gates: "autonomous on execution, but humans own the decisions"; drafting, triage and flagging compliance gaps are execution, judgement calls are surfaced to a human with context; autonomy adjustable by stakes.
- identity-delegation: an AI Teammate has its own Asana account like any colleague; invoked by assignment, @mention or workflow rule.
- enterprise-admin-controls: admins control access to AI Teammates; users control which are active, what they access and what actions they take; every action recorded in task history; customer data not used for training. Framed as the answer to CIO "agent sprawl" worries.
- cost-control-routing: multi-agent architecture with a top-level coordinating agent on Claude and different Claude models per subagent to trade speed against reasoning.
- build-vs-buy: Managed Agents "removed a lot of the undifferentiated heavy lifting" so Asana's team focused on Work Graph integration; Agent Skills cut development time for SharePoint/OneDrive document editing.

## Key points
- Collaboration thesis: Bose argues per-person assistants increase the "coordination tax" and fragmentation; agents fail at work tasks for lack of context more than intelligence.
- Example teammates: Campaign Brief Writer (marketer files objective and audience; agent drafts a structured brief; Asana claims days of back-and-forth became a fifteen-minute review cycle); Launch Planner (monitors cross-functional launch workstreams, flags dependencies, reports status; program manager reviews a summary instead of stitching spreadsheets); a teammate that reviews a project's task history and drafts a status update with next steps.
- No-code creation: describe the role, give instructions, point at projects; examples given are a compliance checklist reviewer and an HR request triager.
- Bose claims Claude follows instructions "to the letter and no further", so teammates won't overreach; this is a model-behaviour claim, not a control.
- Future: more multi-app workflows, learning from team patterns, Agent Skills to systematise work.
- Limits: no adoption, accuracy or error data; no description of how escalation of "judgement calls" is detected.

## Notable quotes
- "AI Teammates should be autonomous on execution, but humans own the decisions." (Bose)

## Could not verify
- Publication date (page shows none; references Opus 4.6 and Managed Agents).
