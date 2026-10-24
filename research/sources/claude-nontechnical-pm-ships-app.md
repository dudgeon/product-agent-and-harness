---
title: "How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks"
source_url: https://claude.com/resources/articles/how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks
author: Anthropic
publisher: Claude (claude.com/resources)
published: 2026-05-01
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [non-engineer-builders, pm-persona-role-expansion, one-job-per-agent, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A founder profile (Anthropic's "Day zero" series) of Kostiantyn Vlasenko, a project manager at Mythical Games with no prior coding, who built and shipped an iOS app with Claude Code and then began shipping features at his day job, which is evidence for the "PM becomes builder" role expansion and for the claim that managing people transfers to managing agents. It is a single, promotional anecdote from a hackathon winner: timings are inconsistent within the page and there is nothing on code quality, security review or maintenance. The more relevant detail for the project is the friction he reports at work, where some engineers struggled to give up "completely controlling every line of code".

## Themes
- non-engineer-builders: a project manager with a decade of experience shipped no code before February 2026, then shipped Respiro to the App Store with Claude Code ("The problem no app could solve"; intro).
- pm-persona-role-expansion: he now commits code releases and ships features at Mythical Games, and a small internal team there delivers work "entirely through Claude" ("Founder mode at work").
- one-job-per-agent: a self-built set of 15+ specialised subagents (TCA architect, Swift developer, Metal specialist, code reviewer and more) running in parallel across modules ("Managing agents like people").
- vendor-claims-vs-independent-evidence: Anthropic-published profile; user counts ("hundreds"), the 99% first-try rate and growth outcomes are the founder's own statements.

## Key points
- **Transfer claim:** he says his project management experience mattered more than coding skill; managing agents in the IDE felt like managing people.
- **Process:** first prompt was a vague "make me less stressed" app; then used Claude to research agent architectures and Apple APIs; pivoted from React Native to a Swift rewrite in a few hours when Android testing was impossible.
- **Non-code work:** used screenshots to have Claude guide him through Apple Developer Program, Meta API token and third-party setup (Sentry, Amplitude), claiming success first try "99 percent of the time"; Claude set up Amplitude funnels and retention metrics, wrote blog posts and suggested a practitioner-referral growth channel.
- **Roadmap:** the next release works from "a roadmap Claude helped him write".
- **Diffusion at work:** he shared his Claude folder and workflows with Mythical's engineers; most reportedly preferred it to their own; adoption friction from engineers' control instincts.
- **Timeline inconsistency:** the page says "in 72 hours", "A month later" live on the App Store, and "just under six weeks" from idea to App Store-ready version. Treat any one figure as loose.
- **Limits:** consumer side project, not an enterprise or regulated context; "project manager" (delivery role), not product manager; no review, testing or security practices described beyond a code-reviewer subagent.

## Notable quotes
- "It's hard for some engineers to switch the mindset of not completely controlling every line of code." (Kostiantyn Vlasenko)
- "I realized this was the same thing, only managing agents inside my IDE..." (Kostiantyn Vlasenko)

## Could not verify
- App user numbers, the subagent architecture, or what "delivering work entirely through Claude" means at Mythical Games.
