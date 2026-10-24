---
title: Update the project README with tasks and deliverables
status: active
directed_by: director-project-agent-and-harness
model: claude-opus-5-5
done_when: README.md at the project root explains the project and lists every task (from tasks/*.md) with its status and its deliverables and artifacts, linked by relative path, plus the research library, options register and films; passes scripts/public-check.sh
---

## Request

dispatch a worker to update the readme.md for the project, including the tasks and artifacts/deliverables

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness.
- 2026-10-24 Worker project-readme started via claude --bg on Opus 5.5 with --remote-control.
- 2026-10-24 Worker: read the request, PROJECT.md, DIRECTOR.md, the old README, all 22 task notes, every task's main deliverables (heads and key sections), the film project READMEs and the explainers output folders (empty: no film rendered yet).
- 2026-10-24 Worker: rewrote README.md: purpose (strategy deck for a resource request; options by dimension, no single answer), folder layout, all tasks grouped (research, teardowns, design and story, films, later phases) with status, a one-line summary and relative links to deliverables, nine claude.ai artifacts with what each is, films 04-09 (named, not linked) with coverage and state, and the note on omitted third-party text. All relative links resolve; `git add README.md` then scripts/public-check.sh: ok. Not committed or pushed.
