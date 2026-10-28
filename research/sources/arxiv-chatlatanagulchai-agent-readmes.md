---
title: "Agent READMEs: An Empirical Study of Context Files for Agentic Coding"
source_url: https://arxiv.org/abs/2511.12884
author: Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa, Brittany Reid, Kundjanasith Thonglek, Pattara Leelaprute, Arnon Rungsawang, Bundit Manaskasemsak, Bram Adams, Ahmed E. Hassan, Hajimu Iida
publisher: arXiv
published: 2025-11-17
retrieved: 2026-10-28
type: paper
evidence: independent
filed_by: research-dependency-agent
themes: [agent-legible-platform, stale-records-mislead-agents, legible-org-for-agents]
relevance: medium
---

## Relevance to the project
The largest empirical look at agent context files (2,303 AGENTS.md/CLAUDE.md-style files from 1,925 repos): they behave like configuration code, maintained through frequent small additions, and they describe how to build and test far more than constraints. Only about one in seven mentions security or performance. If platform teams write agent-facing descriptions the same way, they will tell agents how to use the platform but rarely what it forbids or checks.

## Themes
- agent-legible-platform: across 16 instruction types, most common are test procedures (75.9%), implementation details (70.8%), architecture (68.1%).
- stale-records-mislead-agents: files evolve through small incremental additions rather than deletions (median addition 57 words for Claude Code files, per search summary), so accumulated instructions are rarely pruned.
- legible-org-for-agents: "non-functional requirements such as security (14.8%) and performance (14.5%) are rarely specified."

## Key points
- v1 17 Nov 2025, revised 9 Aug 2026; authors from Japanese, Thai and Canadian universities (incl. Queen's, Polytechnique Montréal).
- Related: `arxiv-evaluating-agents-md` found context files can lower task success.
