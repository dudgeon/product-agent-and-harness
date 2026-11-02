---
title: "uReview: Scalable, Trustworthy GenAI for Code Review at Uber"
source_url: https://www.uber.com/us/en/blog/ureview/
author: Sonal Mahajan, Shauvik Roy Choudhary, Will Bond (Uber)
publisher: Uber Engineering Blog
published: 2025-08-12
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [human-review-gates, verification-capacity-gap, evals-autonomy-trust, build-vs-buy, deterministic-scaffold-model-nodes]
relevance: medium
---

## Relevance to the project
uReview is Uber's in-house AI reviewer that runs in CI on every diff, built because third-party tools assume GitHub and Uber reviews on Phabricator. It is the review stage that agent-written PRs (Minion, 70%+ of PRs by Aug 2026) pass through, and its design (chained generate, grade, filter, dedupe; per-category suppression by developer feedback) is a worked answer to the verification bottleneck. It also gives the model-pairing benchmark Uber used (Claude 4 Sonnet generator, o4-mini-high grader).

## Themes
- human-review-gates: AI comments posted inline before human review; developers rate Useful/Not Useful; humans still approve (Delivery).
- verification-capacity-gap: analyses 90%+ of ~65,000 weekly diffs; median 4 minutes per commit in CI; estimate ~1,500 reviewer hours saved per week (Impact).
- deterministic-scaffold-model-nodes: prompt chain split into generation, filtering, validation and dedupe; confidence thresholds per assistant, language and category; category classifier suppresses low-value categories (Architecture).
- evals-autonomy-trust: 75% of comments marked useful; 65%+ addressed (vs 51% of human comments by the same automated test); golden benchmark with precision/recall/F1 (Evaluation).
- build-vs-buy: third-party tools need GitHub, raise false positives and cannot reach internal systems; Uber's AI cost is "an order of magnitude lower" (Third-party tools).

## Key points
- Pluggable assistants: Standard (bugs), Best Practices (shared style-rule registry), AppSec; companion "Fixer" proposes code changes for human or AI comments.
- Deployed across six monorepos (Go, Java, Android, iOS, TypeScript, Python).
- Lessons: precision over volume; readability and minor logging comments rated poorly; correctness, error handling and best-practice comments with doc links rated well; it sees only code, so is weak on system design; CI chosen over IDE because local tools are outside Uber's control.
- Future: MCP access to past PRs, feature-flag configs and schemas.

## Notable quotes
- "Developers quickly lose confidence in a tool that generates low-quality or irrelevant suggestions."
- "Uber currently uses Phabricator™ instead of GitHub as its primary code review platform."

## Could not verify
- The post gives ~65,000 diffs per week in one place and per month in another.
