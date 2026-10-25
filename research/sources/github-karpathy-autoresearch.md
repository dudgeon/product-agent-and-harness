---
title: "autoresearch (README)"
source_url: https://github.com/karpathy/autoresearch
author: Andrej Karpathy
publisher: GitHub
published: 2026-03-07
retrieved: 2026-10-25
type: other
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [skill-improvement-loops, deterministic-scaffold-model-nodes]
relevance: medium
---

## Relevance to the project
A minimal, widely copied harness for an agent that improves a piece of work overnight against a fixed metric. Its design is instructive for the improvement-loop dimension because the roles are split by file: the evaluator (prepare.py) is fixed and never edited by the agent; the work (train.py) is the only thing the agent changes; the human's whole contribution is program.md, which Karpathy calls a lightweight skill, and which the human iterates on as "research org code". The loop only works because val_bpb is a cheap honest metric, which is the standing obstacle for PM artifacts.

## Themes
- skill-improvement-loops: edit train.py, train for a fixed 5-minute budget, score on validation bits per byte, keep or revert, repeat; about 12 experiments an hour, "roughly 100 overnight"; human iterates on program.md rather than code (README).
- deterministic-scaffold-model-nodes: the evaluation and data code is fixed and off-limits to the agent; only one file is mutable, keeping diffs reviewable (README).

## Key points
- Three files: prepare.py (fixed: data, tokenizer, dataloader, evaluation), train.py (agent-editable: model, optimiser, loop), program.md (human-written agent instructions).
- Karpathy frames the human as designer of the research organisation, not the researcher.
- The README states no benchmark numbers; third-party reports of hundreds of experiments and transferred improvements were not verified here.

## Could not verify
- Results figures circulating in press (e.g. ~700 changes, ~20 transferred improvements) come from search snippets of third-party posts, not from the README.
