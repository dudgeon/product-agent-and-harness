---
title: "How the engineer behind Claude Cowork actually uses Claude | Felix Rieseberg (Anthropic)"
source_url: https://www.lennysnewsletter.com/p/how-the-engineer-behind-claude-cowork
author: Claire Vo (host), Felix Rieseberg (engineering lead, Claude Cowork and Claude Code Desktop, Anthropic)
publisher: How I AI (Lenny's Podcast Network)
published: 2026-05-25
retrieved: 2026-10-24
type: podcast
evidence: vendor-claim
filed_by: research-lennys-newsletter-archive
themes: [product-artifact-primitives, agent-as-service-many-surfaces, agent-led-intent-shaping, human-review-gates, org-context-grounding, harness-over-model, work-structure-spectrum]
relevance: medium
---

## Relevance to the project
The engineering lead for Cowork, Claude Code Desktop and Claude for Chrome explains, from the vendor side, why Claude has several entry points today and how its artifacts are evolving: Anthropic sorts users into three buckets (quick answers, deep meaningful work, engineering) and expects to collapse the tabs eventually; "live artifacts" refresh themselves from connectors, reusing the user's connector auth. Two framings matter for intent shaping: he reaches for the larger model when he "doesn't really know yet what they're asking for", treating reinterpretation of the request as the hard part, and he describes his own role as steering while the agent works asynchronously, judged on output rather than read line by line. The demos are personal (house floor plan, promise tracker, a $20 hardware approval button), so this is product philosophy and vendor framing, not evidence of enterprise PM practice.

## Themes
- agent-as-service-many-surfaces: "we live in this like super interesting time right now ... the time right before we all came up with the glass pebble as the correct shape for a phone" (4:05); more entry points into Claude exist because form factors are unsettled; the end state is likely "here's the one place where you do that"; today the tabs tell Anthropic whether you came for quick answers, "deep meaningful work", or engineering (4:05).
- product-artifact-primitives: an artifact is "some kind of file output from what you've been working on" (pages, PDFs, spreadsheets, presentations); a live artifact "refreshes itself with the latest data" via connectors, with a refresh button and reuse of connector OAuth so no API keys are pasted (23:46-25:51, 33:57-34:56). Example pain it targets: founders re-updating a pitch deck weekly for each investor.
- agent-led-intent-shaping: model choice heuristic: "I reach for opus over sonnet if I have self-identified as someone who doesn't really know yet what they're asking for" (10:11); professionals' real job is reinterpreting "what are you really trying to figure out" (10:11). Host summarises it as choosing by how well the problem is scoped, not technical complexity (11:41).
- harness-over-model: when Claude fails, "the learning I take away is not oh Claude can't do this ... I can maybe change a little bit the harness, the prompt" or the data source, or add a dry run (55:51).
- human-review-gates: a $19 microcontroller with a screen, flashed by Claude Code "in like a one shot", shows pending permission requests and approves them with a physical button; now exposed as an "open hardware buddy" in the desktop app's developer menu (47:01-51:51). Elsewhere he has stepped away "from actually supervising Claude too closely and really only judging it on its impact" (20:07).
- org-context-grounding: the impressive daily brief is not a calendar summary but "go figure out who I'm meeting with ... If it's a co-worker, go on Slack, figure out what kind of stuff they've been working on" (32:34); Claude "gets a lot more powerful ... if you ... give it context ... your emails your calendar" (13:57).
- work-structure-spectrum: "go one abstraction layer up": he stopped typing furniture dimensions, then stopped listing furniture, and had Claude find purchases in email (15:45); then ask how the system keeps itself current (18:06). A promise tracker reads his messages and keeps an SQLite database plus text files he has never inspected (18:06).

## Key points
- Cowork gives Claude "its own computer", a VM where it writes whatever software the task needs; from a floor plan it inferred scale from a garage permit and built an unrequested interactive 3D planner (12:26).
- Latency philosophy: help users "get comfortable with the idea that things are asynchronous"; "I will always trade off taking a little bit longer and giving you a better result"; getting people to stop watching the agent work "has more to do with trust than it has to do with patience" (42:59-45:30).
- Adoption gap (host and guest agree): the biggest gap is not capability but people knowing which problems to bring; Rieseberg compares it to Slack, which only paid off if teams changed how they communicated; "The biggest hurdle we have is how do we design the human model interface?" (37:46-41:05).
- Prompting tip: telling Claude "I know it's possible" increases its persistence on unusual tasks (30:31).
- Thumbs up/down feedback in Claude products "does end up on my desk" and is used in training and product improvement (57:35).

## Notable quotes
- "AI is used poorly if it just needs to move the mouse cursor for you." (45:30)
- "I reach for opus over sonnet if I have self-identified as someone who doesn't really know yet what they're asking for." (10:11)
- "this has more to do with trust than it has to do with patience." (45:30)

## Could not verify
- Transcript read 0:00-36:00 and 39:33-58:54 in full, the rest skimmed (dashboard design banter). Auto-transcription garbles product names ("Cloud", "Kobach" = Cowork).
- All demos used fake folders or demo accounts; the guest says his real use is similar. Statements about product direction (collapsing the tabs) are the speaker's personal view, not a roadmap.
- Evidence is vendor-claim: an Anthropic engineering lead describing Anthropic products.
