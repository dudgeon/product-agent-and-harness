---
title: "Scopes (Teamwork Graph API, Atlassian developer docs)"
source_url: https://developer.atlassian.com/platform/teamwork-graph/scopes/
author: Atlassian
publisher: developer.atlassian.com
published: 2026-09-15
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [product-artifact-primitives, legible-org-for-agents, pm-tool-connectivity]
relevance: high
---

## Relevance to the project

The definitive, verbatim list of every object type the Teamwork Graph API exposes (one read scope per type), the API's release status, and how admins gate graph access per object type. It settles two gaps from the earlier pass: the API is in Forge "Preview" (not EAP, not GA) and is read-only; and the full API object-type list includes Confluence, Atlassian Home (goal, project, tag, comment), Loom, Compass, Focus and Talent types plus "External*" connector types. Shows what a vendor considers the atomic vocabulary of work, and the fail-closed permission pattern a meta-harness could copy.

## Themes

- product-artifact-primitives: full API object-type list (Scope reference): Jira (JiraWorkItem, JiraWorkItemComment, JiraWorkItemStatus, JiraWorkItemPriority, JiraWorkItemRemoteLink, JiraWorklog, JiraSpace, JiraBoard, JiraSprint, JiraVersion); Confluence (ConfluencePage, ConfluenceBlogPost, ConfluenceComment, ConfluenceDatabase, ConfluenceFolder, ConfluenceSpace, ConfluenceWhiteboard); Atlassian (AtlassianUser, AtlassianTeam, AtlassianTeamType, AtlassianGoal, AtlassianGoalUpdate, AtlassianProject, AtlassianProjectUpdate, AtlassianHomeTag, AtlassianHomeComment, AssetsObject); Loom; Compass; Focus (FocusFocusArea, FocusFocusAreaStatusUpdate, FocusChangeProposal); Talent; External* (WorkItem, Document, Space, Project, Comment, Message, Conversation, Repository, Branch, Commit, PullRequest, Build, Deployment, FeatureFlag, Service, Vulnerability, Design, Video, CalendarEvent, Dashboard, DataTable, RemoteLink, Deal, CustomerOrg, CustomerOrgCategory, CustomerContact, Organisation, Position, Worker). No idea/PRD/spec/insight/decision type.
- legible-org-for-agents: "All Teamwork Graph API scopes are read-only — there is no write access to the graph through this API."
- pm-tool-connectivity: status banner: "The Teamwork Graph API is available through Forge's Preview release phase. Preview features are available to all users ... Schemas, fields, and behavior may still change before general availability (GA)". Admins can toggle individual scopes in Atlassian Administration; "A missing scope doesn't produce an error ... A query that reads an object type you weren't granted comes back successful and empty."

## Key points

- Scope pattern `read:graph:<object>:<product>`, e.g. `read:graph:page:confluence`, `read:graph:issue:jira` (JiraSpace is still `read:graph:project:jira`).
- EAP scopes `read:graph:jira` / `read:graph:confluence` are being retired for per-object scopes; Forge has a cap of 50 scopes.
- Every object type traversed in a Cypher query needs its scope, including intermediate hops; mixed traversals return partial results silently; scope changes take about a minute.
- Scopes apply on top of the end user's normal product permissions.
- Page "Last updated Sep 15, 2026".

## Could not verify

Read from a curl download of the page with tags stripped (verbatim text). The per-type API reference index (`/api-reference/object-types/` and `/relationship-types/`) returned 404 at retrieval; individual type pages exist (e.g. `.../api-reference/object-types/AtlassianGoal/`) per search results but were not fetched.
