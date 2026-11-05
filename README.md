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

url = "https://indieml.app/v1/score/substance"
headers = {
    "X-API-KEY": "YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {
    "input_text": "This is a test run."
}
response = requests.post(url, json=payload, headers=headers)

if response.status_code != 200:
    error_data = response.json()
    print(f"HTTP {response.status_code}: {error_data.get('detail')}")
else:
    print(response.json())
```



**Node.js**
```javascript
const response = await fetch('https://indieml.app/v1/score/substance', {
  method: 'POST',
  headers: {
    'X-API-KEY': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    input_text: "This is a test run."
  })
});

if (!response.ok) {
  const errorData = await response.json();
  console.error(`HTTP ${response.status}:`, errorData.detail);
} else {
  const data = await response.json();
  console.log(data);
}
```

### Batch Evaluation
Process up to 100 strings per request.

**cURL**
```bash
curl -X POST https://indieml.app/v1/score/substance/batch \
  -H "X-API-KEY: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input_texts": ["This is a test run.", "This is another test run."]
  }'
```

**Python**
```python
import requests

url = "https://indieml.app/v1/score/substance/batch"
headers = {
    "X-API-KEY": "YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {
    "input_texts": ["This is a test run.", "This is another test run."]
}
response = requests.post(url, json=payload, headers=headers)

if response.status_code != 200:
    error_data = response.json()
    print(f"HTTP {response.status_code}: {error_data.get('detail')}")
else:
    print(response.json())
```

**Node.js**
```javascript
const response = await fetch('https://indieml.app/v1/score/substance/batch', {
  method: 'POST',
  headers: {
    'X-API-KEY': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    input_texts: ["This is a test run.", "This is another test run."]
  })
});

if (!response.ok) {
  const errorData = await response.json();
  console.error(`HTTP ${response.status}:`, errorData.detail);
} else {
  const data = await response.json();
  console.log(data);
}
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

# Single string
single_result = api.score("This is a test run.")
print(single_result)

# Array of strings
batch_result = api.score_batch([
    "This is a test run.", 
    "This is another test run."
])
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
const api = new IndieML({ apiKey: "YOUR_API_KEY_HERE" });

async function run() {
  // Single string
  const singleResult = await api.score("This is a test run.");
  console.log(singleResult);

  // Array of strings
  const batchResult = await api.scoreBatch([
    "This is a test run.",
    "This is another test run."
  ]);
  console.log(batchResult);
}

run().catch(console.error);
```

**Usage (ES Modules / TypeScript)**
```javascript
/**
 * Note: This example uses ES Module syntax and top-level await.
 * To run this file, either:
 * 1. Save the file with an .mjs extension (e.g., example.mjs) OR
 * 2. Add "type": "module" to your project's package.json file.
 */

import { IndieML } from 'indieml';

// Initialize the API
const api = new IndieML({ apiKey: "YOUR_API_KEY_HERE" });

// Single string
const singleResult = await api.score("This is a test run.");
console.log(singleResult);

// Array of strings
const batchResult = await api.scoreBatch([
  "This is a test run.",
  "This is another test run."
]);
console.log(batchResult);
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

The Substance API is a fast and inexpensive pre-screening tool designed to integrate with your existing classification pipeline. It is specifically designed for high-volume, automated data pipelines.

## Machine Facing Applications

### RAG Pipelines & Retrieval
Stop paying tokens for noise. Pre-filter scraped pages and document chunks, dropping menus, boilerplate, and stub text before it reaches your embedding model.\
[LangChain Integration Guide](https://indieml.app/langchain.html)

### Agent Memory Filtering
Keep autonomous agent scratchpads clean. Filter tool outputs and intermediate web crawls so the LLM only retains dense facts, preventing context window bloat.

### Prompt Gating
Reject low-context user prompts (like "fix my code") before triggering expensive LLM inferences, forcing users to provide useful detail first.

### Dataset Curation
Rank and filter large text collections without paying for LLM-as-a-judge. Build fine-tuning sets by keeping high-substance text and dropping filler at scale.

### Web Crawling
Drop SEO filler, navigation menus, and repetitive boilerplate from raw HTML crawls before they enter your data ingestion pipelines.

### Vector Database Pruning
Scan existing vector databases and remove low-substance embeddings to improve search accuracy and reduce cloud storage costs.

## Human Facing Applications

### CRM & Support Tickets
Score support tickets and bug reports before a human opens them. Auto-request missing details from vague one-liners and prioritize actionable messages.\
[Salesforce Integration Guide](https://github.com/ezchx/indieml-salesforce-integration)\
[Zendesk Integration Guide](https://github.com/ezchx/indieml-zendesk-integration)

### User Feedback & Reviews
Separate real signal from "great app" and "it's broken." Score survey responses and route reproducible feedback to Jira, keeping generic noise away from product managers.

### Online Forums & Communities
Surface the most substantive answers in communities and social feeds. Automatically bury reactive, low-effort noise to elevate high-quality, thoughtful discussions.

### Live Input Coaching
Catch thin submissions at the source. Add IndieML to forms and bug reporters to prompt people for what's missing while they're still typing.

### Email & Message Triage
Score inbound lead forms and public-facing email addresses. Flag dense, high-value inquiries for immediate attention while routing empty corporate filler to the archive.

### Form & Application Intake
Score grant proposals, vendor requests, or job applications upon submission to ensure human evaluators only spend time reading substantive, high-effort documents.

<!-- mcp-name: io.github.ezchx/indieml -->
