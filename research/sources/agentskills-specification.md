---
title: Agent Skills specification (agentskills.io)
source_url: https://agentskills.io/specification
author: Agent Skills project (originated by Anthropic)
publisher: agentskills.io
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-agent-runtime-patterns-taxonomy
themes: [skill-standards, harness-portability, single-agent-many-skills]
relevance: high
---

## Relevance to the project
This is the format that the "portable skill" pattern rests on. It defines the small portable core (what any skills-compatible harness must read) and, by omission, everything that is left to each harness: how skills are triggered, which scripts can run, and which tools are allowed. It sets the ceiling on what a skill can carry without a runtime.

## Themes
- skill-standards: six frontmatter fields only (name, description, license, compatibility, metadata, allowed-tools); folder layout SKILL.md + scripts/ references/ assets/.
- harness-portability: `compatibility` field (max 500 chars) is free text for environment needs ("Designed for Claude Code", "Requires git, docker, jq, internet"), i.e. the spec itself admits harness/environment coupling; `allowed-tools` is marked Experimental and "support may vary between agent implementations".
- single-agent-many-skills: progressive disclosure keeps many skills cheap: ~100 tokens of metadata per skill at startup, <5000 tokens recommended for the body, resources loaded on demand.

## Key points
- Required: `name` (<=64 chars, lowercase/digits/hyphens, must match parent directory) and `description` (<=1024 chars, what it does and when to use it).
- Body has "no format restrictions"; recommended <500 lines, with detail moved to files one level deep.
- `scripts/` "supported languages depend on the agent implementation". There is no spec for script sandboxing, permissions, versioning or dependency management (`metadata.version` is only a free-form string).
- Reference validator: `skills-ref validate` (github.com/agentskills/agentskills).
- Overview page: format "originally developed by Anthropic, released as an open standard, adopted by a growing number of agent products"; client showcase at agentskills.io/clients.

## Could not verify
- Publication date of the spec page (not shown); adoption claims on the Client Showcase page were not fetched.
