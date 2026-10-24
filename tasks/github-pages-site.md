---
title: GitHub Pages site for the project
status: active
directed_by: director-project-agent-and-harness
model: claude-opus-5-5
done_when: The public repo dudgeon/product-agent-and-harness serves a GitHub Pages site whose home page introduces the project and links every HTML page the tasks built (lifecycle maps, synthesis map, review aids) and every deliverable, by section, with each section's explainer film embedded as it is rendered (films 04-09); passes scripts/public-check.sh; live at its github.io address
---

## Request

Geoff (2026-10-24): "once the readme.md work finishes, I think we need to set this repo up with a github site/pages to make it easier for readers to see the html pages you are building and the video explainers for each section"

Geoff's decision on films (2026-10-24): put the films in the repo, overriding the explainers rule that voiced audio stays out of public repos, for this project's rendered films only (never the voice model, its weights or raw voiced lines). Keep each mp4 under GitHub's 100 MB file limit (compress) or use Git LFS. Every published film has background music under the narration from start to end (Geoff: it makes fine-tuning on his voice harder); check before uploading: run ffmpeg silencedetect at -50 dB, d=0.3, over each film; no near-silence of 1 s or longer may show other than the fade-in and fade-out (sub-second dips at the ends of lines, where the music is ducked under speech, are accepted).

Related: [[project-readme]], [[pdlc-maps-per-ecosystem]], [[pdlc-cross-ecosystem-map]], [[strategy-story-and-explainer-video]] and the explainer films.

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness, waiting for the README.
- 2026-10-24 README done; worker github-pages-site (a8625ba6, https://claude.ai/code/session_01GQLNgQYd2cVF6wFA3fvz5N) started via claude --bg on Opus 5.5 with --remote-control.
- 2026-10-24 Worker: site served from main at the repo root (.nojekyll added). Home page index.html (inline styles, no scripts) with six sections linking all 13 task-built HTML pages by relative path and the main markdown deliverables on GitHub; 74 links checked, all resolve to repo files.
- 2026-10-24 Worker: films 04 v1 (55.4 MB), 05 (12.7 MB) and 07 (37.7 MB, re-encoded from 115 MB at crf 24) copied into films/ at 1080p with faststart. silencedetect -50 dB d=0.3 on source and copy: only the 0-0.5 s fade-in and sub-second dips (max 0.70 s); no near-silence of 1 s or longer. 06, 08, 09 and strategy v2 have "film coming" slots. The films were swept into the director's commit ae9cfe2 while staged.
- 2026-10-24 Worker: index.html and .nojekyll staged; scripts/public-check.sh passes; no tracked file over 95 MB. Pages not enabled yet: waiting for the director's push.
- 2026-10-24 Worker: added films 06 ramp-glass re-render (13.6 MB) and 08 intent-shaping-options (17.2 MB), 1080p remux; silencedetect: fade-in plus dips of 0.70 s or less. Film 09 held: one near-silence of 1.04 s at 2:35.2-2:36.2 (fails the 1 s test in PROJECT.md); reported to the director. Added the Airbnb, Spotify and Block maps, briefs and options contributions to the research section, the mapping's description, and "nine ecosystems" on the cross map. 75 links checked; public check ok. Strategy v2 slot in place.
- 2026-10-24 Worker: film 09 stripe-teardown added (12.1 MB, 1080p remux, 4:11) on the director's pass under the updated PROJECT.md test; its one 1.04 s near-silence at 2:35 is noted in a caption on the page. All six explainer films are now on the page; only strategy v2 has a "film coming" slot.
