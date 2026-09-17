import json
import urllib.request
import urllib.error

class SubstanceAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://indieml.app/v1/score/substance"

    def score(self, text: str) -> dict:
        url = f"{self.base_url}/score"
        
        payload = json.dumps({"text": text}).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        
        try:
            with urllib.request.urlopen(req) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raise Exception(f"Substance API error ({e.code}): {e.read().decode('utf-8')}")
