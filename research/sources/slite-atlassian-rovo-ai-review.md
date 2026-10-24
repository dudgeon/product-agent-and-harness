---
title: Atlassian Rovo AI review (Slite)
source_url: https://slite.com/learn/atlassian-rovo-ai-review
author: Katerina Alexaki (Senior Account Executive, Slite)
publisher: slite.com
published: 2026-07-21
retrieved: 2026-10-24
type: article
evidence: anecdote
filed_by: research-pm-agents-jobs-to-be-done
themes: [agent-failure-modes, vendor-claims-vs-independent-evidence]
relevance: medium
---

## Relevance to the project
A competitor review (Slite makes a competing knowledge tool and says so: "Obvious disclosure first. We make Slite."), so opinion, not measurement. Its value is as a relay of concrete Rovo failure reports from Atlassian community posts (invented runbook steps, invented release information) plus one small own test. Relevant to the failure-mode and grounding questions for any PM agent. Audit 2026-10-24: original fetched in full and claims checked; the two community posts it cites did not render in fetch, and the Seibert-hosted partner write-up was fetched separately.

## Themes
- agent-failure-modes: A user team reported (Atlassian community post, relayed by Slite) a Rovo runbook summary with "troubleshooting steps, commands, and contact names that appear nowhere on the source page"; a partner reported a custom agent inventing releases for a date range with no data (case 1)
- vendor-claims-vs-independent-evidence: Author is a competitor to Atlassian (Slite employee, article ends in a demo CTA); treat as biased, though the relayed failures are concrete

## Key points
- Runbook failure: not Slite's own test; relayed from an Atlassian community question, https://community.atlassian.com/forums/Jira-questions/Rovo-Agent-hallucinating-runbook-summaries-fabricates-steps-not/qaq-p/3246298 (post body not fetchable; unverified beyond its title).
- Invented releases: Slite quotes a partner's community article, https://community.atlassian.com/forums/App-Central-articles/The-Making-of-Our-First-Rovo-Agent-and-the-Results-We-Didn-t/ba-p/3160646, as saying Rovo "created everything out of thin air with absolute confidence" (quote present in Slite; not confirmed in the community post, which did not render).
- The related partner write-up https://us.seibert.group/blog/rovo-agent-pitfalls ("Building Your First Rovo Agent – Common Pitfalls and How to Avoid Them", Yuri Kudyn, Co-Founder, Release Management Apps, 2025-12-18) was fetched: it does NOT contain "absolute confidence". Its wording: heading "Inventing Releases Out of Thin Air"; "Instead, it confidently invented releases." Other pitfalls it lists: no memory between chats, lost context on large inputs, miscounting work items, date confusion, slow responses, hard-to-test non-determinism. Fixes were temperature 0, chunking, computing counts and dates in the backend. Release Management Apps is a Marketplace app vendor: practitioner anecdote, not measurement.
- Slite's own small test: could not confirm Rovo consistently prefers a current page over a stale conflicting one; Rovo MCP returns candidate documents rather than answers. Single-corpus test, competitor-run.
- Slite also relays security reports (PromptArmor; Varonis "RovoBlast") on manipulating Rovo into exfiltrating data.
- Extra URL folded in (not from Slite; Slite does not mention outages): community thread "Rovo is currently not working", https://community.atlassian.com/forums/Rovo-questions/Rovo-is-currently-not-working/qaq-p/3207370, posted 2026-03-17 per search summary (page did not render). One thread, team-wide "We're not sure what went wrong" errors; a reply relays Atlassian support saying they "had some internal issues yesterday that have been resolved". Secondhand user report, not an Atlassian status incident.

## Could not verify
- The two Atlassian community posts Slite cites did not render in fetch; quotes from them are as relayed by Slite.
- Outage thread date and content are from search summaries only.
