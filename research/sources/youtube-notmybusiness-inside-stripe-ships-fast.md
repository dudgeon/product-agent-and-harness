---
title: An Inside Look Into How This $159B Tech Company Ships So Fast
source_url: https://www.youtube.com/watch?v=0Rqoe5quCJQ
author: Payton Kirol (host), Not My Business (Clay's media team); Stripe engineers on camera (Adam, Alex, Alicia, Michelle; PM "Romi")
publisher: YouTube, Not My Business
published: 2026-10-22
retrieved: 2026-10-24
type: video
evidence: first-party
filed_by: competitive-teardown-stripe-knowledge-agents
themes: [opportunity-to-code-chain, agent-factory-sdlc, legible-org-for-agents, tacit-knowledge-capture, human-review-gates, shared-persistent-sessions, non-engineer-builders, build-vs-buy]
relevance: high
---

## Relevance to the project
The first public look at **Orbit**, Stripe's planning layer above Minions, and the only video naming **Trailhead** (internal docs) and **Compass** (project tracking) as agent context. Orbit reads the codebase and Trailhead, writes a shareable plan teammates comment on, and hands it to a minion that may run 12 hours and pause to ask questions. A Stripe veteran's account of how tacit knowledge moved from "in our heads" to documents to robots is direct evidence for the context-creation hypothesis. Stripe-arranged access filmed by a vendor's media team: treat as first-party marketing.

## Themes
- agent-factory-sdlc: Orbit was built because "Minions were just unable to handle" larger, planned changes (06:00); "Gru" is the internal code-review engine that finds bugs better than people, tested against past problem changes (04:00-06:00).
- tacit-knowledge-capture: Michelle (joined 2013): small team "hold everything in our heads"; at scale "no one has all of the state in their heads anymore ... we start to write a lot of documents ... build robots to help answer questions ... with AI ... they can ingest all of this documentation that we'd written" (08:00).
- legible-org-for-agents: Orbit "is reading files in our code base, it's reading Trailhead, it's trying to understand how everything works" (12:00); Trailhead "a tool we built for internal documentation and finding what you need"; Compass tracks project progress; Kai can "read all the email lists for my team and tell me anything that stands out" (10:00).
- shared-persistent-sessions: Orbit plan is shareable; teammates annotate and comment before handoff; devbox activity shows up in Orbit as "one place to watch everything" (14:00).
- human-review-gates: deploys go to 1% of boxes, auto-pause and roll back on errors; mandated code review (06:00).
- non-engineer-builders: a PM and former engineer built a prototype CLI with internal tools, updated it between morning and afternoon UXR sessions; Stripe Projects launched in 7 weeks (16:00).
- build-vs-buy: built in-house because "we handle financial data ... we prefer building things in-house because we have the flexibility to impose better security" (12:00).

## Key points
- Orbit target: "individual engineers first"; many engineers lack time to experiment with Claude Code/Codex in parallel, so Stripe built shared agents everyone can use (12:00).
- Minion handoff: gets a devbox, the plan and extra instructions; "might go work for the next 12 hours"; pauses to ask for input when unsure (14:00). Engineers work on 3-7 projects in parallel.
- "AI still gets things wrong a lot of times, especially the details"; humans iterate the plan to make it simpler or reuse more (14:00-16:00).
- What takes effort now: "interfaces ... integration ... alignment with humans" (16:00).

## The whiteboard chain: Opportunity → Problem → Goal → Intent → Plan (→ code)
Added 2026-10-24 ("opportunity >> problem >> goal >> intent >> plan >> code").
- **What is on screen (about 12:24-12:31; frames read from the 360p stream, so handwriting is partly blurry):** Adam (Stripe engineer, revenue suite) has written on a whiteboard, top to bottom with hooked arrows:
  `Opportunity` → `Problem` → `Goal` → `Intent` → `Plan`.
  A curly brace spans **Problem and Goal** with a side label that reads as "**Customer conv[ersations]**" (legible: "Custome…" / "Conv…"; most likely "customer conversations", not confirmed). **"Code" is not written on the board.** It is the next step in the narration: the plan is handed to a minion that writes the code (13:40-14:40). So Geoff's six-step wording is the board's five steps plus the step the video shows next.
- **What is said over it (captions):** narrator, 12:22: "Adam explained once a team knows what problem it wants to solve, they need a plan for how to build it." Adam, 12:28, pointing at the lower steps (hand at Plan in the frames): "This is the part that today is happening a lot more in Orbit now." Narrator, 12:33: "So, Orbit isn't just where engineers can send agents like minions off to write code. It's a place where people can figure out what to build and how to build it, too."
- **Owners, hand-offs and artifacts as the video shows them** (my reading; Stripe does not label owners on the board):
  | Stage | Who does it at Stripe (per this video) | Artifact or hand-off |
  |---|---|---|
  | Opportunity | People: the team and leaders; not shown in any tool | none shown |
  | Problem, Goal | People, through customer conversations (the brace); the PM in the video also ran UXR sessions and revised a prototype between them (16:00) | Not shown; Kai, Harbor and Protodash support this step elsewhere (other notes) |
  | Intent | The engineer states it to Orbit ("Let's say I have a feature I want to build. I might know that there's a problem, but I might need to do some research"); Orbit reads the codebase and Trailhead in the background (13:30) | Prompt plus research in Orbit |
  | Plan | Orbit drafts; teammates annotate and comment; the engineer iterates "to get it to be simpler or reuse things" (14:00-15:30) | A shareable plan (seven steps in the demo) |
  | Code | A minion: one button "hand off the minion", gets a devbox, the plan and extra instructions, "might go work for the next 12 hours", pauses to ask for input (14:20) | Branch and PR; then review (Gru agent plus mandated human review) and a 1% canary deploy (06:00) |
- **Takeaway:** the agents at Stripe cover the bottom of the chain (intent research, plan, code, review). The top (opportunity, problem, goal) is still human and conversational. The brace marks customer conversation as the source for problem and goal: tacit knowledge that no Stripe tool shown captures.

## Could not verify
- Whiteboard label under the brace is only partly legible at 360p ('Custome… Conv…'); a higher-resolution stream could not be downloaded (YouTube blocked other formats). Timestamps for frames are from the downloaded file and match the caption times.
- Auto-captions: names are first names only; "Gru" rendered "Grew"; "Romi/Ramy" probably Rami Banna (author of the Stripe Projects post). No numbers on Orbit adoption.
- Sponsored-style content (Clay accelerator ad inside); Stripe chose what to show.

## Added 2026-10-24 (PDLC map)
- Orbit UI text read from a frame of the demo (~13:50): "Tip: Workspaces share context across sessions, all visible to each other." The demo question on screen: how the Treasury send-payout flow handles multiple payment methods such as SEPA.
