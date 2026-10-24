---
title: Decision Models Explained - The New AI Building Block for Product Teams
source_url: https://departmentofproduct.substack.com/p/decision-models-explained-the-new
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-10-13
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [cost-control-routing, risk-review-as-classification, human-review-gates, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A PM-audience explainer on "decision models": models that pick from a fixed set of typed answers with confidence scores instead of generating text, launched by many vendors in September and October 2026. It bears on harness internals rather than PM jobs: the cheap, fast choice steps inside an agent loop (is this action safe to run, which tool or model next, which bucket does this item go in). That makes it evidence for the cost-routing and pre-action safety-check options, and for treating risk review as classification. The one PM-harness case is second-hand: Rippling testing a decision model inside GrowthOS, described as its agent harness for go-to-market teams. All company figures are vendor or executive claims relayed by the author.

## Themes
- cost-control-routing: routing section; argues the routing step (which tool, which model, which team) is usually a small LLM call returning one word, and a decision model does it faster and cheaper. Cites Higgsfield auto-routing image and video models per step, and a Spotify engineer sending grunt work to cheaper models.
- risk-review-as-classification: "Safety checks before an agent acts": the same "is this safe to run?" question asked before every agent action, where latency matters; relays Vercel's CEO claiming an 18x speed-up after switching its safety checks.
- human-review-gates: scoring section; thresholds (e.g. above 0.8 escalates to a person) as the mechanism for routing work to humans.
- vendor-claims-vs-independent-evidence: every figure (Vercel 18x, Rippling 90% vs 50% accuracy and 8x speed, Perplexity 643 of 669 clinical decisions at 42% lower cost, adoption shares on Vercel's gateway and OpenRouter) is a vendor or CEO claim; the author notes the Decision Index leaderboards are only at versions 0.2.1 and 0.3.

## Key points
- **What it is:** input "state" plus "typed questions"; output is a probability per allowed answer, no text tokens. Vercel's definition is quoted to that effect.
- **Why now:** a launch timeline from 17 September to 9 October 2026 (TypeSafe's Jev first, then Cloudflare Clef, Amazon Strands Decider, Perplexity Decider, OpenAI Decision API, Liquid AI d1, Snowflake Decision, Microsoft-Decision-1, Databricks SQL access). Microsoft is said to be testing its model internally in incident response.
- **Five jobs:** safety checks before an agent acts; routing (tool, model, team); classification and triage; scoring against thresholds; inspecting images, audio and video.
- **Company cases (second-hand):** Rippling's GrowthOS (email classification by strategy); Harvey already routes with small LLMs in Vault; Cloudflare uses its own model to find personal data and spam; Lovable exposes Jev to apps its users build.
- **Limitations:** needs a fixed answer set (not for writing, summarising, reasoning); lacks business context. In the same Rippling test it did badly as a control step in a text-to-SQL loop because it could not interpret business definitions like "qualified pipeline"; Rippling concluded a hybrid works best. Benchmarks are immature.
- **How to try one:** three prompts (described, not reproduced): find every fixed-choice step in your product, map the vendor examples to your features, then rank candidates on frequency, speed sensitivity, current LLM cost, answer-set fixedness and cost of a wrong answer. A downloadable dataset of examples is offered.

## Notable quotes
- "returns structured answers with probabilities without generating text tokens" (Vercel, as quoted)

## Could not verify
- None of the launch dates, adoption shares or benchmark numbers were checked against the vendors' own posts; several cited posts were embedded media not present in the text.
- Rippling GrowthOS is named only in passing; no primary source on it is filed.
