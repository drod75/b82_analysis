"""
soda3_client.py

SODA 3 client utility that pulls credentials from environment variables
and flattens multiline queries.
"""

from __future__ import annotations

import os
import re
from typing import Any, Dict, Optional
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def standardize_query(query: str) -> str:
    """
    Cleans and standardizes multiline strings:
    - Strips leading and trailing whitespace
    - Removes trailing semicolons
    - Collapses newlines and multiple spaces into a single space
    """
    if not query:
        return ""
    cleaned = query.strip().rstrip(";")
    return re.sub(r"\s+", " ", cleaned)


class Soda3Client:
    """Client for querying datasets via the SODA 3 API."""

    RESOURCE_ID_REGEX = re.compile(r"([a-z0-9]{4}-[a-z0-9]{4})", re.IGNORECASE)

    def __init__(
        self, dataset_url: str, app_token: Optional[str] = None, timeout: int = 30
    ):
        """
        Initialize the client with a dataset URL.

        :param dataset_url: Web link or API URL to the dataset.
        :param app_token: Optional explicit token; defaults to SOCRATA_APP_TOKEN env variable.
        :param timeout: HTTP request timeout in seconds.
        """
        self.dataset_url = dataset_url
        self.timeout = timeout
        self.app_token = app_token or os.getenv("SOCRATA_APP_TOKEN")
        self.domain, self.resource_id = self._extract_url_components(dataset_url)
        # SODA 3 endpoint format
        self.endpoint = f"https://{self.domain}/api/views/{self.resource_id}/rows.json"

    def _extract_url_components(self, url: str) -> tuple[str, str]:
        """Extracts domain and 4x4 resource identifier from the dataset URL."""
        if not url.startswith(("http://", "https://")):
            url = f"https://{url}"

        parsed = urlparse(url)
        domain = parsed.netloc
        if not domain:
            raise ValueError(f"Invalid domain in URL: {url}")

        match = self.RESOURCE_ID_REGEX.search(parsed.path)
        if not match:
            raise ValueError(f"Could not find a valid 4x4 identifier in URL: {url}")

        return domain, match.group(1).lower()

    def _get_headers(self) -> Dict[str, str]:
        """Build request headers including SODA app token if available."""
        headers = {"Accept": "application/json"}
        if self.app_token:
            headers["X-App-Token"] = self.app_token
        return headers

    def query(self, query_string: str, limit: int = 100) -> Dict[str, Any]:
        """
        Standardizes the query string and executes the request.

        :param query_string: Raw multiline or single-line query string.
        :param limit: Maximum rows to return.
        :return: JSON response payload containing schema, metadata, and rows.
        """
        cleaned_query = standardize_query(query_string)

        # Detect SoQL clauses vs standard search terms
        is_soql = bool(
            re.search(
                r"\b(SELECT|WHERE|GROUP BY|ORDER BY|LIMIT|OFFSET)\b",
                cleaned_query,
                re.IGNORECASE,
            )
        )

        params: Dict[str, Any] = {}
        if is_soql:
            params["$query"] = cleaned_query
        else:
            params["$q"] = cleaned_query
            params["$limit"] = limit

        response = requests.get(
            self.endpoint,
            headers=self._get_headers(),
            params=params,
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response.json()


if __name__ == "__main__":
    load_dotenv()

    dataset = "https://data.cityofnewyork.us/d/erm2-nwe9"

    multiline_query = """
        SELECT * limit 1
    """

    client = Soda3Client(dataset)
    data = client.query(multiline_query)
    print(data)
