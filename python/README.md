# IndieML - Substance API

A lightweight, transformer-based API that evaluates text for substance, depth, and clarity in under 25ms while achieving 87% of the accuracy of a full-scale LLM. 
This package provides REST API, Python SDK, and MCP configuration details to natively connect the hosted Substance API to a wide variety of applications.
For more information, including API key requests, please visit [IndieML](https://indieml.app).

## Python SDK Instructions

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
