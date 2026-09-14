# IndieML MCP Server

An official Model Context Protocol (MCP) server for the [IndieML Substance API](https://indieml.app). 

A lightweight API that evaluates text for substance, depth, and clarity. It approximates LLM judgments to produce a fast Substance score (0.0 to 1.0), which can be used as a high-speed signal to filter, rank, or preprocess high-volume text streams.

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
