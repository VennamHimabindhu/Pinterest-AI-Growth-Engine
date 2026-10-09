from src.analytics.metrics import (
    calculate_ctr,
    calculate_save_rate,
    calculate_engagement_rate,
)


impressions = 12000
clicks = 180
saves = 430


ctr = calculate_ctr(impressions, clicks)
save_rate = calculate_save_rate(impressions, saves)
engagement_rate = calculate_engagement_rate(
    impressions,
    clicks,
    saves
)


print(f"CTR: {ctr:.2f}%")
print(f"Save rate: {save_rate:.2f}%")
print(f"Engagement rate: {engagement_rate:.2f}%")