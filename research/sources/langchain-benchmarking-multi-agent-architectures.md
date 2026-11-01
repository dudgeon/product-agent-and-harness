---
title: Benchmarking Multi-Agent Architectures
source_url: https://www.langchain.com/blog/benchmarking-multi-agent-architectures
author: Will Fu-Hinthorn (LangChain)
publisher: LangChain blog
published: 2025-06-10
retrieved: 2026-10-31
type: article
evidence: vendor-claim
filed_by: research-agent-handoff-models
themes: [relay-information-loss, single-agent-many-skills, agent-failure-modes, handoff-context-transfer]
relevance: high
---

## Relevance to the project
One of the few same-task comparisons of a single agent, a swarm (control transfer, the active agent talks to the user) and a supervisor (sub-agents return to it; only it talks to the user). The supervisor's main loss was "translation" between agents, likened to the game of telephone, and fixing what crosses the handoff (strip routing messages, forward replies verbatim) raised its score by nearly 50%. It is direct evidence that handoff content, not agent count, drives results.

## Themes
- relay-information-loss: supervisor gap attributed to "translation" errors, compared to "telephone"; `forward_message` reduced paraphrase errors.
- single-agent-many-skills: single agent slightly better with one distractor domain, falls off sharply with two or more; its tokens rise with distractors while swarm and supervisor stay roughly flat.
- agent-failure-modes: original supervisor "performed poorly" until fixes.
- handoff-context-transfer: removing handoff messages from sub-agent context helped them focus.

## Key points
- Setup: tau-bench retail, first 100 examples, gpt-4o, plus six synthetic distractor domains of 19 tools each.
- Swarm slightly beat supervisor throughout; supervisor used more tokens.
- Open questions named: multi-hop across agents, comparison with agents-as-tools.

## Could not verify
- Exact scores (in charts only); per-fix effects not isolated; vendor benchmarking its own libraries; single model and domain.
