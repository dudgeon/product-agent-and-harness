---
title: How Zapier's marketing and engineering teams use Claude Cowork to delegate real work
source_url: https://claude.com/customers/zapier-cowork-qa
author: Anthropic
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [harness-portability, non-engineer-builders, risk-sloped-review, compounding-context-repo, metrics-review-agents]
relevance: medium
---

## Relevance to the project
Three Zapier non-engineers (product marketing, influencer marketing, AI automation) describe delegating multi-system work to Cowork, and the head of product marketing describes deliberately keeping skills as local files and tools behind a client-agnostic MCP server so they work across several AI platforms. That is direct customer evidence for the "keep assets portable, stay in vendor harnesses" option, from a company that runs several harnesses. Outcomes are anecdotes (a 15-minute homepage draft, an operations dashboard from 15 SQL queries) and vendor-claim.

## Themes
- harness-portability: Zapier stores skills in local files "instead of on Cowork specifically" for retrieval, editing and headless use across platforms, and routes tools through the client-agnostic Zapier MCP server (Q&A, "plugin and skills architecture").
- non-engineer-builders: a PMM builds landing-page mockups; an influencer marketer built a live GitHub Pages dashboard fed by a Zapier Table, scrapers, Bitly and Databricks (Q&A, Matt Brown and Joe Stych answers).
- risk-sloped-review: "Trust is task-dependent. People relax the loop for familiar work but keep review for novel or high-stakes stuff." (Q&A, trust answer)
- compounding-context-repo: at the end of each session the PMM asks "what should we remember from this?" and has Claude capture it so sessions compound (Q&A, homepage concepting).
- metrics-review-agents: an AI automation engineer ran 15 SQL queries across six engineering systems (GitLab, Jira, Productboard, OpsLevel, Jellyfish, incident tracking) in a Databricks warehouse to produce a team-by-team efficiency dashboard (Q&A, Larisa Cavallaro answer).

## Key points
- **Homepage concepting:** inputs are the live homepage plus a custom PMM skill (voice, positioning, page structure) and Zapier MCP access to Slack and Glean; Claude navigates the page in Chrome, identifies modules and writes an HTML mockup; about 15 minutes to a draft shared with the CMO and CEO. Replaces a design handoff before direction can be judged.
- **Operations analysis:** Cowork connected to the org database, Slack, docs and Jira; Databricks warehouse joins 11 source systems; output an interactive dashboard of friction points. No validation of the findings is described.
- **Skill examples:** PMM homepage concepting, daily Slack summaries, Jira triage.
- **Architecture view:** moving from "connect one app" to "install a workflow" that bundles config, skills and actions.
- **Scale claims:** 97% of employees use AI daily; "thousands" of agents deployed. An earlier Anthropic report (January 2026) cited 89% adoption and 800+ agents for Zapier.
- **Limits:** three individual accounts; no error, review-time or quality data; Zapier is itself an integration vendor and Anthropic MCP partner.

## Notable quotes
- "What's hard now is judgment: knowing when a line sounds wrong, catching a bad metric before it ships." (Joe Stych, Head of Product Marketing)

## Could not verify
- Publication date.
