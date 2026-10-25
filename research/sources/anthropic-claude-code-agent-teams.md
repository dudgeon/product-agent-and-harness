---
title: Orchestrate teams of Claude Code sessions (agent teams)
source_url: https://code.claude.com/docs/en/agent-teams
author: Anthropic
publisher: Claude Code docs
published: unknown
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [shared-persistent-sessions, process-artifacts-as-coordination, human-review-gates]
relevance: high
---

## Relevance to the project
Claude Code's experimental agent teams are the clearest documented multi-agent session in a mainstream harness: a lead, teammates with their own contexts, a shared task list with dependencies, mailboxes, plan approval, and hooks that can refuse task creation or completion. It shows which process artifacts the harness makes deterministic (task states, dependency blocking, locking, hook exit codes) and which stay judgment (synthesis, plan review by the lead).

## Themes
- shared-persistent-sessions: teammates are independent Claude Code sessions that message each other directly; the human can talk to any teammate (overview).
- process-artifacts-as-coordination: shared task list with states pending, in progress, completed; dependent tasks cannot be claimed until dependencies complete; file locking prevents double-claims; task list persists in ~/.claude/tasks/{team}/ after the session (Assign and claim tasks; Architecture).
- human-review-gates: TaskCreated and TaskCompleted hooks can exit 2 to block creation or completion with feedback; TeammateIdle can keep a teammate working (Enforce quality gates with hooks).

## Key points
- Disabled by default (CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1); interactive sessions only.
- Plan approval: a teammate spawned while the lead is in plan mode plans read-only, then sends a plan approval request; by default Claude Code approves as soon as it arrives without the lead reviewing; if the human puts a running teammate into plan mode, the lead reviews instead. So plan review is not a human gate by default.
- Permission prompts from teammates surface in the lead session; a teammate cannot approve on the user's behalf, and in auto mode relayed approval claims are treated as untrusted.
- Guidance: 3-5 teammates; 5-6 tasks per teammate; avoid two teammates editing one file; start with research and review; competing-hypotheses debate as an anti-anchoring pattern.
- Limitations stated: no resumption of in-process teammates; task status can lag and block dependants; lead may declare done early; one team per session; no nested teams; lead is fixed.
- My judgment: the task list is a deterministic process artifact (states, dependencies) but its truth depends on agents updating it; the docs admit "task status can lag", the agent analogue of a checklist marked complete inaccurately.

## Could not verify
- Docs change frequently; version-specific details (v2.1.x) are as of retrieval.
