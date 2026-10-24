---
title: Test plugins with evals (claude plugin eval)
source_url: https://code.claude.com/docs/en/plugin-evals.md
author: Anthropic
publisher: code.claude.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [evals-autonomy-trust, skills-marketplace, skill-standards]
relevance: medium
---

## Relevance to the project
First-party tooling for testing skills/plugins as versioned artefacts: cases, graders, a no-plugin baseline and CI gating. Shows that skill testing is becoming a product feature, but it is Claude Code-only (no cross-harness eval runner found), and the manifest still marks `evals` as `experimental`.

## Themes
- evals-autonomy-trust: each case runs 3 times with the plugin and 3 times without (baseline) in fresh isolated non-interactive sessions; score = fraction of graders passed; six grader types (regex, tool_use, llm judge, baseline, file etc.); "There are no custom-code graders".
- skills-marketplace: `claude plugin validate --strict` + `claude plugin eval` can gate CI on a plugin change or a new model release.

## Key points
- "Most common first finding is a delta near zero with the `tool_used: Skill` grader failing, which means Claude isn't choosing your skill on natural phrasing": i.e. triggering is the main failure mode, corroborating the Vercel and SkillsBench results.
- Every run is a real billed model call; a suite costs roughly cases x runs x 2 (with/without baseline) plus judge calls.
- Separate skill-creator plugin has its own `evals/evals.json` format; "neither tool reads the other's case files".

## Could not verify
- Only the first part of the page was inspected via the saved output.
