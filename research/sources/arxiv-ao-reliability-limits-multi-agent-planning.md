---
title: On the Reliability Limits of LLM-Based Multi-Agent Planning
source_url: https://arxiv.org/abs/2603.26993
author: Ruicheng Ao, Siyang Gao, David Simchi-Levi
publisher: arXiv (cs.MA)
published: 2026-03-27
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [relay-information-loss, agent-failure-modes]
relevance: high
---

## Relevance to the project
A formal and empirical treatment of the relay (model A's shape): without new outside information, a delegated chain of agents is dominated by a centralized decision maker holding the same information, and the gap is what communication and compression lose. In a test where downstream stages see only the relayed message, accuracy fell from 90.7% (one stage) to 22.5% (five stages, prose messages), while structured posterior-vector messages lost about 2.8 points per stage against 8.5 for prose. The implication for a relay of feature context is that what is written at each handoff, and whether later stages can reach the original, decides fidelity.

## Themes
- relay-information-loss: prose relay about 8.5 points lost per stage; posterior-vector relay about 2.8; at three stages 75.2% vs 58.1% (50-question subset).
- agent-failure-modes: five-stage prose relay fell "numerically below the 25% chance level for a four-way task".

## Key points
- Models gpt-4.1-mini and o4-mini; 200 four-way MMLU questions; "downstream stages see only the relayed message and not the original question".
- Theory links lost value to conditional mutual information (log loss) and posterior error (Brier); human review appears only in theory (a posterior-risk threshold for escalation), not tested.
- Technical note; artificial task (stages cannot see the source), which is the worst case for a relay.

## Could not verify
- Whether the result holds when later stages can read the original artifact (the feature-repo case).
