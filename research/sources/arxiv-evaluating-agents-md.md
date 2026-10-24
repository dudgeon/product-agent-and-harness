---
title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
source_url: https://arxiv.org/abs/2602.11988
author: Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev (ETH Zurich)
publisher: arXiv (ICLR 2026 submission)
published: 2026-02-12
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-standards, harness-portability, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
The portable context-file standard is itself under evidence challenge: on AGENTBENCH (138 real Python issues in repos with committed context files) context files reduced task success relative to no context and raised cost over 20%. Argues for minimal, human-written, requirement-only content, which also bears on how much to put in always-on instructions vs on-demand skills.

## Themes
- skill-standards: agents follow context-file instructions, which increases exploration and testing; unnecessary requirements make tasks harder.
- evals-autonomy-trust: three arms (none, LLM-generated, human-written) across several coding agents/models (per secondary coverage: Claude Sonnet 4.5, GPT-5.2, GPT-5.1 mini, Qwen3-30B-coder).

## Could not verify
- Specific percentages (abstract gives none); secondary coverage only for model list; Python-only benchmark.
