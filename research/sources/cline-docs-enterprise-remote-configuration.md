---
title: Cline Enterprise remote configuration, onboarding and prompt storage (docs)
source_url: https://docs.cline.bot/enterprise-solutions/configuration/remote-configuration/overview.md
author: Cline Bot Inc.
publisher: docs.cline.bot
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [build-vs-buy, harness-portability, human-review-gates]
relevance: high
---

## Relevance to the project
The most complete enterprise admin model of the open harnesses examined: WorkOS SSO with IdP role mapping, a hosted admin console that pushes provider, model, MCP, rules and skills policy to members, OpenTelemetry export, and "prompt storage" that copies full conversation transcripts to the org's own S3 or R2 bucket for audit. The weakness for a regulated setting is uneven enforcement: most controls bind only the VS Code and JetBrains extensions, not the CLI or desktop app, and the console is hosted at app.cline.bot. Also read: https://docs.cline.bot/enterprise-solutions/onboarding, https://docs.cline.bot/enterprise-solutions/monitoring/prompt-storage.md, https://cline.bot/enterprise, https://docs.cline.bot/llms.txt.

## Themes
- build-vs-buy: Enterprise needs a licence; cline.bot/enterprise says it runs "VPC, on-prem, air-gapped" with bring-your-own inference (Bedrock, Vertex, Azure OpenAI, self-hosted, local).
- harness-portability: admin-set providers include Anthropic, Bedrock, Vertex, OpenAI-compatible and LiteLLM.
- human-review-gates: Plan and Act with per-action approval by default (repo note); YOLO mode has an enterprise control page.

## Key points
- SSO via WorkOS (Okta, Azure AD, Google Workspace, SAML/OIDC); JIT provisioning; IdP Admin maps to Cline Admin; "All access management and revocation of users is currently handled by your IdP." SCIM not mentioned.
- Remote config delivered from the hosted console: "Configure providers once for the entire organization through the web-based admin console."
- Enforcement matrix: providers/models, MCP marketplace and member MCP servers, skills, telemetry, and blocking personal accounts enforced in VS Code and JetBrains only; rules and workflows also in the CLI; Cline Desktop enforces none of these. "The CLI and Cline Desktop don't enforce provider settings."
- Prompt storage: uploads api_conversation_history.json per task (all tool inputs and outputs, so file contents and command output) to the org bucket; retention set by bucket lifecycle; described as "a centralized repository for compliance, audit trails, and usage analysis". OTel events task.created, task.completed, task.conversation_turn, task.tokens.
- Remote config writes a copy into .cline/remote-config/ that "can include prompt storage access keys", so it must be git-ignored (a small but real leak risk).
- Named customer: Samsung Electronics DX division beta (press item, 2025).

## Could not verify
- Whether the admin console itself can be self-hosted (only the hosted service is described); app-level audit log of admin actions; pricing.
