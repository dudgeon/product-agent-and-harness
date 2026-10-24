---
title: Redesigning source control at Anthropic
source_url: https://www.anthropic.com/engineering/redesigning-source-control
author: Anthropic source control team
publisher: Anthropic Engineering
published: 2026-10-13
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-factory-sdlc, harness-over-model, human-judgment-pm-jobs, shared-persistent-sessions]
relevance: medium
---

## Relevance to the project
Anthropic's account of what broke downstream once agents wrote most of its code: merges to the monorepo rose from about 2,500 a day in May 2026 to over 30,000 in September. Its answer was to replace git with an in-house, always-online system (Scion), a code review surface (Antique) and code search. For the project it is first-party evidence for "the bottleneck moves right of build", the same claim the AI-native SDLC playbook makes. It also gives two concrete operate-stage practices: Claude Tag "superfans" that each watch one component, and post-merge testing in place of a global merge lock. Anthropic says its workload is unusual and that Scion is not for general use.

## Themes
- agent-factory-sdlc: "coding is no longer the bottleneck ... The bottleneck, now, is all of the developer infrastructure built for human scale: source control, builds, and CI" (intro); merges up 12x in four months.
- harness-over-model: an early internal Mythos Preview rewrote the hand-built ingestion pipeline at 20x less memory and 4x the speed with no further instructions (§What we learned).
- human-judgment-pm-jobs: engineers supplied system-level understanding and design trade-offs; "very often ... the role of the engineers was to tell Claude 'no'" when agents violated core constraints (§What we learned).
- shared-persistent-sessions: Claude Tag "superfans", one Slack channel per component (daemon, cache, merge queue), with telemetry and log access, watching for anomalies (§What we learned).

## Key points
- **Scale.** About 25 million CI checkouts a day; main-branch history near 100 GB; several hundred git mirrors at peak.
- **Design principles.** Clients are always online because they are agents and jobs; the server does history, merges and rebases; every source-control query is an API, so tools such as automated bisect and revert need no local copy.
- **Team and pace.** Seven engineers built Scion, Antique and related systems and migrated in five months while daily merges grew 10x. Engineers rate Claude better than themselves at writing code.
- **Process change.** A global merge-queue lock "doesn't make much sense at agent scale", so Anthropic invested in post-merge and pre-deploy automated testing and lets Claude fix conflicting concurrent changes.
- **Security.** Directory-level permissions in the monorepo; review tooling that can express semantic constraints on approvals.
- **Limits.** Anthropic's token budget for internal use is unlike any other company's; the post covers infrastructure, not product decisions.
