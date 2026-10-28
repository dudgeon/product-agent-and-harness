---
title: "Rise of the Overnight Agents"
source_url: https://greptile.com/blog/rise-of-the-overnight-agents
author: Daksh Gupta (Greptile)
publisher: Greptile blog
published: 2026-05-05
retrieved: 2026-10-26
type: article
evidence: vendor-claim
filed_by: research-shared-persistent-agents
themes: [verification-capacity-gap, human-review-gates, vendor-claims-vs-independent-evidence, agent-failure-modes]
relevance: high
---
## Relevance to the project
A large dataset on what unattended agents actually ship (catalogue item 4): across several million PRs in 65,000 organisations reviewed by Greptile, merged PRs with evidence of full AI authorship rose from 0.86% (Feb 2025) to 27.6% (April 2026), and reverts per 1,000 merged PRs were below the human baseline for Codex (1.19) and Claude (1.80) but above it for Cursor background agents (3.41) and Devin (3.50) versus human 2.72. The author's summary: "The bugs don't disappear, they just move." Vendor data from a code-review company, with heuristic attribution.

## Themes
- verification-capacity-gap: autonomous-agent share of merged PRs 0.86% (Feb 2025), 16.02% (Jan 2026), 24.07% (Mar 2026), 27.6% (Apr 2026) (headline chart; vendor data)
- agent-failure-modes: failure categories move by agent: Cursor BG n+1 queries 3.45x human per LOC, Claude IDOR/missing tenant check 1.75x, stale docs 1.69x; Codex/Devin env/config 1.35x (keyword analysis)
- human-review-gates: mean review cycles to merge similar across agents and humans (2.11 to 2.46; medians all 1); "Whatever review process you've built for human PRs probably wasn't built for those" (review section)
- vendor-claims-vs-independent-evidence: attribution relies on bot authors, Co-Authored-By footers and branch prefixes; human PRs may be AI-assisted; adverse selection possible (caveats)

## Key points
- Same developers' AI PRs are about 20% larger by median LOC (171 vs 143).
- AI worse on 1-file PRs (+12% reverts), better on 4-10 files (-17%) and 10+ (-28%).
- Seven-day file churn: Codex 5.7%, Claude 8.1%, Cursor BG 8.8%, human 10.0%, Devin 13.5%.
- No time-of-day data: "overnight" is framing, not measured.

## Notable quotes
- "I didn't see any evidence that agent-generated PRs were any worse than human-written PRs."
- "The bugs don't disappear, they just move."

## Could not verify
- No independent check; ranking inconsistencies between churn and revert metrics (Cursor BG) noted in the post itself.
