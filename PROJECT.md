---
type: project
title: project-agent-and-harness
aliases:
  - product agent and harness
status: active
goal: Research the product agent and harness space, define concepts, and produce a strategy deck, backed by prototypes and competitive teardowns, and possibly an explainer video
health:
next: Research (first task)
created: 2026-10-24
---

# project-agent-and-harness

## Why

Subject (Geoff, 2026-10-24): "Product agent and harness". Brand new project.

## Plan (phases)

1. Research
2. Define concepts. Target output: a strategy deck
3. Prototypes to define certain dimensions
4. Competitive teardowns of existing products and features (as needed, may run alongside 1-3)
5. Possible culmination: an explainer video, which needs a defined style first

## Done when

- [ ] Strategy deck delivered

## Notes

## Decisions

- 2026-10-24 Phase order is research, then concepts (strategy deck), then prototypes; teardowns and an explainer video (with its own style definition) as needed. Only research starts now; later phases are suggested tasks. (Geoff)
- 2026-10-24 The deliverable is a strategy deck that informs a resource request to pick the right pattern, not a PRD for one implementation. So the project aggregates a menu of options split by the dimensions research surfaces, with the key questions that would decide among the options in each; it does not converge on one answer. Standing instruction for all agents; see options/README.md. Dimensions include user and product choices (users, jobs, outcomes, adoption), not only runtime/architecture. Key questions stay unranked for now. (Geoff)
- 2026-10-24 Apply the taxonomy synthesis's register consolidation (01-synthesis.md section D.0, ~29 to 20 dimensions) once the user-story-mapping worker has added its artifact-management dimension; the taxonomy worker asks Geoff its section I questions directly. (Geoff)
- 2026-10-24 Workers that did their own research also make short explainers of their findings (explainers pattern), lower priority than the main story film 04, so Geoff can keep up with each sub-task as well as the overall story. GPU order follows the shared lock, with 04 first. (Geoff)
- 2026-10-24 Films are built end to end before Geoff reviews them: no script sign-off before voicing. Geoff watches the render, then edits the Script Doc. (Geoff, for film 04; the director applies it to the explainer films 05-08 too.)
- 2026-10-24 All research goes in one shared library, `research/` (sources with links, relevance and themes; an index; a theme register), as a standing rule for current and future agents. (Geoff)

## Done

## Log

- 2026-10-24 Started.

## Director

- **Lint after every task:** when a task's worker reports it done, the director starts a lint worker (Opus 5.5) on that task, following [LINTING.md](LINTING.md). One lint pass at a time. The director files its proposed tasks as suggested, sends its follow-ups to the named workers, and brings its questions to Geoff. (Geoff, 2026-10-24)
- **Publishing:** the project is public at https://github.com/dudgeon/product-agent-and-harness. Verbatim third-party text stays out of it (`*.transcript.md` is ignored, and "## Full text" sections are stripped by a git filter). Nothing matches the local `.public-check-terms` list (untracked). Each push waits for Geoff's yes. (Geoff, 2026-10-24)
- **Director infrastructure:** keep [DIRECTOR.md](DIRECTOR.md) (workers, queue, needs-Geoff) current on every change and read it first after a restart or compaction; one line per director action in [log.md](log.md); commit locally after each step (never push without Geoff's yes); rebuild `digest.html` with `python3 scripts/digest.py` after each block of work and send it to Geoff. No git worktrees in this project. (Geoff, 2026-10-24)
- **Worker models:** every worker runs on Opus 5.5 by default (`claude-opus-5-5`), passed explicitly on every start, never inherited from the director. A worker may level up to Fable 5.1 (`claude-fable-5-1`) for cognitively complex tasks (synthesis, strategy, audits), or down to Sonnet 5.5 for pure execution. The same applies to subagents workers start. (Geoff, 2026-10-24)
- **Options by dimension (every agent, every task):** the deliverable is a strategy deck informing a resource request, so aggregate options, don't converge. Add options and key questions to `options/DIMENSIONS.md` per `options/README.md`: options split by dimension, each with evidence links, and the key questions that would decide among them. Don't pick a winner; a lean is fine if the evidence and what would change it are stated. Include this rule in every worker's brief. (Geoff, 2026-10-24)
- **Research filing (every agent, every task):** file all research in `research/` as [research/README.md](research/README.md) defines: one note per primary source in `research/sources/`, with `source_url` (a link to the original) and sections for relevance to the project and extracted themes; one line per source in `research/INDEX.md`; themes and their supporting sources in `research/THEMES.md`. Task folders hold only deliverables, which link to the source notes. Include this rule in every worker's brief. (Geoff, 2026-10-24)
