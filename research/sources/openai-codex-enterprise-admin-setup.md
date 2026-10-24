---
title: Admin setup (Codex / ChatGPT Enterprise rollout guide) and Governance overview
source_url: https://learn.chatgpt.com/docs/enterprise/admin-setup
author: OpenAI
publisher: learn.chatgpt.com (redirected from developers.openai.com/codex/enterprise/admin-setup)
published: unknown
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: research-runtime-patterns-follow-up-round
themes: [enterprise-admin-controls, identity-delegation, cost-control-routing]
relevance: high
---

## Relevance to the project
OpenAI's rollout guide for Codex in ChatGPT Enterprise, read together with its companion Governance page (https://learn.chatgpt.com/docs/enterprise/governance). Together they show how OpenAI splits admin control into separate surfaces (workspace roles, local runtime policy, Codex cloud, connected systems, reporting/compliance), and they state several regulated-setting limits plainly: local computer access with Work Cloud is not strict ZDR, MCP hooks are not a complete audit trail, and spend controls do not set a universal Codex limit. Directly relevant to the regulated-audit requirement and to the governance-control-plane dimension.

## Themes
- enterprise-admin-controls (proposed): "the same role" doesn't control every surface; designated owners recommended for workspace access, local runtime policy, Codex cloud, connected systems and reporting/compliance (admin-setup).
- enterprise-admin-controls: "Codex Cloud is off by default for Enterprise workspaces"; admins grant "Use Codex in the cloud" and "Manage workspace environments" separately; "Allow members to use Codex locally" and "Use Work locally" are separate and "Enabling either one doesn't enable the other" (admin-setup).
- identity-delegation: "Workspace access doesn't grant repository, file, or action access in a connected service"; "Codex cloud respects the repository permissions and protections exposed by the connected source system" (admin-setup).
- cost-control-routing: eligible Codex activity can consume ChatGPT workspace credits and exhausted limits pause access, but "These controls don't set a universal Codex limit or govern Platform API billing" (governance).

## Key points
- Audit: "Use the Compliance API for audit and investigation records." Governance page: local computer access with Work Cloud has records under `conversation_message` and `codex_log`; local execution also emits OpenTelemetry events to a customer collector; "Conversation visibility alone does not establish a complete record of local actions." The Compliance API "It's not an adoption or productivity dashboard."
- Three reporting surfaces: workspace analytics (interactive), Analytics API (aggregated Codex reporting), Compliance API (audit records). Dashboards are "interactive reporting surfaces, not raw audit logs".
- Regulated-setting caveats (admin-setup): "Local computer access with Work Cloud does not provide strict zero data retention." "If your organization requires ZDR, do not enable this feature." Data and inference residency apply only to eligible content, workloads and regions; EKM covers "supported stored content in eligible workspaces"; Work is not supported with UAE inference residency.
- "Cloud environments don't inherit local device policy, MDM settings, or local network access."
- Plugins: plugin installation, bundled skills, connector capabilities, connector actions and source-system authorisation are separate decisions; "Disabling a connector-backed capability doesn't necessarily uninstall the plugin or its bundled skills." Plugins not available in the IDE extension.
- Policy automation: a policy API manages Global settings; Local and Codex Cloud settings are managed in the Agent Security UI (governance).
- "Work" (ChatGPT Work mode, local and cloud) is now a sibling product sharing the same admin surfaces as Codex.

## Could not verify
- SSO/SCIM, retention periods and the GitHub connector specifics are only linked, not described. Third-party role names (Workspace Owner, Codex Admin, Security/Compliance Admin; Vaughan blog) were not confirmed on OpenAI pages.
- Compliance API event coverage per surface (cloud task vs local CLI) is deferred to the API reference, which was not read. help.openai.com Compliance Platform article returned 403.
- Model-summarised fetch; no dates on either page.
