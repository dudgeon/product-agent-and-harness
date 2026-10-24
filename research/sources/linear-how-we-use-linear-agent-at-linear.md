---
title: "How we use Linear Agent at Linear"
source_url: https://linear.app/now/how-we-use-linear-agent-at-linear
author: Rhea Purohit (Linear)
publisher: linear.app/now
published: 2026-04-10
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-pm-agents-jobs-to-be-done
themes: [feedback-triage-agents, human-review-gates, vendor-claims-vs-independent-evidence, agent-factory-sdlc]
relevance: medium
---

## Relevance to the project
The most concrete account of Linear Agent and Triage Intelligence doing PM-adjacent work (feedback intake, dedupe, theming requests, PRD context), but it is the vendor describing its own internal use, so it is dogfooding, not customer evidence. It shows a realistic shape for a feedback-to-issue-to-PR loop with humans kept as assignees and approvers. Bears on case 7 (Linear) and on human gates in agent-led delivery.

## Themes
- feedback-triage-agents: CX turns Intercom emails and in-app feedback into issues; Triage Intelligence routes feature requests to product triage, flags likely duplicates, suggests labels, links Datadog/Sentry context; linked Intercom requests reopen when work ships.
- human-review-gates: humans approve PRs; delegated issues stay assigned to a person; autonomy added gradually; "still a judgment call".
- vendor-claims-vs-independent-evidence: no volumes, time saved or accuracy figures; "The agent typically gets it right" is unquantified.
- agent-factory-sdlc: a PM filed an issue for a missing filter, the agent opened a PR, an engineer reviewed it within the hour.

## Key points
- PM Sid Bhargava uses the agent to find themes across overlapping requests and regroup issues, add usage context to PRDs, draft implementation issues from specs and write PRDs.
- Engineers use it for decision history and delegate to coding agents; a coding agent reviews every PR with final human approval.
- Admits some tools used internally (Code Intelligence, custom MCP servers) are unreleased.
- Small, focused tasks work better than broad ones.

## Could not verify
- No customer evidence: Linear's customers page (https://linear.app/customers, fetched 2026-10-24) lists 18 stories (e.g. Ramp, OpenAI, Coinbase, Scale, Mercury, Cars24); none mentions Triage Intelligence, Product Intelligence, duplicate detection or Linear Agent. Scale (52% faster bug resolution, method not stated) praises plain Triage; Cars24 has no AI-triage content.

Retrieved via WebFetch (model-summarised view); quotes returned as verbatim, re-check before publication.
