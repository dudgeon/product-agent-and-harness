---
title: "Stores: Plan in Its Own Repo (OpenSpec stores beta user guide)"
source_url: https://github.com/Fission-AI/OpenSpec/blob/main/docs/stores-beta/user-guide.md
author: Fission AI
publisher: github.com
published: unknown
retrieved: 2026-11-01
type: docs
evidence: first-party
filed_by: research-sdd-ready-intent
themes: [sdd-input-contracts, docs-as-code-prd, handoff-context-transfer, legible-org-for-agents]
relevance: high
---

## Relevance to the project
The one spec-driven toolchain found that designs for planning outside the code repo: a "store" is a planning-only Git repo with the usual specs and changes, and code repos declare it as a read-only reference. It is a shipped answer to the project's tension between a shared intent repository and specs beside the code: the shared requirements stay in their owner's repo, each code repo opens its own small change that cites them, and an agent in the code repo gets an index of the upstream specs with the exact command to fetch each. It also names the problem in the project's terms: "Requirements are owned by one team and consumed by others. The wiki version drifts, and your coding agent can't read it anyway."

## Themes
- sdd-input-contracts: a code repo's `openspec/config.yaml` declares `references: [platform-reqs]`; its instructions then include "an index of the referenced store's specs — each with a one-line summary and the exact fetch command" (Story: requirements that cross team lines).
- docs-as-code-prd: a store is `.openspec-store/store.yaml` plus `openspec/specs/` ("what is true") and `openspec/changes/` ("what is in motion"); "A store is just a git repo" (The shape).
- handoff-context-transfer: implementation starts with "a small local change for the component's part" that "cites that shared contract"; if the shared change is still open, fetch it explicitly and link the branches in the pull-request descriptions (How does implementation start in each repo?).
- legible-org-for-agents: a platform team owns `platform-reqs`; product teams build against it in their own repos "without anyone pasting context around".

## Key points
- "Declarations, not machinery": references change what OpenSpec can tell the agent, never where commands act. "OpenSpec currently does not route tasks to repos."
- "No sync, ever — by design": a stale checkout shows stale specs until someone pulls.
- Worksets open the store and code repos together in one editor workspace; they are per-machine and never committed.
- Beta: names, flags, formats and JSON may change.

## Could not verify
- Raw Markdown fetched from `main` on the retrieval date; quotes verbatim. No adoption or outcome evidence; the guide says each walkthrough was run against the current build.
