# IndieML MCP Server

An official Model Context Protocol (MCP) server for the [IndieML Substance API](https://indieml.app). 

Returns a 0.0–1.0 substance score for a short passage of text; higher scores indicate denser, more specific, less filler-heavy language.

## Requirements
* Python 3.10+
* An IndieML API Key

## Usage with Claude Desktop

Add the following to your `claude_desktop_config.json` file. 

*(On Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`)*

```json
{
  "mcpServers": {
    "indieml": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/ezchx/indieml-mcp-server",
        "indieml-mcp-server"
      ],
      "env": {
        "INDIEML_API_KEY": "your_api_key_here"
      }
    }
  }
}
