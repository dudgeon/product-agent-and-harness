---
title: What is a Command Line Interface and why do they suddenly matter to product teams?
source_url: https://departmentofproduct.substack.com/p/what-is-a-command-line-interface
author: Rich Holmes
publisher: Department of Product (Substack, Knowledge Series, paid)
published: 2026-05-11
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-department-of-product-knowledge-series
themes: [pm-tool-connectivity, non-engineer-builders, status-update-agents, legible-org-for-agents]
relevance: medium
---

## Relevance to the project
Argues that CLIs are back because agents are text-native and live in the terminal, and teaches PMs to give Claude Code their Google Workspace through Google's Workspace CLI (`gws`), whose bundled workflows and skills include standup reports, meeting prep, email-to-task and weekly digests. For the project this is a third connectivity route beside MCP and APIs: a vendor-shipped CLI that bakes in recommended multi-step workflows and that a general harness can drive. It also frames a vendor CLI as "a distribution channel for the agent economy" (Stripe Projects, Spotify's Save to Spotify, Ramp's CLI). Company facts are second-hand from vendor posts and executives' social posts.

## Themes
- pm-tool-connectivity: hands-on section; `gws <service> <resource> <method>` maps one-to-one onto the Workspace APIs (Gmail, Drive, Calendar, Sheets, Docs, Chat, Meet, Forms and more); setup is a "fiddly" five-step auth flow the author got through by asking Claude Code for help (a globally unique project name was required).
- status-update-agents: "Prepare me for my day" reads calendar and inbox and prioritises; a chained instruction after a sprint review shares the recording, creates a task per action item and posts a summary to Chat in one request (four CLI operations).
- non-engineer-builders: claims CLIs are "now being rapidly adopted by non-engineers and product teams"; the method is to let the coding agent install and explain the CLI.
- legible-org-for-agents: "APIs vs CLIs": an API leaves conventions to the caller, while a well-designed CLI exposes the vendor's recommended patterns (naming, defaults, workflows) as commands an agent can just run.

## Key points
- **Why now:** GUIs optimise for human visual scanning; LLMs read and write text, and a CLI is text in, text out. Agents want deterministic, scriptable, composable interfaces, not onboarding flows.
- **CLI as technology and as product:** compared to how "API" names both a technology and a product with its own PMs.
- **Google Workspace CLI:** full Workspace API surface; workflow commands that make several API calls (standup-report, meeting-prep, email-to-task, weekly-digest, file-announce). The author also had it build a pre-mortem spreadsheet template in Sheets.
- **Stripe Projects (March 2026):** a CLI plugin that provisions and holds credentials for third-party services (Supabase, Clerk, Vercel, PostHog and others). The author reads it as Stripe betting on becoming the provisioning and credential layer agents route through by default. Primary source filed: [Stripe Projects](stripe-projects-dev-stack-from-terminal.md).
- **Spotify Save to Spotify:** a CLI that uploads generated audio as podcast episodes, built for agents (daily briefings, meeting recaps).
- **Ramp:** its CPO is relayed as saying CLI access to Ramp's API has "accelerated aggressively" (second-hand; Glass also ships with Ramp CLI connected, per [Seb Goddijn's article](x-sebgoddijn-glass-article.md)).
- **Roadmap questions for product teams:** which 3-5 frequent, repeatable workflows an agent should do; what an agent beside a power user would be asked to do in the background; what is hard about doing those via the API today (credentials, pagination, rate limits); what distribution you lose if a competitor ships an agent-first CLI first.

## Notable quotes
- "A CLI is, in a sense, a distribution channel for the agent economy."

## Could not verify
- Karpathy, Ramp CPO, Spotify CPO and Vercel CEO statements were embedded social posts, not present as text; not checked.
- The Google Workspace CLI's provenance and support status (official product or Google-org open-source project) is not stated in the post.
