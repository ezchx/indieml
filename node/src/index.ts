import { IndieMLOptions, ScoreResponse } from './types.js';

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
   * Evaluates a single string of text for substance, depth, and clarity.
   * @param text The input string to score.
   */
  async score(text: string): Promise<ScoreResponse> {
    const response = await fetch(`${this.baseUrl}/score/substance`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-KEY': this.apiKey,
      },
      body: JSON.stringify({ input_text: text }),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`IndieML API Error (${response.status}): ${errorText}`);
    }

    const data = await response.json();
    return data.result as ScoreResponse;
  }
}

// Export the types so developers can use them in their own code
export * from './types.js';
