---
title: "How Uber built an AI software factory for agentic coding: the MCP gateway and the platform underneath"
source_url: https://newsletter.port.io/p/how-uber-built-a-software-factory
author: Zohar Einy
publisher: Port newsletter (Substack)
published: 2026-08-24
retrieved: 2026-11-02
type: article
evidence: independent
filed_by: competitive-teardown-uber-cortana
themes: [agent-as-service-many-surfaces, agent-control-plane, vendor-claims-vs-independent-evidence]
relevance: low
---

## Relevance to the project
An independent-but-derivative retelling of the AI Engineer software-factory talk by the CEO of a developer-portal vendor, framed to promote Port; it adds no Cortana facts beyond the talk. Useful only as a cross-check of the talk's figures.

## Themes
- agent-as-service-many-surfaces: Cortana "shows up on Slack, the command line, and the web" with the context graph, skills and tools plugged in; teams personalise it in a team channel; 300 team-specific versions and 20,000+ sessions a day.
- agent-control-plane: LLM gateway with identity and auth first in the chain, under-100 ms guardrail budget, 20+ PII kinds stripped, an "AI guard" of five smaller models.
- vendor-claims-vs-independent-evidence: all figures relayed from the talk without verification.

## Key points
- Hand-off chain as retold: assistant → prototype → Minion → draft PR; inner loop checks before CI; PR arrives with a table of passed checks.
- "Balloon pods": pre-provisioned Kubernetes environments with snapshotted repos and built indexes.

## Could not verify
- No Cortana origin, permissions or visibility detail.
