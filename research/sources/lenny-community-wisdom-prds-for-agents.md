---
title: "Community Wisdom: PRDs for agents, tracking competitor messaging, whether software moats still exist, exercising startup options when you leave, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-prds-for-agents
author: Lenny's Newsletter community (digest compiled by the Community Wisdom editor)
publisher: Lenny's Newsletter
published: 2026-10-17
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [spec-becomes-prototype-and-evals, prd-agents, evals-autonomy-trust, docs-as-code-prd, agent-failure-modes, feedback-triage-agents]
relevance: medium
---

## Relevance to the project
Thread 3 ("Writing PRDs for AI agents") is a small, recent practitioner snapshot of how the spec is changing when the thing being built is an agent: keep the PRD as an alignment tool, add a first-pass eval rubric, and treat PRD, prototype, traces and evals as one loop that keeps revising itself. It also answers a versioning question the project keeps meeting: hand the agent only the current version of a living PRD and keep older versions as history, not as rival sources of truth. It bears on intent-shaping-and-spec, pm-agent-evaluation and artifact-and-project-structure. Thread 2 adds a vivid example of a PM-adjacent agent job (scheduled competitor monitoring with Claude routines). Threads 1 and 4 (stock options, software moats) are not relevant.

## Themes
- spec-becomes-prototype-and-evals: a contributor adds "a first pass at the eval rubric" to the PRD (what good looks like, which failures are already unacceptable, how we'll know it works), then expects prototype traces to reveal unanticipated failures that change the evals, the PRD and the product: "The PRD, prototype, traces, and evals are one learning loop" (thread 3). The original question cites a Calibre article recommending an eval rubric in the PRD.
- prd-agents / agent-failure-modes: another contributor spends more time on a spec for an agent than for a human, because "the agent will use any wiggle room" in an ambiguous spec (thread 3). A third frames the agent as a digital employee that needs maximum-detail requirements plus the problem and expected results.
- docs-as-code-prd: on reconciling PRD versions handed to an agent: a living document with explicit versions; "the agent should always work from the current version, with prior versions preserved as history rather than competing sources of truth" (thread 3).
- evals-autonomy-trust: the asker's team still has "humans reviewing and aligning on the outcome" while building agent-made proofs of concept early (thread 3).
- feedback-triage-agents: competitive monitoring as a scheduled agent job: a marketer runs Claude routines that screenshot competitor pages daily and flag meaningful changes; another routine scans newsletters, LinkedIn and publications (including a burner inbox subscribed to competitor mailing lists), and a morning agent posts one short Slack message linking a dated Google Doc, indexed in a master sheet (thread 2). Two earlier tools the contributor relied on (Fruitful, Yutori Scouts) had shut down, so the work moved to Claude routines.

## Key points
- Thread 3 ambiguity worth noting: the asker clarifies they mean a PRD for an agentic feature in their product, not a PRD handed to a coding agent. Contributors answer both readings, and agree the PRD is the right artifact either way, partly "so you can have AI build off the document".
- Thread 2 shows the pattern of tool churn: point solutions for monitoring disappeared within months and a general harness with schedules absorbed the job.
- Top finds: a link to Glyph Lefkowitz's essay on what a "serious AI product" would need before it could be trusted for real work (built-in mistake-checking, prominent citations, non-chat interfaces, data provenance, context visibility, real sandboxes). Not read; recorded as a pointer.

## Notable quotes
- "The PRD, prototype, traces, and evals are one learning loop, and each should keep evolving as you see what the agent actually does." (thread 3)
- "if I go in with an ambiguous specification, the agent will use any wiggle room to beef it on the task." (thread 3)

## Could not verify
- Digest read in full; only threads 2 and 3 and one top find are filed. Contributors are community members; evidence is anecdote. Names omitted, roles used.
- The Calibre article and the Lefkowitz essay were not read.
