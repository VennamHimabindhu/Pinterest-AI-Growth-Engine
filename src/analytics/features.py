def create_features(pin):
    impressions = pin["impressions"]
    pin_clicks = pin["pin_clicks"]
    saves = pin["saves"]

    features = {
        "pin_id": pin["id"],
        "impressions": impressions,
        "pin_clicks": pin_clicks,
        "saves": saves,

        "ctr": pin.get("ctr", 0),
        "save_rate": pin.get("save_rate", 0),
        "engagement_rate": pin.get("engagement_rate", 0),

        "clicks_per_1000_impressions": (
            pin_clicks / impressions * 1000
            if impressions > 0 else 0
        ),

        "saves_per_1000_impressions": (
            saves / impressions * 1000
            if impressions > 0 else 0
        ),
    }

    return features