---
title: "Open Policy Agent documentation (Introduction)"
source_url: https://www.openpolicyagent.org/docs
author: Open Policy Agent project (CNCF)
publisher: openpolicyagent.org
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [governance-as-code, gate-judge-separation]
relevance: medium
---

## Relevance to the project
OPA is the default policy-as-code engine in platform engineering, and its core idea, decoupling the policy decision from enforcement with JSON in and a structured decision out, is what makes a platform's checks callable by anything, including an agent asking "would this request pass?" before submitting. Rego policies are code, so they can be published and read, but they are rarely written for a consumer to understand.

## Themes
- governance-as-code: software sends structured input, OPA evaluates it against Rego policies and data, and returns a decision that "can be arbitrary structured data", not just allow/deny (Overview).
- gate-judge-separation: OPA decides; the caller (Kubernetes admission, Envoy, CI, Terraform plan check) enforces.

## Key points
- Use cases listed: Kubernetes admission control, Envoy/HTTP/GraphQL API authorisation, Terraform plan validation, CI/CD, Kafka, SSH/sudo.
- CNCF graduated project.
- Example policy outputs a list of violation messages, the form most useful to an agent fixing a request.

## Notable quotes
- "an open source, general-purpose policy engine that unifies policy enforcement across the stack."

## Could not verify
- Maintainer changes after Apple hired Styra's OPA maintainers (2025) are not covered on this page.
