---
title: "My LLM codegen workflow atm"
source_url: https://harper.blog/2025/02/16/my-llm-codegen-workflow-atm/
author: Harper Reed
publisher: harper.blog
published: 2025-02-16
retrieved: 2026-10-31
type: article
evidence: anecdote
filed_by: research-agent-handoff-models
themes: [process-artifacts-as-coordination, docs-as-code-prd, work-structure-spectrum]
relevance: medium
---

## Relevance to the project
A widely cited practitioner account of exactly the sequential-session relay in model A: one chat session hones an idea into spec.md, a reasoning model turns the spec into prompt_plan.md and todo.md, and separate execution sessions (Claude, Aider) work through the prompts while todo.md carries state. It names where it breaks: it is a solo workflow; with more than one person or agent "The bots collide, the merges are horrific, the context complicated."

## Themes
- process-artifacts-as-coordination: spec.md feeds planning; prompt_plan.md supplies execution prompts; todo.md is checked off so work resumes across sessions.
- docs-as-code-prd: the spec (requirements, architecture, error handling, testing plan) is committed to the repo before any code.
- work-structure-spectrum: greenfield gets the full spec-plan-execute chain; brownfield is planned per task.

## Key points
- Each stage uses a different model and a different session; the person carries files between them and is the router.
- Failure notes: moving faster than you can track ("over my skis"), default-stack bias, copy-paste friction, idle waiting, and multi-person collisions.
- Self-dated: "will probably not work in 2 weeks, or it will work twice as well."

## Could not verify
- No measurement; one practitioner. Model-summarised fetch.
