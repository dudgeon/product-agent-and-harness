---
title: Design Lessons from the Fastest Q&A Site in the West
source_url: https://people.eecs.berkeley.edu/~bjoern/papers/mamykina-stackoverflow-chi2011.pdf
author: Lena Mamykina, Bella Manoim, Manas Mittal, George Hripcsak, Björn Hartmann
publisher: Proceedings of CHI 2011 (ACM), pp. 2857-2866
published: 2011-05
retrieved: 2026-10-31
type: paper
evidence: independent
filed_by: define-shaping-and-dependency-agents
themes: [two-sided-cold-start, org-learning-loop, enablement-by-product]
relevance: high
---

## Relevance to the project

The best documented account of how a knowledge Q&A network beat the cold start: Stack Overflow's founders gathered "a critical mass of dedicated users even before the site was introduced" through blogs read by about 140,000 people and weekly podcasts, so thousands were asking and answering on day one. It shows that critical mass came from the founders' standing inside the community and their daily involvement, not from the software alone, which bears on who should launch the dependency agent and its anchor platforms (people feature and platform teams already trust). It also gives a usable shape for the contributor base: 1% of users supplied 28% of answers. Peer-reviewed; authors unaffiliated with the site; data July 2008 to July 2010.

## Themes

- **two-sided-cold-start**: pre-launch community building via the founders' blogs (about 140,000 combined readers) and weekly podcasts meant "thousands of people were asking and answering questions within the first day" (Qualitative study, Achieving Critical Mass). Independent.
- **two-sided-cold-start**: the authors credit success "not primarily" to superior technical design but to "the high visibility and daily involvement of the design team within the community" (abstract).
- **org-learning-loop**: median first answer 11 minutes, 92.6% of questions answered; median answer time flat since launch even as traffic grew, suggesting "motivating users to frequently return and participate is more important than the total number of users" (How well does Stack Overflow perform?).
- **enablement-by-product**: a separate meta site and almost daily releases formed a continuous feedback loop with users (introduction, factor 3).

## Key points

- Scale by August 2010: about 300,000 registered users, 833,000 questions, 2.2 million answers, 7.8 million monthly visitors (performance section, Table 1).
- Contributor ecology: 94.4% of users never highly active supplied 34.4% of answers; "shooting stars" (4.2%) supplied 21.9%; "community activists" (1%) supplied 27.8% (Four answer behaviors; Figure 9).
- 48.5% of registered users had answered at least one question; about a quarter had not asked, answered or voted (Askers and answerers overlap).
- Reputation and badges "got them hooked"; users motivated only by points plateaued and dropped off (the shooting-star pattern), those with intrinsic motivation stayed (Incentives section).
- Slow or unanswered questions cluster on obscure technologies with few users (Some questions are not supported well). For the agent: niche platforms will be thinly covered by a crowd and need owner curation.
- Narrow, precisely drawn community boundaries mattered more than which boundary was chosen (offshoot sites section).
- The authors ask whether outsiders to a community can foster knowledge sharing with the right tools alone (introduction), an open question for an agent launched by a central team.

## Notable quotes

- "Thought-leader status and visibility within their community allowed the founders to gather a critical mass of dedicated users even before the site was introduced" (introduction, factor 2)
