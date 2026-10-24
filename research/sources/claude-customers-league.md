---
title: How League went all in on Claude in a regulated industry
source_url: https://claude.com/customers/league-qa
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [risk-sloped-review, non-engineer-builders, enterprise-admin-controls, task-context-isolation, spec-becomes-prototype-and-evals]
relevance: high
---

## Relevance to the project
A regulated healthcare software company (health plans, protected health information) reports going company-wide on Claude in under a quarter, with patient data kept in a separate environment Claude cannot reach and a Claude bot that triages every pull request by size and risk. It is one of the few filed accounts of an agent rollout inside a regulated business that names its controls (data separation, tiered model access, connector scoping) and its review routing. It also shows product work reshaped into "bets" that return working prototypes instead of decks. All outcome numbers (cycle time halved, 98% AI-authored code) are the customer's, published by Anthropic and unaudited.

## Themes
- risk-sloped-review: a principal engineer built a Claude bot that triages every PR by scale of change and risk so review does not become the bottleneck; vendor security risk assessments run by a Claude skill are signed off by a human (case study, "Shipping to production in 48 hours"; "The outcome").
- task-context-isolation: patient data is kept in a separate environment Claude has no access to; agents had strict limits while controls were put in place (case study, "The solution").
- enterprise-admin-controls: CEO cites tiered model access, control over which connectors are available to whom, and spend/usage transparency as what made regulators' concerns answerable (Q&A, final answer).
- non-engineer-builders: finance built 60+ automated month-end, quarter-end and payroll processes; designers open PRs to fix UI bugs; COO schedules overnight tasks; the AVP of AI Transformation, with no engineering background, opened a PR (Q&A; case study "Everyone becomes a product developer").
- spec-becomes-prototype-and-evals: R&D runs on "bets" where a small team spends 2-3 weeks and returns a working prototype for the market; customer pitches use working demo agents instead of Figma or slides (Q&A final answer; case study "Half the cycle time").

## Key points
- **Adoption path:** no formal evaluation; leadership skipped a bake-off ("your bake-off is going to be wrong as soon as you finish"), committed to a minimum spend after Opus 4.5 (December), signed Enterprise on a Friday and had the company live by Monday. Security foundation took about a quarter. Adoption 80% to 98%.
- **Forcing function:** a 48-hour "Accelatron" in March 2026: take real backlog items to production in 48 hours. Two-week sprints became micro-sprints of 3-4 people landing flagged production code in one sitting ("two weeks of scope ... in three hours").
- **Swarm:** League's own orchestration layer: a lead agent decomposes work and spawns parallel agents that write code, run tests and open PRs overnight; an engineer reviews in the morning; nothing ships without sign-off. Up to 50 parallel agents mentioned. The Q&A says Swarm is built on Claude Code, the case study says on the Claude Platform.
- **Hard problem example:** a system that reads League's own agent-quality scores and rewrites the failing agent's prompt automatically, guarded against overfitting to test cases; landed as eight stacked PRs (about 48,000 lines, 271 files) so each layer could be reviewed separately. League says Claude independently arrived at an approach matching GEPA.
- **Customer-reported outcomes (unaudited):** idea-to-PR cycle time halved in four months; AI-authored code from about 70% to 98% (tracked on their engineering metrics platform); 2-3x PRs merged per engineer per week; vendor security risk assessments from weeks to 15 minutes (49 of last 53 judged safe by Claude, then human sign-off); one implementation two months early.
- **Role blurring:** compliance, legal, finance and the COO now code; town-hall decks are made in Claude Design with the company design system.
- **Limits:** no quality, incident or defect data; no description of how the PR risk-triage bot classifies or what it lets through; "98% AI-authored" is not defined. Dan Galperin is called CEO in the Q&A and CTO in the case study.

## Notable quotes
- "None of it ships until an engineer reviews it and signs off." (Jordan Christensen, SVP Data and AI Engineering)
- "Before, we would show up with a PowerPoint or a Figma prototype. Now we're showing up with the working prototype." (Dan Galperin)

## Companion pages
- https://claude.com/customers/league (case study: "League cuts product development cycle times in half with Claude")

## Could not verify
- Publication dates of both pages; how cycle time and AI-authored share are measured; the risk tiers used by the PR triage bot.
