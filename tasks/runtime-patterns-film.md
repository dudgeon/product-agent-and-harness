---
title: Explainer film: runtime patterns taxonomy
status: active
directed_by: director-project-agent-and-harness
done_when: A short standalone explainer of the 10 pattern classes, the dimensions as a menu, evidence quality, Geoff's answers and open key questions, no winner (6-8 min), as explainers/projects/07-runtime-patterns, rendered for Geoff to review; lower priority than film 04
---

## Request

Geoff (2026-10-24): "the main story and film worker still takes precedence, but I want a number of the agents that did their own research and deliverables to ALSO maker explainers about their findings -- these are lower priority. but it will help me stay on top of the sub tasks findings, as well as the overall story"

Scope: the 10 pattern classes, the dimensions as a menu, evidence quality, Geoff's answers and open key questions, no winner (6-8 min).

Related: [[research-agent-runtime-patterns-taxonomy]], [[strategy-story-and-explainer-video]].

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness.
- 2026-10-24 Script Doc v0.1 written: explainers/projects/07-runtime-patterns/script-doc.md, about 1,080 narrated words (~7 min), claim check in its appendix. Scenes (rtp) and the no-GPU --check delegated to a subagent. No voicing yet: Geoff reviews the Script Doc first, then voicing waits for the GPU lock (film 04 goes first).
- 2026-10-24 Director: Geoff won't review scripts before render; build end to end at our GPU turn (04 first), then send the film with a review note (stand-ins, Script Doc location).
- 2026-10-24 Director: match 04's plate look (16:9, 04's tokens and type, no Helm UI); passed to the scene subagent.
- 2026-10-24 Director: only small exact edits to shared pipeline files (registry.ts, plan.mjs); don't queue on the GPU lock until the director says (order 04, 05, 06, then 07/08).
- 2026-10-24 Director final rule: lightweight review film, no questions to Geoff, 16:9 in 04's plate tokens, 4-6 min. Script trimmed to v0.2 (about 660 words). GPU: queue only once story-film's full build is running or finished, then run voice-only and one full build.
- 2026-10-24 Scenes built (src/scenes/rtp/Patterns.tsx, films/runtime-patterns/), 16:9 plate tokens; --check passes (5 scenes, 50 lines). Waiting for film 04's full build before queuing on the GPU lock.
- 2026-10-24 Director: every film needs background music for its whole length (public site). Build without --no-score; ducking lowers the music but never to silence. Before sending, check out/LISTEN.md and out/score-qa.png. The shared score.json has a 2 s fade-in from t=0, ducking to speechDb, and the bed sized to the film.
- 2026-10-24 Film 04's full build was running, so I queued on the GPU lock as rtp-film (voice-only, then one full build) behind stripe-film and glass-film.
- 2026-10-24 Director: film 04's build was killed by the low-memory guard, and Geoff chose to restart 04 next and hold the shorts. Cancelled my rtp-film GPU job: no process left and no ticket in the queue. Will requeue only after out/product-agent-harness has a film and its build has exited.
- 2026-10-24 Film 04 done (director); stopped my watcher; queued rtp-film (voice-only, then one full build).
- 2026-10-24 First voice pass: 48 of 50 lines passed. 2 failed the speech check ('M C P', and 'finished' heard as 'Finnish'). Added 'm c p' to the shared voice/heard-as.json (one small edit) and reworded the A2A line to 'the agent-to-agent protocol'. Re-synced, --check passes, requeued voice plus full build.
- 2026-10-24 Re-voice passed (50 lines, 240 s of speech). The full build failed at the cue plan: the transcript writes numbers as digits, so the 'eight', 'hundred' and 'thirty' cues found no word. Moved them to 'takes', 'lines' and 'seconds'; --check now passes the plan (4:36). Requeued the full build.
- 2026-10-24 Director: the 480 s bed had a near-silent passage, so builds now use the clean 1140 s bed. Before sending, run silencedetect (-50 dB, d=0.3) over the whole film; only the fade-in and fade-out may show.
- 2026-10-24 Full build rendered (out/runtime-patterns/runtime-patterns.mp4, 4:36, 1140 s bed). silencedetect (-50 dB, d=0.3) shows the fade-in plus four mid-film dips of 0.3-0.7 s (2:32.9, 3:32.2, 3:37.1, 4:18.6): quiet bed moments ducked 20 dB under speech. Not sent; asked the director to choose a fix.
- 2026-10-24 Sent to Geoff (out/runtime-patterns/runtime-patterns.mp4, 4:36). Checked LISTEN.md, score-qa.png (music throughout) and silencedetect: four dips under 1 s at line ends, accepted by the director under the new 1 s rule. Rough spots noted: pre-revision classes, Glass-on-vendor-kit line, crowded end page.
- 2026-10-24 Director: film 07 rendered (4:36) and sent to Geoff; passes the 1 s music rule; known rough spots in its note (old class numbering, dated Glass line, crowded end page).
