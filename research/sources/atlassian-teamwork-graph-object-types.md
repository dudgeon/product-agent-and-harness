---
title: "Teamwork Graph object types (Atlassian developer docs)"
source_url: https://developer.atlassian.com/platform/teamwork-graph/object-types/
author: Atlassian
publisher: developer.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [legible-org-for-agents, harness-portability]
relevance: high
---

## Relevance to the project

Lists the standard connector object types Atlassian maps external tools onto. It shows what a vendor considers the minimal common vocabulary of work artifacts: work item, project, document, space, design, deal and so on. Useful as a reference taxonomy for any meta-harness artifact primitives.

## Themes

- legible-org-for-agents: a fixed set of connector object types lets Rovo Search/Chat treat Asana tasks, Figma files and Google events uniformly.
- harness-portability: external tools are mapped into the vendor's types rather than exposed natively.

## Key points

- Queryable API object types named on the page: Jira work items and Users.
- Connector object types available in Rovo Search and Chat: Branch, Calendar event, Comment, Commit, Conversation, Customer organization, Deal, Design, Document, Message, Project, Pull request, Repository, Space, Video, Work item.
- Connector types not available in Rovo Search/Chat: Build, Deployment, Software service, Test, Test execution, Test plan, Test run.
- Examples: Asana tasks map to Work item, Google Calendar events to Calendar event, Figma files to Design.
- Not product-specific: there is no 'PRD', 'spec', 'insight' or 'idea' type in this list; those would be Document or Work item.

## Could not verify

Confluence and Home entities were not on this page. A web-search summary (not a fetched page, so unverified) said the early-access API also lists Atlassian Home entities (goal, goal update, project, project update, team, comment, tag). Access to the Teamwork Graph API was described in search results as Forge early-access with read:graph:jira / read:graph:confluence scopes; I could not confirm that on a fetched page. The relationship-types overview URL returned 404.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.

## Verification (user-story-mapping audit, 2026-10-24)

Re-read verbatim (curl, tags stripped). Page "Last updated Jul 16, 2025".
- Confirmed: the two examples of queryable types on this page are "Jira work items" and "Users"; the Rovo Search/Chat-indexed connector list (Branch, Calendar event, Comment, Commit, Conversation, Customer organization, Deal, Design, Document, Message, Project, Pull request, Repository, Space, Video, Work item) and the not-indexed list (Build, Deployment, Software service, Test, Test execution, Test plan, Test run) match the earlier note exactly.
- Correction to earlier "Could not verify": the full API object-type list is published on the Scopes page (atlassian-teamwork-graph-scopes.md), not only in search snippets. It includes Confluence types (Page, BlogPost, Comment, Database, Folder, Space, Whiteboard), Atlassian Home types (AtlassianGoal, AtlassianGoalUpdate, AtlassianProject, AtlassianProjectUpdate, AtlassianHomeTag, AtlassianHomeComment), AtlassianTeam/TeamType/User, AssetsObject, Loom, Compass, Focus, Talent, and 29 External* connector types (including ExternalFeatureFlag, ExternalVulnerability, ExternalDataTable, ExternalDashboard, ExternalDeal, ExternalCustomerOrg). Still no idea, PRD, spec, insight or decision type.
- Correction: access is Forge "Preview" (all users, GA-level support, 1-month breaking-change notice), not "early access"; EAP scopes `read:graph:jira`/`read:graph:confluence` are being retired for `read:graph:<object>:<product>`.
- Page also lists where connector data surfaces: Rovo Search, Rovo Chat, dashboards and analytics, Smart Links, personalized recommendations.
