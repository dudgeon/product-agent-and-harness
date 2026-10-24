---
title: "Agent harness design: 3 patterns for harnessing Claude's intelligence"
source_url: https://claude.com/resources/articles/harnessing-claudes-intelligence
author: Lance Martin (member of technical staff, Claude Platform team, Anthropic)
publisher: Claude (claude.com/resources)
published: 2026-04-02
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-claude-resources-articles
themes: [harness-over-model, memory-architecture, single-agent-many-skills, enterprise-admin-controls, cost-control-routing]
relevance: high
---

## Relevance to the project
Anthropic's own rule for harness design is to keep the harness thin and re-test it with each model: lean on general tools the model already knows (bash, a text editor), let the model orchestrate, manage and persist its own context, and promote only security-, UX- or audit-relevant actions to dedicated typed tools. It sharpens the project's harness-over-model theme: a harness matters, but each piece encodes an assumption about model weakness that goes stale, so harness upkeep includes deleting parts. It also gives a concrete criterion (reversibility) for where a harness should put hard boundaries, which bears on governance in a regulated setting.

## Themes
- harness-over-model: "agent harnesses encode assumptions about what Claude can't do on its own, but those assumptions grow stale"; context resets added for Sonnet 4.5's "context anxiety" became "dead weight" with Opus 4.5 ("The future of agent harness design").
- memory-architecture: prefers model-chosen persistence (compaction, a memory folder of files) over retrieval infrastructure; Opus 4.6 Pokémon memory: 10 organised files and a learnings file versus Sonnet 3.5's 31 transcript-like files (Pattern 2, "Let Claude persist its own context").
- single-agent-many-skills: skills as progressively disclosed context (frontmatter preloaded, body read on demand) rather than hand-crafted task prompts; subagents used when Claude decides to fork a fresh context (Pattern 2, "Let Claude manage its own context").
- enterprise-admin-controls: promote actions to dedicated tools when the harness needs a typed hook to gate, render or audit; hard-to-reverse actions such as external API calls can require user confirmation (Pattern 3, "declarative tools").
- cost-control-routing: cache rules: static content first, append updates as messages, don't switch models mid-session (use a subagent for a cheaper model), use tool search instead of changing the tool list (Pattern 3 table).

## Key points
- **Pattern 1, use what Claude knows:** Claude 3.5 Sonnet hit 49% on SWE-bench Verified with only bash and a text editor; skills, programmatic tool calling and the memory tool are compositions of those two tools.
- **Pattern 2, ask what you can stop doing:** let Claude write code to chain tool calls so intermediate results skip the context window (BrowseComp, Opus 4.6: 45.3% to 61.6% with self-filtered tool outputs); let it load skills on demand and edit stale context out; subagents added 2.8% over the best single-agent run on BrowseComp; compaction let Opus 4.6 reach 84% on BrowseComp where Sonnet 4.5 stayed at 43%; a memory folder lifted Sonnet 4.5 from 60.4% to 67.2% on BrowseComp-Plus.
- **Pattern 3, set boundaries carefully:** the Messages API is stateless so the harness repackages context each turn; cached tokens cost 10% of base input. A bash tool gives the harness only a command string; a dedicated tool gives typed arguments it can intercept, gate, log and replay. Write tools can include a staleness check. Tools can also render a question as a modal and block the loop for user input.
- **Auto mode as an alternative boundary:** a second Claude judging bash command strings can reduce the need for dedicated tools, but only "for tasks where users trust the general direction"; dedicated tools still earn their place for high-stakes actions.
- **Limits:** all numbers are Anthropic benchmarks of Anthropic models; nothing on enterprise policy, identity or multi-user concerns; the advice assumes the builder controls the harness.

## Notable quotes
- "Over time, the structure or boundaries in our applications should be pruned based the question: what can I stop doing?" (closing section)
- "Promoting actions to dedicated tools gives the harness an action-specific hook with typed arguments it can intercept, gate, render, or audit." (Pattern 3)
