---
title: "Use Claude Code in the cloud (Claude Code on the web docs)"
source_url: https://code.claude.com/docs/en/claude-code-on-the-web.md
author: Anthropic
publisher: code.claude.com docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, harness-portability, remote-agent-invocation, cost-control-routing]
relevance: high
---
## Relevance to the project
Anthropic's own description of its cloud-session pattern: vendor-managed VM per session, sessions survive laptop close, Team-visibility sharing, one-way CLI teleport, per-user identity. It is the closest vendor-product analogue to what Glass/Inspect built, and it shows where the vendor's shared-session model stops (snapshot sharing, not live multiplayer). Useful as the reference point for 'persistent but single-owner' sessions.

## Themes
- shared-persistent-sessions: cloud sessions keep running after the laptop closes and can be steered from mobile; sharing is Private or Team visibility, and 'recipients see the latest state when they open the link, but their view doesn't update in real time' (Share sessions)
- harness-portability: handoff is deliberately asymmetric: cloud to terminal via --teleport (needs clean git state, same repo, same claude.ai account), terminal to cloud only as a new session or via the Desktop app; the terminal copy is a fork that does not sync back (Move tasks between terminal and cloud)
- memory-architecture: only the conversation history is restored when an expired environment is reopened; running shell commands, subagents and session-scoped scheduled tasks are not (Environment expired)
- cost-control-routing: no separate VM charge; cloud sessions share the account's rate limits, so parallel tasks consume limits proportionately (Limitations)

## Key points
- Runs on Anthropic-managed VMs or, in beta, an org self-hosted environment (see anthropic-self-hosted-environments). Plans: Pro, Max, Team, Enterprise with premium seats. Not available with Bedrock/Vertex, ZDR, HIPAA or CMEK orgs.
- Identity: GitHub credentials stay on Anthropic servers and a proxy attaches them; auto-fix PR replies are posted under the user's GitHub account but labelled as Claude Code (Auto-fix section). Anything acting through the user's connected identity appears as the user.
- Team sharing: Team visibility makes a session visible to org members, with repo-access verification on by default; Claude-in-Slack sessions are auto-shared Team-visible.
- Isolation: separate VM per session, network allowlist by default (Trusted), credential proxy; note when network is disabled Claude Code can still reach the Anthropic API, which 'may allow data to exit the VM'.
- Failure/limits: cloud sessions stop after inactivity and the VM is reclaimed; IP-allowlisted orgs fail all hosted sessions; GitHub-only for clone/PR; capacity is provisioned on demand ('retry after a minute').
