import os
import httpx
from mcp.server.mcpserver import MCPServer

# Initialize the MCP server
mcp = MCPServer("IndieML Substance Engine")

@mcp.tool()
def score_substance(input_text: str) -> float:
    """
    A lightweight API that evaluates text for substance, depth, and clarity. It approximates LLM judgments to produce a fast Substance score (0.0 to 1.0), which can be used as a signal to filter, rank, or preprocess high-volume text streams.
    """
    api_key = os.getenv("INDIEML_API_KEY")
    if not api_key:
        raise ValueError(
            "INDIEML_API_KEY environment variable is required. "
            "Get a free key at https://indieml.app/"
        )

    # Adjust the header name ("X-API-Key") if your FastAPI verify_api_key depends on a different string like "Authorization"
    headers = {
        "X-API-Key": api_key, 
        "Content-Type": "application/json"
    }
    
    # httpx is used here as it is the standard for modern async-friendly MCP servers
    with httpx.Client() as client:
        response = client.post(
            "https://indieml.app/v1/score/substance",
            headers=headers,
            json={"input_text": input_text},
            timeout=10.0
        )
        response.raise_for_status()
        
        # Extracts the score based on your FastAPI ScoreResponse model
        data = response.json()
        return data["result"]["substance_score"]

def main():
    mcp.run()

if __name__ == "__main__":
    main()
