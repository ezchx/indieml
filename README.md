# IndieML - Substance API

A lightweight, transformer-based API that evaluates text for substance, depth, and clarity in under 25ms while achieving 87% of the accuracy of a full-scale LLM. 

This package provides a Python client and Model Context Protocol (MCP) configuration details for natively connecting AI assistants to the hosted Substance API.

## REST API 

For integrations outside the Python and MCP ecosystems (such as standard OpenAI function calling, custom AI scripts, or raw HTTP requests), the hosted endpoint accepts standard JSON payload requests.

**cURL**
```bash
curl -X POST "[https://indieml.app/v1/score/substance](https://indieml.app/v1/score/substance)" \
  -H "X-API-Key: YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"input_text": "This is a test run."}'
```

**Python (Requests)**
```python
import requests

response = requests.post(
    "[https://indieml.app/v1/score/substance](https://indieml.app/v1/score/substance)",
    headers={"X-API-Key": "YOUR_API_KEY_HERE"},
    json={"input_text": "This is a test run."}
)
print(response.json())
```

**Node.js (Fetch)**
```javascript
const response = await fetch("[https://indieml.app/v1/score/substance](https://indieml.app/v1/score/substance)", {
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

# Initialize the API. Automatically defaults to the INDIEML_API_KEY environment variable.
api = Substance(api_key="your_api_key_here")

# Evaluate text for substance, depth, and clarity
result = api.score("This is a test run.")
print(result)
```

## MCP Server Integration

You can natively integrate the Substance API into modern AI coding assistants by routing them to our cloud-native ASGI endpoints.

# Cursor and ChatGPT (Streamable HTTP)
For agents that support native Streamable HTTP / SSE configurations, provide the remote URL and authorization header directly:
```json
{
  "mcpServers": {
    "indieml": {
      "url": "[https://indieml.app/mcp/](https://indieml.app/mcp/)",
      "headers": {
        "X-API-Key": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

# Claude Desktop (stdio via npx Bridge)
For local clients that require stdio transport, use the npx mcp-remote bridge to seamlessly route the connection to the cloud endpoint. Node.js v20+ is required. Ensure your OS environment variables include INDIEML_API_KEY.
```json
{
  "mcpServers": {
    "indieml": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/mcp-remote",
        "[https://indieml.app/mcp/](https://indieml.app/mcp/)"
      ],
      "env": {
        "INDIEML_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```
