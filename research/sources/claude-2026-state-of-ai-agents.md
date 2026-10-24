---
title: "The 2026 State of AI Agents Report"
source_url: https://claude.com/resources/guides/the-2026-state-of-ai-agents-report
author: Anthropic (with research firm Material)
publisher: Claude (claude.com/resources)
published: 2025-12-09
retrieved: 2026-10-24
type: report
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [pm-ai-usage-surveys, vendor-claims-vs-independent-evidence, build-vs-buy, org-context-grounding, outcome-measurement-gap]
relevance: medium
---

## Relevance to the project
An Anthropic-commissioned survey of 500+ US technical leaders that puts numbers on agent adoption beyond coding, including "product development" agents (48% plan to build) and planning/ideation time savings (58%), but it is self-reported sentiment from a vendor's own study, not measured outcomes. Its most useful findings for the project are structural: a hybrid buy-and-build approach dominates (47%), integration (46%) and data access/quality (42%) are the top barriers, and Anthropic's Economic Index section names context, not model capability, as the real bottleneck. That supports grounding a product agent in org context and treating build-vs-buy as a menu, not a binary. The 80% "measurable ROI" headline is respondent agreement with a statement, with no definition of measurement; treat it as sentiment.

## Themes
- pm-ai-usage-surveys: 500+ technical leaders (engineering leaders, IT executives), late 2025; respondents are technical, not PMs (Foreword, Survey methodology).
- vendor-claims-vs-independent-evidence: survey commissioned and published by Anthropic; customer case results (Novo Nordisk, L'Oreal, eSentire etc.) are customer claims, unaudited (ch. 5).
- build-vs-buy: 47% both buy off-the-shelf and build in-house, 21% primarily buy, 20% build with APIs/toolkits; enterprises 54% hybrid (ch. 2).
- org-context-grounding: Economic Index section says each 1% more input context is associated with 0.38% higher output quality/length, and calls data accessibility and context aggregation the main barrier (ch. 6, "Context is the real bottleneck").
- outcome-measurement-gap: 80% "agree" their agent investment has "already delivered measurable financial impact", but no method or metric is defined; only 20% cite unclear ROI as a barrier (ch. 3, ch. 4).

## Key points
- **Method (Foreword):** Anthropic with research firm Material surveyed "over 500" US technical leaders across company sizes and sectors in late 2025. No sample breakdown by size, no response rate, no questionnaire published. Charts are split Startups & SMBs / Mid-Market / Enterprises.
- **Workflow complexity (ch. 2):** 57% deploy agents for multi-step workflows (29% within one department, 16% cross-functional, 12% autonomous with limited oversight); 81% plan more complex use cases in 2026 (ch. 4).
- **Coding (ch. 2):** 86% use coding agents across the SDLC; 42% use them "to lead development, with humans in the loop to review code and set strategy"; 40% to build complete features with limited human review. Time freed is near-even across phases: code generation, research/documentation, review/testing (59% each), planning and ideation (58%).
- **Beyond coding (ch. 3):** planned agents in the next 12 months: research and reporting 56%, supply chain 49%, product development 48%, FP&A 47%, regulatory compliance 41%. Most impactful today: data analysis and report generation 60%, internal process automation 48%, knowledge-base summarising 41%, competitor/market monitoring 30%.
- **Expected outcomes (ch. 3):** efficiency 44%, quality 37%; "stronger compliance or risk management" only 23%.
- **Barriers (ch. 4):** integration 46%, cost 43%, data access/quality 42%, security/compliance 40% (44% at enterprises), employee resistance/training 39% (51% at SMBs), lack of expertise 35%.
- **Work shift (ch. 4):** respondents say employees spend more time on learning (70%), strategic/creative work (66%), relationships (60%); oddly 56% also say more time on routine tasks, which the report does not discuss.
- **Optimism chart caveat (ch. 4):** the optimism question is reported for a subset, "director+ using only off-the-shelf AI agents", though later text cites 96% optimistic as if for all respondents.
- **Case stories (ch. 5), all customer claims:** Doctolib's platform team ships a central repo of prompts, custom commands and subagents every engineer pulls at setup, and runs Claude Code headless in CI to open maintenance PRs and update docs on every change (40% faster shipping claimed); Novo Nordisk says non-technical staff prototype with Claude Code; L'Oreal uses Claude as orchestrator over specialised data agents (99.9% accuracy claimed, metric undefined); eSentire validated against 1,000 real investigations for 95% senior-analyst alignment; Parcha replaced a two-year in-house workflow engine with the Agent SDK.
- **Partner outlooks (ch. 6):** Accenture (stateful, resumable MCP infrastructure), BCG (early wins from constrained agents; quality controls must evolve for non-human work product), Deloitte (the risk is regressing to old behaviour after workflow redesign).
- **Economic Index excerpts (ch. 6):** 77% of business API usage is automation-pattern (vs about 50% consumer); directive conversations rose from 27% to 39% over eight months; tasks needing regulatory approval or dispersed tacit knowledge see minimal adoption.
- **Limits:** technical respondents only; no PM or designer voice; all outcome figures self-reported; no failure or abandonment data.

## Companion pages
- https://claude.com/resources/articles/how-enterprises-are-building-ai-agents-in-2026 (launch article, 2025-12-09, summarises the headline figures)
- Report chapters: /foreword, /research-insights-part-i-the-current-landscape, /research-insights-part-ii-going-deeper, /research-insights-part-iii-the-path-forward, /ai-agents-in-production, /outlooks-and-perspectives (all under https://claude.com/resources/guides/the-2026-state-of-ai-agents-report/)

## Notable quotes
- "Tasks requiring regulatory approval, dispersed tacit knowledge, or capabilities AI can't handle see minimal adoption." (ch. 6)
- "Quality controls and managerial systems need to evolve to handle non-human work product." (ch. 6, BCG)

## Could not verify
- Exact sample size, size-band split and questionnaire wording; the downloadable PDF was not read.
- Published date is that of the launch article; the report pages carry no date.
- How "measurable financial impact" or the L'Oreal 99.9% accuracy were measured.
