---
title: "Webinar Q&A: How Fin 3x'd R&D output in 16 months"
source_url: https://ideas.fin.ai/p/webinar-q-and-a-how-fin-3xd-r-and
author: Darragh Curran (CTO, Intercom / Fin)
publisher: Fin Ideas (Intercom Substack, ideas.fin.ai)
published: 2026-05-22
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [risk-sloped-review, evals-autonomy-trust, skills-marketplace, pm-persona-role-expansion, agent-failure-modes, single-agent-many-skills]
relevance: high
---

## Relevance to the project
Written answers to 72 webinar questions; fills in the review row (the "Shrek" reviewer: GitHub-webhook-triggered sub-agents in short-lived AWS containers using Claude and Codex, per-repo safety criteria, evals on curated historical PRs), skill governance (promotion at 50 weekly active users), and the role split (strong engineers take on PM work; PM and design move to "higher ambiguity" work near customers and GTM; designers ship small fixes and prototypes). It also names failure modes (an agent pushing hundreds of thousands of changes; red-herring incident diagnoses). Self-reported.

## Themes
- risk-sloped-review: eligibility for auto-approval uses PR size, risk and blast radius; first version was deterministic rules approving docs- and test-only changes; non-approved PRs go to human approval with Slack notification (Q: "How do you gate 'Eligible for Auto Approval'?").
- evals-autonomy-trust: Shrek evals are a human-curated set of historical PRs with confirmed issues; prompt/agent changes are re-run and measured for recall and precision with significance; "Building and curating a dataset is by far the hardest and most time consuming part."
- skills-marketplace: "hundreds of skills"; hierarchy of plugins (base plugin plus language, framework, team and product-area plugins, often off by default); private marketplace replaced by forced MDM updates; 50 weekly active users makes a skill eligible for the base plugin; unused skills removed.
- pm-persona-role-expansion: "what is a team today should be a single person on some near-ish timeframe"; strong engineers take on more PM work; PM and design focus on higher-ambiguity work closer to customers and GTM; designers ship, fix small bugs and prototype in parallel (Q: "Are eng moving up front to problem discovery...?").
- agent-failure-modes: an agent pushed "hundreds of thousands of changes" to the Rails monolith, breaking CI until GitHub repaired the repo; "Agents really will try anything to work around blockers"; open-ended incident investigation still WIP because agents "confidently identify plausible suggestions that are red herrings".
- single-agent-many-skills: Claude Code is the single primary tool (biased to Opus); Codex used in approval and review; an open tool policy was dropped.

## Key points
- Shrek infrastructure: isolated short-lived AWS containers triggered by GitHub webhooks; many specialised review agents in parallel; repo owners can add review requirements for their areas; anyone may edit reviewer prompts but changes need peer approval.
- Human accountability: "Engineers still need to have an opinion and take responsibility for the shape of the solution"; incidents get deep postmortems.
- Business outcome framing: shipping more is "required, but not sufficient"; best measures named as release throughput, idea-to-release time and tier-0 marketing releases; revenue "a lagging indicator".
- Harness team: three Principal/Senior Principal ICs, two Senior+ engineers, a Staff TPM and a VP Eng, about six months old; no major reorg.
- Cloud agents (internal "Buzz") are "a small contribution right now"; attribution to the person who started the work had to be fixed to drive use.
- Spend: no token budgets; fixing Playwright's high-resolution screenshots saved a projected $300k a year; all employees have Claude Code and Cowork access.
- Security: an agent could share internal info (e.g. private gists with spec files); locked down. Read-only production and warehouse access mirrors existing permissions.

## Could not verify
- No spec/PRD process or template, no planning or roadmap process, no deploy/on-call detail, no Shrek precision/recall figures.
