---
title: "Agents you can coach: how Asana builds human-agent teams with Claude"
source_url: https://claude.com/resources/articles/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-09-29
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [shared-persistent-sessions, identity-delegation, org-learning-loop, public-by-default-agent-work, feedback-triage-agents]
relevance: high
---

## Relevance to the project
A concrete governance pattern for shared agents: each agent has a role, profile page, scoped access bounded by the triggering person's permissions, and a shared memory that only named admins and editors may commit to, while everyone else's feedback stays task-local. That split (work with the agent vs train it) is a direct option for the context-and-memory and review-and-autonomy dimensions, and the at-risk renewals digest and Slack-question routing are worked examples of status-update and triage agents. Evidence is a customer interview (Asana's CPO, Arnab Bose) published by Anthropic, about a product Asana sells; there are no outcome numbers at all.

## Themes
- shared-persistent-sessions: agent work lives on the shared task: plan and steps posted where everyone with access can read, comment and steer; a colleague can converse with the agent on the same task concurrently ("Keep the agent's work where everyone can see it").
- identity-delegation: agents have their own profile (users, admins, instructions, skills, integrations, permissions) and access scoped to projects/documents/apps; Asana says an agent's effective access is bounded by the permissions of the person who triggers it ("Give every agent a role").
- org-learning-loop: shared memory accumulates across users; only admins and editors can commit feedback to permanent memory, undo or delete it; others' feedback applies only to the current task ("Separate working with an agent from training it").
- public-by-default-agent-work: Bose argues one-on-one agent use hides the prompt and back-and-forth from reviewers, so they cannot align on or revise the instructions.
- feedback-triage-agents: Slack product questions become Asana tasks; agent answers from approved guidance with links, files product gaps to the product intake project, and raises enablement tasks when a question repeats ("Three jobs").

## Key points
- Third post in Anthropic's human-agent teams series; frames the three agent capabilities from post one as persistent memory, own credentials and shared context.
- Upstream step: staff talk unstructured inputs (Slack, Zoom recordings, Databricks reports, Docs) through with Claude, then log actionable items into Asana's Work Graph as projects and tasks, which agents act on. Claude is Asana's default internal AI tool.
- Agents are built around roles (content writer, insights analyst, project manager, work intake specialist, campaign analyst, campaign coordinator), shipped with pre-built skills from Asana's research and integrations (e.g. HubSpot). Advice: write the agent's purpose and owned jobs like a new hire's first-quarter plan; name users and admins separately.
- Training ownership follows standard ownership: the communications team that owns voice and tone edits the writing agent; the CPO can draft with it but not change its behaviour. Bose: one or two people per team become the experts; others never touch skills, behaviour or memory.
- At-Risk Renewal agent: reads every at-risk renewal task (CSM updates, notes, comments) and pushes a daily digest (positive momentum, negative momentum, recommended follow-ups; global then by region) to the CCO, CRO and regional CS leaders; leaders ask follow-ups and coach it to remember things. Replaced a manually synthesised weekly briefing. No accuracy or adoption data.
- Command by Asana: automated feedback-to-PR coding loops bloated cycles and slipped releases; Bose says code generation is no longer the bottleneck, planning and decisions are. Agents populate an unplanned board from customer feedback and a Slack feedback channel; people choose what enters the cycle; tickets go to a person or a coding agent; Command predicts completion (optimistic/balanced/conservative) and answers why a release is off track. Exposed via Asana's MCP server so leaders can query from Claude.
- Limits: product marketing for Asana AI Teammates and Command; single company; no metrics, no failure cases, no detail on how memory commits are reviewed or audited.

## Notable quotes
- "The bottleneck is around planning, decision-making, and refinement." (Bose, "Planning engineering cycles with Command")
- "how do we get to the place where there's standardization of the report, there's a shared workspace, and it keeps getting better with every single run?" (Bose, at-risk renewals)

## Could not verify
- Whether "bounded by the permissions of the person who triggers it" applies to scheduled or rule-triggered runs (e.g. the daily digest) and whose permissions apply then.
