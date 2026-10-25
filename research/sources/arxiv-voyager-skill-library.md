---
title: "Voyager: An Open-Ended Embodied Agent with Large Language Models"
source_url: https://arxiv.org/abs/2305.16291
author: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar
publisher: arXiv (NVIDIA, Caltech, UT Austin, Stanford, ASU)
published: 2023-05-25
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops, skill-standards]
relevance: medium
---

## Relevance to the project
The origin of the "skill library" idea in agent research: an agent writes skills as executable code, verifies them against environment feedback, stores them and retrieves them for later tasks, and the library transfers to new worlds. It shows the self-written end of the improvement-loop dimension working when the environment gives cheap, honest feedback (Minecraft execution errors), which PM work mostly lacks; the gap between this and a PRD skill is the absence of an execution signal, not the loop design.

## Themes
- skill-improvement-loops: an "ever-growing skill library of executable code" plus iterative prompting with environment feedback, execution errors and self-verification; 3.3x more unique items, 2.3x longer travel, up to 15.3x faster tech-tree milestones than prior methods; library transfers to a new world (abstract).
- skill-standards: skills are stored as code with descriptions, which is the pattern later skill formats (SKILL.md plus scripts) adopted (my reading).

## Key points
- Three parts: automatic curriculum for exploration; skill library; iterative prompting with self-verification.
- Lifelong learning without weight updates; everything is in the prompt and the stored code.
- Abstract-only read; the embedding-indexed retrieval detail is not on the abstract page.
