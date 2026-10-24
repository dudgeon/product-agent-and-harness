---
title: "Multi-agent coordination patterns: Five approaches and when to use them"
source_url: https://claude.com/resources/articles/multi-agent-coordination-patterns
author: Cara Phillips (with contributions from Eugene Yan, Jiri De Jonghe, Samuel Weller and Erik S.), Anthropic
publisher: Claude (claude.com/resources)
published: 2026-04-10
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-frameworks, task-context-isolation, agent-failure-modes, one-job-per-agent, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
Anthropic's own taxonomy of five multi-agent coordination patterns (generator-verifier, orchestrator-subagent, agent teams, message bus, shared state), with a default recommendation to start with orchestrator-subagent and evolve only where it struggles. For a product agent harness this gives a vocabulary for how PM-side agents might coordinate (e.g. a verifier for spec or synthesis quality, shared state for research synthesis) and a clear list of each pattern's failure modes. It is design guidance with illustrative examples, not measured results; no benchmarks or production data are given.

## Themes
- agent-frameworks: five named patterns with mechanics, fit and failure modes, plus a situation-to-pattern table ("Getting started").
- task-context-isolation: recommends "context-centric decomposition" (split by what context each agent needs, not by type of work); Claude Code subagents each run in their own context window and return distilled findings (Pattern 2; "Choosing and evolving").
- agent-failure-modes: rubber-stamping verifiers, orchestrator information bottleneck, conflicting teammates, silent routing failures, reactive loops in shared state (each "Where it struggles").
- one-job-per-agent: orchestrator-subagent dispatches distinct checks (security, test coverage, style, architecture) to specialised subagents in a code-review example (Pattern 2).
- evals-autonomy-trust: a verifier "is only as good as its criteria"; loops need a max-iteration limit with fallback to a human or a caveated best attempt (Pattern 1).

## Key points
- **Generator-verifier (Pattern 1):** generator drafts, verifier accepts or rejects with specific feedback, loop until accept or max iterations. Fits when quality is critical and criteria can be explicit (code plus tests, fact-checking, rubric grading, compliance verification). Fails when criteria are vague (illusion of quality control), when judging is as hard as generating, or when the loop oscillates.
- **Orchestrator-subagent (Pattern 2):** lead agent plans, delegates bounded subtasks, synthesises. Claude Code works this way. Weakness: cross-subagent findings must route through the orchestrator and get "lost or summarized away"; sequential subagents cost multi-agent tokens without speed.
- **Agent teams (Pattern 3):** persistent workers claim tasks from a shared queue and accumulate domain context across assignments (codebase migration example). Needs truly independent partitions; completion detection and shared-resource conflicts are hard.
- **Message bus (Pattern 4):** publish/subscribe with a router; suits event-driven pipelines with a growing agent set (security-ops alert triage example). Tracing is harder; a misrouted event "fails silently".
- **Shared state (Pattern 5):** agents read and write a common store with no coordinator (research synthesis across literature, industry reports, patents, news). Removes the single point of failure but risks duplicate work and reactive loops; needs first-class termination (time budget, no new findings for N cycles, or a designated judge agent).
- **Selection heuristics:** orchestrator vs teams = how long workers must hold context; orchestrator vs bus = how predictable the workflow is; teams vs shared state = whether agents need each other's findings; bus vs shared state = discrete events vs accumulating knowledge.
- **Hybrids are normal:** e.g. orchestrator for the overall flow with shared state for one collaboration-heavy subtask.
- **Default:** start with orchestrator-subagent, observe, evolve. Note that a later related article (Oct 2026, listed on the page) argues for folding subagents back into the main loop with progressive disclosure, which tempers the multi-agent framing.
- **Limits:** no production metrics, costs or case studies (promised in "upcoming posts"); examples are engineering/security-flavoured, none from product management.

## Notable quotes
- "The verifier is only as good as its criteria." (Pattern 1)
- "For most use cases, we recommend starting with orchestrator-subagent." (Getting started)

## Could not verify
- The earlier companion post ("Building multi-agent systems: when and how to use them") and the later "fold subagents into your main agent loop" article were not read.
