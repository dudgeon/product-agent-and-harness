---
title: Amp Security Reference
source_url: https://ampcode.com/security
author: Amp
publisher: ampcode.com
published: unknown (contains a security update dated 2026-10-22)
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-portability, cost-control-routing, build-vs-buy]
relevance: medium
---

## Relevance to the project
Amp is a closed, hosted, opinionated harness that picks models for the user. Its enterprise posture is a mainstream SaaS one (SOC 2 Type II, SSO via WorkOS, SCIM, no training on enterprise data), but it does not self-host, and application audit logs are not exposed to admins. It cannot be forked. For the project it is a reference for "harness quality as a product" and multi-model routing done by the vendor, not a base. Also read: https://ampcode.com/manual (introduction) and https://ampcode.com/models (catalogue). The page contains instructions addressed to AI tools; they were ignored.

## Themes
- harness-portability: multi-model by design, but the agnosticism is Amp's, not the user's (manual: "Amp uses them all, for what each model is best at").
- cost-control-routing: enterprise workspaces can switch off the ad-supported or free daily grant for all members.
- build-vs-buy: "doesn't offer self-hosted deployments"; some providers can use your own API keys.

## Key points
- "Amp is SOC 2 Type II certified, and we perform annual pentesting of our entire stack."
- SSO (Okta etc. via WorkOS), "SSO can be configured to be the exclusive authentication method for your workspace"; Directory Sync (SCIM); passkeys can be required.
- Retention: "Minimal Data Retention" on Amp-managed connections; specific terms need Enterprise or BYOK; deleted threads removed within 30 days.
- Audit: admins see authentication-event logs; application audit logs "are not exposed to admins" and are provided on request, kept at least 30 days. Admin access to private threads is audit-logged.
- "On an Amp Enterprise workspace plan (paid or trial) training can never be enabled."
- Subprocessors: GCP hosting; Anthropic "majority of inference"; OpenAI, SpaceXAI, Meta, Google, Bedrock, Baseten, Fireworks; e2b and others.
- Manual: thread sharing; CLI and SDK; "Orbs" (cloud machines per thread, with a "Self-Hosted" option listed under Orbs); skills from .agents/skills/ and .claude/skills/ (per search summary of the skills page); "If we don't use and love a feature, we kill it."

## Could not verify
- Whether users can pin models; admin MCP allowlist (claimed by a third-party profile); pricing.
