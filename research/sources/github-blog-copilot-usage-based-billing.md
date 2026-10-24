---
title: GitHub Copilot is moving to usage-based billing
source_url: https://github.blog/?p=95572
author: Mario Rodriguez (GitHub CPO)
publisher: The GitHub Blog
published: 2026-04-27
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [cost-control-routing, enterprise-admin-controls]
relevance: medium
---

## Relevance to the project
From 2026-06-01 Copilot replaced premium requests with token-metered "AI credits", pooled across a business, with budgets at enterprise, cost-centre and user level and a choice to cap or allow overage. This is the vendor-native version of the per-project meter in the cost-control-routing theme, and it changes the cost model for agentic sessions (cloud agent, partner agents, code review also burning Actions minutes).

## Themes
- cost-control-routing: credits consumed by input, output and cached tokens at each model's published API rate; "pooled included usage across a business"; budgets at enterprise, cost centre and user levels; when the pool runs out, "organizations can choose whether to allow additional usage at published rates or cap spend."
- enterprise-admin-controls (proposed): "Fallback experiences will no longer be available": no silent downgrade to a cheaper model once usage runs out; access is governed by remaining credits and budgets.

## Key points
- Plan prices unchanged: Business $19/user with $19 credits, Enterprise $39/user with $39 credits; promotional extra credits June to August ($30 Business, $70 Enterprise per month).
- Completions and Next Edit suggestions stay included.
- "Copilot code review will also consume GitHub Actions minutes."
- Agentic sessions are called far more compute-intensive; no specific billing detail for cloud or partner agents in the post (the third-party agents page says they consume Actions minutes and AI credits).

## Could not verify
- Budget mechanics in the billing docs were not read. Model-summarised fetch.
