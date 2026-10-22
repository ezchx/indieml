export interface IndieMLOptions {
  /** Your IndieML API key. Defaults to process.env.INDIEML_API_KEY */
  apiKey?: string;
  /** Optional: Override the default API base URL */
  baseUrl?: string;
}

export interface ScoreResponse {
  /** The text that was evaluated */
  text: string;
  /** The calculated substance score between 0.0 and 1.0 */
  substance_score: number;
}
