---
title: "MCP Actions (Backstage AI docs)"
source_url: https://backstage.io/docs/ai/mcp-actions
author: Backstage project (CNCF)
publisher: backstage.io
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-legible-platform, onboarding-as-code, policy-enforcement-fail-open, identity-delegation]
relevance: high
---

## Relevance to the project
Backstage now exposes registered backend actions (catalog queries, Scaffolder templates) as MCP tools, so an agent can read the ownership graph and run a golden-path template directly. This is the most direct existing route from "platform publishes its intake" to "agent submits it". But authorization is left to each action: the Actions Registry does not enforce Backstage permissions automatically, so agent access can fail open unless each action checks.

## Themes
- agent-legible-platform: "The MCP Actions Backend exposes Actions registered with the Actions Registry as MCP tools"; actions from configured `pluginSources` (e.g. `catalog`, `scaffolder`) appear as tools, splittable into several MCP endpoints with include/exclude rules.
- onboarding-as-code: `scaffolder:*` actions let an agent create software from templates (multi-server example).
- policy-enforcement-fail-open: action attributes `destructive`/`readOnly` are hints clients may use to ask for confirmation; defaults are "conservative" and should be set explicitly (Action attributes). Per secondary docs, the registry does not enforce permissions; each action handler must (search summary, see Could not verify).
- identity-delegation: auth via OAuth Client ID Metadata Documents (recommended) after user approval in Backstage; static tokens described as "a temporary workaround until device authentication is completed"; DCR deprecated.

## Key points
- Default endpoint `/api/mcp-actions/v1` exposes every registered action; Streamable HTTP preferred, SSE deprecated.
- Tracing can record principal type and optionally `enduser.id` (off by default); warns that captured arguments may expose sensitive data.
- Red Hat Developer Hub ships this plugin from Backstage 1.40 onward (search result).

## Could not verify
- The "registry does not enforce permissions" statement came from search summaries of the docs, not from the text read on this page.
