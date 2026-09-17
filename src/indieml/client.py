import os
from .api.substance import SubstanceAPI

class IndieMLClient:
    def __init__(self, api_key: str = None):
        # Prioritize an explicitly passed key, fallback to the environment variable
        self.api_key = api_key or os.environ.get("INDIEML_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "API key missing. Initialize with IndieMLClient(api_key='...') "
                "or set the INDIEML_API_KEY environment variable."
            )
        
        # Attach the API module as an attribute so users can call client.substance
        self.substance = SubstanceAPI(api_key=self.api_key)
