---
title: "Model Context Protocol Server (SailPoint Identity Security Cloud)"
source_url: https://documentation.sailpoint.com/saas/help/ai/mcp.html
author: SailPoint
publisher: SailPoint documentation
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [agent-originated-requests, identity-delegation, decision-rationale-records]
relevance: high
---

## Relevance to the project
A shipped example of an agent submitting access requests into an enterprise identity-governance workflow on a user's behalf: SailPoint's MCP server lets an agent list requestable items, initiate a request (including for another user where enabled), check status and cancel, and every such event is stamped "Requested by AI on behalf of <identity>". Approval stays inside SailPoint's normal workflow; the MCP server exposes no approval tools.

## Themes
- agent-originated-requests: tools: list requestable items, initiate access request, query status by request ID, cancel pending request (Access requests).
- identity-delegation: agents act on behalf of the user; request-for-others only if an admin has enabled it.
- decision-rationale-records: audit comments "Requested by AI on behalf of <identity>"; cancellations recorded likewise; searchable.

## Key points
- Also exposes identity-intelligence lookups (profile, access, risk, access history) for SecOps.
- No approve/certify tools: humans (or configured policy) still decide.

## Could not verify
- Auth mechanism, lifecycle status, and whether policy auto-approval applies to AI-initiated requests.
