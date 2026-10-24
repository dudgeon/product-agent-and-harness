---
title: Intent Shaping in a Well-Managed Environment
source_url: https://claude.ai/artifact/LKZqiLtGYeAxEnAQZXoJMM
author: Geoff Dudgeon (written collaboratively with Claude)
publisher: Claude Docs (private artifact)
published: 2026-09-21
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-product-agent-and-harness
themes: [agent-led-intent-shaping, risk-review-as-classification, agent-ready-intent]
relevance: high
---

## Relevance to the project

This is Geoff's companion piece on intent shaping in regulated organisations. It specifies one concrete product agent, a risk advisor, and its harness functions: specification, classification against a taxonomy, and augmentation with a human in the loop. It is a ready-made candidate concept and prototype for later phases, and it shows how a product agent can be evaluated (false positives and negatives against SME labels). It bears on the open questions of which product-agent jobs are tractable first and how to govern and evaluate them.

## Themes

- **agent-led-intent-shaping**: §Iterative intent-shaping. The intent owner proposes, risk advisors assess, mitigations become requirements, and the spec tightens with each loop (for example, "a limited time offer" becomes "a 90-day offer with set language in named channels").
- **risk-review-as-classification**: §Risk review as a classification problem. A knowable universe of risks, each with objective heuristics, so review becomes specifying the intent and then classifying it. Novel risks need a curation path.
- **agent-ready-intent**: §How to build a risk agent, function 1. A canonical spec artifact that absorbs added detail and mitigations so it can be re-assessed.

## Key points

- **The shaping loop in a regulated organisation:**
  1. The intent owner (a BA or PM) states the goal and the initiative.
  2. Risk advisors assess the risks and recommend changes.
  3. The owner revises the plan or goals.
  - This should start before the owner commits to the initiative.
- **Implicit assumptions behind risk review:**
  - a knowable universe of in-scope risks
  - known heuristics for when each applies
  - heuristics objective enough for any capable actor to apply
  - the same heuristics can judge whether a novel mitigation works
- **What follows:** risk review is a specification and classification problem. Specify precisely, classify risks per component, re-classify after mitigations, and the owner accepts the residual risk.
- **The risk agent's three functions:**
  1. *Intent specification*: a canonical spec built from whatever detail exists, with mitigations added to it.
  2. *Risk classification*: a MECE taxonomy assessed component by risk (a "factorial assessment"). Low confidence asks the owner for detail. Review can be limited to one risk category.
  3. *Risk augmentation*: novel or off-taxonomy risks trigger manual SME review, which may add them to the taxonomy.
- **Suitable models:** LLMs, or classification-focused models (the doc names "JEV").
- **Why classification works:**
  - it mirrors today's process
  - it gives consistent judgment
  - it lets humans in the loop label outputs or classify independently
  - false positives and negatives map to heuristic fixes
  - sampled grading by SMEs makes monitoring simple
