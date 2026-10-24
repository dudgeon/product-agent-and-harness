---
title: "RovoDev Code Reviewer: A Large-Scale Online Evaluation of LLM-based Code Review Automation at Atlassian"
source_url: https://arxiv.org/abs/2601.01129v2
author: Kla Tantithamthavorn, Yaotian Zou, Andy Wong, Michael Gupta, Zhe Wang, Mike Buller, Ryan Jiang, Matthew Watson, Minwoo Jeong, Kun Chen, Ming Wu
publisher: arXiv (accepted at ICSE 2026, SEIP track)
published: 2026-01-03
retrieved: 2026-10-24
type: paper
evidence: vendor-claim
filed_by: user-story-mapping
themes: [vendor-claims-vs-independent-evidence, outcome-measurement-gap, human-review-gates, evals-autonomy-trust]
relevance: medium
---

## Relevance to the project
The most rigorous published number for any Atlassian SDLC agent: a peer-reviewed (ICSE SEIP) one-year online evaluation of Rovo Dev's code reviewer. All authors are Atlassian-affiliated (the lead is also at Monash), so it is a vendor claim with peer review, not independent evidence. It also shows the reviewer's design: work item context in the prompt, an LLM judge to filter hallucinated comments, and a classifier for actionability.

## Themes
- `vendor-claims-vs-independent-evidence`: abstract reports 38.70% of comments led to code changes, PR cycle time down 30.8%, human-written comments down 35.6%. Atlassian's other blog claims 45% (see Key points).
- `outcome-measurement-gap`: outcome measured as code resolution rate and PR cycle time, not defect or customer outcomes.
- `evals-autonomy-trust`: companion blog describes "LLM-as-a-Judge" (gpt-4o-mini) filtering factually wrong comments, then a fine-tuned ModernBERT model ranking comments on actionability, trained on 50,000+ dogfood comments.
- `human-review-gates`: blog: "Rovo Dev code reviewer isn't an autonomous agent; it's a human-in-the-loop AI software development agent."

## Key points
- **Paper abstract (documented):** one-year offline, online and user-feedback evaluation; integrated into Bitbucket; "review-guided, context-aware, quality-checked code review comment generation without fine-tuning."
- **Companion blog** ([30.8% Faster PRs](https://www.atlassian.com/blog/artificial-intelligence/developer-productivity-improved-with-rovo-dev), Yaotian Zou, 2026-04-07): built on Claude 3.5 Sonnet; context includes "Related Jira issue summary and descriptions (business motivation and requirements)"; 1,900+ repositories; human comment resolution rate 44.45% vs Rovo Dev 38.70%; GA October 2025.
- **Second blog, different number** ([How Atlassian cut PR cycle time by 45% with AI code reviews](https://www.atlassian.com/blog/rovo/how-we-cut-pr-cycle-time-with-ai-code-reviews), Taroon Mandhana, 2026-01-29): median PR-to-merge had reached "over 3 days"; 18 hours average wait for the first review comment (26% of cycle time) "cut to 0"; "we cut our PR cycle time by 45%"; new engineers using Rovo Dev merged first PR "five days faster"; in beta "cut customer PR cycle time by 32% ... (from 4.18 to 2.85 days)". It says review checks Confluence-held engineering standards and "check PRs against those same Jira work items." The 45% vs 30.8% gap is unexplained (different window or metric likely; not stated).

## Could not verify
- Full paper body (only abstract read); how the 45% figure was computed; any independent replication.
