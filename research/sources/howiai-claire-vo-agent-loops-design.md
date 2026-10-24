---
title: "How to design AI agent loops: schedules, goals, and subagents in Claude Code and Codex"
source_url: https://www.lennysnewsletter.com/p/how-to-design-ai-agent-loops-schedules
author: Claire Vo (host, solo episode)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-06-17
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [remote-agent-invocation, cost-control-routing, agent-ready-intent, one-job-per-agent]
relevance: low
---

## Relevance to the project
A solo How I AI episode that gives a plain taxonomy of agent loops (heartbeat, cron, hook, goal) and five components every loop needs (worktrees, skills, plugins/connectors, subagents, state tracking), with two builds: a daily aging-PR reviewer in Claude Code and a weekly skills-identification loop in Codex. It bears lightly on loop-source and harness-layering (what the vendor harnesses now provide natively for scheduled and goal-driven work) and on the "onboarding an employee" framing for agent design. Filed from show notes only: no transcript was available, so it adds a vocabulary rather than evidence.

## Themes
- remote-agent-invocation: four ways to automate a prompt: heartbeat, cron, hook, goal (show notes, 03:03); the Claude Code build "schedules itself at 10:15 a.m." and alerts the team on aging PRs (show notes intro, 11:58).
- agent-ready-intent: goal loops are "the hardest to write well" (show notes); see the companion goal episode for the six-part goal structure (howiai-claire-vo-codex-goal).
- one-job-per-agent: both builds spawn subagents inside the loop; the Codex loop spawns "goal-based subagents to validate its own output in real time" (show notes intro, 17:08, 22:57).
- cost-control-routing: "two warning signs that your loop is going to get expensive before it gets useful" and goal loops as where "most people burn tokens for nothing" (show notes, 25:28). The signs themselves are not in the notes.

## Key points
- Definition: a loop is "just an automated prompt, not a scary new paradigm" (show notes).
- Design mental model: "onboarding an employee": give the loop what you would give a new hire (09:26; details not in notes).
- Five components: worktrees, skills, plugins/connectors, subagents, state tracking (06:03).
- References Addy Osmani's "loop engineering" article and OpenAI's "Using Goals in Codex" cookbook (show notes).

## Could not verify
- No transcript file was available; worked only from the show notes and chapter list. The loop-design details, the two warning signs, and what listeners do with loops (27:31) were not read.
- Related filed notes cover the same ideas in more depth: howiai-claire-vo-codex-goal, claude-loop-engineering, departmentofproduct-loops-goals-slash-commands.
