---
title: "Now Assist for Strategic Portfolio Management (SPM) release notes"
source_url: https://www.servicenow.com/docs/r/store-release-notes/store-itbm-rn-now-assist-spm.html
author: ServiceNow
publisher: ServiceNow product documentation (Store release notes)
published: 2026-10-01
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [status-update-agents, dependency-detection-automation, human-review-gates, agent-originated-requests]
relevance: high
---
## Relevance to the project
The most complete first-party list of what a portfolio-management vendor's AI actually does with dependencies in late 2026: a Project Task Monitor agent that "autonomously" watches critical-path tasks and emails the project manager; Project Insights that flag "dependency issues and critical path changes"; Project Q&A that answers questions about dependencies; AI-identified project risks the PM accepts or rejects into the RIDAC log; and a Demand Manager AI Specialist that validates and converts demands against governance policies. There is no skill that discovers dependencies; all of it reads dependencies people already recorded.

## Themes
- dependency-detection-automation: Project Insights v9.4.0 (May 2026) added "dependency issues, and critical path changes"; Project Q&A "now supports questions about work notes and dependencies"; the notes describe no standalone dependency analysis skill.
- agent-originated-requests: Monitor Project Tasks agent (v5.1.1, Mar 2025): "Autonomously monitor project tasks on the critical path of a project", emailing the PM; Project Summary emails on cadence or on demand.
- human-review-gates: AI-identified risks are "presented to the project manager for review, allowing them to accept and add them to RIDAC or reject them"; the Demand Manager AI Specialist "Validates and converts operational demands autonomously" but is controlled-availability and "Requires approval from Servicenow".
- status-update-agents: AI Status Reports (draft status reports with red/yellow/green health), Epic Health Status across six risk dimensions, Goal Insights forecasts.

## Key points
- Seventeen skills/agents listed from Aug 2024 to Oct 2026 (v9.12.0); multiple model providers supported (Now LLM, Azure OpenAI, Gemini, Claude on AWS), with skill- and agent-level access controls.
- Demand summarisation pulls cost plans, benefit plans, demand tasks, resource assignments and work notes; auto-trigger switched to false by default.
- "published" is the latest notes entry seen (v9.12.0, October 2026); exact day unknown.
