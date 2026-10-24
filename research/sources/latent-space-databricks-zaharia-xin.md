---
title: "Why the Frontier Ecosystem must be Open — Matei Zaharia and Reynold Xin, Databricks"
source_url: https://latent.space/p/databricks
author: swyx (host); Matei Zaharia, Reynold Xin (guests)
publisher: Latent Space
published: 2026-06-24
retrieved: 2026-10-24
type: podcast
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [meta-harness, shared-persistent-sessions, harness-portability]
relevance: medium
---

## Relevance to the project
Databricks' CTO explaining why Omnigent exists, recorded at Data + AI Summit 2026. Useful for the stated motivation (security approval, sharing personal setups, surviving vendor API changes) and for one adoption claim we can check against the repo. All claims are the builder's own.

## Themes
- [[meta-harness]]: internal coding-agent users, Databricks' agent builders and customer teams kept hitting harness/model switching, session sharing and security approval; Zaharia argues "it's the same problems".
- [[shared-persistent-sessions]]: engineers' useful personal setups could not be used by teammates without a shared server.
- [[harness-portability]]: Omnigent maps each harness to a common API so Databricks does not break when vendors change their APIs.

## Key points
- Claim: about half of the roughly 400 merged PRs in the first days came from outside the Databricks team (first-party; by 2026-10-24 the top ten committers by commit count are Databricks/MLflow staff, see [github-omnigent-repo](github-omnigent-repo.md) follow-up).
- Internal token use at Databricks: unlimited but monitored. Security is "paramount" for Databricks as a cloud provider.
- No internal Omnigent usage figures given (the "3,000+ engineers" figure elsewhere is second-hand).
- Agent Bricks not mentioned; Unity Catalog mentioned as Zaharia's prior governance work.

## Notable quotes
- "I don't want to end up on the front page as, like, I installed some weird npm package and leaked" (Zaharia, paraphrased via summarising fetch; treat as approximate)

## Could not verify
- Only the first ~100k characters of the transcript page were read, through a summarising fetch.
