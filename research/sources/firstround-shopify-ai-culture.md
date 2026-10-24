---
title: "From Memo to Movement: Shopify's Cultural Adoption of AI"
source_url: https://review.firstround.com/shopify-ai/
author: First Round Review (interviewing Farhan Thawar and Shopify staff)
publisher: First Round Review
published: 2025-07-15
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [cost-control-routing, org-learning-loop, non-engineer-builders, outcome-measurement-gap]
relevance: low
---

## Relevance to the project
This is pre-River context from 2025: the LLM proxy, MCP collection, shared agents and Roast that later underpin River. Its main use for the teardown is as a **before/after**: in 2025 Shopify ran a *leaderboard* of Cursor-token spend as "a cool proxy for value". By mid-2026 Thawar says the leaderboard was removed for a usage dashboard (see [venturebeat-beyond-the-pilot-farhan-thawar](venturebeat-beyond-the-pilot-farhan-thawar.md)).

## Themes
- `cost-control-routing`: "We don't have a quota. And I don't want people to gamify it with scripts, but it's a cool proxy for value" (on the internal Cursor-token leaderboard). The LLM proxy is a single access point to many models, also used in production for scaling, tracking and failover.
- `org-learning-loop`: "once someone creates the Slack MCP, everyone can use it". There is "a stable of agents already created by other people for anyone to use".
- `non-engineer-builders`: a sales engineer's Cursor-built dashboard over GSuite, Slack and Salesforce MCPs. A LibreChat-based RFP agent with certainty scores that learns from winning answers. An agent that writes weekly project updates from GitHub PRs, issues and Slack.
- `outcome-measurement-gap`: an internal dashboard measures who uses Cursor, Claude Code and the proxy. Shopify found AI use "had a positive correlation with impact" and ties this to performance reviews.

## Key points
- Roast example: "The CodeAgent (built with Claude Code) summarizes its actions and why it took them" (Samuel Schmidt quote on deterministic + AI tools).
- Thawar: "Instead of just building the feature ... we'd rather spend longer building the infra."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- Page was modified 2026-10-07; the text read may include later edits, though no River mention was found.
