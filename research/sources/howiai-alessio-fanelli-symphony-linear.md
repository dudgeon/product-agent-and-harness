---
title: "How I run autonomous coding agents from my phone with OpenAI Symphony + Linear | Alessio Fanelli (Kernel Labs)"
source_url: https://www.lennysnewsletter.com/p/how-i-run-autonomous-coding-agents
author: Claire Vo (host), Alessio Fanelli (founder, Kernel Labs; co-host, Latent Space)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-07-06
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [agent-factory-sdlc, human-review-gates, cost-control-routing, remote-agent-invocation, agent-ready-intent, compounding-context-repo, skill-standards]
relevance: medium
---

## Relevance to the project
A live demo of the "agent manager, not agent prompter" pattern: a ticket tracker (Linear) is the state machine and source of truth, an orchestrator (OpenAI's open-source Symphony) turns each ticket into a coding run with a plan, acceptance criteria and validations, and the human only writes the spec and reviews at "human review" and "rework" states. It is the coding-side mirror of what a PM meta-harness would hand off to, and shows a ticket carrying the full history (spec, work pad, rework pad) as the handoff artifact. Bears on remote-invocation-route, session-persistence-sharing, intent-shaping-and-spec (spec as entry state) and governance-control-plane (per-task token ledger). One builder's personal setup, not an enterprise.

## Themes
- agent-factory-sdlc: Linear states drive the loop: spec written in a ticket, moved to "to do", Symphony creates a work pad (plan, acceptance criteria, validations), runs, moves to "human review"; PR comments plus a move to "rework" produce a rework checklist; merge moves it to done (4:31-6:02).
- human-review-gates: review happens at the PR and on a Vercel preview; "I don't really look at the traces one by one i just kind of direct the agent" (6:02, 9:07).
- cost-control-routing: he added a per-task token ledger (Symphony has none by default); most tasks are tens of millions of tokens, one made-deployable task was 221 million (7:36, 11:26). Token use against expectation is a signal of missing tooling (12:58).
- remote-agent-invocation: agents run on a cloud VPS (32 GB RAM, coding agents pre-logged in), reachable by text, Linear or shell; local Mac minis did not scale (2:52, 4:31). A side project lets anyone send a coding task to a repo-plus-agent on a VPS (9:07).
- agent-ready-intent: Symphony's spec is "literally just a markdown file" describing primitives, what to store and how to move work forward; host Claire Vo says teams over-engineer orchestration designs when a prescriptive spec is enough (13:17).
- compounding-context-repo: keeping spec, work pad and rework pad on one ticket lets him find where a run went wrong and feed that back into AGENTS.md or the workflow file (18:18).
- skill-standards: purge CLAUDE.md/AGENTS.md and skill files every few months; models add lines rather than remove them, so stale instructions accumulate; auto-created skills often under-specify and then over-constrain the model (14:16-16:40).

## Key points
- **Kanban alone failed (2:52):** easy to kick off a task, hard to intervene over several turns, and local runtimes did not hold up. Moving the runtime to the cloud and adding channels fixed it.
- **Setup (11:26):** he used Symphony's Elixir reference implementation, edited the root workflow.md, and built his own dashboard and token ledger. "The harness ... it's pretty straightforward"; the value is in tools that let runs go longer before needing a human, e.g. Kernel Labs' Glimpse (a Playwright extension for screenshots, visual diffs and videos).
- **Throughput is limited by the human (18:18):** "you can't really like stay on top of like 100 new things a day"; the benefit is "the full state of one task in one place". "Symphony is just a way to shape the context ... it's just helping you wield it."
- **Skill file style (14:16-15:49):** state the environment, exact commands and flags, what to ask for if missing; avoid telling the model what to do step by step. One stale line ("use the worktree manager") kept triggering reinstalls.
- **Second demo (19:42-24:20):** Codex with browser access gathers PSA grading certificates and prices high-value trading cards on eBay for his card shop; Fanelli argues LLMs make businesses built on heterogeneous data newly scalable.
- Sponsor read for Jira Product Discovery (17:06) frames "multiplayer mode" (team alignment on what to build) as where AI-assisted PM work still breaks; that is an advertisement, not the guest's claim.

## Notable quotes
- "Move away from being a agent prompter to kind of be an agent manager" (2:52).
- "Symphony is just a way to shape the context, it's not giving you any new capability" (18:18).

## Could not verify
- Transcript read in full 0:00-19:11 (the orchestration part); the trading-card demo and lightning round were skimmed by search. Auto-transcription is lowercase with errors ("bps" = VPS, "zoo/zoe" = his machine's name).
- Token figures are read off his own dashboard; no cost in dollars was given. Symphony's capabilities are described by a user, not checked against its repository.
