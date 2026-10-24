---
title: Strategy story and 15-minute explainer video
status: active
directed_by: director-project-agent-and-harness
done_when: (1) a strategy-shaped story (situation, complication, questions, options, one hypothetical answer) grounded in the project's research and options register; (2) a designed notional prototype: a defined user flow and a consistent visual and animation system across the walkthrough demos; (3) an explainer film made with the explainers pattern, rendered end to end at about 15 minutes, which Geoff can watch and review
---

## Request

once all of the research lands and the existing workers are dormant, I want you to spin up a story telling worker; it should synthesize all of the findings into a cohesive, "strategy-shaped" story, eg situation, complication, questions, options, with one hypothetical answer to the case, enriched by a series of walk-through demos of a notional prototype application that shows the promise of a thoughtful product manager meta harness, where sessions are persistent and shared/sharable, where common product manager jobs to be done are fully delegated to product persona sub-agents, and where the human playing a product role (whether a designer, engineer, analyst, or pm) is in a steering position, performing higher level, higher judgment tasks. then use the explainers pattern (/Users/geoff/claude-home/explainers) to turn this into a video, taking the production end-to-end, and culminating with a video I can watch and review -- target 15 minutes long. the concept walkthrough should have a defined user flow and animations that are consistent scene to scene, so the storytelling agent should design those -- and not rely on the explainer skills to illustrate them from scene to scene.

Notes for the worker (director):
- The "one hypothetical answer" is an illustration of the case, not the project's recommendation; the options menu and key questions stay the deck's substance (PROJECT.md Decisions).
- Supersedes the suggested task [[explainer-video-style]] (style is defined inside this task).
- The film lives in the explainers pattern: a new project under /Users/geoff/claude-home/explainers/projects/ and a film under its video/ folder, following explainers/CLAUDE.md (Script Doc, voice via ~/repos/geoff-voice under the GPU lock, privacy rules for voiced audio).

Related: [[research-agent-runtime-patterns-taxonomy]], [[user-story-mapping]], [[research-pm-agents-jobs-to-be-done]], [[competitive-teardown-ramp-glass]], [[research-product-agent-and-harness]], [[define-concepts-strategy-deck]].

## Progress

- 2026-10-24 Model when started: Fable 5.1 (cognitively complex: strategy story, prototype design, film), per the worker-model rule.
- 2026-10-24 Filed by director-project-agent-and-harness, waiting until research lands and workers are dormant; the director starts the worker then.
- 2026-10-24 Geoff's section I answers change the reference workload to intent shaping (not PRD review): the story should use it as its lead case.
- 2026-10-24 Worker story-and-film (0bd16627) started via claude --bg on Fable 5.1 with --remote-control (after Geoff re-trusted the folder).
- 2026-10-24 Worker read the task, PROJECT.md, DIRECTOR.md, synthesis (incl. Geoff's answers), follow-ups 1-4 and 6, the three teardowns and the Glass audit, PM brief and jobs map, the 18 stories and S05 derivation, Geoff's two documents, and the explainers house docs; now reading options/DIMENSIONS.md before drafting the story outline for Checkpoint A.
- 2026-10-24 Checkpoint A: outline written (tasks/strategy-story-and-explainer-video/00-outline.md); sent to Geoff with the two decisions (outline; shape of the hypothetical answer).
- 2026-10-24 Geoff approved the outline and Helm as the illustration, asked for a comparison against other implementations in the consideration set (skills in Claude Code etc.) and that Helm be called out as a concept, not the answer. 01-story.md written (situation, complication, questions, options in five banks, Helm with every setting named, the same job three ways, what the request funds, 85-row claim check).
- 2026-10-24 Prototype designed: 02-prototype-design.md (flow, cast, states, tokens, motion grammar, demo plan); nine procedural SVG frames (three looks × three states) in frames/; Checkpoint B page built (frames/checkpoint-b.html).
- 2026-10-24 Checkpoint B: Geoff accepted the flow, asked for mockups of the three looks to accept one, and directed the design to lean into hand-offs at the edges of a product-agent ecosystem (analyst agents in, coding agents out, shepherd and accept, analyst and risk monitoring after launch). Ecosystem added to 02-prototype-design.md (section 1b, states 0, 8, 9, Shepherd persona, demo 4) and 01-story.md (5.5). Building motion mockups per look as the film's scene code.
- 2026-10-24 Director: told the worker about Geoff's opportunity-to-code framework (being sourced by the Stripe worker) as a possible story spine.
- 2026-10-24 Stripe second pass folded in (whiteboard chain sourced; context capture as a by-product with owner verification): script S8/S11/S14, story 5.5 and 4.4, spec 1b. Script Doc draft written (explainers/projects/04-product-agent-harness/script-doc.md, about 2,660 narrated words); film folder video/films/product-agent-harness started; three look mockups rendering at full size.
- 2026-10-24 Checkpoint B answered: plate look chosen; Geoff allows 16:9 and smaller text, and wants the PM collaborating conversationally. Helm flow rewritten as a 1920x1080 conversational thread (src/scenes/helm/flow.ts); script S9-S12 and spec 3b updated; conversational plate mockup rendering; next: the Script Doc for Checkpoint C.
- 2026-10-24 Director: Geoff skipped checkpoint C; build the full film, he edits after watching.
- 2026-10-24 Geoff (via the director): skip Checkpoint C, build the film; he will edit the script after watching. Script Doc complete: https://claude.ai/artifact/BNJKVeJdDxGmiwfVNSBqVy (two-column, claim check as Appendix A). Helm scenes rewritten as a 16:9 conversational thread in the plate look (video/src/scenes/helm/flow.ts); twelve story scenes drawn (video/src/scenes/pah/Story.tsx); voicing queued under the GPU lock behind film 05; story-scene check render queued; then the full build to video/out/product-agent-harness/.
