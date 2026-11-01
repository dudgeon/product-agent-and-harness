---
title: "LLMs Get Lost In Multi-Turn Conversation"
source_url: https://arxiv.org/abs/2505.06120
author: Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
publisher: arXiv
published: 2025-05-09
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [relay-information-loss, agent-failure-modes, docs-as-code-prd]
relevance: high
---

## Relevance to the project
The strongest counter-evidence to "transcripts beat documents": when the same requirements arrive piecemeal over a conversation, 15 models lose 39% on average, but when the pieces are consolidated into one instruction (CONCAT) they keep about 95% of full performance, and the authors recommend summarising and restarting in a fresh conversation. That is evidence for model A's written-artifact handoff and against keeping one long-running session as the only carrier of intent. It also uses "sharding" in the opposite sense to BMAD's document sharding.

## Themes
- relay-information-loss: a long accumulating conversation is itself a lossy carrier: "when LLMs take a wrong turn in a conversation, they get lost and do not recover" (abstract).
- agent-failure-modes: degradation is "a minor loss in aptitude and a significant increase in unreliability"; models make early assumptions and over-rely on premature answers.
- docs-as-code-prd: consolidating requirements into a single instruction recovers most performance; "starting a new conversation that repeats the same information might yield significantly better outcomes" (Section 7.4).

## Key points
- Setup: 600 instructions over six generation tasks, each split into shards revealed one per turn by a simulated user; 15 LLMs from eight families; over 200,000 simulated conversations.
- FULL vs SHARDED: "every model sees its performance degrade on every task ... average degradation of -39%". CONCAT (all shards in one turn) about 95% of FULL.
- Mitigations: RECAP (restate all shards at the end) raised GPT-4o-mini and GPT-4o from 50.4/59.1 to 66.5/76.6; SNOWBALL (restate each turn) 61.8/65.3; both trail FULL.
- Advice: "Consolidate before retrying": ask the model to summarise what the user said, carry it into a fresh conversation.
- Limits: simulated users; generation tasks, not product work; no agent-to-agent setting.

## Could not verify
- Retrieved via WebFetch of HTML v1 (first 100k of 184k characters); table values as summarised, re-check before quoting.
