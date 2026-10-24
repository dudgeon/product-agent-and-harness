---
title: What's New (University of Minnesota DevEx GitHub Enterprise change log)
source_url: https://github-docs.devex.oit.umn.edu/change-log/
author: University of Minnesota OIT DevEx team
publisher: github-docs.devex.oit.umn.edu
published: 2026-07
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-runtime-patterns-follow-up-round
themes: [cost-control-routing, enterprise-admin-controls]
relevance: low
---

## Relevance to the project
A rare public record from an enterprise administrator (not a vendor) of how Copilot was actually rolled out and cost-controlled: a small pilot, cost centres billed to departmental Azure subscriptions, MCP enabled only for pilot users, and, after June 2026 usage under the new credit model, a universal per-user cap. Illustrates the "open broadly, then meter after a spike" sequence seen at Ramp, from a regulated-ish public institution.

## Themes
- cost-control-routing: July 2026 entry: after the June move to usage-based billing, "we have created a Universal user budget of 40,000 AI credits per user per month"; usage stops at the cap; cost-centre budgets apply after the Enterprise Pool runs out; users are steered to Auto model selection because some models consume more credits.
- enterprise-admin-controls (proposed): MCP was enabled for pilot users only (September 2025) and required an Azure subscription to bill premium requests; Copilot only in repositories where it has been enabled (July 2025 pilot).

## Key points
- Timeline: July 2025 small pilot; September 2025 MCP for pilot users; October 2025 metered billing via Azure cost centres; November 2025 GA; July 2026 universal user budget.
- No entries on agents, third-party agents or audit.

## Could not verify
- The precise trigger ("runaway spend") appears in a search summary, not in the fetched text; the fetched text says only that the budget followed the June billing change. Exact entry dates beyond month not given.
