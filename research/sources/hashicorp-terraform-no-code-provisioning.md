---
title: "Provision no-code infrastructure (HCP Terraform)"
source_url: https://developer.hashicorp.com/terraform/cloud-docs/workspaces/no-code-provisioning/provisioning
author: HashiCorp (IBM)
publisher: HashiCorp Developer
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [onboarding-as-code, platform-onboarding-friction]
relevance: low
---

## Relevance to the project
Terraform's no-code modules are a platform team's published intake for infrastructure: the module's undefaulted input variables are the form, typed and validated, and provisioning starts on workspace creation. The intake schema is the module's variable block, readable by an agent; the human check is the optional manual-apply review.

## Themes
- onboarding-as-code: platform teams mark a private-registry module version "No-code Ready"; users supply variables without defaults, name the workspace, choose a project and apply method; types validated.
- platform-onboarding-friction: auto-apply is the default; manual apply requires an operator to confirm; module upgrades notify existing workspaces rather than auto-upgrading.

## Notable quotes
- "Terraform automatically starts a new run to provision no-code infrastructure upon workspace creation."

## Could not verify
- Sentinel/OPA policy checks on no-code runs and API support (not on this page).
