---
title: Agentcore RuntimeにClaude Agent SDK製エージェントをデプロイしてみた (Deploying a Claude Agent SDK agent to AgentCore Runtime)
source_url: https://dev.classmethod.jp/articles/deploy-claude-agent-sdk-on-agentcore-runtime/
author: Miori Takeguchi (Classmethod)
publisher: DevelopersIO (Classmethod)
published: 2026-04-21
retrieved: 2026-10-24
type: article
evidence: independent
filed_by: research-runtime-patterns-follow-up-round
themes: [harness-portability, agent-control-plane, build-vs-buy]
relevance: medium
---

## Relevance to the project
Independent practitioner evidence that a hyperscaler agent runtime can host the Claude Code harness itself: the Claude Agent SDK launches the Claude Code CLI as a subprocess inside AgentCore Runtime, with model calls routed through Bedrock. This makes "Claude Code-quality harness under a hyperscaler control plane" a real build option (P2 inside a governed cloud runtime), not just a theory. It is a hello-world, not a production report.

## Themes
- harness-portability: AWS recommends Strands, but the author shows Claude Agent SDK works on AgentCore Runtime.
- agent-control-plane: once on AgentCore, the agent can sit behind Gateway policy, observability and IAM (not tested in the post).
- build-vs-buy: deploy is a wrapper (`BedrockAgentCoreApp`, `@app.entrypoint`) plus `agentcore configure/deploy/invoke`.

## Key points
- Agent: Python, Claude Haiku 4.5, `allowed_tools=["Bash","Glob"]`, `permission_mode="acceptEdits"`.
- `CLAUDE_CODE_USE_BEDROCK=1` in SDK env; Bedrock short-term API key passed at deploy time as env var (not production-grade secret handling); Direct Code Deploy (no Docker), IAM auth, memory disabled.
- Response in about a second; only final `ResultMessage` returned; observability data can take up to 10 minutes to appear.

## Notable quotes
- (translated) "Claude Agent SDK-based agents also ran without problems in the Runtime environment."

## Could not verify
- Behaviour under real workloads, long sessions, or with AgentCore Policy attached. Japanese source read via WebFetch translation summary.
