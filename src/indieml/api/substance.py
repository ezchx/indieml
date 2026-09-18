import json
import urllib.request
import urllib.error
import time

class SubstanceAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://indieml.app/v1/score/substance"

    def score(self, text: str, max_retries: int = 6) -> dict:
        url = self.base_url
        
        payload = json.dumps({"input_text": text}).encode("utf-8")
        headers = {
            "X-API-KEY": self.api_key,
            "Content-Type": "application/json"
        }
        
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")

        for attempt in range(max_retries + 1):
            try:
                with urllib.request.urlopen(req, timeout=10.0) as response:
                    return json.loads(response.read().decode("utf-8"))
                    
            except urllib.error.HTTPError as e:
                if e.code in (400, 401, 403, 422):
                    raise Exception(f"Substance API error ({e.code}): {e.read().decode('utf-8')}")
                
                if attempt == max_retries:
                    raise Exception(f"Substance API failed after {max_retries} retries ({e.code}): {e.read().decode('utf-8')}")
                    
            except urllib.error.URLError as e:
                if attempt == max_retries:
                    raise Exception(f"Connection failed after {max_retries} retries: {e.reason}")
            
            time.sleep(2 ** attempt)
