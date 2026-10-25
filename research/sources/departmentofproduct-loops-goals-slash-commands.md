---
title: How to use /loops, /goals and other Powerful Slash Commands as a Non-Engineer
source_url: https://departmentofproduct.substack.com/p/beyond-prompts-how-to-use-loops-goals
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-07-21
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [work-structure-spectrum, evals-autonomy-trust, human-judgment-pm-jobs, non-engineer-builders, memory-architecture, cost-control-routing]
relevance: medium
---

## Relevance to the project
A PM-audience guide to the harness features that move a non-engineer from prompting to standing goals and recurring checks: /goal, /loop, /init, /compact and /insights in Claude Code (and Codex equivalents). It is the clearest DoP statement of the "describe done, not the steps" shift and puts a boundary on it: goals suit well-defined, checkable tasks, not strategic judgment or security-sensitive work. Two ideas bear on the strategy: a recurring check is best written as a reusable command file that a short loop calls, and the harness's own usage report (/insights) can show a PM which of their repeated tasks to turn into commands. It is a tutorial with no outcome data; vendor facts are second-hand from Anthropic and OpenAI docs and talks.

## Themes
- work-structure-spectrum: three steps of structure inside one general harness: a one-off prompt, a goal with a completion condition that the agent works toward over many turns, and a loop that reruns a check on an interval (sections "/goal", "/loop"). The competitor-pricing example moves the instructions into a command file so the loop line stays short.
- evals-autonomy-trust: a good goal names the end state, how it will be verified and what must be kept unchanged (citing OpenAI's /goal guide); the churn-reasons example tells the agent to mark "cause unclear" rather than infer a reason it can't cite ("/goal" section).
- human-judgment-pm-jobs: the author says /goal is not for work that needs human judgment ("important strategic decisions") or where a mistake is costly ("/goal" section).
- non-engineer-builders: /insights is pitched as a way for non-engineers to spot candidates for automation: a task that recurs 10 to 15 times with the same shape should become a custom command ("/insights" section).
- memory-architecture: /init generates CLAUDE.md or AGENTS.md as a standing project briefing the harness reads at the start of every session ("/init" section). See [Claude Code memory docs](anthropic-claude-code-memory-docs.md).
- cost-control-routing: /compact framed as a token-cost saver for long PM sessions, with steerable focus ("/compact" section).

## Key points
- Opening: quotes OpenAI's Katia Guzman (stop prompting, state what you're doing), Boris Cherny ("my job is to write loops") and Addy Osmani ("loop engineering"). All second-hand; see the [Cherny Light Cone summary](traces-boris-cherny-light-cone-summary.md) for related Cherny claims.
- Three kinds of slash command: built-in (session mechanics), custom (markdown files that expand into a prompt) and connector-exposed (from MCP servers or plugins).
- /goal: PM examples are a roadmap doc where every item has an owner, quarter and status, and a churn audit where every reason must trace to a ticket, survey answer or usage pattern. Mentions a Codex goal that built a master backlog of every feature and fixed bugs, and a prompt that has the model write its own goals and check progress.
- /loop: interval plus prompt; with no interval the harness picks its own pacing. PM examples: weekly competitor pricing check, changelogs, release notes, weekly metrics. Advises a separate command file for the check and a one-line loop that calls it.
- /insights (with /recap and /usage for comparison): a cross-session report of strengths, friction, request mix and recommendations, including suggested CLAUDE.md edits and new skills. The author shows his own 30-day suggestions.
- /pet (Codex): a desktop companion that shows progress on long-running tasks; included as light relief, but it is a small example of glanceable status for unattended work.
- Links a downloadable guide to 100+ commands across Claude Code and Codex (not reviewed here).

## Notable quotes
- "My job is to write loops" (Boris Cherny, as quoted)

## Could not verify
- The post doesn't say whether a /loop survives closing the session; in Claude Code, /loop runs inside the open session, while cloud routines (/schedule) do not need the laptop. A weekly (7d) session loop may not be practical. Not tested.
- The OpenAI /goal guide, the Google PM's /goal guide and the Guzman, Cherny and Osmani quotes were not opened.
- Paywalled; summarised, not reproduced. Screenshots in the post were not visible in the text copy.
