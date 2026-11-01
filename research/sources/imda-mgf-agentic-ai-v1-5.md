---
title: "Model AI Governance Framework for Agentic AI, Version 1.5"
source_url: https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
author: Infocomm Media Development Authority (IMDA), Singapore
publisher: IMDA
published: 2026-05-20
retrieved: 2026-10-31
type: report
evidence: first-party
filed_by: research-agent-handoff-models
themes: [identity-delegation, regulatory-drivers-of-process, human-review-gates, agent-failure-modes]
relevance: high
---

## Relevance to the project
The most specific government guidance found on what an agent's identity and delegation record must hold: each agent unique and cryptographically verifiable, tied to a supervising agent, human or department, with "the different capacities in which an agent acts (e.g. independently or on behalf of a specified human user) ... recorded for auditability", and "delegations of authority ... clearly recorded" with the rule that a human cannot grant an agent more than the human holds. It is voluntary guidance from Singapore's regulator (not law), launched January 2026 and revised May/June 2026 with feedback from 60+ companies; it is the nearest thing to a regulator's checklist for an auditable agent handoff.

## Themes
- identity-delegation: "Unique ... cryptographically verifiable identity"; "Accounted for: This identity should be tied to a supervising agent, a human user, or an organisational department"; "Differentiated according to the capacity in which it acts"; "Catalogued and centrally managed" to prevent sprawl; authorisations "scoped, time- or session-bound, non-transferable", "Bounded by authorising human's permissions"; "Such delegations of authority should be clearly recorded" (pp. 23-24, "Agent identity").
- identity-delegation (gaps): current systems have "pre-defined, static scopes" and are "based on a single, unique individual", so they struggle "when agents act for multiple human users with different permissions, or recursive delegation scenarios where agents spin up multiple sub-agents" (p. 23).
- human-review-gates: "define significant checkpoints or action boundaries that require human approval" for high-stakes, irreversible ("sending communications, making payments"), outlier and user-defined actions; keep requests "contextual and digestible"; for high-risk actions require "an additional written justification"; audit oversight by tracking "Human override rate" (low may signal rubber-stamping) and "Human response times" (pp. 28-30); "Enforce human approval through system-level controls where possible, vs prompt-layer guardrails" (OpenClaw case study, p. 14).
- regulatory-drivers-of-process: "The organisations that deploy agents and the humans who oversee them remain accountable for the agents' actions"; establish "chains of accountability across the agent value chain and lifecycle" (section 2.2).
- agent-failure-modes: multi-agent risks added in v1.5: agent sprawl, miscoordination ("agents working on the same task may interpret the user's intent differently"), conflict, collusion; sharing context and intermediate outputs raises the chance sensitive data is "unintentionally logged, passed to less secure agents" (section 1.2.3).

## Key points
- Four dimensions: assess and bound risks upfront; make humans meaningfully accountable; implement technical controls and processes; enable end-user responsibility.
- v1.5 changes: controls and logging/monitoring added as core agent components; protocols updated (agentic commerce); systemic and multi-agent risks; 10+ case studies (PwC, Tencent and others); an IMDA OpenClaw case study.
- Technical-controls examples include per-agent identity tokens, scoped API keys, logging of tool calls and access history, and (vendor case) a hardware-attested "tamper-proof audit trail" of each step including blocked actions.
- Cites Microsoft Entra Agent ID, OAuth 2.1 in MCP, OpenID's agentic identity paper and the Cloud Security Alliance's agentic IAM proposal as emerging solutions.

## Notable quotes
- "Such delegations of authority should be clearly recorded." (p. 24)
- "Enforce human approval through system-level controls where possible, vs prompt-layer guardrails, which may be bypassed or 'forgotten'" (p. 14)

## Could not verify
- Nothing on retention periods or the minimum fields of an audit record; no agent-to-agent handoff record schema. Text extracted from the PDF with pypdf; page numbers are the document's printed numbers where visible.
