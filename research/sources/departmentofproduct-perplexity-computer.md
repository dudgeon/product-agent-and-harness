---
title: How to use Perplexity's new Computer to build a Pricing Intelligence Engine, OKR review system, API cost simulator and more
source_url: https://departmentofproduct.substack.com/p/how-to-use-perplexitys-new-computer
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-03-17
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [cost-control-routing, pm-tool-connectivity, status-update-agents, work-structure-spectrum, ai-synthesis-hallucination-risk, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A hands-on guide to Perplexity Computer, a hosted general-purpose agent that plans a goal into subtasks, runs sub-agents in a cloud sandbox, routes each subtask to a different vendor's model and acts through connectors, including as an always-on background worker. For the project it is a data point for a hosted, model-agnostic loop aimed at knowledge workers rather than developers, and its four PM recipes (competitor monitoring, meeting-to-ticket with chasing, quarterly OKR deck, API cost simulator) are concrete candidate PM jobs. The description of how Computer works is the author's summary of Perplexity's own material; the recipes are the author's own builds. Bears on loop-source and model-provider-coupling.

## Themes
- cost-control-routing: per-subtask routing across vendors' models (examples given: Opus 4.6 for reasoning, Grok for fast tasks, GPT 5.2 for long-context recall) is presented as Perplexity's main differentiator; usage runs on credits that can run out, so always-on workflows need watching ("What exactly is Perplexity Computer?", "Getting set up").
- pm-tool-connectivity: connectors for Gmail, Outlook, GitHub, Linear, Slack, Notion, Salesforce and Snowflake read and write; connectors can also be embedded in apps Computer builds as two-way data sources (for example one editor saving to Notion and Google Docs at once).
- status-update-agents: the meeting-to-ticket worker watches the calendar, reads transcripts and pre-read emails, extracts each person's commitments, creates assigned Linear tickets with due dates, emails a summary, then nudges owners of tickets idle for three days.
- work-structure-spectrum: describes the outcome-first mode (describe the result, the agent plans and spawns sub-agents) alongside persistent background workers that run "indefinitely" on triggers and schedules.
- ai-synthesis-hallucination-risk: the competitor-dashboard recipe has to tell the agent to cite a URL for every data point and to flag pricing it cannot see rather than invent it.

## Key points
- **What it is:** a "digital worker" that runs workflows for hours or longer; cloud sandbox first, with a local version announced. Available on Pro and Max plans. The post says Perplexity re-entered Ramp's top-10 fastest-growing SaaS list after launch (relayed).
- **How it works (four steps):** plan into tasks; route each to a model; pull live data and take actions through connectors in parallel; deliver an artifact (deck, report, mini-app).
- **Recipes:** (1) competitor intelligence dashboard: finds 8-12 competitors, baselines pricing, app-store tiers, launches, changelogs and earnings calls, re-checks daily, grades changes by severity and emails major ones; (2) meeting-to-ticket converter with chasing; (3) quarterly OKR kickoff deck from last quarter's results, strategy doc and backlog; (4) API cost simulator that projects vendor spend at several growth rates and finds pricing-tier cliffs.
- **Community examples:** ad campaign monitor, GitHub repo visualiser, plus a shared spreadsheet of builds.
- The author doubts the moat lasts as Google builds multi-model features.

## Notable quotes
- "Run indefinitely in the background. Do not stop after one meeting." (the author's meeting-to-ticket prompt)

## Could not verify
- Perplexity's own announcements, the model-routing examples and the Ramp ranking claim were not read or checked.
- No outcome data for any recipe; demos only.
- Retrieved through a paid subscription; prompts are described, not reproduced.
