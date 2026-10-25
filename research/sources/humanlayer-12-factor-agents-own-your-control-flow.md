---
title: 12-Factor Agents, factor 8 "Own your control flow"
source_url: https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-08-own-your-control-flow.md
author: Dex Horthy (HumanLayer)
publisher: GitHub (humanlayer/12-factor-agents)
published: unknown
retrieved: 2026-10-25
type: docs
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [deterministic-scaffold-model-nodes, human-review-gates, work-structure-spectrum, rules-vs-judgment-encoding, harness-over-model]
relevance: high
---

## Relevance to the project
A practitioner pattern that splits control flow by step: the model proposes the next step as a structured intent, and the developer's own code decides what each intent does (execute and loop, or break out to wait for a human or a long job). It is a small, copyable answer to "who picks the next step": the model picks, code dispatches, and humans are reached by code-chosen breakpoints keyed to the kind of action.

## Themes
- deterministic-scaffold-model-nodes: a `while True` loop over `determine_next_step`, with a switch on the intent type the model returns.
- human-review-gates: `request_clarification` and `create_issue` break the loop (save the thread, message a human, wait for a webhook); `fetch_open_issues` continues ("sync step").

## Key points
- Claim: owning the loop lets you build control structures for your use case, e.g. pause for human approval or for a long-running pipeline.
- The pause is keyed to the action type, not to the model's confidence: approval is required by code for writes (`create_issue`), not for reads.
- My reading: this is risk-sloped human gating implemented as code, not as a model's choice to ask.

## Could not verify
- Undated factor page (series origin 2025-04, per the factor 10 note); practitioner opinion without measurement.

## Merged from a duplicate note of the same source (research-skill-rigidity-spectrum, 2026-10-25)

The same page was filed twice by two subagents; the second note is folded in here.

### Relevance to the project
Factor 8 is the engineering-side answer to "who picks the next step": the model proposes an intent as a structured tool call, and ordinary code (a loop with if/elif branches) decides whether to continue, pause for a human, or request approval. Factor 2 says prompts are first-class code to own, test and iterate rather than framework internals. Together they define the rigid end of control flow for agents built in code, as opposed to skills interpreted by a general agent. Factor 2 page: https://github.com/humanlayer/12-factor-agents/blob/main/content/factor-02-own-your-prompts.md. Factor 10 is noted separately (humanlayer-12-factor-agents-small-focused-agents). Published date is the origin essay's date from that note.

### Themes
- rules-vs-judgment-encoding: model proposes, code disposes: `request_clarification` breaks the loop and waits for a human; `deploy_backend` and `create_issue` break the loop for approval; `fetch_open_issues` (low risk) appends to context and continues (Factor 8).
- human-review-gates: the key capability is to "interrupt a working agent and resume later", especially between tool selection and invocation, so high-stakes calls can be approved without keeping the agent in memory (Factor 8).
- harness-over-model: prompts are "the primary interface between your application logic and the LLM"; own them so you can test and evaluate them like code (Factor 2).

### Key points
- Other owned-control patterns: summarising tool results, LLM-as-judge checks, compaction, tracing, rate limiting, durable waits.
- Classification: control flow code-fixed with model-chosen intents; gates by tool category (risk-sloped by design); stance toward the human = ask via tool call.

### Could not verify
- Factor 7 (contact humans with tool calls) not read.
