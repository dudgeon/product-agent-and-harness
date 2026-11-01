---
title: Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets
source_url: https://arxiv.org/abs/2604.02460
author: Dat Tran, Douwe Kiela
publisher: arXiv (cs.CL)
published: 2026-04-02
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [single-agent-many-skills, relay-information-loss, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
Holding reasoning tokens equal, a single agent matched or beat five multi-agent designs (sequential, subtask-parallel, parallel-roles, debate, ensemble) on multi-hop reasoning, consistent with an information-theoretic argument (data processing inequality). The authors say many reported multi-agent gains reflect extra compute and benchmark or API budget artifacts. Multi-agent became competitive mainly when the single agent's context was corrupted. Relevant to whether splitting intent shaping into several agents buys anything beyond extra tokens.

## Themes
- single-agent-many-skills: average accuracy at 1,000 thinking tokens: single 0.418 vs sequential 0.379, debate 0.388; at 5,000: single 0.427 vs debate 0.420, sequential 0.386.
- relay-information-loss: sequential multi-agent described as "the cleanest multi-agent analogue of single-agent reasoning" and is the weakest at most budgets.
- vendor-claims-vs-independent-evidence: API-based budget control (notably Gemini 2.5) and benchmark artifacts can inflate multi-agent gains.

## Key points
- Benchmarks FRAMES and MuSiQue (4-hop); models Qwen3-30B-A3B, DeepSeek-R1-Distill-Llama-70B, Gemini 2.5 Flash and Pro.
- Under heavy context masking or substitution, sequential multi-agent beat single; with distractors the single agent stayed ahead.

## Could not verify
- Last 20% of the HTML not read.
