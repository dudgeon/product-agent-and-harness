---
title: "Claude's memory works everywhere, and you decide what's in it"
source_url: https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-08-25
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [memory-architecture, enterprise-admin-controls, agent-as-service-many-surfaces, org-context-grounding]
relevance: medium
---

## Relevance to the project
Anthropic made one user memory shared across Claude chat and Cowork (including cloud-run Cowork tasks), written continuously during conversation, stored as short per-topic files the user can read, edit or delete, with sensitive categories off by default and some categories never stored. For a product agent this is a concrete reference design for personal memory with user-visible, editable state and privacy defaults, and for Team/Enterprise it is admin-gated and off for users until they opt in. It is personal memory, not shared team or org memory, and the post does not cover retention, audit or how memory interacts with org data controls.

## Themes
- memory-architecture: memory updates "as you chat" rather than by post-conversation summary; stored as a list of short files under Topics that the user can read, edit, delete, pause or reset ("Memory updates as you chat"; "See and edit").
- enterprise-admin-controls: for Team and Enterprise, admins control availability and memory is off for each user until they turn it on ("Getting started").
- agent-as-service-many-surfaces: same memory in chat and Cowork, including Cowork tasks running in the cloud, carried in both directions ("One memory across Claude Cowork and chat").
- org-context-grounding: examples include team metric definitions explained once in chat and reused in every QBR deck Cowork builds, and knowing the user's manager and their update preferences (same section).

## Key points
- **Sensitive-topic defaults:** health, race, ethnicity, religious beliefs, politics, gender identity and similar are not stored by default; a user can opt in, sees a notice on each such save, and it is not retroactive.
- **Never stored:** government ID numbers, criminal history, immigration status, or AUP-violating content, even with the opt-in; Claude tells the user when it declines to save.
- **Defaults by plan:** on by default for Free, Pro and Max; for Team/Enterprise, admin-controlled and off per user until enabled.
- **Correction model:** a fix in one topic file propagates to all future conversations (e.g. a renamed company).
- **Missing:** whether memory is shared across a team or project, how long topic files are retained, whether admins can view or export memory, interaction with Claude Code memory (not mentioned), and how wrong inferred memories are detected other than by user inspection.

## Notable quotes
- "Everything Claude remembers is in a list of files under Topics in Memory settings, where you can read, edit, or delete each one."

## Could not verify
- Help Center detail on retention and enterprise controls was not read.
