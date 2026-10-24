---
title: "What we're learning from engineers getting the most from Claude Code"
source_url: https://ideas.fin.ai/p/what-were-learning-from-engineers
author: Andrew Walker (Engineering Director, Fin / Intercom)
publisher: Fin Ideas (Intercom Substack, ideas.fin.ai)
published: 2026-03-25
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-pm-agents-jobs-to-be-done
themes: [compounding-context-repo, agent-led-intent-shaping, org-learning-loop]
relevance: medium
---

## Relevance to the project
The only Intercom source found on the "plan the change" row: three Principal/Staff engineers start from the problem, spend five to twenty plan-mode turns gathering context, comparing options and challenging edge cases before "build it", and keep local claude.md files updated several times a day. No formal spec, issue or design-doc template is described: the plan lives in the session. Anecdotal (informal conversation with three engineers).

## Themes
- agent-led-intent-shaping: engineers ask Claude to map how part of the codebase works and lay out options before choosing; writing a tech plan becomes "asking Claude to help think through the approach"; one uses the "superpowers" plugin to make Claude ask more clarifying questions.
- compounding-context-repo: local claude.md files capture fixes whenever Claude errs; one engineer updates his "multiple times a day"; Claude can draft them from a session.
- org-learning-loop: Brian Scanlan's "feed the flywheel" idea spreads local optimisations to everyone; documentation treated as infrastructure.

## Key points
- Prompt styles: long "war and peace" up-front prompts vs voice-dictated unstructured prompts with fast course correction (WisprFlow).
- Context handoff from planning to building stays in session memory; "build me X" without planning yields code nobody understands (anecdote of a feature shipped on time whose author could not explain it).
- Review: "close the PR and go again" when output is poor.
- A week-long understanding task now about half an hour (one engineer's estimate). The 80% plan-mode figure is about Boris Cherny, not Intercom.

## Could not verify
- Parallel agents/worktrees, testing, CI, formal design docs; results beyond three engineers.
