---
title: How we built our multi-agent research system
source_url: https://www.anthropic.com/engineering/multi-agent-research-system
author: Jeremy Hadfield, Barry Zhang, Kenneth Lien, Florian Scholz, Jeremy Fox, Daniel Ford (Anthropic)
publisher: Anthropic Engineering blog
published: 2025-06-13
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [work-structure-spectrum, single-agent-many-skills, cost-control-routing, evals-autonomy-trust]
relevance: high
---

## Relevance to the project
Names which *kind of work* multi-agent fits (breadth-first, parallelizable, open-ended research) and which it does not (coding, shared-context, many dependencies), with cost data. It is the Anthropic-side companion to Cognition's post and the best published example of a "research synthesis" agent shape. Written for a research product, not for team process standardization.

## Themes
- work-structure-spectrum: open-ended research where steps cannot be planned in advance suits an orchestrator with subagents; coding has "fewer truly parallelizable tasks".
- cost-control-routing: agents use about 4x chat tokens, multi-agent about 15x; token use explained about 80% of performance variance on BrowseComp; the task must be valuable enough to pay.
- evals-autonomy-trust: start evals with about 20 real queries; LLM-as-judge with a rubric plus human testing; evaluate end state for stateful agents.

## Key points
- Lead Opus 4 plus Sonnet 4 subagents beat single-agent Opus 4 by 90.2% on Anthropic's internal research eval (vendor-reported).
- Limits: agents "are not yet great at coordinating and delegating to other agents in real time"; small lead-agent changes can change subagent behaviour unpredictably.

## Could not verify
- Internal eval not independently reproduced.
