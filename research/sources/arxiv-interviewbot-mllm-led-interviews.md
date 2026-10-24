---
title: "When the Interviewer Is a Bot: Behavior, Breakdowns, and Trust in MLLM-Led Interviews"
source_url: https://arxiv.org/abs/2608.10412
author: He Zhang, Kambinachi Chukwuma, ChanMin Kim, John M. Carroll
publisher: arXiv (accepted to ACM HCOMP 2026)
published: 2026-08-11
retrieved: 2026-10-24
type: paper
evidence: independent
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [tacit-knowledge-capture, research-synthesis-agents, agent-failure-modes]
relevance: high
---

## Relevance to the project

Independent, behaviour-level evidence on what an off-the-shelf LLM interviewer actually does: it acknowledges a lot and probes very little, which is exactly the move tacit-knowledge elicitation depends on. Bears directly on whether an interview-style context-creation agent can get past surface answers without heavy design work. Read at abstract level.

## Themes

- **tacit-knowledge-capture**: deepening probes were only 4.9% of 428 interviewer turns; the bot is "acknowledgment-heavy but probe-light" (abstract).
- **agent-failure-modes**: 28.7% of question-bearing turns stacked multiple questions despite an explicit one-question rule; four breakdowns in live use: information loss, premature termination, latency, interruption (abstract).
- **research-synthesis-agents**: reduced social pressure coincided with shallower elaboration; trust tracked perceived stakes and what using AI signalled about the organiser (abstract).

## Key points

- InterviewBot wraps a real-time multimodal (voice) LLM with a researcher-written outline; framed as an instrument to observe default behaviour, not a new architecture.
- N=15 participants, each followed by a human-led reflection session; turn-level analysis of 428 turns.
- Participants credited content-grounded paraphrase as listening; generic social filler earned no credit.
- Design implications: explicit depth control, transparent handoffs, non-templated listening.

## Could not verify

- Read at abstract level only; full-paper detail (prompts, domain of the interviews) not checked. Small sample; topic was not expert tacit knowledge specifically.
