---
title: Creating a bespoke LLM for AI-generated documentation
source_url: https://www.databricks.com/blog/creating-bespoke-llm-ai-generated-documentation
author: Matthew Hayes, Hongyi Zhang, Tao Feng, Jan van der Vegt, Zaheera Valani, Reynold Xin
publisher: Databricks Blog
published: 2023-11-21
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [tacit-knowledge-capture, human-review-gates, legible-org-for-agents]
relevance: medium
---

## Relevance to the project

Evidence for a hybrid of owner curation and agent drafting: when the model drafts table and column descriptions and the owner accepts or edits them, documentation actually gets written ("more than 80%" of metadata updates AI-assisted). It shows the agent can lower the owner's cost of documenting. It does not show the drafts capture tacit meaning (they come from schemas). Vendor claim about its own product.

## Themes

- **legible-org-for-agents**: the problem stated is that most customer tables lack documentation, hurting both people and agents finding data (intro).
- **human-review-gates**: suggestions can be accepted one by one, in bulk, or edited; post-launch quality is tracked mainly by acceptance rate (review workflow, quality section).
- **tacit-knowledge-capture**: "more than 80% of the table metadata updates on Databricks are AI-assisted" (results). Drafts are generated from schema, so they capture what is inferable, not what only the owner knows.

## Key points

- Hackathon prototype on a SaaS LLM, then a fine-tuned MPT-7B on ~3,600 synthetic examples; two engineers, one month, under $1,000 compute; ~10x lower inference cost.
- Pre-launch eval: four employees, double-blind, 62 unseen tables. Small and informal.

## Could not verify

- No acceptance-rate number is published; no measure of whether accepted descriptions were correct or added business meaning.
