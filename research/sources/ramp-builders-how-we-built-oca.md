---
title: How we built OCA, our AI on-call assistant
source_url: https://builders.ramp.com/post/how-we-built-oca-our-ai-on-call-assistant
author: Richard Marmorstein, Austin Ray
publisher: Ramp Builders (builders.ramp.com)
published: 2026-09-09
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-ramp-glass
themes: [agent-factory-sdlc, human-review-gates, evals-autonomy-trust, harness-portability]
relevance: high
---

## Relevance to the project

Ramp's incident agent: the "operate and learn" step of its lifecycle, with a documented handoff to Inspect for code fixes. It also shows a different harness choice from Glass: OCA runs inside Claude Code or Codex (switching with the models), orchestrated by Temporal. Useful for the PDLC map, the review/autonomy dimension, and the harness-coupling question.

## Themes

- **agent-factory-sdlc**: incident.io opens a Slack channel; OCA joins, posts an interim update at ~5 minutes and a report at ~13; when there is an obvious fix it "asks Inspect to prepare a PR for human review" (An OCA investigation).
- **human-review-gates**: read-only access broadly, narrow write; "nothing it triggers gets merged without a human"; Slack buttons for destructive actions (Autonomy).
- **evals-autonomy-trust**: responders rate each investigation Helpful / Not helpful / Didn't read, used to compare models and settings; one-shot hook "detours" force self-checks before posting (Improvement; Just-in-time instructions).
- **harness-portability**: "We use Claude Code when running Anthropic models ... and Codex when running OpenAI models"; moved to GPT-6 Astra in the past week (Building OCA).

## Key points

- Last four weeks (to Sept 2026): assisted 575 of 1,220 incident-fix PRs; incidents with OCA-assisted fixes averaged 37% fewer engineers and ~50% less estimated engineer time (estimated from Slack activity); rated helpful 90% of the time.
- Can run as a Claude Code custom subagent locally for prompt development against live transcripts.
- Experimental memory notes indexed by monitor, team, service; no rating effect, faster investigations.
- Goal: routine incidents end to end without humans.

## Could not verify

All figures self-reported and estimated from Slack activity; no control group.
