---
title: "Teamwork Graph glossary (Atlassian developer docs)"
source_url: https://developer.atlassian.com/platform/teamwork-graph/glossary/
author: Atlassian
publisher: developer.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [legible-org-for-agents, org-context-grounding]
relevance: medium
---

## Relevance to the project

Atlassian's own vocabulary for its 'graph of work': objects, object types, directional typed relationships, ARIs, connectors and ACLs. It is the closest first-party example of a platform defining generic artifact primitives (object, relationship, permission) that sit under product-specific objects. Directly relevant to whether a product meta-harness should define primitives or just map onto existing platform graphs.

## Themes

- legible-org-for-agents: the graph is explicitly the layer that links work data across Atlassian apps and connected external tools (Core concepts, 'Teamwork Graph').
- org-context-grounding: ACLs are specified per object that a connector adds, so permissions travel with the object.

## Key points

- Object = single item of data (Jira work item, Confluence page, Google Drive file); each belongs to an object type that defines structure, properties and possible relationships.
- Two kinds of object type: API object types (queryable) and connector object types (for adding external data).
- Relationship = directional (from, to) with a type. Categories: canonical (structural: ownership, containment, parent-child; set by connectors via parentKey, containerKey, associations), activity (user actions, generated automatically, shorter TTL), inferred (derived from patterns/ML, e.g. suggested collaborators).
- ARI (Atlassian Resource Identifier): globally unique ID, pattern ari:cloud:{app}:{siteId}:{objectType}/{objectId}.
- Query: curated GraphQL API; Cypher for traversal. Connector SDK covers object, user and group operations; ACLs per object.

## Could not verify

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.

## Verification (user-story-mapping audit, 2026-10-24)

Re-read verbatim (curl, tags stripped). Page "Last updated Jan 27, 2025".
- Confirmed: object/object type, API vs connector object types, ARI pattern `ari:cloud:{app}:{siteId}:{objectType}/{objectId}`, directional typed relationships, ACL per connector object, "curated GraphQL API", Cypher "originally developed by Neo4j".
- Correction: the glossary defines canonical, activity and inferred relationships, but the Relationships page (atlassian-teamwork-graph-relationships.md) lists four kinds, adding "logical" (union views such as AtlassianUserCreatedDocuments).
- Added detail: "Atlassian provides 100 out-of-the-box connectors"; TTL: "activity relationships typically have shorter TTLs (30 days) while canonical relationships may have longer TTLs (365-730 days)"; Teamwork Graph is "a common data model for work items, documents, messages, users, groups, projects, and more"; API object type examples "Jira work item, User, and Atlassian project".
- Access status (from Scopes and Call-the-API pages, same date): Forge Preview, read-only, per-object-type scopes, Forge apps installed in Jira/Confluence only, org-admin install. See atlassian-teamwork-graph-scopes.md, atlassian-teamwork-graph-call-the-api.md, atlassian-teamwork-graph-limitations.md.
