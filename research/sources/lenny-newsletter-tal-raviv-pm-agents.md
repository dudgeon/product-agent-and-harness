---
title: "Make product management fun again with AI agents (Lenny's Newsletter)"
source_url: https://www.lennysnewsletter.com/p/make-product-management-fun-again
author: Tal Raviv (in Lenny's Newsletter)
publisher: Lenny's Newsletter
published: 2025-04-29
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-pm-agents-jobs-to-be-done
themes: [status-update-agents, human-review-gates, human-judgment-pm-jobs, evals-autonomy-trust, org-context-grounding, research-synthesis-agents, agent-failure-modes]
relevance: medium
---

## Relevance to the project
Guide to agents for PM updates, meetings and info sync: pick a low-risk high-impact task first and apply a five-question safety checklist. Paywalled, so no outcomes were visible.

Extended 2026-10-24 by research-lennys-newsletter-archive (full text read via Geoff's paid session; relevance raised to medium): a widely read early-2025 framework for PM agents built on no-code "AI automation" platforms (Zapier Agents, Lindy, Relay, Gumloop, Cassidy). Useful to the project for its six-behaviour definition of "agentic", the junior-intern test for what to delegate, concrete low-downside patterns (draft, recommend, append, DM me), the observation that companies grant write access more readily than read access, which blocks agents from checking their own work, and the "AI isn't endangering your job, but letting AI read for you is" warning. Bears on review-and-autonomy, work-structure and human-judgment boundaries. The tooling is dated (pre-MCP-everywhere, pre-coding-harness for PMs).

## Themes
- status-update-agents: agents for updates, meetings and information sync.
- human-review-gates: five-question safety checklist; start with a low-risk task.
- human-review-gates (extended): low-downside swaps: DM me instead of pinging a channel; create a draft instead of sending; recommend instead of deciding; append suggestions instead of modifying a document (section "Can I keep the downside low?"). Hard platform permissions "physically limit the AI system's behavior".
- evals-autonomy-trust: "Trust is gained in drops": widen scope (send without approval, add a data source) only after several good cycles (section "Releasing your agent into the wild").
- human-judgment-pm-jobs: "AI isn't endangering your job, but letting AI read for you is"; use AI to traverse and cluster but insist on exact quotes and links to the raw tickets and calls (checklist item 5, "Danger zone").
- research-synthesis-agents: Gumloop analyses each helpbot chat for root cause ("What is this person struggling with?") and reports with links back to the raw conversation, rather than summarising (item 5).
- org-context-grounding: the agent needs where data lives, your decision guidance and who is on which team, not the three-year vision (item 4).
- agent-failure-modes: an agent hallucinated sprint numbers because examples said "Sprint 5" while the board had no sprints, and marked tasks done because the board had end dates but no status field: context gaps, not model failures (section "Be forgiving and compassionate").

## Key points
- Paywalled guide; Lenny predicted a top-five post (editor's note: it became one).
- Extended 2026-10-24 by research-lennys-newsletter-archive:
- Method: interviews with agent-platform founders, usability sessions with PMs building first agents, and a workshop of 5,000+ PMs (introduction).
- Agent as a spectrum of six behaviours: acts proactively, makes a plan, leverages context, draws on live data, takes real-world action, creates its own feedback loop. "Takes real-world action" varies most, because of integrations and the trust a company already places in the tool (section "What is an AI agent?").
- Delegation test: "if my company assigned me a junior intern, what would I have them do?"; prefer continuous trigger-driven tasks over one-off batch tasks, which suit a chat LLM or MCP instead.
- Don't vibe-code your own agent app: registering apps with each SaaS service, IT permission and security review make it "tempting, but not recommended"; use a platform the company already trusts ("The best AI agent platform is the one that your company already uses and trusts").
- Permissions paradox: companies grant "write access" (create a Salesforce contact, post to Slack) more readily than read access, so agents cannot observe their own results; "build" is stronger than "test" and "learn" in the loop (section "Closing the feedback loop without a human").
- Prediction (April 2025): copilots, AI prototyping and agents will blend into tools with company context, real-world I/O and conversation.
- Cost advice (Relay.app founder): get it working with a good model and lots of data, then optimise only high-frequency runs by cheaper model or less data. Security framing: compare AI risk to existing third-party automations and human permissions; "Consult your local CISO."

## Could not verify
- Partly paywalled. (Resolved 2026-10-24: full text read via Geoff's paid session; screenshots and the platform comparison chart not visible in the text copy.)
- Platform-founder quotes are vendor claims; the usability-session anecdotes have no counts or outcomes.
- Audit 2026-10-24 (research-pm-agents-jobs-to-be-done): visible part read: first exercise is a Zapier call-prep agent that only DMs you in Slack; checklist confirmed (understand the task, start smaller, keep downside low, give enough context, stay close to raw customer signals).
