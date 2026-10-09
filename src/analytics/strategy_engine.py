from __future__ import annotations

from typing import Any


def choose_mode(
    trend_lifecycle: str | None,
    account_signal: str | None,
) -> str:
    """
    Deterministic exploration/exploitation decision.

    EXPLOIT = use proven account patterns.
    EXPLORE = investigate a new/emerging external signal.
    """
    if trend_lifecycle in {"EMERGING", "GROWING"}:
        return "explore"
    if account_signal == "winner":
        return "exploit"
    return "explore"


def build_strategy_decisions(
    pins: list[dict[str, Any]],
    trend_opportunities: list[dict[str, Any]],
    creative_patterns: list[dict[str, Any]] | None = None,
    max_decisions: int = 5,
) -> list[dict[str, Any]]:
    creative_patterns = creative_patterns or []

    winner_pins = [
        pin for pin in pins if pin.get("classification") == "winner"
    ]

    decisions = []

    # Exploration: external trend + account/board context.
    for opportunity in trend_opportunities:
        mode = choose_mode(
            opportunity.get("lifecycle"),
            "winner" if winner_pins else None,
        )

        decisions.append(
            {
                "objective": "discover_new_opportunity",
                "mode": mode,
                "trend": opportunity["trend"],
                "recommended_board": opportunity["board"],
                "hypothesis": (
                    f"An original Pin using the '{opportunity['trend']}' trend "
                    f"and a suitable creative pattern may create a new performance signal."
                ),
                "evidence": [
                    f"Trend lifecycle: {opportunity['lifecycle']}",
                    f"Trend growth: {opportunity['growth']}%",
                    f"Board: {opportunity['board']}",
                    f"Board fit: {opportunity['board_fit']}",
                ],
                "creative_principles": [
                    pattern["derived_creative_principle"]
                    for pattern in creative_patterns[:3]
                ],
                "action": "create_original_trend_experiment",
                "confidence": round(
                    min(
                        0.95,
                        0.40
                        + (max(opportunity["growth"], 0) / 200)
                        + (opportunity["board_fit"] * 0.20),
                    ),
                    3,
                ),
            }
        )

    # Exploitation: protect strong patterns but create variations.
    for pin in winner_pins[:max_decisions]:
        decisions.append(
            {
                "objective": "improve_existing_winner",
                "mode": "exploit",
                "trend": None,
                "recommended_board": pin.get("board"),
                "hypothesis": (
                    "A controlled creative variation of this winning pattern "
                    "may outperform the current champion."
                ),
                "evidence": [
                    f"Pin {pin['id']} is classified as a winner.",
                    f"Score: {pin.get('score', 0):.3f}",
                    f"CTR: {pin.get('ctr', 0):.2f}%",
                    f"Engagement: {pin.get('engagement_rate', 0):.2f}%",
                ],
                "creative_principles": [
                    pattern["derived_creative_principle"]
                    for pattern in creative_patterns[:3]
                ],
                "action": "create_challenger_variation",
                "confidence": 0.80,
            }
        )

    return decisions[:max_decisions]
