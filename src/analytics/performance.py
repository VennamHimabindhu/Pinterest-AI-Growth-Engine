from src.analytics.metrics import (
    calculate_ctr,
    calculate_save_rate,
    calculate_engagement_rate,
)


def analyze_pin(pin):

    ctr = calculate_ctr(
        pin["impressions"],
        pin["clicks"]
    )

    save_rate = calculate_save_rate(
        pin["impressions"],
        pin["saves"]
    )

    engagement_rate = calculate_engagement_rate(
        pin["impressions"],
        pin["clicks"],
        pin["saves"]
    )

    if engagement_rate >= 6:
        performance = "high"

    elif engagement_rate >= 3:
        performance = "medium"

    else:
        performance = "low"

    return {
        **pin,
        "ctr": ctr,
        "save_rate": save_rate,
        "engagement_rate": engagement_rate,
        "performance": performance,
    }