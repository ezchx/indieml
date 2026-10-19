import os
from .api.substance import SubstanceAPI

class Substance:
    def __init__(self, api_key: str = None):
        # Prioritize an explicitly passed key, fallback to the environment variable
        self.api_key = api_key or os.environ.get("INDIEML_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "API key missing. Initialize with Substance(api_key='...') "
                "or set the INDIEML_API_KEY environment variable."
            )
        
        # Store the internal connection logic privately
        self._client = SubstanceAPI(api_key=self.api_key)
        
    def score(self, text: str):
        return self._client.score(text)
