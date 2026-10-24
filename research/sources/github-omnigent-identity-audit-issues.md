---
title: "omnigent-ai/omnigent issues and discussions on shared-session identity, audit evidence and enterprise authorisation (#2150, #5670, #10359, #11493, discussions #5931 and #1133)"
source_url: https://github.com/omnigent-ai/omnigent/issues/2150
author: Omnigent users and maintainers (incl. SciChart, external evaluators)
publisher: GitHub
published: 2026-10-24
retrieved: 2026-10-24
type: other
evidence: anecdote
filed_by: research-runtime-patterns-follow-up-round
themes: [identity-delegation, shared-persistent-sessions, meta-harness, harness-portability, policy-enforcement-fail-open]
relevance: high
---

## Relevance to the project
The nearest thing to adopter testimony: outside teams evaluating Omnigent for multi-user pilots describe exactly the gaps a regulated audit setting would hit. Shared sessions execute as the owner (anyone with edit rights acts with the owner's credentials), there is no durable governance evidence timeline, authorisation stops at authentication (no IdP group mapping, no SCIM, no durable audit trail), and the subscription-auth story is unclear relative to Anthropic's terms. URLs: issues [#2150](https://github.com/omnigent-ai/omnigent/issues/2150), [#5670](https://github.com/omnigent-ai/omnigent/issues/5670), [#10359](https://github.com/omnigent-ai/omnigent/issues/10359), [#11493](https://github.com/omnigent-ai/omnigent/issues/11493), [#11413](https://github.com/omnigent-ai/omnigent/issues/11413), discussions [#5931](https://github.com/omnigent-ai/omnigent/discussions/5931), [#1133](https://github.com/omnigent-ai/omnigent/discussions/1133), [#1434](https://github.com/omnigent-ai/omnigent/discussions/1434). Published date is retrieval of the latest activity.

## Themes
- [[identity-delegation]]: #2150 (opened 2026-07-07, still open): shaunmlowry (2026-07-20) notes tools in a shared session run with the session owner's identity, so anyone with edit permission can impersonate the owner for git, Atlassian, Slack; and any user in the chat can approve tool calls. Maintainer PattaraS (2026-07-28) proposes the invariant "A shared session always executes as its owner. Message authorship is informational and must never silently change credentials or authorization identity", restricting approvals to the owner.
- [[identity-delegation]]: David Burleigh (antichaosdb, SciChart, 2026-07-27): SciChart ran its own multi-agent platform (SciClawd) in production for about four months and built per-message acting identity (Ed25519-signed messages, four-tier access matrix, authorisation resolved against the latest human sender) over about six weeks, then removed it in June; the identity plumbing "fought the harness" (an MCP-proxy header approach shipped and was torn out the same day) and identity that looked correct still produced privilege escalation. Now "experimenting with Omnigent". bradleyfay (2026-07-10/14) built a fork patch "while evaluating omnigent for a multi-user pilot".
- [[shared-persistent-sessions]]: #11413 (2026-10-23, P1 feature): sharing does not separate chat access from host access (terminals, files).
- [[meta-harness]] / audit: #5670 (philtief, 2026-08-27, open): no single durable timeline of policy evaluations, denials, approvals, reviewer decisions, agent switches and child sessions; an auditor must reconstruct it from messages, transient SSE events, several transcripts and external logs. jsingh-github (2026-09-27) runs Omnigent programmatically (orchestrator via REST API, custom policies on hand-offs) and says policy decisions exist only as trace spans needing a separate tracing backend.
- [[identity-delegation]]: #10359 (jsonmp-k8, 2026-10-16, open, labelled help wanted): authentication is good (PKCE OIDC, trusted-header mode, per-session READ/EDIT/MANAGE grants) but "authorization stops at 'who are you'": admins are a static file, no IdP group-to-role mapping, header mode has no trusted-proxy guard (later a critical advisory, GHSA-x6v6), no durable audit trail, no SCIM.
- [[harness-portability]]: README lists "Subscription: A Claude Pro/Max or ChatGPT plan, via the official `claude` / `codex` CLIs". #11493 (andrewreid, 2026-10-24) proposes storing a user's `claude setup-token` token server-side, encrypted, and vending it to managed sandboxes as `CLAUDE_CODE_OAUTH_TOKEN`; the author says he has built and run it on Kubernetes. Discussion #1133 (2026-06-24) asks whether Omnigent's Claude auth breaches Anthropic's terms; no answer at retrieval.
- [[policy-enforcement-fail-open]] (proposed): discussion #5931 (rafaelasor, 2026-08-31; promotes the poster's own engine) argues three gaps: a policy is not narrowed across sub-agent hand-offs; permissions are described by a person rather than derived from the session; the record of what was allowed lives inside the harness, so "An auditor has to trust it rather than verify it". Claims a hash-chained, offline-verifiable log running against Omnigent 0.11.0 unmodified (vendor claim, not checked).

## Key points
- Named outside users or evaluators in the tracker: SciChart (experimenting), Southeast Marketing Services (following, attended a workshop by Aravind Segu and Dhruv Gupta), bradleyfay (multi-user pilot evaluation, organisation not stated), jsingh-github (programmatic multi-agent use), andrewreid (Kubernetes managed-sandbox deployment). No named production adopter outside Databricks/Neon.
- GitHub Discussions are little used: 12 discussions in total at retrieval; the roadmap thread (#1434) collected feature asks (other subscriptions, voice, tasks inbox, auth-expiry recovery, MCP config management).

## Could not verify
- Organisations of most commenters; author_association NONE/CONTRIBUTOR says only that they are not repo collaborators.
- Whether #11493's design is compatible with Anthropic's terms (see [anthropic-claude-code-legal-and-compliance](anthropic-claude-code-legal-and-compliance.md)); this is our reading, not a ruling.
