---
title: "Community Wisdom: Evaluating startup equity, navigating pre-seed fundraising, MCPs vs. CLIs, Monzo's U.S. exit, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-evaluating-startup
author: Lenny's Newsletter community (Community Wisdom digest, compiled by Lenny's community team)
publisher: Lenny's Newsletter
published: 2026-04-04
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [compounding-context-repo, tacit-knowledge-capture, legible-org-for-agents, memory-architecture, shared-persistent-sessions, pm-tool-connectivity, harness-portability, identity-delegation]
relevance: medium
---

## Relevance to the project
Two threads are useful practitioner evidence. Thread 3 asks how to build an org and product "knowledge graph" for newcomers and agents in a 30-40 person company; replies converge on a pattern the project has seen elsewhere: knowledge captured as a by-product of real workflows (not a separate documentation task), a small set of canonical entities, a curated "trusted" layer separated from raw capture, and humans in the loop for important nodes. They also report that a single-person Obsidian plus Claude Code vault works but breaks down when it goes multiplayer. Thread 4 (MCPs vs CLIs) gives concrete reasons practitioners prefer CLI plus skill over MCP: token load, one auth for all agents, composability, and keeping credentials out of inference. Bears on context-and-memory, artifact-and-project-structure and capability-format-portability. Threads 1, 2 and 5 (equity, fundraising, a neobank exit) are out of scope.

## Themes
- compounding-context-repo: a member's personal setup: Obsidian vault with Claude Code as the engine; Claude wrote its own CLAUDE.md from guidance on what to capture but not how to structure; no templates; Claude cross-links with wiki links so "the graph builds itself"; skills for quick capture (routes a brain dump to the right pages), daily briefings and journaling that updates knowledge pages "as a side effect"; could be shared as a Git repo with contributions by PR (Thread 3).
- tacit-knowledge-capture: "The real unlock for me was having AI write to it as part of normal workflows, not as a separate 'documentation' task" (Thread 3). Another member logs every workflow run (input, model version, output, accepted or corrected by a human) so "what the system has learned and validated" becomes the knowledge layer.
- legible-org-for-agents: recommended approach: build "a living product/org memory for onboarding and AI agents", start from a few use cases, define a small entity set (product areas, features, projects, people, teams), require lightweight documentation going forward instead of backfilling, use AI to extract relationships with humans checking important nodes; avoid ontology-first exercises and expecting the system to infer intent when much work happens in meetings (Thread 3).
- memory-architecture / shared-persistent-sessions: a team moved from a single-person vault to a shared Obsidian vault and then "had to build something else" for multiplayer use, because you must "curate the context that is trusted and 'golden'" and keep it current; another warns that after a few weeks "no one really knows what to rely on anymore" without a trusted vs captured split (Thread 3).
- pm-tool-connectivity / harness-portability: CLIs are authed once on the machine and every agent can use them, whereas each MCP must be set up per agent; a CLI plus a skill explaining it beats MCP tool descriptions; one member avoids Cowork because it can't use local CLIs (Thread 4).
- identity-delegation: having an agent call an API directly means "the agent is having to craft API requests which include your auth credentials", passed to the inference provider; CLIs and MCP OAuth flows keep credentials out of the model's context (Thread 4).

## Key points
- Thread 4 other points: MCP tool definitions consume tokens just by being loaded; MCP tools aren't composable, wasting turns and reducing determinism; one builder replaced 30 MCP tools with a single "execute_script" tool and saw order-of-magnitude token savings; another exposes a 100+ tool surface as one CLI plus a skill; MCPs "disconnect all the time".
- Counterpoint in Thread 4: token cost is implementation-specific, not inherent to the protocol; Cowork users can build skills over APIs.
- Thread 3 caution: activity streams are signal, not the source of truth; tie them back to canonical entities.

## Notable quotes
- "The real unlock for me was having AI write to it as part of normal workflows, not as a separate 'documentation' task." (Thread 3)
- "You have to curate the context that is trusted and 'golden' and be able to separate that from the rest of the signal in the org." (Thread 3)

## Could not verify
- Full digest read; only threads 3 and 4 filed. All claims are individual members' experience, without numbers beyond the "order of magnitude" token saving, which is the member's own estimate.
