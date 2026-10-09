def extract_pin_performance(pin):
    metrics = pin.get("pin_metrics")

    if not metrics:
        return []

    records = []

    for metric_window, values in metrics.items():
        records.append({
            "pin_id": pin["id"],
            "impressions": values.get("impression", 0),
            "saves": values.get("save", 0),
            "pin_clicks": values.get("pin_click", 0),
            "outbound_clicks": values.get("outbound_click", 0),
            "profile_visits": values.get("profile_visit", 0),
            "user_follows": values.get("user_follow", 0),
            "reactions": values.get("reaction", 0),
            "comments": values.get("comment", 0),
            "metric_window": metric_window,
        })

    return records