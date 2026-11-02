---
title: "Solving the Identity Crisis for AI Agents"
source_url: https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/
author: Matt Mathew, Prasad Borole, Meng Huang (Uber AI Security)
publisher: Uber Engineering Blog
published: 2026-05-21
retrieved: 2026-11-02
type: article
evidence: first-party
filed_by: competitive-teardown-uber-cortana
themes: [identity-delegation, agent-protocol-security, agent-control-plane, enterprise-admin-controls, remote-agent-invocation]
relevance: high
---

## Relevance to the project
Uber's design for agent identity is the most concrete first-party answer to "who did what, on whose behalf" across agent hops: SPIRE attests the workload, an Agent Registry binds agent to workload, and a Security Token Service mints single-hop, minutes-long JWTs that carry the full actor chain (user, then each agent) to the MCP Gateway. It is the identity layer that lets Cortana or Minion act "with the user's permissions" and still leave an audit trail. It bears directly on the identity-delegation and agent-to-agent invocation questions in the harness design.

## Themes
- identity-delegation: each token embeds an attested actor chain, e.g. [user1, oncall-agent, investigation-agent], so the gateway sees full lineage; per-hop exchange "conceptually based on" OAuth 2.0 Token Exchange (RFC 8693) (Identity issuance).
- agent-protocol-security: only the STS may mint agent tokens; tokens are single-hop with a specific audience and TTL "in the order of minutes", so they cannot be replayed elsewhere (STS).
- agent-control-plane: Agent Registry (populated by Michelangelo) is the source of truth tying agents to workloads; MCP Gateway is the policy enforcement point; AI Gateway with AI Guard mediates model calls (prompt injection, jailbreak, content safety, PII) (Architecture).
- remote-agent-invocation: a standard A2A client (on the A2A protocol) automates token exchange and actor-chain propagation; legacy agent-to-agent calls are being migrated in phases (Paved path).
- enterprise-admin-controls: policies follow internal risk classification; high-risk systems have mandated policies at the MCP Gateway; "Agent IAM Observability" dashboard shows each hop with ALLOWED/denied decisions (Observability).

## Key points
- Problem 1: identity models know humans and non-human identities (service accounts, keys) but not agency, i.e. an entity acting for another. Problem 2: "Execution context (originating user, intermediate agents) is dropped across agent hops."
- Worked example: an on-call engineer's Oncall Agent delegates to Investigation and Monitoring agents, which open a PR; without the chain, the engineer is untraceable in the PR.
- Uber built an internal agent platform in early 2025 (Python SDK, framework-agnostic, plus no-code UI authoring; both deploy to Kubernetes). "Thousands of internal agents" now.
- Flow: workload gets SPIFFE SVID from SPIRE; SDK sends metadata, inbound JWT and outbound audience to STS; STS checks the registry; returns a next-hop JWT. P99 for token exchange under 40 ms.
- Considered the open-source agentgateway proxy but put the logic in the SDK, because context propagation is an application-layer problem.
- Roadmap: (1) identity and trust foundation (this post); (2) dynamic access control incl. human-in-the-loop and workflow authorization; (3) unified enforcement plane. Future token claims may include session IDs and request intent. Tracks IETF WIMSE and an AI-agent auth draft.

## Notable quotes
- "Delegation is the default mode - agents work on behalf of others" (Motivation)
- "Only the STS is permitted to mint tokens for AI agents." (Providing agent identities)
- "who did what, when and why" (Introduction)

## Could not verify
- Cortana, Minion and Genie are not named; whether Cortana personas are registered agents in this registry is not stated.
- "Thousands of agents" is not broken down (no-code vs SDK, personas vs services).
