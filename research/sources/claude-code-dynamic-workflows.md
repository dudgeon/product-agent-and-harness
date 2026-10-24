---
title: Introducing dynamic workflows
source_url: https://claude.com/resources/articles/introducing-dynamic-workflows-in-claude-code
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-05-28
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [work-structure-spectrum, spec-edge-case-review, cost-control-routing, enterprise-admin-controls]
relevance: medium
---

## Relevance to the project
Dynamic workflows let Claude Code write its own orchestration script and fan a task out to tens or hundreds of parallel subagents, with other agents trying to refute findings before results are merged. For the project it is a vendor-native option between "one agent" and "a team of agents you build": the model generates the structure per task, rather than a human designing a fixed workflow. Use cases named include stress-testing a plan "from every angle before you commit", relevant to spec review. Token cost is the main stated trade-off.

## Themes
- work-structure-spectrum: structure is generated per task by the model rather than predefined; a customer quote places it "between firing off a single subagent and building out a full agent team" (intro; quotes).
- spec-edge-case-review: "a plan you want stress-tested from every angle before you commit to it"; adversarial agents try to break a result before the user sees it (intro; "Dynamic workflows in action").
- cost-control-routing: workflows "can consume substantially more tokens"; first trigger shows what will run and asks to confirm; recommended to start on a scoped task ("How it works"; intro note).
- enterprise-admin-controls: admins can disable workflows through managed settings ("How it works"; "Getting started").

## Key points
- **Mechanism:** Claude plans, breaks work into subtasks, runs subagents in parallel, checks results before folding them in, and iterates until answers converge. Coordination runs outside the conversation and progress is saved, so an interrupted run resumes.
- **Starting it:** ask for a workflow, or turn on "ultracode" (sets effort to xhigh and lets Claude decide when to use a workflow). Auto mode recommended.
- **Use cases:** codebase-wide bug, performance and security audits with independent verification of each finding; large migrations; critical work checked by independent attempts and adversarial agents.
- **Bun example (Anthropic's account):** Zig-to-Rust port, about 750,000 lines, 99.8% of tests passing, eleven days to merge; hundreds of agents with two reviewers per file and a fix loop on build and tests. Stated as not yet in production.
- Generally available in CLI, Desktop and VS Code across paid plans and on major clouds; on by default for Max, Team and Enterprise.
- **Limits:** all examples are code; no cost figures; no quality comparison against a single-agent run.
