---
title: Internal AI tools for non-engineers (Department of Product PDF)
source_url: https://drive.google.com/file/d/18FcgDw6V04RntXJ_TOIL7c1NoWwAPiex/view
author: Rich Holmes (Department of Product)
publisher: Department of Product (Google Drive PDF linked from the paid Stripe Kai deep dive)
published: 2026-08-04
retrieved: 2026-10-24
type: report
evidence: independent
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [tacit-knowledge-capture, non-engineer-builders, org-context-grounding, enablement-by-product, skills-marketplace]
relevance: medium
---

## Relevance to the project
A three-page comparison table of 15 internal AI tools and practices for non-engineers (Stripe, Intercom, Asana, Retool, Spotify, Atlassian, DoorDash, Dropbox, Instacart, Gusto ×2, Block, Figma, Rippling, Uber). Each row has what it does, its impact, who uses it, and a source link. It widens our peer set beyond Stripe, Ramp and Shopify. Three rows bear directly on the context-creation hypothesis, so I read their primary sources and filed them: Spotify's expert-curated "context layer" ([note](spotify-engineering-vedder-context-layer.md)), Intercom's rule that a feature isn't shipped until the support agent can answer about it ([note](intercom-fin-npi-agent-readiness.md)), and Uber's Agentic Pods, where engineers shadow domain experts ([note](x-praveen-uber-agentic-pods.md)). The table itself is a secondary summary, with the author's own categories and "unverified" flags.

## Themes
- tacit-knowledge-capture: Spotify Vedder: "domain experts each own a cluster of datasets, vetted question-and-SQL examples, and business docs", with curators rejecting 87.5% of auto-generated SQL examples. Intercom Fin NPI: "knowledge freshness a hard sign-off alongside engineering and design". Uber Agentic Pods: engineers "shadow employees to learn a workflow end-to-end".
- org-context-grounding: Atlassian Rovo "Definitions" (highlight a term, get a definition sourced from company docs); Rippling AI answers with live data under role-based permissions and shows the SQL behind each answer.
- non-engineer-builders: Asana's AI Teammate triages sales and partner requests from Slack into tasks (3-4 days to minutes; ~165 hours and ~$100k a year, per the table).
- skills-marketplace: Figma "Skills" turn frequent prompts into shared slash commands for design teams.
- enablement-by-product: Uber's Agentic Pods are an adoption practice, not a tool.

## Key points
Rows, as categorised by the author (category; date):
- Stripe Kai (cross-functional agent platform; Jul 30, 2026).
- Intercom Fin NPI (knowledge retrieval and workplace context; Jun 26, 2026).
- Asana AI Teammate for the revenue team (cross-functional; Jun 26, 2026).
- Retool AI model registry (governance and infrastructure: one hosted JSON of models and prices, refreshed live; Jul 30, 2026).
- Spotify Vedder context layer (knowledge retrieval; Jun 10, 2026).
- Atlassian Rovo Definitions (knowledge retrieval; "live by 2026").
- DoorDash "Ask DoorDash" agent platform: a Gateway that authenticates, assembles context and translates clients to a shared agent-to-agent protocol, plus MCP and Skills (governance and infrastructure; Jul 24, 2026).
- Dropbox Riviera content processing extended for AI (Jul 20, 2026).
- Instacart Blueberry on-call agent (Jul 2026).
- Gusto Universal Document Processing (Feb 2026).
- Gusto persistent storage for agents (flagged "unverified, no public source").
- Block Buzz: an open-source workspace where humans and agents are equal participants with portable cryptographic identities (Jul 21, 2026).
- Figma skills for its design agent (Jun 24, 2026).
- Rippling AI (~Jul 28, 2026).
- Uber Agentic Pods (2026).

## Could not verify
- Only the Spotify, Intercom and Uber primaries were read. The other rows' figures (e.g. Asana's $100k a year) are the table's summaries and were not checked. Read through Geoff's browser session; the PDF was not downloaded.
