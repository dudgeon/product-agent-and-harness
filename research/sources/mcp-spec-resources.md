---
title: "Resources (MCP specification 2025-06-18)"
source_url: https://modelcontextprotocol.io/specification/2025-06-18/server/resources
author: Model Context Protocol project
publisher: modelcontextprotocol.io
published: 2025-06-18
retrieved: 2026-10-24
type: docs
evidence: first-party
filed_by: user-story-mapping
themes: [artifact-standardization, pm-tool-connectivity, skill-standards]
relevance: high
---

## Relevance to the project
MCP resources are the closest existing protocol primitive for 'a document or artifact an agent can read' with URI, type and modified time. They are application-controlled, and in practice many vendor servers expose only tools, so the primitive is under-used for PM artifacts.

## Themes
- artifact-standardization: resource = uri, name, title, description, mimeType, size, plus annotations `audience` [user|assistant], `priority` 0-1, `lastModified` ISO-8601; resource templates via RFC 6570 URI templates; `resources/list`, `resources/read`, `resources/subscribe`.
- pm-tool-connectivity: spec says resources are application-driven (host decides how to include context) and access controls SHOULD be implemented; Snowflake's managed server supports tools only (see snowflake note), showing resources are not universally implemented.

## Key points
- Capabilities `subscribe` and `listChanged` are optional.
- Standard URI schemes: https://, file://, git://; custom schemes allowed per RFC 3986.
- No built-in notion of version history, owner, or status beyond lastModified; those would need conventions on top.

## Could not verify
- This is the 2025-06-18 revision; a 2026-07-28 revision is covered in mcp-spec-2026-07-28-key-changes and was not re-checked for resource changes.
