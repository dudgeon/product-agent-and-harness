---
title: "Linear for Agents (developer docs)"
source_url: https://linear.app/developers/agents
author: Linear
publisher: linear.app
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [identity-delegation, shared-persistent-sessions, harness-portability]
relevance: high
---

## Relevance to the project

Linear's model for third-party agents: install as an OAuth app with actor=app, appear as a workspace member, be delegated (not assigned) issues, receive agent-session webhooks. The delegate-not-assignee rule is a clean first-party pattern for human accountability, relevant to the harness.

## Themes

- identity-delegation: assigning an issue to an agent sets it as delegate; the human stays assignee.
- shared-persistent-sessions: agent sessions start automatically on mention or delegation; webhook expects a thought activity within 10 seconds.

## Key points

- Agents can be @mentioned, assigned issues, comment, and collaborate on projects and documents; installed agents are not billable users.
- Scopes: app:assignable (delegate on issues, project member), app:mentionable, plus customer and initiative read/write.
- Admins can change or revoke team access; PermissionChange webhook.
- promptContext builds a string from issue, comments and guidance.

## Could not verify

The page does not enumerate everything an agent can read or write; the separate Agent Interaction docs would. Linear MCP page (linear.app/docs/mcp) lists issues, projects and comments tools, and does not mention initiatives or documents, with endpoints mcp.linear.app/mcp and a /mcp/readonly variant using OAuth 2.1 or API key.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.
