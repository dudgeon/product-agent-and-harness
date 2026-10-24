---
title: User story mapping: harness-agnostic modular stories
status: active
directed_by: director-project-agent-and-harness
done_when: A set of harness-agnostic modular user stories (goal and need, with today's no-agent way of working and the variants in how an agent/harness could serve it) in tasks/user-story-mapping/, linked to the PM jobs map and the dimensions in options/DIMENSIONS.md, plus a worked example of deriving one harness-specific journey; the format agreed with Geoff
---

## Request

Start a new worker for user story mapping. I want to come up with a conceptual set of user stories that describe how a product manager could navigate various incarnations of product agents and harnesses, and include how the user would navigate these processes today in the absence of an agent harness. Then we could use this generic set of user journeys, and the user journeys should be harness agnostic, to describe, to create harness or implementation specific user journeys in the various harness embodiments that we propose with the various dimensions. And then those could be used to drive representative prototypes and walkthrough videos. Ask me questions if this is vague. I know that user stories generally include both the user goal and a description of how they would interact with a product's feature set to achieve the goal. So this is a bit of a departure from that. But I'm thinking of these as kind of like modular user stories, where the needs are consistent, but the approach and the feature set is highly variable.

Related: [[research-pm-agents-jobs-to-be-done]] (PM jobs map), [[research-agent-runtime-patterns-taxonomy]], [[prototypes-define-dimensions]], [[explainer-video-style]].

## Progress

- 2026-10-24 Task filed by director-project-agent-and-harness.
- 2026-10-24 Worker proposed as a card (task_e2118ca1); waiting for Geoff to start it. Then enable Remote Control.
- 2026-10-24 Worker user-story-mapping-1 (613dd94f) started in the background with Remote Control, run by hand (Duo closed); the earlier card is superseded.
- 2026-10-24 Geoff had already started the card session (local_8ebd568e...), so the duplicate background worker user-story-mapping-1 was stopped; the card session is the worker for this task.
- 2026-10-24 Worker started. Format checked with Geoff via AskUserQuestion: stories first (lean format, not over-engineered), performer-agnostic (job is the unit), stories may span days, baseline = inconsistent Claude Code use with poor artifact management; 15 stories approved (10 job + 5 cross-cutting).
- 2026-10-24 Wrote tasks/user-story-mapping/: README (format, derivation recipe), stories-jobs (S01–S10), stories-cross-cutting (S11–S15), worked-derivation-s05 (local harness+skills+repo vs deployed shared spec agent), INDEX.
- 2026-10-24 Filed 12 key questions tagged (user-story-mapping) in options/DIMENSIONS.md (10 dimensions + cross-cutting). No new dimensions. No new web research; Today sections cite the existing library, baseline marked [G]/[A].
- 2026-10-24 Director: sent Geoff's artifact-management follow-up (research, new dimension, fold into stories). Message got no confirmation of being read.
- 2026-10-24 Follow-up from director/Geoff: artifact management and project structure as a major dimension. Two research subagents started (platforms; standardization); then add dimension, fold into stories S11/S12 and others, revise recipe and S05 derivation.
- 2026-10-24 Artifact follow-up done: two research subagents filed 40 source notes (INDEX/THEMES updated; new themes artifact-standardization, docs-as-code-prd, pm-tool-connectivity, project-taxonomy, product-artifact-primitives); syntheses in tasks/user-story-mapping/research-artifacts-{platforms,standardization}.md.
- 2026-10-24 Added dimension artifact-and-project-structure (7 options, 10 key questions) to options/DIMENSIONS.md. Geoff chose +3 stories: S16 start a project, S17 find and reuse, S18 share with a multi-party team; S11–S13 rewritten, V4 variants on S02–S06/S09/S10, recipe and S05 derivation updated.
- 2026-10-24 Director: worker had run on Sonnet 5.5 (inherited); switched to Fable 5.1 and asked for a self-audit (claims vs sources, source notes, gaps, register placement); switch to Opus 5.5 after.
- 2026-10-24 Audit on Fable 5.1 (Sonnet earlier): all 18 stories re-read; 5 overstated source tags fixed, 37 stale anchors regenerated, slugs remapped to the consolidated register (parent/sub), 11 identity variants retagged, 3 ordering bugs fixed, V4 added to S01/S08; Atlassian/Ramp verification pass filed 12 notes and corrected the Teamwork Graph access claim; log in tasks/user-story-mapping/audit-2026-10-24.md.
- 2026-10-24 Director: asked for a task-anchored PDLC/SDLC agent map of this ecosystem, see [[pdlc-maps-per-ecosystem]].
- 2026-10-24 New piece: Atlassian PDLC/SDLC agent-ecosystem map (task pdlc-maps-per-ecosystem), in the Stripe map's frame; gap research subagent running.
