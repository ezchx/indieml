## Python SDK

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
