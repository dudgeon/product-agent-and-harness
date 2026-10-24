---
title: "Inside-Out AI: Rebuilding Airbnb Behind the Scenes and Across the Guest Experience"
source_url: https://latent.space/p/airbnb
author: Richard MacManus (interview with Ahmad Al-Dahle, CTO, Airbnb)
publisher: Latent Space
published: 2026-10-02
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [spec-becomes-prototype-and-evals, compounding-context-repo, legible-org-for-agents, org-context-grounding, remote-agent-invocation, cost-control-routing, evals-autonomy-trust, human-review-gates, pm-persona-role-expansion]
relevance: high
---

## Relevance to the project
The CTO's clearest account of Airbnb's "inside-out" plan: use AI to change how product is built first, then ship the same capabilities to guests. It names the process change (PM, design and engineering move straight to prototypes; "the code being the artifact that we reason upon"), the internal context graph Everest that let a second partner-integration service ship in six weeks after the first took eight to nine months, the internal agent AirChat with MCP org context, and event-triggered async agents that take first on-call. Evidence type is first-party: these are Al-Dahle's claims, reported by an independent outlet that checked two against earnings material.

## Themes
- spec-becomes-prototype-and-evals: the old chain (requirements, then Figma design, then engineering, then testing) with team handoffs has given way to teams working directly with prototypes; "We moved away from excessive artifact generation".
- compounding-context-repo: learnings from building grocery delivery went into Everest, so airport pickup (a similar partner API integration) took about six weeks versus eight to nine months (Chesky gave the same numbers on the Q2 2026 call).
- legible-org-for-agents: Everest is "an internal organizational context graph" built and queried with LLMs, embeddings and AI retrieval; it lets "generalists work across very specialist parts of the code".
- org-context-grounding: AirChat "[includes] basically all the necessary MCP organizational context".
- remote-agent-invocation: async agents in containers, triggered by events; teams automating on-call: when a Grafana-style alert trips, agents triage and start the response, propose a PR for a human to review, and can close alerts they judge flaky.
- cost-control-routing: "multi-model company"; at least 10 customised production models; most post-training and RL on open models; choose per use case along a cost, performance, latency frontier; strongest frontier model for coding, smaller post-trained models for latency-bound search.
- evals-autonomy-trust: evals built per use case from sampled production data (search queries; support queries including edge cases); large synthetic data sets used to test the support agent before production.
- human-review-gates: safety issues still route to humans; rule that "every engineer must be able to explain, even if an AI generated the PR, ... what they built".
- pm-persona-role-expansion: organise teams around outcomes and missions, not features, as a condition for being AI-native.

## Key points
- Numbers (Al-Dahle, Oct 2026): 60% of code AI-authored; nearly 80% more features and improvements shipped year over year; average engineer PR throughput up about 1.6x; roughly half of support tickets resolved purely by AI (article notes Q2 2026 letter says nearly 45%).
- Support was the first user-facing AI area, chosen as "the hardest problem to deploy" because mistakes are costly.
- Future: "large amounts of asynchronous agents" monitoring fraud, trust violations, marketplace quality and software defects.
- Worry: junior engineers building judgement when AI writes much of the code.

## Notable quotes
- "the code being the artifact that we reason upon, and prototypes"
- "we're able to have generalists work across very specialist parts of the code"

## Could not verify
- Everest has no public technical description; how it is fed (code, docs, tickets, decisions) is not stated. The 1.6x PR figure differs from the 65% DX TrueThroughput figure (dx-airbnb-beyond-the-cli-airchat); they may measure different things or periods.
