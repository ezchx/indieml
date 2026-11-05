# IndieML - Substance API

A lightweight, transformer-based API that evaluates text for substance, depth, and clarity in under 25ms while achieving 87% of the accuracy of a full-scale LLM. 
This package provides REST API, Python SDK, and MCP configuration details to natively connect the hosted Substance API to a wide variety of applications.
For more information, including API key requests, please visit [IndieML](https://indieml.app).

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

<!-- mcp-name: io.github.ezchx/indieml -->

