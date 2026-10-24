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
