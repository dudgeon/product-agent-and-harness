---
title: a2a-sdk download statistics (pepy.tech), with GitHub and PyPI dependency checks
source_url: https://pepy.tech/projects/a2a-sdk
author: pepy.tech (data); measurements by this research round
publisher: pepy.tech, GitHub API, PyPI JSON API
published: 2026-10-24
retrieved: 2026-10-24
type: other
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, vendor-claims-vs-independent-evidence, agent-frameworks]
relevance: medium
---

## Relevance to the project
Usage signals not authored by the A2A project. Downloads are substantial in absolute terms but about 22 times lower than MCP's, include CI traffic, and arrive mostly as optional extras of agent frameworks, so they measure framework installs rather than agents talking to each other. Most implementations found are still on A2A 0.3, seven months after v1.0.

## Themes
- `vendor-claims-vs-independent-evidence`: a2a-sdk (Python): 89,472,507 total downloads, 12,198,490 in the last 30 days, latest 1.2.2 (2026-10-05), CI traffic included. `mcp` (Python, https://pepy.tech/projects/mcp): 2,522,364,654 total, 273,946,672 in the last 30 days, latest 2.3.0 (2026-10-02). Ratio about 22:1 over 30 days. An HN commenter who builds A2A packages cited about 10.9M vs 257M (about 24:1) in June 2026.
- `agent-frameworks`: PyPI `requires_dist` (checked 2026-10-24): google-adk 2.13.0 (`a2a-sdk>=0.3.4,<2` under extras `a2a`/`all`); strands-agents 1.62.0 (`a2a-sdk>=0.3.0,<0.4.0`, extra); crewai 1.15.30 (`a2a-sdk~=0.3.10`, extra); bedrock-agentcore 1.25.0 (0.3 under `a2a`, `>=1.0.1` under `a2a-v1`); Microsoft agent-framework-a2a 1.0.0b (`a2a-sdk>=1.0.0`). No a2a dependency in pydantic-ai 2.61.0 or langgraph-api 0.16.6 metadata.
- `remote-agent-invocation`: GitHub stars (2026-10-24): a2aproject/A2A 26,280; a2a-python 2,213; a2a-js 647; a2a-java 507. For comparison modelcontextprotocol/python-sdk 24,658; modelcontextprotocol/modelcontextprotocol 9,524. Spec-repo stars are comparable; SDK usage is not.

## Key points
- Version lag: AWS Strands and CrewAI pin A2A below 0.4; Atlassian's gateway, Gemini CLI's sample cards, Eon, and ServiceNow's current release are all on 0.3 (see the linked notes). v1.0 changed transport fields, so 0.3 and 1.0 peers need version negotiation or adapters.
- Earlier pepy snapshot in a search snippet (undated) showed 59.6M total and 14.7M per 30 days with 1.0.3 as latest, so monthly downloads have been roughly flat at 11-15M.

## Could not verify
- GitHub dependents counts (not available via API); downloads excluding CI; npm, Maven and NuGet figures.
