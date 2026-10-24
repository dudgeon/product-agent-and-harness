---
title: How Delivery Hero's agent merges 100+ pull requests a day with Claude
source_url: https://claude.com/customers/delivery-hero
author: Anthropic (quoting Rodrigue Schäfer, Vice President of Platform, Delivery Hero)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [remote-agent-invocation, human-review-gates, harness-portability, agent-failure-modes]
relevance: medium
---

## Relevance to the project
Delivery Hero's Herogen takes Jira tickets, writes and tests code and opens PRs that a mixed Claude-and-Gemini "council of agents" reviews before a human's final check; the company claims over 100 merged PRs a day (about 9% of all PRs) and an 85% ticket success rate. It shows a ticket-to-PR route to agent invocation, deliberate multi-model review to avoid shared blind spots, and model access via a LiteLLM proxy on Google Cloud so engineers keep their own tools. The VP's warning that five times more changes means five times more incidents at a constant failure rate names the downstream bottleneck. Bears on remote-invocation-route, model-provider-coupling, review-and-autonomy. Engineering-only; numbers are the customer's claims.

## Themes
- remote-agent-invocation: Herogen "picks up tasks assigned through Jira", writes code, iterates on tests, submits a PR; roadmap adds Slack handoffs and calling it into existing PRs (§The outcome, §Looking ahead).
- human-review-gates: a "council of agents" of Claude and Gemini reviews from different perspectives "before a human does a final check"; multi-model by design (§The outcome).
- harness-portability: a LiteLLM proxy in front of Google Cloud's model service routes engineers to any model "hooked up with whatever tools they use"; Claude is about 95% of requests by choice, not lock-in (§The solution).
- agent-failure-modes: "If you churn out five times more changes ... you will have five times more incidents if the change failure rate remains at the same level"; investing in agent-driven operations and safer rollouts (§Looking ahead).

## Key points
- **Claims.** More than 100 merged PRs a day from Herogen, about 9% of all PRs; 85% success on assigned tickets, most with zero or one developer interactions; Q1 2026 ended at 18x the original 100-PR goal; cross-repo changes across hundreds of codebases "in minutes"; CTO-group survey 9 to 2 for the Claude setup.
- **Origin.** A self-funded virtual team (one principal, two staff engineers) inside the platform org; MVP with one merged PR in Q4 2025; GA in February 2026. Primary model Claude Opus 4.5.
- **Fit.** Strongest on many-repo infrastructure config updates and refactors; Claude Code is kept for exploratory, interactive work (e.g. a design-system overhaul across 100 UI components).
- **Adoption.** Only about 15% of engineers use Herogen so far; target 50% of 4,000+ engineers on Claude and "every fifth" merged PR from Herogen in 2026; a team will build a Claude tool stack with built-in context for payment, order and infrastructure APIs.
- **Organisational point.** Schäfer credits better models, not tooling, for the change; centralising a federated set of acquired companies' platforms took a year and a half of persuasion.
- **Limits.** "Success rate" and "interaction" undefined; no quality, revert or incident data for Herogen PRs; PR count is a volume measure.

## Notable quotes
- "The tooling itself wasn't the main driver of the success of agentic engineering." (Rodrigue Schäfer)

## Could not verify
- Publication date (page undated; refers to Q1 2026 results).
- Definition of the 85% success rate.
