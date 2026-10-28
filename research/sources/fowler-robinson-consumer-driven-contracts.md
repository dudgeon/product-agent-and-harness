---
title: "Consumer-Driven Contracts: A Service Evolution Pattern"
source_url: https://martinfowler.com/articles/consumerDrivenContracts.html
author: Ian Robinson (Thoughtworks)
publisher: martinfowler.com
published: 2006-06-12
retrieved: 2026-10-28
type: article
evidence: anecdote
filed_by: research-dependency-agent
themes: [platform-onboarding-friction, legible-org-for-agents, dependency-knowledge-carriers]
relevance: medium
---

## Relevance to the project
The original statement of consumer-driven contracts: each consumer states what it actually uses of a provider's interface, and the provider's contract becomes the union of those expectations. The provider can then see which consumers depend on which elements and judge whether a change breaks anyone before making it. For a dependency agent this is a model of machine-readable dependency knowledge on the provider side: a registry of who depends on what, which is exactly what large organisations lack when a platform changes its API or deprecates a version.

## Themes
- legible-org-for-agents: consumer contracts make the hidden coupling between a service and its consumers explicit and checkable (section on consumer-driven contracts).
- dependency-knowledge-carriers: without them the provider "cannot see how consumers actually use its contract"; with them providers can deprecate elements while targeting specific consumers.
- platform-onboarding-friction: strict whole-schema binding forces consumers to redeploy in lockstep with the provider, burdening the enterprise "with services".

## Key points
- Provider contract: closed, complete, single, authoritative. Consumer contract: open, incomplete, multiple, non-authoritative. Consumer-driven contract: closed and complete, but driven by consumers.
- The pattern exposes coupling but does not remove it: "a breaking change is still a breaking change".
- It needs providers and consumers to agree channels and conventions, adding complexity; it is not an SLA.
- "A service is of value to the business only to the extent it is consumed."
