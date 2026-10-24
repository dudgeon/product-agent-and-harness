---
title: "A better way to plan, build, and ship products | Ryan Singer (creator of \"Shape Up,\" early employee at 37signals)"
source_url: https://www.lennysnewsletter.com/p/shape-up-ryan-singer
author: Lenny Rachitsky (host), Ryan Singer (former Head of Strategy, 37signals; author of Shape Up)
publisher: Lenny's Podcast
published: 2025-03-30
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [opportunity-to-code-chain, agent-ready-intent, spec-edge-case-review, intent-factory-before-discovery, human-judgment-pm-jobs, artifact-standardization]
relevance: high
---

## Relevance to the project
Shape Up is a pre-AI method, but its "shaping" step is close to a working definition of what the film calls intent that is ready to ship: before any build time is committed, a small group (the PM who knows why, a designer, and the senior engineer "who actually knows where the bodies are buried") narrows the problem, sets an appetite (a time budget), and works the solution down to fewer than ten moving parts, opening the code to find hidden dependencies, until "we can give this to a technical person and they say, 'Yeah, I know what to go build now.'" That makes it a concrete, named option for intent-shaping-and-spec and a template for what an intent-shaping agent would need to produce: problem frame, appetite, breadboard of the flow, known rabbit holes resolved. Singer also says the dominant failure is "not enough detail", which cuts against the prototype-instead-of-spec pole. Lenny explicitly links the upstream shift of the PM role to AI doing the building (1:27:42). Evidence is the author's experience; he consults on the method.

## Themes
- agent-ready-intent: shaped work is not a PRD or Figma file and not a user story, but "the architecture with key components" as breadboards and fat-marker sketches that show flow and logic (44:23); test of done: a technical person says "I know what to go build now" (1:02:23); "If it's shaped well, you can usually describe it in less than 10 moving pieces" (42:21); after kickoff the build team should fit the work into about nine chunks (show notes).
- spec-edge-case-review: the "grumpy old plumber" engineer insists on opening the walls before quoting: "let's take a quick look at the code"; a fintech team's one-step onboarding change turned out to have three branches by partner bank, which shaping surfaces before green-light instead of in week four (50:42-53:47).
- opportunity-to-code-chain: demand side first (Jobs-to-be-Done research on where people struggle), then framing (narrow the problem; "calendar" becomes "see empty spaces"), then shaping (supply side: what can ship in the appetite), then a whole idea handed to a team that writes its own tasks (40:36, 1:38:37). Singer calls framing "the link to product strategy".
- intent-factory-before-discovery: the root cause of projects not shipping "is actually that the input at the very beginning of the process is too unclear" (1:38:37); "the dominant failure case that I see in the real world is always, again and again, not enough detail" (47:26).
- human-judgment-pm-jobs: in Shape Up the PM "moves upstream": less "project management" chasing builds, more understanding business context, narrowing the problem and negotiating with the CPO over which slice is worth a few weeks (1:26:10). Lenny: in an AI world "the bigger question now is like, 'What the hell should I build?'" (1:27:42).
- artifact-standardization: detail is a dial set by who is on the build team: more guidance for junior engineers, less for trusted senior ones; if a builder wants a say in the approach, bring them into shaping (47:26-49:00). Figma comes later, once "we already know where the sink is going" (59:52).

## Key points
- Three ingredients: appetite (work back from how much time it is worth; six weeks is a ceiling, not a cadence), shaping (vary scope inside the fixed time), and handing a whole shaped idea to a team rather than the Scrum "paper shredder" of 100 tickets (19:10-22:41).
- Appetite misuse: giving a team a vague big project with a six-week box is "just cruel"; "You can't put 10 pounds of crap in a five pound bag" (25:30).
- If a project won't finish, don't just cut scope or extend; take it "out of build mode and bring this back into shaping mode" (29:48-31:26). The original "circuit breaker" (cancel) is rarely stomached.
- Shaping sessions: about three hours, repeated two or three times for work on an existing stack; try to break each idea from technical and value angles; deliberately generate a very different alternative rather than polishing one (54:21-58:33).
- Works inside large companies team by team, e.g. a few teams at a pharmaceutical clinical-trials company of thousands, if a senior engineer untangles dependencies and protects the team's capacity (35:47).
- The method pays off at 30-50 people in product and engineering, or from "the first step away from the work" when a founder hands off to a PM (show notes; 1:25:26).

## Notable quotes
- "the dominant failure case that I see in the real world is always, again and again, not enough detail." (47:26)
- "it's shaped if we can give this to a technical person and they say, 'Yeah, I know what to go build now.'" (1:02:23)
- "the root cause is actually that the input at the very beginning of the process is too unclear" (1:38:37)

## Could not verify
- Transcript read 19:00-1:02:37, 1:25:00-1:28:00 and 1:38:20-1:42:00 in full; the rest (background, getting started, feature factories, Basecamp, second edition) skimmed via show notes. The episode barely mentions AI beyond Lenny's comment.
- Adoption examples (the pharmaceutical company, the fintech onboarding case) are unnamed and anecdotal. Singer consults on Shape Up adoption.
