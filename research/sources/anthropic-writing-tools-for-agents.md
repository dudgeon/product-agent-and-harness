---
title: Writing effective tools for agents — with agents
source_url: https://www.anthropic.com/engineering/writing-tools-for-agents
author: Anthropic
publisher: Anthropic Engineering
published: 2025-09-11
retrieved: 2026-10-25
type: article
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [deterministic-scaffold-model-nodes, work-structure-spectrum, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Gives a third place to put rigidity besides workflow code and gates: inside the tool. Consolidating a multi-step procedure into one tool (`schedule_event` rather than list-then-create) fixes the sequence in code while leaving the choice of *when* to call it to the model. For PM skills this suggests packaging fixed sub-procedures (e.g. "assemble the decision log") as tools or scripts the model calls.

## Themes
- deterministic-scaffold-model-nodes: tools are "a contract between deterministic systems and non-deterministic agents"; consolidate workflows into single tools (`schedule_event`, `search_logs`, `get_customer_context`).
- evals-autonomy-trust: evaluate tools with realistic multi-step tasks with verifiable outcomes, read transcripts, track tool-call counts, errors, tokens; held-out test sets.

## Key points
- Agents may call a tool, answer from general knowledge or ask a clarifying question, so tools must be designed for agents rather than wrapped APIs.
- Too many or overlapping tools distract agents from efficient strategies.
- Iterate on tools with Claude Code itself.

## Could not verify
- Read via summary fetch; no quantified results recorded here.
