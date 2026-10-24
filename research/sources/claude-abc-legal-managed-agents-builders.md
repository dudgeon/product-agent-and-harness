---
title: How ABC Legal turned every employee into a builder with Claude Managed Agents
source_url: https://claude.com/resources/articles/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-08-17
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [evals-autonomy-trust, non-engineer-builders, one-job-per-agent, org-learning-loop, outcome-measurement-gap]
relevance: high
---

## Relevance to the project
ABC Legal moved employee-built agents off personal desktops into a governed fleet where every agent is config plus prompt in git, changed only by an approved pull request, and starts as a recommender that earns autonomy by matching human decisions. It is the most complete operating model filed so far for non-engineers building production agents under governance: a starter-kit repo, one job per agent, Slack reactions harvested as labels, a weekly tuner that proposes prompt changes as PRs, and a per-agent value-versus-cost metric. All figures (50+ agents, about 50% cost reduction on some tasks, 98% agreement for one reviewer agent) are the customer's claims, published by Anthropic.

## Themes
- evals-autonomy-trust: every agent starts by posting recommendations for human review; once it is as good as or better than humans on that task it moves to "automation mode" and stays inside the same measurement framework ("Why Claude Managed Agents"; "Best practices").
- non-engineer-builders: a 15-person steering committee from finance, marketing, ops and development, none of them software developers, all had working agents within a week by cloning a repo and describing the agent to Claude Code ("Bridging the technical divide").
- one-job-per-agent: "Each agent has a name, an owner, and a single job"; most of the fleet are single-task runners ("Bridging the technical divide"; "harvest, tune, repeat").
- org-learning-loop: Initial Agent / Harvester (hourly-daily, Slack replies and emoji become labels) / Tuner (weekly, proposes prompt or config changes as a PR for human merge) ("Making the agents smarter").
- outcome-measurement-gap: each agent reports its own value in hours and dollars to a data warehouse on every run, tracked as an efficiency ratio of value to cost; agents follow a J-curve ("Why Claude Managed Agents").

## Key points
- **Context:** US legal document delivery company, 1,100 employees; Claude Enterprise rolled out early 2026; about 310 employees use Claude daily. Early agents ran as scheduled tasks on individual desktops, with no single view of what existed, what it cost or whether it ran.
- **Agents as code:** prompt, tool list, schedule, credentials and memory as config files in git; merge to main deploys. Starter kit: two templates (event-driven, scheduled), each agent in its own folder (JSON config, Markdown system prompt, deploy scripts, ops docs). Scheduled agents run on cron through Bitbucket Pipelines.
- **Division of responsibility:** Anthropic's Managed Agents owns the loop, sessions, memory, console and models; ABC Legal owns prompt, tool list, triggers, audit trail and the outcome feedback loop. Selection criteria: versioning, observable sessions, workspace billing, model selection, memory primitives, MCP wiring, no infrastructure to run.
- **Example agents:** AI code reviewer on four codebases (engineers wait for it before merging); eFiling rejection diagnoser (Slack diagnosis in about a minute); court job verification via an in-agent browser; attorney coverage outreach; AR remittance file built for one-click approval; capitalise-or-expense verdict per engineering ticket; Google Ads weekly recommendation; "Charvis", a service-job reviewer claimed to agree with compliance about 98% of the time.
- **"Deliveries-as-code":** at sister company Docketly, about 145 routing rulesets are YAML files in git; a four-agent loop (verdict, harvester, tuner, deployer) turns an emoji flagging a mis-routed delivery into a merged rule change within a week. The deployer only executes human-approved changes; human review is the only manual step.
- **Model routing and cost:** Sonnet default, Haiku for high-volume, Opus where reasoning justifies cost; all AI spend tracked by vendor, tool, team and use case; spend fell from July while usage grew.
- **Lessons stated:** make decisions look like pull requests; start humans in the loop; the hurdle was git, not AI (non-engineers struggled with cloning and PRs); not every task deserves an agent; skip local scheduled tasks and go straight to a hosted runtime.
- **Limits:** no error rates, incidents or audit findings reported; the 50% cost reduction is "up to" and "before heavy optimization"; how "as good as humans" is judged per agent is not specified beyond agreement with human calls.

## Notable quotes
- "If you want an agent involved in a decision, make the decision look like a pull request." (Brandon Fuller, CTO)
- "Every agent earns trust before it acts alone. It doesn't start there." (Brandon Fuller)

## Could not verify
- Named author of the article; thresholds used to move an agent from recommendation to automation mode.
