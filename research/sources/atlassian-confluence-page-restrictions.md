---
title: "Add or remove page restrictions (Confluence Cloud support)"
source_url: https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [identity-delegation, human-review-gates]
relevance: medium
---

## Relevance to the project

The per-item layer of Confluence sharing: "General access" (open-by-default within the space), then Open: anyone can view / specific people edit, Restricted, or Restricted by a parent. View restrictions inherit down the tree, edit restrictions do not. The Rovo MCP server exposes exactly these states (`getConfluenceContentRestrictionState`: OPEN, EDIT_RESTRICTED, fully restricted) so an agent can read and set them. Relevant to how a harness shares a PRD with a sub-team or an external party.

## Themes

- identity-delegation: "General access ... refers to the general audience for the content item — everyone who has at least view access to the space a content item lives in, or, if a parent item is restricted, everyone who has at least view access to the parent item."
- human-review-gates: "All editing is restricted to specific people. Even if people have permission at the space level to edit content, they can't edit this content unless they're explicitly listed with Can edit in Specific access"; "You can't restrict access to content on the free plan."

## Key points

- States: "No restrictions. Consume whatever the space's access settings are."; edit-restricted; "Restricted: Only specific people can view or edit"; "Restricted by a parent: Anyone on the parent can edit" / inherited view.
- "View restrictions added to the parent item or folder are inherited down to all content items nested under it." Edit restrictions do not inherit (WebFetch summary).
- Org admins on Premium/Enterprise can bypass with an admin key (section "Bypass page restrictions with admin key").
- Public links are a separate feature (related article, not covered here).

## Could not verify

Who exactly may add or remove restrictions is not given as a matrix on the page; the WebFetch summary says space admins and anyone with edit plus restriction-management permission.
