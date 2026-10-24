---
title: About GitHub Copilot cloud agent (coding agent)
source_url: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
author: GitHub
publisher: docs.github.com
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, skill-standards]
relevance: medium
---

## Relevance to the project
GitHub's native delegate-to-cloud-agent flow: start from the agents panel, chat, issue or PR; the agent works in an ephemeral cloud environment and opens a PR. Hard limits: one repository, one branch, one PR per task, 59-minute maximum session. Supports custom agents, agent skills, hooks and MCP (default GitHub MCP scoped to the repo).

## Themes
- `remote-agent-invocation`: Max 59 minutes per session (not extendable; shorter via timeout-minutes), one repo, one PR per task, GitHub-hosted repos only; teammates can follow shared sessions.

## Key points
- Custom agents and skills give task-specific instructions to delegated work.
- Repository admins can disable it per repo; billing via premium requests (details elsewhere).

## Could not verify
- Firewall details and cost not on the fetched page.
