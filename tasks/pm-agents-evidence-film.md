---
title: Explainer film: the PM-agents evidence
status: active
directed_by: director-project-agent-and-harness
done_when: A short standalone explainer (about 4-6 min) of the PM-agents findings, made with the explainers pattern (projects/05-pm-agents-evidence), rendered for Geoff to review, with every number from the audited files
---

## Request

Geoff asked the PM-agents worker (in its own session, relayed by it to the director): make an explainer video of the PM-agents findings "when you next have a chance (and the gpu is free)", timing coordinated with the director.

Related: [[research-pm-agents-jobs-to-be-done]], [[strategy-story-and-explainer-video]] (film 04 has GPU priority).

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness; worker is the PM-agents session (local_84be37e8…).
- 2026-10-24 Worker: director's go received (separate film, house style, queue behind 04 for GPU, show Geoff the Script Doc before voicing). Script v0.1 drafted at explainers/projects/05-pm-agents-evidence/script-doc.md; starting scene build and --check (no GPU).
- 2026-10-24 Worker: film built without GPU: script synced (6 scenes, 42 lines, ~4.4 min est.), shots.mjs and scene code src/scenes/pmae/Evidence.tsx registered (registry.ts, page-travel in plan.mjs), --check passes; CPU-only preview contact sheet in projects/05-pm-agents-evidence/. Script Doc sent to Geoff for approval before voicing.
- 2026-10-24 Worker: Geoff approved the script for voicing; GPU lock free and no build running; voicing under the lock (voice-only first).
- 2026-10-24 Worker: per director, restyled to 16:9 with film 04's plate palette and type (no Helm UI); voicing (voice-only) holds the GPU lock since 13:14, ~9/42 lines done; full build will wait for 04's voice and build.
- 2026-10-24 Worker: per director's final rule (lightweight, no questions to Geoff, 16:9 plate, 04 first): voicing nearly done; a watcher queues this film's full build only once story-film's full build is running or finished.
- 2026-10-24 Worker: voice-only voiced 36/42 lines; 6 failed the speech check on British spellings and 'three in four'; script switched to US spellings and one line rephrased, re-synced, --check passes; the queued full build will voice the 6 lines.
- 2026-10-24 Worker: per director (04 restarts first, shorts held), cancelled the queued pmae-film full build and its watcher; will requeue only after film 04's film exists in out/product-agent-harness/ and its build has exited.
- 2026-10-24 Worker: film 04 rendered; watcher stopped; queued film 05's full build on the GPU lock.
- 2026-10-24 Worker: rendered (4:25, out/pm-agents-evidence/pm-agents-evidence.mp4); score checked (LISTEN.md, score-qa.png, silencedetect: audible from 0.35 s to end); sent to Geoff and reported to the director.
- 2026-10-24 Director: film 05 rendered and checked (4:25, 1080p, audio); worker confirmed music throughout and sent it to Geoff.
- 2026-10-24 Worker: rebuilding with the clean 1140 s score bed (director set aside the 480/600 s beds).
