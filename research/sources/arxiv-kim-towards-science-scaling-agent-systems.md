---
title: Towards a Science of Scaling Agent Systems
source_url: https://arxiv.org/abs/2512.08296
author: Yubin Kim, Ken Gu, Chanwoo Park, ... Daniel McDuff, Xin Liu (Google Research, Google DeepMind, MIT)
publisher: arXiv (cs.AI)
published: 2025-12-09
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: research-agent-handoff-models
themes: [relay-information-loss, work-structure-spectrum, single-agent-many-skills, verification-capacity-gap]
relevance: high
---

## Relevance to the project
The largest controlled comparison of a single agent against four multi-agent topologies on the same tasks. It finds multi-agent coordination helps decomposable, parallel work (centralized +80.8% on Finance-Agent) and hurts sequential planning (every variant -39% to -70% on PlanCraft), returns diminish once a single agent passes about 45%, and topologies without a central verifier amplify errors more (17.2x independent versus 4.4x centralized). Intent shaping and dependency mapping are largely sequential, interdependent reasoning, which this result bears on directly.

## Themes
- relay-information-loss: multi-agent systems "impose intrinsic information fragmentation"; global context must be compressed into inter-agent messages, which is lossy; a single agent keeps one memory stream.
- work-structure-spectrum: gains depend on task structure more than agent count; parallelisable tasks benefit, sequential ones do not.
- single-agent-many-skills: capability saturation (beta -0.404, p < 0.001 above a ~45% single-agent baseline); tool-heavy tasks suffer from multi-agent overhead (beta -0.267).
- verification-capacity-gap: centralized verification contains error amplification (4.4x versus 17.2x for independent agents).

## Key points
- Architectures: single agent; independent (parallel, aggregated without cross-checking); centralized (orchestrator, hub-and-spoke messages, verifies before aggregating); decentralized (peer debate rounds); hybrid.
- v2 (2025-12-17): 180 configurations, four benchmarks (Finance-Agent, BrowseComp-Plus, PlanCraft, Workbench); mixed-effects model cross-validated R^2 0.524; picks the best architecture for 87% of held-out configurations. v3 (2026-04-08): 260 configurations, six benchmarks, three LLM families; abstract reports R^2 0.373 (0.413 with a task-grounded capability metric).
- Decentralized helped web navigation (BrowseComp-Plus +9.2% vs +0.2% centralized).
- Evidence label: independent research by Google authors, not about a Google product.

## Could not verify
- v3 body not read (numbers above from v2 body and v3 abstract); error taxonomy section not read.
