---
title: Glean Agents can now work independently, build faster, and stay governed at scale
source_url: https://www.glean.com/blog/glean-agents-go-2026
author: Glean
publisher: glean.com blog
published: 2026-08-26
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, identity-delegation, evals-autonomy-trust, skill-supply-chain-security, remote-agent-invocation]
relevance: medium
---

## Relevance to the project
Glean's 2026 agent platform release adds the control-plane pieces (per-agent identity in public beta, agent scanning at publish, combined governance policies, skill scanning and rollback, pre-publish evals) and, notably, lets builders author Glean agents from Claude Code or Cursor with Git sync, plus A2A interop. So Glean is a governed agent workspace on top of an enterprise graph that treats coding harnesses as authoring tools, not as runtimes it governs.

## Themes
- identity-delegation: "Each one gets its own identity and provisioned access" (agent identity public beta; scoped credentials across a dozen+ tools).
- agent-control-plane: governance policies combining access, behaviour and usage-limit rules, scoped to groups or agents, testable before rollout.
- evals-autonomy-trust: built-in evals (private beta) generate test sets before publishing.
- skill-supply-chain-security: skills scanned for risk before they run; versioned with one-click rollback; agent scanning (beta) flags over-provisioned write tools and holds risky agents for moderator approval.
- remote-agent-invocation: A2A support for agents on other platforms.

## Key points
- "Independent agents" own multi-step workflows and call a human only for decisions; targets on-call, voice-of-customer synthesis, sales.
- Build in Claude Code/Cursor, sync with Git; version checkpoints; collaborative editing.
- No customers or metrics named; deployment model not stated (other Glean pages describe single-tenant customer environment).

## Notable quotes
- "Each one gets its own identity and provisioned access, so you can see exactly what it touched and why."

## Could not verify
- Glean's security showcase page (glean.com/security-showcase, Glean Protect, AWARE framework with Databricks and Palo Alto Networks) was read but gave no concrete controls; not filed separately. Retrieved via WebFetch (model-summarised view).
