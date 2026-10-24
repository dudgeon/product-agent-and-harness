---
title: "2× – nine months later: We did it"
source_url: https://ideas.fin.ai/p/2x-nine-months-later
author: Darragh Curran (CTO, Intercom / Fin)
publisher: Fin Ideas (Intercom Substack, ideas.fin.ai)
published: 2026-04-16
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-pm-agents-jobs-to-be-done
themes: [leadership-permission-mandate, agent-factory-sdlc, risk-sloped-review, outcome-measurement-gap, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
The CTO's own scorecard for Intercom's "2x" programme: the metric (merged PRs per R&D head, including product and design leaders), the mandate ("All technical work is becoming agent-first"), and release-row numbers (313 automatic production deployments and 2,539 CI jobs in 24 hours). It frames R&D as a "factory" whose output is merged PRs and reports idea-to-shipped time. It is the clearest statement of what Intercom optimises, and of what it does not describe: discovery, specs and PM/design workflows.

## Themes
- leadership-permission-mandate: CTO goal set in mid-2025 to double R&D productivity in 12 months; adoption targets with short deadlines (agent-driven PRs >80% within six weeks, then 95%); "All technical work is becoming agent-first. This is the top priority for R&D." (section 6).
- agent-factory-sdlc: 93.6% of PRs agent-driven; 497 PRs fully autonomous in four weeks (Claude wrote, approved and shipped); new engineers ship to production on day one.
- risk-sloped-review: AI approval started with the lowest-risk changes (feature-flag cleanups, small bug fixes); 19.2% of merged PRs auto-approved; 86% of auto-approved PRs are 20 lines or fewer; median merge 14.6 min vs 75.8 min org median.
- outcome-measurement-gap: the metric is merged PRs / all R&D headcount, which the author calls imperfect ("Wait, you measured what now?"); engineers are tiered on AI usage intensity, output, $/PR and prompt quality.
- vendor-claims-vs-independent-evidence: all figures self-reported; most charts are images; definitions of "product change", "idea" and the code-quality score not given.

## Key points
- Release row: last 24 hours 2,539 CI jobs and 313 automatic production deployments; downtime from breaking changes down 35% over 11 months while deployments doubled.
- Quality: core product defect backlog down 54% year to date; all critical/high defects closed; defect SLO of fixing reported issues in under 24 hours at 10.4% and climbing; static-analysis code quality fell as AI use grew, then had a five-week net-positive streak.
- Product throughput: product changes more than 2x; median idea-to-shipped "nearly cut in half" (heading says 39% faster). Says removing backlog management, prioritisation overhead and "issue ping pong".
- Scale: 473 people in R&D; nearly 1,100 of 1,305 employees active Claude Code users at peak; 153 contributors / 267 skills in the plugins repo; top 5% of contributors produce more than 6x the median.
- Non-engineers build analyses, reports and small tools; reports published with access controls and versioning (Snowflake + Streamlit).

## Could not verify
- How PMs and designers work, how ideas become specs, how planning is done: not described. The post promises follow-ups (2x principles, auto-approval method).
- Baseline and calculation for the 3x-over-16-months claim.
