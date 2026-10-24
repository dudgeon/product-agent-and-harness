---
title: "Limitations and considerations (Teamwork Graph, Atlassian developer docs)"
source_url: https://developer.atlassian.com/platform/teamwork-graph/limitations-and-considerations/
author: Atlassian
publisher: developer.atlassian.com
published: 2025-09-18
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [pm-tool-connectivity, harness-portability]
relevance: medium
---

## Relevance to the project

The constraints that decide whether an external product harness can use Atlassian's graph: Forge apps only, Jira/Confluence-installed apps only, org-admin install, and a stated intent to stop data leaving the Atlassian platform ("Runs on Atlassian"). This pushes any meta-harness toward the Rovo MCP server for read/write and away from the graph API as a data source.

## Themes

- pm-tool-connectivity: "Only Forge apps ... can add Teamwork Graph connectors to their app or call the Teamwork Graph API. These features are not supported for Connect apps." "Installing apps with the Teamwork Graph scopes requires organization administrator permissions".
- harness-portability: "For Preview and General Availability, we will implement policies and controls to ensure data accessed via the Teamwork Graph API is not egressed from the Atlassian platform."

## Key points

- API "only available for apps installed into Jira or Confluence"; connectors "only available for apps installed into Jira".
- An app can either call the API or provide a connector, not both (stated on the Teamwork Graph landing page, same retrieval).
- DevOps data sent via both Jira DevOps modules and the graph is scoped separately and duplicates.
- Page "Last updated Sep 18, 2025".
