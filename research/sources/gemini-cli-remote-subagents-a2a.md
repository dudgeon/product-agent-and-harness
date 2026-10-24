---
title: Remote Subagents (Gemini CLI documentation)
source_url: https://geminicli.com/docs/core/remote-agents/
author: Google (gemini-cli maintainers)
publisher: geminicli.com / github.com/google-gemini/gemini-cli (docs/core/remote-agents.md)
published: 2026-01-27
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, harness-portability, identity-delegation]
relevance: high
---

## Relevance to the project
The one general-purpose coding harness found with a native, documented A2A client. Remote agents are declared exactly like local subagents (Markdown files with YAML frontmatter in `.gemini/agents/` or `~/.gemini/agents/`), so an A2A agent is a drop-in subagent that a team can version in the repo. This is the shape a Claude Code or Codex A2A client would most likely take, and it shows the client side is small; neither has one.

## Themes
- `remote-agent-invocation`: `kind: remote`, `name`, and `agent_card_url` or inline `agent_card_json`; multiple remote agents per file; points to ADK samples as compatible A2A servers.
- `harness-portability`: Project-level definitions are "shared with your team" through the repo, same as local subagents.
- `identity-delegation`: `auth` block supports `apiKey`, `http`, `google-credentials` and `oauth` (OAuth 2.0 with PKCE via browser); traffic honours `general.proxy` or `HTTP(S)_PROXY`, which matters for egress control in a regulated network.

## Key points
- Doc first committed 2026-01-27, last changed 2026-04-10 (git history of `docs/core/remote-agents.md`).
- Sample agent cards in the doc use `"protocolVersion": "0.3.0"`.

## Could not verify
- Whether remote subagents are on by default or behind an experimental flag (third-party sources disagree). An HN commenter (2026-06-19) claims Gemini CLI "is deprecated and replaced by antigravity-cli"; not checked.
