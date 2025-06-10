from ..http.http_client import HttpClient

class LuccaClient(HttpClient):
    """
        Classe `LuccaClient` permettant d'effectuer les appels GET vers l'API lucca.
        L'API lucca permet de gérer 50 appels/min --> request_rate_limit_delay = 1.2s
    """
    def __init__(
        self,
        host: str,
        api_key: str,
        request_rate_limit_delay: float = 1.2,
        defaut_offset: int = 0,
        default_limit: int = 1000
    ):
        super().__init__(
            base_url=f"https://{host}",
            headers={
                "Authorization": f"lucca application={api_key}",
                "Accept": "application/json",
            },
            request_rate_limit_delay=request_rate_limit_delay,
            defaut_offset=defaut_offset,
            default_limit=default_limit
        )

    @staticmethod
    def _define_api_version(endpoint: str) -> int:
        """
            Détermine la version de l'API en fonction de l'enpoint donné (3 ou 4)
        """
        if "/api/v3/" in endpoint:
            return 3
        return 4

    def _get_parameters_limit(self, params: dict) -> int:
        """
            Récupère le champ limit dans le dict params de l'appel http en fonction de la version de l'API
        """
        if params.get("paging"):
            try:
                return int(params.get("paging").split(",")[1])
            except Exception as e:
                print(f"[ParamWarning] - invalid Paging, use default instead {self.default_limit}. {e}")
                return self.default_limit
        elif params.get("limit"):
            try:
                return int(params.get("limit"))
            except Exception as e:
                print(f"[ParamWarning] - invalid limit, use default instead {self.default_limit}. {e}")
                return self.default_limit
        else:
            return self.default_limit

    def get_itemless_data(self, endpoint: str, params: dict = None) -> dict:
        """
            Récupère les données pour les endpoints qui ne disposent pas d'items.
            Exemple : "/api/v3/departments/tree"
        """
        try:
            api_version = self._define_api_version(endpoint)
            response = self.get(endpoint, params)
            if api_version == 3:
                return response.get("data", {})
            return response
        except Exception as e:
            print(f"Failed to fetch data from '{endpoint}': {e}")
            return {}

    def get_all_paginated_items(self, endpoint: str, params: dict = None):
        """
            Récupère l'ensemble des items pour l'endpoint donné.
        """
        all_items = []
        parameters = params or {}
        page = 0
        limit = self._get_parameters_limit(parameters)
        api_version = self._define_api_version(endpoint)
        try:
            while True:
                print(f"Processing page {page + 1} for {endpoint} using limit={limit}")
                if api_version == 3:
                    parameters["paging"] = f"{page * limit},{limit}"
                else:
                    parameters["page"] = page + 1
                    parameters["limit"] = limit

                response = self.get(endpoint, parameters)

                if api_version == 3:
                    items = response.get("data", {}).get("items", [])
                else:
                    items = response.get("items", [])

                if not items:
                    break

                all_items.extend(items)
                page += 1
            return all_items
        except Exception as e:
            print(f"Failed to fetch items for endpoint {endpoint}: {e}")
            return []