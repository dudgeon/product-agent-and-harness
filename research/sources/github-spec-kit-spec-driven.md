---
title: "Spec-Driven Development (spec-kit spec-driven.md)"
source_url: https://github.com/github/spec-kit/blob/main/spec-driven.md
author: GitHub
publisher: github.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [agent-ready-intent, spec-becomes-prototype-and-evals]
relevance: high
---

## Relevance to the project

The methodology doc behind Spec Kit: specs are the primary artifact, code is their generated expression, and the per-feature directory has a defined file set. It gives a concrete candidate list of artifact types (spec, plan, research, data-model, contracts, quickstart, tasks, constitution) that a product meta-harness could adopt or deliberately extend upstream.

## Themes

- agent-ready-intent: spec.md has user stories and acceptance criteria, ambiguity marked [NEEDS CLARIFICATION] instead of guessed; templates act as structured prompts with self-review checklists.
- spec-becomes-prototype-and-evals: contrast; here the spec stays primary and code is regenerated.

## Key points

- Each feature lives in specs/<NNN-branch-name>/ with spec.md, plan.md, research.md, data-model.md, contracts/, quickstart.md, tasks.md ([P] marks parallel tasks).
- /specify assigns the next feature number and creates the matching branch name and directory.
- Constitution (memory/constitution.md): nine articles (library-first, CLI interface, test-first, simplicity, anti-abstraction, integration-first testing); amendments need rationale and review.
- Production metrics and incidents are meant to feed back into specs.

## Could not verify

This fetch reflects the file at retrieval; the README's newer command names (/speckit-*) differ from /speckit.* here, so the docs may be partly out of date. Nothing in either page defines upstream PM artifacts such as roadmap, insight or initiative, other than the assess extension.

Retrieved via WebFetch, which returns a model-summarised view of the page, not verbatim text; wording and exact lists should be re-checked against the live page before quoting.
