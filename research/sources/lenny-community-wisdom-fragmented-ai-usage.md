---
title: "Community Wisdom: Managing fragmented AI usage across teams, avoiding generic UX when building with AI, tracking funnel metrics at the pre-PMF stage, thoughts on Anthropic's Cowork, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-managing-fragmented
author: Lenny's Newsletter community (members-only Slack), compiled by the community team
publisher: Lenny's Newsletter
published: 2026-01-17
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [org-learning-loop, shared-persistent-sessions, enterprise-admin-controls, compounding-context-repo, outcome-measurement-gap, enablement-by-product, agent-control-plane, memory-architecture]
relevance: medium
---

## Relevance to the project
A community thread names the team-level problem a PM harness would solve: AI use is fragmented across personal ChatGPT and Claude accounts, prompts and small projects never get shared, there is no visibility into usage against policy, and "most value today accrues to individual power users, not teams". Replies show the workarounds people actually use (a shared file space with Claude Code or Codex, an internal MCP registry, internal chat with usage tracking, Slack channels and learning labs) and the gap that remains ("unified memory layer across the assistants is still absent"). It bears on session-persistence-sharing, governance-control-plane, context-and-memory and adoption-model. Cowork reactions show PMs saw it as productizing their Claude Code + Obsidian "personal OS" hacks, but worried that a separate tool fragments sharing further. All evidence is anecdote from community members.

## Themes
- org-learning-loop: original post: "Useful prompts, experiments, and even small projects live inside someone's personal ChatGPT or Claude and never get shared. Over time it feels like we're losing a lot of learning" (thread 1).
- shared-persistent-sessions: people share "the final artifact but not the prompts, iterations, dead ends, or how they got there. That might be why tools for collaborative AI are so rare" (thread 1, original poster follow-up).
- enterprise-admin-controls: the poster wants per-task model choice, usage-based pricing and enforceable policies; the company "AI usage doc in Notion ... is basically advisory"; a smaller business says OpenAI usage reporting is only for large orgs; one company blocks non-approved apps via IT content filtering and runs "an internal implementation of chat that can use different models where we can track usage" (thread 1).
- agent-control-plane: one respondent's stack: "Unifying the underlying intelligence layer across the org with Claude Code", an "Internal MCP registry" connected to Cursor, Claude Code, Claude and ChatGPT, and an internal MCP for prompt rewriting and style enforcement (thread 1).
- memory-architecture: same respondent: "unified memory layer across the assistants is still absent"; outputs are exported to Google Docs, GitHub or Notion and unified through Claude Code (thread 1).
- compounding-context-repo: a PM uses Claude Code with a shared file space for the team (his team uses Codex) "so everyone can access the same data and everything is properly persisted"; keeps a "master context folder with product strategy"; another wants "a working shared context of our insights, research, PRDs" that anyone can take to any tool, e.g. "an LLM-friendly markdown file of your customer profile" (thread 1).
- outcome-measurement-gap: "we've failed to make an outcome-based argument for using it more fully"; also "Context sharing is broken": folder-based agents handle text, chat LLMs handle binaries but are "walled-garden creators" (thread 1).
- enablement-by-product: the shared-folder PM says his setup "took me 6 months to figure out" and weeks of hand-holding to teach friends; "It's not about the setup ... What is much more important and much more difficult is how to actually utilize and manage the context effectively"; he is sceptical of "Cursor for PM" products (thread 1).

## Key points
- People-side practices reported: weekly internal AI newsletters showcasing custom GPTs; hackathons; an "AI Lab" Slack channel with a club every two weeks and a contest for best experiments; biweekly learning-lab workshops; a 6-8 person cross-org AI working group running workshops, mentorship, tools and curriculum (thread 1).
- MCP cost: one member calls MCP-based context sync "really expensive"; another says Notion and Drive have direct, free integrations (thread 1).
- Cowork reactions (thread 5): "a game changer for non-technicals"; a member says Anthropic built it after observing "PMs and creators using Claude Code + Obsidian and the like as their personal OS" and productizing it; another questions making it a separate tool because "when everyone is working in different tools, it's hard to share things" and asks how skills and marketplaces carry over; claims it was built "in 1.5 weeks" and that early UI "needs more work" (citing a ChatPRD review).
- Design-prompt thread (thread 3): members keep a "universal design prompt" as a Markdown file or Cursor/Claude Code rule; one exports Magic Patterns prototype code into the coding agent's context. Minor relevance to prototyping.
- Threads 2 (sales enablement) and 4 (pre-PMF funnel metrics) are not relevant to the project and are not summarized.

## Notable quotes
- "Most value today accrues to individual power users, not teams" (thread 1, original poster).
- "Slack is still where the tea around tools, prompts and techniques break" (thread 1).

## Could not verify
- All claims are individual community members' reports; company names and sizes are mostly not given. The "1.5 weeks" Cowork build time is a member's relay, not sourced in the thread.
