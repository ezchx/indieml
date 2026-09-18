# IndieML - Substance API

A lightweight, transformer-based API that evaluates text for substance, depth, and clarity in under 25ms while achieving 87% of the accuracy of a full-scale LLM. 

This package provides a Python client and Model Context Protocol (MCP) server for the Substance API.

## Python SDK

**Installation**
```bash
pip install indieml
```

**Quickstart**
```python
from indieml import IndieMLClient

# Initialize the client
client = IndieMLClient(api_key="your_api_key_here")

# Score text using the Substance API
result = client.substance.score("This is a test run.")
print(result)
```

## MCP Server Integration

The `indieml` package includes a built-in MCP server, allowing AI coding assistants (like Claude Desktop, Cursor, and Zed) to natively access the Substance API.

To configure your AI assistant, add the following to your MCP configuration file. Using `uvx` ensures the server runs in an isolated environment with all necessary dependencies:

```json
{
  "mcpServers": {
    "indieml": {
      "command": "uvx",
      "args": ["indieml"],
      "env": {
        "INDIEML_API_KEY": "your_api_key"
      }
    }
  }
}
```
## REST API (Non-Python Environments)

For integrations outside the Python and MCP ecosystems (such as standard OpenAI function calling, custom AI scripts, or raw HTTP requests), IndieML provides a standard REST API.

View the full cURL documentation and REST implementation guide at [indieml.app](https://indieml.app).
