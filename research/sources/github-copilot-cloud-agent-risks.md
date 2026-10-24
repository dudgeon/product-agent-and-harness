---
title: "Risks and mitigations for GitHub Copilot cloud agent"
source_url: https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations
author: GitHub
publisher: GitHub Docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, human-review-gates]
relevance: high
---
## Relevance to the project
The most explicit vendor control model for an agent that acts on behalf of a human inside a shared repo: co-authored signed commits, one writable branch, draft PRs that the requester cannot approve, write-access gating on who may trigger it, and session logs plus audit events. A strong template for the governance axis.

## Themes
- human-review-gates: PRs are drafts a human must review and merge; the agent cannot mark them ready, approve or merge; the requester cannot approve their own agent-created PR; workflows do not run until a user with write access approves
- shared-persistent-sessions: identity: commits are authored by Copilot with the requesting developer as co-author, signed ('Verified'), each linked to its session log; logs and audit events available to admins
- shared-persistent-sessions: only users with write access can trigger the agent and comments from others never reach it; pushes confined to one branch (the PR branch or a new copilot/ branch)

## Key points
- Hidden characters are filtered from input as a prompt-injection mitigation; firewall on by default but, per the firewall page, it covers only processes started via the agent's Bash tool, not MCP servers or setup steps.
- Runs in a GitHub Actions sandbox with read-only repo access; only secrets in the 'copilot' environment are passed (Microsoft Learn module, via search snippet).

## Could not verify
- Session lifecycle and exact identity/token used were not found in what was retrieved.
