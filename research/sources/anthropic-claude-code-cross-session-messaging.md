---
title: "Message your other Claude Code sessions (cross-session messaging)"
source_url: https://code.claude.com/docs/en/cross-session-messaging
author: Anthropic
publisher: Claude Code docs (code.claude.com)
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [human-relay-removed, identity-delegation, agent-protocol-security, delegation-return-contract]
relevance: high
---

## Relevance to the project
Claude Code now has a built-in peer channel: one session can send plain text to another of the same person's sessions on the same machine, another machine (through Anthropic's servers via Remote Control) or the cloud. It removes the person as copy-paste relay between their own sessions, which is the use case the A2A feature request (#28300) asked for. It is scoped to one user: nothing here lets the person's session message a platform owner's agent or another person's session, so it does not carry a dependency ask to an owner outside the team. Its trust rules (a peer message is never consent, never changes configuration, commands do not run) are a ready-made design for how an intent or dependency agent should treat messages from other agents.

## Themes
- human-relay-removed: "When one of your sessions learns something another session needs ... Claude passes it along instead of you copy-pasting between terminals."
- delegation-return-contract: "A message is a piece of text one Claude writes to another, never the sender's conversation history or files. To move a whole conversation or its context, resume the session instead." Plain text only; about one million characters cap on the same machine.
- identity-delegation: same OS user only on a machine (socket restricted to the user); beyond the machine it needs a claude.ai sign-in and Remote Control; "Permission boundaries stay per-session"; Claude is told never to ask another session for an action denied in its own.
- agent-protocol-security: an incoming message "can't approve anything", "can't change configuration", "Commands don't run"; inbound policy `accept`, `hold` or `refuse`; sessions that bypass permissions hold incoming messages for approval by default; `isolatePeerMachines` requires approval before any message leaves the machine; loops throttled (50 queued, repeats dropped).

## Key points
- Tools: `ListAgents` and `SendMessage`; @-mention a session by name; `/list-agents` shows subagents, teammates, local sessions, cloud sessions and Remote Control sessions.
- Delivery: read between tool calls during a turn, or starts a new turn when idle; held messages wait for approval (dialog expires after 5 minutes by default).
- `notify_when_idle`: a session can ask for one notice when another local session goes idle or exits; dropped after 12 hours.
- Cloud sessions cannot reply with SendMessage to a message from another machine.
- Not available with an API key or on Bedrock, Google Cloud or Foundry for beyond-machine sessions.
- Admins can turn it off org-wide (deny `SendMessage`, `ListAgents`; `crossSessionInbound: refuse`).

## Notable quotes
- "a message from another session never counts as your consent, so it can't answer a pending permission prompt on your behalf."

## Could not verify
- Whether messages are logged anywhere an organisation could audit; the page does not say.
- Requires v2.1.224 or later; behaviour as of 2026-10-31.
