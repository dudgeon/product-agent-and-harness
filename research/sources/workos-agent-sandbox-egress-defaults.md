---
title: What your agent sandbox can reach by default
source_url: https://workos.com/blog/agent-sandbox-egress-defaults
author: Maria Paktiti
publisher: WorkOS blog
published: 2026-09-15
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, agent-failure-modes, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
An independent (WorkOS sells identity infrastructure, not coding agents) comparison of what Codex cloud and Claude Code can reach by default. It names gaps the vendors' own docs leave implicit: Codex setup-phase egress cannot be restricted and has no blocked-egress log; Claude Code's sandbox covers only Bash and repo-level hardening can silently do nothing. Copilot is not covered. Useful as the outside check on the egress rows in the comparison.

## Themes
- agent-failure-modes: Codex setup scripts "still run with internet access" and no documented setting restricts setup-phase egress; secrets are removed before the agent phase; no documented blocked-egress log.
- agent-failure-modes: Claude Code `strictAllowlist` is read only from user, managed or CLI settings, so setting it in a repo's `.claude/settings.json` "has no effect"; the sandbox restricts only Bash, while built-in file tools, MCP servers and hooks run on the host; credential paths readable unless denied; Claude Code on the web has a roughly 200-domain Trusted allowlist with four bypass paths, including the Anthropic API at None.
- vendor-claims-vs-independent-evidence: quotes Anthropic: "Any approach that allows network egress can still leak data the agent can read."

## Key points
- Recommends GET/HEAD/OPTIONS restriction on Codex, which would have blocked OpenAI's own exfiltration example.
- Argues egress restriction is a real control while detection filters catching "95% of attacks" are not sufficient.

## Could not verify
- Claims were not reproduced; model-summarised fetch. Copilot not covered.
