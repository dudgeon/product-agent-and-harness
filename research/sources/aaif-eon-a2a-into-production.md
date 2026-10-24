---
title: What We Learned Putting A2A Into Production
source_url: https://aaif.io/blog/what-we-learned-putting-a2a-into-production
author: Rachel Neriya Schifter (Eon)
publisher: aaif.io (Agentic AI Foundation blog)
published: 2026-08-26
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, identity-delegation, agent-failure-modes, one-job-per-agent]
relevance: high
---

## Relevance to the project
The only named, first-hand account found of an organisation running A2A between agents in production with engineering detail. Eon (a cloud data platform) moved three of about 20 specialist agents behind A2A because they cross an ownership boundary (separate release cycles, production credentials, tenant-built agents Eon cannot see). It is first-party and published on the foundation's own blog, so it is a builder's view in a promotional venue, not independent evaluation, and it gives no volumes. Its failure list maps directly onto what a regulated intent-shaping agent would face: the asker's identity is lost across the hop, answers arrive without provenance, sync calls hit 60 s gateway timeouts, and empty error events led the orchestrator to fabricate answers.

## Themes
- `remote-agent-invocation`: Root orchestrator plus about 20 in-process specialists; only three moved out of process behind A2A (triage agent with production credentials, a semantic-layer agent, and tenant-built agents on other frameworks). Rationale: bespoke HTTP would mean owning auth, retries, streaming and task lifecycle; for tenant agents a shared contract and runtime-readable agent card were required.
- `identity-delegation`: "Cross-agent calls lost the asker's identity", so the far side answered as a service identity; Eon encoded user identity in `context_id` (`ADK/{app}/{user}/{session}`) because the spec has no first-class way to say who is asking.
- `agent-failure-modes`: Error events with no content were dropped, so the orchestrator fabricated answers; the first fix made it keep citing one old 502. Remote context exhaustion broke long conversations (fixed with an epoch counter in `context_id`). Non-streaming `message/send` hit a 60 s gateway timeout; `message/stream` fixed it.
- `one-job-per-agent`: Keep specialists in-process where a function call is enough; put a protocol boundary only where ownership, credentials or release cadence differ.

## Key points
- Extensions built: a `DataContext` provenance envelope (executed query, lineage with freshness, confidence, governance flags) declared in `capabilities.extensions` and opted into with an `A2A-Extensions` header; `auto_route` switch; SSRF guard on agent and token-endpoint URLs; about 400 lines of wrapper code.
- Still on A2A 0.3; v1.0 replaces transport fields with `supportedInterfaces`.
- Proposes upstream: session-lifecycle signalling across a hop, a portable retryable error signal, an extension URI registry.
- Verdict: would choose A2A again, while saying it "added failure modes rather than removing them".

## Notable quotes
- "Adopting A2A added failure modes rather than removing them."
- "We'd choose A2A again."
- "You can't import a stranger's agent. You can only call it, and to call it you need a contract neither side wrote for the other."

## Could not verify
- No traffic volumes, latency figures, user counts or cost. Author's role not stated. Published on the foundation's blog, so selection bias toward positive accounts is likely.
