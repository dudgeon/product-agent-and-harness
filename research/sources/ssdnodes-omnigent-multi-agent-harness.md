---
title: "Omnigent: one harness for many agent CLIs"
source_url: https://www.ssdnodes.com/learn/omnigent-multi-agent-harness
author: Matt Connor (Founder & CEO, SSD Nodes)
publisher: SSD Nodes Learn
published: 2026-10-12
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, harness-portability, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A recent, detailed self-hosting guide by someone with no stake in Omnigent (but a commercial interest in selling VPS hosting). Its value is the release-history reading and an explicit "I would not" list, which maps onto what a regulated trial must check. It does not say the author ran Omnigent; treat its setup steps as documentation-based.

## Themes
- [[meta-harness]]: frames Omnigent as supervising installed vendor CLIs as child processes, versus a framework where your program is the agent; connector layers solve "what an agent can reach", Omnigent "which agent runs, in what order, under what limits".
- [[harness-portability]]: switching vendor is a one-line YAML change to `harness` and `model`; but the YAML spec on `main` documents features (e.g. `acp:<slug>`) absent from v0.7.0, and the spec should not be treated as stable across minor versions.
- [[vendor-claims-vs-independent-evidence]]: "The project says alpha, and the release history above shows it means alpha"; two releases removed or renamed commands earlier guides documented. Notes ~10.8k stars and ~685 open issues on 2026-10-12, cautioning stars are not maturity.

## Key points
- Sandbox: bubblewrap + seccomp on Linux praised, but it does not cover MCP servers or the supervisor itself.
- Each sub-agent adds its own process; sizing guidance is for the supervisor alone.
- Telemetry added in v0.6.0 and on by default; read the telemetry page before client work.
- "I would not" list: run it on a host with production credentials; run unattended without a cost budget; expose it publicly without auth and TLS; treat the YAML spec as stable across minor versions.
- Cost of the layer: every Omnigent bug sits between you and an agent that used to work on its own.

## Notable quotes
- "The cost is the layer itself."
- "Every bug in Omnigent is now a bug sitting between you and an agent that used to work on its own."
- "I would not run it on a host that holds production credentials"

## Could not verify
- Whether the author ran the steps; the article does not say so.
