---
title: Scaling Managed Agents (Anthropic engineering)
source_url: https://anthropic.com/engineering/managed-agents
author: Anthropic
publisher: Anthropic Engineering blog
published: 2026-04-08
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [meta-harness]
relevance: high
---

> Note rebuilt on 2026-10-24: the original note was lost before the project had version history. Only the Track 1 addendum below survived; the source should be re-read to restore Key points.

## Relevance to the project

Anthropic's own description of Managed Agents as a "meta-harness" over many harnesses, including Claude Code, dated 2026-04-08: the earliest first-party use of the term found.


## Added by Track 1 (meta-harnesses)
- Anthropic's own text calls Managed Agents "a meta-harness" that accommodates many harnesses, including Claude Code and task-specific harnesses. This is first-party use of the term, from the vendor of Claude Code, dated 2026-04-08, two months before Databricks used it for Omnigent. See [[meta-harness]].
- The session / harness / sandbox split is the architectural pattern a portable layer would have to keep stable; compare Cloudflare Project Think (durable fibers, tree sessions) in [cloudflare-project-think](cloudflare-project-think.md).
