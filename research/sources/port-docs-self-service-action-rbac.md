---
title: "Set self-service actions RBAC (Port)"
source_url: https://docs.port.io/actions-and-automations/create-self-service-experiences/set-self-service-actions-rbac/
author: Port
publisher: Port documentation
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [onboarding-as-code, decision-rights-for-agents, identity-delegation]
relevance: medium
---

## Relevance to the project
Shows how an internal developer portal encodes "who may request" and "who approves" for a platform's self-service action: execution can be limited to users, teams or the entity's owning team; manual approval can be required with ANY-or-ALL approvers; approvals are grantable via API. The `run_as` parameter lets a token act on behalf of another user, which is the hook an agent would use.

## Themes
- onboarding-as-code: permissions managed in UI or Terraform; per-action approval with specific users/teams as approvers, any-one or all must approve; runs wait until approved.
- decision-rights-for-agents: access can be granted to the entity's owners based on its Team property, linking decision rights to catalog ownership.
- identity-delegation: an organisation token can trigger an action on behalf of another user with `run_as`; approvals can be granted or declined through the API.

## Key points
- Notifications by email by default, or webhook (incl. Slack-formatted), or off.
- Run visibility per action: admins see all, approvers see assigned runs, members see their own.
