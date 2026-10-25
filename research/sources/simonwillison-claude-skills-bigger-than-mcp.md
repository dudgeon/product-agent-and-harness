---
title: "Claude Skills are awesome, maybe a bigger deal than MCP"
source_url: https://simonwillison.net/2025/Oct/16/claude-skills/
author: Simon Willison
publisher: simonwillison.net
published: 2025-10-16
retrieved: 2026-10-25
type: article
evidence: independent
filed_by: research-skill-rigidity-spectrum
themes: [skill-standards, rules-vs-judgment-encoding, skill-supply-chain-security]
relevance: medium
---

## Relevance to the project
An independent practitioner's case that skills (Markdown plus optional scripts) fit "the spirit of LLMs: give the model text and let it work out the rest", with scripts used where reliability matters. His Slack GIF example shows the core hybrid: the model does the creative part, a validation script checks the hard constraint (Slack's 2MB limit) and the model retries. He flags the unsolved cost: skills need a code environment, and safe sandboxing against prompt injection is open.

## Themes
- rules-vs-judgment-encoding: slack-gif-creator: output was poor but the bundled validator let the model check file size and retry; scripts make results more reliable while instructions stay loose.
- skill-standards: skills are "Markdown with a tiny bit of YAML metadata and some optional scripts"; only the frontmatter description loads at start (a few dozen tokens each); portable to Codex CLI and Gemini CLI.
- skill-supply-chain-security: dependence on a filesystem and command execution makes safe sandboxes more important; "safe" is doing a lot of work; prompt-injection containment unsolved.

## Key points
- Claude Code is "best described as a general agent"; skills make that explicit (example: a folder of data-journalism skills forming a data journalism agent).
- MCP tool definitions can consume tens of thousands of tokens; a CLI with `--help` often does the same job.
- Does not discuss how detailed skill instructions should be.

## Could not verify
- Willison's later posts on skills and on prompt injection were not read for this note.
