---
title: "Running a Software Factory Efficiently at Uber Scale"
source_url: https://www.uber.com/us/en/blog/efficient-software-factory/
author: Uday Kiran Medisetty (Distinguished Engineer, Uber)
publisher: Uber Engineering Blog
published: 2026-08-27
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [cost-control-routing, harness-portability, agent-control-plane, org-context-grounding, legible-org-for-agents, skills-marketplace, evals-autonomy-trust, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
Uber's written companion to the AI Engineer "software factory" talk is the most detailed first-party account of how Uber governs cost, models and context under its agent harness: one wrapper over every interactive harness, a shared spend pool, Slack nudges at 50/80/100% of expected spend, Pareto model selection on an internal SWE benchmark, code-mode for MCP tools, and an AI Context Graph that grounds agents. It gives the dated adoption numbers (70%+ of PRs agent-attributed; 3,600+ skills; 30K+ skill executions/day; 7x weekly active users Feb to Aug 2026) that update the talk's figures. It does not name Cortana, Minion or DevPods, so it describes the platform under Cortana rather than the assistant itself. It bears on the harness-ownership, cost-control and grounding questions in the Cortana teardown.

## Themes
- cost-control-routing: real-time spend visibility instead of hard caps; one shared pool for all interactive harnesses; separate tiers for managed agents; manager sign-off for tier upgrades; Slack nudges at 50/80/100% of expected spend; a "cost check" skill; live cost in the terminal status line (Cost governance section).
- cost-control-routing: subagents default to a cheaper model, the primary model decomposes and evaluates; reasoning effort defaults to Medium; auto-compaction at 400K tokens even on 1M-context models; interactive cache TTL moved from 5 min to 1 h, subagents stay at 5 min (Defaults, Prompt caching).
- harness-portability: a "unified harness wrapper" handles install, config, auth and cost visibility for all interactive harnesses, serving frontier and open-weight models behind one interface (Architecture).
- evals-autonomy-trust: models chosen by Pareto efficiency (cost per completed task, quality, reliability) on an "Uber SWE Benchmark" built from thousands of real PRs, run on a model-agnostic harness; uReview benchmarked on real PRs with known bugs (Model selection).
- org-context-grounding: AI Context Graph, 24M nodes, 80M edges, 86 node types, 117 edge types, 30+ source systems; grounded run 38 s and correct vs ungrounded 20 min 09 s and wrong (Requests/turn).
- legible-org-for-agents: 1,000+ MCP servers behind one gateway; 1K+ internal tools projected as CLI commands; tool search to load tools on demand; 50-70K tokens of schema overhead per session if 100+ tools are preloaded (MCP section).
- skills-marketplace: 3,600+ skills across the SDLC, 30K+ skill executions per day; 25+ prebuilt code-mode skills for the most-used MCP servers (Introduction, Code-mode).
- vendor-claims-vs-independent-evidence: all numbers self-reported; cost per 1,000 requests down ~34% from peak (Feb to Jul, model held constant), cost per session down 52% from June peak; no independent check.

## Key points
- Framing: "AI tools are now embedded in every phase of software development"; four layers of agent usage, from specialised managed agents to general interactive harnesses; more control over cost, quality and model choice at the managed end (Introduction, Figure 3).
- Adoption (as of late Aug 2026): 70%+ of PRs attributed to local or cloud agents; weekly active users of agentic offerings up 7x and weekly agentic requests up 9.4x, Feb to Aug 2026, de-duplicated across tools; total AI spend "relatively stabilized since April".
- Code-mode: batched tool calls run as a script in a subprocess, so intermediate results stay out of context; measured token savings 55-71% on simple SQL calls and ~100% on a wide-table result; bulk workflows save over 90%.
- Third-party SaaS MCP servers are the hard part: big schemas (a workspace suite at 49 tools, ~22K tokens) and responses that persist in context (40KB examples).
- Session analysis dashboard built into the runtime analyses traces across local and cloud sandboxes and flags 16 anti-pattern categories (e.g., wrong model for the job, uncached prompts).
- Managed agents named: code review, self-healing CI, end-to-end PRs with visual validation, on-call alert triage, bug debugging, code maintenance; measured per merged PR, per review, per alert, per cleanup, with revert rate, F1 and MTTR as quality signals.
- Strategy: "moving from interactive developer workflows to fully managed agents" (Conclusion).

## Notable quotes
- "More than 70% of pull requests are attributed to local or cloud agents." (Introduction)
- "An ungrounded agent fails slowly rather than cheaply." (Requests/turn)
- "The core strategic shift is moving from interactive developer workflows to fully managed agents." (Conclusion)

## Could not verify
- Layer names for the four-layer model appear only in a figure; extraction did not capture them.
- The post does not name Cortana, Minion, DevPods or a "model gateway"; mapping them to the talk's six building blocks is inference.
- Context-graph size differs from the talk (talk: 150 node/edge types, 40M entries; post: 86 node + 117 edge types, 24M nodes / 80M edges); different counting, date, or both.
