---
title: Google Cloud Next 2026 wrap-up
source_url: https://cloud.google.com/blog/topics/google-cloud-next/google-cloud-next-2026-wrap-up
author: Google Cloud
publisher: Google Cloud Blog
published: 2026-04-24
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A negative signal from A2A's originator: Google's own wrap-up of Next 2026 (hundreds of announcements, 1,302 customer stories referenced, 70+ marketplace agents) does not mention A2A or Agent2Agent once, and none of its named customers is described as having agents talk to another vendor's agents. Its customer numbers are about deploying many agents inside one platform (GE Appliances 800+ agents, Tata Steel 300+), which is the intra-platform pattern, not cross-vendor A2A.

## Themes
- `remote-agent-invocation`: Interop items are Agent Gateway ("secure, unified connectivity between agents and tools across any environment"), Agent Registry, Bring Your Own MCP, and the Agent-to-UI protocol (A2UI). Agent Gallery and Agent Marketplace list partner agents (Accenture, Adobe, Atlassian, Deloitte, Oracle, Palo Alto Networks, Replit, S&P Global, Salesforce, ServiceNow, Workday); the wrap-up does not say they connect over A2A.
- `vendor-claims-vs-independent-evidence`: Customer stories (Capcom, Citi Wealth, Deutsche Telekom, GE Appliances, Home Depot, Macy's, Merck, Unilever, Vodafone Business and others) describe their own agents; none describes cross-vendor agent traffic.

## Key points
- Agent Gateway partners for securing agentic traffic: Broadcom, Check Point, Cisco, CrowdStrike, F5, Netskope, Okta, Palo Alto Networks, Ping Identity, Zscaler and others ("In preview soon").
- Wiz agent studio support lists AWS AgentCore, Gemini Enterprise Agent Platform, Copilot Studio and Agentforce, i.e. security vendors treat these as the agent platforms to watch.

## Could not verify
- Whether Agent Gallery partner agents are A2A agents. Gemini Enterprise release notes ([note](gemini-enterprise-release-notes-a2a.md)) show A2A agent registration GA on 2026-08-17 and Marketplace A2A agents, which suggests they are, but this page does not say so.
