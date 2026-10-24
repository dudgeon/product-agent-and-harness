---
title: "Rewriting All of Spotify's Code Base, All the Time (QCon London 2026 presentation)"
source_url: https://www.infoq.com/presentations/spotify-ai-codebase-migration-agent/
author: Aleksandar Mitic and Jo Kelly-Fenton (Spotify)
publisher: InfoQ (QCon London 2026)
published: 2026-08-07
retrieved: 2026-10-24
type: video
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [evals-autonomy-trust, agent-failure-modes, risk-sloped-review, legible-org-for-agents, verification-capacity-gap, non-engineer-builders]
relevance: high
---

## Relevance to the project
The full QCon talk (given 17 March 2026, video posted on InfoQ 7 Aug 2026; 44 min, read via the page's transcript). It goes deeper than the existing InfoQ news note (`infoq-spotify-honk`): why the LLM judge was dropped, the move to a separate verification service that runs real CI before a PR exists, and the speakers' view that review is now the bottleneck. It also gives the clearest account of how Spotify sets standards (small advisory boards pick a "golden technology") so agents have less variety to handle.

## Themes
- evals-autonomy-trust: the judge caught removed tests but gave false positives (blocked a repo for not migrating a method it never used); as models improved and tests/builds proved better judges, it was dropped; speakers say judges are "not inherently bad" (judge section, mid-talk).
- agent-failure-modes: agent games the build (downgrades Java version), comments out tests; infra failures after moving from laptops to Linux VMs; "hallucinated" errors that were really missing libraries.
- risk-sloped-review: ideas for auto-merge limited to docs and easily reverted internal systems, "not fully answered"; a migration driver who is the domain expert may approve their own PRs.
- verification-capacity-gap: cites Bainbridge's "Ironies of Automation"; review is the new bottleneck; responses: review-time expectations, closing stale PRs, a proposed PR inbox.
- legible-org-for-agents: advisory boards of five or six senior engineers pick golden technologies; enforcement by monorepo, one dependency version, lint failures on non-approved tech, shared agent skills; standardisation-review flywheel.
- non-engineer-builders: non-technical users can trigger changes via Slack; an engineer does the final check (Q&A).

## Key points
- Before Honk: fleet management cut time to 70% adoption of a new framework version from almost a year to under a week; the last 30% long tail stayed hard.
- Insight: a migration is the normal dev loop (requirements, write, build, test, iterate) with an LLM writing the code.
- Verify tool fans out to Maven, Yarn and Bazel verifiers; teams can add their own deterministic checks; an LLM summarises build logs.
- Hack Week: an engineer put Honk on Slack and use jumped. An API lets teams build their own triggers (Slack, PR comments, Jira); the agent can pull context from logs, monitoring and Jira.
- New architecture: agent in a pod uses local verify for cheap checks, pushes a branch, a verification service runs real CI and summarises failures; PR opens only after CI passes.
- Scale: 1,000 merged PRs took 3 months at an earlier talk, now takes 10 days (speaker claim, Mar 2026). Java 25 migration at about 80% of fleet.
- Cost: "manageable", no figures.
- Deterministic targeting; users are shown blast radius ("this will impact this many repos") before large runs.
- Monitoring agents via conversation logs; a second agent can read logs and suggest prompt fixes.

## Could not verify
- Backstage and Fleetshift are not named in the talk. Who writes migration prompts is not stated (library owners, by inference). The QCon abstract cites 3,000+ merged PRs; the talk gives rate figures instead.
