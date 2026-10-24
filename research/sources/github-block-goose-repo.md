---
title: Goose (block/goose) repository
source_url: https://github.com/block/goose
author: Block / Agentic AI Foundation
publisher: GitHub
published: unknown
retrieved: 2026-10-24
type: other
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [agent-frameworks, harness-portability, build-vs-buy]
relevance: medium
---

## Relevance to the project
Open-source general-purpose agent (Apache-2.0, Rust, MCP extensions, custom distributions) now under the Linux Foundation AAIF. It is the base Stripe forked for its Minions, so it is the best-evidenced "fork an open harness" example. Complements the existing Goose podcast note.

## Themes
- agent-frameworks: desktop app, CLI and embeddable API; 70+ MCP extensions; 15+ providers or subscriptions via ACP.
- build-vs-buy: supports custom distributions with preconfigured providers, extensions and branding.

## Key points
- Rust; Apache-2.0; about 55.6k stars; part of the Agentic AI Foundation at the Linux Foundation (GOVERNANCE.md present).
- Recipes folder exists; not explained on the page.

## Could not verify
- Governance details and recipe semantics not read.

## Follow-up (2026-10-24)
Filed by research-runtime-patterns-follow-up-round. Read: https://github.com/aaif-goose/goose (README), GOVERNANCE.md and CUSTOM_DISTROS.md in the same repo.
- **Repo moved** to the aaif-goose organisation (search summaries date the move 2026-04-07; not confirmed on the page). Apache-2.0; about 55.6k stars, 6.4k forks, 5,882 commits at retrieval. Description: "an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM". 15+ providers (Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock) and ACP connections to existing Claude, ChatGPT or Gemini subscriptions.
- **Governance (GOVERNANCE.md, first-party):** "Founded by Block and now stewarded by AAIF (Agentic AI Foundation)"; a Series of LF Projects, LLC, which must approve governance changes. Maintainers and 3-7 Core Maintainers; consensus first, Core Maintainer majority vote if stalled; major changes need an issue, one week of review and majority approval. Tie-breaker named: "goose's creator, Bradley Axen". Membership "tied to individual contributions, not employer affiliation". Trademark ownership not stated (points to LF Projects policies). Contributors keep copyright; code Apache-2.0, docs CC BY 4.0.
- **Why the foundation (secondary):** The New Stack, "Why Block handed Goose to the Linux Foundation" (https://thenewstack.io/block-goose-agentic-foundation/), body could not be fetched; search summaries quote Manik Surtani (ex-head of open source at Block, now AAIF CTO) that Block's ownership of the trademarks and opaque governance were the main obstacle to enterprise adoption. Treat as unverified until the article is read.
- **Custom distributions (CUSTOM_DISTROS.md, first-party):** a documented white-label path: preset provider/model and credentials (incl. MDM-injected keys), bundled internal MCP servers, custom providers, edited system prompts (crates/goose/src/prompts/system.md), branding, and YAML recipes with sub-recipes and subagent settings. Must keep licence notices, mark modifications and not imply goose trademark endorsement. It recommends upstreaming generic changes because "heavily diverged forks" are costly and miss security updates. Example audiences include a legal research assistant, i.e. a non-coding distribution is an intended use. No named company examples.
- **Enterprise controls:** none built in beyond configuration (no SSO, audit or admin console in the project; those would be the distributor's job). The docs list an extension allowlist (not read).
- Skills support filed separately: [goose-docs-using-skills](goose-docs-using-skills.md).
