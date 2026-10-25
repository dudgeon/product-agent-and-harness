---
title: "TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation"
source_url: https://arxiv.org/abs/2410.03608
author: Jonathan Cook, Tim Rocktäschel, Jakob Foerster, Dennis Aumiller, Alex Wang
publisher: arXiv
published: 2024-10-04
retrieved: 2026-10-25
type: paper
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [standard-form-spectrum, model-judge-biases, skill-improvement-loops]
relevance: high
---

## Relevance to the project
Direct evidence on checklist vs holistic judgment for model evaluators: turning an instruction into per-instruction yes/no questions raised agreement with human preferences and, when the same checklists were handed to human raters, raised their agreement with each other too. It also closes the loop from evaluation to generation: a model that checks its own draft against the generated checklist and revises (Self-TICK) improves, which is the simplest form of a skill improving its output at run time. The checklist here is generated per task, not fixed, so it is a rubric instantiated as a checklist.

## Themes
- standard-form-spectrum: an LLM splits each instruction into YES/NO requirement questions and grades against them; exact agreement with human preferences rose from 46.4% to 52.2% vs direct scoring (abstract).
- model-judge-biases: human inter-annotator agreement on WildBench rose from 0.194 to 0.256 when raters were given the generated checklists (abstract): a checklist steadies human judges, not only model judges.
- skill-improvement-loops: Self-TICK self-refinement gave +7.8% absolute on LiveBench reasoning; checklist-scored best-of-N gave +6.3% on WildBench (abstract).

## Key points
- Protocol is fully automated and interpretable: each item shows which requirement a response met.
- The authors frame the gain as decomposition: multi-faceted preferences are not reduced to one ranking.
- My reading: the checklist is derived from the instruction, so it measures compliance with what was asked, not quality beyond the ask; the agreement gain is real but modest (about 6 points).
