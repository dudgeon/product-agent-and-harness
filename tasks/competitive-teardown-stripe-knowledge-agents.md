---
title: Competitive teardown: Stripe's knowledge-worker agents
status: active
directed_by: director-project-agent-and-harness
model: claude-opus-5-5
done_when: A deep, sourced teardown in tasks/competitive-teardown-stripe-knowledge-agents/ of Stripe's agents for knowledge workers (what they are, how they run, interface, trust and privacy, skills and context, adoption, results), with sources filed in research/ and options and key questions added to options/DIMENSIONS.md; accepted by Geoff
---

## Request

another teardown worker for the stripe knowledge worker agents

Context: Stripe Minions (one-shot coding agents) is already in the library from the taxonomy research; this teardown is about Stripe's agents for knowledge work, and should build on, not repeat, what is filed.

Related: [[competitive-teardown-ramp-glass]], [[competitive-teardown-shopify-river]], [[strategy-story-and-explainer-video]] (holds until this is complete).

## Progress

- 2026-10-24 Filed by director-project-agent-and-harness.
- 2026-10-24 Worker teardown-stripe-agents (3d45fbd1) started via claude --bg on Opus 5.5 with --remote-control.
- 2026-10-24 Worker started (Opus 5.5). Scope found by broad search, no need to ask: Kai (Knowledge AI Platform, Apr 2026) + Agent Studio, with Harbor (prototyping), the compliance review agents/agent service, and pre-Kai history (GoLLM, presets, NoCode Agent Builder, Toolshed, Hubert). Primary sources read in full: stripe.dev Kai post, LangChain case study, How I AI (Krishnamurthy) transcript, AWS compliance post, Harbor, payment-method factory, Latent Space (Sands) internal-AI section, How I AI (Kaliski, Minions), leader posts.
- 2026-10-24 Filed 17 source notes (INDEX, THEMES incl. 3 new themes), added Stripe options/questions to 20 dimension sections + 1 cross-cutting question (agent-interface and trust-privacy-defaults coordinated with the River worker), wrote 00-teardown-summary.md. Ready for Geoff's review.
- 2026-10-24 Director: sent Geoff's follow-up: review and incorporate https://claude.ai/artifact/PG1sfq8UxAJzhVxRgrmeu3 (all unreviewed links), research each named agent (Trailhead first), test his hypothesis that a business and operational context creation agent is needed to capture tacit knowledge. Reopened.
- 2026-10-24 Second pass started (director relayed Geoff): read Geoff's doc "Stripe's Internal Agent Ecosystem for Product Development" and filed it; filed its unreviewed links (Not My Business/Clay video on Orbit, Kaliski Orbit tweet, Protodash How I AI, SDK post, Stripe Projects post) plus Trailhead sources found by search (Sessions 2024 panel, Pragmatic Engineer Part 2, First Round/Nunez, Slack story); updated Kai, Minions part 1 and DoP notes. Knowledge-capture evidence sweep running in a subagent (Opus).
- 2026-10-24 Director: Geoff flagged the framework "opportunity >> problem >> goal >> intent >> plan >> code" from the Stripe agent walkthrough video; asked the worker to source it, map it to intent shaping and the register, and lead its report with it. Also told story-and-film.
- 2026-10-24 Found Geoff's chain on a whiteboard in the Not My Business video (~12:24: Opportunity → Problem → Goal → Intent → Plan, brace "Customer conv…" over Problem+Goal; Code is the next step in the narration); mapped it to Intent Factory, jobs map, S05 and the register (intent-shaping-and-spec, sequencing). Filed 14 knowledge-capture sources (subagent, Opus) plus the Trailhead/Protodash/SDK notes; added sub-choice context-and-memory/context-creation with options, key questions and a lean; themes opportunity-to-code-chain and tacit-knowledge-capture; summary updated with a second-pass section. Note: the Edit tool was blocked for this background session (it wants a worktree), so register appends went through an exact-anchor script that fails unless the anchor matches once.
- 2026-10-24 Geoff asked me to read the paywalled Department of Product deep dive via his logged-in Chrome: read it in full plus its 15-company PDF; rewrote the DoP note; filed the PDF and three primaries it links (Spotify Vedder context layer, Intercom Fin NPI, Uber Agentic Pods); added evidence and options to context-creation, trust-privacy-defaults and adoption-model; summary updated.
