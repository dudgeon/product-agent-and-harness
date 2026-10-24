---
title: Claude Cowork - Overview and Security Considerations
source_url: https://answers.atlassian.syr.edu/wiki/spaces/ITSAI/pages/836698117/Claude+Cowork+Overview+and+Security+Considerations
author: Ryan E. Elstad (Syracuse University ITS)
publisher: Syracuse University Answers wiki
published: 2026-02-20
retrieved: 2026-10-24
type: docs
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, human-review-gates, vendor-claims-vs-independent-evidence]
relevance: high
---

## Relevance to the project
A real enterprise customer (a university with compliance obligations) disabled Claude Cowork org-wide because its activity was not captured in Anthropic's audit logs, Compliance API or data exports, citing Anthropic's own guidance not to enable Cowork for regulated workloads. It shows that, for a regulated buyer, audit coverage of each agent surface decides adoption, independent of capability. The gap was later closed (see anthropic-compliance-api-cowork-claude-code, GA 2026-08-26), and the page is now marked archived.

## Themes
- agent-control-plane: audit coverage per surface is the gating control; only one org-wide on/off toggle, no role-based control at the time.
- human-review-gates: Cowork could permanently delete files in granted folders; documented cases of unintended deletion; prompt-injection exposure.
- vendor-claims-vs-independent-evidence: independent customer decision record.

## Key points
- Cowork: autonomous agent in Claude Desktop (macOS, Windows), research preview from January 2026, built on Claude Code's architecture; reads/writes/deletes files, runs code, uses Claude in Chrome, plugins and MCP.
- Conversation history stored locally only, outside Anthropic retention and university governance; plugins stored per machine, not centrally managed.
- Decision: disabled for all users; alternatives Claude Chat (covered by audit) and Claude Code/API (premium seat).

## Notable quotes
- Anthropic guidance quoted: "If your organization requires audit trails for compliance purposes, do not enable Cowork for regulated workloads."
- "Cowork is currently disabled for all users in the Syracuse University Claude Enterprise organization."

## Could not verify
- Whether Syracuse re-enabled Cowork after Compliance API coverage reached GA. Retrieved via WebFetch (model-summarised view).
