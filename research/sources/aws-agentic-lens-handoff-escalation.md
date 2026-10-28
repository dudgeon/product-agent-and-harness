---
title: "AGENTOPS01-BP02 Design multi-agent handoff procedures with human-in-the-loop escalation (AWS Well-Architected Agentic AI Lens)"
source_url: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops01-bp02.md
author: Amazon Web Services
publisher: AWS documentation
published: unknown
retrieved: 2026-10-26
type: docs
evidence: vendor-claim
filed_by: research-shared-persistent-agents
themes: [human-review-gates, agent-protocol-security, one-job-per-agent, agent-failure-modes]
relevance: medium
---
## Relevance to the project
AWS's prescriptive guidance treats an agent handoff as "a data contract before it is a workflow step": a versioned context package (task description, completed work, memory artifacts, handoff reason) travels with every handoff (catalogue item 3), and escalation to a human is a separate, instrumented trigger (low confidence, high stakes, exhausted retries) from agent-to-agent routing (item 8). It also names the silent failure of agents waiting on each other. Vendor guidance (it promotes AgentCore and Agent Registry) without outcome data, but the anti-patterns list is a ready checklist.

## Themes
- human-review-gates: "Agent-to-human escalation happens when confidence drops below a threshold, the stakes are high, or the retry budget has been exhausted"; mixing it with routing "sends too many routine tasks to humans (creating fatigue and bottlenecks)" or too many high-stakes ones to automation (Implementation guidance)
- agent-protocol-security: structured context package schema, versioned "so receivers can reject malformed handoffs"; MCP and A2A named as the shared vocabulary (Implementation steps 2)
- one-job-per-agent: agent-to-agent escalation is "a routing decision" for capability mismatch; a registry catalogues which agents exist and whether they accept work now (guidance)
- agent-failure-modes: "Deadlocks deserve their own attention because they are silent"; "A deadlock that requires a human to notice is a deadlock that lasts until someone notices" (guidance)

## Key points
- Anti-patterns: handoffs without context packages force re-derivation; no agent-to-human triggers; no deadlock/timeout handling; not tracking handoff success rates.
- Metrics to track: handoff latency, context-transfer completeness, collaboration success rate.

## Notable quotes
- "A handoff is a data contract before it is a workflow step."

## Could not verify
- Page undated; no evidence of measured outcomes.
