---
title: "Inside Uber's software factory (Inside the Software Factory)"
source_url: https://software-factories.port.io/uber
author: Port (unnamed)
publisher: Port, "Inside the Software Factory" research index
published: 2026-10-11
retrieved: 2026-11-02
type: report
evidence: independent
filed_by: competitive-teardown-uber-cortana
themes: [vendor-claims-vs-independent-evidence, agent-control-plane, identity-delegation, cost-control-routing, org-context-grounding]
relevance: medium
---

## Relevance to the project
A cited fact sheet on Uber's software factory that lists the primary Uber sources with authors and dates and flags where Uber's own numbers conflict (context graph size, skills count, Minion share of PRs). It is the best map for chasing primary sources, though it says little about Cortana itself (only Slack/CLI/web and 20,000+ sessions a day). Bears on the teardown's evidence-quality section. Date is the page's "updated" date.

## Themes
- vendor-claims-vs-independent-evidence: Minion ~11% of merged PRs (May 2026, Uber blog) vs ~15% (Oct 2026 header, podcast) vs 11% of PRs opened (March 2026, Pragmatic Engineer); context graph "24M nodes and 80M edges" (efficiency blog) vs "forty million entries" (talk), units undefined.
- agent-control-plane: MCP gateway authorisation through Uber's Access Control System with charter policies for humans, services and agents; for third-party servers it relays the caller's user token (MCP gateway blog, 2026-10-01).
- identity-delegation: short-lived scoped tokens minted per hop with an actor chain; token exchange P99 under 40 ms ("Solving the Identity Crisis for AI Agents", 2026-05-21).
- cost-control-routing: cost per 1,000 requests down ~34% Feb-July; cost per session down 52% June-August; code mode cuts tokens 55-71%; weekly active users of agentic tools 7x Feb-Aug (efficiency blog, 2026-08-27).
- org-context-grounding: grounded agent answered in 38 s; ungrounded run took 20 min 9 s and was wrong.

## Key points
- Primary sources listed: Medisetty "Running a Software Factory Efficiently at Uber Scale" (2026-08-27); uReview blog (2025-08-12); identity blog (2026-05-21); AIE talk; "Uber Minion: 11% Agent-Generated PRs" (Nikhil Ramakrishnan, 2026-05-07); Pragmatic Engineer deep dive (2026-03-10); MCP gateway blog (2026-10-01); Pragmatic Engineer podcast (2026-10-14).
- MCP: 800+ servers and 5,000+ tools (gateway blog) vs 1,000+ servers (efficiency blog). Skills: 3,600+ skills and 30,000+ executions/day (efficiency blog) vs 2,500 and 20,000+ (talk).
- uReview: ~90% of ~65,000 weekly diffs; 75% of comments rated useful; 65% addressed in the same changeset; Uber later dropped hours-saved framing internally.

## Could not verify
- No personas, no Cortana permission model; the "carries forward existing user permissions" phrase found by search engines is not on this page.
