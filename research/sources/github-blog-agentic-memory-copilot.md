---
title: Building an agentic memory system for GitHub Copilot
source_url: https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/
author: Tiferet Gazit (GitHub)
publisher: The GitHub Blog
published: 2026-01-15
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [memory-architecture, tacit-knowledge-capture, org-learning-loop, compounding-context-repo]
relevance: high
---

## Relevance to the project

The strongest first-party evidence that write-back from finished work can be made self-correcting: Copilot agents store memories as they work, each with code citations, and verify those citations at read time instead of curating offline. It answers the staleness objection to passive capture for one domain (code), with A/B numbers. It bears on whether a context-creation agent should curate offline (the Ramp Glass 24-hour pipeline) or verify just in time.

## Themes

- **memory-architecture**: chooses "just-in-time verification" over offline curation (deduplication, conflict resolution, branch tracking, expiry), which the authors judged too costly at GitHub's scale (design section).
- **tacit-knowledge-capture**: memories are created by the agent itself via a store-memory tool (subject, fact, citations, reason) when it finds something likely to matter later; the example is "API version must match across client, server and docs" (design section).
- **org-learning-loop**: memories learned by one agent are used by others (code review to coding agent to CLI) (cross-agent section).
- **compounding-context-repo**: A/B: coding-agent PR merge rate 83% without memory to 90% with; code-review positive feedback 75% to 77%; both p < 0.00001 (results section).

## Key points

- Each memory carries citations (file paths, line numbers). Before use, the agent checks the cited code on the current branch; if contradicted it stores a corrected memory, if confirmed it re-stores to refresh the timestamp.
- Adversarial test: repositories seeded with false memories and broken citations; agents "consistently" caught and corrected them, so the pool "self-healed" (no numbers given).
- Offline code-review eval: +3% precision, +4% recall (relative vs absolute not stated).
- Scope: repository-only; created only from actions by users with write access, used only by users with read access. Retrieval is recency-only at session start; search is future work.
- Public preview, opt-in. GitHub docs (not read in full here) say memories auto-expire after 28 days.

## Notable quotes

- "Information retrieval is an asymmetrical problem: It's hard to solve, but easy to verify."
- "the agent is prompted to verify its accuracy and relevance by checking the cited code locations"

## Could not verify

- Memory-pool sizes and quantitative adversarial results are not given. Citation checks only confirm the cited lines still exist; an independent DEV Community critique argues semantic context can shift while citations survive. The method relies on code as ground truth; business and operational knowledge usually has no equivalent citable source.
