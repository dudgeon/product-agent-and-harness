---
title: "Call the Teamwork Graph API (Atlassian developer docs)"
source_url: https://developer.atlassian.com/platform/teamwork-graph/call-the-teamwork-graph-api/
author: Atlassian
publisher: developer.atlassian.com
published: 2026-02-11
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [pm-tool-connectivity, legible-org-for-agents]
relevance: medium
---

## Relevance to the project

States the access status and mechanics of the Teamwork Graph API: Forge Preview, GraphQL wrapper around Cypher, callable only from Forge apps (`api.asUser().requestTeamworkGraph` or `@forge/bridge`), with a hosted Query Builder. Confirms that a harness cannot call the graph directly with a user OAuth token; it needs a Forge app installed by an org admin.

## Themes

- pm-tool-connectivity: "The Teamwork Graph API is available through Forge's Preview release phase" with "a minimum 1-month deprecation notice" for breaking changes; calls go through `@forge/api` (`api.asUser().requestTeamworkGraph(...)`) or `@forge/bridge` (`requestTeamworkGraph`), and "Frontend API calls will always run as the current user".
- legible-org-for-agents: "two-layer query approach: Cypher queries ... GraphQL wrapper - Wraps Cypher queries and returns full object details."

## Key points

- Manifest needs a per-object scope, e.g. `read:graph:issue:jira`; `forge deploy` fails without it.
- Echo query for connectivity test; Query Builder at `https://teamwork-graph.atlassian.com/query-builder`; site endpoint `https://<site>.atlassian.net/gateway/api/graphql/twg`.
- Page "Last updated Feb 11, 2026".

## Could not verify

Only the first ~115 lines of the stripped page were read (setup and connectivity); later sections on query patterns and errors were not read.
