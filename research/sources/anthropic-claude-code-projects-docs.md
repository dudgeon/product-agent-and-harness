---
title: "Let Claude coordinate ongoing work with Projects (Claude Code docs)"
source_url: https://code.claude.com/docs/en/claude-projects
author: Anthropic
publisher: Claude Code docs (code.claude.com)
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [shared-persistent-sessions, memory-architecture, identity-delegation, through-line-context-budget, delegation-return-contract]
relevance: high
---

## Relevance to the project
Projects are Anthropic's product answer to a through line that lasts days or weeks: one coordinator conversation that starts parallel cloud threads, shares project memory and instructions, and "keeps going for as long as the project runs" because it works from recent messages, recent threads and memory, not full history. The docs page adds what the launch article ([projects redesigned](claude-code-projects-redesigned.md)) did not: the coordinator sees only what threads report back; a project is single-user with no sharing and no organisation controls; threads use the person's own GitHub access and claude.ai connectors; and it is not on Team or Enterprise plans. That bounds model B for a regulated organisation today.

## Themes
- through-line-context-budget: "You don't manage context windows in a project. Threads compact automatically, and the conversation works from recent messages, recent threads, and project memory rather than its full history ... Put anything that must never be dropped in project memory."
- delegation-return-contract: the coordinator "sees what threads report back, not every step they take"; each thread "reports back to the conversation when it finishes" and opens a PR when the work calls for one; the person can open any thread's transcript in Overview.
- memory-architecture: project memory is files (MEMORY.md index plus files) that every cloud thread reads at start; project instructions up to 16,000 characters sent to every new thread; Claude saves preferences to memory itself, and they are "instructions Claude keeps to, not enforced settings".
- identity-delegation: "A project is yours alone ... it uses your own GitHub access and connectors"; threads run in auto mode; an approval prompt lives inside the thread and "Telling Claude in the project conversation to go ahead doesn't reach it."
- shared-persistent-sessions: cloud threads keep running when the laptop is closed; "Limitations: A project belongs to one user. You can't share a project or its threads with another user ... There are no organization-level controls for projects during the beta."

## Key points
- Availability: public beta on Pro, Max and Ultra; "Projects aren't offered on Team or Enterprise plans yet"; web, desktop and mobile only, not the terminal CLI or IDE extensions; not via Bedrock, Google Cloud or Foundry.
- What a cloud thread starts with: project repos and files, instructions and memory, each repo's root CLAUDE.md (not its skills, settings.json or .mcp.json), claude.ai connectors, a cloud environment.
- A thread can run on the person's own machine via Remote Control when it needs local resources; it then starts with project instructions but not memory files.
- Coordinator and thread models and effort are set separately; enforced cap of 500 new threads per day; idle projects use no plan; threads that hit plan limits wait and resume.
- Sandbox resume failure can lose uncommitted changes: "On long tasks, ask Claude to commit and push work in progress."
- Contrasted with Claude Tag (team Slack channels, admin-set connections, shared steering) for multi-person work.
- Suggested thread brief: "If you can't reach something you need ... say exactly what's missing in your first message and stop. Don't substitute, mock, or guess."

## Could not verify
- Retention of project memory and transcripts, and whether memory files can be exported; not stated on the parts read.
