from collections import defaultdict

from src.analytics.metrics import (
    calculate_ctr,
    calculate_save_rate,
    calculate_engagement_rate,
)


def analyze_boards(pins):

    boards = defaultdict(
        lambda: {
            "impressions": 0,
            "clicks": 0,
            "saves": 0,
            "pin_count": 0,
        }
    )

    # Group Pins by board
    for pin in pins:

        board = pin["board"]

        boards[board]["impressions"] += pin["impressions"]
        boards[board]["clicks"] += pin["clicks"]
        boards[board]["saves"] += pin["saves"]
        boards[board]["pin_count"] += 1

    # Calculate board-level metrics
    results = []

    for board, data in boards.items():

        ctr = calculate_ctr(
            data["impressions"],
            data["clicks"]
        )

        save_rate = calculate_save_rate(
            data["impressions"],
            data["saves"]
        )

        engagement_rate = calculate_engagement_rate(
            data["impressions"],
            data["clicks"],
            data["saves"]
        )

        results.append({
            "board": board,
            "pin_count": data["pin_count"],
            "impressions": data["impressions"],
            "clicks": data["clicks"],
            "saves": data["saves"],
            "ctr": ctr,
            "save_rate": save_rate,
            "engagement_rate": engagement_rate,
        })

    return results