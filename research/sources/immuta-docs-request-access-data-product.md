---
title: "Requesting access to a data product (Immuta)"
source_url: https://documentation.immuta.com/SaaS/request/access-data-products/how-to-guides/requesting-access-to-a-data-product
author: Immuta
publisher: Immuta documentation
published: unknown
retrieved: 2026-10-28
type: docs
evidence: first-party
filed_by: research-dependency-agent
themes: [onboarding-as-code, agent-originated-requests, risk-sloped-review]
relevance: medium
---

## Relevance to the project
Data-access onboarding in the shape the dependency agent needs: a consumer answers the product's access questions, accepts its data use agreement, and either gets access automatically (low-risk, fully protected data) or enters an approval flow; a REST endpoint accepts the request and returns it with status. The intake (questions, agreement) is defined per data product, so it is readable before submission.

## Themes
- onboarding-as-code: `POST /api/data-product/{id}/request` (and `/request/masking-exception`) with a Request-app personal access token; 201 returns the hydrated request.
- agent-originated-requests: requests can be made for oneself or on behalf of other users.
- risk-sloped-review: if approval isn't required, access is granted once the agreement is accepted and questions answered; otherwise status `Pending` until decided; provisioning via data-platform policies.

## Key points
- Statuses include Pending, Approved, Denied; Immuta marketing describes multi-approver routing by data sensitivity and ownership (search summary).

## Could not verify
- How auto-approval is configured, and whether any agent-specific identity is recorded.
