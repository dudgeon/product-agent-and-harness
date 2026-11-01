---
title: "Tutorial: Hand off work between agents in VS Code"
source_url: https://code.visualstudio.com/docs/agents/agents-handoff-tutorial
author: Microsoft (VS Code team)
publisher: code.visualstudio.com
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [harness-portability, identity-delegation, meta-harness, remote-agent-invocation]
relevance: medium
---

## Relevance to the project
Shows the session itself moving between harnesses: from a Local session, the Session Target dropdown hands the ongoing task to the Copilot, Claude or Codex harness, and "the conversation history and context move to the destination session" while tools, permissions and models may change. It is a third shape beside relay and through line: the conversation is the through line and the harness under it is swapped. The handoff is one-way (Copilot, Claude and Codex sessions can receive but not hand off further), and a cloud session does not receive local files or the local conversation.

## Themes
- harness-portability: Local to Copilot, Claude or Codex by dropdown; "Copilot, Claude, and experimental Codex sessions can receive handoffs but can't hand off to another harness or to a cloud session"; customizations follow the selected harness.
- identity-delegation: Copilot uses the same GitHub authentication as VS Code chat, including a GitHub Enterprise account; Claude and Codex use a Copilot sign-in or a separate provider account or API key, and "The model you select determines the provider and billing for that turn"; the page does not say which identity carries over.
- remote-agent-invocation: enabling cloud sessions "does not move a local conversation or local files into the cloud"; Cloud sessions replace the Copilot cloud agent workflow on GitHub Actions in the Agents window.

## Key points
- Policy-driven move: enterprise sandbox or permission settings can move a Local session to the Copilot harness, archiving the original read-only; history and unsent input are preserved, no prompt submitted.
- SDK Policy Hooks are not loaded in Local sessions; check hook compatibility before reuse.
- Related (search snippets, not read in full): a `/delegate` command and "Continue In > Cloud" carry full chat history into a cloud agent session ([cloud agents page](https://code.visualstudio.com/docs/agents/agent-types/cloud-agents)).

## Could not verify
- How uncommitted changes and worktrees transfer; whether cloud sessions open branches or PRs. Page dated 10/28/2026.
