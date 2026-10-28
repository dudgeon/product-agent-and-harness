---
title: "Enforce least-privilege authorization in multi-agent AI chains using Cedar"
source_url: https://aws.amazon.com/blogs/security/enforce-least-privilege-authorization-in-multi-agent-ai-chains-using-cedar/
author: Dhananjay Karanjkar (AWS)
publisher: AWS Security Blog
published: 2026-07-06
retrieved: 2026-10-28
type: article
evidence: first-party
filed_by: research-dependency-agent
themes: [governance-as-code, identity-delegation, agent-protocol-security]
relevance: medium
---

## Relevance to the project
A worked reference design for the over-permissioning failure mode when agents delegate to agents: authorisation silently widens across hops unless each hop is re-checked against the originating human's rights. The three-layer Cedar policy (agent-to-tool, agent-to-agent, originating user) plus RFC 8693 token exchange per hop is a concrete pattern for a dependency agent that calls platform agents on a PM's behalf.

## Themes
- governance-as-code: three Cedar layers evaluated in order, first deny wins: L1 agent-to-tool (trust score 1-5, namespace, lifecycle stage); L2 delegation (max five hops, requested task must be a subset of the target agent's registered capabilities); L3 originating user (role, MFA, allowed delegation depth).
- identity-delegation: Cognito JWT claims are HMAC-signed into Cedar context; RFC 8693 issues a scoped on-behalf-of token to each downstream agent.
- agent-protocol-security: cites OWASP Top 10 for Agentic Applications ASI03, Identity & Privilege Abuse.

## Notable quotes
- Goal: "prevent authorization scope from silently expanding."

## Could not verify
- Whether the full post includes a human-approval step (content truncated).
