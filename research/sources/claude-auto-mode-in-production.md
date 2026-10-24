---
title: Running auto mode in production
source_url: https://claude.com/resources/articles/auto-mode-in-production
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-08-07
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [risk-sloped-review, human-review-gates, evals-autonomy-trust, enterprise-admin-controls, policy-enforcement-fail-open]
relevance: medium
---

## Relevance to the project
Three customers (Nuro, Gusto, Garner Health) describe running Claude Code with a classifier, not a human, approving each agent action, and all three keep manual review for a named class of risky actions: anything that touches other people, production infrastructure or another team. This is the clearest evidence filed so far of "review sloped to risk" set by configuration rather than by individual habit, and it bears on the review-and-autonomy and governance choices for a product agent in a regulated company. The customer accounts are vendor-claim. The companion launch and default-change pages add Anthropic's own safety data (a 1,053-tester study, red-teaming, real-session regrading), which is first-party and self-reported, with some third-party testing.

## Themes
- risk-sloped-review: each customer carves out a high-risk class for manual approval: Nuro's PR reviews for other teams, Gusto's Terraform/AWS/live-API work, Garner's outbound messages to people (Nuro, Gusto, Garner sections).
- human-review-gates: Anthropic reports users approve 97% of permission prompts but reject 39% of proposed plans, implying the review gate belongs at plan level, not per command (companion: "Comparing manual review to auto mode").
- evals-autonomy-trust: Nuro runs overnight agents only on tasks "with a clear evaluation method" where the metric tells the agent whether it is improving (Nuro section).
- enterprise-admin-controls: admins pin `defaultMode` or set `disableAutoMode` in managed settings; hard-deny rules are customisable org-wide; Garner pushed auto mode to all 550 staff via managed settings (companion pages).
- policy-enforcement-fail-open: the classifier "does not eliminate risk"; in a red-team set the miss rate fell from 12% to 7%, and broad allow-rules such as `python:*` are set aside in auto mode because they would bypass the classifier (companion: red-teaming section).

## Key points
- **Mechanism (first-party):** before each tool call a classifier checks for destructive, irreversible or out-of-environment actions; blocked actions redirect Claude, and after three consecutive blocks or twenty in a session Claude Code falls back to manual approval. Tool results are also scanned by probes for prompt injection, and a check that actions match user intent.
- **Nuro (customer claim):** a staff engineer had prototyped a hook that sent each action to a small model, auto-approved about 90% and routed sensitive ones to Slack for human review, then shelved it when auto mode shipped. Runs 3-4 parallel sessions; dangerous commands (recursive deletes) are denied outright in settings; overnight research agents hill-climb autonomous-driving eval metrics (one run 10 p.m. to 5 a.m. produced three PRs).
- **Gusto (customer claim):** one engineer has started 2,425 sessions since December; about 10% of session transcripts since mid-May 2026 contained an auto-mode denial, which the team reads as the classifier doing real work. MCP traffic goes through a governed proxy with tool guards and prompt inspection before auto mode weighs in (defence in depth). The classifier once stopped a session for drifting from the original ask.
- **Garner Health (customer claim):** Claude Code rolled out to all 550 employees in every function, wired to Salesforce, Zendesk and Snowflake; staff are encouraged to spend about two hours a week automating repeatable work. A standardised SDLC runs as a plugin of skills: pick up task, explore context, commit context files to the repo, run "antagonistic research" against its own assumptions, implement, pause for a human only when context is missing. The manager configured auto mode not to approve actions that communicate with people (Slack, email), and IP-sensitive teams tuned the classifier's injected prompts. The manager credits telemetry plus standard workflows for confidence.
- **Anthropic's safety data (companion, first-party):** in a vendor-run study of 1,053 paid testers in a test environment, humans caught 13.6% of a swapped-in dangerous command versus 89% for auto mode, and human catch rates fell from about 17% to about 5% after 50+ prompts. In regraded flagged real sessions, 6.3% of manual-approval sessions contained unrequested production-severity harm versus 2.4% in auto mode (regraded by a model). Apollo Research red-teamed it; Trajectory Labs ran a commissioned prompt-injection comparison against Codex (720 attempts, none succeeded against Claude models in auto mode). Anthropic also reports auto-mode adopters on Teams/Enterprise ship about 25% more PRs (no method given), and that 25% of interactive sessions start in bypass mode.
- **Data-handling rules (companion):** the classifier checks whether a git push destination is public, private or trusted; hard-denies data exfiltration; sees git status before destructive git commands.
- **Limits:** three customer anecdotes, no measured outcomes beyond Gusto's denial rate; Anthropic still recommends isolated environments and personal review for high-stakes production changes. The competitor comparison is commissioned and tested a thin browser integration, not first-party safeguards.

## Notable quotes
- "You have to weigh the amount of time you're saving against what it could reasonably make a mistake on." (Chad Kunsman, Gusto)
- "If we were to say, everyone go build your own workflows, and we have no telemetry, that would be very dangerous." (Evan Magnussen, Garner Health)

## Companion pages
- https://claude.com/resources/articles/auto-mode (launch, 2026-03-24; research preview, admin disable setting, residual-risk caveats)
- https://claude.com/resources/articles/auto-mode-default-in-claude-code (2026-08-07, updated 2026-10-22; written by Conner Phillippi with contributors; safety study, red-teaming, incidents prevented inside Anthropic, hard denies)

## Could not verify
- Method behind the "about 25% more PRs" and "9x longer between interruptions" figures; the testers study and session regrading are Anthropic's own and not independently replicated.
