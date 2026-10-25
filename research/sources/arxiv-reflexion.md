---
title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
source_url: https://arxiv.org/abs/2303.11366
author: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
publisher: arXiv (NeurIPS 2023)
published: 2023-03-20
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops]
relevance: medium
---

## Relevance to the project
The template for improvement by stored natural-language reflection rather than retraining: after a failed attempt the agent writes a critique of what went wrong into an episodic memory and reads it on the next try. Nearly every later "learn from corrections" mechanism (agent memory files, improver skills, cheatsheets) is a variant. The dependence on a feedback signal is the limit for PM work: on code the unit tests tell the agent it failed; on a PRD something or someone has to.

## Themes
- skill-improvement-loops: agents "verbally reflect on task feedback signals" and keep the text in an episodic memory buffer; 91% pass@1 on HumanEval vs 80% for GPT-4 (abstract).

## Key points
- No weight updates; improvement is via linguistic feedback carried between trials.
- Works with scalar or free-form feedback from the environment or a judge.
- Abstract-only read; ALFWorld and HotPotQA numbers not confirmed here.
