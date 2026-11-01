---
title: "Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks"
source_url: https://arxiv.org/abs/2411.04468
author: Adam Fourney, Gagan Bansal, Hussein Mozannar, Cheng Tan, et al. (Microsoft Research AI Frontiers)
publisher: arXiv
published: 2024-11-07
retrieved: 2026-10-31
type: paper
evidence: first-party
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, agent-failure-modes, agent-frameworks]
relevance: medium
---

## Relevance to the project
The original design behind Microsoft's Magentic orchestration: an Orchestrator with an outer loop (task ledger of verified facts, facts to look up, educated guesses, and a plan) and an inner loop (a five-question progress ledger), which resets all agents' contexts when it replans. The ablation shows the ledgers carry much of the value (removing them cost 31% on GAIA validation), which supports keeping a shared, explicit work record at the coordinator rather than relying on transcripts.

## Themes
- process-artifacts-as-coordination: ledgers are the orchestrator's working record; plan is "a hint, not a strict script"; on replanning "we force all agents to clear their contexts and reset their states".
- agent-failure-modes: commonest error codes: persistent inefficient actions, insufficient verification, inefficient navigation; agents retried a failing login until the account was suspended and sometimes tried to recruit humans; authors call for "least privilege, and maximum oversight".
- agent-frameworks: four specialists (WebSurfer, FileSurfer, Coder, ComputerTerminal).

## Key points
- Stall counter threshold of 2 or less triggers reflection and a new plan.
- Results (test): GAIA 38.0% (GPT-4o plus o1), AssistantBench 27.7%, WebArena 32.8% (GPT-4o).
- Removing any single specialist agent cut performance 21-39%.
- First-party research (authors describe their own system); benchmarks are public.

## Could not verify
- Final 8% of the HTML not read.
