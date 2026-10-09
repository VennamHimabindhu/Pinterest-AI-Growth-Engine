from src.database.connection import get_connection

from src.analytics.features import create_features
def get_lifetime_performance():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    pin_id,
                    impressions,
                    saves,
                    pin_clicks,
                    outbound_clicks,
                    profile_visits,
                    user_follows,
                    reactions,
                    comments,
                    recorded_at
                FROM pin_performance
                WHERE metric_window = 'lifetime_metrics'
                ORDER BY recorded_at;
                """
            )

            rows = cursor.fetchall()

            return [
                {
                    "pin_id": row[0],
                    "impressions": row[1],
                    "saves": row[2],
                    "pin_clicks": row[3],
                    "outbound_clicks": row[4],
                    "profile_visits": row[5],
                    "user_follows": row[6],
                    "reactions": row[7],
                    "comments": row[8],
                    "recorded_at": row[9],
                }
                for row in rows
            ]

    finally:
        connection.close()


def calculate_metrics(record):
    impressions = record["impressions"]

    if impressions == 0:
        return {
            **record,
            "ctr": 0.0,
            "save_rate": 0.0,
            "outbound_ctr": 0.0,
            "engagement_rate": 0.0,
        }

    ctr = (record["pin_clicks"] / impressions) * 100
    save_rate = (record["saves"] / impressions) * 100
    outbound_ctr = (record["outbound_clicks"] / impressions) * 100

    engagement_rate = (
        (
            record["pin_clicks"]
            + record["saves"]
            + record["outbound_clicks"]
            + record["reactions"]
            + record["comments"]
        )
        / impressions
    ) * 100

    return {
        **record,
        "ctr": ctr,
        "save_rate": save_rate,
        "outbound_ctr": outbound_ctr,
        "engagement_rate": engagement_rate,
    }
def get_pins_for_analytics():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    p.id,
                    p.title,
                    p.board_id,
                    pp.impressions,
                    pp.pin_clicks,
                    pp.saves,
                    pp.outbound_clicks,
                    pp.profile_visits,
                    pp.user_follows,
                    pp.reactions,
                    pp.comments
                FROM pins p
                JOIN pin_performance pp
                    ON p.id = pp.pin_id
                WHERE pp.metric_window = 'lifetime_metrics'
                ORDER BY pp.recorded_at;
                """
            )

            rows = cursor.fetchall()

            pins = []

            for row in rows:
                pin = {
                     "id": row[0],
                    "title": row[1],
                    "board": row[2],
                    "impressions": row[3] or 0,
                    "pin_clicks": row[4] or 0,
                    "clicks": row[4] or 0,
                    "saves": row[5] or 0,
                    "outbound_clicks": row[6] or 0,
                    "profile_visits": row[7] or 0,
                    "user_follows": row[8] or 0,
                    "reactions": row[9] or 0,
                    "comments": row[10] or 0,
                }

                pins.append(calculate_metrics(pin))

            return pins

    finally:
        connection.close()

if __name__ == "__main__":
    records = get_lifetime_performance()

    print(f"Found {len(records)} lifetime records.")

    for record in records:
        metrics = calculate_metrics(record)
        features = create_features(metrics)

        print(
            f"{features['pin_id']} | "
            f"CTR: {features['ctr']:.2f}% | "
            f"Save Rate: {features['save_rate']:.2f}% | "
            f"Clicks/1000: {features['clicks_per_1000_impressions']:.2f} | "
            f"Saves/1000: {features['saves_per_1000_impressions']:.2f}"
        )