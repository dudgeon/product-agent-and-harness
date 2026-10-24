---
title: "The $47K agent loop: why logging, monitoring and max_tokens all failed to stop it"
source_url: https://dev.to/prashar32/the-47k-agent-loop-why-logging-monitoring-and-maxtokens-all-failed-to-stop-it-19ch
author: Adarsh Prashar
publisher: DEV Community
published: unknown
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-agent-runtime-patterns-taxonomy
themes: [cost-control-routing, agent-failure-modes, shared-persistent-sessions]
relevance: medium
---
## Relevance to the project
Second-hand, unverified account of a runaway multi-agent loop (about $47,000 over eleven days, November 2025) used to argue that cost control must be a deterministic pre-call per-run limit, not monitoring. The author sells a related tool (RiskKernel), and relays a post-mortem he says he has seen without linking it. Treat the incident as a plausible anecdote, the design argument as opinion.

## Themes
- cost-control-routing: claims four LangChain agents on A2A looped (Verifier requesting, Analyzer producing) with no termination condition or budget cap; 'They had logging. They had monitoring. They did not have a hard limit.'
- shared-persistent-sessions: argues enforcement should be deterministic, pre-call and per-run (cost, iterations, wall clock) with an external kill switch, separate from the agent

## Key points
- Search results also cite a '$50K accounting bot' (attributed to a Mandiant red team case) and a Claude Code sub-agent runaway; neither was traced to a primary source.

## Could not verify
- Incident not verified against a primary post-mortem; year of the DEV post not stated.
