---
title: "Stripe's AI minions ship 1,300 PRs weekly from a Slack emoji | Steve Kaliski (How I AI)"
source_url: https://www.youtube.com/watch?v=o5Mi5SYSDnY
author: Claire Vo (host), Steve Kaliski (software engineer, Stripe)
publisher: How I AI; summary at https://www.chatprd.ai/how-i-ai/stripes-ai-minions-ship-1300-prs-weekly-from-a-slack-emoji
published: 2026-03-24
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [remote-agent-invocation, shared-persistent-sessions, non-engineer-builders, human-review-gates, harness-over-model, build-vs-buy, agent-frameworks]
relevance: high
---

## Relevance to the project
Fills the gap noted in the Minions Part 2 note ("does not say how runs are started"): minions start from a **Slack emoji reaction** on any message (the message becomes the prompt), from Google Docs, tickets or Slack threads, including from a phone; the engineer follows along in Slack and can drop into the devbox (VS Code web or Claude Code with Stripe's MCP tools). Kaliski runs minions in a **public Slack channel** ("Steve Kaliski robots", 76 humans) so others watch and "pair prompt": an open-by-default visibility choice. Non-engineers are starting to use it because "the entire company's in Slack". Bears on remote-invocation-route, agent interface (Slack as front door), trust/privacy defaults and adoption.

## Themes
- remote-agent-invocation: reaction "create-minion pay-server" selects the repo; a devbox agent replies in-thread with branch and "follow along" link (07:50-08:30). Kicked off from Slack on the phone "on the subway" (18:40).
- shared-persistent-sessions: the robots channel "started off as just me and my robots, and now there's ... audience observing"; "we don't pair program anymore but we ... pair prompt" (06:30, 12:40).
- non-engineer-builders: "We're starting to see more non-engineer usage there" because a PM brief or design feedback is "in effect just writing a prompt" (24:00).
- human-review-gates: ~1,300 PRs/week "no human assistance besides review"; confidence comes from CI, synthetics, blue-green deploys and rollback "independent of the nature of the authoring" (22:00).
- harness-over-model: minions sit on years of devex investment: hosted devboxes, CI, docs; "if there's a very blessed path for 90% of the common activities ... the propensity that the agent succeeds [is] really high" (10:00).
- build-vs-buy / agent-frameworks: forked Goose as a base loop; Claude Code and Cursor are also widely available; "there's no singular tool to rule them all" (14:00-15:30).

## Key points
- Bots help write prompts by searching code, PRs and Google Docs; "most things that could have an MCP server have an MCP server" (12:20).
- If coding becomes free, bottlenecks shift to review, idea supply and distribution (23:00).
- Second half is a machine-payments demo (agent pays third-party services; $5.47 total); not about internal agents.

## Could not verify
- Auto-caption transcript ("Khaliski", "Strike"); 2-minute timestamp buckets. Non-engineer usage is qualitative, no numbers.
