def calculate_ctr(impressions: int, clicks: int) -> float:
    if impressions == 0:
        return 0.0

    return (clicks / impressions) * 100


def calculate_save_rate(impressions: int, saves: int) -> float:
    if impressions == 0:
        return 0.0

    return (saves / impressions) * 100


def calculate_engagement_rate(
    impressions: int,
    clicks: int,
    saves: int
) -> float:

    if impressions == 0:
        return 0.0

    engagement = clicks + saves

    return (engagement / impressions) * 100