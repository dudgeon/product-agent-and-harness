---
title: Explainer film: the Stripe teardowns
status: active
directed_by: director-project-agent-and-harness
done_when: A lightweight explainer (about 4-6 min) of the Stripe knowledge-agent teardown (Kai, Agent Studio, Trailhead, Orbit, Minions, the whiteboard chain, the context-creation verdict), explainers/projects/09-stripe-teardown, rendered for Geoff to watch
---

## Request

Geoff (2026-10-24): "make a film for the stripe teardowns too; but please stop bugging me with questions about these; these are lightweight deliverables to make reviewing the material easier -- not polished products"

Related: [[competitive-teardown-stripe-knowledge-agents]], [[strategy-story-and-explainer-video]].

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness; worker teardown-stripe-agents.
- 2026-10-24 Script v0.1 (6 scenes, 626 voiced words, ~4.5 min) in explainers/projects/09-stripe-teardown/script-doc.md with claim check; film video/films/stripe-teardown; scenes src/scenes/stripe/Stripe.tsx; registry and page-travel entries added; build --check passes. Queued to voice behind story-film's full build (watcher running).
- 2026-10-24 New rule from the director (Geoff): score bed under the whole film, never --no-score; check out/stripe-teardown/LISTEN.md and score-qa.png before sending. Shared score config (score/score.json: speech duck -20 dB, gaps -11 dB, 2 s fade-in) already meets it; no changes needed.
- 2026-10-24 14:4x The queued voice-only job (waiting behind story-film's full build, which started 14:44) was stopped by Claude Code because the machine ran low on memory. Nothing had been voiced or rendered. Not restarted: it needs Geoff or the director to say go. Others now ahead in the queue: pmae-film, rtp-film, intent-film.
- 2026-10-24 Director: hold until film 04 is rendered and its build has exited, then requeue. Watcher set (voice-only, then stills to check the drawing, then one full build).
- 2026-10-24 Voice-only ran; 3 lines failed the speech check (a garbled tail; the slow five-word list; numerals heard as digits). Reworded those lines in script-doc.md (the 1,300 figure is now written as digits with a 'said as' entry), re-synced, remapped events; check passes. Re-queued voice for the 3 lines, then stills.
- 2026-10-24 Director: the 480 s bed had a near-silent stretch and has been set aside; film 09 will use the 1140 s bed. Before sending: silencedetect -50 dB, d=0.3 over the whole film; only the fade-in and fade-out may show, otherwise report to the director instead of sending.
- 2026-10-24 Director's final music test replaces the previous one: silencedetect -50 dB over the whole film; no near-silence of 1 s or longer except the fade-in and fade-out; sub-second dips at line ends are accepted and get noted in the note to Geoff.
- 2026-10-24 Two lines still failed on numerals (ASR digits); spoken lines now avoid numbers ('thousands of small agents', 'thousands of pull requests a month'), exact figures stay in on-screen tags; claim check notes it. Re-queued voice + stills.
- 2026-10-24 Voice done (38 lines, 215 s); timing cues moved off spoken numbers; stills reviewed (fixed an S1 overlap and an S3 label); film 4:11. Full build started.
