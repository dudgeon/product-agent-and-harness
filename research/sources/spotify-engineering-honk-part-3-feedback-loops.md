---
title: "Background Coding Agents: Predictable Results Through Strong Feedback Loops (Honk, Part 3)"
source_url: https://engineering.atspotify.com/2025/12/feedback-loops-background-coding-agents-part-3
author: Max Charas and Marc Bruggmann, Spotify
publisher: Spotify Engineering blog
published: 2025-12-09
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [evals-autonomy-trust, human-review-gates, agent-failure-modes, one-job-per-agent, task-context-isolation]
relevance: high
---

## Relevance to the project
Spotify's design for trusting an unsupervised agent: hidden, automatically chosen verifiers exposed as one MCP tool, a stop hook that blocks PRs until all verifiers pass, and an LLM judge that compares the diff with the original prompt. It names the failure that matters most for trust (PR passes CI but is wrong) and gives the only judge numbers we have from a large deployment. For our harness, it is a pattern for checking agent work against the stated intent, not only against tests.

## Themes
- evals-autonomy-trust: judge vetoes about a quarter of sessions; after a veto the agent corrects course about half the time; no evals yet for the judge itself (Spotify claim, Dec 2025, section "LLM as a judge").
- agent-failure-modes: three failure modes: no PR, PR fails CI, PR passes CI but is functionally wrong (worst, "erodes trust"); causes: weak test coverage, agent going beyond the prompt, agent unable to run builds.
- human-review-gates: with Claude Code, all relevant verifiers run in the stop hook; if any fails, no PR opens.
- one-job-per-agent: the agent only sees the codebase, edits files and runs verifiers; pushing, Slack and prompt writing live in surrounding infrastructure.
- task-context-isolation: container with limited permissions, few binaries, almost no access to other systems.

## Key points
- Verifiers are hidden from the agent, switched on by repo contents (e.g. Maven if pom.xml exists), and summarise errors to keep the context window clean.
- The judge gets the diff plus the original prompt and runs last. Most common veto reason: scope creep (refactoring, disabling flaky tests).
- Next steps named: verifiers beyond Linux x86 (macOS for iOS, ARM64), acting on GitHub CI checks as an "outer loop", structured evals to compare prompts, architectures and LLM providers.
- No overall PR success rate is given.

## Notable quotes
- "Without these feedback loops, the agents often produce code that simply doesn't work."

## Could not verify
- The judge's system prompt is an image and was not read. Later sources say the judge was removed: QCon talk (`infoq-qcon-spotify-ai-codebase-migration-agent`) cites false positives and better models; the Anthropic office-hours video (`claude-customers-spotify-office-hours`) cites models and harness catching up.
