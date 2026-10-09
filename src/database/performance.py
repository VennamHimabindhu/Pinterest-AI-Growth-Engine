from src.database.connection import get_connection
def save_performance_batch(records):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            for record in records:
                cursor.execute(
                    """
                    INSERT INTO pin_performance (
                        pin_id,
                        impressions,
                        saves,
                        pin_clicks,
                        outbound_clicks,
                        profile_visits,
                        user_follows,
                        reactions,
                        comments,
                        metric_window
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

                    ON CONFLICT (pin_id, metric_window)
                    DO UPDATE SET
                        impressions = EXCLUDED.impressions,
                        saves = EXCLUDED.saves,
                        pin_clicks = EXCLUDED.pin_clicks,
                        outbound_clicks = EXCLUDED.outbound_clicks,
                        profile_visits = EXCLUDED.profile_visits,
                        user_follows = EXCLUDED.user_follows,
                        reactions = EXCLUDED.reactions,
                        comments = EXCLUDED.comments,
                        recorded_at = CURRENT_TIMESTAMP;
                    """,
                    (
                        record["pin_id"],
                        record["impressions"],
                        record["saves"],
                        record["pin_clicks"],
                        record["outbound_clicks"],
                        record["profile_visits"],
                        record["user_follows"],
                        record["reactions"],
                        record["comments"],
                        record.get("metric_window", "lifetime"),
                    ),
                )

        connection.commit()

    finally:
        connection.close()