---
title: "Build on Dovetail (docs)"
source_url: https://docs.dovetail.com/help/build-on-dovetail
author: Dovetail
publisher: docs.dovetail.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [research-synthesis-agents, harness-portability]
relevance: medium
---

## Relevance to the project

Dovetail's programmatic surface (MCP, REST, CLI) and the objects it exposes: projects, docs, data, highlights, contacts, channels, transcripts. Shows the research-repository side of PM artifacts and its MCP access; also the HIPAA gotcha that disabling API keys disables MCP.

## Themes

- research-synthesis-agents: MCP can read workspace content and create projects, docs, data, highlights and channel data.

## Key points

- Three options: MCP server, REST API (default 200 requests/min per workspace), CLI 'dt' for bulk import from Notion, Confluence, Google Drive and files (no sync after import).
- All act with the user's own permissions.
- On HIPAA workspaces API key generation is off by default, which also disables MCP connectors.

## Could not verify

Page did not define a full object model (notes, insights as separate objects are not confirmed). Companion MCP page (docs.dovetail.com/integrations/mcp-server) lists search/read of transcripts, projects, docs, highlights, contacts, folders, comments, channel themes, project tags, and creation of projects, docs, data, highlights and channel data; auth by personal API key or first-party sign-in (Claude, ChatGPT, Figma Make, etc.); search summaries conflicted on OAuth vs API key for the hosted endpoint.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.
