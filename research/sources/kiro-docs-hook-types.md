---
title: "Hook types (Kiro docs)"
source_url: https://kiro.dev/docs/hooks/types/
author: Kiro (AWS)
publisher: kiro.dev
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [blackboard-coordination, deterministic-scaffold-model-nodes, human-review-gates]
relevance: high
---

## Relevance to the project
Kiro's hooks are the shipped example of "agents wake on file change" in a spec-driven chain, but this page sets a hard limit: "File triggers respond only to changes made by the agent." A human edit, another session, or another tool changing requirements.md does not fire a hook. So in Kiro the file is not a cross-party event bus; the next step is still chosen inside one agent session (or by the person). This matters for any design where a dependency owner's change to a shared record is meant to wake the requirements or dependency agent.

## Themes
- blackboard-coordination: triggers are File Create, File Save, File Delete, but "File triggers respond only to changes made by the agent".
- deterministic-scaffold-model-nodes: Pre/Post Task Execution hooks run around spec tasks ("Triggers after a spec task completes execution"; e.g. run tests after a task).
- human-review-gates: Prompt Submit, Agent Stop, Pre/Post Tool Use, Session Start/End, and Manual hooks (Manual listed in CLI V3 but `/hooks` cannot invoke them).

## Key points
- Trigger availability varies across IDE, CLI 2.x and CLI V3.
- Complements kiro-hooks-docs (fields, command vs agent actions) and kiro-specs-docs (requirements.md, design.md, tasks.md).
- The specs page (kiro.dev/docs/specs, fetched the same day) mentions a floating Review button per document and a Quick Spec mode "without approval gates", and runs tasks in dependency waves; it says nothing on keeping specs in sync with code or on drift.

## Could not verify
- Page undated; model-summarised fetch.
