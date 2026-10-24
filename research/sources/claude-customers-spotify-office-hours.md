---
title: "Office Hours: Asynchronous coding and the end of the IDE with Spotify"
source_url: https://claude.com/customers/spotify-boris-office-hours
author: Anthropic (Boris Cherny, Creator of Claude Code, interviewing Niklas Gustavsson, Chief Architect and VP of Engineering, Spotify)
publisher: Claude (claude.com/resources)
published: unknown
retrieved: 2026-10-24
type: video
evidence: vendor-claim
filed_by: research-claude-resources-articles
themes: [non-engineer-builders, prototyping-agents-limits, human-review-gates, outcome-measurement-gap, legible-org-for-agents]
relevance: medium
---

## Relevance to the project
Spotify's chief architect reports 73% of PRs are AI-authored and that anyone, including non-engineers and the co-CEOs, can build an end-to-end prototype in the real mobile apps in an hour or two and share it through an internal prototype app store. For the project this is evidence that a company-wide prototyping substrate for PMs and designers is being built on top of engineering's agent infrastructure (Honk on the Claude Agent SDK), and that the enabling investments are test automation, verification and codebase standardisation rather than the agent itself. It also shows the outcome-measurement gap plainly: activity metrics are easy, while linking PRs to user value and revenue is still being built. All figures are the customer's own claims on an Anthropic page, unaudited.

## Themes
- non-engineer-builders: prototyping infrastructure aimed at "the non-engineering cohort"; prototypes from everyone "up to our co-CEOs" in an internal app store (closing segment).
- prototyping-agents-limits: prototypes run in real apps with real users and data within an hour or two, but "not every idea ships in an hour"; many need lots of exploration (deployments segment; closing segment).
- human-review-gates: owning teams were told they may no longer see automated PRs, which are auto-merged; this forced stronger test automation, now reused as the agents' verification (Honk architecture segment).
- outcome-measurement-gap: 75%+ improvement in PR frequency and 73% AI-authored PRs claimed; connecting PRs to work items, A/B tests and user value is "what we're trying to build right now" (ROI segment).
- legible-org-for-agents: standardisation of codebases, tools and frameworks, done for humans, makes agents work better; "if they look ten different ways, Claude is going to be more confused" (advice segment).

## Key points
- **Customer claims (unaudited):** 2,900 engineers; 73% of PRs AI-authored; 75%+ improvement in PR frequency attributed to AI tooling; about 4,500 production deployments a day; backend over 20 million lines of code; idea-to-production down to "an hour or something like that".
- **Honk.** Grew out of "fleet management" (automated migrations across thousands of repos, millions of merged PRs from deterministic scripts that hit a complexity ceiling). Now the Claude Agent SDK in a Kubernetes pod; before V2 tools were an allowlisted set, now users can add their own internal tools; it can run CI on Linux and macOS. Invoked also from Slack for general tasks.
- **Judge removed.** An LLM judge took PR success from roughly 20-30% to 80% in early iterations; Gustavsson says it was later removed because models and harness "caught up". Boris Cherny calls under-investing in the verification loop a common mistake.
- **Personal workflow.** 5-10 terminal tabs of Claude sessions in worktrees on large monorepos; no IDE since about two months after Opus 4.5. CLAUDE.md files needed iteration for internal tooling.
- **Prototyping for non-engineers.** Spotify built infrastructure for end-to-end prototypes in its mobile apps and backend plus an internal "app store" for sharing them; Figma-to-UI via simulator integration used for porting TV apps from iOS apps.
- **Quality.** Gustavsson says quality metrics are held "neutral" while speed rises significantly, and that this "does not come for free".
- **Limits:** a promotional conversation hosted by the vendor; no data on prototype-to-ship conversion, prototype quality, or who maintains prototypes; ROI to user value not yet measured.

## Notable quotes
- "There's a new actor in your code base, but the fundamentals seem to apply equally well." (Gustavsson, advice segment)
- "It allows you to test out an idea in a day instead of weeks or months." (Gustavsson, closing segment)

## Could not verify
- Publication date (the page gives none; it references Honk "V2" released "today" and Opus 4.5 "back in November/December").
- The independent InfoQ write-up of Spotify's QCon talk (`infoq-spotify-honk`) says the judge was dropped as too rigid with verification moved to a separate service; this page gives model improvement as the reason.
