---
title: "Open-Inspect (ColeMurray/background-agents) README"
source_url: https://github.com/ColeMurray/background-agents
author: Cole Murray
publisher: GitHub
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, build-vs-buy, agent-frameworks]
relevance: high
---
## Relevance to the project
An MIT open-source reimplementation of the Inspect pattern on Cloudflare Workers/Durable Objects plus Modal/Daytona/E2B sandboxes, with an explicit single-tenant threat model and honest documentation of access-control gaps. A reusable reference for shared-persistent-session design and its pitfalls. Community project, not Ramp's code.

## Themes
- shared-persistent-sessions: a Durable Object per session holds SQLite, a WebSocket hub and event stream; clients are web, Slack, GitHub, Linear, webhooks; presence indicators and prompts attributed to authors in git commits
- shared-persistent-sessions: access model has Workspace/Team/Private visibility separate from ownership, break-glass audited read for workspace owners, but 'Team-visibility read restrictions only apply when TEAMS_ENFORCEMENT=on. The default is shadow'
- agent-frameworks: sandbox runs a Supervisor, a harness (OpenCode or Claude Agent) and a Bridge back to the control plane; harness is pluggable

## Key points
- Single-tenant only: users assumed trusted; recommended SSO/VPN and narrow GitHub App installs.
- Documented gaps: credentials cached on disk so snapshots can retain them; revoking a grant does not immediately revoke issued tokens; session creation does not check the user's personal GitHub repo permissions; GitLab uses a deployment-wide PAT.
- Operational limits: 30-minute sandbox boot budget default; automations auto-pause after 3 consecutive failures; multi-repo capped at 10.
- Reported popularity at retrieval: ~3.4k stars (the README page); other listings vary.

## Could not verify
- Maturity/release status not stated in the README; docs/AUTH.md not read.

## Verification (user-story-mapping audit, 2026-10-24)

Re-read README verbatim (raw.githubusercontent.com, main) plus docs/HOW_IT_WORKS.md, for how sessions, projects, artifacts and outputs are organised. GitHub API at retrieval: 3,395 stars, MIT, created 2026-01-25, pushed 2026-10-24, homepage backgroundagents.dev. README credits: "inspired by Ramp's Inspect" (links builders.ramp.com/post/why-we-built-our-background-agent); it is not Ramp's repository, and a `ramp/open-inspect` repo does not exist (404).
- Unit of work: "A session is the core unit of work in Open-Inspect." Sessions are "Tied to a workspace" (one repo, up to 10 ad hoc, a saved environment, or no repository), persistent, multiplayer, stateful.
- What a session stores (HOW_IT_WORKS, "What's Stored in a Session"): Messages, Prompt attachments, Events, "Artifacts | PRs created, screenshots captured", Participants, Sandbox state. Each session has its own SQLite database in a Durable Object. Lifecycle Created -> Active -> Archived (restorable).
- "Project" does not exist as a concept; the grouping objects are repositories, environments ("a named, reusable set of repositories", workspace- or team-owned, immutable ownership), and teams ("Teams own sessions, environments, and automations"). Visibility is Workspace / Team / Private, separate from ownership.
- Outputs are pull requests (one per repository per session), screenshots, and session event streams; artifacts are "announced to clients" via `artifact_created` events. No document, spec or knowledge store; "Managed Skills" are reusable instructions pinned by revision to a session. Linear integration maps Linear team and project to repository or environment, i.e. the project record lives in Linear.
- Finding work: a session sidebar lists repositories, branches and PRs; the README mentions no search over past sessions.
