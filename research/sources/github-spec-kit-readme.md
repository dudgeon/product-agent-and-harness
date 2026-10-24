---
title: "github/spec-kit (README)"
source_url: https://github.com/github/spec-kit
author: GitHub
publisher: github.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [agent-ready-intent, spec-becomes-prototype-and-evals, compounding-context-repo]
relevance: high
---

## Relevance to the project

The most-starred open spec-driven-development kit (about 142.7k stars per the page). It defines spec artifacts as repo files with fixed phases (constitution, specify, plan, tasks, implement, converge) plus extensions for bug-fixing and idea assessment. It is the closest existing 'artifact primitives as files in a repo' standard to compare against.

## Themes

- agent-ready-intent: a standard command set and Markdown artifacts per stage; constitution is the project-level baseline.
- compounding-context-repo: state kept under .specify/ (memory, bugs/<slug>/, assessments/<slug>/ with decision.md).

## Key points

- Workflow: /speckit-constitution (once per project), then per feature /speckit-specify, -plan, -tasks, -implement, -converge. Runs as skills in the agent's chat.
- Extensions: bug fixing (assess/fix/test; verdict verified/partial/failed) and idea assessment (intake/research/define/shape/decide; decision go/needs-clarification/kill). The assessment extension reaches upstream into PM work.
- Connects to agents through integrations; examples use GitHub Copilot. Requires Python 3.11+, uv.
- Community catalog listings are not audits; review code before running.

## Could not verify

Page showed '1.0' mention and star count but no maturity statement. Per-feature file layout is documented in spec-driven.md, not on the README as fetched; the README as fetched did not mention a specs/ directory.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.
