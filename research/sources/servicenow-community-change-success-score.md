---
title: "Change Success Score (Gamification)"
source_url: https://www.servicenow.com/community/itsm-blog/change-success-score-gamification/ba-p/2294799
author: gregmorriso (ServiceNow employee)
publisher: ServiceNow Community ITSM blog
published: 2021-04-18
retrieved: 2026-10-28
type: article
evidence: first-party
filed_by: research-dependency-agent
themes: [risk-sloped-review, risk-review-as-classification, decision-rights-for-agents]
relevance: medium
---
## Relevance to the project
Change Success Score is a team-level track record (start at 500, successful changes raise it, failed changes lower it; bands from Low under 500 to Excellent 700+) that change owners can use to auto-approve low-risk changes from teams with good history, or to add approvals for teams with poor history. It is a precedent for earned autonomy in a regulated process: approval rights sloped to a team's measured record, which a dependency agent's own asks or a platform's intake could borrow.

## Themes
- risk-sloped-review: change process owners "may allow for the auto approval of low risk changes" once a success criterion is met; CSS can also trigger additional approvals.
- risk-review-as-classification: "a numerical expression that represents a group's change success history"; "every failed change will decrement the score"; formula customisable.
- decision-rights-for-agents: implemented as a Flow Designer action ("Check Change Success Score") in approval flows, i.e. a policy hook, not a model decision.

## Key points
- ITSM Pro feature; requires the Change Success Score plugin; a decorator on the Assignment group field opens the team's scorecard and a leaderboard.
- 2021 post; current behaviour not re-verified against 2026 release notes.
