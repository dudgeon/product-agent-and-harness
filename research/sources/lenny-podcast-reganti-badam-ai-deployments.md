---
title: "Why most AI products fail: Lessons from 50+ AI deployments at OpenAI, Google, and Amazon"
source_url: https://www.lennysnewsletter.com/p/what-openai-and-google-engineers-learned
author: Lenny Rachitsky (host), Aishwarya Naresh Reganti (LevelUp Labs; ex-Amazon/Google), Kiriti Badam (OpenAI, Codex)
publisher: Lenny's Podcast
published: 2026-01-11
retrieved: 2026-10-24
type: podcast
evidence: anecdote
filed_by: research-lennys-newsletter-archive
themes: [evals-autonomy-trust, risk-sloped-review, agent-project-failure-rates, org-context-grounding, tacit-knowledge-capture, single-agent-many-skills, outcome-measurement-gap, human-judgment-pm-jobs]
relevance: medium
---

## Relevance to the project
Two practitioners with enterprise deployment experience argue that agents should earn autonomy in stages (route, then draft for a human, then resolve end to end), logging what humans change at each stage as free error analysis, and that evals catch only known failures so production signals must find new ones. That is a concrete, sequencing-friendly answer to review-and-autonomy ("earned from measured accuracy") and pm-agent-evaluation, with two regulated examples (bank underwriting, insurance pre-authorization). Also useful: "evals" now means many different things, the "PMs write evals, they're the new PRDs" line is called a misreading, and peer-to-peer multi-agent designs are called misunderstood. Evidence is the guests' consulting experience; they sell a course on the method.

## Themes
- evals-autonomy-trust: "agency control trade-off": every grant of decision-making gives up control, so the agent must earn trust (9:34); continuous calibration, continuous development (CC/CD) loop: curate expected inputs/outputs, set evaluation metrics, deploy, then analyse unexpected behaviour and add metrics only for recurring failures (47:58-49:37). Move to the next stage when calibration stops producing surprises (58:18).
- risk-sloped-review: insurance pre-authorization: routine MRIs and blood tests can be automated while invasive surgery stays with a human; autonomy can be constrained by number of actions or by topic risk (16:02, 55:55).
- agent-project-failure-rates: cites a Berkeley/Databricks study in which about 74-75% of enterprises named reliability as their biggest problem, which is why most deployed AI is low-autonomy productivity tooling (21:45); they shut down one end-to-end support agent after endless hot fixes (46:18). Claims of one-click agents with gains in days are "pure marketing"; critical workflows take "four to six months" (30:31).
- org-context-grounding / tacit-knowledge-capture: messy enterprise taxonomies (a dead 2019 node in a retail category tree) and "really weird rules within enterprises that are not documented anywhere" that human agents know and agents do not (51:10-52:46).
- outcome-measurement-gap: logging how much of a draft a human used or omitted gives error analysis "for free" (52:46); implicit signals such as regenerations or switching off a code-review product matter as much as thumbs (35:17, 43:28).
- single-agent-many-skills: multi-agent is "misunderstood": supervisor plus sub-agents works, but splitting by function and letting agents talk peer to peer is not ready, especially when any agent might reply to a customer (1:01:34-1:03:44).
- human-judgment-pm-jobs: "Building is really cheap today. Design is more expensive" (1:04:22); careers will turn on taste and judgment (1:08:52).

## Key points
- **Two differences from normal software (8:01-9:34):** non-determinism on both input (natural-language intent) and output, and the agency-control trade-off.
- **Staged autonomy examples (13:38-17:41, 51:10-54:22):** support agent: V1 routing (humans can undo), V2 copilot drafts from SOPs with human edits logged, V3 end-to-end resolution; coding assistant: inline suggestions, then larger blocks for review, then autonomous PRs; marketing: drafts, then multi-step campaigns, then auto-optimized launches.
- **Roles (5:54):** old handoffs between PMs, engineers and data teams are broken; they now "own the same feedback loop", reading agent traces together to decide behaviour.
- **Success triangle (25:43-30:31):** hands-on leaders who relearn intuitions (a CEO with a daily 4-6 a.m. AI catch-up block), an empowering culture (subject-matter experts refuse to help if they fear replacement), and obsession with the workflow, mixing ML models, deterministic code and agents.
- **Evals debate (33:47-44:24):** evals and production monitoring catch different things; vendors' "experts writing evals" usually means error analysis; one client's "evals" were public leaderboards. Codex keeps core regression evals, A/B tests model changes on its code-review product, and has each engineer throw their own hard problems at new models.
- **Recalibration triggers (58:18-1:01:24):** model deprecations (GPT-4o to GPT-5) and evolving user behaviour. A bank underwriting assistant worked for three or four months until underwriters began asking "for a case that looks like this, what did previous underwriters do?", which needed a different system.
- **Prediction (1:05:30):** proactive background agents plugged into where work happens, e.g. "I have fixed five of your linear tickets ... review them at the start of your day".

## Notable quotes
- "Evaluation metrics catch only the errors that you're already aware of" (55:55).
- "If someone's selling you one click-agents, it's pure marketing" (30:31).
- "There are really weird rules within enterprises that are not documented anywhere" (52:46).

## Could not verify
- Transcript read 5:16-1:12:07 in full; intro and lightning round skimmed. Auto-transcription errors ("Kodex", "Cloud Code").
- Lenny's written takeaways add points (confidence-score UX, treating prompts as versioned CI/CD artifacts, startup vs enterprise playbooks) that I did not find in the transcript sections read; treat those as the show notes' gloss.
- "50+ deployments", the 74-75% reliability figure (attributed to a paper by Matei Zaharia's group, linked in the show notes), and the underwriting time gains are the guests' statements; no data shown. The method behind CC/CD is set out in an earlier guest post ("Why your AI product needs a different development lifecycle") not filed here.
