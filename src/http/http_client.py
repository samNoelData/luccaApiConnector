import requests
import time

class HttpClient:
    """
        Classe `HttpClient` permettant d'effectuer des requêtes HTTP GET vers une API
        Ce client est conçu pour gérer exclusivement la méthode GET dans le cadre du cas pratique
    """
    def __init__(
        self,
        base_url: str,
        headers: dict = None,
        timeout: int = None,
        backoff_seconds: float = 1,
        backoff_retries: int = 5,
        request_rate_limit_delay: float = None,
        defaut_offset: int = None,
        default_limit: int = None
    ):
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout
        self.backoff_seconds = backoff_seconds
        self.backoff_retries = backoff_retries
        self.request_rate_limit_delay = request_rate_limit_delay
        self.defaut_offset = defaut_offset
        self.default_limit = default_limit

    def _get_url(self, endpoint: str):
        return self.base_url + endpoint

    def _retry_handler(self):
        """
            Gère la logique de retry pour les requêtes HTTP
        """
        retries = 0
        def _should_retry(response) -> bool:
            nonlocal retries
            if retries < self.backoff_retries:
                if response.status_code in (500, 502, 503, 504, 408, 429):
                    retries += 1
                    backoff = self.backoff_seconds ** retries
                    print(f"[HttpError - {response.status_code}] Retry {retries}, backoff: {backoff}s")
                    time.sleep(backoff)
                    return True
            return False

        return _should_retry

    def get(self, endpoint: str, params: dict = None) -> dict:
        """
            Méthode get avec gestion des erreurs HTTP.
            Si l'erreur http n'est pas gérable par le retry handler alors on pousse une erreur.
        """
        url = self._get_url(endpoint)
        retry_handler = self._retry_handler()
        while True:
            response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
            if retry_handler(response):
                continue
            break

        response.raise_for_status()
        if self.request_rate_limit_delay:
            time.sleep(self.request_rate_limit_delay)
        try:
            return response.json()
        except Exception:
            raise ValueError(f"Invalid JSON response: {response.text}")
