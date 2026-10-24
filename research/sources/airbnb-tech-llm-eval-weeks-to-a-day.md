---
title: "From weeks to a day: how we made LLM evaluation fast enough to iterate on"
source_url: https://airbnb.tech/ai-ml/from-weeks-to-a-day-how-we-made-llm-evaluation-fast-enough-to-iterate-on/
author: Baharak Saberidokht (Airbnb)
publisher: The Airbnb Tech Blog (airbnb.tech)
published: 2026-07-27
retrieved: 2026-10-24
type: article
evidence: first-party
filed_by: research-airbnb-spotify-product-practices
themes: [evals-autonomy-trust, harness-over-model, human-review-gates]
relevance: low
---

## Relevance to the project
A deep ML-infrastructure post on making LLM evaluation deterministic and fast enough to ship same-day model fixes. Relevant to the project mainly as evidence that, at Airbnb, the bottleneck for iterating on AI features was evaluation noise and seams between components, not model quality. It supports the case that a harness's eval layer (caching, stable judges, end-to-end checks) is where trust is earned.

## Themes
- evals-autonomy-trust: roughly three-quarters of LLM-generated references differ across runs on identical inputs, and the same judge drifts about 1% between runs, when real signal is 1-3% (Layer 1). Fix: per-sample cache of references and judge scores, making evaluation deterministic (Layer 2).
- harness-over-model: "the debt accumulates at the seams, not in the components" (Conclusion); validated components still failed together (language detection on code-mixed input, truncation, cache-warmth latency) (Layer 4).
- human-review-gates: "micro adapters" (small LoRA patches, rank under 50, train in under an hour on one GPU) ship like hotfixes behind two gates: no regression on expert-reviewed domains, and high-uncertainty outputs flagged for human review; canary with auto-rollback (Layer 3).

## Key points
- Four layers: name the noise (epistemic vs aleatoric), deterministic evaluation foundation, bounded model mutation, end-to-end validation at the seams.
- Over half of model outputs across candidates were identical strings; much observed noise came from the test process itself.
- Base model mentioned: an 8-billion-parameter model with shared adapters (product not named).
- Patch lifecycle rules: fuse co-triggering patches, retrain when patches pile up, unload unused patches.
- End-to-end set: traffic-weighted sample plus over-represented tail locales and prior incident cases, run on every release candidate.

## Could not verify
- The product the system serves is not named (it handles locales and input modalities; likely support or messaging). Headline "weeks to a day" is the author's claim.
