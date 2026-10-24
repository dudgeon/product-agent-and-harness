---
title: "Agent Card Poisoning: A Metadata Injection Vulnerability in the Systems using Google A2A Protocol"
source_url: https://keysight.com/blogs/en/tech/nwvs/2026/03/12/agent-card-poisoning
author: Keysight (author not stated)
publisher: Keysight blog
published: 2026-03-12
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-protocol-security]
relevance: low
---

## Relevance to the project
Shows that an Agent Card is untrusted text that ends up in the caller's prompt: a malicious remote agent embeds instructions in its card, and the host LLM follows them. Same class as MCP tool-description poisoning. Keysight sells security test tooling (CyPerf), so it has a product interest but none in A2A adoption.

## Themes
- `agent-protocol-security` (proposed): Card metadata "treated as authoritative planning input rather than inert metadata"; in a simulated hotel-booking delegation the host POSTed the full booking payload, including payment card data, to an attacker endpoint before the legitimate delegation.

## Key points
- Simulation with a host agent holding `http_get`, `http_post`, `delegate_task`, `execute_python`; evidence from packet captures.
- Implied mitigation: strict separation of card content from instructions. Our inference, not stated by Keysight: signed cards would not help here, since a signed card from a malicious agent is still malicious.

## Could not verify
- Date taken from the URL path; author not shown; no named framework or SDK tested.
