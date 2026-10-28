---
title: "Track dependencies in Delivery Plans - Azure Boards"
source_url: https://learn.microsoft.com/en-us/azure/devops/boards/plans/track-dependencies?view=azure-devops
author: Microsoft
publisher: Microsoft Learn
published: 2026-02-28
retrieved: 2026-10-28
type: docs
evidence: vendor-claim
filed_by: research-dependency-agent
themes: [dependency-types-and-practices, process-artifacts-as-coordination, pm-tool-connectivity]
relevance: medium
---

## Relevance to the project
Microsoft's documentation for dependency tracking in Azure Boards Delivery Plans shows the standard tool model: dependencies are predecessor/successor links between work items, conflicts are detected only as date inversions, and nothing crosses an organisation boundary. Large regulated enterprises often run several Azure DevOps organisations (or Azure DevOps beside Jira), so the "same organisation only" limit is exactly where cross-platform dependencies fall out of view. The page now also shows the same queries run through an Azure Boards MCP server, the first step toward agent access.

## Themes
- dependency-types-and-practices: tracking supports only the Predecessor/Successor link type; "Dependency conflicts occur when a successor work item is scheduled to complete before its predecessor" (§Resolve dependency conflicts).
- process-artifacts-as-coordination: green/red icons on cards and black/red lines on the plan; best practice is to check dependency status in sprint planning and reviews (§Best practices).
- pm-tool-connectivity: "You can create dependencies between work items across different projects and teams within the same organization. Dependencies across organizations aren't supported." (§Prerequisites tip); §Use AI lists example MCP prompts such as "Find work items with predecessor links where the predecessor is scheduled after the successor".

## Key points
- Prerequisites: a configured Delivery Plan, edit permissions on the relevant Area Paths, and work items already linked.
- A dependency's end date comes from the item's Target Date or its Iteration Path end date, so the check is only as good as those fields.
- Resolution advice includes "Re-evaluate dependencies: Consider if dependency relationships are still accurate" (staleness is left to humans).
- Microsoft's older Dependency Tracker extension is superseded by Delivery Plans (per Learn's previous-versions page; not read in full).
