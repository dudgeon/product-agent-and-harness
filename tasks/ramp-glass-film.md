---
title: Explainer film: the Ramp Glass teardown
status: active
directed_by: director-project-agent-and-harness
done_when: A short standalone explainer (about 4-6 min) of the Ramp Glass teardown, made with the explainers pattern (projects/06-ramp-glass-teardown), rendered for Geoff to review, with every number from the audited files and Ramp's claims labelled as first-party
---

## Request

Geoff asked the Glass teardown worker (in its own session, relayed by it to the director): an explainer video of the Ramp Glass findings "when you next have a chance (and the gpu is free)", timing coordinated with the director.

Related: [[competitive-teardown-ramp-glass]], [[pm-agents-evidence-film]], [[strategy-story-and-explainer-video]]. GPU order: film 04, then 05, then this one.

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness; worker is the Glass teardown session (local_dabad5f3…).
- 2026-10-24 Worker: Script Doc v0.1 written (explainers/projects/06-ramp-glass-teardown/script-doc.md, ~760 words, 6 scenes, claim check in Appendix A); film films/ramp-glass with shots.mjs and scene code src/scenes/glass/Glass.tsx (scene kind glass, registered; 'glass' added to page-travel in pipeline/plan.mjs); --check passes, typecheck clean. No GPU work yet; waiting on Geoff's script review, then the GPU queue (04, 05 first).
- 2026-10-24 Worker: Geoff waived script review (films first, then he edits the Script Doc); frame switched to 16:9 plate look to match film 04 (Geoff left it to the director). Full build queued under the shared GPU lock as glass-film, behind 05 and 04's current voice jobs.
- 2026-10-24 Worker: film rendered (video/out/ramp-glass/ramp-glass.mp4, 4:59, with score) and sent to Geoff. Fixes on the way: two lines reworded for the speech check (S2-3, S3-2), five event cues moved off spoken numbers. Score checked (LISTEN.md, score-qa.png, silencedetect): near-silences at 0:00-0:00.4 (fade-in) and 1:02.9-1:03.4, the latter from a silent stretch in the shared cached bed (seed 12, 61.6-63.2 s), reported to the director. Rough: overlapping labels in S1 and S3.
- 2026-10-24 Worker: re-rendered with the director's 1140 s bed and both label fixes (S1 99%, S3 harness labels); silencedetect -50 dB: fade-in 0.4 s, dips 0.44-0.65 s (2:37, 3:29.6+3:30.1 back to back, 3:35.5); new copy sent to Geoff.
- 2026-10-24 Director: film 06 re-rendered (4:59) on the clean bed with label fixes; passes; sent to Geoff.
