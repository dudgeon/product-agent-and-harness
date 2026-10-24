---
title: Ramp built an AI agent harness in six weeks — and LangChain's CEO says it's part of a bigger shift
source_url: https://thenewstack.io/ramp-laminar-agent-harness/
author: Amanda Caswell
publisher: The New Stack
published: 2026-10-22
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: competitive-teardown-ramp-glass
themes: [build-vs-buy, harness-over-model, cost-control-routing, agent-factory-sdlc]
relevance: high
---

## Relevance to the project

Independent trade-press coverage (with the usual caveat that it relies on Ramp's own blog post) of Laminar, Ramp's in-house agent harness that now runs Glass, Inspect and customer-facing agents. It materially changes the Glass picture: the April 'built on the Claude Agent SDK' account is superseded by a model-agnostic Ramp harness by October. It also carries an independent data point on routing inside the harness (LangChain's Open SWE experiment). Central to the loop-source, harness-layering and model-provider-coupling dimensions.

## Themes

- **build-vs-buy**: Ramp tested managed agent APIs, open-source frameworks and third-party platforms, then built Laminar in six weeks; 'We studied the other offerings on the market and decided that we could do better, move faster, and have stronger alignment ... by building in house' (Sam Kronick). The article notes Ramp has published no operating-cost comparison, so whether in-house is cheaper is unknown.
- **harness-over-model**: Model independence and observability (a built-in trace debugger) were the stated reasons; the harness is where routing, sandboxing, approvals and async run.
- **cost-control-routing**: LangChain's Open SWE router: median LLM cost per thread $2.61 to $0.94 (-64%) across 973 threads with no significant change in merged-PR rate; argues routing belongs in the harness, not a generic gateway. Ramp was not in that experiment.
- **agent-factory-sdlc**: 'Laminar runs everything from customer service agents to Ramp Inspect ... and Glass, which handles longer-running, collaborative work.'

## Key points

- Architecture (as reported): sessions stored separately from sandboxes ('sandbox-as-a-tool'; credentials and orchestration stay outside the sandbox); async/non-blocking agents by default; a Connectors Service centralising auth, credentials, access control and tool execution behind one API; own observability/debugging UI.
- Build: V1 in six weeks; 'agents generated all of Laminar's initial code, with experienced engineers guiding'. daily.dev's summary of the Ramp post adds: Postgres, Temporal, S3, disposable cloud workers; tested OpenAI Agents SDK, Claude Agents SDK, Claude Managed Agents API, OpenCode, LangChain, Sierra; 'five months later, every agentic product at Ramp runs on Laminar, serving tens of millions of sessions'; code written with Opus 4.7 and GPT 5.5.
- Maintenance caveat raised by the author: Ramp still needs engineers for incidents, upgrades and product-team support.
- Disclosure: TNS's owner is an investor in LangChain.

## Could not verify

The original Ramp post ('Building Laminar: Ramp's Managed Agents Platform', builders.ramp.com, Oct 20, 2026, by Sam Kronick) has since been read and filed as [ramp-builders-building-laminar](ramp-builders-building-laminar.md). 'Tens of millions of sessions' and the tested-tools list come from daily.dev's summary of that post.

