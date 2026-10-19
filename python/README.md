# IndieML - Substance API

A lightweight, transformer-based API that evaluates text for substance, depth, and clarity in under 25ms while achieving 87% of the accuracy of a full-scale LLM. 
This package provides REST API, Python SDK, and MCP configuration details to natively connect the hosted Substance API to a wide variety of applications.
For more information, including API key requests, please visit [IndieML](https://indieml.app).

## REST API 

For integrations outside the Python and MCP ecosystems (such as standard OpenAI function calling, custom AI scripts, or raw HTTP requests), the hosted endpoint accepts standard JSON payload requests.

**cURL**
```bash
curl -X POST https://indieml.app/v1/score/substance \
  -H "X-API-Key: YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"input_text": "This is a test run."}'
```

**Python (Requests)**
```python
import requests

response = requests.post(
    "https://indieml.app/v1/score/substance",
    headers={"X-API-Key": "YOUR_API_KEY_HERE"},
    json={"input_text": "This is a test run."}
)
print(response.json())
```

**Node.js (Fetch)**
```javascript
const response = await fetch("https://indieml.app/v1/score/substance", {
  method: "POST",
  headers: {
    "X-API-Key": "YOUR_API_KEY_HERE",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ input_text: "This is a test run." })
});
console.log(await response.json());
```

## Python SDK

**Installation** (requires Python 3.11 or higher)
```bash
pip install indieml
```

**Usage**
```python
from indieml import Substance

# Initialize the API
api = Substance(api_key="YOUR_API_KEY_HERE")

# Evaluate text for substance, depth, and clarity
result = api.score("This is a test run.")
print(result)
```

## MCP Server Integration

You can integrate the Substance API into AI coding assistants by routing them to our cloud-native ASGI endpoints.

### Cursor, ChatGPT, and Claude Code (Streamable HTTP)
For agents that support native Streamable HTTP / SSE configurations, provide the remote URL and authorization header directly:
```json
{
  "mcpServers": {
    "indieml": {
      "type": "http",
      "url": "https://indieml.app/mcp/",
      "headers": {
        "X-API-Key": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### Claude Desktop (stdio via npx Bridge)
For local Linux, Mac, and Windows clients that require stdio transport, use the npx mcp-remote bridge to route the connection to the cloud endpoint. Node.js v20+ is required. Ensure your OS environment variables include INDIEML_API_KEY.
```json
{
  "mcpServers": {
    "indieml": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://indieml.app/mcp/",
        "--header",
        "X-Api-Key:${INDIEML_API_KEY}"
      ],
      "env": {
        "INDIEML_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

## Applications & Use Cases

The Substance API is a fast and inexpensive pre-screening tool designed to integrate with your existing filters.

While it evaluates substance across any text, it is uniquely suited for high-volume, automated data pipelines:

### 1. CRM & Support Triage
Score inbound support tickets, emails, and lead forms based on information density before an agent sees the record. Automatically trigger follow-up emails for vague, one-line inquiries like "my login is broken," while routing detailed tickets containing error logs and reproduction steps to human agents.
[Salesforce Integration Guide](https://github.com/ezchx/indieml-salesforce-integration)  
[Zendesk Integration Guide](https://github.com/ezchx/indieml-zendesk-integration)

### 2. Real-Time Form & Input Coaching
Prevent low-context submissions before they ever enter your database. IndieML can run inside web forms, bug reporters, and marketplace listings prompting users to add missing details so your team receives actionable data without having to circle back to the user.

### 3. Product Feedback & Review Triage
Separate actionable bug reports and architectural critiques from zero-context "great app" or "it's broken" ratings. IndieML evaluates survey responses and app reviews on submission, routing detailed descriptions of workflow bottlenecks or reproducible bugs directly to Jira, Linear, or Slack while filtering out generic feedback.

### 4. Agent & LLM Context Filtering
Autonomous agents routinely pull noisy web scrapes and bloated tool outputs into their context windows, wasting tokens and degrading accuracy. Sitting inline as a sub-25ms pre-filter, IndieML strips low-substance text segments from the prompt payload before you make an expensive LLM call.

### 5. RAG & Dataset Gatekeeping
Standard RAG pipelines embed entire documents, filling vector databases with navigation menus, boilerplate disclaimers, and shallow stub articles. IndieML scores and filters text before it is submitted to an expensive model to reduce costs and improve data quality.

### 6. Dataset Curation & Stream Filtering
Filter fine-tuning data, scraped web text, or live social streams without paying LLM-as-a-judge compute costs. IndieML evaluates text segments to strip generic filler and low-effort comments—curating high-density JSONL training sets and powering real-time, high-signal feeds.

<!-- mcp-name: io.github.ezchx/indieml -->
