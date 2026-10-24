---
title: "Community Wisdom: Sharing Claude Code skills across the org, Why did lennysjobs.com shut down, opening an LLC for side work, AI for SMB sales, and more"
source_url: https://www.lennysnewsletter.com/p/community-wisdom-sharing-claude-code
author: Lenny's Newsletter community (Slack members); compiled by Kiyani
publisher: Lenny's Newsletter
published: 2026-04-18
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [skills-marketplace, skill-standards, meta-harness, compounding-context-repo, org-context-grounding, one-job-per-agent, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
The first thread asks the question the project's capability-distribution-trust dimension is about, from a roughly 50-person startup where product, engineering and go-to-market all use Claude Code daily: everyone builds skills locally and nobody can find or reuse them. Replies sketch the practical options and their costs: organization plugins, a Git-hosted plugin marketplace that only people with GitHub access can use, the maintainer burden of duplicates and naming, eval-gated skill changes, and one member's distributed custom agent harness (a Go "meta-harness" orchestrating opencode sessions with specialized roles) whose org documentation is served to every agent through an in-house MCP server rebuilt by CI. Anecdotal, but concrete on how distribution actually goes wrong for non-engineers. Bears on capability-distribution-trust, context-and-memory and harness-layering.

## Themes
- skills-marketplace: a team running a plugin marketplace says the downside is that "people have to have GitHub access to pull and editor access to contribute", so use is limited to product and engineering; managing it "is like an open source project": who can submit, how to handle duplicates "that have different flavors of the same goal", naming conventions (thread 1).
- evals-autonomy-trust: one member suggests a maintainer plus "skills have associated evals and any changes have to pass those evals" (thread 1).
- skill-standards: a reply explains the vocabulary for non-engineers: a marketplace is "just a 'bag of plugins'", a plugin can hold skills, agents and scripts, and a marketplace "is just a Git repository"; points to Anthropic's official and knowledge-work plugin marketplaces and project-scoped install so settings are visible (thread 1).
- meta-harness: one member's company distributes a custom agent harness, "a meta-harness that orchestrates dozens of simultaneous agent and sub-agent sessions" with specialized roles (plan, implement, code review, QA) "to implement a dark factory"; it is a Go app that orchestrates opencode, manages file-based handoff and context, has a TUI and a headless mode for CI (thread 1).
- compounding-context-repo / org-context-grounding: in that setup docs live in their repos; a GitHub Actions job updates a submodule ref in an engineering-docs repo, which triggers a rebuild and redeploy of an in-house MCP server that serves the docs as flat text, so "the next agent invocation across any individual/business function/CI run/etc. has the most up-to-date context" (thread 1). Doc-generation guidance sits in each repo's AGENTS.md, and teams can run the harness as a CI job to update docs from what changed.
- one-job-per-agent: custom agent profiles ship with the harness, each with its own prompts, MCP and context (thread 1).

## Key points
- The question's three sub-questions are exactly the open ones: where shared skills live (repo, built-in team skills, other), how non-technical teammates find and use them, and gotchas beyond a handful of power users. No reply answers the non-technical discovery problem well; the plugin path requires Git.
- Another member is "exploring Organization Plugins (bundles of skills)" for sharing and a single source of truth.
- Other threads (LLC advice, why a jobs site shut down, AI for SMB sales) are off-topic. A "top find" mentions a member's blunt reviews of 21 "AI-Native Product Manager" lightning lessons, kept inside the community.

## Notable quotes
- "It's like an open source project where you have to think about who can submit skills, how you deal with duplicates" (thread 1)
- "Could see a world where skills have associated evals and any changes have to pass those evals." (thread 1)

## Could not verify
- Community Slack thread; the custom-harness description is one member's account, with no write-up ("Unfortunately I don't [have one]"). Company names are not given.
- Off-topic threads read but not filed.
