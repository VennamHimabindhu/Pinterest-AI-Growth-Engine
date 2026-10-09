from src.analytics.sample_data import pins
from src.analytics.metrics import (
    calculate_ctr,
    calculate_save_rate,
    calculate_engagement_rate,
)


for pin in pins:

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

    print("\n----------------------------")

    print(f"Pin: {pin['title']}")
    print(f"Board: {pin['board']}")

    print(f"Impressions: {pin['impressions']}")
    print(f"Clicks: {pin['clicks']}")
    print(f"Saves: {pin['saves']}")

    print(f"CTR: {ctr:.2f}%")
    print(f"Save Rate: {save_rate:.2f}%")
    print(f"Engagement Rate: {engagement_rate:.2f}%")