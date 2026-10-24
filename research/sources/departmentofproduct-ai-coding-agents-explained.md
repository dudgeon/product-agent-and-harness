---
title: How do AI coding agents work?
source_url: https://departmentofproduct.substack.com/p/how-do-ai-coding-agents-work
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2025-06-02
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [agent-factory-sdlc, product-coherence-over-automation, human-review-gates, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
An early (June 2025) PM explainer of coding agents: assign a task from the IDE or GitHub, the agent reads, edits and runs tests in a loop, and returns a pull request for human review; plus an explanation of SWE-bench and SWE-bench Verified. It is mostly superseded by the project's first-party coding-agent sources, but it states one PM-level argument worth keeping: if agents remove engineering capacity as the constraint, the backlog stops being the limiter and the risk becomes "feature slop", so the PM's job shifts from what is feasible to what is worth shipping and discoverable. Company facts are second-hand vendor claims.

## Themes
- agent-factory-sdlc: the coding-agent loop as the author describes GitHub Copilot's agent: read_file, edit_file, run_in_terminal, repeat on test failure, then a PR; MCP brings in requirements from Jira, Linear or Notion. See [GitHub Copilot cloud agent](github-copilot-cloud-agent.md).
- product-coherence-over-automation: if a company could ship 200 features a month instead of 20, the challenge becomes discovery; cites a Spotify case where reminding users a feature existed raised its use dramatically ("The future of AI coding agents").
- human-review-gates: every agent task ends in a pull request a human engineer reviews.
- vendor-claims-vs-independent-evidence: Devin's claims (PR reviews in minutes vs about four days; Linktree about 300 PRs authored and 100 merged in a month; 300+ commits at Cal.com) are relayed without scrutiny.

## Key points
- **Typical stack:** IDE, agent/LLM (model picker), repository APIs and MCP servers, PR for human review.
- **Current remit:** framed by vendors as "work engineers don't want to do": bug fixes, test coverage, refactoring, endpoints. GitHub's billing team uses its agent for test coverage.
- **SWE-bench:** 2,294 issue/PR pairs from 12 Python repos (Princeton, 2023), judged by the repos' unit tests; SWE-bench Verified is OpenAI's human-validated 500-task subset graded by difficulty; Lite and Multimodal variants also exist. Claude 4 models reported about 72.5-72.7% on Verified at the time.
- **Backlog thesis:** engineers reporting cleared backlogs leads the author to ask whether a backlog is needed at all, and to warn about feature bloat.

## Could not verify
- The Spotify figure is given as an increase "by 20,000" with no unit or source.
- Devin, GitHub and Microsoft examples are vendor claims relayed second-hand; not checked.
- Paywalled text summarised, not reproduced.
