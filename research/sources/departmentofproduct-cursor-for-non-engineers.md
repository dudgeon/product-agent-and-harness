---
title: How to use Cursor for Non-Engineering use cases
source_url: https://departmentofproduct.substack.com/p/how-to-use-cursor-for-non-engineering
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-02-23
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [non-engineer-builders, metrics-review-agents, pm-tool-connectivity, skills-marketplace, org-context-grounding, prototyping-agents-limits]
relevance: medium
---

## Relevance to the project
A hands-on tutorial for PMs using Cursor (and Claude Code in its terminal) as a daily driver. Its most useful part for the project is a worked "product analytics insight pipeline": three marketplace plugins (Amplitude, Linear, Notion), a context file stating what healthy metrics look like, a plain-English workflow prompt, and a saved slash command, which together check metrics, flag anomalies, open Linear tickets and update a Notion log. That is a concrete, small-scale picture of a PM metrics-review agent built from harness parts (plugins, context file, command) rather than a product, and a data point on what a PM must set up by hand. It is the author's own build; the company facts (Stripe's 3,000 engineers, an Amplitude PM's quote) are second-hand.

## Themes
- metrics-review-agents: the pipeline pulls seven days of activation and retention data, compares with healthy ranges in a context file, flags anomalies, creates investigation tickets and records findings; the author advises tuning the ranges after the first run ("Build a product analytics insight pipeline").
- org-context-grounding: the context file states the product's metrics and normal ranges; "the more specific you are here, the better the agent's judgement".
- skills-marketplace: Cursor's Plugin Marketplace (launched the week of the post) bundles MCP integrations, skills, agents and hooks into one-click installs, compared to Claude's equivalent.
- pm-tool-connectivity: plugins authenticate per tool; Figma's MCP became bidirectional with a `generate_figma_design` tool so Claude Code can push a running local UI into Figma as editable frames.
- non-engineer-builders: claims PMs and designers increasingly use Cursor daily; vibe coding and prototyping now part of interviews at many companies; an Amplitude PM calls Cursor his go-to for analysing dashboards (second-hand).
- prototyping-agents-limits: the @browser agent test only works reliably against hosted versions, not the local app; the author hit MCP configuration trouble until restarting.

## Key points
- **Two ways in:** build from scratch (prototypes) or work against an existing codebase (understanding it, generating PRDs or docs).
- **Working directory matters:** open too high and the agent sifts noise; too low and it loses project context.
- **Web vs desktop:** the web app is a "launch and monitor" surface for background agents; the desktop app is for real work; a task started on the web can be reviewed on desktop.
- **Use cases walked through:** Mermaid architecture diagrams of a codebase to learn a tech stack; Cursor's four modes (Agent for building, Ask/Plan for questions); built-in Browser the agent can drive, plus a Design sidebar for tweaking elements; the analytics pipeline; Claude Code in Cursor's terminal pushing a local UI to Figma.
- **Pipeline recipe (summarised):** install three plugins and authenticate; create a folder with context, findings and prompts subfolders; write a product-context file and a workflow prompt; set up a Notion log; save the prompt as a slash command; run, then tune.

## Notable quotes
- "Opening the right folder from the start is important" (section on the working directory)

## Could not verify
- Stripe rolling Cursor out to over 3,000 engineers and the Amplitude PM quote (an embedded image) are second-hand.
- The pipeline is described as a recipe; the post does not show it running on real data or report results.
- Paywalled text summarised, not reproduced.
