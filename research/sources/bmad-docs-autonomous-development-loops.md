---
title: "Autonomous Development Loops (BMad Method docs)"
source_url: https://docs.bmad-method.org/build/autonomous-development-loops/
author: BMad Code
publisher: docs.bmad-method.org
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, human-review-gates, deterministic-scaffold-model-nodes, one-job-per-agent]
relevance: high
---

## Relevance to the project
The most explicit "builder contract" found for an artifact-mediated relay: the unattended builder does one named unit, writes a terminal status into the plan file's frontmatter, and never picks the next ticket or marks anything done. The next step is chosen by an orchestrator (an AI coding session, or a planned loop) reading statuses from files, with human checkpoints read from the ticket tree. It answers "who decides the next step" for model A precisely: neither the stage agent nor the artifact; a separate orchestrator or person.

## Themes
- process-artifacts-as-coordination: "a ticket's status lives in its plan"; "the plan is the contract between planning, implementation, and review"; statuses draft, ready-for-dev, in-progress, in-review, built, done, blocked, dropped.
- human-review-gates: `plan_checkpoint` and `done_checkpoint` are read by the orchestrator; "To honor `done_checkpoint`, pause after that ticket's run until a person says to continue"; "Build Auto never moves a ticket to `done`."
- deterministic-scaffold-model-nodes: the orchestrator runs `tickets.py next`, dispatches one build run per ready ticket, order set by `after` fields; reads terminal state from files "rather than inferring success from chat output alone".
- one-job-per-agent: "Build Auto builds only what its invocation names; it never picks the next ticket itself."

## Key points
- Failure: a run that cannot continue ends `blocked` with a recorded reason (e.g. unclear intent, review repair loop exceeded 5 iterations); "A blocked plan halts every later dispatch of its ticket"; an intent-gap halt saves the attempted change as a patch to resume.
- Resumption: each run is a fresh invocation; pass the same ticket ref or plan path; it resumes from the plan's status.
- Typed record: YAML frontmatter status plus a TOML ticket tree; prose plan body.

## Could not verify
- Page undated; whether `bmad-loop` has shipped; retrieved via WebFetch (model-summarised).
