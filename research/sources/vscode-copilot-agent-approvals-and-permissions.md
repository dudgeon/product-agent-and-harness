---
title: "VS Code docs: Approvals and permissions for agent sessions (GitHub Copilot)"
source_url: https://code.visualstudio.com/docs/agents/run/approvals
author: Microsoft (VS Code team)
publisher: code.visualstudio.com
published: unknown (current as of retrieval)
retrieved: 2026-10-25
type: docs
evidence: first-party
filed_by: research-skill-rigidity-spectrum
themes: [decision-rights-for-agents, risk-sloped-review, gate-judge-separation, policy-enforcement-fail-open]
relevance: medium
---

## Relevance to the project
The second major coding harness's autonomy slider, for comparison with Claude Code and goose. Three per-session permission levels (Manual, Assisted with an LLM judge, Allow all) plus an Autopilot mode; approvals scoped to one use, session, workspace or global; regex allow/deny lists for terminal commands; and sandboxing that stays in force even under Allow all. The structure converges with Claude Code's (human prompt, model judge, or none, with deterministic deny rules and a sandbox underneath), which suggests the industry has settled on the same three gate types the project's dimension 2 names.

## Themes
- decision-rights-for-agents: permission levels are chosen per chat session; `/yolo` and `/autoApprove` are session-scoped; `chat.tools.global.autoApprove` applies everywhere, and the docs recommend session scope "when possible" (Scope of auto-approval).
- gate-judge-separation: "Assisted permissions" (experimental, folder isolation only) has an LLM judge review each tool call; the docs warn it "can make mistakes in its risk assessment" (Permission levels).
- risk-sloped-review: terminal auto-approval takes true, false or a regex per command; compound commands need every subcommand to match; a false rule forces approval but does not block (Terminal commands).
- policy-enforcement-fail-open: terminal auto-approval is "a best-effort convenience, not a security boundary" with known detection gaps; sandboxing or a container is recommended for high-risk work (Warnings).

## Key points
- Tool approval can be granted for a single use, the session, the workspace or all future invocations; `chat.tools.eligibleForAutoApproval: false` removes the option for a tool.
- URL requests and responses are approved separately; trusted domains skip request approval only.
- `github.copilot.chat.claudeAgent.allowDangerouslySkipPermissions` bypasses all checks and is recommended only in an isolated sandbox without internet.
- First-time warning dialogs appear for Allow all, Autopilot, Assisted permissions and global auto-approve.
- Sandboxing restricts filesystem and network independently of permission level (Preview on macOS/Linux/WSL2).

## Could not verify
- Page date; the separate "chat agent mode" page did not cover the ask/edit/agent mode distinctions.
