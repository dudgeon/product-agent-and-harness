# Contributions from competitive-teardown-stripe-knowledge-agents

For the director to merge into options/DIMENSIONS.md. Grouped by dimension slug.

## session-persistence-sharing
- Key question: Stripe's Kai keeps context "locked in" single-user sessions (roadmap: share across sessions, many people and agents on one artifact), while Orbit's UI says "Workspaces share context across sessions, all visible to each other". Would our users accept one shared session spanning PM shaping and engineering planning, or do they want a handoff artifact (spec, plan) at the boundary? — *answered by:* user interviews; prototype both — *affects:* shared/multiplayer, fork-copy handoff, branch-only handoff. Evidence: [Kai post](../research/sources/stripe-meet-knowledge-ai-platform.md) (first-party); [Not My Business video](../research/sources/youtube-notmybusiness-inside-stripe-ships-fast.md) (first-party). Detail: [PDLC map](../tasks/competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md).

## intent-shaping-and-spec
- Evidence note: at Stripe the PM → engineering boundary (goal/intent → Orbit plan) is a human handoff over documents, Slack, tickets and prototypes; no source documents a Kai → Orbit handoff. Documented agent-to-agent links are Kai → Harbor, Harbor → coding agents, Slack/Docs/tickets → Minions, Orbit → Minions. Source: [PDLC map](../tasks/competitive-teardown-stripe-knowledge-agents/02-pdlc-agent-ecosystem-map.md).
- Key question: who writes the intent Orbit starts from on PM-led work, the PM or the engineer, and does Kai share anything with Orbit? — *answered by:* Stripe's Agent Foundation team; a second Orbit demo — *affects:* plan as the agent-ready artifact, agent-led interrogation.

## remote-invocation-route
- Evidence row candidate: "Agents linked by a shared tool layer and documents, no orchestrator": Stripe's Toolshed (~500 MCP tools) is used by "hundreds of different agents"; specialist tools (Harbor) expose MCP toolsets; work moves between agents mostly through documents, threads and tickets. Maturity early-adopter. Evidence: [Minions part 2](../research/sources/stripe-minions-part-2.md); [Harbor](../research/sources/stripe-harbor-ai-prototyping.md) (first-party).
