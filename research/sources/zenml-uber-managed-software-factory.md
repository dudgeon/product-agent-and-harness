---
title: "Uber: Building a Managed Software Factory with Agentic AI"
source_url: https://www.zenml.io/llmops-database/building-a-managed-software-factory-with-agentic-ai
author: ZenML (unnamed editor)
publisher: ZenML LLMOps Database
published: unknown
retrieved: 2026-11-02
type: article
evidence: independent
filed_by: competitive-teardown-uber-cortana
themes: [agent-as-service-many-surfaces, skills-marketplace, org-context-grounding, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
An independent-but-derivative write-up of Uber's AI Engineer software-factory talk; it adds no Cortana facts beyond the talk and is useful only as a cross-check of the talk's numbers and for its critical caveat that volume metrics do not show business value or code quality. Use the talk note instead for claims.

## Themes
- agent-as-service-many-surfaces: Cortana as "the unified interface layer" on Slack, CLI and web; employees add custom skills and prompts and put it in team Slack channels; 300 personas in the first month, 20,000+ sessions a day (Cortana section).
- skills-marketplace: 2,500 skills, 20,000+ executions/day, lint checks and review before acceptance, feedback from traces and comments to authors.
- org-context-grounding: context graph of ~150 node and edge types and ~40M entries replacing 20-30 systems; used for on-call RCA, planning, data analysis and security scans.
- vendor-claims-vs-independent-evidence: the entry's own assessment says the quantity metrics (70%+ agent PRs, 2x lines per engineer) do not establish business value or quality.

## Key points
- Restates the six building blocks (model gateway with SPIFFE/SPIRE identity and per-project/user/team attribution; MCP gateway with 1,000+ tools and 40% token savings via direct MCP → "Omni MCP" → CLI projection → code-mode skill; DevPods; skills; context graph; Cortana) and the feature walkthrough (Cortana determines rollout scope, drafts two Figma variants for an A/B test; Minion stops at a draft PR; validation table with screenshots).
- Maintenance loops capped and scheduled on Sundays.

## Could not verify
- No author or exact date on the page. Nothing here beyond the talk.
