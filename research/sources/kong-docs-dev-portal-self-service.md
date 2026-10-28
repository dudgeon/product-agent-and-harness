---
title: "Developer self-service and application registration (Kong Dev Portal)"
source_url: https://developer.konghq.com/dev-portal/self-service/
author: Kong
publisher: Kong Developer docs
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [onboarding-as-code, platform-onboarding-friction]
relevance: medium
---

## Relevance to the project
Shows how API-gateway onboarding encodes approval: developer sign-ups and application registrations need admin approval by default; auto-approval can be set portal-wide or per API, and everything is drivable through the Portal Management API. That is a policy knob (auto vs manual per API) a platform could tie to risk, and an API an agent can call.

## Themes
- onboarding-as-code: Konnect Portal Management v3 API creates and approves developers, creates applications, registers them to APIs, manages forms and publications; custom registration forms per portal.
- platform-onboarding-friction: "Developer sign ups and application creation require admin approval by default."; portal-level auto-approve overrides per-API settings.

## Key points
- App auth strategies: key-auth, OIDC, Dynamic Client Registration; user login: basic, OIDC, SAML with optional RBAC.
- Key-auth credentials cannot be created or imported automatically.
