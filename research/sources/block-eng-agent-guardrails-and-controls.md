---
title: "Agent Guardrails and Controls: Applying the CORS Model to Agents"
source_url: https://engineering.block.xyz/blog/agent-guardrails-and-controls
author: Alex Rosenzweig and Clinton Carpene (Block)
publisher: Block Engineering Blog
published: 2026-01-11
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-block-product-practices
themes: [agent-protocol-security, human-review-gates, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
A proposed (not shipped) deterministic control for goose: treat any tool call made after another tool call, with no user message in between, as "cross-origin" and stop or ask. It is a concrete design for where an approval gate should sit in a general agent that reads untrusted content (email, docs, tickets), which a PM agent constantly does.

## Themes
- agent-protocol-security: maps LLM to untrusted client code, agent to browser, MCP server to web server; poisoned-email scenario (threat model).
- human-review-gates: halt or ask the human on a second chained tool call; reset after the next user prompt (proposed controls).
- evals-autonomy-trust: "none of the decision making involved with authorising tool calls can or should be handled by the LLM" (caveats); Block says it will benchmark the idea in goose and publish either way.

## Key points
- Optionally flush tool-call responses from context between user turns, at the cost of re-running tools.
- Reviews existing defences (OAuth, app stores, classifiers like Prompt Guard, sandboxing) and their gaps; does not stop second-order injection.
- Feedback invited via a goose GitHub discussion.

## Could not verify
- Whether the proof of concept or benchmark was published.
