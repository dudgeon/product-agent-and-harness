---
title: WeChat opens the door to phone-based AI agents, on its own terms
source_url: https://kr-asia.com/wechat-opens-the-door-to-phone-based-ai-agents-on-its-own-terms
author: Cheng Zi (adapted from 36Kr, Wang Yuchan)
publisher: KrASIA
published: 2026-06-09
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [remote-agent-invocation, vendor-claims-vs-independent-evidence, identity-delegation]
relevance: medium
---

## Relevance to the project
Independent journalism on the largest named "A2A" deployment claim (WeChat with phone-maker assistants). It confirms agent-to-agent integrations between phone assistants and WeChat are being built, but does not name the protocol, so AAIF's claim that WeChat integrates "over A2A" is not independently confirmed as the LF A2A protocol. The design is instructive anyway: a platform owner prefers controlled agent-to-agent calls with dual authorisation over GUI agents that drive its screens.

## Themes
- `vendor-claims-vs-independent-evidence`: Article says "agent-to-agent (A2A) capabilities" and an "encrypted and controlled protocol", with no reference to Google's Agent2Agent or the Linux Foundation; contrast with [AAIF](aaif-a2a-joins-aaif.md).
- `remote-agent-invocation`: System assistants (Huawei Xiaoyi, Xiaomi Xiao Ai, Honor Yoyo, Vivo V, Meizu Aicy) parse intent and send instructions to WeChat's agent, which executes in the background (calls, messages) and returns the result.
- `identity-delegation`: "dual authorization: user authorization and app authorization".

## Key points
- Phone makers named: Huawei, Xiaomi, Honor, Oppo, Vivo. "Several manufacturers have already completed integration, according to the sources"; no public launch date.
- Context: Tencent blocked GUI phone agents (Doubao phone episode, December 2025); "Tencent may not accept GUI agents, but it can accept A2A integrations."
- Sources: unnamed Tencent sources via 36Kr, Martin Lau's Q1 2026 earnings call, FT report 2026-06-02.

## Could not verify
- Whether the protocol is LF A2A, Huawei's HarmonyOS agent protocol or something Tencent-specific; whether the feature is live. A Portuguese HDC 2026 report (search snippet only) says HarmonyOS supports "the A2A protocol, adopted by more than 150 organizations", which points to LF A2A on the Huawei side.
