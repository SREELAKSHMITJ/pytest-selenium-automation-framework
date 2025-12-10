import requests

DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}


class APIClient:
    """
    Simple reusable API client for GET, POST, PUT, DELETE.
    """

    def __init__(self, base_url: str, headers: dict | None = None):
        self.base_url = base_url.rstrip("/")
        # merge default headers + custom headers (if any)
        self.headers = DEFAULT_HEADERS.copy()
        if headers:
            self.headers.update(headers)

    def _build_url(self, endpoint: str) -> str:
        if not endpoint.startswith("/"):
            endpoint = "/" + endpoint
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint: str, params: dict | None = None):
        url = self._build_url(endpoint)
        return requests.get(url, params=params, headers=self.headers)

    def post(self, endpoint: str, payload: dict | None = None):
        url = self._build_url(endpoint)
        return requests.post(url, json=payload, headers=self.headers)

    def put(self, endpoint: str, payload: dict | None = None):
        url = self._build_url(endpoint)
        return requests.put(url, json=payload, headers=self.headers)

    def delete(self, endpoint: str):
        url = self._build_url(endpoint)
        return requests.delete(url, headers=self.headers)