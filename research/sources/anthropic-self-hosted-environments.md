---
title: "Self-hosted environments (Claude Code cloud sessions on your infrastructure)"
source_url: https://code.claude.com/docs/en/self-hosted-environments
author: Anthropic
publisher: code.claude.com docs
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, meta-harness, remote-agent-invocation]
relevance: medium
---
## Relevance to the project
Shows the vendor-hosted control plane plus customer-hosted runner split, analogous to CI runners. Relevant to 'org-deployed service' placement: execution and repo checkouts stay in the org network while transcripts and orchestration stay with the vendor. Notes the owner-locked runner design that prevents code mixing between users.

## Themes
- shared-persistent-sessions: control plane (queue, session stream, claude.ai UI) stays Anthropic-hosted; runners execute sessions; 'Anthropic stores the session transcript so you can resume the session from another supported surface' (What stays on your infrastructure)
- shared-persistent-sessions: a runner locks to one owner (a user account or a Claude Tag agent) at a time so checked-out code never mixes between owners; minimum fleet size equals active owners (Runner lifecycle)

## Key points
- Public beta, Team and Enterprise, off by default; unavailable under ZDR or HIPAA. Runner polls outbound HTTPS only; lease lapses after about 60 s without a poll and requeue can take 'a few minutes and sometimes longer'.
- A turn that outlives a host kill is lost; signal-less host kills look like crashes and the session requeues. Session identity can be verified from internal services via a session token (self-hosted-environments-identity page, not read).
- Inference still goes to Anthropic (or Bedrock/Vertex on the runner), and conversation content still goes to api.anthropic.com in all cases.
