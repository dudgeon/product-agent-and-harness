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

## Follow-up (2026-10-24): what the public Recipe Cookbook contains for product work
Filed by research-block-product-practices (PM-practice subagent). Read: the cookbook data directory https://github.com/block/goose/tree/main/documentation/src/pages/recipes/data/recipes (README and five recipe files) and https://goose-docs.ai/recipes/ (which renders client-side and showed only "Loading recipes...").
- The archived cookbook holds 46 recipe YAML files plus a subrecipes folder. Almost all are developer tasks (PR review per language, migrations, lint, test coverage, security audit, changelog, commit messages, the rpi-research/plan/implement/iterate chain, ralph loop).
- None is a PRD, spec, user-research, interview-synthesis, customer-feedback or roadmap recipe. The nearest to product work: `ab-test-framework-generator` (generates variant code, tracking, significance analysis and a dashboard; community author "scaler"), `data-analysis-pipeline` (CSV/JSON/Excel/Parquet to cleaned data, stats, charts and a markdown report), `daily-standup-report-generator` (GitHub PRs, issues and blockers into a dated `./standup/` file), `smart-task-organizer` (action items from files, emails and messages) and `pr-demo-planner` (turns a PR into a demo script and "business value" narrative; author "lifei").
- Themes: prd-agents (absence: no public PRD recipe from Block or the community), status-update-agents (standup generator), metrics-review-agents (data-analysis pipeline, A/B framework).
- The README confirms the submission programme ended; the cookbook "remains available as an archive". Authorship is mostly community handles, so these are not evidence of Block-internal PM practice.
