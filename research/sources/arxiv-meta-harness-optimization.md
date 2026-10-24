---
title: Meta-Harness: End-to-End Optimization of Model Harnesses
source_url: https://arxiv.org/abs/2603.28052
author: Yoonho Lee, Roshen Nair, Qizheng Zhang, Kangwook Lee, Omar Khattab, Chelsea Finn
publisher: arXiv
published: 2026-03-30
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness, harness-over-model]
relevance: low
---

## Relevance to the project
Shows 'Meta-Harness' also names an academic system that searches over harness code. Useful to disambiguate the term and as evidence that the harness (not the model) is a first-class optimisable object.

## Themes
- [[meta-harness]]: the paper's sense is vertical: an outer-loop system that searches over harness code; unrelated to orchestrating Claude Code/Codex.
- [[harness-over-model]]: reports +7.7 points over a SOTA context-management system with 4x fewer context tokens on text classification, and harnesses beating hand-engineered baselines on TerminalBench-2.

## Key points
- Agentic proposer reads prior candidates' code, scores and traces via a filesystem.
