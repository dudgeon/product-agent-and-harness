---
title: "Notion 3.8 release notes (October 13, 2026)"
source_url: https://www.notion.com/releases/2026-10-13
author: Notion
publisher: Notion releases
published: 2026-10-13
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [identity-delegation, enterprise-admin-controls, process-artifacts-as-coordination]
relevance: medium
---

## Relevance to the project
The most recent first-party change found in this track's area: Notion's version history now covers pages and databases and attributes each change to the person or agent that made it, and new column permissions set which properties each person or agent can view or edit. For a shared record that several agents and people write (a dependency register), per-property attribution and per-property write rights are the record-level audit and separation-of-duties primitives; they are not an approval workflow.

## Themes
- identity-delegation: "With agents and people making constant updates, version history has never been more important"; "Review what changed, see who changed it, and restore prior versions."
- enterprise-admin-controls: column permissions "let database owners control which properties each person or agent can view or edit"; admins "can see who connected each AI tool, check when it was last used" and can allow only verified or chosen MCP tools.
- process-artifacts-as-coordination: MCP-compatible agents "can read your workspace context and update docs and task trackers"; rebuilt synced databases (GitHub, Jira, Salesforce) show sync health so agents work from current data.

## Key points
- Skills API loads Notion Skills into GitHub; Notion Agent and Custom Agents draw on 150+ connected tools via MCP.
- No new trigger or session features in this release.

## Could not verify
- Whether attribution distinguishes an agent acting on its own from an agent acting for a named person. Read via WebFetch (model-summarised view).
