# IndieML - Substance API

A lightweight, transformer-based API that evaluates text for substance, depth, and clarity in under 25ms while achieving 87% of the accuracy of a full-scale LLM. 

This package provides REST API, Python SDK, and MCP configuration details to natively connect the hosted Substance API to a wide variety of applications.

For more information, including API key requests, please visit https://indieml.app.

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

**Installation**
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

You can natively integrate the Substance API into AI coding assistants by routing them to our cloud-native ASGI endpoints.

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
