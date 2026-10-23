# IndieML - Substance API

A lightweight, transformer-based API that evaluates text for substance, depth, and clarity in under 25ms while achieving 87% of the accuracy of a full-scale LLM. 
This package provides REST API, Python SDK, and MCP configuration details to natively connect the hosted Substance API to a wide variety of applications.
For more information, including API key requests, please visit [IndieML](https://indieml.app).

## REST API 

For integrations outside the Python and MCP ecosystems (such as standard OpenAI function calling, custom AI scripts, or raw HTTP requests), the hosted endpoint accepts standard JSON payload requests.

### Single Evaluation

**cURL**
```bash
curl -X POST https://indieml.app/v1/score/substance \
  -H "X-API-Key: YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"input_text": "This is a test run."}'
```

**Python**
```python
import requests

response = requests.post(
    "https://indieml.app/v1/score/substance",
    headers={"X-API-Key": "YOUR_API_KEY_HERE"},
    json={"input_text": "This is a test run."}
)
print(response.json())
```

**Python**
```python
import requests

url = "https://indieml.app/v1/score/substance"
headers = {
    "X-API-KEY": "YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {
    "input_text": "This is a test run."
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```



**Node.js**
```javascript
const response = await fetch("https://indieml.app/v1/score/substance", {
  method: "POST",
  headers: {
    "X-API-Key": "YOUR_API_KEY_HERE",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ input_text: "This is a test run." })
});
console.log(await response.json());
```

### Batch Evaluation
Process up to 100 strings per request.

**cURL**
```bash
curl -X POST https://indieml.app/v1/score/substance/batch \
  -H "X-API-Key: YOUR_API_KEY_HERE" \
  -H "Content-Type: application/json" \
  -d '{"input_texts": ["This is a test run.", "This is another test run."]}'
```

**Python**
```python
import requests

response = requests.post(
    "https://indieml.app/v1/score/substance/batch",
    headers={"X-API-Key": "YOUR_API_KEY_HERE"},
    json={"input_texts": ["This is a test run.", "This is another test run."]}
)
print(response.json())
```

**Node.js**
```javascript
const response = await fetch("https://indieml.app/v1/score/substance/batch", {
  method: "POST",
  headers: {
    "X-API-Key": "YOUR_API_KEY_HERE",
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ input_texts: ["This is a test run.", "This is another test run."] })
});
console.log(await response.json());
```

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

# Evaluate a single string
single_result = api.score("This is a test run.")
print(single_result)

# Evaluate an array of strings (automatically chunks into batches of 100)
batch_result = api.score_batch(["This is a test run.", "This is another test run."])
print(batch_result)
```

## Node SDK

**Installation**
```bash
npm install indieml
```

**Usage (CommonJS)**
```javascript

const { IndieML } = require('indieml');

// Initialize the API
const api = new IndieML({ apiKey: 'YOUR_API_KEY_HERE' });

// Evaluate a single string
const singleResult = await api.score("This is a test run.");
console.log(singleResult);

// Evaluate an array of strings (automatically chunks into batches of 100)
const batchResult = await api.scoreBatch(["This is a test run.", "This is another test run."])
console.log(batchResult)
```

**Usage (ES Modules / TypeScript)**
```javascript

import { IndieML } from 'indieml';

// Initialize the API
const api = new IndieML({ apiKey: 'YOUR_API_KEY_HERE' });

// Evaluate a single string
const singleResult = await api.score("This is a test run.");
console.log(singleResult);

// Evaluate an array of strings (automatically chunks into batches of 100)
const batchResult = await api.scoreBatch(["This is a test run.", "This is another test run."])
console.log(batchResult)
```




## MCP Server Integration

You can integrate the Substance API into AI coding assistants by routing them to our cloud-native ASGI endpoints.

### Cursor, ChatGPT, and Claude Code (Streamable HTTP)
For agents that support native Streamable HTTP / SSE configurations, provide the remote URL and authorization header directly:
```json
{
  "mcpServers": {
    "indieml": {
      "type": "http",
      "url": "https://indieml.app/mcp/",
      "headers": {
        "X-API-Key": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### Claude Desktop (stdio via npx Bridge)
For local Linux, Mac, and Windows clients that require stdio transport, use the npx mcp-remote bridge to route the connection to the cloud endpoint. Node.js v20+ is required. Ensure your OS environment variables include INDIEML_API_KEY.
```json
{
  "mcpServers": {
    "indieml": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://indieml.app/mcp/",
        "--header",
        "X-Api-Key:${INDIEML_API_KEY}"
      ],
      "env": {
        "INDIEML_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

## Applications & Use Cases

The Substance API is a fast and inexpensive pre-screening tool designed to integrate with your existing filters.

While it evaluates substance across any text, it is uniquely suited for high-volume, automated data pipelines:

### Inbox & Intake Triage
Score support tickets, shared mailboxes, lead forms, and bug reports before a human opens them. Auto-request missing details from vague one-liners and put detailed, actionable messages first. Works as an API call, a mail header, or a label in the tools you already use.\
[Salesforce Integration Guide](https://github.com/ezchx/indieml-salesforce-integration)  
[Zendesk Integration Guide](https://github.com/ezchx/indieml-zendesk-integration)

### Live Input Coaching
Catch thin submissions at the source. Add IndieML to forms, listings, and bug reporters to prompt people for what's missing while they're still typing. Your team gets complete, usable input the first time, without chasing follow-ups.

### Feedback & Review Triage
Separate real signal from "great app" and "it's broken." Score survey responses, NPS comments, and app reviews as they arrive, then route detailed, reproducible feedback to Jira, Linear, or Slack and keep generic noise out of the way.

### LLM Context & RAG Filtering
Stop paying tokens for noise. Pre-filter scraped pages, tool outputs, and document chunks, dropping menus, boilerplate, and stub text before it reaches your embedding model or prompt. Lower cost, faster calls, better answers.

### Dataset Curation
Rank and filter large text collections without paying for LLM-as-a-judge. Build fine-tuning sets, clean scraped corpora, and assemble eval sets by keeping high-substance text and dropping filler, in batch and at scale.

### Content & Output Quality
Surface the most substantive answers, comments, and reviews in communities and feeds, or monitor chatbot and agent responses for fluff in CI and production. One consistent score for any text where depth matters.

<!-- mcp-name: io.github.ezchx/indieml -->
