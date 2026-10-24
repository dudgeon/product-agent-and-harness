---
title: "Anthropic's Third-Party Claude Crackdown: How It Hit OpenCode, Zed, and the Wider Tooling Ecosystem"
source_url: https://falcao.org/posts/anthropic-claude-access-crackdown-ecosystem-fallout/
author: Danilo Falcão da Silva
publisher: falcao.org
published: 2026-05-24
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-portability, cost-control-routing, build-vs-buy]
relevance: high
---

## Relevance to the project
The fullest dated timeline found of Anthropic's restrictions on third-party clients (January to June 2026). It shows the restriction is on subscription credentials, not on Claude itself: any open or third-party harness can still use Claude at API rates, and the Agent SDK gets a capped monthly credit. For an internal tool on company API or cloud-provider contracts, the crackdown changes cost comparisons, not feasibility. Independent blog; most steps attributed to named people, some unsourced.

## Themes
- harness-portability: subscription OAuth tokens work only in Claude Code and Claude.ai; affected OpenCode, Cline, RooCode, OpenClaw (2026-01-09).
- cost-control-routing: from 2026-06-15 programmatic use outside Claude Code is metered at API list prices beyond monthly "Agent SDK credits" ($20 Pro, $100 Max 5x, $200 Max 20x, no rollover).
- build-vs-buy: open harnesses lose the flat-rate subsidy; OpenAI moved the other way, extending Codex subscription support to OpenCode, OpenHands and RooCode (around February; author's reading).

## Key points
- 2026-01-09: server-side block of subscription tokens outside Claude Code; error "This credential is only authorized for use with Claude Code and cannot be used for other API requests."
- 2026-02-17 to 20: Consumer Terms updated; Free/Pro/Max OAuth tokens only in Claude Code and Claude.ai (Thariq Shihipar quoted).
- 2026-03-19: legal demands to OpenCode; Dax Raad merged PR #18186 removing Anthropic OAuth, the spoofed beta header and Anthropic provider references.
- 2026-04-04: Pro/Max no longer cover third-party tools (Boris Cherny quoted); transition credits ($100 Pro, $200 Max) until 2026-04-17.
- 2026-05-13: Agent SDK credits announced, effective 2026-06-15; Theo Browne's estimate of a 25x price increase for heavy users attributed.
- Still permitted: API keys billed per token (never blocked); Claude Code and Claude.ai on subscriptions; Agent SDK within credits then API rates.
- Feb 12 to 14: Google similarly blocked Gemini AI Ultra subscribers routing through OpenClaw (unsourced in article).

## Could not verify
- Zed-specific action (named in the title, not in the body). Anthropic's own announcements were not read first-hand in this round.
