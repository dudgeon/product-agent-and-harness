---
title: How to use Google's new Ideate Agent for Product Discovery and Ideation
source_url: https://departmentofproduct.substack.com/p/how-to-use-googles-new-ideate-agent
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-02-16
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [agent-led-intent-shaping, prototyping-agents-limits, spec-becomes-prototype-and-evals, prd-agents, opportunity-to-code-chain, pm-tool-connectivity, research-synthesis-agents]
relevance: medium
---

## Relevance to the project
Walks through Google Stitch's Ideate Agent, a discovery-stage agent that researches the web and named competitor products, proposes several design directions, drafts a PRD for the chosen one for the PM to edit, and then generates screens; and then chains Stitch into Claude Code over MCP. The Claude Code chain is the useful part for the project: from research transcripts in a folder to a three-item shortlist, a PRD for the chosen item, screens generated through Stitch's MCP, and a PowerPoint deck that combines the research and screens, all in one session. That is a compact example of a PM moving down the opportunity-to-prototype chain inside a general harness with one specialist tool attached. The author is clear the output is discussion material, not production design. Product facts are second-hand from Google's posts and docs; the examples are the author's own.

## Themes
- agent-led-intent-shaping: Ideate is given a problem statement and where to look (named postpartum, meditation and time-poor-user apps); it returns three named directions, asks which to pursue, then drafts a PRD for approval before designing ("Get design inspiration..." section).
- prototyping-agents-limits: "by no means production-ready pixel perfect designs"; useful as talking points; beta Google Labs product, free with monthly limits (HMW section; final thoughts).
- spec-becomes-prototype-and-evals: the PRD is an intermediate step the agent writes and the PM edits, then the screens become the artifact taken to stakeholders.
- prd-agents: Claude Code turns a chosen research finding into a "simple PRD", which becomes the prompt for screen generation ("Turn research discovery insights into prototypes").
- opportunity-to-code-chain: research → shortlist → PRD → screens → stakeholder deck in one Claude Code session with the Stitch MCP; the deck reused the Stitch colour scheme ("Generate a discussion deck").
- pm-tool-connectivity: Stitch MCP added to Claude Code with an API key; tools listed include list/get projects and screens and generate a screen from text.
- research-synthesis-agents: Claude Code reads two research transcripts and proposes three changes; the transcripts were mock ones the author wrote.

## Key points
- Framing: a Google PM calls this "Deep Design", design tools that also do the research needed in discovery.
- Use cases shown: onboarding inspiration for a new-parent fitness app; one Ideate session per "how might we" question for a design sprint (kept separate for distinct explorations); three SaaS pricing-page directions built side by side for comparison.
- Suggests organising sprint output by HMW question: question, two or three directions, reference patterns, screens.
- Export paths: paste to Figma with auto layout, or HTML/CSS for further work in Claude Code.

## Could not verify
- The post says the MCP exposes six tools but lists five; tool names were not checked against Google's docs.
- The research inputs were mock transcripts, so how well the shortlist reflects real research is not shown.
- Paywalled; summarised, not reproduced.
