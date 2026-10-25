---
title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
source_url: https://arxiv.org/abs/2510.04618
author: Qizheng Zhang, Changran Hu, Shubhangi Upasani, Boyuan Ma, Fenglu Hong, Vamsidhar Kamanuru, Jay Rainton, Chen Wu, Mengmeng Ji, Hanchen Li, Urmish Thakker, James Zou, Kunle Olukotun
publisher: arXiv (ICLR 2026)
published: 2025-10-06
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops, memory-architecture]
relevance: high
---

## Relevance to the project
The paper closest to "a skill file that rewrites itself". It names the two failure modes of naive self-rewriting, brevity bias (the rewriter compresses away domain detail) and context collapse (repeated whole-file rewrites erode the document), and replaces monolithic rewrites with a playbook that grows by small, structured delta updates produced by separate generate, reflect and curate steps. That is the design argument for curating corrections into a skill incrementally rather than letting an agent regenerate SKILL.md, and it reports gains without labelled data by using execution feedback.

## Themes
- skill-improvement-loops: contexts as "evolving playbooks that accumulate, refine, and organize strategies" through generation, reflection and curation; +10.6% on agent benchmarks (AppWorld) and +8.6% on finance tasks; matches the top production agent on the AppWorld leaderboard with a smaller open model (abstract).
- memory-architecture: works offline on system prompts and online on agent memory; structured incremental updates rather than rewrites (abstract).

## Key points
- Named failure modes of prior context-adaptation methods: "brevity bias" and "context collapse".
- Adapts without labelled supervision, from natural execution feedback.
- Claims lower adaptation latency and rollout cost, no figures on the abstract page.
- My reading: the roles (generator, reflector, curator) are the same split as Warp's base skill plus improver skill, with the human replaced by a curator model; the paper does not test where a human in the curate step would help.
