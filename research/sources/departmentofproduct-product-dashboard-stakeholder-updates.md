---
title: How to build the ultimate Product Dashboard that generates stakeholder updates on demand
source_url: https://departmentofproduct.substack.com/p/how-to-build-the-ultimate-product
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-06-29
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [status-update-agents, metrics-review-agents, non-engineer-builders, pm-tool-connectivity, artifact-standardization]
relevance: medium
---

## Relevance to the project
A build tutorial in which a PM vibe-codes, with Claude Code or Codex, a local dashboard that shows product health, work in progress, competitor releases and a "decision queue", then turns any selected data points into a Slack message, email or cloned-voice audio update for a chosen audience. It is a concrete picture of the status-update and metrics-review jobs done as a personal tool rather than through a shared agent, and of the "decision queue" as a PM artifact distinct from a task list. Most data is dummy; only Google Analytics and Linear have live hooks, and Slack/Gmail wiring is left as a prompt. It is evidence of what PMs are being taught to build, not of outcomes.

## Themes
- status-update-agents: "Stakeholder update generator": select data points, pick format (Slack, email, audio) and audience (C-suite, product users, teammates), get a draft; audio goes script first, then ElevenLabs with the PM's voice clone.
- metrics-review-agents: product-health panel across users, UX, commercial and DORA engineering metrics (plus AI-coding adoption), reusing the five-dimension health model from the earlier Projects post ([note](departmentofproduct-claude-projects-product-health.md)).
- non-engineer-builders: opening claims that non-engineers' AI-written commits are up sharply and that dashboards are now "akin to building spreadsheets"; cites Rippling's CEO building a dashboard to monitor inefficient Claude spend (second-hand).
- pm-tool-connectivity: live connectors are thin (GA4 property ID, Linear API key); the inbox and decision queue run on dummy data unless the PM asks the agent to wire Slack and Gmail credentials.
- artifact-standardization: the decision queue has a fixed record shape (the call to be made, kind, who it waits on, age, short context), and a prompt makes Claude extract those records from inbox highlights at load time.

## Key points
- **What gets built:** an added feature in the app from two earlier DoP tutorials (persona feature tester, strategy thought partner); four sections: day-to-day (backlog/WIP, decision queue, inbox and Slack summary, recent releases), competitors (changelog RSS and news, plus a "principle of the day" from product books), product health, and the update generator.
- **Method:** first prompt asks the coding agent to restate the requirements and ask clarifying questions before writing code; then iterate per component with targeted prompts.
- **Decision queue:** framed as "a forcing function" rather than a to-do list; made dynamic by having Claude extract open decisions from inbox data on load, with a refresh button.
- **Competitor monitoring:** RSS changelogs plus news search terms per competitor, split into "press" and "shipped".
- **Personas link:** updates can be targeted at the user personas built in an earlier tutorial.
- **Caveats:** runs locally; "involve your DevOps teams" before publishing it anywhere. A downloadable template is offered to paid subscribers.

## Notable quotes
- "Not a task manager - a forcing function." (on the decision queue)

## Could not verify
- The Rippling CEO dashboard, the commit-growth figure and the Gokul Rajaram "Build Ceiling" quote are cited without links in the retrieved text.
