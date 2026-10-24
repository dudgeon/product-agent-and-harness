---
title: How to use Claude Cowork as a Competitive Intelligence System
source_url: https://departmentofproduct.substack.com/p/how-to-use-claude-cowork-as-a-competitive
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-02-11
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [single-agent-many-skills, status-update-agents, org-context-grounding, pm-tool-connectivity, human-review-gates, work-structure-spectrum]
relevance: medium
---

## Relevance to the project
A hands-on walkthrough of a PM chaining several jobs in one general agent (Claude Cowork): browser research of competitor pricing into an Excel matrix and a deck, a structured UI critique into a Word doc, then the official product-management plugin's /stakeholder-update command turning the deck into a Slack-ready message, and finally a trigger phrase that reruns the whole chain. It is a concrete independent picture of the "general harness plus a role plugin" option for PM work, and of how thin the "workflow" layer can be (a named phrase, a working folder). It is one author's trial, early in Cowork's beta, with no measurement; Anthropic product facts are second-hand. Rated medium rather than high because it shows the shape of the work, not evidence that it holds up.

## Themes
- single-agent-many-skills: one Cowork session uses built-in document skills (xlsx, pptx, docx, pdf), the Chrome extension, connectors and the PM plugin's slash commands in sequence (hands-on sections).
- status-update-agents: /stakeholder-update asks the update type (ad hoc, research completion) and audience (executives), then reformats for Slack; the author notes connectors could send it too. See [Anthropic's plugin announcement](anthropic-cowork-plugins-product-management.md) and the [plugin repo check](infoq-claude-cowork-plugins.md).
- org-context-grounding: recommends a "my-company" folder of strategy decks and OKRs, and a competitor list kept as a file, so the agent can judge strategic gaps; the author admits he gave it little context.
- pm-tool-connectivity: connectors for Gmail, Calendar, Notion, Asana, Slack; Google Drive limited at the time to Google Docs up to 10MB, main text only (no images, comments, suggestions).
- human-review-gates: closes with "worth double checking its output before sharing anything"; browser automation results "a bit hit and miss".
- work-structure-spectrum: "Run the intel workflow" is a user-defined key phrase that tells Cowork to rerun the chain, structure added on demand inside a general agent.

## Key points
- Mental model offered: Chat is standard Claude, Cowork is a co-worker you delegate to, Code is "a CTO who writes code"; Claude Code can do all three but the terminal puts people off.
- Cowork needs its own working directory; files it creates land there, and saved screenshots give later tasks more context.
- Advice to give Cowork specific, outcome-described tasks (an example prompt specifies slides, data file and length).
- File organisation: reads contents rather than names, renames and categorises, and documents each decision for review.
- PM plugin commands listed: write-spec, roadmap-update, stakeholder-update, synthesize-research, competitive-brief, metrics-review.

## Could not verify
- The "SaaSpocalypse" market framing and the quoted CEO remarks (press, not linked).
- Screenshots and the shared output files were not inspected.
