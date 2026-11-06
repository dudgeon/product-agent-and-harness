---
title: "LLMREI: Automating Requirements Elicitation Interviews with LLMs"
source_url: https://arxiv.org/abs/2507.02564
author: Alexander Korn, Samuel Gorsch, Andreas Vogelsang
publisher: arXiv (RE 2025)
published: unknown
retrieved: 2026-11-06
type: paper
evidence: independent
filed_by: design-requirements-agent
themes: [elicitation-agent-evidence, agent-led-intent-shaping, ai-synthesis-hallucination-risk]
relevance: high
---

## Relevance to the project
A controlled study of a GPT-4o interview bot run with 33 role-playing stakeholders against a baseline of 18 trained human student interviewers. The bot made about as few interviewer mistakes as the trained humans and elicited up to 73.7% of the ground-truth requirements (60.9% fully, 12.8% partially), with a large share of context-deepening questions. It also hallucinated once (a price estimate) and asked once for an email address, and sometimes ended interviews early. It is the best measured evidence on the "inquire" step of the intent-shaping agent: useful for a first pass with many stakeholders, with humans following up on complex or sensitive topics.

## Themes
- elicitation-agent-evidence: requirements coverage up to 73.7%; ratings disagreed that mistakes were present in 64.2% (long prompt) and 59.1% (short prompt) of items; communication skills rated slightly better than human interviewers (RQ1, RQ2).
- agent-led-intent-shaping: question types: context-deepening 44.4% (short) and 32.3% (long); context-enhancing (the bot suggesting) 15.3% and 10.4%; context-independent about 28% (RQ3). The short prompt's key instruction was to ask one question at a time.
- ai-synthesis-hallucination-risk: one unfounded price estimate; one request for personal data; early termination when the user seemed busy (limitations).

## Key points
- Two prompts: a three-sentence zero-shot prompt and a long prompt with a role, a five-step interview guideline and error handling; no statistically significant difference in requirements elicited. Fine-tuning GPT-3.5 on 50 transcripts was abandoned (incoherent, language switching).
- Scenarios were generic (a salon, a ski resort) with 8 and 12 ground-truth requirements; participants were students role-playing.
- Authors' implication: most value in early, automated interviews at scale; context-enhancing suggestions can steer the stakeholder and need care.

## Could not verify
- Read through WebFetch's model-summarised view of HTML v1. Publication day left unknown (arXiv July 2025; RE 2025 research track listing seen in search).
