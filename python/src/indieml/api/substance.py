import json
import urllib.request
import urllib.error
import time
from typing import List, Dict, Any

class SubstanceAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://indieml.app/v1/score/substance"

    def _make_request(self, url: str, payload_data: dict, max_retries: int) -> dict:
        """Internal helper to handle HTTP requests and exponential backoff."""
        payload = json.dumps(payload_data).encode("utf-8")
        headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json"
        }
        
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

        for attempt in range(max_retries + 1):
            try:
                with urllib.request.urlopen(req, timeout=15.0) as response:
                    return json.loads(response.read().decode("utf-8"))
                    
            except urllib.error.HTTPError as e:
                # Fail fast on client errors (Bad Request, Unauthorized, Forbidden, Unprocessable)
                if e.code in (400, 401, 403, 422):
                    raise Exception(f"Substance API error ({e.code}): {e.read().decode('utf-8')}")
                
                if attempt == max_retries:
                    raise Exception(f"Substance API failed after {max_retries} retries ({e.code}): {e.read().decode('utf-8')}")
                    
            except urllib.error.URLError as e:
                if attempt == max_retries:
                    raise Exception(f"Connection failed after {max_retries} retries: {e.reason}")
            
            # Exponential backoff (1s, 2s, 4s, 8s, 16s, 32s) for server errors/timeouts
            time.sleep(2 ** attempt)

    def score(self, text: str, max_retries: int = 6) -> dict:
        """Evaluate a single string for substance."""
        response_data = self._make_request(self.base_url, {"input_text": text}, max_retries)
        return response_data.get("result", response_data)

    def score_batch(self, texts: List[str], max_retries: int = 6) -> List[Dict[str, Any]]:
        """Evaluate a list of strings, automatically chunking them into blocks of 100."""
        all_results = []
        chunk_size = 100
        batch_url = f"{self.base_url}/batch"
        
        for i in range(0, len(texts), chunk_size):
            chunk = texts[i:i + chunk_size]
            response_data = self._make_request(batch_url, {"input_texts": chunk}, max_retries)
            all_results.extend(response_data.get("results", []))
            
        return all_results
