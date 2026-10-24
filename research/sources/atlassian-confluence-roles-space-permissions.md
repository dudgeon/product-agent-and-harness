---
title: "What are Confluence's roles? (space permissions, Confluence Cloud support)"
source_url: https://support.atlassian.com/confluence-cloud/docs/what-are-space-permissions/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [identity-delegation, human-review-gates, work-structure-spectrum]
relevance: medium
---

## Relevance to the project

Defines who can see and change a document in Confluence: role-based space access (Admin, Manager, Collaborator, Viewer, custom), the individual permissions behind each role, and the split-out admin powers for public links, guest access and anonymous access. For a multi-party PRD/spec this is the model a harness has to respect or reproduce: visibility is set at space level by role, then narrowed per item by restrictions.

## Themes

- identity-delegation: "Each role has a different set of individual permissions associated with it"; roles can be assigned to classes such as "All Confluence users"; "you can't assign or remove roles that include permissions you don't have."
- human-review-gates: Admin-split permissions "Allow and manage public links", "Manage guest access to space", "Allow and manage anonymous access", "Delete space", "Archive space" are separate grants, not bundled with editing.
- work-structure-spectrum: default roles: Admin "Manages everything in the space" (IT teams, space owners); Manager "Manages people and content but not settings" (project leads); Collaborator "Adds and edits content in the space"; Viewer "Views and comments on content in the space."

## Key points

- The URL `what-are-space-permissions` now serves the article "What are Confluence's roles?"; "Role-based access is now generally available (GA)."
- Content permissions: View content ("No one can view content they're restricted from viewing"), Create content, Edit content, Delete own content, Archive any content, Delete anyone's content; blogs, comments, attachments, export have their own grants.
- Restriction management: "Manage access to individual content" and "Manage all content in space" (can change content ownership; unlocks bulk actions).
- Deleted spaces stay in trash 60 days.

## Could not verify

Read via curl with tags stripped (verbatim) plus one WebFetch summary. The exact permission set inside each default role is behind expandable sections that were not captured. Global/product-level permissions are not covered on this page.
