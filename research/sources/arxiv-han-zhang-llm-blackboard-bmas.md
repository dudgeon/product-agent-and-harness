---
title: "Exploring Advanced LLM Multi-Agent Systems Based on Blackboard Architecture"
source_url: https://arxiv.org/abs/2507.01701
author: Bochen Han, Songmao Zhang
publisher: arXiv
published: 2025-07-02
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [blackboard-coordination, agent-frameworks, process-artifacts-as-coordination]
relevance: medium
---

## Relevance to the project
The clearest 2025 LLM revival of the classic blackboard: agents never message each other; each selected agent reads the whole shared board and writes back to it, and an LLM "control unit" decides who acts each round. It shows what a shared-record coordination medium buys (no per-agent memory, any specialist can contribute) and that someone still has to decide who acts next. Bears on whether the feature repo, or a shared record, can be the only integration point between a person's harness and the intent-shaping and dependency-mapping modules.

## Themes
- blackboard-coordination: "agents communicate solely through the blackboard without any direct contact" (Section 3); the control unit, itself an LLM, "selects the agents to participate in the current round".
- agent-frameworks: LbMAS adds predefined planner, decider, critic, cleaner and conflict-resolver roles to query-generated expert agents.
- process-artifacts-as-coordination: the board (public space plus private debate spaces) is the only shared state; a cleaner removes redundant entries and a conflict-resolver pulls contradicting agents into a private space.

## Key points
- Architecture: control unit + blackboard (public and private spaces) + agent group; each agent gets a randomly chosen base LLM.
- Loop: per round the control unit picks agents from query, board contents and agent descriptions; each picked agent takes the full board as its prompt and writes its output back; stops at 4 rounds or when the decider produces a solution; otherwise majority vote by similarity.
- Results: average 81.68 over six reasoning benchmarks (MMLU, ARC-C, GPQA-Diamond, BBH date, MATH, GSM8K) vs 80.09 CoT and 80.56 ChatEval; authors report +4.33% over CoT and +5.02% over static multi-agent systems on average.
- Cost: MATH at about 4.72M tokens vs 13.0M for MaAS. Removing the control unit raised tokens to about 13.9M with roughly unchanged accuracy: the scheduler mainly saves cost, not quality (as reported).
- Stated limits: few agent types, no code writing or tool use, limited benchmarks, no comparison against a shared memory pool.
- My reading: the board is untyped prose; "who acts next" is centralised in an LLM scheduler, so the blackboard decouples communication but not control. Short tasks (4 rounds), nothing like weeks-long asks.

## Could not verify
- Retrieved via WebFetch (model-summarised view of the HTML v1); numbers should be re-checked against the paper before quoting. Not peer-reviewed as far as the page shows.
