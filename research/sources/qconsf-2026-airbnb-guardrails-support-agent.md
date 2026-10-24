---
title: "How Airbnb Guardrailed Its AI Customer Support Agent (QCon San Francisco 2026 abstract)"
source_url: https://qconsf.com/presentation/nov2026/how-airbnb-guardrailed-its-ai-customer-support-agent
author: Weiping Peng (Distinguished Engineer, Airbnb)
publisher: QCon San Francisco 2026
published: unknown
retrieved: 2026-10-24
type: other
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [policy-enforcement-fail-open, evals-autonomy-trust, risk-sloped-review]
relevance: low
---

## Relevance to the project
Abstract only (talk is on 2026-11-16, not yet given). Describes the layered safety stack around Airbnb's support agent and says it became the base of a centralised AI risk platform used across Airbnb. Relevant to trust defaults: measure in shadow before enforcing, and ship mitigations as configuration.

## Themes
- policy-enforcement-fail-open: deterministic input sanitisation, fine-tuned classifiers for jailbreak, prompt injection and harmful content on both user messages and the agent's drafts; repeat-offender tracking; blocked messages removed from history.
- evals-autonomy-trust: LLM-as-judge labelling of production traffic, tiered golden and holdout sets, shadow runs; one shadow run showed a configuration would have over-blocked legitimate messages.
- risk-sloped-review: escalation ladder from regex blocklists, to zero-shot prompt hotfixes, to trained classifiers.

## Key points
- The agent serves "millions of customers" (abstract).
- Track: "Guardrails & Safety Nets (Evals) for the New Landscape".

## Could not verify
- No metrics; slides and video not yet available.
