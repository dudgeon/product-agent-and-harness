---
title: "Behind the build: A hands-on AI Teammates walkthrough from Asana's CPO"
source_url: https://forum.asana.com/t/behind-the-build-a-hands-on-ai-teammates-walkthrough-from-asanas-cpo/1134227
author: Arnab Bose (Asana CPO)
publisher: Asana Community forum
published: 2026-04-09
retrieved: 2026-10-28
type: article
evidence: vendor-claim
filed_by: research-dependency-agent
themes: [dependency-detection-automation, human-review-gates, agent-originated-requests, shared-persistent-sessions]
relevance: medium
---
## Relevance to the project
The one worked example of Launch Planner in operation: a recurring check reads timelines, engineering backlogs, standup transcripts and capacity data, flags a slipping API migration that opens a "40-hour engineering capacity gap that could delay the entire launch", and proposes to "reprioritize the migration task and reassign one backend engineer"; "The team reviews, agrees, and the work gets updated." It shows the propose-then-human-approve loop, and that the inputs include meeting transcripts, not only tracker links.

## Themes
- dependency-detection-automation: reasoning across the Work Graph, "connecting signals across projects, meeting notes, and team capacity".
- human-review-gates: approvals at checkpoints (brief approval triggers the next teammate; the team approves the re-plan).
- agent-originated-requests: "Instead of just surfacing the problem, the teammate proposes specific operational actions".
- shared-persistent-sessions: teammates are "co-workers that operate within your team's shared workflows", not personal assistants.

## Key points
- Demo scenario (marketing campaign), recorded; not a customer outcome.
