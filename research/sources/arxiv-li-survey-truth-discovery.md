---
title: "A Survey on Truth Discovery"
source_url: https://arxiv.org/abs/1505.02463
author: Yaliang Li, Jing Gao, Chuishi Meng, Qi Li, Lu Su, Bo Zhao, Wei Fan, Jiawei Han
publisher: ACM SIGKDD Explorations Newsletter 17(2) (arXiv preprint)
published: 2015-05-11
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: define-shaping-and-dependency-agents
themes: [context-trust-mechanisms]
relevance: high
---

## Relevance to the project
The standard survey of "consensus from several sources" methods: they jointly estimate how reliable each source is and which value is true, instead of majority voting. It bears on whether consensus is a sound trust mechanism for written-back context (several sessions or experts giving a platform's lead time): weighted consensus beats voting, but it depends on sources being independent, needs enough claims per source, and cannot be evaluated without ground truth. Those are exactly the conditions an enterprise store with few, correlated contributors fails.

## Themes
- context-trust-mechanisms: majority voting "assume[s] all the sources are equally reliable"; truth discovery infers source reliability from the data, giving more weight to sources that agree with inferred truths (section 1, section 2.2).

## Key points
- The Mount Everest example: the most frequent value on the web was wrong and a single reliable source was right; voting picks the wrong answer (section 1).
- Source independence assumption: many methods assume sources observe independently rather than copying; when sources copy, shared errors look like confirmation. Copy-detection methods exist (common mistakes signal dependence), but co-copying and transitive copying remain hard (sections 3.2.2-3.2.3). In an enterprise store, two sessions that both read the same stale wiki page are not two sources.
- Long tail: "many sources only provide very few observations", so a point estimate of reliability is unreasonable; confidence-aware methods (CATD) give an interval instead (section 4). Most enterprise experts answer a handful of questions; their reliability is mostly unknown.
- Open problem stated by the authors: methods are evaluated against ground truth that in practice is unavailable and expensive to label (section 5, "Performance evaluation").
- Methods compared in tables 2-3 by input data type, source dependency handling, and output.
