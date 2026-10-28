---
title: "Define dependencies between work with plans in Jira"
source_url: https://learning.atlassian.com/learning/course/jira-plans-tutorial/lesson/jira-plans-dependencies
author: Atlassian
publisher: Atlassian Learning (Jira Plans tutorial)
published: unknown
retrieved: 2026-10-28
type: docs
evidence: vendor-claim
filed_by: research-dependency-agent
themes: [dependency-types-and-practices, process-artifacts-as-coordination]
relevance: medium
---

## Relevance to the project
Atlassian's own tutorial shows what dependency management looks like inside Jira Plans (formerly Advanced Roadmaps): directional links between work items, date-conflict warnings, and a matrix report, all of which depend on people creating and maintaining the links by hand. It is the baseline any dependency agent inherits in Jira-heavy enterprises: the tool can show a dependency only if someone recorded it, and can check dates but not whether the dependency is real or still current.

## Themes
- dependency-types-and-practices: dependencies are directional ("The dependent work item must be scheduled later than the required work item"); link types depend on site configuration (blocks / is blocked by; causes / is caused by; depends on / is depended on by) (lesson body).
- process-artifacts-as-coordination: the Dependencies report shows all dependencies in a plan as a visual matrix to spot bottlenecks, filterable by parent, epic, space, team, sprint or dependency type; lines "will turn red if there are conflicting dates" (lesson body).

## Key points
- Dependencies appear as badges or connecting lines on the timeline; created by hovering and dragging, or via "Linked work items" on the Jira issue (saved both ways).
- Dragging between bars makes it hard to set the dependency type, so type data is often inconsistent.
- The lesson says nothing about work outside the plan; community threads (not read in full here) report that out-of-plan dependencies do not show in the report unless the plan filter includes the other project.
- Atlassian's 2017 blog on Portfolio for Jira described the prior state as "shoulder tapping" and issue links, a "time-consuming and manual process" (https://www.atlassian.com/blog/jira/portfolio-for-jira-dependency-management, Laura Daly, 2017-09-06; read for this note).

## Could not verify
- Current behaviour for cross-plan and cross-instance dependencies.
