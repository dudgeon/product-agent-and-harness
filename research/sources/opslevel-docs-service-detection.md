---
title: "Service Detection"
source_url: https://docs.opslevel.com/docs/service-detection
author: OpsLevel
publisher: docs.opslevel.com
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [ownership-inference, stale-records-mislead-agents, human-review-gates, legible-org-for-agents]
relevance: high
---
## Relevance to the project
A concrete, documented pattern for keeping a catalog's ownership records current with a human in the loop: OpsLevel detects components from git, monitoring and alerting tools, suggests owners from recent commit history rolled up to teams, and asks a person to accept, rename, merge, reassign ("This is not my component") or ignore each suggestion, logging every action. This is the "improve the records as you go" loop a dependency agent needs, already shipping for services, with at most one reminder email a day.

## Themes
- ownership-inference: for repository-based detections, OpsLevel reads recent commit history, matches contributors to known users, and suggests their teams, aggregating contributions per team (hover shows the breakdown).
- human-review-gates: reviewers can change the action or name before accepting, ignore and later unignore, or say "This is not my component"; each action is recorded in Recent Activities.
- stale-records-mislead-agents: detection runs continuously from Git, Datadog, PagerDuty, New Relic, OpsGenie, deploy and custom events; close alias matches are proposed as Merge rather than duplicate Register.
- legible-org-for-agents: each user sees a personalised suggestion list by team membership; optional pending-suggestion emails go to the team's default contact, manager or members, "at most once a day".

## Key points
- Owner suggestions come only from repository detections, not from alert-based ones.
- The docs do not say how many commits are read or how aggregation is weighted.
