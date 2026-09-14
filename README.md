# IndieML MCP Server

An official Model Context Protocol (MCP) server for the [IndieML Substance API](https://indieml.app). 

This server provides AI assistants (like Claude, Cursor, and Gemini CLI) with the `score_substance` tool, allowing them to instantly evaluate the structural information density of text streams, RAG corpora, or social media feeds.

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
        "git+[https://github.com/ezchx/indieml-mcp-server](https://github.com/ezchx/indieml-mcp-server)",
        "mcp",
        "run",
        "server.py"
      ],
      "env": {
        "INDIEML_API_KEY": "your_api_key_here"
      }
    }
  }
}
