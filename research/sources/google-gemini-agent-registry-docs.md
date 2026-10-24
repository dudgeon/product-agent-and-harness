---
title: Agent Registry (Gemini Enterprise Agent Platform docs)
source_url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry
author: Google Cloud
publisher: docs.cloud.google.com
published: 2026-10-22
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, capability-distribution-trust, remote-agent-invocation]
relevance: medium
---

## Relevance to the project
Shows what an agent registry concretely holds in Google's stack: agents, MCP servers, tools, skills (preview) and endpoints, with bindings that connect an agent to downstream MCP servers and auth providers, governed by IAM per project. The registry is a catalog plus binding layer, not a runtime. Useful as a reference design for a registry of intent-shaping agents and skills.

## Themes
- agent-control-plane: "central hub for governance, discovery, and search for your AI ecosystem".
- capability-distribution-trust: standalone skills can be registered (preview), alongside MCP servers and tools.
- remote-agent-invocation: registered A2A agents; endpoints define destinations agents may connect to; IAM egress policies (`roles/iap.egressor`).

## Key points
- Automatic registration from supported runtimes; manual registration for custom deployments and custom ADK agents.
- Bindings link source agent to MCP servers, endpoints and auth providers; managed declaratively with Terraform.
- Release notes (secondary search) list Agent Registry GA in June 2026 and "semantic governance policies" entering public preview late June with a dry-run mode.
- The page does not mention audit logging or cross-cloud (non-Google) agents.

## Notable quotes
- "Register agents automatically from supported runtimes or manually for custom deployments."

## Could not verify
- GA date and semantic-policy preview come from search snippets of release notes, not read directly. Retrieved via WebFetch (model-summarised view).
