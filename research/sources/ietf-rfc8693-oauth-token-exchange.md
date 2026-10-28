---
title: "RFC 8693: OAuth 2.0 Token Exchange"
source_url: https://www.rfc-editor.org/rfc/rfc8693.html
author: M. Jones, A. Nadalin, B. Campbell, J. Bradley, C. Mortimore
publisher: IETF / RFC Editor
published: 2020-01
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [identity-delegation]
relevance: medium
---

## Relevance to the project
The standards-track basis for most agent delegation designs: it distinguishes impersonation (the actor is indistinguishable from the subject) from delegation (the actor keeps its own identity and acts for the subject), and defines the `act` claim that records a chain of actors. A platform that wants to record "agent X acting for PM Y" in its decision log needs delegation semantics, not impersonation.

## Themes
- identity-delegation: delegation: "In a sense, A is an agent for B"; `act` claim identifies the current actor, nested for chains with the most recent outermost; only the current actor is used for access control, prior actors are informational; `may_act` states who is permitted to act for a subject (Sections 1.1, 4.1, 4.4).

## Key points
- Standards Track, January 2020; makes the authorisation server a Security Token Service.
- Used by AWS's Cedar multi-agent pattern to issue scoped on-behalf-of tokens per hop (see `aws-security-cedar-multi-agent-least-privilege`).
