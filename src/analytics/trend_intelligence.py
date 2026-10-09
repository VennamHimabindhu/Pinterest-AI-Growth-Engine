from __future__ import annotations

import re
from collections import defaultdict
from typing import Any


def _tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", text.lower())
        if len(token) > 2
    }


def classify_lifecycle(growth: float, history: list[float] | None = None) -> str:
    """
    Internal analytical lifecycle, not an official Pinterest label.
    """
    history = history or []

    if growth <= -20:
        return "DECLINING"
    if growth < 0:
        return "SATURATED"
    if history and len(history) >= 3:
        recent = history[-1]
        previous = history[-2]
        if recent > previous and growth >= 20:
            return "GROWING"
        if recent <= previous and growth >= 0:
            return "PEAK"
    if growth >= 20:
        return "GROWING"
    return "EMERGING"


def normalize_trend(raw: dict[str, Any]) -> dict[str, Any]:
    growth = float(raw.get("pct_growth_wow", raw.get("growth", 0)) or 0)
    history = raw.get("time_series") or []

    return {
        "keyword": raw.get("keyword", "").strip(),
        "region": raw.get("region", "US"),
        "growth": growth,
        "time_series": history,
        "detected_at": raw.get("detected_at"),
        "lifecycle": classify_lifecycle(growth, history),
        "related_boards": raw.get("related_boards", []),
        "related_products": raw.get("related_products", []),
        "confidence": raw.get("confidence", 0.5),
        "source": raw.get("source", "pinterest_trends"),
    }


def detect_emerging_topics(trends: list[dict[str, Any]]) -> list[dict[str, Any]]:
    normalized = [normalize_trend(trend) for trend in trends]

    return [
        trend
        for trend in normalized
        if trend["lifecycle"] in {"EMERGING", "GROWING"}
    ]


def trend_board_fit(keyword: str, board_name: str) -> float:
    trend_words = _tokens(keyword)
    board_words = _tokens(board_name)

    if not trend_words or not board_words:
        return 0.0

    overlap = len(trend_words & board_words)
    return overlap / len(trend_words)


def build_trend_opportunities(
    trends: list[dict[str, Any]],
    boards: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Connect external trend signals to the user's own boards.

    This does not copy Pins. It produces research opportunities.
    """
    opportunities = []

    for raw_trend in trends:
        trend = normalize_trend(raw_trend)

        for board in boards:
            board_name = board.get("board", board.get("name", ""))
            fit = trend_board_fit(trend["keyword"], board_name)

            if fit > 0 or trend["lifecycle"] == "GROWING":
                opportunities.append(
                    {
                        "type": "trend_content_opportunity",
                        "trend": trend["keyword"],
                        "lifecycle": trend["lifecycle"],
                        "growth": trend["growth"],
                        "board": board_name,
                        "board_fit": round(fit, 3),
                        "reason": (
                            f"Trend '{trend['keyword']}' is {trend['lifecycle'].lower()} "
                            f"and may be worth testing on '{board_name}'."
                        ),
                        "source": trend["source"],
                    }
                )

    return sorted(
        opportunities,
        key=lambda item: (item["board_fit"], item["growth"]),
        reverse=True,
    )


def analyze_creative_patterns(evidence: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Convert structured observations about high-performing content into
    reusable creative principles.

    Expected evidence fields may include:
    performance, topic, title_style, image_features, content_features, source.
    """
    pattern_counts: dict[str, int] = defaultdict(int)
    pattern_sources: dict[str, list[str]] = defaultdict(list)

    for item in evidence:
        performance = float(item.get("performance", 0) or 0)
        if performance <= 0:
            continue

        source = item.get("source", "unknown")

        for field in ("title_style", "image_features", "content_features"):
            values = item.get(field, [])
            if isinstance(values, str):
                values = [values]

            for value in values:
                pattern = str(value).strip()
                if pattern:
                    pattern_counts[pattern] += 1
                    pattern_sources[pattern].append(source)

    patterns = []
    for pattern, count in pattern_counts.items():
        patterns.append(
            {
                "observed_pattern": pattern,
                "source_evidence": sorted(set(pattern_sources[pattern])),
                "confidence": min(0.95, 0.50 + (count * 0.10)),
                "derived_creative_principle": (
                    f"Consider testing '{pattern}' when it fits the topic and hypothesis."
                ),
            }
        )

    return sorted(patterns, key=lambda item: item["confidence"], reverse=True)
