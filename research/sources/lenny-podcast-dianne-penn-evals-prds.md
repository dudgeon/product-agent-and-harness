---
title: "Anthropic's first technical PM on token maxing, the jagged edge, and living in the future | Dianne Penn"
source_url: https://www.lennysnewsletter.com/p/anthropics-first-technical-pm-on
author: Lenny Rachitsky (host), Dianne Penn (Head of Product, AI Research and Labs, Anthropic)
publisher: Lenny's Podcast
published: 2026-07-26
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-lennys-newsletter-archive
themes: [spec-becomes-prototype-and-evals, evals-autonomy-trust, human-judgment-pm-jobs, pm-job-stable-methods-change, org-learning-loop, human-review-gates, outcome-measurement-gap]
relevance: high
---

## Relevance to the project
The clearest first-party statement from inside a lab of "evals are the new PRDs": Anthropic's research PM team treats a small set of prompts with golden answers (30 to 40 to start) as the main artifact for turning vague user pain into something researchers can act on and measure. It is careful, though: PRDs survive for aligning large groups (engineering, legal, safety) and for ambiguous zero-to-one bets, so this is evidence for "spec plus evals" rather than "evals replace specs". It bears on intent-shaping-and-spec (what the handoff artifact is), pm-agent-evaluation, and on which PM jobs stay human (judgment, sign-off). Caveat: her team's "users" are researchers and her product is a model, so the eval-as-spec pattern may transfer only partly to ordinary product teams.

## Themes
- spec-becomes-prototype-and-evals: "we actually have a saying on the team of evals are the new PRDs" (41:00). The eval is described as "a personification of that user need". But PRDs persist: every model gets a PRD as a source of truth for product surfaces, engineering, legal and safety, and PRDs stay useful for ambiguous bets like computer use where no concrete pain points exist yet (48:03-49:35). Lenny notes the Codex app lead (Andrew Ambrosino) said the same: "PRD's not dead" (49:39).
- evals-autonomy-trust: capabilities arrive discontinuously ("jagged"), so "unless you have the evals ... these jumps might actually happen and you don't know" (17:53). Products sit "at the intersection of models with harnesses, with a set of contexts for a set of users", so evals matter beyond model teams: "you can't improve what you can't measure" (46:54).
- outcome-measurement-gap: worked example of turning vague feedback into a measurable signal. Early complaints that Claude "was not good at following instructions" were dug into; about 80% turned out to mean malformed JSON; 30-40 failing examples became the eval set; it now scores 99.9-100% on every model and is no longer a pain point (44:29-46:07).
- human-judgment-pm-jobs: judgment is "accumulation of so much nuance and so much experience" models have not had; choosing which of the many buildable things to build stays human (1:12:09). Closing claim: we need more user-centric PMs, not fewer (1:22:13).
- pm-job-stable-methods-change: hiring loop unchanged for three years (40:04); the job is the same (user value) but the artifact changed (PRD to eval) and user research moved from watching pixels to reading model transcripts: "sweat the tokens as much as you sweat the pixels" (42:32).
- human-review-gates: for standardized writing such as a monthly business review, she wants Claude to write it end to end via a skill while she is "a reviewer and a verifier"; "who's signing off" matters more than who wrote it (1:01:38, 1:08:29).
- org-learning-loop: early Anthropic tested models in a company-wide Slack channel, "working in public internally"; within about 10 requests on a shared idea, a use case would emerge; "experimentation is not always necessarily an individual sport" (20:37-22:55, 54:06).

## Key points
- Transcript-reading as the new user research (29:50, 42:32): vague feedback ("Claude hallucinated") is not actionable for researchers. The team reads consented trajectories and classifies the failure (wrong tool call, right document but wrong facts, overconfidence, alignment), because each class routes to a different team and fix. The failure description becomes an eval checked for being "on distribution" with both positive and negative cases.
- Eval shape (44:29): prompt plus golden answer; 30-40 examples to start; added to a shared eval repository and run on each new model version. Lenny calls it "test-driven development for PMs"; she agrees it is now core to PM work at Anthropic and says PMs at other companies are adopting it (46:54).
- When PRDs still win (48:03): (1) aligning a big cross-functional group (including legal and safety) on goals and a source of truth; (2) ambiguous opportunities where you need product vision before you have pain points.
- Labs operating model (23:58-27:30): strongly held theme, weakly held prototype; pods are tiny, sometimes one engineer; large teams on ambiguous bets slow down; bets that fail are revisited one or two model generations later; prototypes that never ship still count as learning. Produced Claude Code, MCP, Skills, Claude Design.
- Forward compatibility check (34:03): "let's say Claude 8 comes around. What changes in what users do?" asked of every product being built.
- Managers must build (50:19-52:35): tenured PM hires get the same onboarding as early-career ones (read transcripts, read consented feedback, talk to customers); she owns one or two workstreams per model release to keep her "theory of mind".
- Token spend is an input; the outcome to target is experimentation (20:37).
- Protect your thinking (1:01:38): form your own point of view first, then use Claude as a sparring partner; delegate fully only where the writing is worth less than the thinking.
- Personal skills: a "Crucial Conversations" coaching skill shared with her managers (58:22-1:00:25); an MBR-writing skill being improved (1:01:38). Used a research Opus to pressure-test Claude pricing because it pushes back (1:04:49).
- Pace: four model series shipped in all of 2024; more than that in Q2 2026 alone (1:17:01).
- Claude Tag mentioned as a new paradigm of letting an agent go off and bring work back; versions of it are used internally (58:22, 1:27:12). No detail.

## Notable quotes
- "evals are the new PRDs" (41:00)
- "You have to sweat the tokens as much as you sweat the pixels" (42:32)
- "Who's signing off? Maybe less around who's writing" (1:08:29)
- "if you're not building yourself, ... you're not going to make it" (Lenny's paraphrase, 52:35, which she endorses)

## Could not verify
- Full transcript read (Substack auto-transcription; the guest's name is spelled "Diane" in it).
- The 80% JSON figure and the 99.9-100% eval scores are her recollection, not shown.
- The eval-as-spec practice is described for a research PM team whose product is the model; no evidence here on how far it is used by Anthropic's application product teams.
- Sponsor reads removed from consideration.
