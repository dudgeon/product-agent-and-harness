---
title: "Loop engineering: Getting started with loops"
source_url: https://claude.com/resources/articles/getting-started-with-loops
author: Delba de Oliveira and Michael Segner (Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-06-30
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [agent-factory-sdlc, evals-autonomy-trust, cost-control-routing, feedback-triage-agents, human-review-gates]
relevance: high
---

## Relevance to the project
The Claude Code team defines a loop as "agents repeating cycles of work until a stop condition is met" and sorts loops by trigger, stop condition and primitive: turn-based (you hand off the check), goal-based with /goal (the stop condition), time-based with /loop and /schedule (the trigger), and proactive (the prompt itself). That taxonomy is a practical way to describe how far a PM agent's work is handed off and is the mechanism behind any "closed" opportunity-to-code loop, e.g. a scheduled routine that triages a feedback channel, fixes and reviews. It bears on loop-source, review-and-autonomy and cost dimensions. Several primitives are research preview; no outcome data.

## Themes
- agent-factory-sdlc: proactive-loop example composes /schedule, /goal, dynamic workflows and auto mode to check #project-feedback hourly, triage, fix (three parallel worktrees with an adversarial judge) and respond (section "Proactive loops").
- evals-autonomy-trust: verification encoded as a SKILL.md (example "verify-frontend-change"); /goal uses an evaluator model to send Claude back to work until a deterministic criterion is met or a turn cap is hit (sections "Turn-based", "Goal-based").
- cost-control-routing: route routines to smaller models and keep the most capable for judgment; pilot dynamic workflows on a slice; scripts for deterministic steps; match intervals to change rate; /usage, /goal and /workflows show spend (section "Managing token usage").
- feedback-triage-agents: bug reports and issue triage named as the best fit for proactive loops.
- human-review-gates: "Loops that write code need loops that check it"; use a second agent with fresh context for review (section "Maintaining code quality").

## Key points
- Turn-based: triggered by a prompt, stops when Claude judges done; improve by encoding manual checks into skills with tools that let Claude see or measure results; "The more quantitative the checks are, the easier it is for Claude to self-verify."
- Goal-based (/goal): stop on goal met or max turns; deterministic criteria (tests passed, a score threshold) work best. Example: Lighthouse score 90+, stop after 5 tries.
- Time-based: /loop re-runs a prompt on an interval on your own machine (stops if the machine is off); /schedule moves it to the cloud as a routine. Example: check a PR every 5 minutes, address comments, fix CI.
- Proactive: event or schedule trigger, no human in real time; each task exits on goal, the routine runs until turned off. Fit: recurring well-defined streams (bug reports, triage, migrations, dependency upgrades).
- Summary table: turn-based hands off the check; goal-based the stop condition; time-based the trigger; proactive the prompt.
- Quality rules: keep the codebase clean because Claude copies existing patterns; encode "what good looks like" in skills; when one output misses, encode the fix into the system, not only the instance.
- Advice to start: pick one task where you are the bottleneck and ask which piece can be handed off (the check, the goal, the trigger).
- Status: /schedule and dynamic workflows marked research preview; auto mode lets routines run without permission prompts, which is a governance choice the article does not discuss.
- Limits: engineering-centred examples; nothing on non-code verification, failure rates or cost figures.

## Notable quotes
- "On the Claude Code team, we define loops as agents repeating cycles of work until a stop condition is met."
- "When an individual result doesn't meet the standard, don't stop at fixing the individual issue, try to encode it to improve the system for all future iterations."

## Could not verify
- Linked docs pages (/loop, /schedule, /goal, dynamic workflows) were not read.
