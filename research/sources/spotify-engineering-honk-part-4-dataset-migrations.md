---
title: "Background Coding Agents: Supercharging Downstream Consumer Dataset Migrations (Honk, Part 4)"
source_url: https://engineering.atspotify.com/2026/4/background-coding-agents-dataset-migrations-honk-part-4
author: Devon Edwards Joseph (Senior Engineer, Spotify)
publisher: Spotify Engineering blog
published: 2026-04-22
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [legible-org-for-agents, agent-ready-intent, human-review-gates, org-context-grounding, artifact-standardization]
relevance: medium
---

## Relevance to the project
A worked example of the full chain for one cross-team change: Backstage lineage finds the affected consumers, code search and the Fleetshift plugin pick target repos, a hand-written context file instructs Honk, owning teams test and merge. It shows that a human migration guide was not good enough as agent input (Honk guessed mappings) and that explicit mapping tables were. It also shows the agent flagging judgment calls instead of guessing, which is a useful default for any agent acting on someone else's intent.

## Themes
- legible-org-for-agents: Backstage endpoint lineage listed downstream consumers and showed the scale (about 1,800 direct pipelines, several thousand indirect).
- agent-ready-intent: repurposing the human migration guide gave incomplete context and guessed mappings; explicit field-mapping tables in a context file worked (section on context).
- human-review-gates: BigQuery Runner and dbt repos rarely had build-time tests, so Honk could not self-verify; owning teams tested by hand before merging.
- org-context-grounding: Honk had no skills, no schema queries and no external docs at the time (a deliberate guardrail), so the prompt had to be self-contained.
- artifact-standardization: consistent BigQuery Runner and dbt patterns could be automated; Scio was too varied and was dropped.

## Key points
- Six-month deadline to migrate about 1,800 direct downstream pipelines across three frameworks.
- 240 automated migration PRs; about 10 engineering weeks saved (Spotify estimate, Apr 2026). No merge or rework rate is given.
- Where a field needed a use-case decision, Honk left it unchanged and added a comment linking to the human guide.
- Fleetshift's overview UI tracked progress and gave one-click access to each PR; also used to talk to owners.
- Planned: let Honk gather its own context (tickets, docs) before changing code.

## Could not verify
- How the 10-week estimate was made; how many of the 240 PRs merged.
