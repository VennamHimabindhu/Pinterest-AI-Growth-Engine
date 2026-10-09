from __future__ import annotations

import os
from abc import ABC, abstractmethod
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()


class TrendProvider(ABC):
    """Provider interface so Pinterest Trends can be swapped or mocked."""

    @abstractmethod
    def get_trending_keywords(
        self,
        region: str = "US",
        trend_type: str = "growing",
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        raise NotImplementedError


class PinterestTrendsAPIProvider(TrendProvider):
    """
    Uses the currently documented Pinterest Trends keyword endpoint.

    This does NOT claim to expose the entire public trends.pinterest.com
    experience. The current API is limited to the supported Trends API data.
    """

    BASE_URL = "https://api.pinterest.com/v5"

    def __init__(self, access_token: str | None = None):
        self.access_token = access_token or os.getenv("PINTEREST_ACCESS_TOKEN")
        if not self.access_token:
            raise ValueError("PINTEREST_ACCESS_TOKEN is required.")

    def get_trending_keywords(
        self,
        region: str = "US",
        trend_type: str = "growing",
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        limit = max(1, min(limit, 50))

        url = f"{self.BASE_URL}/trends/keywords/{region}/top/{trend_type}"
        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json",
            },
            params={"limit": limit},
            timeout=30,
        )
        response.raise_for_status()

        data = response.json()
        return data.get("trends", data.get("items", []))


class MockTrendProvider(TrendProvider):
    """Clearly labeled development data. Never treat it as live Pinterest data."""

    def __init__(self, trends: list[dict[str, Any]] | None = None):
        self.trends = trends or [
            {
                "keyword": "minimalist skincare",
                "trend_type": "growing",
                "region": "US",
                "pct_growth_wow": 42,
                "source": "development_mock",
            },
            {
                "keyword": "morning skincare routine",
                "trend_type": "growing",
                "region": "US",
                "pct_growth_wow": 28,
                "source": "development_mock",
            },
        ]

    def get_trending_keywords(
        self,
        region: str = "US",
        trend_type: str = "growing",
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        return [
            trend
            for trend in self.trends
            if trend.get("region", region) == region
            and trend.get("trend_type", trend_type) == trend_type
        ][:limit]
