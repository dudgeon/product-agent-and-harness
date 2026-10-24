---
title: "Claude Skills explained: How to create reusable AI workflows"
source_url: https://www.lennysnewsletter.com/p/claude-skills-explained
author: Claire Vo (host)
publisher: How I AI (Lenny's Podcast Network)
published: 2025-10-22
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [skill-standards, prd-agents, harness-portability, single-agent-many-skills]
relevance: low
---

## Relevance to the project
A solo "mini episode" from launch week of Anthropic's Agent Skills (October 2025), in which the host (founder of ChatPRD, a PM-tool vendor) explains what a skill is and builds PM-flavoured skills: a PRD generator, a changelog-to-newsletter skill and a demo-notes-to-follow-up-email skill. It adds little beyond the skills sources already filed, so relevance is low; its value is as an early practitioner's view of the authoring and distribution friction (a skill is "a folder", zip upload to the web app, naming errors, the built-in skill creator over-generating files) and of skills as the unit of a reusable PM workflow. Bears on capability-format-portability and capability-distribution-trust.

## Themes
- skill-standards: a skill "is a folder" with a SKILL.md (YAML name and description used for discovery, Markdown instructions) plus relative-linked resources and optional Python scripts; she found the docs unclear on what the asset is: "primitives built by engineers expected to be grokked by everyday people" (6:16-9:26).
- prd-agents: the Claude.ai skill creator's PRD skill included a decision tree, a long template, several PRD formats and clarifying questions to ask the user, which she says she wouldn't have written herself (12:36-14:09).
- harness-portability: the same folder works in Claude Code locally or zipped and uploaded to Claude.ai; she authored skills in Cursor (faster, about three minutes) by pointing it at the docs, then invoked them from Claude Code (16:08-20:15). Upload failed first on a naming rule (lowercase, hyphenated) (24:47).
- single-agent-many-skills: skills are invoked by inference from context, with no magic word; pasting a changelog was enough to trigger the newsletter skill (20:15). She contrasts skills (on-demand, task-specific) with Projects and custom GPTs (always-on, general context) (1:38).

## Key points
- Prefers natural-language skills over "if this, then that" workflow builders (3:12).
- Bundled scripts give consistent behaviour where model-generated code would vary (6:16); Cursor added a validation script she found "a little bit overkill" (23:16).
- Built-in skill creator in Claude.ai produced 12 files where five were needed, and download failed (14:09-15:43).
- Recommended setup: a local "Claude Skills" folder or repo, a skill that creates skills, revise each skill as output drifts (e.g. too many emoji) (21:45).

## Could not verify
- Transcript read in full. Reflects October 2025 product behaviour; the upload flow, naming rules and skill creator have likely changed since.
- Host is a PM-tool vendor; the episode is sponsored by her own product.
