---
title: GenAI Security Principles
source_url: https://engineering.block.xyz/blog/genai-security-principles
author: Wes Ring and Josiah Peedikayil (Block Product Security)
publisher: Block Engineering Blog
published: 2025-08-19
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [risk-review-as-classification, risk-sloped-review, enterprise-admin-controls, agent-protocol-security, human-review-gates]
relevance: medium
---

## Relevance to the project
Block's tiered requirements for any GenAI integration, keyed to its four Data Safety Levels. It explains how Block governs AI integrations at scale: a review process that got "several hundred requests", made tractable by a design-phase checklist. A transferable model for classifying agent capabilities by data sensitivity before review.

## Themes
- risk-review-as-classification: DSL-1 public to DSL-4 (full card numbers, SSNs); Tier 2/3/4 requirements map to DSL levels with RFC 2119 MUST/SHOULD.
- risk-sloped-review: e.g. least privilege SHOULD at Tier 2, MUST at Tiers 3-4; human reviewers for high-impact decisions SHOULD at all tiers.
- enterprise-admin-controls: review process for AI integrations; principles used as a checklist early in design to speed approvals.
- agent-protocol-security: "Everything is a prompt injection vector"; "LLMs are not good at authorization"; LLM output inherits input sensitivity.

## Key points
- MUSTs at every tier: treat LLM output as user content, never let the LLM enforce access control, avoid executing generated content.
- Mentions goose only as Block's open-source agent; MCP not discussed.
