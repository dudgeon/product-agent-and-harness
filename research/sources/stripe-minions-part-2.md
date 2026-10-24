---
title: "Minions: Stripe's one-shot, end-to-end coding agents - Part 2"
source_url: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
author: Alistair Gray (Stripe)
publisher: stripe.dev blog
published: 2026-02-19
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, human-review-gates, single-agent-many-skills, agent-factory-sdlc]
relevance: high
---
## Relevance to the project
A large engineering org's account of unattended agents on pooled devboxes: full permissions inside an isolated QA devbox, no human credentials, a small curated MCP toolset, hard cap of one CI iteration plus one retry, then handoff to a human. Offers a counter-pattern to multi-user live sessions (one-shot, per-task, human-review at the PR). Vendor-of-self claim, no independent audit.

## Themes
- human-review-gates: every minion PR is human-reviewed; a minion gets one full CI iteration plus one retry, after which the branch goes back to a human
- shared-persistent-sessions: blast radius bounded by environment not by prompts: devboxes (EC2, pre-warmed, ~10 s) run in QA with no real user data, production services or arbitrary egress; engineers run about half a dozen at once
- single-agent-many-skills: 'Toolshed' internal MCP server with nearly 500 tools but a small curated subset per agent; blueprints mix deterministic nodes with agent nodes

## Key points
- Scale claimed: over 1,300 PRs merged weekly (up from 1,000 in Part 1); more than three million tests as feedback.
- Per the retrieval, the post does not say how runs are started; search results elsewhere say Slack (not confirmed here). Some secondary sources swap the Part 1/Part 2 labels.

## Could not verify
- Part 1 post not fetched.
