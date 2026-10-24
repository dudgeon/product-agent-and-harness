---
title: Explainer film: the intent-shaping options menu
status: active
directed_by: director-project-agent-and-harness
done_when: A short standalone explainer of the options menu for intent shaping: the five dimensions this worker added (review gating, context location, intent-shaping mode, spec standard, investment sequencing), their options and key questions, grounded in Geoff's two docs (4-6 min), as explainers/projects/08-intent-shaping-options, rendered for Geoff to review; lower priority than film 04
---

## Request

Geoff (2026-10-24): "the main story and film worker still takes precedence, but I want a number of the agents that did their own research and deliverables to ALSO maker explainers about their findings -- these are lower priority. but it will help me stay on top of the sub tasks findings, as well as the overall story"

Scope: the options menu for intent shaping: the five dimensions this worker added (review gating, context location, intent-shaping mode, spec standard, investment sequencing), their options and key questions, grounded in Geoff's two docs (4-6 min).

Related: [[research-product-agent-and-harness]], [[strategy-story-and-explainer-video]].

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness.
- 2026-10-24 Worker (research-product-agent-and-harness session) started. Script v0.1 written: explainers/projects/08-intent-shaping-options/script-doc.md (8 scenes, ~830 narrated words, ~5 min; claim check, concept map and sources appendices). Film video/films/intent-shaping-options set up (script.md via sync-table, shots.mjs/shots.json, square tokens); scenes drawn in video/src/scenes/intent/Intent.tsx (scene kind `intent`, registered in registry.ts and in plan.mjs page-travel). `build.mjs --check` passed; tsc clean. No GPU work; frames not yet rendered or viewed. Waiting on Geoff's script review and the director's GPU go.
- 2026-10-24 Director: Geoff watches films built end to end and then edits the Script Doc, so there's no script review before render; match film 04's look. Reworked to 1920 × 1080 with 04's tokens and smaller type, in the plate palette (no Helm UI): options on the left, the accent question card on the right. --check passed again; tsc clean. Not queued on the GPU lock; waiting for the director's go (order 04, 05, 06, then 07 and 08).
- 2026-10-24 Director's final rule: lightweight deliverable, no questions to Geoff; queue on the GPU lock only once story-film's full build is running or done. Background watcher started; voice-only and one full build follow.
- 2026-10-24 New rule (music under the whole film): the build will be scored (no --no-score); house score.json ducks to -20 dB under speech and -11 dB in gaps, never silent. Will check out/intent-shaping-options/LISTEN.md and score-qa.png before sending.
- 2026-10-24 story-film full build running; queued intent-film voice-only then full build on the GPU lock (behind stripe, glass, pmae).
- 2026-10-24 Director: film 04 build killed by the low-memory guard; Geoff: restart 04 next, hold the shorts. Cancelled intent-film's queued job (no processes or queue ticket left); watcher already exited. Requeue only after out/product-agent-harness/ has its film and 04's build has exited.
