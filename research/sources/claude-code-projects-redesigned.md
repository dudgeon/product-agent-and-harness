---
title: "Projects redesigned: from folder to conversation"
source_url: https://claude.com/resources/articles/projects-redesigned
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-09-17
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [project-taxonomy, shared-persistent-sessions, memory-architecture, product-artifact-primitives, remote-agent-invocation]
relevance: high
---

## Relevance to the project
Anthropic redefines a "project" in Claude Code from a folder of context to a goal-driven conversation: a coordinator chat that scopes, delegates to parallel threads (each a full cloud Claude Code session on its own branch), reviews and assembles, over a shared project memory and a library of files and artifacts. That is a vendor's concrete answer to the project-taxonomy and artifact-and-project-structure questions, and to session persistence (keeps working after you leave; steer from a phone). Beta, cloud-only threads, Pro/Max first; no usage or quality data.

## Themes
- project-taxonomy: a project = goal + repo or context + configured environment, connectors, plugins, instructions and model; work is "longer than one reply and has more than one part" (sections "Threads do the work", "Context builds over time").
- shared-persistent-sessions: work continues after you step away; monitor in the main project chat or dive into a thread; brief it "the way you'd brief a chief of staff".
- memory-architecture: every thread adds to and draws from a shared project memory (e.g. release moved to Friday, why the export was dropped, who to check with before touching billing); also remembers working and communication style.
- product-artifact-primitives: project library collects files you add and artifacts Claude produces.
- remote-agent-invocation: threads run in the cloud and are steerable from a phone; local threads "coming very soon".

## Key points
- Coordinator plus threads: Claude suggests first work on project start, routes requests to new or existing threads, checks in and follows through.
- Each thread is a Claude Code cloud session with its own branch and repo copy; overlaps surface as ordinary merge conflicts; threads may split work further with subagents, loops and workflows.
- Examples: goal to cut checkout p75 latency (profile endpoints, test optimisations, open PRs in parallel); retire a v1 endpoint across API, web and mobile repos, with Claude saying which PRs merge first.
- Controls given: check project-specific usage; choose model and effort level separately for coordinator and worker threads; adjust check-in frequency and update detail.
- Rollout: beta to select Pro and Max users on cloud sessions with no existing projects; Team and Enterprise and the rest of Claude (chat, Cowork) later; existing projects unchanged until upgraded.
- Cost warning stated: several full sessions at once reach usage limits faster.
- Limits: no multi-user sharing described (single owner implied); no governance or admin controls mentioned; nothing on memory inspection or editing.

## Notable quotes
- "Brief Claude in the project the way you'd brief a chief of staff and it routes work to new or pre-existing threads."

## Could not verify
- Whether project memory is inspectable or editable as files, and whether projects can be shared with teammates; the page does not say.
- The embedded "one project across a week" illustration is not in the text extract.
