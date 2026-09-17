# IndieML

A Python client and Model Context Protocol (MCP) server for the Substance API. 

## Python SDK

**Installation**
```bash
pip install indieml
```

## Quickstart

from indieml import IndieMLClient

# Initialize the client
client = IndieMLClient(api_key="your_api_key_here")

# Score text using the Substance API
result = client.substance.score("This is a test run.")
print(result)
