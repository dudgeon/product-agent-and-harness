---
title: Introducing Gemini Enterprise Agent Platform
source_url: https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform
author: Google Cloud
publisher: Google Cloud Blog
published: 2026-04-22
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, identity-delegation, agent-frameworks, non-engineer-builders]
relevance: high
---

## Relevance to the project
Google's full-stack answer: build (low-code Agent Studio, code-first ADK), run (Agent Runtime, Sessions, Memory Bank, Sandbox), govern (Agent Identity, Agent Registry, Agent Gateway) and optimise (evals, simulation, observability), with the employee-facing Gemini Enterprise app as the delivery surface. Unlike Microsoft's governance-only Agent 365, this bundles runtime and governance in one cloud. Claude models are available in Model Garden, so a Claude-based intent-shaping agent could run here, but under Google's runtime, not Claude Code's harness.

## Themes
- agent-control-plane: "Govern" pillar of Agent Identity, Agent Registry, Agent Gateway ("air traffic control"), anomaly detection and security dashboard via Security Command Center.
- identity-delegation: "every agent receives a unique cryptographic ID".
- agent-frameworks: ADK code-first plus Agent Garden templates; "programmatic interface" lets coding agents build, evaluate and deploy agents.
- non-engineer-builders: Agent Studio low-code builder; agents delivered to employees in the Gemini Enterprise app.

## Key points
- Launched at Next '26; replaces Vertex AI ("now delivered only through Agent Platform").
- Runtime claims: sub-second cold starts, multi-day workflows; Memory Bank long-term memory.
- Model Garden 200+ models including Anthropic Claude Opus, Sonnet, Haiku. Partner agents can be governed through the registry and gateway.
- Named customers: Burns & McDonnell, Color, Comcast, Geotab, Gurunavi, L'Oréal, Payhawk, PayPal. No outcome data.
- No pricing or industry-specific compliance claims in the post.

## Notable quotes
- "Agent Identity improves the security posture of your agents by ensuring every agent receives a unique cryptographic ID."
- "Agent Gateway acts as the air traffic control for your agent ecosystem."

## Could not verify
- Whether Gemini Enterprise app can host or govern an external harness such as Claude Code (not stated). Retrieved via WebFetch (model-summarised view).
