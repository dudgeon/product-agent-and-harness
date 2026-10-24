---
title: "Evals, error analysis, and better prompts: A systematic approach to improving your AI products | Hamel Husain (ML engineer)"
source_url: https://www.lennysnewsletter.com/p/evals-error-analysis-and-better-prompts
author: Claire Vo (host), Hamel Husain (AI consultant and educator)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-10-13
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [evals-autonomy-trust, outcome-measurement-gap, spec-becomes-prototype-and-evals, agent-failure-modes, human-judgment-pm-jobs, metrics-review-agents]
relevance: medium
---

## Relevance to the project
A practitioner walkthrough of how to evaluate an LLM product (worked example: Nurture Boss, an AI assistant for property managers) that maps directly onto our open dimension **pm-agent-evaluation**: read real traces, write one-line notes on the first upstream error, cluster and count, then write binary, failure-specific evals, and validate any LLM judge against hand labels before showing it to anyone. Two claims bear on the film and on intent shaping: the PM is usually the subject-matter expert who should do the annotation; and, citing the "Who Validates the Validators?" paper, people are "really bad at writing specifications or requirements until they need to react to what an LLM is doing". The evidence is consulting experience from a seller of an evals course, so anecdote, but the method is widely cited.

## Themes
- evals-autonomy-trust: LLM-judge dashboards with 1-5 scores for "helpfulness" are uninterpretable; use binary pass/fail per specific failure, hand-label data, and measure judge agreement before trusting it (29:34-31:56). Showing evals that disagree with people's lived experience of the product is "the moment like people lose trust in you" (31:10).
- spec-becomes-prototype-and-evals: requirements are externalised by critiquing model output: people can't write specs well "until they need to react to what an LLM is doing" (33:14, citing Shankar et al.). Evals are written only for failures actually observed, so the eval set becomes a record of what "good" means.
- outcome-measurement-gap: thumbs-up/down feedback captures only "a sliver" because users tolerate or abandon rather than report (host, 24:33); error analysis on traces is the substitute.
- agent-failure-modes: Nurture Boss's top counted issues were handoff to a human, tour scheduling (rescheduling created duplicate tours), missing follow-up and wrong information (20:11); a low-hanging cause was the system prompt lacking today's date (34:39); retrieval is "the Achilles heel of a lot of AI products" (34:39). Host: two wrong words in ChatPRD's system prompt silently broke a tool call (37:04).
- human-judgment-pm-jobs: "a lot of times it is the product manager that should be doing that annotation" because the PM holds the taste; AI engineer, AI PM and data scientist roles still all apply and won't collapse soon (48:28).
- metrics-review-agents: transition matrices across agent steps show where multi-step agents fail (e.g. generate-SQL to execute-SQL) (38:15); the host notes the same view doubles as product discovery on what users try to do (39:38).

## Key points
- **Process:** log traces; review a sample with a custom, vibe-coded annotation UI (filters by channel, annotated or not); note only the most upstream error per trace; have an LLM help bucket notes; count (16:33-20:11). The first pass "only took a few hours".
- **Eval types:** code-based checks for deterministic issues (e.g. user IDs leaking into replies) and LLM judges for subjective ones; synthetic inputs where traces are scarce (27:01-28:02).
- **Fixing:** mostly prompt engineering and experimentation; fine-tuning rarely needed but "basically free" once eval infrastructure exists (ReChat needed it) (36:11).
- **Non-technical experts:** host hopes operational staff (e.g. leasing agents) will contribute quality judgments directly (49:51).

## Notable quotes
- "People are really bad at writing specifications or requirements until they need to react to what an LLM is doing" (33:14).
- "The error analysis is the foundation for everything" (50:49).

## Could not verify
- Show notes read in full; transcript read 4:00-41:00 and 47:58-51:00; the rest (Hamel's personal writing and YouTube-chapter tools, ChatPRD prompt aside) skimmed by search.
- Claims of "immense" quality gains are client anecdotes without numbers. Hamel sells an evals course; the host's product sponsored the network.
- The cited paper's finding is paraphrased by the speaker; not checked against the paper here.
