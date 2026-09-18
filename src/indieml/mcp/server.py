import os
from mcp.server.mcpserver import MCPServer
from indieml.client import IndieMLClient

# Initialize the MCP server
mcp = MCPServer("IndieML Substance Engine")

@mcp.tool()
def score_substance(input_text: str) -> float:
    """
    A lightweight API that evaluates text for substance, depth, and clarity. It approximates LLM judgments to produce a fast Substance score (0.0 to 1.0), which can be used as a signal to process high-volume text streams.
    """
    api_key = os.getenv("INDIEML_API_KEY")
    if not api_key:
        raise ValueError(
            "INDIEML_API_KEY environment variable is required. "
            "Get a free key at https://indieml.app/"
        )

    # Use the Python SDK to handle routing, authentication, and retry logic
    client = IndieMLClient(api_key=api_key)
    data = client.substance.score(input_text)
    
    # Extract the score based on the FastAPI ScoreResponse model
    return data["result"]["substance_score"]

def main():
    mcp.run()

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
