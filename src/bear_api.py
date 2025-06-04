import os
from typing import List, Dict
import requests

class BearAPI:
    """Simple Bear API client."""

    def __init__(self, token: str | None = None) -> None:
        self.token = token or os.environ.get("BEAR_API_TOKEN", "")
        self.base_url = os.environ.get("BEAR_API_URL", "https://api.bear.app")
        self.session = requests.Session()
        if self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def get_notes(self) -> List[Dict]:
        """Retrieve notes from Bear API."""
        url = f"{self.base_url}/notes"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json().get("notes", [])
