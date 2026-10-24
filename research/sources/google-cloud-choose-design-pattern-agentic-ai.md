---
title: Choose a design pattern for your agentic AI system
source_url: https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system
author: Google Cloud Architecture Center
publisher: Google Cloud docs
published: 2026-05-28
retrieved: 2026-10-24
type: docs
evidence: vendor-claim
filed_by: research-agent-runtime-patterns-taxonomy
themes: [work-structure-spectrum, single-agent-many-skills, human-review-gates, agent-frameworks]
relevance: high
---

## Relevance to the project
The most explicit decision table from a major vendor mapping *task characteristics* to runtime pattern (non-agentic call, single agent, sequential, parallel, loop, review/critique, coordinator, hierarchical, swarm, human-in-the-loop, custom logic). Page shows "last updated 2026-05-28" (an earlier version dated 2025-10-08 exists). It is the closest vendor equivalent to the classification this track proposes, keyed to requirements (predefined vs open-ended, latency, cost, human involvement) rather than to user roles.

## Themes
- work-structure-spectrum: predictable or structured single-call work (summarise, translate, classify) needs no agent; fixed repeatable steps -> sequential pipeline with no model orchestration; ambiguous open-ended problems -> hierarchical decomposition; creative trade-offs -> swarm/debate (most costly, risk of non-convergence).
- single-agent-many-skills: start with a single agent; go multi-agent when many tools or distinct responsibilities cause latency, wrong tool choices or failures.
- human-review-gates: human-in-the-loop for "high-stakes decisions, safety-critical operations, or subjective approvals"; low-risk tasks do not need it.

## Key points
- Review and critique (generator + critic) for outputs that must meet strict accuracy/format/safety standards (e.g. code security review), at the cost of an extra model call.
- Each added model call raises latency and cost; custom orchestration is more error-prone than a predefined pattern.

## Could not verify
- No evidence base is cited for the pattern recommendations; they are design guidance.
