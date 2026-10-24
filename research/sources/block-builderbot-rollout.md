---
title: Block rolls out Builderbot, a new suite of AI-native tools that changes the way we ship
source_url: https://block.xyz/inside/block-rolls-out-builderbot-a-new-suite-of-ai-native-tools-that-changes-the-way-we-ship
author: Block
publisher: Block (block.xyz/inside)
published: 2026-06-17
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-block-product-practices
themes: [agent-factory-sdlc, agent-as-service-many-surfaces, shared-persistent-sessions, human-review-gates, build-vs-buy, org-context-grounding, remote-agent-invocation, opportunity-to-code-chain, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
Builderbot is Block's internal multi-agent orchestration layer, "built on goose", invoked from Slack and fed by Linear and Jira tickets, with whole-codebase context. It is Block's move from one general agent per person to a shared, team-visible agent service for implementation, and it is the clearest case at Block of a backlog item going to code with humans only steering and deciding. Builderbot is also introduced in the Q1 2026 letter ([block-q1-2026-shareholder-letter](block-q1-2026-shareholder-letter.md)).

## Themes
- agent-factory-sdlc: picks up tickets from Linear and Jira, creates the branch, writes code, opens the PR, watches CI, iterates on feedback (How it works).
- agent-as-service-many-surfaces / shared-persistent-sessions: "anyone can tag @builderbot" in Slack; multiple team members steer it in the thread in real time; "the conversation is the development environment."
- org-context-grounding: "understands the full context of Block's codebase, every service, every API, every convention"; a Cash App engineer can change a Square service they have never touched.
- human-review-gates: "Humans step in where humans add the most value"; operates on source code and system configuration only, no customer data, payments or PII.
- build-vs-buy: built because no coding tool could operate across "hundreds of millions of lines of code"; built on goose (Open foundations).

## Key points
- 200,000+ operations per day; ~1,500 merged PRs per week, about 15% of all production code changes at Block.
- Brad Axen, Head of AI Capabilities: "the missing layer between AI coding tools and how engineering actually works at scale."
- Square example: features sellers had waited months for shipped in days; "an idea can go from backlog to live ... in days instead of months" (Axen).
- "100% of Block's engineers regularly use AI in their work."

## Could not verify
- Architecture (which agents, models, how goose is embedded) is not described; secondary coverage mentions adversarial agent review, not confirmed here.

## Second reading (2026-10-24, research-block-product-practices, PM-practice pass)
A second subagent read the same source for PM practice; its notes, merged here from a duplicate note:

### Relevance to the project
Block's public description of Builderbot, its goose-based orchestration layer: anyone tags @builderbot in a Slack thread with a short description, or it picks up a Linear or Jira ticket, then researches, plans, branches, codes, opens the PR, watches CI and iterates on feedback while teammates steer in the thread. For the PM lifecycle this is the documented plan-to-code handoff at Block: the artifact is a ticket or a Slack thread, not a spec document, and the human gate is at review and push. Numbers are Block's own.

### Themes
- opportunity-to-code-chain / agent-factory-sdlc: "It picks up tickets directly from Linear and Jira, creates the branch, writes the code, opens the pull request, watches CI, and iterates based on feedback." (How it works)
- shared-persistent-sessions / remote-agent-invocation: "anyone can tag @builderbot with a short description"; "Multiple team members can collaborate with it in real time"; "the conversation is the development environment." (How it works)
- human-review-gates: "Humans step in where humans add the most value"; engineers "made the decisions that shaped the product" (How it works; Axen quote).
- vendor-claims-vs-independent-evidence: "over 200,000 operations per day", "approximately 1,500 pull requests per week, about 15% of all production code changes"; "What used to take months now takes days." (What it means)

### Key points
- Scope claim: understands every service, API and convention across "hundreds of millions of lines of code", so a Cash App engineer can change a Square service they have never touched.
- Product example (Axen): Square "took a list of features sellers had been waiting on for months and our engineers shipped them in days"; "backlog to live ... in days instead of months". This is the closest public link between a seller-request backlog and agent implementation.
- "100% of Block's engineers regularly use AI in their work."
- Operates on source code and system configuration only, not customer, payment or personal data.

### Could not verify
- Whether PMs or designers invoke Builderbot directly; the post says "anyone" but every example is an engineer. How the "list of features sellers had been waiting on" was produced (support data, research, roadmap) is not said.
- No independent confirmation of the PR counts; The New Stack's coverage did not load.
