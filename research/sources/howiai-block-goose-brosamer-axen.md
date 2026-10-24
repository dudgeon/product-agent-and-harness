---
title: "How Block's custom AI agent supercharges every team, from sales to data to engineering | Jackie Brosamer & Brad Axen"
source_url: https://www.lennysnewsletter.com/p/blocks-custom-ai-agent-goose
author: Claire Vo (host), Jackie Brosamer (VP Engineering, data, Block), Brad Axen (principal engineer, Block)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-07-28
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [build-vs-buy, harness-portability, pm-tool-connectivity, non-engineer-builders, metrics-review-agents, enablement-by-product, cost-control-routing, agent-failure-modes]
relevance: medium
---

## Relevance to the project
A first-party look at Block's own agent harness, Goose: an open-source, local, model-agnostic agent whose capabilities come entirely from MCP servers ("extensions"), with five bundled and "40 or 50" internal ones, including a data MCP that "knows all that context" about revenue and an internal publishing MCP (BlockCell) that turns any HTML output into an internal URL. It is evidence for the "own the harness, plug in any model" pole of loop-source and model-provider-coupling, and for publish-to-share as the artifact pattern for non-technical users. Most of the episode is a demo (CSV analysis, Square catalog, vibe-coding an email MCP), not PM work; PM-relevant content is thin, hence medium rather than the triage's high. The companion Lenny's Podcast episode with Block's CTO is [lenny-podcast-block-dhanji-goose](lenny-podcast-block-dhanji-goose.md).

## Themes
- build-vs-buy / harness-portability: Goose was open-sourced partly so Block isn't tied to one provider: bundled vendor tools "can only use like that kind of models", while "every month a new model is coming out" (6:40). No auto model selection; users switch per context, e.g. Claude Sonnet for code and tool use, an OpenAI reasoning model for a design doc, or a local Qwen model (32:49).
- pm-tool-connectivity: everything is MCP; internally Google Drive (the VP's most-used), a data MCP, BlockCell publishing, a developer extension and a computer controller (14:41); "when we use it internally, we have like 40 or 50" (15:44). The show notes cite "How to scale an internal MCP catalog" but the transcript does not cover it.
- non-engineer-builders: adoption was "both bottoms up and tops down"; salespeople were early demanders (3:04); non-developers are "so creative and so tolerant of like stringing together a bunch of different tools" (4:17). Business users publish their own dashboards as internal static sites (12:21).
- metrics-review-agents: the data team's goal is for "our finance team, our sales team, anyone in the company" to self-serve analysis instead of waiting for a data scientist (15:57); demo: messy CSV to pandas analysis, recommendations and a Plotly HTML report (7:46-14:08). "LLMs ... function as like data duct tape" (22:19).
- enablement-by-product: organisational transformation, not the model, decides the winners: "It's like really easy to get technology to go exponentially and humans don't go exponentially so well" (3:04).
- agent-failure-modes / guardrails: Goose tried to read a `.env` file holding an API key and the read was denied by a built-in check (28:50); the agent over-works simple tasks (21:00) and needed interruption when heading down "a slightly wrong path" (33:47).
- cost-control-routing: no automatic routing; model choice is manual per task (32:49), relevant as a counterpoint to harnesses that route centrally.

## Key points
- Goose runs locally, which suits Block's local developer environments and open-source users who want "end-to-end control"; best mode is a background task: hand it the job, walk away, come back (13:10, 23:59).
- Square's MCP uses progressive disclosure: rather than exposing every operation, it offers a lookup method per area (e.g. catalog) so the model isn't overwhelmed (20:27).
- Workflow for building an MCP: first make a plain script that does the thing (the hard part), then paste an SDK example and ask the agent to wrap it as an MCP tool, then register it as a stdio extension; a new tool can be enabled mid-conversation and used by a session that never saw it built (27:47-40:35).
- Debugging: "I almost always let the LLM try once"; the human's edge is tenacity (38:10). When a session goes wrong, both guests start over, one carrying forward an agent-written summary of the good parts (44:23, 44:58).
- Search: ripgrep found to be "really effective" versus fancier semantic search (8:13).

## Notable quotes
- "humans don't go exponentially so well." (3:04)
- "when we use it internally, we have like 40 or 50." (15:44, on MCP extensions)

## Could not verify
- Full transcript read (Substack auto-transcription; "MZP/NCP/MTP" = MCP, "Cloud Sonnet" = Claude Sonnet, "BlockCell" spelling uncertain).
- The show notes promise "how to scale an internal MCP catalog" and "the organizational transformation required"; the episode only touches these in two sentences. No usage numbers were given in this episode.
- Demos used fake farm-stand data and a demo Square account; internal usage was asserted, not shown.

## Follow-up (2026-10-24, research-block-product-practices)
- The internal publishing capability described here (BlockCell MCP) appears to have been succeeded by Block App Kit (launched mid-March 2026), first an MCP server and then a skill, with ~80% of users outside engineering and 1,000+ apps ([block-eng-app-kit-localhost-to-launched](block-eng-app-kit-localhost-to-launched.md)); the post does not name BlockCell, so the succession is my inference.
- The "data MCP that knows all that context" is detailed as Block Data MCP plus Query Expert MCP ([block-eng-data-foundation-automated-analytics](block-eng-data-foundation-automated-analytics.md)).
- "40 or 50" internal extensions (July 2025) compares with "over 60" (June 2025 playbook), "over 100" (Oct 2025 talk) and "about 150 services" (Nov 2025 investor day): counts depend on who is counting what.
