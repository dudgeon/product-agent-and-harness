---
title: "Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory"
source_url: https://arxiv.org/abs/2504.07952
author: Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan Jurafsky, James Zou (Stanford, Together AI)
publisher: arXiv (EACL 2026)
published: 2025-04-10
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops, agent-failure-modes]
relevance: medium
---

## Relevance to the project
A self-rewriting memory with no labels: the model stores strategies and code snippets it found useful and reads them on later problems. The headline result (GPT-4o on Game of 24 from 10% to 99% after it stored a brute-force solver) shows how much a stored skill can be worth. The limitations section is the useful part for PM harness design: memory quality depends on the model judging its own answers, faulty heuristics persist and spread, weak models gained little, and token cost rose about fivefold. These are the risks of the self-rewriting end of the improvement-loop dimension stated by its own proponents.

## Themes
- skill-improvement-loops: persistent inference-time memory of "reusable strategies, solution sketches, and code snippets"; DC-Cu (answer then curate) vs DC-RS (retrieve similar cases, refine, then answer); no ground truth or human feedback used (sections 2-3).
- skill-improvement-loops: Game of 24 GPT-4o 10% to 99% (DC-RS); Claude 3.5 Sonnet AIME 2024 23.3% to 50.0% and AIME 2025 6.7% to 36.7% (DC-Cu); GPQA-Diamond 59.6% to 68.7% (results).
- agent-failure-modes: self-curation without labels, persistent stored errors needing pruning, little gain for smaller models (GPT-4o-mini, Claude 3.5 Haiku), retrieval noise hurting some tasks, memory bloat; average tokens on AIME 2024 rose from 370 to 1,831 (limitations).

## Key points
- Black-box: no weight changes; everything lives in the prompt-side memory.
- Sequential design makes it awkward for parallel batch work.
- My reading: in PM work there is no "99% on Game of 24" moment because the task has no verifier; the failure list, not the gains, is what transfers.
