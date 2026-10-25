---
title: About protected branches (GitHub Docs)
source_url: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
author: GitHub
publisher: GitHub Docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [human-review-gates, process-artifacts-as-coordination]
relevance: medium
---

## Relevance to the project
Branch protection is the engineering world's mature deterministic wrapper around human judgment: the platform enforces that N humans approved, that conversations are resolved and that checks passed, but never judges the content. It is the model for how a PM-artifact repo could enforce "a named owner signed off and open questions are closed" without automating the judgment itself.

## Themes
- human-review-gates: required approving reviews, optionally from code owners; dismiss stale approvals when new commits change the diff; require approval from someone other than the last pusher (body).
- process-artifacts-as-coordination: "require conversation resolution" blocks merge until all PR comments are resolved (body).

## Key points
- Required status checks must pass, be skipped or neutral; strict mode requires the branch to be up to date with base; loose mode allows post-merge breakage.
- Other rules: signed commits, linear history, merge queue (checks against latest target plus queued PRs), required deployments, lock branch.
- Admins bypass by default unless "Do not allow bypassing" is set.
- One protection rule per branch; rulesets lift this limit.
- My judgment: the "approval from someone other than the last pusher" rule is a ready-made separation-of-duties rule for agent-authored changes.
