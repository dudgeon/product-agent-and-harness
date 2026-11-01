---
title: Handoffs (OpenAI Agents SDK)
source_url: https://openai.github.io/openai-agents-python/handoffs/
author: OpenAI
publisher: OpenAI Agents SDK docs
published: unknown
retrieved: 2026-10-31
type: docs
evidence: first-party
filed_by: research-agent-handoff-models
themes: [handoff-context-transfer, agent-frameworks, human-review-gates]
relevance: high
---

## Relevance to the project
The most precise first-party statement of what crosses a control-transfer handoff: by default the receiving agent sees the whole prior conversation, and the developer narrows it with an input filter or an opt-in history-collapsing mode. This is the reference mechanism for "the conversation follows the transfer" and bears on model A (finish-to-start relay) versus model B (through line), because in a handoff the user's conversation moves to the receiving agent for the rest of the turn.

## Themes
- handoff-context-transfer: "the receiving agent gets to see the entire previous conversation history" by default; `input_filter` receives `HandoffInputData` (`input_history`, `pre_handoff_items`, `new_items`, `input_items`, `run_context`) and returns a new one (section "Input filters").
- agent-frameworks: handoffs are represented to the model as tools named `transfer_to_<agent_name>`; `handoff_description` is appended to the tool description (section "Creating a handoff").
- human-review-gates: authorisation for an argument-bearing handoff belongs at the start of `on_handoff`, which can raise to stop the transfer; `is_enabled` runs before arguments exist and so cannot authorise them.

## Key points
- Handoffs stay inside one run; each destination gets its own handoff tool.
- `input_type` is a schema for model-generated metadata on the handoff call (reason, priority), passed to `on_handoff`; it does not change what the receiving agent reads. Application state goes in `RunContextWrapper.context`.
- Prebuilt filters (`agents.extensions.handoff_filters`), e.g. `remove_all_tools`, drop structured tool items; the page warns this does not redact tool content already copied into messages.
- `nest_handoff_history` (opt-in beta, "disabled by default while we stabilize it") collapses prior history into assistant summary segments wrapped in `<CONVERSATION HISTORY>`; it "does not redact sensitive data". `handoff_history_mapper` gives full control of the forwarded items.
- Server-managed conversations (`conversation_id`, `previous_response_id`) do not support handoff input filters.
- Recommended prompt prefix `RECOMMENDED_PROMPT_PREFIX` tells agents about handoffs.

## Could not verify
- Page undated; no guidance on measured quality differences between full and filtered history.
