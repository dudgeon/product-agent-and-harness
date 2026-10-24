---
title: Recipes, Recipe Reference and Shareable Recipes (goose docs)
source_url: https://goose-docs.ai/docs/guides/recipes/recipe-reference
author: goose maintainers (AAIF)
publisher: goose-docs.ai
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-block-product-practices
themes: [one-job-per-agent, skill-standards, skill-supply-chain-security, org-learning-loop, work-structure-spectrum]
relevance: high
---

## Relevance to the project
Recipes are goose's unit of packaged task capability: a YAML file bundling instructions, prompt, typed parameters, required extensions, model settings, sub-recipes, a JSON output schema and shell-checked retries. They can be shared as links or files and scheduled. Read alongside skills ([goose-docs-using-skills](goose-docs-using-skills.md)), they show goose's split between always-available know-how (skills, hints) and launched task agents (recipes). Also read: the Recipes overview (https://goose-docs.ai/docs/guides/recipes/) and Shareable Recipes (https://goose-docs.ai/docs/guides/recipes/session-recipes).

## Themes
- one-job-per-agent: `settings` fix provider, model, temperature and `max_turns`; `sub_recipes` chain single-purpose steps; `response.json_schema` enforces structured output for automation (reference).
- work-structure-spectrum: Desktop-only `activities` (clickable prompt bubbles) versus headless `prompt`-driven runs and cron schedules (reference; scheduling).
- skill-supply-chain-security: first run of a shared recipe shows title, description and instructions and requires "Trust and Execute"; warning repeats only if the recipe changes; retry checks and `on_failure` are shell commands to review (shareable recipes; security).
- org-learning-loop: Recipe Library, `goose recipe deeplink` with pre-filled params, YAML export/import; recipients get their own session; memory, keys and credentials are excluded.
- skill-standards: recipes are goose-specific, unlike SKILL.md skills which are cross-harness.

## Key points
- Validation: every template variable needs a parameter; optional parameters need defaults; file parameters cannot have defaults; `goose recipe validate`.
- Retry: all checks must exit 0; on failure goose runs `on_failure`, resets history and restarts, up to `max_retries`.
- Scheduler: from the Recipe Library, background or foreground, frequency converted to cron; sessions created by schedules can be viewed or restored.
- The public Recipe Cookbook stopped accepting community submissions (per the 2025-10-08 cookbook-generator post, read too).

## Could not verify
- Whether Block runs an internal recipe library distinct from its skills marketplace.
