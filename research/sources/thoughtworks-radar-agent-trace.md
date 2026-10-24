---
title: "Agent Trace (Thoughtworks Technology Radar Vol. 34)"
source_url: https://www.thoughtworks.com/radar/platforms/agent-trace
author: Thoughtworks
publisher: Thoughtworks Technology Radar
published: 2026-04-15
retrieved: 2026-10-24
type: report
evidence: independent
filed_by: research-agent-runtime-patterns-taxonomy
themes: [shared-persistent-sessions, harness-portability]
relevance: medium
---
## Relevance to the project
Independent assessment of Cursor's open Agent Trace spec for attributing code changes to humans vs AI and to the conversation that produced them. A candidate standard for auditability and transcript linkage across harnesses; rated Assess (early). Relevant to session storage/replay and 'who did this' audit.

## Themes
- harness-portability: vendor-neutral JSON trace record linking code ranges to contributor type (human/AI/mixed/unknown) and, per the spec's draft, to the originating conversation; works with Git, Mercurial, Jujutsu
- shared-persistent-sessions: Radar ring: Assess; support cited in Cline, OpenCode and a Git AI implementation

## Key points
- Spec itself (agent-trace.dev) is a 0.1.0-draft RFC from January 2026 per search snippets; backers named in a DeepWiki summary include Cognition and Cloudflare, not confirmed from the spec.

## Could not verify
- Spec text not read directly.
