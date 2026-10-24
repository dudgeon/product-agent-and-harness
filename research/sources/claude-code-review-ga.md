---
title: Code Review is now generally available
source_url: https://claude.com/resources/articles/code-review-is-now-generally-available
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-10-15
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [human-review-gates, risk-sloped-review, enterprise-admin-controls, cost-control-routing]
relevance: medium
---

## Relevance to the project
Anthropic's managed multi-agent PR review, launched as a research preview in March 2026 and generally available for Team and Enterprise from October 2026, is the packaged service behind the review stage of the AI-native SDLC playbook: parallel agents find bugs, verify them to filter false positives, rank by severity and post one summary plus inline comments, but never approve. It gives concrete numbers for the agent-review gate (16% to 54% of PRs with substantive comments internally; under 1% of findings marked incorrect; $15-25 per review) and per-repository depth tiers. It bears on review-and-autonomy and governance-control-plane. All figures are Anthropic's own.

## Themes
- human-review-gates: "It won't approve PRs — that's still a human call" (launch post, §Managing the review bottleneck).
- risk-sloped-review: admins set Quick, Standard (default) or Deep per repository so critical codebases get deeper review (GA post, What's new); review depth also scales automatically with PR size (launch post, §How it works).
- enterprise-admin-controls: admin enables in Claude Code settings, installs the GitHub App and picks repositories; developers need no configuration (both posts, Get started).
- cost-control-routing: token-billed, averaging $15-25 per review; monthly org spend caps, repo-level enablement, an analytics dashboard of PRs reviewed, acceptance rate and cost (launch post, §Cost and control).

## Key points
- **Mechanism.** On PR open, a team of agents searches for bugs in parallel, verifies candidates, ranks by severity; output is one overview comment plus inline comments. Positioned as deeper and more expensive than the open-source Claude Code GitHub Action, which remains available.
- **Internal figures (launch post).** Run on nearly every Anthropic PR; substantive review comments rose from 16% to 54% of PRs; PRs over 1,000 lines: 84% get findings, averaging 7.5 issues; under 50 lines: 31%, averaging 0.5; under 1% of findings marked incorrect by engineers. Code output per engineer up 200% in a year.
- **Anecdotes.** A one-line production change flagged as critical because it would have broken authentication; a TrueNAS ZFS encryption refactor where it found a pre-existing type mismatch wiping a key cache.
- **GA changes.** Most reviews about 3x faster (from about 20 minutes to 6-10); terser findings stating problem, trigger and fix; per-repo depth tiers. Promotional credits of at least $10,000 for eligible Enterprise orgs claimed by 15 January 2027 (expire 30 days after claiming).
- **Limits.** "Marked incorrect" under 1% measures engineer disagreement, not missed bugs (no recall figure); no customer outcome data at GA beyond "preview customers told us"; GitHub only per the setup steps; cost at volume is material and the posts give no total-cost example.

## Companion pages
- https://claude.com/resources/articles/code-review ("Code Review for Claude Code", 2026-03-09): the research-preview launch post; source of the mechanism, internal figures, cost and admin controls above.

## Notable quotes
- "It won't approve PRs — that's still a human call." (launch post)

## Could not verify
- Whether the GA speed-up changed cost per review; neither post says.
- Recall (bugs missed); not reported.
