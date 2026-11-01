---
title: "LLM-based Multi-Agent Blackboard System for Information Discovery in Data Science"
source_url: https://arxiv.org/abs/2510.01285
author: Alireza Salemi, Mihir Parmar, Palash Goyal, Yiwen Song, Jinsung Yoon, Hamed Zamani, Tomas Pfister, Hamid Palangi (UMass Amherst, Google Cloud AI Research)
publisher: arXiv
published: unknown
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [blackboard-coordination, agent-frameworks, org-context-grounding]
relevance: high
---

## Relevance to the project
The best measured comparison found of a blackboard (broadcast a request, let specialists volunteer) against an orchestrator that assigns tasks (master-slave). Its argument against the orchestrator, that the controller must hold an accurate model of every agent's capabilities and holdings, is exactly the problem a dependency-mapping module faces: the feature team does not know which platform, process or gate owner holds what. It is evidence for a "post the ask, owners respond" pattern, with a measured cost premium.

## Themes
- blackboard-coordination: "there is no task assignment; instead, requests are broadcast on a blackboard"; helper agents decide for themselves whether to respond; responses go to a separate board only the main agent reads (Section 3).
- agent-frameworks: compared against master-slave, RAG and DS-GRU baselines across four backbone models.
- org-context-grounding: helper agents each own a cluster of files in a data lake; the main agent does not need to know which agent holds what.

## Key points
- Critique of orchestrators: subordinates must follow instructions even when they lack the information; "the central controller must maintain an accurate model of each agents capabilities to assign tasks"; overlapping expertise makes assignment ambiguous.
- Mechanism: main agent posts a request (e.g. likely column names, formats); file agents and a web-search agent volunteer responses (file locations, loading code, structure notes); main agent capped at 10 actions.
- Results (average macro, blackboard vs master-slave vs RAG): Claude 4 Opus 31.43 / 27.63 / 23.00; Gemini 2.5 Pro 28.53 / 24.01 / 18.51; abstract claims 13-57% relative end-to-end gains over the best baseline and up to 9% relative gain in file-discovery F1.
- Cost: about 1.8x master-slave and 2.3x RAG per question; similar runtime.
- Limits (my reading): benchmarks modified by the authors (filtered questions, pooled data lake); clustering by file names only; absolute scores low in some domains.
- Control: decentralised for "who contributes" (volunteering) but the main agent still decides what to use and when to stop; one main agent, so the through line of control stays with one party.

## Could not verify
- Retrieved via WebFetch of HTML v2 (revised 2026-01-31); only the first 100k characters were read. Exact original submission day not confirmed (arXiv ID implies October 2025).
