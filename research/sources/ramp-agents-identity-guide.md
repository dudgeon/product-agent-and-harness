---
title: "Agent identity (Ramp for Agents developer guide)"
source_url: https://agents.ramp.com/docs/guides/identity
author: Ramp
publisher: agents.ramp.com (Ramp developer docs)
published: unknown
retrieved: 2026-10-26
type: docs
evidence: first-party
filed_by: research-shared-persistent-agents
themes: [identity-delegation, agent-stewardship, shared-persistent-sessions]
relevance: high
---
## Relevance to the project
Ramp's own developer docs split agent identity into two models: an agent acting as the human who completed OAuth, and a business-owned "standalone agent" with its own credentials, explicitly granted permissions, and an accountable human owner. This is the clearest first-party statement found of how a session or agent can outlive the person who created it (catalogue item 9): only the standalone model decouples the agent from one person's access. It is a vendor's product doc, and the standalone model is in limited early access with no date, so it describes intent, not measured practice.

## Themes
- identity-delegation: two models side by side: "MCP and CLI actions run as the Ramp user who completed OAuth" (on-behalf-of, available now) versus a standalone agent that is a business identity with its own Client ID/secret (limited early access) (Identity models section; first-party, undated)
- agent-stewardship: every standalone agent must be assigned "an active human owner in the same business" who owns its setup and operation (Accountable owner section; first-party)
- shared-persistent-sessions: the user-model agent's continuity "Depends on the user's connection and access"; standalone agents have a lifecycle the business manages independently, so they are the model meant for background automation and shared company workflows (comparison table; first-party)

## Key points
- On-behalf-of model: permissions follow the connected user's Ramp permissions; suited to personal and interactive work.
- Standalone model: starts with minimal access; admins grant only what the job needs. Being added to an approval workflow does not by itself confer approval authority; the agent also needs the permission.
- Lifecycle: admins can pause access, rotate credentials or remove a standalone agent without affecting other identities.
- Attribution: supported standalone activity is attributed to the agent, not a person.
- The page does not say what happens to a standalone agent when its human owner leaves, nor what happens to a user-model agent when the user is offboarded.

## Notable quotes
- "MCP and CLI actions run as the Ramp user who completed OAuth."
- Continuity "Depends on the user's connection and access."

## Could not verify
- No publication date on the page; early-access status undated.
- The brief asked for a Ramp builders blog post titled "Agentic identity"; searches did not find one. This docs page is the closest Ramp primary source.
- Owner-departure behaviour is not documented.
