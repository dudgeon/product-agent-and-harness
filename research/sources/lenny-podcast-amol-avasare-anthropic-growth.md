---
title: "Head of Growth (Anthropic): \"Claude is growing itself at this point\" | Amol Avasare"
source_url: https://www.lennysnewsletter.com/p/anthropics-1b-to-19b-growth-run
author: Lenny Rachitsky (host), Amol Avasare (Head of Growth, Anthropic)
publisher: Lenny's Podcast
published: 2026-04-05
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [agent-factory-sdlc, agent-led-intent-shaping, human-judgment-pm-jobs, pm-persona-role-expansion, prd-agents, spec-becomes-prototype-and-evals, metrics-review-agents, status-update-agents, legible-org-for-agents, org-context-grounding, risk-sloped-review, human-review-gates, evals-autonomy-trust, intent-factory-before-discovery]
relevance: high
---

## Relevance to the project
A first-party account of how one AI-native product org (Anthropic's roughly 40-person growth team) has redistributed PM work. Four points bear directly on the deck: (1) CASH, an internal system that runs the growth-experiment loop with Claude across four stages (find opportunities, build, test against quality and brand bar, analyse), each scored and hill-climbed as an eval, now at a junior-PM win rate on copy and small UI changes, with a human approving; (2) engineering leverage has outrun PM and design, so one PM effectively manages the output of 15-20 engineers, and Anthropic answers by hiring more PMs and deputising engineers as "mini PMs" for any project under two engineering weeks; (3) 60-80% of what ships has no PRD, with risk-sloped process (Slack for small, a 30-minute cross-functional kickoff with legal and safeguards for large); and (4) Cowork used to detect cross-team misalignment in Slack, a concrete agent job in the coordination layer he calls the real bottleneck. Bears on sequencing, intent-shaping-and-spec, review-and-autonomy, target-user and context-and-memory, and on the film's "bottleneck moved to intent" claim.

## Themes
- agent-factory-sdlc / agent-led-intent-shaping: CASH ("Claude Accelerates Sustainable Hypergrowth"), started "a couple of months ago", not workable before Opus 4.5, promising with Opus 4.6; four stages each evaluated and hill-climbed; "it ultimately prints money"; win rate like "a junior PM, two, three years in" (33:47-37:03). Lenny: AI is "getting really good at telling us what to do, not just taking our orders" (39:50).
- human-judgment-pm-jobs: the stage CASH can't do is "cross-functional stakeholder management"; "we will have AGI and it will still be impossible to get six people in a room to get to align" (head of design, 37:54). That is why he thinks PM work "is not going away" (37:31).
- human-review-gates / evals-autonomy-trust: humans approve CASH output today; he tracks week-on-week whether time spent per stage falls and results improve; brand review could move into "a skill that contains your brand guidelines ... dos and don'ts", so "the need to human review this really, really decreases" (38:48).
- pm-persona-role-expansion: a default team of five engineers, one designer, one PM; Claude Code makes the five behave like 15-20, so PM and design are "absolutely squeezed" (43:04). Response: hire more growth PMs, and if a project is two engineering weeks or less, "the engineer is on the hook to effectively be the PM", including security, legal and stakeholders; PM advises (45:00). Claude Code's PMs "are all basically engineers themselves anyway" (43:04). Small companies blend roles most; large orgs, "the jury is still very much out" (41:28).
- risk-sloped-review / spec-becomes-prototype-and-evals: "probably 70%, maybe 60, 70, 80% of what we ship does not have a PRD"; 20-30% important work gets good documentation; "PRDs are just outdated at this point" (51:29). Small work is kicked off on Slack; large work gets a 30-minute kickoff with "legal, ... safeguards, everyone in the room" (52:48). He prototypes to articulate ideas (51:29).
- prd-agents: when he does write a PRD, he uses a PRD skill plus a project holding all previous PRDs; sometimes just dumps thoughts into Cowork five minutes before a meeting (54:24).
- intent-factory-before-discovery: a PM with 20 engineers adds more by improving "the why and the what ... by 5%" than by shipping "the 21st PM feature" (47:52-49:30).
- metrics-review-agents: a Cowork scheduled task checks 20-25 Hex charts each morning (Chrome extension for some, MCP for others) and flags what's concerning; trust grows as false positives and negatives fall (59:17-1:00:20).
- status-update-agents / org-context-grounding: weekly scheduled Cowork run over Slack via the Slack MCP finds "areas of potential misalignment"; the enterprise lead found cases that "would've caused teams to spin their wheels significantly or do overlapping work" (55:35, 1:03:58). Also weekly manager feedback on direct reports from OKRs, transcripts and Slack, and a simulated-manager coach; quality "hit or miss", like "a coach who is kind of like drunk at times" (1:01:08-1:03:58). Setup needs an admin to enable the Slack MCP in team or enterprise orgs (1:06:01).
- legible-org-for-agents: everyone has a "notebook channel" (an internal feed) used to scale leaders' views; "it is something that goes to Claude"; some HR onboarding docs carry a warning to check with an owner before editing because "this is a document that Claude references as a key thing" (1:28:22-1:29:52). Legal has done enablement on setting up a Claude that mimics what legal would say (55:35).

## Key points
- Numbers (his and Lenny's): $1B ARR at start of 2025, about $4B mid-2025, $9B end of 2025, $19B by end of February 2026, "already out of date" (3:24, 10:13). Growth team about 40 people: horizontals (growth platform, monetization) plus audience pods (B2B, Claude Code, knowledge worker, API) (25:22).
- 70% of his time is "success disasters" firefighting (11:21). Big bets over micro-optimisation (70/30 or 50/50) because AI product value may be "100 to a 1,000x" in two years (26:11-29:00). The growth team built the Chrome extension that now underpins Cowork and Claude Code use cases (30:36).
- Capability overhang: by the time a team learns how to onboard users to a new model's capabilities, the next model can make the learnings irrelevant (15:19-16:49).
- Onboarding: friction that helps users see why the product is for them raises conversion (Mercury, MasterClass, Calm, Anthropic); Mercury's regulated onboarding (beneficial ownership, address types) was fixed with a quality-only quarter, his most impactful (18:57-20:28).
- Willing to forgo metric impact for safety, brand and quality; two classes of controversial test: red-line (don't run) vs run-if-high-conviction (1:14:12).
- Anthropic still uses Slack, Figma, Workday; builds some internal tools; "SaaS is dead" is partly overblown (1:30:58).

## Notable quotes
- "We will have AGI and it will still be impossible to get six people in a room to get to align." (37:54, quoting head of design)
- "If a project is two weeks of engineering time or less, then the engineer is on the hook to effectively be the PM for that." (45:00)
- "Probably 70%, maybe 60, 70, 80% of what we ship does not have a PRD." (51:29)
- "Your shipping in this world as bigger companies is going to be constrained often by all the cross-functional coordination." (1:03:58)

## Could not verify
- Full transcript read (about 1h52m); sponsor reads, the brain-injury story and lightning round read but not filed.
- CASH win rate is qualitative ("junior PM"); no numbers on volume, revenue impact or eval method. "Prints money" is his characterisation.
- The 2-3x engineer leverage (five behaving like 15-20) is his estimate, not a measured figure. ARR figures are public numbers as quoted in the episode (February 2026).
- Speaker is an Anthropic employee describing Anthropic products; vendor interest applies to the Cowork usage examples.
