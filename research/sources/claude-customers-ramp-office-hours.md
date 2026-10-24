---
title: "Office Hours: Building for the model that doesn't exist yet (Ramp, with Boris Cherny)"
source_url: https://claude.com/customers/ramp-boris-office-hours
author: Anthropic (Boris Cherny with Rahul Sengottuvelu and Austin Ray of Ramp)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: video
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [remote-agent-invocation, harness-over-model, agent-factory-sdlc, cost-control-routing, harness-portability]
relevance: high
---

## Relevance to the project
Ramp's CTO states that more sessions on Inspect, Ramp's background coding agent, are now started by automations (schedules, external-system triggers) than by humans, which makes automation-originated work, not chat, the main entry point for a company agent. The conversation also gives Ramp's operating stance: build for the model 3-6 months out and keep removing scaffolding as models outgrow the harness, debug by studying single "correct traces" rather than benchmarks, least-privilege read-only keys set up by security, and no per-person token budgets. It adds detail to the Ramp teardown (Glass for non-technical staff, Inspect as a "digital coworker", On-call Assistant on every incident) and to the loop-versus-dynamic-workflow distinction. Anthropic-published customer conversation: all outcome claims are Ramp's or Anthropic's, unaudited.

## Themes
- remote-agent-invocation: Inspect is invoked by @-mention in Slack threads, via web, and increasingly by automations; "more Inspect sessions are coming from automations than humans" (Rahul, late in transcript).
- harness-over-model: Ramp keeps removing scaffolding "because the model has just outgrown the harness" and builds for the model 3-6 months ahead (Rahul, mid and closing answers).
- agent-factory-sdlc: Ramp says it has agents across ideation, bug finding, log alerts, coding, review and post-deploy monitoring, plus security (Rahul, "implemented agents at pretty much every part").
- cost-control-routing: no per-person token or dollar caps; instead defaults, batch/flex APIs and cheaper models for non-human-controlled automations, plus personal outreach to sudden top spenders (Rahul and Austin, cost section).
- harness-portability: Ramp tolerates "competing harnesses" internally; the platform team productizes desire paths (Rahul and Austin, decentralization answer).

## Key points
- **Automations outnumber humans as session starters** (Rahul): triggers are scheduled times or external systems; a session runs and notifies people in channels or DMs. No numbers given.
- **Loops vs dynamic workflows** (Boris): loops are repetitive "horizontal" work (babysit PRs, fix CI, rebase, delete dead code daily); dynamic workflows are Claude orchestrating many subagents when steps are unknown, framed as another level of test-time compute. Vertical example: Claude Tag shipping an experiment, monitoring exposure via a self-scheduled routine and later putting up the ship PR, with Boris only stamping the first PR.
- **Boris's CI claim**: a dynamic workflow cut Anthropic CI from about 18 min to about 6 min P50 over days of self-scheduled iterations (Anthropic's claim, no detail).
- **Ramp's internal stack**: Glass is "home base" for non-technical staff using the coding agent; Inspect runs on Modal with GitHub, Linear, Slack, Datadog, Sentry, Zendesk access; every PR gets its own VM, sessions are link-shared and multiplayer; adoption spread by people @-mentioning Inspect in others' Slack threads. A code-review bot is built on Inspect, pulling from memories and team-written skill files that codify review knowledge. On-call Assistant (built on Claude Code, proven locally then containerized with guardrails) runs on every incident assigned to engineers since about Feb/Mar.
- **Control model**: least privilege, read-only service keys (e.g. BigQuery, Datadog); security team built the network access policies and keys and are themselves users; "layers of defense" said to let them grant more agency. Targets problems where worst-case blast radius is known and constrained.
- **Evaluation**: study individual traces against the "correct trace" (what should the agent have run, was it context or tool access) rather than aggregate benchmarks; shape behaviour via prompts, tools and skills. Prompts should be declarative ("what, not how").
- **Review shifts**: reviewers stop checking classes of mistakes newer models no longer make (Austin).
- **Cost stance**: positive-ROI framing, expects cost of a given intelligence level to fall; no budgets. Contrasts with Glass launch narrative (see below).
- **Model-first, harness-light setups**: Austin runs vanilla Claude Code with few plugins/MCPs and adversarial-review subagents; Rahul is mostly background sessions for information gathering.
- Companion pages: https://claude.com/customers/ramp (older case study, no date): Anthropic-reported Ramp figures of 1M+ lines of AI-suggested code in 30 days, about 50% weekly active usage in engineering, up to 80% faster incident investigation ("early observations ... could reduce"); uses include test-loop automation via the CLI's stdin/stdout, parallel sessions, MCP to Datadog/Sentry for incidents, ticket-to-code, and natural-language Snowflake queries by product, design, data and non-technical staff.
- Limits: no metrics on automation share, Inspect volume or quality; mentions Fable and model "2.7" without detail; a conversation, not a write-up.

## Notable quotes
- "More Inspect sessions are coming from automations than humans at this point." (Rahul Sengottuvelu, CTO)
- "We don't really like to impose a certain token budget or a tool budget." (Rahul Sengottuvelu)
- "Loops are repetitive work. And dynamic workflows are dynamic work." (Boris Cherny)

## Could not verify
- Publication date (page shows none); the video itself was not watched, only the page transcript.
- Ramp's case-study figures (1M lines, 50% WAU, 80%) and how they were measured.
- The no-budget stance sits awkwardly with the Glass launch post's account of an AI budget overrun ([ramp-introducing-glass](ramp-introducing-glass.md)); timing and scope (engineering vs company-wide) may differ.
