---
title: Coding agents love decision records
source_url: https://duncandavidson.com/agents-love-decisions
author: James Duncan Davidson
publisher: duncandavidson.com
published: 2026-09-01
retrieved: 2026-10-25
type: article
evidence: anecdote
filed_by: research-skill-rigidity-spectrum
themes: [decision-rationale-records, stale-records-mislead-agents, process-artifacts-as-coordination]
relevance: high
---

## Relevance to the project
A named practitioner (creator of Tomcat and Ant) reports what happens when ADRs become binding instructions for coding agents: agents follow them more rigidly than people, which helps and hurts. Both failure cases he names (overfitting to an obsolete decision; agents bloating the records) are directly relevant to a PM agent that keeps a decision log over weeks.

## Themes
- decision-rationale-records: accepted ADRs are binding, proposed ones non-binding context, superseded ones history only; stored in docs/decisions with rules in AGENTS.md (body).
- stale-records-mislead-agents: an agent preserved an outdated storage abstraction because an ADR called it mandatory, adding a compatibility layer instead of flagging the mismatch (body, failure cases).
- process-artifacts-as-coordination: agents are told to stop and propose an ADR change when a task conflicts with an accepted ADR (body).

## Key points
- Each ADR holds only current text; Git is the changelog; one "Updated:" line on substantive change; "Superseded-On:" for superseded; each rule stated once and cross-referenced.
- Benefits observed: agents less likely to mistake implementation detail for foundational rule; no code archaeology through issues.
- Failure 2, "deliberation bloat": when invited to update ADRs, agents added amendment logs, promoted small details to rules and repeated cross-references, making them hard for humans to read.
- Mitigations: explicitly allow agents to question decisions that no longer fit; watch for overfitting; keep ADRs short. He says the instructions are still evolving.
- Acceptance appears to stay with humans; the post does not state who writes ADRs.
