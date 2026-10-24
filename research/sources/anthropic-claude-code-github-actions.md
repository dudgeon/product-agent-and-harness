---
title: Claude Code GitHub Actions
source_url: https://code.claude.com/docs/en/github-actions
author: Anthropic
publisher: code.claude.com
published: 2026
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [remote-agent-invocation, skill-standards, cost-control-routing]
relevance: high
---

## Relevance to the project
The event-driven pattern: Claude Code runs on a CI runner on @mentions, PRs or cron, with a plugin skill as the prompt (e.g. code-review). It is the cheapest way to run a standardised review agent shared by a team (workflow file plus shared secret), with identity via the GitHub App or OIDC workload-identity federation instead of a stored key.

## Themes
- `remote-agent-invocation`: Interactive mode (trigger phrase) vs automation mode (prompt input); runs plugin skills such as `/code-review:code-review --comment`.
- `cost-control-routing`: Costs: GitHub Actions minutes plus tokens; `--max-turns`, timeouts, concurrency controls; org-level reusable workflows.

## Key points
- Auth: ANTHROPIC_API_KEY, CLAUDE_CODE_OAUTH_TOKEN (tied to one person's subscription), or OIDC federation to a Console service account; Bedrock/Vertex/Foundry via OIDC.
- The shared GitHub App has a broad fixed permission set (Actions, Contents, Workflows, ...); a custom app is possible for the Action only.
- Trigger checks: needs write access, rejects bot actors unless allow-listed; fork PRs get no secrets on public repos.
- Code Review is also offered as a product without maintaining a workflow.
