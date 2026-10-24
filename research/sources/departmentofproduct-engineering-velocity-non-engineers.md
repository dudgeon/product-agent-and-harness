---
title: "How to speed up engineering velocity with AI: a non-engineer's guide"
source_url: https://departmentofproduct.substack.com/p/how-to-speed-up-engineering-velocity
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-08-18
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [enablement-by-product, compounding-context-repo, agent-ready-intent, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
A mid-2025 guide for PMs on five topics to raise with a CTO about AI in engineering: onboarding, documentation, AI-written code, AI code review and adoption tactics. It is engineering-focused and mostly restates vendor case studies and surveys, so it adds little to the PM agent and harness question. Two items are worth keeping: a procurement pattern (attributed to Brex) where engineers spend a monthly budget on approved tools and the ones that spread get adopted company-wide, a bottom-up adoption model; and a legacy-code tool (attributed to Morgan Stanley) that first writes plain-English specs of old code, which developers then rewrite from. All company facts are second-hand.

## Themes
- enablement-by-product: Brex's "superhuman product-market-fit test": per-engineer monthly tool budget, company-wide adoption of whatever wins on use and praise (section 5). Related: [Brex on Claude Code](claude-brex-claude-code.md).
- compounding-context-repo: CLAUDE.md as the place to record code style, tests, repo etiquette and environment setup so new hires (and the agent) get up to speed; cites Anthropic's account of its teams ([How Anthropic teams use Claude Code](anthropic-how-teams-use-claude-code.md)) for Claude Code as the new-hire starting point (section 1).
- agent-ready-intent: the Morgan Stanley tool translates legacy code into English specs first, and engineers rewrite from those specs; 280,000 hours saved is the bank's claim via WSJ (section 3).
- vendor-claims-vs-independent-evidence: Jellyfish (5.1 hours of review time saved per quarter, up from 2.9), Graphite at Shopify (33% more PRs per developer, with stacked PRs), Glean (30% lower first-year turnover with onboarding assistants), all repeated without checks (sections 1, 4).

## Key points
- Onboarding: ask Claude Code how the codebase works; learning or study modes from Anthropic, OpenAI and Google for juniors; ElevenLabs uses its own voice agents for new-hire product tours.
- Docs: Amazon Q writing READMEs and diagrams via an AWS MCP server; Mintlify drafting docs from code and API specs and answering non-engineers' API questions (Perplexity playground, Replit changelog automation, per Mintlify).
- AI coding capabilities listed (natural-language-to-code, chat, autocomplete, code from Jira tickets, autonomous agents, PR summaries).
- Adoption: a survey shows paying for licences and encouraging experimentation as the top leader action.

## Could not verify
- None of the cited case studies, surveys or the WSJ report were opened.
- Paywalled; summarised, not reproduced.
