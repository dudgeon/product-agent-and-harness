---
title: "ReqElicitGym: An Evaluation Environment for Interview Competence in Conversational Requirements Elicitation"
source_url: https://arxiv.org/abs/2602.18306
author: Dongming Jin, Zhi Jin, Zheng Fang, Linyu Li, XiaoTian Yang, Yuanpeng He, Xiaohong Chen (Peking University and others)
publisher: arXiv
published: 2026-02-20
retrieved: 2026-11-06
type: paper
evidence: independent
filed_by: design-requirements-agent
themes: [elicitation-agent-evidence, agent-led-intent-shaping, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
A 2026 benchmark that measures how well frontier models elicit implicit requirements over a multi-turn interview with a simulated user who only answers what is asked. Across 101 website scenarios and 632 hidden requirements, the best model elicited 32% of implicit requirements; Claude Opus 4.5 elicited 7 to 8% while ending interviews after about six turns. Free-form chat, without a structure for what to ask about, misses most of what a person did not say. This is direct support for the intent-shaping design choice to screen against a fixed category list and read context before asking, rather than rely on open conversation; it also gives a ready-made eval harness pattern (oracle user, LLM judge validated against experts).

## Themes
- elicitation-agent-evidence: IRE (share of implicit requirements elicited) best 0.32 (DeepSeek V3.2, no chain-of-thought); GPT-5.2 0.13; Gemini 3 Flash 0.11; Claude Opus 4.5 0.08; style requirements near zero in almost all settings.
- agent-led-intent-shaping: models ask far more probing than clarifying questions and clarification is less effective (GPT-5.2 ESR 0.04 for clarify versus 0.22 for probe); useful questions tend to come late; chain-of-thought raises the rate of key questions asked early (TKQR) and shortens dialogues but does not reliably raise coverage.
- evals-autonomy-trust: the oracle user was validated against 33 real interview transcripts (Cohen's kappa 0.73); the LLM judge against expert annotations (kappa 0.78 for action, 0.73 for relevance).

## Key points
- Scenario = underspecified initial requirement + hidden implicit requirements (interaction, content, style) + complete final requirement; 20-turn cap.
- Stopping behaviour varies widely: GPT-5.2 used almost all 20 turns; most models stopped at 4 to 8 turns.
- Structured, task-oriented application types (dashboards, IRE about 0.27) did better than e-commerce (about 0.05).

## Could not verify
- Read through WebFetch's model-summarised view of HTML v1, which noted internal inconsistencies (10 versus 20 application types; six versus seven models; oracle model version). Website domain only; generalisation to enterprise or regulated features is untested.
