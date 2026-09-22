import re

import pandas as pd
import requests


class SOQL_Querying:
    def __init__(self, dataset_url: str, app_token: str):
        domain = re.search(r"https?://([^/]+)", dataset_url).group(1)  # type: ignore
        view_id = re.search(r"([a-z0-9]{4}-[a-z0-9]{4})", dataset_url, re.I).group(1)  # type: ignore

        self.endpoint = f"https://{domain}/api/v3/views/{view_id}/query.json"
        self.headers = {"X-App-Token": app_token} if app_token else {}

    def parse_query(self, query_str: str) -> str:
        """Flattens newlines."""
        return " ".join(query_str.split())

    def query(
        self, soql_query: str = "SELECT *", page_number: int = 1, page_size: int = 1000
    ) -> pd.DataFrame:
        clean_query = self.parse_query(soql_query)
        payload = {
            "query": clean_query,
            "page": {"pageNumber": page_number, "pageSize": page_size},
            "includeSynthetic": False,
        }
        response = requests.post(self.endpoint, headers=self.headers, json=payload)
        response.raise_for_status()

        data = response.json()
        records = (
            data.get("data", data.get("rows", data)) if isinstance(data, dict) else data
        )
        return pd.DataFrame(records)
