---
title: "Building a Natural Language Interface to the Spotify Ads API with Claude Code Plugins"
source_url: https://engineering.atspotify.com/2026/5/spotify-ads-api-claude-plugins
author: Alex Murphy (Staff Software Engineer, Spotify)
publisher: Spotify Engineering blog
published: 2026-05-01
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [pm-tool-connectivity, skill-standards, human-review-gates]
relevance: low
---

## Relevance to the project
A side case: Spotify ships an open-source Claude Code plugin that turns plain-English ad goals into Ads API calls. It explains why they chose a CLI plus OpenAPI spec over MCP (a big API would flood context with tool definitions) and why every call is shown as an editable curl command before it spends money. Relevant to how we expose large tool surfaces to agents and keep humans in the loop on costly actions.

## Themes
- pm-tool-connectivity: CLI-first with the 8,600-line OpenAPI spec as source of truth; OpenAPI links act as a workflow graph (campaign, ad set, ad).
- skill-standards: plugin is Markdown skills, an agent, a PreToolUse hook for OAuth, a bash script and two Python helpers; listed in Anthropic's plugin marketplace.
- human-review-gates: every call shown as curl so users can audit before budgets are affected; respects the user's confirmation preference.

## Key points
- Fixing an API quirk often means adding one sentence to a Markdown file.
- Limits: Claude Code and macOS only; simple flows; idempotency keys not yet done.
