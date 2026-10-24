---
title: Amazon Bedrock AgentCore adds quality evaluations and policy controls for deploying trusted AI agents
source_url: https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/
author: Danilo Poccia (AWS)
publisher: AWS News Blog
published: 2025-12-02
retrieved: 2026-10-24
type: article
evidence: vendor-claim
filed_by: research-runtime-patterns-follow-up-round
themes: [agent-control-plane, evals-autonomy-trust, harness-portability, human-review-gates]
relevance: high
---

## Relevance to the project
AWS's governance layer for agents is enforced at the tool-call boundary: Cedar policies attached to AgentCore Gateway, evaluated "outside of the agent's reasoning loop", independent of framework or model. That is a deterministic gate a regulated company can audit, and it applies to any agent whose tools go through the gateway, including a Claude Agent SDK agent hosted on AgentCore Runtime (see the Classmethod note). Paired with managed online evaluations, it is the closest hyperscaler analogue to Omnigent-style policies, but for agents rather than CLIs.

## Themes
- agent-control-plane: Policy intercepts Gateway tool calls before they run; enforce or log-only mode.
- evals-autonomy-trust: AgentCore Evaluations continuously samples and scores live interactions (correctness, faithfulness, tool selection etc.), custom LLM-judge evaluators, CloudWatch alarms.
- harness-portability: "The policies operate independently of how the agent was built or which model it uses"; names CrewAI, LangGraph, LlamaIndex, Strands.
- human-review-gates: log-only mode lets teams validate policies before enforcing.

## Key points
- Policies written in Cedar or natural language (converted to Cedar and validated; unenforceable rules flagged).
- Update notes in the post: Policy GA 2026-03-03; Evaluations GA 2026-03-31.
- Episodic long-term memory strategy added to AgentCore Memory.
- Customer claims (vendor-reported): PGA TOUR (1,000% faster content writing, 95% lower cost), Workday (30% less planning analysis time), Grupo Elfa (observability for audit traceability, 50% faster problem resolution).
- Regions include US, Asia Pacific and EU (Frankfurt, Ireland).

## Notable quotes
- "Policy gives you control over the actions agents can take and are applied outside of the agent's reasoning loop"
- "The policies operate independently of how the agent was built or which model it uses."

## Could not verify
- AgentCore Identity, pricing and Amazon Quick Suite (AWS's employee-facing agent workspace) were not read. Retrieved via WebFetch (model-summarised view).
