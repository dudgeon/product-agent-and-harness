---
title: "Under the Hood: Scaling Responsible AI at Uber"
source_url: https://www.uber.com/us/en/blog/scaling-responsible-ai/
author: Melissa Barr, Melda Salhab (Senior TPMs, Uber)
publisher: Uber Engineering Blog
published: 2026-04-13
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [process-governance-load, governance-as-code, docs-as-code-prd]
relevance: low
---

## Relevance to the project
Uber's responsible-AI programme starts governance in the PRD and ERD review process ("shift-left") and gates deployment on Model Cards held in a central Model Catalog. It shows PRD/ERD reviews already act as the governance checkpoint at Uber, which is the process the first-pass PRD reviewer and the PRD/ERD tool feed. It covers ML models, not agents.

## Themes
- process-governance-load: checks begin in PRD and ERD document review, not at release (Review process).
- governance-as-code: Model Cards prompted before deployment create an auditable gate; Model Catalog as single source of truth for deployed models (Gating, Registry).
- docs-as-code-prd: PRD and ERD reviews are the named entry point for governance.

## Key points
- Five pillars; explainability tooling in Michelangelo (PFI, TreeSHAP, integrated gradients); training courses and an AI Resource Hub.
- No numbers; no agent-specific governance, AI Guard or risk tiers.

## Notable quotes
- "we built an evergreen, centralized inventory of all AI systems at Uber"

## Could not verify
- Whether agents (personas, Minion runs) go through the same Model Card / catalog gate.
