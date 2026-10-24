---
title: Security and Privacy Hardening (Cursor enterprise docs)
source_url: https://cursor.com/docs/enterprise/security-hardening
author: Cursor (Anysphere)
publisher: cursor.com
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-portability, human-review-gates]
relevance: medium
---

## Relevance to the project
The fullest set of admin controls found on any harness in this round: SSO, SCIM, audit logs streamed to a SIEM, org-enforced Privacy Mode with ZDR for Cursor-routed models, model and MCP allowlists, fail-closed hooks distributed by MDM or cloud, and an org sandbox policy. It is the bar an open or third-party harness has to meet in a regulated setting.

## Themes
- harness-portability: ZDR holds only for Cursor-routed models; with personal API keys, ZDR depends on your own provider agreement, so the guide recommends restricting BYOK.
- human-review-gates: org Run Mode policy; "Auto-review" sandboxes shell commands when it can and routes the rest through "a best-effort classifier", so pair it with hooks.

## Key points
- Audit logs for authentication and admin events, streamable to SIEM, webhook or S3.
- Privacy Mode enforced org-wide, on by default for Enterprise; non-ZDR models need admin approval.
- MCP allowlist with per-server tool restriction and network modes.
- Hooks at lifecycle points (block commands, scrub secrets, audit); set failClosed for critical hooks.
- Not covered: self-hosted workers, data residency.
