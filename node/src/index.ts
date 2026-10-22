import { IndieMLOptions, ScoreResponse } from './types.js';

const sleep = (ms: number) => new Promise((resolve) => setTimeout(resolve, ms));

export class IndieML {
  private apiKey: string;
  private baseUrl: string;

  constructor(options: IndieMLOptions = {}) {
    // Falls back to checking environment variables if the user doesn't pass a key directly
    this.apiKey = options.apiKey || process.env.INDIEML_API_KEY || '';
    this.baseUrl = options.baseUrl || 'https://indieml.app/v1';

    if (!this.apiKey) {
      throw new Error(
        'IndieML API key is required. Pass it in options or set the INDIEML_API_KEY environment variable.'
      );
    }
  }

  /**
   * Internal helper to handle HTTP requests and exponential backoff.
   */
  private async _makeRequest(url: string, payloadData: object, maxRetries: number): Promise<any> {
    for (let attempt = 0; attempt <= maxRetries; attempt++) {
      try {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 15000); // 15-second timeout

        const response = await fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-API-KEY': this.apiKey,
          },
          body: JSON.stringify(payloadData),
          signal: controller.signal,
        });

        clearTimeout(timeoutId);

        if (!response.ok) {
          // Fail fast on client errors (Bad Request, Unauthorized, Forbidden, Unprocessable)
          if ([400, 401, 403, 422].includes(response.status)) {
            const errorText = await response.text();
            throw new Error(`IndieML API Error (${response.status}): ${errorText}`);
          }
          
          if (attempt === maxRetries) {
            const errorText = await response.text();
            throw new Error(`IndieML API failed after ${maxRetries} retries (${response.status}): ${errorText}`);
          }
          
          throw new Error(`HTTP ${response.status}`);
        }

        return await response.json();
        
      } catch (error: any) {
        // Bubble up explicitly thrown client errors immediately
        if (error.message.includes('IndieML API Error')) {
          throw error;
        }
        
        if (attempt === maxRetries) {
          throw new Error(`Connection failed after ${maxRetries} retries: ${error.message}`);
        }
        
        // Exponential backoff (1s, 2s, 4s, 8s, 16s, 32s)
        await sleep(Math.pow(2, attempt) * 1000);
      }
    }
  }

  /**
   * Evaluates a single string of text for substance.
   * @param text The input string to score.
   * @param maxRetries Maximum number of times to retry failed network requests.
   */
  async score(text: string, maxRetries: number = 6): Promise<ScoreResponse> {
    const url = `${this.baseUrl}/score/substance`;
    const data = await this._makeRequest(url, { input_text: text }, maxRetries);
    return data.result as ScoreResponse;
  }

  /**
   * Evaluates an array of strings, automatically chunking them into batches of 100.
   * @param texts Array of input strings to score.
   * @param maxRetries Maximum number of times to retry failed network requests.
   */
  async scoreBatch(texts: string[], maxRetries: number = 6): Promise<ScoreResponse[]> {
    const allResults: ScoreResponse[] = [];
    const chunkSize = 100;
    const batchUrl = `${this.baseUrl}/score/substance/batch`;

    for (let i = 0; i < texts.length; i += chunkSize) {
      const chunk = texts.slice(i, i + chunkSize);
      const data = await this._makeRequest(batchUrl, { input_texts: chunk }, maxRetries);
      allResults.push(...data.results);
    }

    return allResults;
  }
}

export * from './types.js';
