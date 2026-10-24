---
title: "AI is approving our pull requests: Here's how we made it safe"
source_url: https://intercom.com/blog/ai-is-approving-our-pull-requests-heres-how-we-made-it-safe
author: Kesha Mykhailov and Niamh Young (Intercom)
publisher: The Intercom Blog (Engineering); also cross-posted at https://ideas.fin.ai/p/ai-is-approving-our-pull-requests (2026-04-24)
published: 2026-04-21
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [risk-sloped-review, human-review-gates, agent-factory-sdlc, evals-autonomy-trust, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
First-party description of Intercom's review and release rows: a PR-review agent split into sub-agents (problem description quality, diff-matches-intent, safety, logic, anti-patterns) that can auto-approve small low-risk PRs, with the shipping engineer still accountable for monitoring and rollback. It shows the review step checking the code *against the stated intent* in the PR, which is the key context handoff from "write the code" to "review". Self-reported figures; Intercom also sells AI products.

## Themes
- risk-sloped-review: the agent will not approve PRs that are too large, complex or broad and asks for them to be split; automated approval is optional and any engineer can request a human (Mechanisms).
- human-review-gates: "the engineer who ships a change must monitor it in production and be ready to roll back"; AI approval does not change this.
- agent-factory-sdlc: in the broader rollout 497 PRs in four weeks were fully autonomous: Claude wrote the code, the approval system reviewed, approved and shipped.
- evals-autonomy-trust: engineers flag whether each review comment was helpful and that feedback refines the Intercom-specific guidance; pilot of 100+ PRs had zero reverts before scaling; auditor Schellman engaged before scaling.
- vendor-claims-vs-independent-evidence: revert rates (backend 0.53% AI-approved vs 5.39% human; frontend 0.22% vs 2.00%), "about 5x faster" approval and 6-16x faster at p75 are self-reported with no revert definition or window.

## Key points
- Context: deploys "hundreds of times a day"; average merge-to-production 12 minutes; downtime from breaking changes down 35% while deployments doubled.
- Over 93% of PRs in the two main codebases are agent-driven; over 19% (19.2%) auto-approved with no human reviewer; about 60% evaluated by the AI reviewer.
- Every AI-approved PR is labelled, logged and queryable (review comments, decision, test results, merge event); frameworks listed: SOC 2, HIPAA, ISO 27001, ISO 42001, AIUC-1.
- Most large outages historically were not product-code changes; past product-code outages were all human-reviewed.
- Next: a separate agent to diagnose production issues proactively (stated plan, not built).

## Could not verify
- Eligibility criteria and risk tiers for auto-approval, rule text and owners, tools/models beyond Claude, rollback mechanics, feature flags, monitoring tools. (Curran's webinar Q&A adds some: see ideas-fin-webinar-qa-3x-rd-output.)
