---
title: "Understanding Cross App Access with Okta for AI Agents"
source_url: https://support.okta.com/help/s/article/understanding-cross-app-access-with-okta-for-ai-agents
author: Okta
publisher: Okta Support
published: 2026-06-08
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [identity-delegation, decision-rights-for-agents, scoped-governance-containers]
relevance: high
---

## Relevance to the project
Okta's Cross App Access (XAA, the ID-JAG grant) moves the decision "may this agent reach that app for this user?" from per-user OAuth consent prompts to admin-defined policy in the enterprise identity provider. For a regulated org, that is the realistic shape of agent access to internal platforms: the IdP holds a directional "managed connection" from agent to resource app, and the agent exchanges its ID token for an access token under that policy.

## Themes
- identity-delegation: the agent uses an Identity Assertion Authorization Grant (ID-JAG) flow to exchange its ID token for an access token to the resource app (Flow).
- decision-rights-for-agents: "Okta moves complex Open Authorization (OAuth) consent flows away from end users and into the Admin Console"; admins define which apps can access which.
- scoped-governance-containers: access is a directional managed connection between a requesting app and a resource app.

## Key points
- Applies to Okta Identity Engine; page updated 8 Jun 2026.
- Secondary sources: XAA was added as an official MCP authorisation extension (Enterprise-Managed Authorization, Nov 2025); Microsoft Entra can also issue ID-JAGs; "Okta for AI Agents" governance product GA April 2026; sources disagree on licensing.

## Could not verify
- Audit/visibility features (not on the page; page showed a loading error banner).
