---
title: Glean: Agents as tools (exposing Glean agents through the Glean MCP server)
source_url: https://docs.glean.com/administration/platform/mcp/agents-as-tools
author: Glean
publisher: docs.glean.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, one-job-per-agent]
relevance: high
---

## Relevance to the project
The clearest concrete example found of a deployed, admin-curated task agent exposed to general harnesses (Claude Desktop, Cursor, VS Code) over MCP. Its own restrictions are the evidence: read-only, no human-in-the-loop, no write tools, finish in about 30 seconds, because hosts time out. This is the realistic shape of 'a PRD-review agent behind MCP' today without the Tasks extension.

## Themes
- `remote-agent-invocation`: Agents added by admins under Platform > Glean MCP server > Available tools; agents with write tools or 'wait for user input' steps are rejected, including via sub-agents.
- `one-job-per-agent`: Guidance to keep a small set of high-quality, non-overlapping agents; build separate agents for interactive and MCP use.

## Key points
- Approximate host timeouts: Claude Desktop ~60s, Cursor 30-60s, VS Code ~30s, others 30-120s; recommended agent runtime under ~30s. On timeout Glean may keep running but the result is not returned.
- Descriptions must start with an action verb, name connectors and output, 2-3 sentences, because the host LLM routes on them.
- Large tool lists degrade host tool selection; group by use case and use dynamic toolsets.
- Authentication is not covered on this page.

## Could not verify
- Page date unknown; timeout figures are vendor-reported and may be out of date.
