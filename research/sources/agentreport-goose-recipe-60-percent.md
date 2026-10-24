---
title: "Block Open-Sourced Goose: How a YAML Recipe File Scaled an AI Agent to 60% of the Company"
source_url: https://the-agent-report.com/2026/05/block-goose-ai-agent-recipe-runner-scaled-60-percent/
author: The Agent Report
publisher: The Agent Report
published: 2026-05-27
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-block-product-practices
themes: [one-job-per-agent, single-agent-many-skills, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
An aggregator piece that circulates two figures often repeated about Block: about 60% of roughly 12,000 employees using goose weekly, across 15 job profiles including product. It cites no source for either, and its "product manager triaging a Jira ticket" is a rhetorical example, not a reported case. Filed so the figure can be traced and discounted; its one useful contribution is a clear statement of the pattern (one binary, a directory of recipes, a directory of MCP servers), which Block's own docs support ([goose-docs-recipes](goose-docs-recipes.md)).

## Themes
- one-job-per-agent: argues the recipe (YAML: instructions, parameters, extensions, a stepwise prompt) is the unit that lets one agent serve many jobs, so Block does not build a separate review agent and triage agent (section "Why This Pattern Scaled").
- single-agent-many-skills: "one Goose binary, then ship a directory of recipes and a directory of MCP servers" (same section).
- vendor-claims-vs-independent-evidence: the 60% weekly and 15 job profiles figures carry no citation; the 12,000 headcount predates the February 2026 cut to under 6,000.

## Key points
- Claims PMs can author, copy and run recipes "no deploy, no code review, no engineering handoff"; presented as reasoning, not observation.
- Notes the move to the Agentic AI Foundation as lowering enterprise governance risk.

## Could not verify
- The origin of the 60% figure. A search summary attributes it to a Block open-source office post; not found.
