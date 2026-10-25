---
title: Guardrails (OpenAI Agents SDK)
source_url: https://openai.github.io/openai-agents-python/guardrails/
author: OpenAI
publisher: OpenAI Agents SDK docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [gate-judge-separation, agent-frameworks, policy-enforcement-fail-open]
relevance: medium
---

## Relevance to the project
OpenAI's gate primitive is deliberately agnostic about who judges: a guardrail can be a cheap model agent, an external classifier or a plain function, and it trips a wire that halts the run. It also names a tradeoff the PM harness will face: run checks in parallel (fast, but the agent may already have acted) or blocking (slower, no side effects).

## Themes
- gate-judge-separation: input and output guardrail examples use "a small, cheap agent" to classify; tool guardrails are plain Python functions (block arguments matching an `sk-` pattern); a guardrail "can call an external classifier directly; it does not need to run another agent."
- policy-enforcement-fail-open: parallel by default, so "the agent may already have used tokens or run tools before a tripwire cancels it"; `run_in_parallel=False` makes the guardrail run "and complete before the agent starts".

## Key points
- Three kinds: input guardrails (first agent only), output guardrails (final agent only, always after it finishes), tool guardrails (before and after each function tool; can skip the call, replace output or trip).
- A tripwire raises an exception and stops the run; the app catches it.
- Example: a fast agent detects math-homework requests sent to a customer-support agent and trips.

## Could not verify
- Page undated; no guidance on error rates of model-based guardrails.
