---
title: "How Agents Manage Other Agents: Four Subagents Patterns in 2026"
source_url: https://www.philschmid.de/subagent-patterns-2026
author: Philipp Schmid
publisher: philschmid.de
published: 2026-05-05
retrieved: 2026-10-31
type: article
evidence: independent
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-failure-modes, remote-agent-invocation]
relevance: medium
---

## Relevance to the project
A practitioner taxonomy of how a main agent manages others, ordered by coordination load: inline tool (fresh context, task string in, result out), fan-out (spawn several, wait), agent pool (persistent agents that keep their history and take follow-up messages), and teams (agents message each other). In every pattern the main agent talks to the user. It names the failure that grows with each step: models lose track of which agent holds which context.

## Themes
- handoff-context-transfer: inline tool "runs in its own context with its own tools and instructions"; pool agents retain "full conversation history"; in teams "The main agent's context stays clean" and sees only what agents report.
- agent-failure-modes: inline tool has "No way to send follow-up instructions, check progress, or cancel early"; pools: smaller models "lose track of which agent has which context"; teams: wrong recipient, missed completion, loops, "failures cascade".
- remote-agent-invocation: async inline results come back as injected notifications.

## Key points
- Advice: start with the inline tool; frontier models "might handle 2-4 agents okayish" in a pool; stay with patterns 1-2 on smaller models.
- Author works in Google DeepMind developer relations; the post is a personal blog, not product documentation.

## Could not verify
- No measurements.
