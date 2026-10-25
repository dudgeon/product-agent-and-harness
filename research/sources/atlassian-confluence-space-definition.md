---
title: "What is a Confluence space"
source_url: https://support.atlassian.com/confluence-cloud/docs/what-is-a-space/
author: Atlassian
publisher: support.atlassian.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [work-structure-spectrum]
relevance: medium
---

## Relevance to the project

Confluence's 'space' is the container for documents tied to a team, project or initiative, and the Jira-side 'space' reuses the word. Shows that the doc container and the work-tracking container are separate objects joined by links, not one 'project' object.

## Themes

- work-structure-spectrum: a space is a loose knowledge container (knowledge base, launch or campaign space) with no enforced artifact types.

## Key points

- A space is a container for creating, storing and collaborating on work tied to a team, shared project or initiative; examples: a knowledge base, or a space per launch or campaign.
- A sibling page (use-spaces-to-organize-your-work) lists: personal space, overview/landing page, labels, whiteboards, databases, Smart Links, folders as organising elements.

## Could not verify

Space types (team, project, documentation, personal), permissions and page-hierarchy detail were not on the fetched pages.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.

## Verification (user-story-mapping re-check, 2026-10-24)

Re-read verbatim (curl, tags stripped), plus three sibling pages filed separately.
- Confirmed definition: "A space is a container where you and your team create, store, and collaborate on work related to a shared project or initiative. Think of it as a collaborative workspace or knowledge base for your team." (same sentence on create-a-space).
- Space types (earlier gap): current Confluence offers a "purpose" at creation: Collaboration, Knowledge base, or Custom, plus a permissions scheme; one space owner (user or group), many admins. See atlassian-confluence-create-a-space.md.
- Permissions (earlier gap): role-based space access is GA with default roles Admin, Manager, Collaborator, Viewer and custom roles; admin powers for public links, guest access, anonymous access, delete and archive are separate grants. Per-item restrictions: open, edit-restricted, restricted, restricted-by-parent; view restrictions inherit down, edit restrictions do not; no restrictions on the free plan. See atlassian-confluence-roles-space-permissions.md and atlassian-confluence-page-restrictions.md.
- Agent reach: the Rovo MCP server can read and set restriction state and content permissions, enable/disable public links, create spaces and set "space instructions" (see atlassian-rovo-mcp-server-supported-tools.md, Verification section).
- Where PRDs/specs/decisions live: Atlassian's guidance is page templates in a space, linked to Jira by embedded issue links (`/jira`), not typed objects: PRD template, project poster, DACI decision template (atlassian-confluence-prd-template.md, atlassian-confluence-project-poster-template.md, atlassian-confluence-daci-decision-template.md). None of the three mentions JPD ideas or Atlassian Home projects.
