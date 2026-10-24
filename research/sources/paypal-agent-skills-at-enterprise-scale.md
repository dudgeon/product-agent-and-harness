---
title: Agent skills at enterprise scale
source_url: https://developer.paypal.com/community/blog/agent_skills_at_enterprise_scale
author: PayPal engineering
publisher: PayPal Developer Community blog
published: 2026-10-09
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skills-marketplace, skill-supply-chain-security, org-learning-loop]
relevance: high
---

## Relevance to the project
A second enterprise "Dojo-like" design, independent of Ramp: a governed internal skills marketplace on top of team Git repos, with fail-closed validation and human review. Design principle "Decentralize authoring. Centralize trust, governance, and distribution." Describes architecture only; no usage metrics.

## Themes
- skills-marketplace: teams connect repos through a read-only GitHub App; webhooks create submissions; automated checks (structure, sensitive data, harmful instructions, prompt injection; duplicate detection advisory) then admin review of ownership, intent and scope; each version revalidated; only approved versions visible in the internal marketplace.
- skill-supply-chain-security: cites Snyk's 36.8% figure as motivation; roadmap adds secret scanning, static analysis, SBOMs, red-team evals.
- org-learning-loop: "thousands of employees"; planned "Agent Plugins" bundling approved skills and approved MCP servers by business function or persona (Sales, HR, IT, Developer).

## Key points
- Distribution targets named: Claude Desktop and Codex, "other AI tools": i.e. skills registry as harness-neutral distribution.

## Could not verify
- No numbers on skills, teams, adoption, incidents; "planned" features are not shipped claims.
