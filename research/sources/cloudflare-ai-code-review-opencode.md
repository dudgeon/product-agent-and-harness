---
title: Orchestrating AI Code Review at scale
source_url: https://blog.cloudflare.com/ai-code-review/
author: Cloudflare
publisher: Cloudflare Blog
published: 2026-04-20
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [single-agent-many-skills, cost-control-routing, evals-autonomy-trust, harness-portability]
relevance: high
---

## Relevance to the project
A production account of a task-specific agent built on an open harness (OpenCode) and run as a CI component rather than a chat session. Counterpoint to the general-harness pattern: it shows a structured job (code review) packaged as a deployable multi-agent pipeline with per-repo AGENTS.md customisation, with real numbers.

## Themes
- [[cost-control-routing]]: average $1.19 per review (median $0.98, P99 $4.45); cost scaled by risk tier (trivial $0.20, full $1.68); model routing via a Worker + KV that can reroute in ~5s.
- [[evals-autonomy-trust]]: 'break glass' override used on 0.6% of MRs; findings ~1.2 per review.
- [[harness-portability]]: built on OpenCode with a plugin architecture; the same agents can be run locally with /fullreview in the OpenCode TUI.

## Key points
- Scale 2026-03-10 to 04-09: 131,246 review runs, 48,095 merge requests, 5,169 repos; median 3m39s.
- Design: coordinator launches up to seven specialist reviewers, dedupes, judges severity, posts one comment; depth by risk tier; teams customise via AGENTS.md.
- Lessons: naive diff-in-prompt was noisy; prompts moved to stdin; heartbeat logs because users cancelled 'hung' runs; circuit breakers and failback chains; weak at architectural context and subtle concurrency bugs.

## Added by research-agent-runtime-patterns-taxonomy (track 6, work-structure fit)
- Review as a standardised, repeatable job (first-party, Cloudflare, 2026-04-20): up to seven specialised reviewers plus a coordinator that dedupes, grades severity and filters false positives; the first naive attempt (one prompt over a diff) was noisy. "What NOT to flag" sections were central. Risk tiers (trivial / lite / full) set agent count and cost ($0.20 / $0.67 / $1.68 average). Numbers (2026-03-10 to 04-09): 131,246 runs, 48,095 MRs, 5,169 repos, median 3m39s, average $1.19. Bias toward approval; a human "break glass" override was used on 0.6% of MRs; the authors say it does not replace human review. Illustrates one-job-per-agent inside a single orchestrated system, with a risk-sloped gate.
