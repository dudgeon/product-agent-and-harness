---
title: A Security Engineer's Guide to the A2A Protocol
source_url: https://semgrep.dev/blog/2025/a-security-engineers-guide-to-the-a2a-protocol
author: Kurt Boberg (Semgrep)
publisher: Semgrep blog
published: 2025-12-17
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-protocol-security, identity-delegation]
relevance: medium
---

## Relevance to the project
The primary source behind the widely repeated claim that A2A "supports but does not enforce Agent Card signing", which Track 3 had only second-hand. It also notes no enforced short-lived tokens, coarse scopes, no protocol-level consent step, and authorisation left to implementations. Written against v0.3; v1.0 later added signed-card support and dropped implicit/password OAuth flows but, per a vendor blog (grith, 2026-03-20, read), still leaves signing optional.

## Themes
- `agent-protocol-security` (proposed): "supports but does not enforce Agent Card signing", enabling spoofing; no central registry, so cheap spoofing is expected as background noise. Stream hijacking with a stolen session token; webhook push to arbitrary targets as a watch item; SDK serialisation bugs expected early.
- `identity-delegation`: "A2A doesn't enforce short-lived tokens"; scopes coarse; no protocol requirement for user approval before data is shared between agents; authorisation "implementation-defined". Recommends capability-based access control to avoid confused-deputy problems.

## Key points
- Advice: define the authorisation model for agentic users before building; treat inputs as untrusted; choose SDKs carefully; watch Unicode normalisation, nesting depth, payload size, dynamic typing.
- Links an A2A audit checklist (not read).
- grith's post (https://grith.ai/blog/a2a-protocol-zero-defenses-prompt-injection, vendor advocacy, not filed separately) argues the v1.0 spec still has no consent task state, no prompt-injection defence and opaque remote execution, while crediting v1.0 with PKCE and removing implicit/password flows.

## Could not verify
- Whether each point still holds for v1.0; the checklist itself.
