---
title: Agent management for enterprises (GitHub Copilot docs) and "Enterprise AI Controls & agent control plane now generally available"
source_url: https://docs.github.com/en/copilot/concepts/enterprise/agent-management
author: GitHub
publisher: GitHub Docs; GitHub Changelog
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, identity-delegation, skills-marketplace, harness-portability]
relevance: high
---

## Relevance to the project
GitHub's "agent control plane" (AI Controls) is the only vendor console found that governs several vendors' agents (Copilot cloud agent plus Claude and Codex as partner agents) in one place, with session search, audit and enterprise-wide custom agents. It is a hosted multi-harness control plane in the sense of the governance-control-plane dimension, but bounded to agents running on GitHub.com; local agents in VS Code are outside it. Companion read: GA changelog dated 2026-02-26 (https://github.blog/changelog/2026-02-26-enterprise-ai-controls-agent-control-plane-now-generally-available/).

## Themes
- enterprise-admin-controls (proposed): AI Controls is "a centralized platform where you can manage and monitor AI policies and agents across your enterprise"; enterprise owners and AI managers set Copilot cloud agent policy in four states (one named: "Enabled for selected organizations", selectable by custom properties such as compliance tier); enterprise policy cannot be overridden at org level; REST API available (docs).
- harness-portability: partner agents Claude and Codex have separate policies; "Disabling or restricting Copilot cloud agent does not automatically disable third-party agents, and vice versa" (docs).
- skills-marketplace: enterprise custom agents version-controlled in `.github-private/agents/*.md`; a one-click push rule protects `.github/agents/*.md` across the enterprise; API to apply enterprise-wide custom agent definitions (changelog 2026-02-26).
- identity-delegation: enterprise custom roles can grant fine-grained access to audit logs, agent session activity and AI Controls (changelog).

## Key points
- Agents page: availability of cloud agent, code review and custom agents; who can manage enterprise custom agents; sessions from the last 24 hours; agentic audit events. GA lifted the 1,000-record session cap and added per-agent search including third-party agents.
- MCP: allow or block MCP entirely; registry of approved servers; "Private MCP registries apply to Copilot CLI and IDEs, but not to cloud agents that run on GitHub." For cloud agents, MCP servers are configured per repository or in enterprise custom agent profiles. Enterprise-wide MCP allowlists stayed in preview at GA (later GA via managed settings, 2026-08-06; see [enterprise managed settings](github-copilot-enterprise-managed-settings.md)).
- `managed-settings.json` (hosted on GitHub or installed on machines) controls plugin installation and "allow all" commands.
- "Agents running in Visual Studio Code are not managed through GitHub at all."
- Custom properties are evaluated only at configuration time; orgs are not re-enabled or disabled automatically when properties change.
- The legacy Copilot policies page was removed; AI Controls is the permanent home.

## Could not verify
- The other three cloud-agent policy states are not named on the page. Docs page undated; changelog dated 2026-02-26. Model-summarised fetch.
- GitHub's Well-Architected "Governing agents" page (learn.github.com) rendered empty; its reported anti-pattern ("enabling agents without audit log streaming or model restrictions") was seen only in a search summary.
