---
title: Inside Shopify's AI-first engineering playbook
source_url: https://www.bvp.com/atlas/inside-shopifys-ai-first-engineering-playbook
author: Bessemer Venture Partners Atlas editors, interviewing Farhan Thawar (VP & Head of Engineering, Shopify)
publisher: Bessemer Venture Partners (Atlas)
published: 2026-04-02
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-shopify-river
themes: [cost-control-routing, identity-delegation, human-review-gates, outcome-measurement-gap, non-engineer-builders, harness-portability]
relevance: medium
---

## Relevance to the project
An interview with Shopify's head of engineering published about eight weeks before "Under the River". It does **not mention River at all**, even though River was in use by then (Tobi's May chart shows threads from March). It gives the platform context River sits on: the LLM proxy, MCP servers that preserve user permissions, Quick, and a mandatory human PR review. Evidence is first-party (exec quotes) but published by an investor's content arm.

## Themes
- `identity-delegation`: MCP servers connect AI to the wiki, GSD (the PM tool), the data warehouse, Salesforce, Slack and Google Workspace. "Because it's going through the same auth flow that you have ... it's not going to give me information that I don't have access to." This is user-delegated access for *assistant tools*. Whether River, a shared bot in public channels, uses the same model is not said.
- `cost-control-routing`: all requests go through one LLM proxy. "I can look at usage by team, by project, by person ... We get alerts if someone spends more than $250 in tokens in a day." Alerts lead to investigation, not shutdown. The ML infra team running the proxy is "pretty sure it's six engineers".
- `human-review-gates`: "Shopify is not yet at the place where we allow AI to check in code automatically into the repos ... We still require a human PR reviewer, which is now becoming a big bottleneck." Also: "the team never merges code without a senior engineer's review."
- `outcome-measurement-gap`: no LOC or PR-count KPIs ("easily gamed"). Weekly demos are the best signal. Reversion rate is "roughly the same" while PRs per week rose slightly. A roughly 20% productivity gain is "a humble estimate".
- `harness-portability`: "we always have one tool for one job—except for with AI". Cursor, Claude Code, Copilot, Codex and Gemini tools coexist.
- `non-engineer-builders`: Quick (drag-and-drop internal hosting) and "n-of-1 software" built by sales, finance and HR. Cursor adoption spread to sales, finance and HR.

## Key points
- AI-reflexiveness is assessed in the biannual performance reviews.
- Biggest long-term risk is "comprehension debt": engineers must understand systems "two or three layers below".
- Security: AI as a vulnerability-hunting "pairing partner" (IDOR prompt example), not trusted to write secure code by default.
- "The move in 2026 is agentic harnesses": parallel agents with human merge, or long critique loops.

## Notable quotes
- "Because it's going through the same auth flow that you have, it's not going to give me information that I don't have access to."
- "We still require a human PR reviewer, which is now becoming a big bottleneck."

## Full text

_Full text omitted from the public repository; see `source_url` for the original._

## Could not verify
- Whether "same auth flow" applies to River. Under the River reportedly mentions a credentials proxy (per adaptordie.io), but the mechanism is undocumented in these secondary sources.
- The reversion-rate claim has no numbers.
