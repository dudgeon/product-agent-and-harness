---
title: "The coming AI security crisis (and what to do about it) | Sander Schulhoff"
source_url: https://www.lennysnewsletter.com/p/the-coming-ai-security-crisis
author: Lenny Rachitsky (host), Sander Schulhoff (AI security researcher)
publisher: Lenny's Podcast
published: 2025-12-21
retrieved: 2026-10-24
type: podcast
evidence: independent
filed_by: research-lennys-newsletter-archive
themes: [task-context-isolation, policy-enforcement-fail-open, agent-protocol-security, human-review-gates, identity-delegation, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
A prompt-injection researcher argues that guardrail products do not work against determined attackers, that the risk scales with what an agent can read and do, and that the practical defence is classical permissioning: assume the agent will be compromised and limit its data and actions. For a PM harness that reads untrusted inputs (customer feedback, emails, web pages, tickets) and can write to shared systems, this bears directly on trust-privacy-defaults, governance-control-plane and agent-identity-delegation. His most useful idea for the project is task-scoped permissions (Google's CAMEL): grant only the actions the user's request needs, which blocks injection in read-only tasks but fails when one task combines reading untrusted data with sending. He also doubts that per-action human approval will survive market pressure for agents that "just go and do stuff".

## Themes
- task-context-isolation: CAMEL "would look at my prompt" and grant only needed permissions, e.g. read-only for "summarize my emails", so an injected "send this to the attacker" cannot run; it fails when read and write are combined in one request ("read my recent emails and then forward any ops request") (1:04:24-1:07:28). Requires re-architecting; favoured by classical security people.
- policy-enforcement-fail-open: guardrails "do not work"; bypassable by determined attackers essentially all the time and "quite likely to make you overconfident in your security posture" (show notes; 1:27:24). Automated red teaming "works too well": every model breaks (30:14).
- agent-protocol-security: agents reading untrusted content are the exposure: a malicious email instructing the inbox agent to also forward to an attacker; an AI browser agent exfiltrating account data after visiting a page with hidden text (Comet cited, "probably all the AI browsers") (1:01:09-1:04:24). In his agentic red-teaming competitions, tricking agents was easier than eliciting CBRNE information (1:01:09).
- identity-delegation: "any data that AI has access to, the user can make it leak it. Any actions that it can possibly take, the user can make it take" (48:49); treat the agent like an untrusted employee and sandbox it (show notes). Example fix: run AI-written code in a container, not on the application server (52:54).
- human-review-gates: human-in-the-loop on suspicious actions is "great from a security perspective", but "what people want is AIs that just go and do stuff", so he expects that approach to fade (1:25:48-1:27:24). A useful counterweight to review-heavy harness designs.
- evals-autonomy-trust: log all inputs and outputs as standard deployment practice, for review and improvement, even though it is not a defence (56:19).

## Key points
- Jailbreaking (user versus model) versus prompt injection (attacker input into an application built on a model) (8:38).
- Risk tiers (45:11-1:01:09): (1) a read-only chatbot that only touches the current user's data needs no special defence; (2) make sure a "chatbot" really cannot take actions or reach others' data, which is a classical permissioning job; (3) truly agentic systems exposed to untrusted data sources are where injection matters.
- Claude Code cyber-attack case: attackers split a malicious goal into innocuous-looking requests across separate instances (16:34). ServiceNow agent issue mentioned (18:27).
- Most companies don't know what AI they run; security teams find more deployments than leadership knows (show notes).
- Recommends having an AI security researcher on the team, and people at the intersection of AI and classical security (50:21, 58:34). Advises against spending on multiple guardrails and automated red-teaming products; predicts a market correction in AI security vendors (56:19, 1:23:54).

## Notable quotes
- "You can patch a bug, but you can't patch a brain." (1:28:56)

## Could not verify
- Show notes and takeaways read in full; transcript read 15:01-19:44, 45:11-1:08:03 and 1:25:48-1:29:00; the rest (guardrail industry, adaptive evaluation, adversarial training, lightning round) skimmed by search.
- Competition results and the browser exfiltration case are described, not documented in the episode. The guest runs red-teaming competitions and education, so he has some stake, though he argues against buying security products; classed as independent.
